/* Minimal, dependency-free full-text matching helpers.
 * Works as a browser global and a Node CommonJS module for regression tests.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (root) root.ExplorerSearch = api;
})(typeof globalThis !== "undefined" ? globalThis : undefined, function () {
  "use strict";
  const normalize = (value) => String(value || "").normalize("NFKC").toLocaleLowerCase();
  function tokenize(query) {
    return normalize(query).split(/\s+/).filter(Boolean);
  }
  function metadata(item, topicLabels) {
    return [item.title, item.id, item.summary, item.source, item.author,
      item.published_at, ...(topicLabels || [])].join(" ");
  }
  function matches(item, tokens, body, topicLabels) {
    const head = normalize(metadata(item, topicLabels));
    const full = typeof body === "string" ? normalize(body) : "";
    return tokens.every((token) => head.includes(token) || full.includes(token));
  }
  function rank(item, tokens, body, topicLabels) {
    if (!tokens.length) return item.kind === "article_note" ? 2 : item.kind === "source_article" ? 1 : 0;
    const title = normalize(item.title), id = normalize(item.id);
    const summary = normalize(item.summary), tags = normalize((topicLabels || []).join(" "));
    const text = typeof body === "string" ? normalize(body) : "";
    return tokens.reduce((score, token) => score +
      (title.includes(token) ? 12 : 0) + (id.includes(token) ? 6 : 0) +
      (tags.includes(token) ? 4 : 0) + (summary.includes(token) ? 2 : 0) +
      (text.includes(token) ? 1 : 0), 0);
  }
  function snippet(body, tokens, limit) {
    if (typeof body !== "string" || !tokens.length) return "";
    const normalized = normalize(body);
    const occurrences = tokens.map((t) => normalized.indexOf(t)).filter((i) => i >= 0);
    if (!occurrences.length) return "";
    const index = Math.min(...occurrences);
    const width = limit || 220;
    const start = Math.max(0, index - 65);
    const sliced = body.slice(start, start + width).replace(/\s+/g, " ").trim();
    return (start ? "…" : "") + sliced + (start + width < body.length ? "…" : "");
  }
  return { normalize, tokenize, matches, rank, snippet };
});
