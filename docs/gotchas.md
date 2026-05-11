# Web Page Building Gotchas

沉淀自 anthropic-engineering-learn 项目的 HTML 页面构建经验。

---

## 1. 页面架构模式

### 1.1 深度研究型页面（Deep-Dive）

适用于：需要保留文章全部核心内容、用可视化方式呈现的场景。

**固定结构：**
```
导航栏 (sticky nav)
  ↓
Hero 区（渐变背景 + 关键数字卡片）
  ↓
目录导航 (TOC)
  ↓
Section 1~N（每个 section = h2 + lead + 内容块）
  ↓
Footer
```

**关键设计要素：**
- 导航栏：`position:sticky` + `backdrop-filter:blur`
- Hero：`linear-gradient` 深色背景 + 4 个关键数字卡片
- TOC：grid 布局的编号链接
- Section：`h2` 带 emoji + `lead` 灰色引导文字
- 内容块：`.card` / `.compare-grid` / `.chart` / `.timeline` / `.fail-grid`

### 1.2 速读卡片页面（Quick-Read）

适用于：30 秒快速了解核心内容的场景。

**固定结构：**
```
TL;DR 一句话卡片
  ↓
4 个关键数字
  ↓
5 步流程（编号圆圈 + 描述）
  ↓
对比卡片 / 核心启示
```

---

## 2. CSS 设计系统

### 2.1 CSS Variables（必用）

```css
:root {
  --bg: #fafbfc;           /* 页面背景 */
  --surface: #fff;         /* 卡片背景 */
  --text: #0f172a;         /* 主文字 */
  --text-secondary: #64748b; /* 次要文字 */
  --border: #e2e8f0;       /* 边框 */
  --radius: 14px;          /* 圆角 */
  --purple: #6366f1;       /* 主色调 */
  --teal: #14b8a6;         /* 次色调（每篇文章可换） */
  --amber: #f59e0b;
  --green: #10b981;
  --red: #ef4444;
  --blue: #3b82f6;
  --mono: 'JetBrains Mono', monospace;
  --sans: 'Noto Sans SC', 'Inter', sans-serif;
}
```

### 2.2 字体栈

```css
font-family: 'Noto Sans SC', 'Inter', system-ui, sans-serif;
```
- 中文内容用 `Noto Sans SC`
- 英文/数字用 `Inter`
- 代码用 `JetBrains Mono`
- Google Fonts 引入（带 `&display=swap`）

### 2.3 Hero 渐变配色方案

每篇文章换一个主色调：

| 主题 | 渐变 |
|------|------|
| BrowseComp（紫色系） | `#0f172a → #1e1b4b → #312e81` |
| Demystifying Evals（青色系） | `#0f172a → #134e4a → #0f766e` |
| 通用 | `#0f172a → #1e293b → #0f172a` |

---

## 3. 常用可视化组件

### 3.1 柱状图（Chart）

```html
<div class="chart">
  <div class="chart-row">
    <div class="chart-label">标签</div>
    <div class="chart-bar-wrap">
      <div class="chart-bar purple" style="width:80%">80%</div>
    </div>
  </div>
</div>
```
- `.purple` / `.amber` / `.green` / `.red` / `.blue` / `.teal` / `.pink`
- `width` 用百分比控制长度
- `chart-bar` 自带渐变

### 3.2 时间线（Timeline）

```html
<div class="timeline">
  <div class="tl-item">
    <div class="tl-dot"></div>
    <div class="tl-phase">阶段名</div>
    <div class="tl-token">附加信息</div>
    <div class="tl-desc">描述</div>
  </div>
</div>
```
- 自动用渐变色点（前 5 个子项各有不同颜色）
- `::before` 生成左侧渐变竖线

### 3.3 对比卡片（Compare Grid）

```html
<div class="compare-grid">
  <div class="compare-card old">红色边框（❌ 负面）</div>
  <div class="compare-card new">蓝色边框（✅ 正面）</div>
</div>
```
- 响应式：移动端自动变单列

### 3.4 流程图（Flow Diagram）

```html
<div class="flow">
  <div class="flow-step">步骤 1</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step purple">步骤 2</div>
</div>
```
- `.purple` 变紫色步骤
- 移动端自动变纵向

### 3.5 网格卡片（Grid Cards）

