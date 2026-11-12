# Tool Calling with LangChain: 让大模型学会"打电话"调用工具

> **一句话总结：** LangChain 推出了标准化的工具调用接口（Tool Calling Interface），通过 `bind_tools()`、`AIMessage.tool_calls` 和 `create_tool_calling_agent()` 三个核心组件，让你用同一套代码调用 OpenAI、Anthropic、Gemini 等不同模型的工具能力。

---

## 核心要点

### 1. 为什么需要标准化工具调用

大模型本身只能生成文本，但工具调用（Tool Calling）让它能"伸出手"操作外部世界 -- 查数据库、调 API、执行计算。问题在于，各家模型提供商的工具调用接口都不一样：OpenAI 用一种格式，Anthropic 用另一种，Gemini 又是一种。如果你想换模型，就得重写一堆代码。LangChain 的标准化接口就是要解决这个问题：写一次，到处用。

### 2. 三大核心组件

| 组件 | 作用 | 类比 |
|---|---|---|
| `ChatModel.bind_tools()` | 告诉模型"你有哪些工具可用" | 给员工一份工具清单 |
| `AIMessage.tool_calls` | 从模型回复中提取"它想调用哪些工具" | 员工填写的工具申请单 |
| `create_tool_calling_agent()` | 构建一个能自动调用工具的 Agent | 雇一个会用工具的员工 |

### 3. bind_tools() -- 四种定义工具的方式

`bind_tools()` 的强大之处在于它接受多种格式的工具定义，你用哪种都行：

```
+---------------------+     +---------------------+
| Pydantic class      |     | LangChain @tool     |
| (类型安全，适合     | --> |  装饰器             |
|  复杂参数)          |     | (最简洁写法)        |
+---------------------+     +---------------------+
         |                            |
         v                            v
    +------------------------------------+
    |        bind_tools()                |
    |   统一转换为模型能理解的格式        |
    +------------------------------------+
         ^                            ^
         |                            |
+---------------------+     +---------------------+
| 普通 Python 函数    |     | OpenAI 格式 dict    |
| (零依赖)            |     | (兼容已有代码)      |
+---------------------+     +---------------------+
```

示例代码对比：

```python
# 方式1: Pydantic class
class multiply(BaseModel):
    """Return product of 'x' and 'y'."""
    x: float = Field(..., description="First factor")
    y: float = Field(..., description="Second factor")

# 方式2: @tool 装饰器
@tool
def exponentiate(x: float, y: float) -> float:
    """Raise 'x' to the 'y'."""
    return x**y

# 方式3: 普通函数
def subtract(x: float, y: float) -> float:
    """Subtract 'x' from 'y'."""
    return y - x

# 绑定到任意模型 -- 同一套工具定义
llm = ChatAnthropic(model="claude-3-sonnet-20240229")
llm_with_tools = llm.bind_tools([multiply, exponentiate, subtract])
```

### 4. AIMessage.tool_calls -- 标准化的输出

以前，不同模型返回工具调用的位置和格式都不同。有的放在 `additional_kwargs` 里，有的放在 `content` 里，你得写一堆 if-else 来处理。现在统一了：

```python
# 调用模型
response = llm_with_tools.invoke("what's 5 raised to 2.743?")

# 标准化提取 -- 不管底层是哪个模型
response.tool_calls
# -> [{'name': 'exponentiate', 'args': {'x': 5.0, 'y': 2.743}, 'id': '...'}]
```

`ToolCall` 的结构非常简洁：

| 字段 | 类型 | 含义 |
|---|---|---|
| `name` | `str` | 工具名称 |
| `args` | `Dict[str, Any]` | 调用参数 |
| `id` | `Optional[str]` | 调用唯一标识 |

### 5. bind_tools vs with_structured_output

这两个容易混淆，区别如下：

| 维度 | `bind_tools` | `with_structured_output` |
|---|---|---|
| 返回内容 | 文本 + 工具调用（可能0个或多个） | 强制返回指定结构 |
| 模型自由度 | 高 -- 模型自己决定调不调、调哪个 | 低 -- 必须按你的 schema 输出 |
| 适用场景 | Agent 应用（需要灵活决策） | 信息抽取（需要固定格式输出） |

---

## 类比理解

想象你经营一家餐厅。`bind_tools()` 就是你给厨师准备了一套厨具（锅、刀、烤箱）并告诉他"这些你都可以用"。厨师（大模型）收到顾客的点单后，自己决定用哪些厨具来做菜。`AIMessage.tool_calls` 就是厨师的操作记录 -- "我用了炒锅炒了青菜，用了烤箱烤了面包"。而 `with_structured_output` 更像是要求厨师必须用标准模具做出固定形状的饼干，没有发挥空间。

---

## 为什么重要

1. **真正的模型无关（Model-agnostic）：** 同一套业务代码可以无缝切换 OpenAI、Anthropic、Gemini、Mistral 等模型，不需要改工具调用逻辑。
2. **生态统一的基石：** `tool_calls` 是 LangChain 后来推出 `create_tool_calling_agent()` 和 LangGraph 的基础。没有标准化的工具调用，就没有标准化的 Agent 框架。
3. **降低迁移成本：** 当某个模型提供商涨价或性能退化时，你可以快速切换，而不是重写整个应用。

---

## 延伸思考

- **Tool Calling 不等于 Function Calling。** OpenAI 最初叫"Function Calling"，后来改名为"Tool Calling"。区别在于 Tool Calling 支持一次调用多个工具（并行调用），而早期的 Function Calling 一次只能调一个。
- **流式工具调用（Streaming Tool Calls）是更复杂的场景。** 当模型一边生成回复一边决定调用工具时，你需要处理 `tool_call_chunks` -- 这在实时对话场景中很关键。
- **标准化的下一步是 MCP（Model Context Protocol）。** 如果说 LangChain 的 `bind_tools` 统一了"模型调用工具"的接口，MCP 则试图统一"工具暴露给模型"的协议，两者是互补关系。

---

*原文来源：[Tool Calling with LangChain - LangChain Blog](https://www.langchain.com/blog/tool-calling-with-langchain) (2024-04-11)*
