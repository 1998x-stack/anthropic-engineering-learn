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

## Part 30：Agent 记忆工程

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 97 | [LangGraph Memory 语义搜索](./97-semantic-search-langgraph-memory.md) | LangChain Team | 从精确匹配到按"意思"检索记忆 |
| 98 | [LangMem SDK](./98-langmem-sdk.md) | LangChain Team | 三种记忆（语义/程序/情景），自动优化行为模式 |
| 99 | [Agent Builder 记忆实战](./99-how-we-built-agent-builder-memory.md) | LangChain Team | 文件即记忆，用户反馈驱动自然生长 |

## Part 24：RAG 深度技术

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 79 | [结构化切分与元数据 RAG](./79-a-chunk-by-any-other-name.md) | LangChain Team | HTML 标题层级切分 + 自查询检索器 |
| 80 | [图元数据过滤 RAG](./80-graph-metadata-filtering-rag.md) | LangChain Team | Neo4j 多跳关系预过滤 + 向量搜索 |
| 81 | [查询构造四策略](./81-query-construction.md) | LangChain Team | 元数据过滤/SQL/SQL+语义/Cypher |

## Part 25：工具系统

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 82 | [Agent 工具包](./82-agent-toolkits.md) | LangChain Team | 7 种 Toolkit，SQL 纠错循环 |
| 83 | [工具调用标准化](./83-tool-calling-with-langchain.md) | LangChain Team | bind_tools/tool_calls/agent 三组件 |
| 84 | [Command 多 Agent 工具](./84-command-tool-multi-agent.md) | LangChain Team | 无边图概念，跨层级 Handoff |

## Part 26：安全与合规

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 85 | [Agent 授权入门](./85-agent-authorization.md) | LangChain Team | AuthN vs AuthZ，Agent 三大独特挑战 |
| 86 | [两种 Agent 授权模式](./86-two-types-agent-authorization.md) | LangChain Team | Assistant(代理用户) vs Claw(独立凭证) |
| 87 | [PII 数据处理](./87-handling-pii-data.md) | LangChain Team | Presidio vs OpaquePrompts，日志脱敏 |

## Part 27：生产运维与自学习

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 88 | [在 AI 中 Traces 就是文档](./88-in-ai-traces-document-the-app.md) | Harrison Chase | 面向 Trace 的工程实践迁移 |
| 89 | [生产环境 Agent 监控](./89-production-monitoring.md) | LangChain Team | 四大支柱：采集/发现/评估/审核 |
| 90 | [自学习 AI 系统](./90-self-learning-gpts.md) | LangChain Team | 四步闭环：追踪→反馈→筛选→Few-shot 注入 |

## Part 28：系统化改进与基准测试

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 91 | [SCIPE 系统化改进](./91-scipe-systematic-improvement.md) | LangChain Team | 概率分析定位最值得修复的节点 |
| 92 | [Promptim 自动优化](./92-promptim-prompt-optimizer.md) | LangChain Team | 跑分→元提示改写→再跑分循环，vs DSPy |
| 93 | [Agent 工具使用基准](./93-benchmarking-agent-tool-use.md) | LangChain Team | 4 个基准任务，7 个模型对比 |

## Part 29：知识图谱、Functional API 与工程复盘

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 94 | [知识图谱增强 RAG](./94-knowledge-graphs-enhance-rag.md) | LangChain Team | 自动建图 + 三路混合检索 |
| 95 | [LangGraph Functional API](./95-langgraph-functional-api.md) | LangChain Team | @entrypoint/@task 两原语，vs Graph API |
| 96 | [重建 Chat LangChain](./96-rebuilding-chat-langchain.md) | LangChain Team | 放弃向量检索，双模 Agent + 子图架构 |

## Part 21：Runtime 设计与 Agent 记忆

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 70 | [构建 LangGraph](./70-building-langgraph.md) | LangChain Team | Channel-Node 执行算法，六大核心特性 |
| 71 | [别再做 Workflow Builder](./71-not-another-workflow-builder.md) | Harrison Chase | 可视化工作流被高低两端夹击，真正问题是什么 |
| 72 | [Agent 记忆系统](./72-memory-for-agents.md) | LangChain Team | CoALA 三种记忆（程序/语义/情景），热路径 vs 后台 |

## Part 22：Ambient Agent、中间件与可观测性

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 73 | [Ambient Agent 概念](./73-introducing-ambient-agents.md) | LangChain Team | 后台主动工作，通知/提问/审核三模式，Agent Inbox |
| 74 | [Agent 中间件模式](./74-agent-middleware-patterns.md) | LangChain Team | before/after/modify 三钩子，洋葱模型执行 |
| 75 | [框架与可观测性](./75-agent-frameworks-and-observability.md) | LangChain Team | LangSmith 框架无关设计，多框架+OTEL 集成 |

## Part 23：LLM 评估方法论

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 76 | [LLM 评估器准确性](./76-how-correct-are-llm-evaluators.md) | LangChain Team | 三种评估器基准测试，GPT-4 优势与固有偏见 |
| 77 | [LLM-as-Judge 对齐人类偏好](./77-aligning-llm-judge-human-preferences.md) | LangChain Team | 自改进评估四步飞轮，少样本+人类纠正 |
| 78 | [评估驱动开发](./78-evaluation-driven-development.md) | LangChain Team | Dosu 案例，EDD 六步工作流，失败信号金字塔 |

