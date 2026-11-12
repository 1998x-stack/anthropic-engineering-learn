"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const Search = require("../docs/explore/search-engine.js");
const entry = {
  id: "source:langchain:memory", kind: "source_article",
  title: "Understanding tools", summary: "Introduction to agents",
  source: "langchain", author: "Team"
};

test("a hidden long-tail phrase is discoverable in full body", () => {
  const tokens = Search.tokenize("跨会话记忆压缩机制");
  assert.equal(Search.matches(entry, tokens, undefined, ["工具"]), false);
  assert.equal(Search.matches(entry, tokens, "中间大量文字…最后：跨会话记忆压缩机制。", ["工具"]), true);
});

test("full text is AND across multiple terms, including mixed languages", () => {
  assert.equal(Search.matches(entry, Search.tokenize("tools 记忆"), "这些讨论包含 记忆", []), true);
  assert.equal(Search.matches(entry, Search.tokenize("tools 不存在"), "这些讨论包含 记忆", []), false);
  assert.deepEqual(Search.tokenize("  RAG  Agent  "), ["rag", "agent"]);
});

test("body-only matches rank below title hits", () => {
  const terms = ["tools"];
  assert.ok(Search.rank(entry, terms, undefined, []) >
            Search.rank({...entry, title: "Other"}, terms, "tools", []));
});

test("snippets are bounded and never interpreted as HTML", () => {
  const text = "x".repeat(400) + "<script>alert('XSS')</script>终章";
  const excerpt = Search.snippet(text, ["终章"], 100);
  assert.ok(excerpt.includes("终章"));
  assert.ok(excerpt.length <= 110);
  assert.equal(Search.snippet(text, ["not_found"]), "");
});


test("browser shard loader accepts generated JSON names and rejects traversal", () => {
  const fs = require("node:fs");
  const path = require("node:path");
  const js = fs.readFileSync(path.join(__dirname, "../docs/explore/app.js"), "utf8");
  const match = js.match(/if \(!\/(.+?)\/\.test\(shard\.file\)\)/);
  assert.ok(match, "shard filename validation must stay present");
  const pattern = new RegExp(match[1]);
  assert.ok(pattern.test("langchain-000.json"));
  assert.ok(pattern.test("browser-use-015.json"));
  assert.equal(pattern.test("../notes-000.json"), false);
  assert.equal(pattern.test("evil.json/../langchain-000.json"), false);
  assert.equal(pattern.test("langchain-000.json.js"), false);
});
