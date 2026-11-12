# 在 LangChain 中处理个人隐私数据（PII）

> 原文: [Handling PII data in LangChain](https://www.langchain.com/blog/handling-pii-data-in-langchain) | LangChain Blog | 2023-10-03

## 一句话总结

用户可能在聊天中随口说出姓名、电话、信用卡号等隐私信息（PII），你需要在数据**发送给 LLM 之前**和**写入日志之前**分别做脱敏处理，LangChain 提供了 Microsoft Presidio 和 OpaquePrompts 两条现成路径。

---

## 核心要点

### 1. 什么是 PII，为什么在 LLM 场景下特别危险

PII（Personally Identifiable Information，个人可识别信息）是指能够直接或间接识别个人身份的数据——姓名、邮箱、手机号、身份证号、信用卡号等。在传统应用中，PII 通常出现在表单里，你能预见并控制它。但在聊天场景中，**用户会主动"投喂"PII**——"你好，我是张伟，我的手机号是 138xxxx"——你事先根本不知道用户会说什么。

这些数据如果不做处理，会流向两个危险的终点：LLM 提供商的服务器和你自己的日志系统。

### 2. LLM 提供商的隐私风险

OpenAI、Anthropic、Cohere 等 LLM 提供商都有各自的隐私政策（Privacy Policy），规定了它们如何使用你通过 API 发送的数据。有些提供商可能用这些数据来改进模型或训练新版本。由于 LLM 有时会在推理中"回忆"训练数据中的内容，**理论上你用户的 PII 可能出现在其他用户的回答中**。

这不是恐吓——这是一个已被学术界验证的真实风险。虽然各大提供商都在努力降低这种风险，但隐私政策随时可能变更，你不能把安全完全交给第三方。

```
PII 数据的两条危险路径
=====================

  用户输入: "你好，我是张伟，手机 13812345678"
       |
       +----------+----------+
       |                     |
       v                     v
  +----------+         +-----------+
  | LLM 提供商|         | 日志系统   |
  | (OpenAI) |         | (LangSmith)|
  +----------+         +-----------+
       |                     |
  可能用于模型训练       可能被内部人员
  可能被其他用户看到     或攻击者获取
```

### 3. 脱敏方案一：Microsoft Presidio

Presidio 是微软开源的 PII 识别和脱敏工具，工作分两步：

| 步骤 | 动作 | 技术手段 |
|------|------|---------|
| 第一步：分析 | 扫描文本，找出所有 PII | 规则引擎 + NER 机器学习模型 |
| 第二步：脱敏 | 用占位符或伪造值替换 PII | 替换为 `<PERSON>` 或用 Faker 生成假数据 |

Presidio 的亮点在于它的识别能力：结合了基于规则的逻辑（正则匹配信用卡号格式）和基于机器学习的 NER 模型（识别人名、地名），能开箱检测信用卡号、邮箱、电话、地址、全名等实体。在 LangChain 中，Presidio 作为 chain 的一个步骤嵌入，像"消毒液"一样过滤掉 PII：

```python
# Presidio 脱敏在 LangChain 中的用法
anonymizer = PresidioAnonymizer()

template = """Rewrite this text into an official, short email:
{anonymized_text}"""

prompt = PromptTemplate.from_template(template)
llm = ChatOpenAI(temperature=0)

# 关键：anonymizer.anonymize 作为 chain 的第一步
chain = {"anonymized_text": anonymizer.anonymize} | prompt | llm
response = chain.invoke(text)
```

Presidio 还可以和 LLMGuard 配合使用。LLMGuard 是一套 LLM 安全工具包，不仅覆盖输入端的 PII 脱敏和越狱防护（Jailbreak），还覆盖输出端的恶意链接检测和毒性过滤。

### 4. 脱敏方案二：OpaquePrompts

OpaquePrompts 是另一个选择，和 Presidio 的多技术组合不同，它用**单一的 ML 模型**检测和脱敏 PII。它有两个独特优势：

```
OpaquePrompts 的差异化特性
==========================

+------------------------------------------+
| 1. 极简集成                               |
|    只需把 LLM 包一层即可:                  |
|    OpenAI() --> OpaquePrompts(OpenAI())   |
+------------------------------------------+
| 2. 机密计算 (Confidential Computing)      |
|    连 OpaquePrompts 自己的服务都无法       |
|    访问你的原始数据                        |
+------------------------------------------+
| 3. 自动反脱敏                              |
|    LLM 返回结果后，自动把占位符还原        |
|    为原始实体，用户看到正常的回答          |
+------------------------------------------+
```

在 LangChain 中的使用方式极其简洁——只需把 `OpenAI()` 替换为 `OpaquePrompts(base_llm=OpenAI())`：

```python
chain = LLMChain(
    prompt=prompt,
    llm=OpaquePrompts(base_llm=OpenAI()),  # 一行搞定
    memory=memory,
)
```

### 5. 两种工具的对比

| 维度 | Microsoft Presidio | OpaquePrompts |
|------|-------------------|---------------|
| 识别方式 | 规则 + NER 模型组合 | 单一 ML 模型 |
| 集成复杂度 | 中等（需加入 chain 步骤） | 极低（包装 LLM 即可） |
| 多语言支持 | 有专门教程 | 取决于模型 |
| 反脱敏 | 需手动处理 | 自动还原 |
| 安全保障 | 标准加密 | 机密计算（连服务商都看不到） |
| 生态集成 | 可配合 LLMGuard | 独立使用 |

### 6. LangSmith 日志的脱敏问题

脱敏不只是防止 LLM 提供商看到 PII——如果你用 LangSmith 记录对话日志，原始输入同样会被写入日志。即使你在 chain 中对发往 LLM 的数据做了脱敏，**未脱敏的原始输入仍然会被 LangSmith 记录**。

LangSmith 提供两种解决方案：

**方案 A：完全不记录输入输出**

```bash
# 设置环境变量，LangSmith 将不记录任何输入输出
LANGCHAIN_HIDE_INPUTS=true
LANGCHAIN_HIDE_OUTPUTS=true
```

注意：输出也必须隐藏，因为 LLM 可能在回答中复述用户的 PII（"你好张伟！很高兴认识你"）。这种方案最安全，但你会完全失去调试和数据分析的能力。

**方案 B：脱敏后再记录**

更实用的做法是在**输入进入 chain 之前**就完成脱敏，这样 LLM 和 LangSmith 收到的都是脱敏后的数据。你仍然可以用这些数据来调试、分析甚至微调模型，只是其中不再包含真实的 PII。

```
两种 LangSmith 脱敏方案对比
===========================

方案 A: 完全隐藏
用户 --> [原始数据] --> Chain --> LLM
                        |
                   LangSmith: [空]
                   (什么都不记录)

方案 B: 脱敏后记录
用户 --> [原始数据] --> 脱敏 --> [脱敏数据] --> Chain --> LLM
                                    |
                               LangSmith: [脱敏数据]
                               (记录但不含 PII)
```

---

## 类比理解

把 PII 脱敏想象成**给信件内容打码后再交给快递公司**。快递公司（LLM 提供商）负责把信送到目的地，但你不希望他们看到信的内容。同时，你自己的邮件系统（LangSmith）也会留存一份副本——所以打码这件事必须在信件离开你手中之前就完成，而不是交给快递公司之后再想办法。

Presidio 像一个专业的保密团队，先用 X 光扫描（ML 模型）和人工检查（规则引擎）找出敏感内容，再逐一打码。OpaquePrompts 则像一台智能打码机，你把信塞进去，它自动完成所有工作——甚至连打码机本身（机密计算）都看不到原文。

---

## 为什么重要

- **合规不是可选项**：GDPR、CCPA 等法规对 PII 处理有强制要求，违规罚款可达年营收的 4%
- **用户信任是产品基石**：一次 PII 泄露事件可以摧毁多年建立的用户信任
- **LLM 的记忆风险是独特的**：传统数据库泄露是一次性的，但 LLM 如果在训练中记住了 PII，它可能在未来无限次地向其他用户"回忆"这些信息
- **成本极低**：加几行代码就能显著降低风险，没有理由不做

---

## 延伸思考

1. **脱敏的精度与召回率的权衡**：过于激进的脱敏可能把正常文本误判为 PII（比如把产品名"张三丰"识别为人名），过于保守又可能漏掉真正的 PII。如何根据你的业务场景调整这个平衡？
2. **脱敏后的数据还有多大价值？** 如果你的应用场景恰恰需要 PII 才能正常工作（比如"帮我给张伟发邮件"），脱敏后 Agent 就无法完成任务了。此时你需要的不是脱敏，而是严格的访问控制和数据最小化策略。
3. **端到端加密 vs 脱敏**：脱敏是"信息不出去"，端到端加密是"信息出去了但看不懂"。未来是否会出现支持在加密数据上推理的 LLM（同态加密 + LLM），从根本上解决 PII 问题？
