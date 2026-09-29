#!/usr/bin/env node
/* Post-export SEO pass, run after `next build` (static export): gives every page a self-referencing canonical
   (and og:url) unless the page set its own, then writes out/sitemap.xml with every indexable page.
   Run: node scripts/generate-sitemap.mjs */
import fs from 'node:fs';
import path from 'node:path';

const OUT = path.join(process.cwd(), 'out');
const BASE = 'https://examshortcut.in';
const urls = ['/', '/about/', '/exams/', '/daily-quiz/', '/exams/ssc-cgl/', '/learn/', '/exams/ssc-cgl/mocks/', '/formula-sheet/', '/exams/ssc-cgl/cutoffs/', '/exams/ssc-cgl/score-calculator/', '/current-affairs/'];

const noindex = new Set();
let canonicals = 0;

function walk(dir) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) { if (f !== '_next') walk(p); }
    else if (f === 'index.html') {
      // path.relative yields no leading slash — without it the URL joins as
      // "https://examshortcut.inssc-cgl/…" and the seed-list dedupe misses.
      // Strip "index.html" as a whole segment so the root page maps to "/", not "/index.html".
      const rel = ('/' + path.relative(OUT, p).replaceAll('\\', '/')).replace(/index\.html$/, '');
      let html = fs.readFileSync(p, 'utf8');
      if (/<meta name="robots" content="[^"]*noindex/.test(html)) {
        noindex.add(rel);
        continue;
      }
      if (!html.includes('rel="canonical"')) {
        const tags = `<link rel="canonical" href="${BASE}${rel}"/>` + (html.includes('property="og:url"') ? '' : `<meta property="og:url" content="${BASE}${rel}"/>`);
        html = html.replace('</head>', tags + '</head>');
        fs.writeFileSync(p, html);
        canonicals++;
      }
      if (!urls.includes(rel)) urls.push(rel);
    }
  }
}
if (fs.existsSync(OUT)) walk(OUT);

const listed = urls.filter((u) => !noindex.has(u));
const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${listed.map((u) => `  <url><loc>${BASE}${u === '/' ? '/' : u}</loc></url>`).join('\n')}\n</urlset>\n`;
fs.writeFileSync(path.join(OUT, 'sitemap.xml'), xml);
console.log(`sitemap.xml: ${listed.length} URLs (${noindex.size} noindex pages left out) · canonical added to ${canonicals} pages`);
