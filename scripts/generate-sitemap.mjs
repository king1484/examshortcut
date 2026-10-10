#!/usr/bin/env node
/* Static-export SEO pass. Lastmod uses content metadata, never build time. */
import fs from 'node:fs';
import path from 'node:path';
const OUT = path.join(process.cwd(), 'out');
const BASE = 'https://examshortcut.in';
const pages = new Map();
const redirects = [];
let noindex = 0, alternate = 0, tagsAdded = 0;
const escape = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&apos;');
const groups = new Map(['pages', 'lessons', 'study-guides', 'exams', 'current-affairs', 'exam-analysis'].map(g => [g, []]));
function groupFor(url) {
  if (/^\/(quant|reasoning|english|ga|computer)\//.test(url)) return 'lessons';
  for (const g of ['study-guides', 'exams', 'current-affairs', 'exam-analysis']) if (url.startsWith(`/${g}/`)) return g;
  return 'pages';
}
function walk(dir) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) { if (f !== '_next') walk(p); continue; }
    if (f !== 'index.html') continue;
    const route = ('/' + path.relative(OUT, p).replaceAll('\\', '/')).replace(/index\.html$/, '');
    let html = fs.readFileSync(p, 'utf8');
    const head = html.slice(0, html.indexOf('</head>'));
    const canonical = head.match(/<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"/);
    const url = BASE + route;
    const tags = [];
    if (!canonical) tags.push(`<link rel="canonical" href="${url}"/>`);
    const title = head.match(/<title>([\s\S]*?)<\/title>/)?.[1];
    const description = head.match(/<meta\b[^>]*name="description"[^>]*content="([^"]*)"/)?.[1];
    // Next has already HTML-escaped these values. Keep page-specific tags.
    for (const [key, value] of [['og:title', title], ['og:description', description], ['og:url', canonical?.[1] ?? url], ['twitter:title', title], ['twitter:description', description]]) {
      const name = key.startsWith('og:') ? 'property' : 'name';
      if (value && !head.includes(`${name}="${key}"`)) tags.push(`<meta ${name}="${key}" content="${value}"/>`);
    }
    if (tags.length) {
      html = html.replace('</head>', tags.join('') + '</head>');
      fs.writeFileSync(p, html); tagsAdded += tags.length;
    }
    if (canonical && canonical[1] !== url) {
      alternate++;
      if (canonical[1].startsWith(BASE + '/')) redirects.push(`${route} ${canonical[1].slice(BASE.length)} 301`);
      continue;
    }
    if (/<meta\b[^>]*name="robots"[^>]*content="[^"]*noindex/.test(head)) { noindex++; continue; }
    const modified = head.match(/property="article:modified_time" content="([^"]+)"/)?.[1];
    const lastmod = modified && /^\d{4}-\d{2}-\d{2}(?:T.*)?$/.test(modified) && !Number.isNaN(Date.parse(modified)) ? modified : undefined;
    pages.set(url, { url, lastmod });
    groups.get(groupFor(route)).push({ url, lastmod });
  }
}
walk(OUT);
const xmlHeader = '<?xml version="1.0" encoding="UTF-8"?>\n';
function writeMap(file, entries) {
  const items = entries.sort((a, b) => a.url.localeCompare(b.url));
  const xml = xmlHeader + '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + items.map(p => `  <url><loc>${escape(p.url)}</loc>${p.lastmod ? `<lastmod>${escape(p.lastmod)}</lastmod>` : ''}</url>`).join('\n') + '\n</urlset>\n';
  fs.writeFileSync(path.join(OUT, file), xml);
}
// Retain the existing URL for previously submitted search properties.
writeMap('sitemap.xml', [...pages.values()]);
const maps = [];
for (const [group, entries] of groups) {
  if (!entries.length) continue;
  const file = `sitemap-${group}.xml`; writeMap(file, entries); maps.push(file);
}
fs.writeFileSync(path.join(OUT, 'sitemap-index.xml'), xmlHeader + '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + maps.map(file => `  <sitemap><loc>${BASE}/${file}</loc></sitemap>`).join('\n') + '\n</sitemapindex>\n');
console.log(`SEO: ${pages.size} canonical URLs, ${maps.length} grouped sitemaps, ${noindex} noindex pages excluded, ${alternate} alternate pages excluded; ${tagsAdded} metadata tags added.`);
if (redirects.length) {
  const file = path.join(OUT, '_redirects');
  const existing = fs.readFileSync(file, 'utf8');
  const marker = '\n# Generated canonical route redirects\n';
  fs.writeFileSync(file, existing.split(marker)[0] + marker + redirects.sort().join('\n') + '\n');
}
