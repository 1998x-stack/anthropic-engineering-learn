# LangChain Blog — Agent 工程深度文章合集

> 收集自 [LangChain Blog](https://www.langchain.com/blog)，精选 Agent 工程技术深度文章。  
> 全部改写为中文教学风格，配有类比解释、ASCII 架构图、核心要点总结。  
> 更新时间：2026-05-14

---

## 目录

| # | 标题 | 作者 | 核心主题 |
|---|------|------|----------|
| 01 | [Agent 线束解剖学](./01-the-anatomy-of-an-agent-harness.md) | Vivek Trivedy | Agent = Model + Harness，从模型能力推导线束设计 |
| 02 | [后台运行子 Agent](./02-running-subagents-in-the-background.md) | Hunter Lovell, Colin Francis | 异步子 Agent 模式，解决阻塞和并发问题 |
| 03 | [可观测性需要反馈](./03-agent-observability-needs-feedback.md) | Harrison Chase | 追踪 + 反馈 = 学习闭环，三层改进模型/线束/上下文 |
| 04 | [GTM Agent 实战](./04-how-we-built-langchains-gtm-agent.md) | Vishnu Suresh, Jess Ou | 销售自动化：转化率提升 250%，记忆系统、子代理委托 |
| 05 | [人类判断改进循环](./05-human-judgment-in-the-agent-improvement-loop.md) | Rahul Verma | 将人类专业判断融入 Agent 开发全流程，自动化评估飞轮 |
| 06 | [线束与记忆](./06-your-harness-your-memory.md) | Harrison Chase | 记忆不是插件而是线束，开源线束避免厂商锁定 |

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

1. **入门** → 读 `01 线束解剖学`，理解 Agent 系统的核心架构
2. **进阶** → 读 `02 异步子 Agent`，了解长任务编排模式
3. **观测与改进** → 读 `03 可观测性` + `05 人类判断飞轮`，建立 Agent 改进闭环
4. **实战案例** → 读 `04 GTM Agent 实战`，看真实业务落地
5. **深度思考** → 读 `06 线束与记忆`，理解开源线束的战略意义
