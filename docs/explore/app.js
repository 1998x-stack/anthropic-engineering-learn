"use strict";

(function () {
  const ROOT = "https://github.com/1998x-stack/anthropic-engineering-learn/blob/main/";
  const $ = (id) => document.getElementById(id);
  const pageSize = 24;
  const kinds = {source_article: "SOURCE", article_note: "RESEARCH", paper: "PAPER"};
  const references = {
    matched: "已按 URL 对齐",
    linked_by_id_url_mismatch: "已有 ID 关联，URL 不一致",
    external_only: "仅有外部原文引用",
    no_explicit_citation: "缺少明确原文 URL",
    ambiguous: "来源存在歧义"
  };
  const filters = ["source", "kind", "topic", "visibility", "reference"];
  const state = {data: null, byId: new Map(), inbound: new Map(), shown: 0, matches: []};

  function element(tag, className, text) {
    const result = document.createElement(tag);
    if (className) result.className = className;
    if (text !== undefined && text !== null) result.textContent = String(text);
    return result;
  }
  function safeExternal(raw) {
    try {
      const u = new URL(raw);
      return u.protocol === "https:" ? u.href : null;
    } catch (_) {
      return null;
    }
  }
  function encodedPath(path) {
    return String(path).split("/").map(encodeURIComponent).join("/");
  }
  function githubFile(path) {
    return ROOT + encodedPath(path);
  }
  function linkFor(item) {
    const page = item.site_path;
    if (typeof page === "string" && page.startsWith("docs/")) {
      return "../" + encodedPath(page.substring(5));
    }
    return githubFile(item.content_path);
  }
  function externalAnchor(label, raw, className) {
    const href = safeExternal(raw);
    if (!href) return null;
    const a = element("a", className, label);
    a.href = href;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    return a;
  }
  function normal(value) {
    return String(value || "").normalize("NFKC").toLocaleLowerCase();
  }
  function topicLabel(id) {
    const t = (state.data.topics || []).find((x) => x.id === id);
    return t ? t.label_zh : id;
  }
  function hasLocalSource(item) {
    return (item.related_ids || []).some((id) => id.startsWith("source:") || id.startsWith("paper:"));
  }
  function matchesFilters(item, tokens) {
    if ($("source").value && item.source !== $("source").value) return false;
    if ($("kind").value && item.kind !== $("kind").value) return false;
    if ($("topic").value && !(item.topics || []).includes($("topic").value)) return false;
    if ($("visibility").value && item.publication_status !== $("visibility").value) return false;
    const ref = $("reference").value;
    if (ref) {
      if (item.kind !== "article_note") return false;
      if (ref === "unlinked") {
        if (hasLocalSource(item)) return false;
      } else if (item.reference_status !== ref) {
        return false;
      }
    }
    if (!tokens.length) return true;
    const text = normal([item.title, item.id, item.summary, item.source, item.author,
      item.published_at, ...(item.topics || []).map(topicLabel)].join(" "));
    return tokens.every((term) => text.includes(term));
  }
  function score(item, tokens) {
    if (!tokens.length) return item.kind === "article_note" ? 2 : item.kind === "source_article" ? 1 : 0;
    const title = normal(item.title), id = normal(item.id), summary = normal(item.summary);
    const topics = normal((item.topics || []).map(topicLabel).join(" "));
    return tokens.reduce((score, term) => score +
      (title.includes(term) ? 12 : 0) + (id.includes(term) ? 6 : 0) +
      (topics.includes(term) ? 4 : 0) + (summary.includes(term) ? 2 : 0), 0);
  }
  function syncURL() {
    const params = new URLSearchParams();
    if ($("search").value.trim()) params.set("q", $("search").value.trim());
    filters.forEach((id) => { if ($(id).value) params.set(id, $(id).value); });
    if (!$("detail").hidden && $("detail").dataset.selected) params.set("id", $("detail").dataset.selected);
    window.history.replaceState(null, "", window.location.pathname +
      (params.toString() ? "?" + params.toString() : ""));
  }
  function count(n) {
    return new Intl.NumberFormat("zh-CN").format(n || 0);
  }
  function makeCard(item) {
    const card = element("article", "result-card");
    const meta = element("div", "meta-line");
    const type = element("span", "kind " + item.kind, kinds[item.kind] || item.kind);
    meta.append(type, element("span", "", item.source.toUpperCase()),
      element("span", "", item.publication_status === "published" ? "可网页阅读" : "GitHub 原文件"));
    if (item.published_at) meta.append(element("span", "", item.published_at));
    card.append(meta);
    const heading = element("h3");
    const title = element("a", "", item.title);
    title.href = linkFor(item);
    heading.append(title);
    card.append(heading);
    if (item.summary) card.append(element("p", "summary", item.summary));
    const tags = element("div", "tag-row");
    for (const topic of item.topics || []) tags.append(element("span", "topic", topicLabel(topic)));
    if (item.kind === "article_note" && !hasLocalSource(item)) {
      tags.append(element("span", "ref-warning", "来源待关联"));
    }
    card.append(tags);
    const actions = element("div", "result-actions");
    const read = element("a", "small-link",
      item.publication_status === "published" ? "阅读网页 ↗" : "查看 Markdown ↗");
    read.href = linkFor(item);
    const detail = element("button", "", "证据与关联 →");
    detail.type = "button";
    detail.addEventListener("click", () => showDetail(item.id, true));
    actions.append(read, detail);
    card.append(actions);
    return card;
  }
  function renderPage() {
    const list = $("result-list");
    const take = state.matches.slice(state.shown, state.shown + pageSize);
    const fragment = document.createDocumentFragment();
    for (const item of take) fragment.append(makeCard(item));
    list.append(fragment);
    state.shown += take.length;
    $("load-more").hidden = state.shown >= state.matches.length;
  }
  function refresh() {
    if (!state.data) return;
    const tokens = normal($("search").value).split(/\s+/).filter(Boolean);
    const source = state.data.records.filter((item) => matchesFilters(item, tokens));
    state.matches = source.sort((a, b) =>
      score(b, tokens) - score(a, tokens) ||
      String(a.title).localeCompare(String(b.title), "zh-CN") ||
      a.id.localeCompare(b.id));
    state.shown = 0;
    $("result-list").replaceChildren();
    $("result-count").textContent = count(state.matches.length);
    $("status").textContent = state.matches.length
      ? "覆盖 Registry 全量内容。主题分类是规则建议，详情可查看明确的来源关系。"
      : "未找到匹配条目，请更换关键词或清除筛选条件。";
    if (state.matches.length) renderPage();
    else {
      const empty = element("div", "empty");
      empty.append(element("h3", "", "未找到匹配内容"),
        element("p", "", "试试更短的关键词，或切换内容来源与主题。"));
      $("result-list").append(empty);
      $("load-more").hidden = true;
    }
    syncURL();
  }
  function detailRow(label, text) {
    const wrap = element("div");
    wrap.append(element("dt", "", label), element("dd", "", text));
    return wrap;
  }
  function sectionLinks(parent, heading, links) {
    if (!links.length) return;
    parent.append(element("h3", "", heading));
    const list = element("div", "detail-links");
    links.forEach((item) => { if (item) list.append(item); });
    parent.append(list);
  }
  function showDetail(id, updateUrl) {
    const item = state.byId.get(id);
    if (!item) return;
    const panel = $("detail"), body = $("detail-content");
    panel.hidden = false;
    panel.dataset.selected = id;
    body.replaceChildren();
    body.append(element("p", "section-label", item.source.toUpperCase() + " / " + (kinds[item.kind] || "")));
    body.append(element("h2", "", item.title));
    if (item.summary) body.append(element("p", "detail-summary", item.summary));
    const info = element("dl", "detail-info");
    info.append(detailRow("内容类型", kinds[item.kind] || item.kind));
    info.append(detailRow("状态", item.review_status === "verified" ? "已审核" : "未完成人工审核"));
    info.append(detailRow("发布", item.publication_status === "published" ? "已映射 HTML" : "GitHub 原文件"));
    if (item.kind === "article_note") {
      info.append(detailRow("原文关系", references[item.reference_status] || "待核对"));
    }
    if (item.published_at) info.append(detailRow("发表日期", item.published_at));
    if (item.author) info.append(detailRow("作者", item.author));
    body.append(info);

    const read = element("a", "reference-btn",
      item.publication_status === "published" ? "阅读站点 HTML ↗" : "查看 GitHub 原文件 ↗");
    read.href = linkFor(item);
    body.append(read);
    const sources = [];
    if (item.canonical_url) sources.push(externalAnchor("官方文章原文 ↗", item.canonical_url));
    if (item.source_reference_url) sources.push(externalAnchor("笔记引用的原始来源 ↗", item.source_reference_url));
    sectionLinks(body, "原文与证据", sources);

    if (item.topics && item.topics.length) {
      body.append(element("h3", "", "主题建议"));
      const tags = element("div", "tag-row");
      item.topics.forEach((topic) => tags.append(element("span", "topic", topicLabel(topic))));
      body.append(tags);
      body.append(element("p", "detail-note", "关键词规则生成，未经逐篇人工确认。"));
    }
    const related = new Set([...(item.related_ids || []), ...(state.inbound.get(id) || [])]);
    related.delete(id);
    if (related.size) {
      body.append(element("h3", "", "关联内容 · " + related.size));
      let displayed = 0;
      for (const rid of related) {
        const dest = state.byId.get(rid);
        if (!dest || displayed >= 14) continue;
        const btn = element("button", "related-row", (kinds[dest.kind] || "") + " · " + dest.title);
        btn.type = "button";
        btn.addEventListener("click", () => showDetail(rid, true));
        body.append(btn);
        displayed++;
      }
      if (related.size > displayed) body.append(element("p", "footnote", "其余关联请使用检索查找。"));
    }
    const projectLinks = (item.related_projects || []).map((ident) => {
      const project = state.data.projects.find((p) => p.id === ident);
      return project ? externalAnchor(project.title + " ↗", project.url) : null;
    }).filter(Boolean);
    sectionLinks(body, "相关工程仓库", projectLinks);
    if (projectLinks.length) body.append(element("p", "detail-note",
      "仅关联 GitHub 工程仓库，不代表项目实验结果经过独立验证。"));
    if (item.legacy_markdown_path) {
      body.append(element("h3", "", "历史兼容路径"));
      const old = externalAnchor("旧 Markdown 入口 ↗", githubFile(item.legacy_markdown_path));
      if (old) body.append(old);
    }
    body.append(element("p", "detail-note", "Registry ID：" + item.id));
    if (updateUrl) syncURL();
    panel.focus({preventScroll: true});
    if (window.matchMedia("(max-width: 1180px)").matches) panel.scrollIntoView({behavior: "smooth", block: "start"});
  }
  function populateFilters() {
    const records = state.data.records;
    const sourceList = [...new Set(records.map((r) => r.source))].sort();
    for (const value of sourceList) {
      const opt = element("option", "", value.toUpperCase());
      opt.value = value;
      $("source").append(opt);
    }
    for (const topic of state.data.topics) {
      const opt = element("option", "", topic.label_zh + " / " + topic.label_en);
      opt.value = topic.id;
      $("topic").append(opt);
    }
    const stats = state.data.statistics;
    $("stat-all").textContent = count(stats.total);
    $("stat-site").textContent = count(stats.published_html);
    $("stat-notes").textContent = count(stats.research_notes);
    $("stat-review").textContent = count(stats.notes_without_local_source);
  }
  function restoreFromURL() {
    const params = new URLSearchParams(window.location.search);
    $("search").value = params.get("q") || "";
    filters.forEach((key) => { $(key).value = params.get(key) || ""; });
    const id = params.get("id");
    const valid = id && state.byId.has(id);
    $("detail").hidden = !valid;
    $("detail").dataset.selected = valid ? id : "";
    refresh();
    if (valid) showDetail(id, false);
  }
  async function load() {
    try {
      const response = await fetch("../catalog.json");
      if (!response.ok) throw new Error("HTTP " + response.status);
      const data = await response.json();
      if (data.schema_version !== 2 || !Array.isArray(data.records) ||
          data.records.length !== data.statistics.total) {
        throw new Error("未知的 Catalog 版本或 Registry 记录缺失");
      }
      state.data = data;
      state.byId = new Map(data.records.map((r) => [r.id, r]));
      for (const item of data.records) {
        for (const parent of item.related_ids || []) {
          if (!state.inbound.has(parent)) state.inbound.set(parent, []);
          state.inbound.get(parent).push(item.id);
        }
      }
      populateFilters();
      restoreFromURL();
      $("search").addEventListener("input", refresh);
      filters.forEach((id) => $(id).addEventListener("change", refresh));
      $("load-more").addEventListener("click", renderPage);
      $("reset").addEventListener("click", () => {
        $("search").value = "";
        filters.forEach((id) => { $(id).value = ""; });
        refresh();
        $("search").focus();
      });
      $("close-detail").addEventListener("click", () => {
        $("detail").hidden = true;
        $("detail").dataset.selected = "";
        syncURL();
      });
      window.addEventListener("popstate", restoreFromURL);
      window.addEventListener("keydown", (event) => {
        if (event.key === "/" && document.activeElement !== $("search") &&
            !["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement.tagName)) {
          event.preventDefault();
          $("search").focus();
        }
        if (event.key === "Escape" && !$("detail").hidden) $("close-detail").click();
      });
    } catch (error) {
      $("status").textContent = "知识索引加载失败：" + error.message +
        "。请重新刷新页面或通过 GitHub 查看源码。";
    }
  }
  load();
})();
