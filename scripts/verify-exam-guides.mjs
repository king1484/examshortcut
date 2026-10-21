import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { EXAMS } from '../src/lib/exams.ts';
import { allExamGuides, validateGuide } from './validate-exam-guides.mjs';

const guides = allExamGuides();
for (const { guide, id } of guides) validateGuide(guide, id);
for (const exam of EXAMS) assert(guides.some(item => item.exam === exam.id && item.guide.publishedAt), `No new guide for ${exam.id}`);
const fresh = guides.filter(item => item.guide.publishedAt);
const routes = ['/study-guides/', ...EXAMS.map(exam => `/exams/${exam.id}/guides/`), ...fresh.map(item => `/exams/${item.exam}/guides/${item.id}/`)];
const sitemap = fs.readFileSync('out/sitemap.xml', 'utf8');
const search = JSON.parse(fs.readFileSync('out/search-index.json', 'utf8'));
const documents = Array.isArray(search) ? search : search.docs;
for (const route of routes) {
  const html = fs.readFileSync(path.join('out', route, 'index.html'), 'utf8');
  assert(sitemap.includes(`<loc>https://examshortcut.in${route}</loc>`), `Not in sitemap: ${route}`);
  assert(html.includes(`rel="canonical" href="https://examshortcut.in${route}"`), `Canonical mismatch: ${route}`);
  assert(!/<meta[^>]+name="robots"[^>]+noindex/.test(html), `Unexpected noindex: ${route}`);
  assert(documents.some(doc => doc.url === route), `Not searchable: ${route}`);
}
for (const item of fresh) {
  const route = `/exams/${item.exam}/guides/${item.id}/`;
  const html = fs.readFileSync(path.join('out', route, 'index.html'), 'utf8');
  assert(html.includes(`property="article:modified_time" content="${item.guide.updatedAt}"`), `Missing article date: ${route}`);
  assert(html.includes('My action checklist') && html.includes('Original learning checks'), `Missing interactive content: ${route}`);
  const entry = sitemap.split('<url>').find(entry => entry.includes(`<loc>https://examshortcut.in${route}</loc>`));
  assert(entry?.includes(`<lastmod>${item.guide.updatedAt}</lastmod>`), `Incorrect sitemap date: ${route}`);
  for (const source of item.guide.sources) assert(html.includes(source.url.replaceAll('&', '&amp;')), `Missing official reference: ${route}`);
  for (const match of JSON.stringify(item.guide).matchAll(/\]\((\/[^)]+)\)/g)) {
    const target = match[1].split('#')[0].split('?')[0];
    assert(fs.existsSync(path.join('out', target, 'index.html')), `Broken guide link: ${route} → ${target}`);
  }
}
if (process.argv.includes('--live')) {
  for (let attempt = 0; attempt < 7; attempt++) {
    const failed = [];
    for (let offset = 0; offset < routes.length; offset += 5) {
      await Promise.all(routes.slice(offset, offset + 5).map(async route => {
        try {
          const response = await fetch(`https://examshortcut.in${route}`, { signal: AbortSignal.timeout(20000), headers: { 'Cache-Control': 'no-cache' } });
          const html = await response.text();
          const item = fresh.find(item => route === `/exams/${item.exam}/guides/${item.id}/`);
          if (!response.ok || !html.includes('<h1') || (item && !html.includes(`property="article:modified_time" content="${item.guide.updatedAt}"`))) failed.push(route);
        } catch { failed.push(route); }
      }));
    }
    if (!failed.length) break;
    if (attempt === 6) assert.fail(`Live guide versions not ready: ${failed.join(', ')}`);
    await new Promise(resolve => setTimeout(resolve, 10000));
  }
}
console.log(`${process.argv.includes('--live') ? 'Live + export' : 'Export'}: ${EXAMS.length} exams, ${fresh.length} new guides, ${routes.length} routes, source links, sitemap dates and search entries verified.`);
