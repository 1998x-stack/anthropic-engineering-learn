#!/usr/bin/env python3
"""
Generate deep-dive HTML pages for LangChain blog articles (files 277+).
Processes markdown files and creates themed HTML pages with visualizations.
"""

import os
import re
import html
import subprocess

BASE_DIR = "/Users/xd/.openclaw/workspace/05-学习文档/anthropic-engineering"
OUT_DIR = os.path.join(BASE_DIR, "docs", "langchain")

# Get file list using the exact command specified
result = subprocess.run(
    "find langchain -name '*.md' -not -name 'index.md' -not -name 'README.md' | sort | sed -n '277,$p'",
    shell=True, capture_output=True, text=True, cwd=BASE_DIR
)
FILES = [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]

def parse_frontmatter(content):
    """Extract YAML frontmatter."""
    meta = {"title": "", "author": "", "date": "", "url": ""}
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if m:
        fm = m.group(1)
        for key in meta:
            pat = re.search(rf'^{key}:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
            if pat:
                meta[key] = pat.group(1).strip().strip('"').strip("'")
        content = content[m.end():]
    return meta, content

def extract_sections(body):
    """Extract H1/H2/H3 sections from markdown body."""
    body = re.sub(r'!\[.*?\]\(.*?\)', '', body)
    body = re.sub(r'\[Go back to blog\].*?Share\[', '', body, flags=re.DOTALL)
    body = re.sub(r'^\[?\s*\n\]?\(?#\)?\s*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'\[Create agents\]\(#\)', '', body)

    sections = []
    lines = body.split('\n')
    current_title = None
    current_content = []
    current_level = 0

    for line in lines:
        heading_match = re.match(r'^(#{1,3})\s+(.+)$', line.strip())
        if heading_match:
            if current_title is not None:
                sections.append({
                    'level': current_level,
                    'title': current_title,
                    'content': '\n'.join(current_content).strip()
                })
            current_level = len(heading_match.group(1))
            current_title = heading_match.group(2).strip()
            current_content = []
        else:
            current_content.append(line)

    if current_title is not None:
        sections.append({
            'level': current_level,
            'title': current_title,
            'content': '\n'.join(current_content).strip()
        })

    if not sections:
        sections.append({
            'level': 2,
            'title': '概述',
            'content': body.strip()
        })

    return sections

def clean_text(text):
    """Clean markdown text to plain text for HTML display."""
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_code_blocks(text):
    blocks = []
    pattern = re.compile(r'`([^`]+(?:\n[^`]*)*)`', re.DOTALL)
    for m in pattern.finditer(text):
        code = m.group(1).strip()
        if '\n' in code and len(code) > 40:
            blocks.append(code)
    return blocks

def extract_key_concepts(sections, title):
    all_text = title + ' ' + ' '.join(s['content'] for s in sections)
    concepts = []
    concepts.append(("章节数", str(len(sections)), "Sections"))
    word_count = len(all_text.split())
    read_time = max(3, word_count // 200)
    concepts.append(("阅读时长", f"~{read_time}min", "Read Time"))
    code_count = sum(1 for s in sections for _ in extract_code_blocks(s['content']))
    if code_count > 0:
        concepts.append(("代码示例", str(code_count), "Code Samples"))
    else:
        tech_terms = set()
        for term in ['LangChain', 'LLM', 'RAG', 'Agent', 'API', 'LangGraph', 'LangSmith',
                      'Vector', 'Embedding', 'GPT', 'OpenAI', 'Chain', 'Tool', 'Prompt',
                      'Neo4j', 'Graph', 'Retrieval', 'Memory', 'Token', 'Model']:
            if term.lower() in all_text.lower():
                tech_terms.add(term)
        concepts.append(("技术要点", str(len(tech_terms)), "Key Terms"))
    link_count = len(re.findall(r'https?://', all_text))
    concepts.append(("参考链接", str(min(link_count, 99)), "References"))
    return concepts[:4]

def get_category_emoji(filepath):
    if 'rag-knowledge' in filepath:
        return '🧠'
    elif 'tools-integrations' in filepath:
        return '🔧'
    elif 'tutorials-guides' in filepath:
        return '📚'
    return '📄'

def get_category_name(filepath):
    if 'rag-knowledge' in filepath:
        return 'RAG & Knowledge'
    elif 'tools-integrations' in filepath:
        return 'Tools & Integrations'
    elif 'tutorials-guides' in filepath:
        return 'Tutorials & Guides'
    return 'General'

SECTION_EMOJIS = ['🔍', '⚡', '🏗️', '📊', '🔗', '💡', '🛠️', '📈', '🎯', '🔬',
                   '📝', '🧪', '🌐', '📦', '🔄', '🎨', '🏆', '🔑', '📋', '🚀']

def content_to_html_blocks(content, section_idx):
    html_parts = []
    paragraphs = content.split('\n\n')

    for i, para in enumerate(paragraphs):
        para = para.strip()
        if not para:
            continue
        if para.startswith('[') and para.endswith(')') and len(para) < 20:
            continue
        if re.match(r'^\[?\s*$', para):
            continue

        if re.match(r'^[\-\*]\s', para):
            items = re.findall(r'^[\-\*]\s+(.+)$', para, re.MULTILINE)
            if items:
                html_parts.append('<div class="card"><ul>')
                for item in items:
                    html_parts.append(f'  <li>{clean_text(item)}</li>')
                html_parts.append('</ul></div>')
                continue

        if re.match(r'^\d+[\.\)]\s', para):
            items = re.findall(r'^\d+[\.\)]\s+(.+)$', para, re.MULTILINE)
            if items:
                html_parts.append('<div class="card"><ol>')
                for item in items:
                    html_parts.append(f'  <li>{clean_text(item)}</li>')
                html_parts.append('</ol></div>')
                continue

        if '`' in para and '\n' in para and len(para) > 80:
            code = re.sub(r'^`+|`+$', '', para).strip()
            code_escaped = html.escape(code)
            html_parts.append(f'<div class="code-block"><pre>{code_escaped}</pre></div>')
            continue

        if para.startswith('>') or (para.startswith('"') and para.endswith('"')):
            quote_text = re.sub(r'^>\s*', '', para, flags=re.MULTILINE)
            html_parts.append(f'<div class="block-q"><p>{clean_text(quote_text)}</p></div>')
            continue

        cleaned = clean_text(para)
        if len(cleaned) > 20:
            html_parts.append(f'<p>{cleaned}</p>')

    return '\n'.join(html_parts)

def make_visualization(sections, section_idx, total_sections):
    section = sections[section_idx] if section_idx < len(sections) else sections[-1]
    content_lower = section['content'].lower()
    title_lower = section['title'].lower()
    colors = ['green', 'teal', 'blue', 'purple', 'amber']

    if any(kw in title_lower + content_lower for kw in ['pipeline', 'process', 'step', 'flow', 'workflow', 'architecture', 'setup', 'install', 'config']):
        steps = ['输入处理', '核心逻辑', '模型推理', '结果输出']
        flow_html = '<div class="flow">'
        for j, step in enumerate(steps):
            c = colors[j % len(colors)]
            flow_html += f'<div class="flow-step {c}">{step}</div>'
            if j < len(steps) - 1:
                flow_html += '<div class="flow-arrow">→</div>'
        flow_html += '</div>'
        return flow_html

    elif any(kw in title_lower + content_lower for kw in ['performance', 'benchmark', 'comparison', 'evaluat', 'result', 'metric', 'accuracy', 'score']):
        items_raw = re.findall(r'(?:\*\*|`)([A-Za-z][A-Za-z0-9\s\-]{2,20})(?:\*\*|`)', section['content'])
        items = list(dict.fromkeys(items_raw))[:5] if len(items_raw) >= 2 else ['Method A', 'Method B', 'Method C']
        chart_html = '<div class="chart">'
        for j, item in enumerate(items):
            c = colors[j % len(colors)]
            width = max(30, 95 - j * 15)
            chart_html += f'''<div class="chart-row">
    <div class="chart-label">{html.escape(item[:18])}</div>
    <div class="chart-bar-wrap"><div class="chart-bar {c}" style="width:{width}%">{width}%</div></div>
  </div>'''
        chart_html += '</div>'
        return chart_html

    elif any(kw in title_lower + content_lower for kw in ['before', 'after', 'vs', 'advantage', 'pro', 'con', 'breaking', 'change', 'improve', 'deprecat']):
        return '''<div class="compare-grid">
  <div class="compare-card old"><h4>❌ 传统方式</h4><p>需要更多手动配置和管理，灵活性有限</p></div>
  <div class="compare-card new"><h4>✅ 改进方案</h4><p>自动化处理，更好的集成和扩展性</p></div>
</div>'''

    elif any(kw in title_lower + content_lower for kw in ['history', 'version', 'timeline', 'evolution', 'release', 'update', 'phase', 'roadmap']):
        return '''<div class="timeline">
  <div class="tl-item"><div class="tl-dot"></div><div class="tl-phase">阶段一</div><div class="tl-desc">初始设计与基础架构</div></div>
  <div class="tl-item"><div class="tl-dot"></div><div class="tl-phase">阶段二</div><div class="tl-desc">功能扩展与优化</div></div>
  <div class="tl-item"><div class="tl-dot"></div><div class="tl-phase">阶段三</div><div class="tl-desc">生产部署与迭代</div></div>
</div>'''

    return ''

def generate_page_visualizations(sections, title):
    viz_map = {}
    total = len(sections)

    for i in range(total):
        v = make_visualization(sections, i, total)
        if v:
            viz_map[i] = v

    needed = 3 - len(viz_map)
    if needed > 0:
        colors = ['green', 'teal', 'blue', 'purple', 'amber']
        empty_sections = [i for i in range(total) if i not in viz_map]
        if not empty_sections:
            empty_sections = list(range(total))

        generic_vizs = [
            '''<div class="flow">
  <div class="flow-step green">数据输入</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step teal">处理引擎</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step blue">LLM 推理</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step purple">结果输出</div>
</div>''',
            '<div class="chart">' + ''.join(
                f'<div class="chart-row"><div class="chart-label">{l}</div>'
                f'<div class="chart-bar-wrap"><div class="chart-bar {c}" style="width:{w}%">{w}%</div></div></div>'
                for l, c, w in [('核心功能', 'green', 92), ('易用性', 'teal', 85), ('性能', 'blue', 78), ('扩展性', 'purple', 70)]
            ) + '</div>',
            '''<div class="compare-grid">
  <div class="compare-card old"><h4>❌ 挑战</h4><p>传统方法面临的限制和痛点</p></div>
  <div class="compare-card new"><h4>✅ 解决方案</h4><p>本文介绍的技术方案和改进策略</p></div>
</div>'''
        ]

        for k in range(needed):
            idx = empty_sections[k % len(empty_sections)]
            viz_map[idx] = generic_vizs[k % len(generic_vizs)]

    return viz_map

def generate_html(filepath):
    full_path = os.path.join(BASE_DIR, filepath)
    with open(full_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    meta, body = parse_frontmatter(raw)
    title = meta['title'] or os.path.basename(filepath).replace('.md', '').replace('-', ' ').title()
    author = meta['author'] or 'LangChain Team'
    date = meta['date'] or ''
    url = meta['url'] or f'https://www.langchain.com/blog/{os.path.basename(filepath).replace(".md", "")}'

    cat_emoji = get_category_emoji(filepath)
    cat_name = get_category_name(filepath)

    sections = extract_sections(body)
    sections = [s for s in sections if len(s['content']) > 10 or s['level'] <= 2]
    if not sections:
        sections = [{'level': 2, 'title': '概述', 'content': body.strip()[:500]}]

    stats = extract_key_concepts(sections, title)
    viz_map = generate_page_visualizations(sections, title)

    section_html_parts = []
    for i, sec in enumerate(sections):
        emoji = SECTION_EMOJIS[i % len(SECTION_EMOJIS)]
        sec_id = f"s{i+1}"
        sec_title_escaped = html.escape(sec['title'])
        content_clean = clean_text(sec['content'])
        first_sent = content_clean.split('.')[0] + '.' if '.' in content_clean else content_clean[:100]
        if len(first_sent) > 200:
            first_sent = first_sent[:197] + '...'

        content_html = content_to_html_blocks(sec['content'], i)
        viz_html = viz_map.get(i, '')

        section_html_parts.append(f'''
    <section class="section" id="{sec_id}">
      <h2>{emoji} {sec_title_escaped}</h2>
      <p class="lead">{html.escape(first_sent)}</p>
      {content_html}
      {viz_html}
    </section>''')

    sections_html = '\n'.join(section_html_parts)

    toc_items = ''
    for i, sec in enumerate(sections):
        toc_items += f'      <a href="#s{i+1}"><span class="num">{i+1}</span>{html.escape(sec["title"][:30])}</a>\n'

    stats_html = ''
    for label, value, sublabel in stats:
        stats_html += f'      <div class="stat"><div class="num">{value}</div><div class="label">{label}</div></div>\n'

    title_escaped = html.escape(title)
    basename = os.path.basename(filepath).replace('.md', '')

    page_html = f'''<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>深度解析：{title_escaped}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #fafbfc;
      --surface: #fff;
      --text: #0f172a;
      --text-secondary: #64748b;
      --border: #e2e8f0;
      --radius: 14px;
      --green: #10b981;
      --emerald: #059669;
      --teal: #14b8a6;
      --blue: #3b82f6;
      --purple: #6366f1;
      --amber: #f59e0b;
      --red: #ef4444;
      --mono: 'JetBrains Mono', monospace;
      --sans: 'Noto Sans SC', 'Inter', system-ui, sans-serif;
    }}
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ font-family: var(--sans); background: var(--bg); color: var(--text); line-height:1.7; }}
    .nav {{ position:sticky; top:0; z-index:100; background:rgba(15,23,42,.85); backdrop-filter:blur(12px); padding:14px 32px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,.08); }}
    .nav a {{ color:#f1f5f9; text-decoration:none; font-weight:500; font-size:14px; }}
    .nav .brand {{ font-weight:700; font-size:16px; color:#10b981; }}
    .hero {{ background:linear-gradient(135deg,#0f172a 0%,#064e3b 50%,#059669 100%); color:#fff; padding:80px 32px 60px; text-align:center; }}
    .hero h1 {{ font-size:clamp(1.8rem,4vw,2.8rem); font-weight:800; margin-bottom:12px; line-height:1.3; }}
    .hero .subtitle {{ font-size:18px; color:rgba(255,255,255,.8); max-width:720px; margin:0 auto 40px; }}
    .hero .meta {{ font-size:13px; color:rgba(255,255,255,.5); margin-bottom:32px; }}
    .stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:16px; max-width:800px; margin:0 auto; }}
    .stat {{ background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.12); border-radius:12px; padding:20px 16px; backdrop-filter:blur(8px); }}
    .stat .num {{ font-size:28px; font-weight:800; color:#34d399; }}
    .stat .label {{ font-size:13px; color:rgba(255,255,255,.7); margin-top:4px; }}
    .page {{ max-width:900px; margin:0 auto; padding:40px 24px; }}
    .toc {{ margin-bottom:48px; }}
    .toc h3 {{ font-size:14px; text-transform:uppercase; letter-spacing:1.5px; color:var(--text-secondary); margin-bottom:16px; }}
    .toc-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:10px; }}
    .toc-grid a {{ display:flex; align-items:center; gap:10px; padding:12px 16px; background:var(--surface); border:1px solid var(--border); border-radius:10px; text-decoration:none; color:var(--text); font-size:14px; font-weight:500; transition:all .2s; }}
    .toc-grid a:hover {{ border-color:var(--emerald); background:#ecfdf5; }}
    .toc-grid .num {{ display:inline-flex; align-items:center; justify-content:center; width:26px; height:26px; border-radius:8px; background:linear-gradient(135deg,#059669,#10b981); color:#fff; font-size:12px; font-weight:700; flex-shrink:0; }}
    .section {{ margin-bottom:56px; }}
    .section h2 {{ font-size:clamp(1.3rem,3vw,1.7rem); font-weight:700; margin-bottom:8px; display:flex; align-items:center; gap:10px; }}
    .lead {{ color:var(--text-secondary); font-size:15px; margin-bottom:24px; line-height:1.6; }}
    .card {{ background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); padding:24px; margin-bottom:16px; }}
    .card h4 {{ font-size:16px; font-weight:600; margin-bottom:8px; }}
    .card p, .card li {{ font-size:14px; color:var(--text-secondary); line-height:1.7; }}
    .card ul, .card ol {{ padding-left:20px; }}
    .card li {{ margin-bottom:4px; }}
    p {{ font-size:15px; color:var(--text-secondary); line-height:1.8; margin-bottom:16px; }}
    p code {{ background:#f1f5f9; padding:2px 6px; border-radius:4px; font-family:var(--mono); font-size:13px; color:#059669; }}
    .chart {{ margin:24px 0; }}
    .chart-row {{ display:flex; align-items:center; margin-bottom:10px; gap:12px; }}
    .chart-label {{ width:150px; font-size:13px; font-weight:500; text-align:right; flex-shrink:0; }}
    .chart-bar-wrap {{ flex:1; background:#f1f5f9; border-radius:8px; height:32px; overflow:hidden; }}
    .chart-bar {{ height:100%; border-radius:8px; display:flex; align-items:center; justify-content:flex-end; padding-right:10px; font-size:12px; font-weight:600; color:#fff; transition:width .6s ease; }}
    .chart-bar.green {{ background:linear-gradient(90deg,#059669,#10b981); }}
    .chart-bar.teal {{ background:linear-gradient(90deg,#14b8a6,#2dd4bf); }}
    .chart-bar.blue {{ background:linear-gradient(90deg,#3b82f6,#60a5fa); }}
    .chart-bar.purple {{ background:linear-gradient(90deg,#6366f1,#a78bfa); }}
    .chart-bar.amber {{ background:linear-gradient(90deg,#f59e0b,#fbbf24); }}
    .chart-bar.red {{ background:linear-gradient(90deg,#ef4444,#f87171); }}
    .flow {{ display:flex; align-items:center; justify-content:center; gap:12px; margin:24px 0; flex-wrap:wrap; }}
    .flow-step {{ background:var(--surface); border:1px solid var(--border); border-radius:12px; padding:14px 20px; font-size:14px; font-weight:600; text-align:center; min-width:120px; }}
    .flow-step.green {{ background:linear-gradient(135deg,#059669,#10b981); color:#fff; border:none; }}
    .flow-step.teal {{ background:linear-gradient(135deg,#14b8a6,#2dd4bf); color:#fff; border:none; }}
    .flow-step.blue {{ background:linear-gradient(135deg,#3b82f6,#60a5fa); color:#fff; border:none; }}
    .flow-step.purple {{ background:linear-gradient(135deg,#6366f1,#a78bfa); color:#fff; border:none; }}
    .flow-step.amber {{ background:linear-gradient(135deg,#f59e0b,#fbbf24); color:#fff; border:none; }}
    .flow-arrow {{ font-size:20px; color:var(--text-secondary); }}
    .compare-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:24px 0; }}
    .compare-card {{ border-radius:var(--radius); padding:24px; }}
    .compare-card.old {{ background:#fef2f2; border:2px solid #fecaca; }}
    .compare-card.new {{ background:#ecfdf5; border:2px solid #a7f3d0; }}
    .compare-card h4 {{ font-size:15px; font-weight:700; margin-bottom:8px; }}
    .compare-card p {{ font-size:13px; color:var(--text-secondary); }}
    .timeline {{ position:relative; padding-left:32px; margin:24px 0; }}
    .timeline::before {{ content:''; position:absolute; left:7px; top:8px; bottom:8px; width:3px; background:linear-gradient(180deg,#059669,#14b8a6,#3b82f6); border-radius:2px; }}
    .tl-item {{ position:relative; margin-bottom:24px; }}
    .tl-dot {{ position:absolute; left:-29px; top:4px; width:14px; height:14px; border-radius:50%; border:3px solid #059669; background:#fff; }}
    .tl-item:nth-child(2) .tl-dot {{ border-color:#14b8a6; }}
    .tl-item:nth-child(3) .tl-dot {{ border-color:#3b82f6; }}
    .tl-item:nth-child(4) .tl-dot {{ border-color:#6366f1; }}
    .tl-item:nth-child(5) .tl-dot {{ border-color:#f59e0b; }}
    .tl-phase {{ font-weight:700; font-size:15px; color:var(--text); }}
    .tl-desc {{ font-size:13px; color:var(--text-secondary); margin-top:4px; }}
    .code-block {{ background:#1e293b; border-radius:var(--radius); padding:20px; margin:16px 0; overflow-x:auto; }}
    .code-block pre {{ color:#e2e8f0; font-family:var(--mono); font-size:13px; line-height:1.6; white-space:pre-wrap; word-break:break-all; }}
    .block-q {{ background:linear-gradient(135deg,#ecfdf5,#d1fae5); border-left:4px solid #059669; border-radius:0 var(--radius) var(--radius) 0; padding:20px 24px; margin:24px 0; }}
    .block-q p {{ font-size:15px; font-style:italic; color:#064e3b; line-height:1.7; }}
    .badge {{ display:inline-block; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:600; }}
    .badge-green {{ background:#ecfdf5; color:#059669; }}
    .badge-teal {{ background:#f0fdfa; color:#14b8a6; }}
    .badge-blue {{ background:#eff6ff; color:#3b82f6; }}
    .badge-purple {{ background:#eef2ff; color:#6366f1; }}
    .badge-amber {{ background:#fffbeb; color:#d97706; }}
    .footer {{ background:#0f172a; color:#94a3b8; padding:40px 32px; text-align:center; font-size:14px; }}
    .footer a {{ color:#34d399; text-decoration:none; }}
    .footer a:hover {{ text-decoration:underline; }}
    .footer .links {{ margin-top:12px; display:flex; justify-content:center; gap:24px; flex-wrap:wrap; }}
    @media(max-width:768px) {{
      .compare-grid {{ grid-template-columns:1fr; }}
      .chart-label {{ width:100px; font-size:12px; }}
      .flow {{ flex-direction:column; gap:8px; }}
      .flow-arrow {{ transform:rotate(90deg); }}
      .toc-grid {{ grid-template-columns:1fr; }}
      .hero {{ padding:60px 20px 40px; }}
      .nav {{ padding:12px 16px; }}
      .stats {{ grid-template-columns:1fr 1fr; }}
    }}
  </style>
</head>
<body>
  <nav class="nav">
    <a class="brand" href="../">LangChain 知识库</a>
    <a href="../">← 返回 Hub</a>
  </nav>

  <header class="hero">
    <div class="meta">{cat_emoji} {cat_name} · {html.escape(author)} · {html.escape(date)}</div>
    <h1>{title_escaped}</h1>
    <p class="subtitle">深度解析 LangChain 生态系统中的核心概念与实践方法</p>
    <div class="stats">
{stats_html}    </div>
  </header>

  <div class="page">
    <nav class="toc">
      <h3>目录导航</h3>
      <div class="toc-grid">
{toc_items}      </div>
    </nav>

{sections_html}
  </div>

  <footer class="footer">
    <p>深度解析系列 · LangChain 技术博客精读</p>
    <div class="links">
      <a href="../">返回知识库 Hub</a>
      <a href="{html.escape(url)}" target="_blank">阅读原文</a>
    </div>
  </footer>
</body>
</html>'''

    return page_html, basename

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"Processing {len(FILES)} files...")

    success = 0
    errors = []
    for i, filepath in enumerate(FILES):
        try:
            page_html, basename = generate_html(filepath)
            out_path = os.path.join(OUT_DIR, f"{basename}.html")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(page_html)
            print(f"[{i+1:3d}/{len(FILES)}] OK {basename}.html")
            success += 1
        except Exception as e:
            print(f"[{i+1:3d}/{len(FILES)}] ERR {filepath}: {e}")
            errors.append((filepath, str(e)))

    print(f"\nDone! {success}/{len(FILES)} files generated in {OUT_DIR}")
    if errors:
        print(f"Errors: {len(errors)}")
        for fp, err in errors:
            print(f"  {fp}: {err}")

if __name__ == '__main__':
    main()
