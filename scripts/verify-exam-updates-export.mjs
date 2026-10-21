import fs from 'node:fs';
import assert from 'node:assert/strict';
const items = JSON.parse(fs.readFileSync('content/exam-updates.json', 'utf8'));
const sitemap = fs.readFileSync('out/sitemap.xml', 'utf8');
const feed = fs.readFileSync('out/exam-updates.xml', 'utf8');
for (const route of ['exam-updates', 'results', 'answer-keys']) {
  const html = fs.readFileSync(`out/${route}/index.html`, 'utf8');
  assert(html.includes('<h1'), route);
  assert(sitemap.includes(`https://examshortcut.in/${route}/`), route);
}
for (const item of items) {
  const route = `/exam-updates/${item.slug}/`;
  if (!item.published) { assert(!sitemap.includes(route)); assert(!feed.includes(route)); continue; }
  const html = fs.readFileSync(`out${route}index.html`, 'utf8');
  assert(html.includes('NewsArticle'), route);
  assert(html.includes(`property="article:published_time" content="${item.publishedAt}"`), route);
  assert(html.includes(`property="article:modified_time" content="${item.updatedAt}"`), route);
  assert(html.includes(`rel="canonical" href="https://examshortcut.in${route}"`), route);
  for (const source of item.sources) {
    const escaped = source.url.replaceAll('&', '&amp;').replaceAll('"', '&quot;');
    assert(html.includes(`href="${escaped}"`), `Missing official action link: ${route}`);
  }
  assert(sitemap.includes(`https://examshortcut.in${route}`), route);
  assert(feed.includes(`https://examshortcut.in${route}`), route);
}
assert.equal((feed.match(/<item>/g) ?? []).length, items.filter(item => item.published).length);
console.log('Exam updates export: result hub, all article routes, official action links, metadata, sitemap and RSS passed.');
