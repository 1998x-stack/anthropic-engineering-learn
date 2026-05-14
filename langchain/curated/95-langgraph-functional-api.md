# 95 | LangGraph Functional API：用普通 Python 函数构建 AI 工作流

> 原文: Introducing the LangGraph Functional API (LangChain Blog)

## 一句话总结

LangGraph 推出 Functional API，让你用 `@entrypoint` 和 `@task` 两个装饰器就能构建带持久化、人工审批、流式输出的 AI 工作流，不再需要手动定义图结构。

---

## 核心要点

### 1. 两个原语搞定一切

Functional API 只有两个核心概念。`entrypoint`(入口点) 是工作流的起点，负责管理执行流程和中断恢复；`task`(任务) 是最小工作单元，比如一次 API 调用或数据处理。你在 `entrypoint` 里调用 `task`，`task` 返回一个类似 Future 的对象，调用 `.result()` 就能拿到结果。整个过程就是写普通 Python 函数，不需要画图。

### 2. 人工审批(Human-in-the-Loop)变得简单

想在工作流中间暂停、等人类审批？用 `interrupt()` 函数即可。它会把当前状态序列化并持久保存，工作流无限期挂起。等用户通过 `Command` 提交审批结果后，工作流从中断处恢复，已完成的 task 不会重跑。这对内容审核、合规决策等低容错场景非常关键。

### 3. 短期记忆：对话历史自动管理

用 `previous` 参数可以拿到上一轮对话的状态，用 `entrypoint.final()` 可以分别指定"返回给用户的值"和"存到检查点的值"。这样你可以只返回最新回复，但在后台保存完整对话历史。多用户、多会话的记忆管理开箱即用。

### 4. 长期记忆：跨会话的用户偏好

通过 `store` 参数接入持久存储层(BaseStore)，工作流可以跨不同对话读写用户偏好、历史行为等信息。适合推荐系统、个人助手等需要"越用越懂你"的场景。

### 5. 流式输出：三种模式实时反馈

LangGraph 内置流式支持，你可以订阅三种流：`updates`(工作流进度)、`messages`(LLM Token 逐字输出)、`custom`(自定义进度信息)。用 `StreamWriter` 就能在工作流中随时发送自定义状态更新。

### 6. 可观测性与部署

`entrypoint` 和 `task` 的输入输出可以自动上报到 LangSmith 做追踪和调试。用 `entrypoint` 定义的工作流可以直接部署到 LangGraph Platform 生产环境。

---

## Functional API vs Graph API 对比

| 维度 | Functional API | Graph API (StateGraph) |
|------|---------------|----------------------|
| 控制流 | 普通 Python 代码，if/for 随便写 | 需要定义节点和边的图结构 |
| 状态管理 | 状态局限在函数内部，无需声明 | 需要显式声明 State 和 Reducer |
| 代码量 | 更少，省去图结构定义 | 更多，但结构更清晰 |
| 时间旅行(Time-travel) | 检查点粒度较粗(每个 entrypoint) | 检查点粒度更细(每个节点) |
| 可视化 | 不支持(执行流是动态的) | 支持(可导出为图) |
| 混合使用 | 可以在 entrypoint 中调用 Graph | 可以在 Graph 节点中使用 task |

---

## 整体架构图

```
+------------------------------------------+
|           @entrypoint (入口)              |
|                                          |
|   +----------+    +----------+           |
|   | @task    |    | @task    |           |
|   | 写草稿   |    | 调API    |           |
|   +----+-----+    +----+-----+           |
|        |               |                 |
|        v               v                 |
|   .result()       .result()              |
|        |               |                 |
|        v               |                 |
|   interrupt() -----> 暂停等待人工审批     |
|        |                                 |
|   Command(resume) --> 恢复执行           |
|        |                                 |
|   entrypoint.final(                      |
|     value=返回值,                        |
|     save=持久化值                        |
|   )                                      |
+------------------------------------------+
         |
         v
   LangGraph Platform 部署
   LangSmith 可观测性
```

## 短期记忆工作原理

```
第1轮对话                    第2轮对话
+-----------+               +-----------+
| entrypoint|               | entrypoint|
| previous: |               | previous: |
|   None    |               | [msg1,    |
+-----------+               |  msg2]    |
     |                      +-----------+
     v                           |
messages = []                    v
messages.append(用户消息)   messages = previous
response = call_llm()      messages.append(新消息)
messages.extend(response)   response = call_llm()
     |                      messages.extend(response)
     v                           |
final(                           v
  value=response,           final(
  save=messages             value=response,
)                             save=messages
                            )
     |                           |
     v                           v
 检查点: [msg1, msg2]      检查点: [msg1..msg4]
```

---

## 类比理解

Graph API 像是画流程图——你先画好所有方框和箭头，然后让引擎按图执行。Functional API 更像写剧本——你直接用文字描述"先做A，如果成功就做B，中间暂停让导演审批"，引擎按剧本推进。两种方式最终都能拍出同一部电影，但写剧本对编剧(开发者)来说更自然，画流程图对制片人(运维)来说更直观。

---

## 为什么重要

1. **降低入门门槛**：很多开发者觉得图结构抽象难懂，Functional API 让你用最熟悉的 Python 函数就能构建复杂工作流。
2. **人工审批是生产级 AI 的刚需**：LLM 不可能 100% 准确，在关键决策点加入人工审批是保障可靠性的必要手段。`interrupt` + `Command` 让这件事变成两行代码。
3. **短期+长期记忆的统一方案**：很多团队在对话记忆管理上重复造轮子，LangGraph 用 `previous` + `store` 提供了开箱即用的完整方案。

---

## 延伸思考

1. Functional API 的检查点粒度比 Graph API 粗，这意味着出错时回滚的精度更低。在什么场景下你会因此选择 Graph API？
2. `interrupt` 机制要求所有状态都能 JSON 序列化，如果你的工作流中有数据库连接、文件句柄等不可序列化对象，你会如何处理？
3. 短期记忆用 `previous` 保存完整对话历史，随着对话轮次增多，Token 消耗会线性增长。你会采用什么策略来控制上下文窗口大小？
