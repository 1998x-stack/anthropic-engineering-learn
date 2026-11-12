# 反思型智能体 (Reflection Agents)

> 一句话总结：让 AI 学会"回头看"自己的答案、批评自己、改进自己，用额外的计算时间换取更高的输出质量。

---

## 核心要点

- **反思 (Reflection)** 是一种提示策略，让 LLM 审视并批评自己过去的输出，从而提升 Agent 的成功率
- 它对应人类心理学中的"系统2思维"——从本能反应升级到深思熟虑
- 本文介绍三种递进的反思架构：基础反思、Reflexion、LATS（语言智能体树搜索）
- 核心权衡：用更多推理时间换更好的输出质量，适合质量优先的场景

---

## 三种反思架构对比

| 维度 | 基础反思 (Basic Reflection) | Reflexion | LATS |
|------|---------------------------|-----------|------|
| 核心思路 | 生成器 + 反思器来回迭代 | 带工具调用的显式自我批评 | 蒙特卡洛树搜索 + 反思 |
| 外部信息 | 无 | 有（搜索工具、引用） | 有（环境反馈 + 反思评分） |
| 搜索路径 | 单条线性路径 | 单条线性路径 | 多条分支路径（树结构） |
| 适用场景 | 写作润色、简单改进 | 需要事实核查的回答 | 复杂推理、代码生成 |
| 计算开销 | 低 | 中 | 高 |

---

## 架构流程图

```
=== 基础反思 ===

  用户输入
     |
     v
 [生成器] ---> 输出草稿
     ^            |
     |            v
     +------- [反思器] (扮演老师角色，提出批评)
     
  循环固定次数后返回最终结果


=== Reflexion ===

  用户输入
     |
     v
 [草稿生成] --> [执行工具(搜索/查证)] --> [修订器(反思+引用)]
     ^                                          |
     |                                          v
     +--- 未达到最大迭代次数? <--- 是 ---  检查迭代次数
                                   否
                                    |
                                    v
                               返回最终结果


=== LATS (语言智能体树搜索) ===

                    [根节点: 初始响应]
                   /        |        \
                  /         |         \
           [动作A1]    [动作A2]    [动作A3]    <-- 扩展: 并行生成N个候选
              |            |            |
         [反思+评分]  [反思+评分]  [反思+评分]   <-- 反思+评估
              |            |            |
         [回传分数]   [回传分数]   [回传分数]    <-- 反向传播
                           |
                      [选择最优]                <-- 用UCT公式选择
                      /         \
                 [继续展开]   [返回结果]
```

---

## 类比理解

**基础反思**就像你写完一篇作文后，请一位老师帮你改。老师给出批评，你改完再交给老师看，来回几轮后交卷。问题是这位"老师"其实也是你自己——缺乏外部视角，改进幅度有限。

**Reflexion**则像是你写完作文后，不仅请老师批评，还要求自己去图书馆查证每一个事实。你必须注明引用来源，明确列出"哪些内容是多余的""哪些关键信息遗漏了"。因为有了外部事实的锚定，反思的质量大幅提升。

**LATS**更像下棋时的思考方式。你不是只想一步走一步，而是在脑中模拟多种走法（蒙特卡洛树搜索），评估每种走法的胜率，选择最有前途的分支继续深入。如果某条路走不通，还能回退换一条路，不会像 Reflexion 那样一条路走到黑。

---

## 深入原理

### 系统1 vs 系统2思维

心理学家 Daniel Kahneman 将人类思维分为两个系统。系统1是快速、直觉式的——看到"2+2"立刻知道答案是4。系统2是慢速、审慎的——比如计算"17x24"时你需要一步步推演。

普通的 LLM 调用本质上都是"系统1"——一次前向传播，立刻给出回答。反思机制的价值在于，通过多次推理迭代，让模型能够进入"系统2"模式，真正地检查和修正自己的推理过程。

### Reflexion 的关键设计

Reflexion 强制要求 Agent 做三件事：
1. **生成引用 (Citations)**：每个断言必须有来源支撑
2. **列出多余内容 (Superfluous)**：哪些部分偏题了
3. **列出遗漏内容 (Missing)**：哪些关键点没有覆盖

这种结构化的自我批评比简单的"请改进一下"有效得多，因为它把模糊的"反思"变成了具体的、可执行的检查清单。

### LATS 的 UCT 公式

