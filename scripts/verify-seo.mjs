import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
const OUT = 'out';
const BASE = 'https://examshortcut.in';
const flat = fs.readFileSync(path.join(OUT, 'sitemap.xml'), 'utf8');
const getLocs = xml => [...xml.matchAll(/<loc>(.*?)<\/loc>/g)].map(m => m[1]);
const urls = getLocs(flat);
assert.equal(new Set(urls).size, urls.length);
const index = getLocs(fs.readFileSync(path.join(OUT, 'sitemap-index.xml'), 'utf8'));
const grouped = index.flatMap(url => getLocs(fs.readFileSync(path.join(OUT, new URL(url).pathname), 'utf8')));
assert.deepEqual([...grouped].sort(), [...urls].sort());
let checked = 0;
for (const url of urls) {
  assert(url.startsWith(BASE + '/'));
  const html = fs.readFileSync(path.join(OUT, new URL(url).pathname, 'index.html'), 'utf8');
  const head = html.split('</head>')[0];
  assert(!/name="robots" content="[^"]*noindex/.test(head), url);
  assert(head.includes(`rel="canonical" href="${url}"`), url);
  assert(head.includes('property="og:title"'), url);
  assert(head.includes('property="og:description"'), url);
  assert(head.includes('name="twitter:title"'), url);
  checked++;
}
const read = route => fs.readFileSync(path.join(OUT,route,'index.html'),'utf8');
assert(!urls.includes(BASE+'/exams/ssc-cgl/mocks/cat-mock-1/'));
assert(fs.readFileSync(path.join(OUT,'_redirects'),'utf8').includes('/exams/ssc-cgl/mocks/cat-mock-1/ /exams/cat/mocks/cat-mock-1/ 301'));
assert(read('exams/ssc-cgl/mocks/cat-real-2025-1130-s2/').includes('noindex'));
assert(fs.readFileSync(path.join(OUT,'sitemap-study-guides.xml'),'utf8').includes('<lastmod>2026-10-10</lastmod>'));
assert(fs.readFileSync(path.join(OUT,'robots.txt'),'utf8').includes(BASE+'/sitemap-index.xml'));
// Every exported sitemap URL must resolve; canonical redirects stay outside it.
console.log(`SEO export checks passed: ${checked} canonical pages, ${index.length} sitemaps, metadata, content dates and duplicate-test redirects.`);