```html
<div class="fail-grid">     <!-- 3 列 -->
<div class="agent-grid">    <!-- 2 列 -->
<div class="method-grid">   <!-- 自动填充 -->
```

### 3.6 引用块（Blockquote）

```html
<div class="block-q">
  <p>"引用文字"</p>
</div>
```

### 3.7 标签（Badge）

```html
<span class="badge badge-purple">标签</span>
<span class="badge badge-amber">标签</span>
<span class="badge badge-green">标签</span>
<span class="badge badge-red">标签</span>
<span class="badge badge-blue">标签</span>
<span class="badge badge-teal">标签</span>
```

### 3.8 进度条

```html
<div class="progress-bar"><div class="fill" style="width:60%"></div></div>
```

---

## 4. 响应式适配

**必加断点：**
```css
@media(max-width:768px) {
  .compare-grid, .pass-chart, .agent-grid, .fail-grid {
    grid-template-columns: 1fr;
  }
  .chart-label { width: 120px; font-size: 12px; }
  .flow { flex-direction: column; gap: 8px; }
  .flow-arrow { transform: rotate(90deg); }
  .toc-grid { grid-template-columns: 1fr; }
}
```

---

## 5. 文件组织

```
docs/
├── assets/
│   └── style.css          ← 共享样式（首页用）
├── index.html             ← 首页（使用 assets/style.css）
└── evals/
    ├── eval-awareness-browsecomp.html      ← 深度页（内联 style）
    └── demystifying-evals-for-ai-agents.html ← 深度页（内联 style）
```

**⚠️ Gotcha**: 深度研究型页面使用**内联 `<style>`**，不依赖共享 CSS。因为每个页面有独特的配色和组件。共享 CSS 只用于首页。

---

## 6. 常见陷阱

### 6.1 edit 工具匹配失败
- 如果用 `edit` 修改文件，`oldText` 必须与文件内容**完全匹配**（包括空格和换行）
- 如果不确定，先用 `read` 确认当前内容
- 首页 index.html 容易被多次修改后内容不同步

### 6.2 中文渲染
- 必须引入 `Noto Sans SC` 字体
- `font-family` 中 `Noto Sans SC` 要放在 `Inter` 前面（对中文内容）

### 6.3 GitHub Pages 缓存
- 推送后需要等待 1-3 分钟部署
- 浏览器可能需要 `Cmd+Shift+R` 强制刷新
- 国内访问 GitHub Pages 可能不稳定

### 6.4 图片引用
- 原文中的图片 URL 是 Anthropic CDN 的相对路径
- 在静态页面中要么下载图片到本地，要么用完整 URL
- 当前策略：**不用原文图片**，用 CSS 可视化替代

### 6.5 代码块渲染
- 用 `<pre>` 或自定义 `.code-block` / `.canary` 类
- 避免用默认的 `<code>` 标签包裹多行代码

### 6.6 表格溢出
- 所有表格必须包在 `.tbl-wrap { overflow-x: auto }` 中
- 移动端表格会横向滚动

---

## 7. 页面构建 Checklist

- [ ] Hero 区：渐变背景 + 标题 + 副标题 + 4 个关键数字
- [ ] TOC 导航：所有章节链接
- [ ] 每个 Section：h2（带 emoji）+ lead（灰色引导）
- [ ] 至少 3 种可视化（图表/时间线/对比卡片/流程图等）
- [ ] 原文关键引用用 `.block-q` 呈现
- [ ] 响应式适配（768px 断点）
- [ ] Footer 带返回链接和原始来源
- [ ] 内联 style（不依赖外部 CSS）
- [ ] Google Fonts 引入（Noto Sans SC + Inter + JetBrains Mono）
- [ ] 更新 index.html 标记为 Done

---

## 8. 模板骨架

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>深度解析：文章标题</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* CSS Variables + Reset */
    /* Nav + Hero + Page layout */
    /* TOC + Section + Card */
    /* Chart + Timeline + Compare + Flow + Grid */
    /* Table + Badge + Quote + Footer */
    /* Responsive @media */
  </style>
</head>
<body>
  <nav class="nav">...</nav>
  <header class="hero">...</header>
  <div class="page">
    <nav class="toc">...</nav>
    <section class="section" id="s1">...</section>
    <!-- ... more sections ... -->
  </div>
  <footer class="footer">...</footer>
</body>
</html>
```
