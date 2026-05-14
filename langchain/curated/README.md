# LangChain Blog — Agent 工程深度文章合集

> 收集自 [LangChain Blog](https://www.langchain.com/blog)，精选 Agent 工程技术深度文章。  
> 全部改写为中文教学风格，配有类比解释、ASCII 架构图、核心要点总结。  
> 更新时间：2026-05-14

---

## Part 1：Agent 线束基础

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 01 | [Agent 线束解剖学](./01-the-anatomy-of-an-agent-harness.md) | Vivek Trivedy | Agent = Model + Harness，从模型能力推导线束设计 |
| 02 | [后台运行子 Agent](./02-running-subagents-in-the-background.md) | Hunter Lovell, Colin Francis | 异步子 Agent 模式，解决阻塞和并发问题 |
| 03 | [可观测性需要反馈](./03-agent-observability-needs-feedback.md) | Harrison Chase | 追踪 + 反馈 = 学习闭环，三层改进模型/线束/上下文 |
| 04 | [GTM Agent 实战](./04-how-we-built-langchains-gtm-agent.md) | Vishnu Suresh, Jess Ou | 销售自动化：转化率提升 250%，记忆系统、子代理委托 |
| 05 | [人类判断改进循环](./05-human-judgment-in-the-agent-improvement-loop.md) | Rahul Verma | 将人类专业判断融入 Agent 开发全流程，自动化评估飞轮 |
| 06 | [线束与记忆](./06-your-harness-your-memory.md) | Harrison Chase | 记忆不是插件而是线束，开源线束避免厂商锁定 |

## Part 2：Harness 工程进阶

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 07 | [上下文工程](./07-context-engineering-for-agents.md) | LangChain Team | 四大策略：写入/选择/压缩/隔离，管理 Agent 上下文窗口 |
| 08 | [中间件定制线束](./08-how-middleware-lets-you-customize-your-agent-harness.md) | LangChain Accounts | 6 个中间件钩子，Deep Agents 架构拆解 |
| 09 | [Agent 持续学习](./09-continual-learning-for-ai-agents.md) | LangChain Team | 三层学习：模型权重/线束代码/上下文记忆 |
| 10 | [Harness 工程优化实战](./10-improving-deep-agents-with-harness-engineering.md) | LangChain Team | Terminal Bench Top 30→Top 5，Ralph Loop，推理三明治 |
| 11 | [Eval 驱动的 Harness 爬坡](./11-better-harness-eval-driven-hill-climbing.md) | LangChain Accounts | Eval 即训练数据，自动化爬坡方法论 |
| 12 | [Agent 工程：新学科](./12-agent-engineering-a-new-discipline.md) | LangChain Team | 定义 Agent 工程学科，产品思维+工程+运维三支柱 |

---

## 文章结构说明

每篇文章均采用统一的教学风格：

| 元素 | 说明 |
|------|------|
| **一句话总结** | 开篇精炼概括全文核心观点 |
| **核心要点** | 3-5 条关键收获，快速把握重点 |
| **类比理解** | 用生活化比喻解释技术概念 |
| **ASCII 架构图** | 可视化系统架构和数据流 |
| **为什么重要** | 解释概念的实际意义和影响 |
| **延伸思考** | 引导深入思考的开放性问题 |

---

## 推荐阅读路径

### 路径 A：从零到一（适合初学者）

1. `12 Agent 工程新学科` → 理解这个领域是什么
2. `01 线束解剖学` → 理解 Agent 系统的核心架构
3. `07 上下文工程` → 掌握最关键的工程技能
4. `04 GTM Agent 实战` → 看一个完整的业务落地案例

### 路径 B：构建改进闭环（适合实践者）

1. `03 可观测性与反馈` → 建立观测基础
2. `05 人类判断飞轮` → 融入人类专家知识
3. `11 Eval 驱动爬坡` → 系统化改进方法论
4. `10 Harness 工程优化` → 看 Top 30→Top 5 的具体操作

### 路径 C：深度架构（适合架构师）

1. `01 线束解剖学` → 核心架构
2. `08 中间件定制` → 扩展机制
3. `02 异步子 Agent` → 并发编排
4. `09 持续学习` → 三层学习架构
5. `06 线束与记忆` → 开源战略思考
