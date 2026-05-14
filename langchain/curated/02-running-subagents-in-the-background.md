# 在后台运行子代理 (Running Subagents in the Background)

**作者:** Hunter Lovell, Colin Francis  
**来源:** [LangChain Blog](https://www.langchain.com/blog/running-subagents-in-the-background)  
**日期:** 2026 年 4 月 16 日  
**阅读时间:** 约 4 分钟

---

> **一句话总结:** 传统的同步子代理 (Subagent) 会阻塞主代理的思考能力，异步子代理 (Async Subagent) 让任务在后台并行运行，主代理随时可以继续工作和响应用户——从"发射后等待"变为"发射后操控"。

## 核心要点

- **同步子代理的致命缺陷：** 主代理在等待子代理返回结果时完全"死锁"，无法处理任何新请求
- **异步子代理的核心思想：** 启动任务后立即获得任务 ID，主代理继续工作，随时可查询/更新/取消任务
- **五个任务管理工具** 构成了完整的异步生命周期：启动、查询、更新、取消、列举
- **基于 Agent Protocol 标准：** 框架无关的 API 规范，支持托管部署或自建部署

---

## 传统子代理在哪里失灵了？

子代理 (Subagent) 是指主管代理 (Supervisor) 将特定范围的工作委派给的下级代理。这个模式本身没问题，但当任务变得更长、更复杂时，**同步调用**的子代理开始暴露出严重问题。

### 问题一：主代理被"死锁"

> **类比：** 想象你是一个经理，派员工去出差调研。同步模式下，你站在办公室门口一动不动地等他回来——不接电话、不开会、不处理任何事。员工出差一小时，你就呆站一小时。

在 Agent 的工具调用 (Tool Call) 机制中，主代理必须等待子代理返回结果后才能继续推理。如果子代理需要一个小时才能完成，主代理就被阻塞一个小时，期间用户无法与之交互。

### 问题二：新信息难以协调

同步子代理带来三个协作障碍：

| 障碍 | 说明 |
|------|------|
| 用户被隔离 | 主代理阻塞期间，用户无法与之对话 |
| 无法并行 | 多个子代理不能同时运行，结果无法交叉参考 |
| 全有或全无 | 子代理要么全部完成，要么什么都不返回——没有中间状态更新 |

### 为什么重要

> 随着 Agent 承担的任务越来越复杂（深度研究、多步骤规划、跨系统协调），同步阻塞不仅仅是"慢"的问题——它从根本上限制了 Agent 系统的并发能力和用户体验。

---

## 异步子代理：后台运行的子代理

一句话理解异步子代理：**在后台运行的子代理，而不是串行阻塞的子代理。**

> **类比：** 还是那个经理的例子。异步模式下，你派员工出差后立刻拿到一个"任务追踪单号"，然后继续处理其他工作。你可以随时查看出差进度、发送新指示、甚至取消出差。这就是"发射后操控" (fire-and-steer)，而不是"发射后遗忘" (fire-and-forget)。

### 架构对比

```
同步模式 (Inline Subagent):
┌──────────┐     ┌──────────┐
│ Supervisor│────▶│ Subagent │
│  (阻塞)   │◀────│ (执行中)  │
└──────────┘     └──────────┘
     ⏳ 主代理完全停止，等待返回

异步模式 (Async Subagent):
┌──────────┐  启动   ┌──────────┐
│ Supervisor│──────▶│ Subagent │
│ (继续工作) │  返回ID │ (后台执行) │
└─────┬────┘◀──────└──────────┘
      │
      ├── 响应用户新消息
      ├── 启动更多子代理
      ├── 随时查询/更新任务
      └── 汇总所有结果
```

---

## 任务管理工具集

异步子代理通过五个工具实现完整的任务生命周期管理：

| 工具 | 用途 | 类比 |
|------|------|------|
| `start_async_task` | 在远程代理上启动任务，**立即返回**任务 ID | 派出快递并拿到快递单号 |
| `check_async_task` | 轮询任务状态，完成后获取结果 | 查询快递物流信息 |
| `update_async_task` | 向运行中的任务发送后续指令 | 联系快递员修改送货地址 |
| `cancel_async_task` | 取消运行中的任务 | 取消快递订单 |
| `list_async_tasks` | 列出所有被追踪任务及其当前状态 | 查看所有在途快递 |

### 任务生命周期

```
start_async_task ──▶ [运行中] ──▶ check_async_task ──▶ [已完成] ──▶ 获取结果
                        │
                        ├── update_async_task (发送新指令)
                        └── cancel_async_task (取消任务)

随时可调用: list_async_tasks (查看全局状态)
```

---

## 基于 Agent Protocol 构建

> Agent Protocol 是一个**框架无关的 API 规范**，用于管理远程代理。它定义了创建线程 (Thread)、启动运行 (Run)、轮询状态、发送更新和管理长期记忆的标准端点 (Endpoint)。

### 为什么重要

选择 Agent Protocol 作为底层意味着：
- **不绑定特定框架** —— 用 LangChain、LlamaIndex 还是自研框架都能对接
- **部署灵活** —— 使用 LangSmith 托管服务，或在自有基础设施上自建
- **标准化互操作** —— 不同团队、不同语言实现的 Agent 可以通过统一协议协作

---

## 代码示例

### 托管部署 (Managed Deployment)

```typescript
// agents.ts
import { createAgent } from "langchain";
import { createDeepAgent } from "deepagents";

// 创建一个研究员子代理：负责深度搜索和信息收集
export const researcher = createAgent({
  model: "anthropic:claude-sonnet-4-6",
  instructions: "Perform deep research on the given topic.",
  tools: [searchWeb, readUrl],  // 配备网页搜索和 URL 阅读工具
});

// 创建主管代理 (Deep Agent)：可以异步调度研究员子代理
export const agent = createDeepAgent({
  model: "anthropic:claude-opus-4-6",
  subagents: [{
    name: "researcher",                         // 子代理名称
    description: "Performs deep research on a topic.",  // 描述，帮助主管决定何时调用
    graphId: "researcher",                       // 关联到上面定义的 researcher
  }],
});
```

### 自建部署 (Self-hosted)

```typescript
export const agent = createDeepAgent({
  model: "anthropic:claude-opus-4-6",
  subagents: [{
    name: "researcher",
    description: "Performs deep research on a topic.",
    graphId: "researcher",
    url: "http://localhost:2024",  // 指向自建服务器，实现 Agent Protocol 端点
  }],
});
// 自建服务器可以部署在任何地方：Docker 容器、虚拟机、Kubernetes 集群
```

---

## 延伸思考

1. **任务协调复杂度：** 当多个异步子代理的结果之间存在依赖关系时（例如子代理 B 需要子代理 A 的输出），主管代理如何高效地编排执行顺序？
2. **错误处理与重试：** 异步任务失败后，主管代理应该自动重试、换一个子代理执行、还是上报给用户？不同策略的权衡是什么？
3. **状态一致性：** 如果主管代理在子代理运行途中崩溃重启，如何恢复对所有进行中任务的追踪？这对持久化存储提出了什么要求？
4. **资源控制：** 如果主管代理不受限地启动大量异步子代理，如何避免资源耗尽？是否需要并发上限或优先级队列？

---

**扩展阅读:** [Async Subagents 官方文档](https://docs.langchain.com/oss/javascript/deepagents/async-subagents)
