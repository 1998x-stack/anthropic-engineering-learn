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

## Part 3：Deep Agents 全生态

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 13 | [深度 Agent](./13-deep-agents.md) | Harrison Chase | 四大特征：详尽提示/规划工具/子Agent/文件系统 |
| 14 | [生产级运行时](./14-runtime-behind-production-deep-agents.md) | Sydney Runkle, Vivek Trivedy | 11 层运行时基础设施：持久执行/记忆/多租户/HITL/可观测性 |
| 15 | [技能系统](./15-using-skills-with-deep-agents.md) | Lance Martin | Skills = 渐进式披露，token 高效，持续学习 |
| 16 | [上下文管理](./16-context-management-for-deepagents.md) | LangChain Team | 三层机制：大结果卸载/大输入截断/摘要压缩 |
| 17 | [调试 Deep Agents](./17-debugging-deep-agents-with-langsmith.md) | LangChain Accounts | Polly AI 助手 + LangSmith Fetch CLI 调试工具链 |
| 18 | [多模型调优](./18-tuning-deep-agents-different-models.md) | Vivek Trivedy, Mason Daugherty | Harness Profiles：按模型定制提示/工具/中间件 |

## Part 4：评估与追踪实战

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 19 | [评估工程：少即是多](./19-how-we-build-evals-for-deep-agents.md) | LangChain Accounts | 行为目录驱动评估设计，正确性优先于效率 |
| 20 | [评估深度 Agent 五条经验](./20-evaluating-deep-agents-our-learnings.md) | LangChain Accounts | 定制断言/单步评估/完整轮次/多轮模拟/环境隔离 |
| 21 | [追踪驱动改进循环](./21-traces-start-agent-improvement-loop.md) | LangChain Accounts | 追踪→富化→改进→验证→部署，完整反馈闭环 |

## Part 5：上下文工程崛起与开放生态

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 22 | [上下文工程的崛起](./22-the-rise-of-context-engineering.md) | Harrison Chase | 定义上下文工程，与提示工程的区别，五大要素 |
| 23 | [文件系统驱动的上下文工程](./23-how-agents-can-use-filesystems-for-context-engineering.md) | Nick Huang | 文件系统解决四类上下文失败：过多/过大/找不到/缺失 |
| 24 | [Deep Agents Deploy：开放替代方案](./24-deep-agents-deploy-open-alternative.md) | LangChain Team | 一键部署 vs 围墙花园，记忆所有权是核心战场 |

## Part 6：生产自愈与规模化洞察

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 25 | [Agent 生产自愈](./25-how-my-agents-self-heal-in-production.md) | LangChain Team | 部署→监控→分诊→修复自动循环，Poisson 检测 + Open SWE |
| 26 | [从追踪到洞察](./26-from-traces-to-insights.md) | LangChain Accounts | 聚类发现未知模式，传统分析无法回答的 WHY |
| 27 | [Terminal Bench 基准评估](./27-evaluating-deepagents-cli-on-terminal-bench.md) | LangChain Accounts | 基线建立 42.65%，Harbor 沙箱隔离评估框架 |

## Part 7：架构选型与实战案例

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 28 | [框架/运行时/线束三层架构](./28-agent-frameworks-runtimes-and-harnesses.md) | LangChain Accounts | LangChain/LangGraph/DeepAgents 各层定位 |
| 29 | [技能评估方法论](./29-evaluating-skills.md) | LangChain Accounts | 四步评估流水线，82% vs 9% 的技能增益 |
| 30 | [Moda 设计 Agent 实战](./30-how-moda-builds-design-agents.md) | LangChain Team | 自定义 DSL、动态工具加载、Cursor 式协作 UX |

## Part 8：多 Agent 架构与实战

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 31 | [多 Agent 架构四模式](./31-choosing-the-right-multi-agent-architecture.md) | Sydney Runkle | 子代理/技能/交接/路由四种模式选型与性能对比 |
| 32 | [构建多 Agent 应用](./32-building-multi-agent-applications-with-deep-agents.md) | LangChain Team | 子代理隔离上下文 + 技能渐进披露，可组合使用 |
| 33 | [尽职调查 Agent](./33-building-due-diligence-agent.md) | LangChain Team | 五路并行子代理→竞品扇出→交叉验证→合规审计 |