LATS 用上置信界 (Upper Confidence Bound, UCT) 来平衡"利用"和"探索"：

```
UCT = value/visits + c * sqrt(ln(parent.visits) / visits)
```

- 第一项 `value/visits`：历史平均奖励，越高说明这条路径越好（利用已知好路径）
- 第二项 `c * sqrt(...)`：访问次数越少的节点，这个值越大（鼓励探索新路径）
- `c` 是平衡系数，控制探索力度

这个公式的精妙之处在于：它不会贪心地只走看起来最好的路，也会留出精力去尝试未知路径——万一有惊喜呢？

### LATS 的四步循环

1. **选择 (Select)**：用 UCT 找到最值得探索的节点
2. **扩展+模拟 (Expand & Simulate)**：并行生成 N 个候选动作并执行
3. **反思+评估 (Reflect & Evaluate)**：观察执行结果，给每个动作打分
4. **回传 (Backpropagate)**：将分数从叶节点传回根节点，更新路径统计

---

## 代码骨架

### 基础反思 (LangGraph)

```python
from langgraph.graph import MessageGraph

builder = MessageGraph()
builder.add_node("generate", generation_node)
builder.add_node("reflect", reflection_node)
builder.set_entry_point("generate")

def should_continue(state):
    if len(state) > 6:        # 固定迭代3轮(每轮2条消息)
        return END
    return "reflect"

builder.add_conditional_edges("generate", should_continue)
builder.add_edge("reflect", "generate")
graph = builder.compile()
```

### Reflexion (LangGraph)

```python
MAX_ITERATIONS = 5
builder = MessageGraph()
builder.add_node("draft", first_responder.respond)
builder.add_node("execute_tools", execute_tools)
builder.add_node("revise", revisor.respond)

builder.add_edge("draft", "execute_tools")
builder.add_edge("execute_tools", "revise")

def event_loop(state):
    if _get_num_iterations(state) > MAX_ITERATIONS:
        return END
    return "execute_tools"

builder.add_conditional_edges("revise", event_loop)
builder.set_entry_point("draft")
graph = builder.compile()
```

### LATS (LangGraph)

```python
from langgraph.graph import END, StateGraph

class TreeState(TypedDict):
    root: Node       # 完整搜索树
    input: str       # 原始输入

def should_loop(state):
    root = state["root"]
    if root.is_solved:
        return END
    if root.height > 5:
        return END
    return "expand"

builder = StateGraph(TreeState)
builder.add_node("start", generate_initial_response)
builder.add_node("expand", expand)
builder.set_entry_point("start")
builder.add_conditional_edges("start", should_loop)
builder.add_conditional_edges("expand", should_loop)
graph = builder.compile()
```

---

## 为什么重要

反思机制回答了一个根本问题：**如何让 AI 系统的输出质量突破单次推理的天花板？**

在实际应用中，很多任务（写研究报告、解复杂代码题、做深度分析）都不是一次就能做好的。人类写论文也要反复修改，反思型 Agent 正是把这种"迭代改进"的能力赋予了 AI 系统。

从工程角度看，这三种架构形成了一个清晰的选择谱系：
- 简单任务、低延迟要求 -> 基础反思或不反思
- 需要事实准确性 -> Reflexion
- 复杂推理、容错要求高 -> LATS

---

## 延伸思考

1. **反思的收益递减**：反思迭代不是越多越好。经验表明，2-3轮反思通常就能获得大部分收益，之后的改进趋于平缓甚至引入新错误。如何动态决定"何时停止反思"是一个开放问题。

2. **反思 vs 搜索时计算 (Test-time Compute)**：反思本质上是一种 test-time compute 策略。OpenAI 的 o1 模型内置了链式推理，可以看作是把反思"编译"进了模型内部。外部反思架构和内置推理各有什么优劣？

3. **LATS 在代码生成中的天然优势**：代码任务有天然的评估函数——单元测试。LATS 可以根据测试通过率给每条路径打分，这让搜索过程获得了高质量的反馈信号，远比纯 LLM 打分可靠。

4. **轨迹记忆与微调**：保存好的推理轨迹可以作为微调数据，让模型在未来"一次就做对"。这意味着反思不仅是运行时的改进手段，更是持续学习的数据来源。

---

> 原文来源：LangChain Blog - Reflection Agents (2024-02-21)
