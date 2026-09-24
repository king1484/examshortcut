#!/usr/bin/env node
/* Generates out/sitemap.xml after `next build` (static export). Run: node scripts/generate-sitemap.mjs */
import fs from 'node:fs';
import path from 'node:path';

const OUT = path.join(process.cwd(), 'out');
const BASE = 'https://examshortcut.in';
const urls = ['/', '/about/', '/revision/', '/search/', '/exams/', '/daily-quiz/', '/exams/ssc-cgl/', '/learn/', '/exams/ssc-cgl/mocks/', '/formula-sheet/', '/exams/ssc-cgl/cutoffs/', '/exams/ssc-cgl/score-calculator/', '/current-affairs/'];

function walk(dir) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) walk(p);
    else if (f === 'index.html') {
      // path.relative yields no leading slash — without it the URL joins as
      // "https://examshortcut.inssc-cgl/…" and the seed-list dedupe misses
      const rel = '/' + path.relative(OUT, p).replaceAll('\\', '/').replace('/index.html', '/');
      if (!urls.includes(rel)) urls.push(rel);
    }
  }
}
if (fs.existsSync(OUT)) walk(OUT);

const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map((u) => `  <url><loc>${BASE}${u === '/' ? '/' : u}</loc></url>`).join('\n')}\n</urlset>\n`;
fs.writeFileSync(path.join(OUT, 'sitemap.xml'), xml);
console.log(`sitemap.xml: ${urls.length} URLs`);