## Part 19：框架思考、RAG 解构与记忆系统

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 64 | [如何思考 Agent 框架](./64-how-to-think-about-agent-frameworks.md) | Harrison Chase | 工作流 vs Agent 混合体，控制上下文是关键 |
| 65 | [RAG 技术全景拆解](./65-deconstructing-rag.md) | LangChain Team | 查询变换/路由/构造/索引/后处理五大模块 |
| 66 | [Agent Builder 记忆系统](./66-agent-builder-memory-system.md) | LangChain Team | 虚拟文件系统表示记忆，用户纠正驱动学习 |

## Part 20：Prompt 优化与产品指标

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 67 | [Prompt 优化系统性方法](./67-exploring-prompt-optimization.md) | LangChain Team | 5 种算法对比，优化 = 长期记忆 |
| 68 | [Few-shot 提升工具调用](./68-few-shot-prompting-tool-calling.md) | LangChain Team | 3 个动态示例 ≈ 13 个固定示例，消息格式 > 字符串 |
| 69 | [AI 产品成功的隐藏指标](./69-hidden-metric-ai-product-success.md) | LangChain Team | CAIR 信心框架：Value/(Risk×Correction) |

## Part 17：Agent 设计模式深潜

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 58 | [反思型 Agent](./58-reflection-agents.md) | LangChain Team | 基础反思→Reflexion→LATS，系统1/系统2思维 |
| 59 | [规划型 Agent](./59-planning-agents.md) | LangChain Team | Plan-and-Execute/ReWOO/LLMCompiler，DAG 并行调度 |
| 60 | [何时构建多 Agent 系统](./60-how-and-when-multi-agent.md) | LangChain Team | 上下文工程 + 读写分离，Cognition/Anthropic 洞察 |

## Part 18：AI 新范式与工具链

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 61 | [赢在 AI 新技术栈](./61-winning-in-ai-new-stack.md) | 5 位 CEO 联合 | AI 技术栈 6 大组件，四个发展阶段 |
| 62 | [Polly：AI Agent 工程师](./62-introducing-polly-ai-agent-engineer.md) | LangChain Team | 追踪调试/对话分析/提示词优化三大能力 |
| 63 | [开源模型跨越门槛](./63-open-models-crossed-threshold.md) | LangChain Team | GLM-5/MiniMax vs Opus/GPT，混合架构趋势 |

## Part 15：Agent UX 设计三部曲

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 52 | [Agent UX：聊天模式](./52-ux-for-agents-chat.md) | LangChain Team | 流式/非流式聊天，聊天只是起点不是终点 |
| 53 | [Agent UX：环境模式](./53-ux-for-agents-ambient.md) | LangChain Team | 人在环上 vs 人在环中，Agent Inbox 反转模式 |
| 54 | [Agent UX：后台与新范式](./54-ux-for-agents-background.md) | LangChain Team | 电子表格式/生成式 UI/协作式，五大 UX 范式总览 |

## Part 16：基础设施与战略思考

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 55 | [OpenAI 对认知架构的押注](./55-openais-bet-on-cognitive-architecture.md) | Harrison Chase | GPTs/Assistants API 战略，开源 vs 闭源认知架构 |
| 56 | [为什么需要 Agent 基础设施](./56-why-agent-infrastructure.md) | LangChain Team | 持久执行/心跳/任务队列/扩缩容六大需求 |
| 57 | [外包基础设施，拥有认知架构](./57-outsource-infrastructure-own-architecture.md) | LangChain Team | 贝索斯"啤酒理论"判断自研 vs 外包 |

## Part 14：认知架构、MCP 辩论与构建指南

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 49 | [什么是认知架构](./49-what-is-a-cognitive-architecture.md) | Harrison Chase | 五级自主光谱：纯代码→单调用→链→路由→Agent |
| 50 | [MCP：昙花一现还是未来标准](./50-mcp-fad-or-fixture.md) | Harrison Chase vs Nuno Campos | CEO vs 技术负责人辩论，正反方观点深度碰撞 |
| 51 | [六步构建 Agent 实操指南](./51-how-to-build-an-agent.md) | LangChain Accounts | 定义→SOP→MVP→编排→测试→部署，邮件 Agent 全程案例 |

## Part 13：开源 Agent 工具链与 EPD 变革

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 46 | [Open SWE：开源编程 Agent](./46-open-swe-open-source-coding-agent.md) | LangChain Team | 内部编程 Agent 架构模式，Stripe/Ramp/Coinbase 对比 |
| 47 | [Open Deep Research](./47-open-deep-research.md) | LangChain Team | 三阶段深度研究：范围→研究→写作，多 Agent 并行 |
| 48 | [编程 Agent 重塑 EPD](./48-how-coding-agents-reshape-epd.md) | Harrison Chase | PRD 已死/万岁，构建者 vs 评审者，系统思维为王 |

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
