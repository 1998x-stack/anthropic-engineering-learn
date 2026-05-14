# 构建企业尽职调查 Agent：Deep Agents + LangSmith + 并行子代理

**作者:** LangChain Team  
**来源:** [LangChain Blog](https://www.langchain.com/blog/building-due-diligence-agent)  
**日期:** 2025 年  
**阅读时间:** 约 12 分钟

---

> **一句话总结**  
> 用 Deep Agents 框架构建了一个四阶段企业尽职调查 (Due Diligence) Agent：5 个研究子代理并行收集企业画像、财务健康、诉讼监管、新闻舆情和竞争格局，然后扇出 (Fan-out) 竞品分析、交叉校验矛盾、生成带风险标记和引用的最终报告。以 Rivian Automotive 为验证案例，9 个并行 API 调用在约 23 分钟内完成全流程。

---

## 核心要点

1. **并行子代理是效率杠杆** —— 5 个研究维度互不依赖，并行执行将原本串行需要数小时的调查压缩到约 23 分钟
2. **文件系统即工作底稿** —— 每个子代理将发现写入独立的 Markdown 文件（`corporate-profile.md`、`financial-health.md` 等），既是中间结果也是审计证据
3. **逐字段引用 + 置信度评分** —— 不是笼统给出结论，而是每个字段都附带来源 URL 和置信度 (Confidence Score)，低置信度字段自动触发追加查询
4. **四阶段流水线设计** —— 并行研究 → 竞品扇出 → 交叉校验 → 综合报告，每个阶段的输入是上一阶段的文件系统产出
5. **研究赛道可插拔** —— 替换子代理字典即可从企业尽调切换到信用承销、KYB/KYC、M&A 筛选或供应商风险评估

---

## 一、问题：传统尽职调查为什么慢？

### 人工尽调的痛点

企业尽职调查 (Due Diligence) 是投资、并购、合规审查中的核心环节。一个分析师团队通常需要 2-4 周才能完成一份完整的尽调报告，涉及多个维度的信息搜集和交叉验证。

| 维度 | 传统做法 | 时间成本 | 痛点 |
|------|---------|---------|------|
| 企业画像 | 手动查询工商登记、SEC 文件 | 1-2 天 | 多个数据源，格式不统一 |
| 财务健康 | 阅读财报、分析融资轮次 | 2-3 天 | 数据分散在 Crunchbase、SEC、新闻中 |
| 诉讼与监管 | 检索法院记录、制裁名单 | 1-2 天 | 需要专业法律数据库 |
| 新闻舆情 | 搜索新闻、分析情感倾向 | 1-2 天 | 信息量大，需要甄别噪音 |
| 竞争格局 | 竞品调研、市场定位分析 | 2-3 天 | 每个竞争对手都需要独立分析 |

> **类比理解**  
> 传统尽调就像让一个人串行地跑五个政府部门办事 —— 先去工商局查企业注册，拿到结果后再去法院查诉讼记录，然后去税务局查财务数据......每个部门都要排队等候。而 Agent 方案就像同时派五个人分别去五个部门，最后一起汇合对账。

### 为什么重要

> 尽职调查的核心价值不在于"收集信息"，而在于"发现矛盾"—— 财务数据和新闻报道是否一致？企业声称的市场地位和竞争分析是否吻合？诉讼风险是否被财报披露？**只有当多个维度的信息同时在手，交叉校验才有意义。** 这正是并行子代理的核心优势：不仅更快，而且让交叉分析成为可能。

---

## 二、四阶段架构总览

```
企业尽职调查 Agent 四阶段流水线
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  用户输入: "对 Rivian Automotive 做尽职调查"
    │
    ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  Phase 1: 并行研究 (Parallel Research)                          │
  │                                                                 │
  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ ┌────────┐ │
  │  │ 企业画像  │ │ 财务健康  │ │ 诉讼监管  │ │ 新闻舆情 │ │ 竞争格局 │ │
  │  │ Subagent │ │ Subagent │ │ Subagent │ │Subagent│ │Subagent│ │
  │  └────┬─────┘ └────┬─────┘ └────┬─────┘ └───┬────┘ └───┬────┘ │
  │       │            │            │            │          │       │
  │       ▼            ▼            ▼            ▼          ▼       │
  │  corporate-  financial-  litigation-  news-and-  competitive-  │
  │  profile.md  health.md   regulatory.md reputation.md landscape.md│
  └─────────────────────────────────────────────────────────────────┘
    │
    ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  Phase 2: 竞品扇出 (Competitor Fan-out)                         │
  │                                                                 │
  │  从 competitive-landscape.md 提取 Top 3 竞争对手                 │
  │                                                                 │
  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
  │  │ 竞品分析 #1   │  │ 竞品分析 #2   │  │ 竞品分析 #3   │          │
  │  │ (e.g. Tesla) │  │ (e.g. Lucid) │  │ (e.g. Fisker)│          │
  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
  │         ▼                 ▼                  ▼                  │
  │  competitor-1.md   competitor-2.md   competitor-3.md            │
  └─────────────────────────────────────────────────────────────────┘
    │
    ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  Phase 3: 交叉校验 (Cross-Reference)                            │
  │                                                                 │
  │  读取全部工作底稿，检查：                                         │
  │  · 财务数据 vs 新闻报道 —— 数字是否一致？                          │
  │  · 企业声称 vs 竞品分析 —— 市场定位是否真实？                       │
  │  · 诉讼记录 vs 财报披露 —— 风险是否被隐瞒？                        │
  │                                                                 │
  │  输出: contradictions.md                                        │
  └─────────────────────────────────────────────────────────────────┘
    │
    ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  Phase 4: 综合报告 (Final Report)                               │
  │                                                                 │
  │  汇总所有工作底稿 + 矛盾发现                                      │
  │  · 执行摘要 (Executive Summary)                                 │
  │  · 风险标记 (Risk Flags) 🔴🟡🟢                                │
  │  · 每项结论附带引用 (Citations)                                   │
  │  · 置信度评级 (Confidence Rating)                                │
  │                                                                 │
  │  输出: final-report.md                                          │
  └─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rivian 验证案例: 9 个并行 API 调用，全流程约 23 分钟
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 三、Phase 1：五个研究子代理并行出击

### 编排器 (Orchestrator) 的角色

编排器不做研究，只做三件事：解析用户请求 → 并行启动 5 个子代理 → 等待全部完成后进入下一阶段。

```python
# 编排器启动 Phase 1 的伪代码
research_tracks = {
    "corporate_profile": {
        "task": "调查企业法律实体、高管团队、公司历史",
        "output": "corporate-profile.md"
    },
    "financial_health": {
        "task": "分析融资轮次、收入、估值、烧钱速率",
        "output": "financial-health.md"
    },
    "litigation_regulatory": {
        "task": "检索诉讼记录、SEC 执法行动、制裁名单",
        "output": "litigation-regulatory.md"
    },
    "news_reputation": {
        "task": "搜索新闻报道、争议事件、情感分析",
        "output": "news-and-reputation.md"
    },
    "competitive_landscape": {
        "task": "识别 Top 3 竞争对手、市场定位、差异化分析",
        "output": "competitive-landscape.md"
    }
}

# 使用 Parallel Task API 并行启动全部子代理
tasks = []
for track_name, config in research_tracks.items():
    task = client.tasks.create(
        agent_id=research_agent_id,
        input=f"目标公司: {company_name}\n任务: {config['task']}",
        # 每个子代理写入独立文件
        output_path=f"./reports/{config['output']}"
    )
    tasks.append(task)

# 等待全部完成（并行，非串行）
results = await asyncio.gather(*[wait_for_task(t) for t in tasks])
```

### 五个研究维度详解

| 子代理 | 关注领域 | 数据来源示例 | 输出文件 |
|--------|---------|-------------|---------|
| **企业画像** (Corporate Profile) | 法律实体、注册地、高管、股权结构、公司历史 | SEC EDGAR, 工商注册, LinkedIn | `corporate-profile.md` |
| **财务健康** (Financial Health) | 融资轮次、收入、估值、现金流、烧钱速率 | Crunchbase, 10-K/10-Q, 新闻 | `financial-health.md` |
| **诉讼与监管** (Litigation & Regulatory) | 在途诉讼、SEC 调查、OFAC 制裁名单、环保违规 | PACER, SEC, OFAC, EPA | `litigation-regulatory.md` |
| **新闻与声誉** (News & Reputation) | 媒体报道、争议事件、高管负面新闻、情感倾向 | 新闻 API, Google News, Reddit | `news-and-reputation.md` |
| **竞争格局** (Competitive Landscape) | Top 3 竞争对手、市场份额、差异化定位 | 行业报告, Crunchbase, 新闻 | `competitive-landscape.md` |

> **类比理解**  
> 五个子代理就像律所的五个专业团队 —— 公司法团队查实体结构、财务顾问看账本、诉讼律师翻法院记录、公关团队监控舆情、战略顾问分析竞争。他们同时开工、各写各的备忘录 (Memo)，最后交给合伙人汇总。关键是：**他们之间不需要等对方的结果就能开始工作**，这正是并行化的前提。

---

## 四、关键设计模式

### 模式一：文件系统即工作底稿 (Filesystem as Workpapers)

每个子代理不是把结论"返回"给编排器，而是**写入文件系统**。这个设计有三重好处：

```
为什么用文件系统而不是内存传递？
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  内存传递 (In-Memory)                文件系统 (Filesystem)
  ──────────────────                 ─────────────────────
  · 子代理结果存在上下文中              · 子代理结果写入 .md 文件
  · 编排器上下文越来越大               · 编排器按需读取，上下文可控
  · 任务失败 = 结果丢失               · 任务失败可重跑，已有结果不丢
  · 不可审计                          · 文件本身就是审计证据
  · 难以跨阶段复用                    · Phase 3 直接读 Phase 1 的文件

  目录结构：
  ./reports/
    ├── corporate-profile.md        ← Phase 1 产出
    ├── financial-health.md         ← Phase 1 产出
    ├── litigation-regulatory.md    ← Phase 1 产出
    ├── news-and-reputation.md      ← Phase 1 产出
    ├── competitive-landscape.md    ← Phase 1 产出
    ├── competitor-1-tesla.md       ← Phase 2 产出
    ├── competitor-2-lucid.md       ← Phase 2 产出
    ├── competitor-3-fisker.md      ← Phase 2 产出
    ├── contradictions.md           ← Phase 3 产出
    └── final-report.md             ← Phase 4 产出

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **为什么重要**  
> 在金融合规场景下，"工作底稿"不是可选项 —— 它是审计要求。每一项结论都必须可追溯到原始数据来源。文件系统天然满足这个需求：文件名是索引、文件内容是证据、文件修改时间是时间戳。`FilesystemBackend` 将 Agent 的中间产物变成了合规资产。

### 模式二：逐字段引用与置信度评分 (Per-Field Citations & Confidence)

传统 LLM 的输出是一段流畅的文本，但尽调报告要求**每一项断言都有出处**。本方案的每个字段都附带两个元数据：

```python
# 子代理输出格式示例
{
    "company_name": {
        "value": "Rivian Automotive, Inc.",
        "source": "https://www.sec.gov/cgi-bin/browse-edgar?company=rivian",
        "confidence": 0.98  # 高置信度，来自权威数据源
    },
    "total_funding": {
        "value": "$10.7B",
        "source": "https://www.crunchbase.com/organization/rivian",
        "confidence": 0.85  # 中等置信度，Crunchbase 数据可能滞后
    },
    "pending_lawsuits": {
        "value": "3 件集体诉讼在途",
        "source": "https://www.courtlistener.com/...",
        "confidence": 0.60  # 低置信度 → 触发追加查询
    }
}
```

### 模式三：低置信度触发追加查询 (Low-Confidence Follow-up)

当某个字段的置信度低于阈值时，系统不是简单标记"不确定"，而是**自动触发链式追加查询 (Chained Follow-up)**：

```
低置信度追加查询流程
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  初始查询
    │
    ▼
  ┌─────────────────────────────┐
  │ pending_lawsuits            │
  │ confidence: 0.60            │
  │ source: courtlistener.com   │
  └────────────┬────────────────┘
               │
               │  confidence < 0.75 → 触发追加查询
               │
               ▼
  ┌─────────────────────────────┐
  │ 追加查询 #1                  │
  │ "Rivian class action 2024"  │
  │ via interaction_id 关联      │
  │ 新 source: reuters.com       │
  │ 更新 confidence: 0.82       │
  └─────────────────────────────┘
               │
               │  confidence >= 0.75 → 接受
               ▼
  写入 litigation-regulatory.md
  附带两个 source URLs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

通过 `interaction_id` 将追加查询与初始查询关联，确保 LangSmith 的 Trace 中可以完整追溯一条信息从"低置信度"到"被验证"的全过程。

### 模式四：Parallel Task API 编排

Phase 1 的 5 个子代理和 Phase 2 的 3 个竞品分析子代理，都通过 Parallel Task API 实现真正的并行执行：

| 指标 | 串行执行 (假设) | 并行执行 (实测) | 加速比 |
|------|---------------|---------------|--------|
| Phase 1 (5 个研究子代理) | ~50 分钟 | ~15 分钟 | 3.3x |
| Phase 2 (3 个竞品子代理) | ~18 分钟 | ~8 分钟 | 2.3x |
| Phase 3 + 4 (交叉校验 + 报告) | ~10 分钟 | ~10 分钟 | 1.0x (串行) |
| **总计** | **~78 分钟** | **~23 分钟** | **3.4x** |

> Rivian 验证案例中，9 个并行 API 调用（5 + 3 + 交叉查询）在约 23 分钟内完成全部四个阶段。

---

## 五、Phase 2-4：从研究到报告

### Phase 2：竞品扇出

Phase 1 的竞争格局子代理识别出 Top 3 竞争对手后，Phase 2 为每个竞争对手各启动一个独立的分析子代理：

```python
# 从 competitive-landscape.md 提取竞争对手列表
competitors = extract_competitors("./reports/competitive-landscape.md")
# 例如: ["Tesla", "Lucid Motors", "Fisker"]

# 为每个竞争对手启动独立的分析子代理
competitor_tasks = []
for i, competitor in enumerate(competitors[:3]):
    task = client.tasks.create(
        agent_id=competitor_analysis_agent_id,
        input=f"详细分析 {competitor} 作为 {company_name} 的竞争对手。"
              f"对比产品线、市场定位、财务状况、技术路线。",
        output_path=f"./reports/competitor-{i+1}-{competitor.lower().replace(' ', '-')}.md"
    )
    competitor_tasks.append(task)

# 三个竞品分析并行执行
await asyncio.gather(*[wait_for_task(t) for t in competitor_tasks])
```

### Phase 3：交叉校验

交叉校验 Agent 读取全部工作底稿，专门寻找**矛盾和不一致**：

```
交叉校验矩阵
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  检查项                  文件 A              文件 B             发现
  ─────────────         ──────────         ──────────         ──────
  收入数据一致性          financial-         news-and-          财报显示
                        health.md          reputation.md      Q3 收入 $1.3B
                                                              新闻称 $1.1B
                                                              → 🔴 矛盾

  诉讼风险披露            litigation-        financial-         3 件集体诉讼
                        regulatory.md      health.md          在途，但 10-K
                                                              未提及
                                                              → 🔴 矛盾

  市场定位真实性          competitive-       news-and-          自称"电动皮卡
                        landscape.md       reputation.md      市场领导者"
                                                              但 Ford F-150
                                                              Lightning 销量
                                                              领先
                                                              → 🟡 值得关注

  高管背景验证            corporate-         news-and-          CTO 简历匹配
                        profile.md         reputation.md      无负面信息
                                                              → 🟢 一致

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Phase 4：综合报告

最终报告不是简单的"复制粘贴"，而是带有结构化风险标记的综合分析：

```markdown
# Rivian Automotive 尽职调查报告

## 执行摘要
...

## 风险总览
| 风险类别 | 等级 | 描述 | 来源 |
|---------|------|-----|------|
| 诉讼风险 | 🔴 高 | 3 件未决集体诉讼 | litigation-regulatory.md §2.1 |
| 现金流风险 | 🟡 中 | 烧钱速率高，需 18 个月内再融资 | financial-health.md §3.2 |
| 信息一致性 | 🔴 高 | 收入数据在不同来源间存在 $200M 差异 | contradictions.md §1 |
| 竞争地位 | 🟡 中 | 市场领导者声称与销量数据不符 | contradictions.md §3 |
| 高管团队 | 🟢 低 | 背景验证通过，无负面记录 | corporate-profile.md §1.3 |

## 详细分析
[引用各工作底稿的具体章节...]
```

---

## 六、金融合规视角

### Trace = 机器侧工作底稿

在传统尽调中，分析师的工作底稿是审计的核心证据。在 Agent 尽调中，**LangSmith 的 Trace 扮演了完全相同的角色**：

| 合规要求 | 传统做法 | Agent 做法 |
|---------|---------|-----------|
| 每项结论可追溯 | 分析师在备忘录中标注来源 | 每个字段附带 `source` URL + `confidence` |
| 工作流程可审计 | 工作底稿按时间归档 | LangSmith Trace 记录完整执行路径 |
| 质量控制 | 合伙人审核底稿 | Phase 3 交叉校验 + 置信度阈值 |
| 数据保留 | 物理存档 N 年 | `FilesystemBackend` 持久化到磁盘 |

### EU AI Act 合规

欧盟 AI 法案 (EU AI Act) 对高风险 AI 系统提出了明确的日志记录要求。尽职调查 Agent 在金融服务中属于高风险类别，必须满足：

```
EU AI Act 日志要求 vs Agent 实现
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  法规要求                        Agent 实现方式
  ────────                       ────────────────
  系统运行日志                    LangSmith Trace
  输入数据记录                    用户查询 + 研究 API 响应
  输出决策记录                    最终报告 + 各阶段 .md 文件
  模型版本追溯                    Trace 中记录模型 ID 和参数
  人工审核接口                    Phase 4 报告供人类审阅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 供应商监督 (Vendor Oversight)

当 Agent 调用外部研究 API 或第三方模型时，金融机构需要对供应商进行监督：

- **外部模型** —— Trace 记录每次模型调用的输入/输出，确保可审计
- **研究 API** —— 每个数据来源都带有 URL 引用，可以人工验证
- **置信度评分** —— 不是盲信模型输出，低置信度结论会被标记或追加验证

> **为什么重要**  
> 金融服务是一个"信任但要验证"的行业。Agent 不能是黑盒。**每一条推理路径都必须可追溯、每一项结论都必须有出处、每一次模型调用都必须有日志。** 这不是技术偏好，而是监管硬要求。

---

## 七、可泛化性：替换研究赛道

这套架构的核心价值在于**研究赛道可插拔**。编排器和基础设施（并行执行、文件系统、引用追踪、交叉校验）保持不变，只需替换子代理的任务定义即可适配不同场景：

```
可泛化架构
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  不变的部分 (基础设施层)           可变的部分 (业务层)
  ──────────────────              ─────────────────
  · Orchestrator 编排逻辑          · research_tracks 字典
  · Parallel Task API              · 每个子代理的任务描述
  · FilesystemBackend              · 输出文件命名
  · 置信度评分 + 追加查询           · 置信度阈值
  · 交叉校验引擎                   · 校验规则
  · LangSmith 追踪                 · (无需变更)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

| 应用场景 | 替换哪些研究赛道 | 新增赛道示例 |
|---------|----------------|-------------|
| **信用承销** (Credit Underwriting) | 财务健康 → 信用历史、偿债能力、抵押品评估 | `credit-history.md`, `collateral.md` |
| **KYB/KYC** (Know Your Business/Customer) | 企业画像 → 受益所有权、PEP 筛查、制裁名单 | `beneficial-ownership.md`, `pep-screening.md` |
| **M&A 筛选** (M&A Screening) | 竞争格局 → 协同效应分析、整合风险、文化评估 | `synergy-analysis.md`, `integration-risk.md` |
| **供应商风险评估** (Vendor Risk) | 诉讼监管 → 供应链韧性、ESG 合规、信息安全 | `supply-chain.md`, `esg-compliance.md` |

```python
# 示例：将尽调 Agent 改造为 KYB 合规 Agent
# 只需替换 research_tracks 字典
kyb_tracks = {
    "beneficial_ownership": {
        "task": "识别最终受益所有人 (UBO)，穿透股权结构至自然人",
        "output": "beneficial-ownership.md"
    },
    "pep_screening": {
        "task": "在 PEP (政治公众人物) 数据库中筛查高管和股东",
        "output": "pep-screening.md"
    },
    "sanctions_check": {
        "task": "在 OFAC、EU、UN 制裁名单中检查企业及关联方",
        "output": "sanctions-check.md"
    },
    "adverse_media": {
        "task": "负面媒体筛查：洗钱、欺诈、腐败相关报道",
        "output": "adverse-media.md"
    },
    "corporate_registry": {
        "task": "验证工商注册信息、营业执照、税务登记",
        "output": "corporate-registry.md"
    }
}
# 编排器代码完全不需要修改
```

> **类比理解**  
> 这就像一个通用的"调查公司模板"。骨架 —— 并行派出调查员、收集独立报告、交叉比对、写总结 —— 是固定的。变化的只是"派谁去调查什么"。换一批调查员（子代理）就能从企业尽调变成反洗钱审查。

---

## 八、关键技术决策总结

| 决策 | 选择 | 替代方案 | 为什么这样选 |
|------|------|---------|------------|
| 子代理间通信方式 | 文件系统 (`.md` 文件) | 内存状态传递 | 满足审计要求，支持断点续跑，上下文可控 |
| 并行化策略 | Parallel Task API | `asyncio.gather` 本地并发 | 支持分布式执行和 LangSmith 全链路追踪 |
| 引用粒度 | 逐字段 (Per-field) | 逐段落 / 文档级 | 金融合规要求每项断言可追溯 |
| 低置信度处理 | 自动追加查询 | 标记为"待人工确认" | 尽量减少人工介入，提升自动化率 |
| 竞品分析方式 | 动态扇出 (Fan-out) | 固定数量的竞品子代理 | 竞争对手数量因目标公司而异 |
| 交叉校验时机 | 独立阶段 (Phase 3) | 嵌入 Phase 1 | 需要全部维度的数据才能做有意义的交叉比对 |
| 报告格式 | 结构化 Markdown | PDF / JSON | Markdown 兼顾可读性和可解析性 |

---

## 延伸思考

1. **置信度校准的挑战：** 子代理自我报告的置信度评分可靠吗？一个子代理说"我 95% 确信这个融资数据是准确的"，这个 0.95 是校准过的 (Calibrated) 还是随意给的？是否需要一个独立的"置信度审计 Agent"来验证置信度评分本身的可信度？在金融决策中，过度自信和过度不自信都可能导致严重后果。

2. **23 分钟的实用性边界在哪里？** Rivian 是一家信息高度公开的上市公司。如果目标是一家私有公司，信息稀疏度急剧上升 —— 没有 SEC 文件、没有公开财报、新闻覆盖有限。并行化能加速已有信息的采集，但无法创造不存在的信息。这套方案在"信息黑洞"场景下的降级策略是什么？

3. **交叉校验的深度 vs. 广度：** Phase 3 检查的是"不同维度之间"的矛盾，但"同一维度内部"的矛盾呢？比如两篇新闻对同一事件的报道相互矛盾 —— 这需要子代理自身具备内部一致性检查的能力，还是应该交给 Phase 3 统一处理？

4. **从"收集信息"到"做出判断"的鸿沟：** 当前系统生成的是"带风险标记的信息汇总"，最终的投资/合规决策仍由人类做出。但如果 Agent 需要给出"投 / 不投"的建议呢？这需要什么样的额外能力 —— 行业经验的编码、风险偏好的量化、还是对不确定性的更精细建模？

5. **多租户场景下的数据隔离：** 如果尽调 Agent 被多个客户共用，Agent A 调查的公司 X 的信息是否可能泄露到 Agent B 的调查中？文件系统路径隔离是否足够，还是需要进程级或容器级的隔离？在金融服务中，这不是性能问题，而是合规红线。