## Part 9：Agentic 工程与评估体系

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 34 | [Agentic 工程重塑软件开发](./34-agentic-engineering-redefining-software.md) | Renuka Kumar, Prashanth Ramagopal (Cisco) | 多 Agent 协作镜像真实团队，93% 调试提速 |
| 35 | [Agent 评估就绪清单](./35-agent-evaluation-readiness-checklist.md) | LangChain Accounts | 6 步清单：追踪→数据集→评分器→CI/CD 门控 |
| 36 | [可观测性驱动评估](./36-agent-observability-powers-evaluation.md) | LangChain Accounts | Run/Trace/Thread 三原语映射三级评估 |

## Part 12：沙箱与自主上下文压缩

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 43 | [用沙箱执行代码](./43-execute-code-with-sandboxes.md) | LangChain Team | 五大沙箱需求、Setup 脚本、安全防护 |
| 44 | [Agent 连接沙箱的两种模式](./44-two-patterns-agents-connect-sandboxes.md) | LangChain Team | Agent 在沙箱内 vs 沙箱作为工具，安全与迭代权衡 |
| 45 | [自主上下文压缩](./45-autonomous-context-compression.md) | LangChain Accounts | 时机比阈值重要，Agent 自主决定何时压缩 |

## Part 10：Agent 实用指南

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 37 | [什么是 Agent](./37-what-is-an-agent.md) | Harrison Chase | Agent 是光谱，越 agentic 越需要框架/运行时/观测 |
| 38 | [Agent 规划与推理](./38-planning-for-agents.md) | Harrison Chase | 领域特定认知架构 > 通用推理，代码替 LLM 做规划 |
| 39 | [Claude Code → 领域 Agent](./39-how-to-turn-claude-code-into-domain-agent.md) | Aliyan Ishfaq | Claude.md + MCP = 最佳组合，82% vs 9% 完成率 |

## Part 11：沟通、加速与互操作

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 40 | [沟通就是一切](./40-communication-is-all-you-need.md) | Harrison Chase | Agent 出错 = 沟通失败，七个推论覆盖提示/代码/UX |
| 41 | [如何加速你的 Agent](./41-how-do-i-speed-up-my-agent.md) | Harrison Chase | 五策略：找瓶颈/降感知/减调用/加速单次/并行 |
| 42 | [Agent Protocol 互操作标准](./42-agent-protocol-interoperability.md) | LangChain Accounts | Runs/Threads/Store 三概念，跨框架标准通信 |

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
3. `13 深度 Agent` → 了解什么让 Agent 从浅层变深度
4. `07 上下文工程` → 掌握最关键的工程技能
5. `04 GTM Agent 实战` → 看一个完整的业务落地案例

### 路径 B：构建改进闭环（适合实践者）

1. `03 可观测性与反馈` → 建立观测基础
2. `05 人类判断飞轮` → 融入人类专家知识
3. `11 Eval 驱动爬坡` → 系统化改进方法论
4. `10 Harness 工程优化` → 看 Top 30→Top 5 的具体操作
5. `17 调试 Deep Agents` → Polly + CLI 实战调试

### 路径 C：深度架构（适合架构师）

1. `01 线束解剖学` → 核心架构
2. `08 中间件定制` → 扩展机制
3. `02 异步子 Agent` → 并发编排
4. `16 上下文管理` → 卸载/摘要/恢复策略
5. `14 生产级运行时` → 持久执行、多租户、沙箱
6. `18 多模型调优` → Harness Profiles 适配不同模型

### 路径 D：Deep Agents 从入门到生产

1. `13 深度 Agent` → 什么是 Deep Agents
2. `15 技能系统` → Skills 渐进式披露
3. `16 上下文管理` → 长时运行的上下文压缩
4. `14 生产级运行时` → 部署到生产环境
5. `17 调试` → 排查生产问题
6. `18 多模型调优` → 适配不同模型提供商

### 路径 E：评估体系（适合质量工程师）

1. `19 评估工程` → 如何设计有效的 Eval
2. `20 评估五条经验` → 单步/多步/多轮/环境隔离实操
3. `21 追踪驱动改进` → 从追踪到改进的完整闭环
4. `11 Eval 驱动爬坡` → 自动化爬坡方法论
5. `03 可观测性与反馈` → 反馈来源与平台需求
