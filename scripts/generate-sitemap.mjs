#!/usr/bin/env node
/* Static-export SEO pass. Lastmod comes from page metadata or the content/source
   that generated the page; the build date is only a last-resort fallback. */
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const OUT = path.resolve(process.env.SITEMAP_OUT ?? path.join(ROOT, 'out'));
const CONTENT = path.join(ROOT, 'content');
const APP = path.join(ROOT, 'src', 'app');
const BASE = 'https://examshortcut.in';
const BUILD_DATE = new Date().toISOString().slice(0, 10);
const pages = new Map();
const redirects = new Set();
let noindex = 0, alternate = 0, tagsAdded = 0;
const escape = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&apos;');
const groups = new Map(['pages', 'lessons', 'study-guides', 'exams', 'current-affairs', 'exam-analysis', 'exam-updates'].map(g => [g, []]));
function groupFor(url) {
  if (/^\/(quant|reasoning|english|ga|computer)\//.test(url)) return 'lessons';
  for (const g of ['study-guides', 'exams', 'current-affairs', 'exam-analysis', 'exam-updates']) if (url.startsWith(`/${g}/`)) return g;
  return 'pages';
}

/* ------------------------------------------------------------------ dates */
const isoDate = (value) => {
  if (typeof value !== 'string') return undefined;
  const v = value.trim();
  if (!/^\d{4}-\d{2}-\d{2}(?:[T ].*)?$/.test(v)) return undefined;
  return Number.isNaN(Date.parse(v)) ? undefined : v;
};
const fileDate = (file) => {
  try { return fs.statSync(file).mtime.toISOString().slice(0, 10); } catch { return undefined; }
};
const newest = (dates) => dates.filter(Boolean).sort((a, b) => Date.parse(a) - Date.parse(b)).at(-1);
const newestOfFiles = (files) => newest(files.map(dateForFile));

const dateCache = new Map();
/** Prefer an explicit content date (updatedAt/modified/updated/lastVerified or Markdown
    frontmatter). If the content has no usable date, fall back to the file's real mtime. */
function dateForFile(file) {
  if (dateCache.has(file)) return dateCache.get(file);
  let date;
  try {
    if (file.endsWith('.json')) {
      const data = JSON.parse(fs.readFileSync(file, 'utf8'));
      if (data && !Array.isArray(data)) {
        date = isoDate(data.updatedAt) ?? isoDate(data.modified) ?? isoDate(data.updated) ?? isoDate(data.lastVerified);
      }
    } else if (/\.(md|mdx)$/.test(file)) {
      const text = fs.readFileSync(file, 'utf8');
      const fm = text.match(/^---\s*([\s\S]*?)\s*---/);
      if (fm) {
        const field = (key) => fm[1].match(new RegExp(`^${key}:\\s*(.+)$`, 'm'))?.[1]?.trim().replace(/^['"]|['"]$/g, '');
        date = isoDate(field('updated')) ?? isoDate(field('modified')) ?? isoDate(field('date'));
      }
    }
  } catch { /* unreadable/invalid file: use its mtime below */ }
  date ??= fileDate(file);
  dateCache.set(file, date);
  return date;
}

/* ------------------------------------------------------------------ content routes */
const SECTION_IDS = new Set(['quant', 'reasoning', 'english', 'ga', 'computer']);
const MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'];
const monthNumber = (name) => MONTHS.indexOf(name.toLowerCase()) + 1;

function examContentDate(parts) {
  const exam = parts[1];
  const dir = path.join(CONTENT, 'exams', exam);
  if (!fs.existsSync(dir)) return undefined;
  const contentFile = (...rel) => path.join(dir, ...rel);
  const kind = parts[2];

  if (!kind) return dateForFile(contentFile('exam.json'));

  if (kind === 'guides') {
    if (parts[3]) return dateForFile(contentFile('guides', `${parts[3]}.json`));
    const guides = path.join(dir, 'guides');
    const files = fs.existsSync(guides) ? fs.readdirSync(guides).filter(f => f.endsWith('.json')).map(f => path.join(guides, f)) : [];
    return newest([...files.map(dateForFile), dateForFile(contentFile('exam.json'))]);
  }

  if (kind === 'mocks') {
    const partsDir = path.join(dir, 'mocks', 'parts');
    const all = fs.existsSync(partsDir) ? fs.readdirSync(partsDir).filter(f => f.endsWith('.json')) : [];
    const files = parts[3] ? all.filter(f => f.startsWith(`${parts[3]}--`)) : all;
    return newest([...files.map(f => dateForFile(path.join(partsDir, f))), dateForFile(path.join(ROOT, 'src', 'lib', 'content.ts'))]);
  }

  if (kind === 'posts') {
    return newest([dateForFile(contentFile('exam.json')), dateForFile(path.join(ROOT, 'src', 'lib', 'postDetails.ts'))]);
  }
  if (kind === 'cutoffs') return dateForFile(contentFile('cutoffs.json'));
  if (kind === 'syllabus') return dateForFile(contentFile('syllabus.json'));
  if (kind === 'expected-cutoff') return newest([dateForFile(contentFile('expected-cutoff.json')), dateForFile(contentFile('exam.json'))]);
  if (kind === 'calendar' || kind === 'admit-card') return dateForFile(contentFile('process.json'));
  if (kind === 'weightage') return dateForFile(contentFile('weightage.json'));
  if (kind === 'eligibility' || kind === 'exam-pattern' || kind === 'salary-and-posts') return dateForFile(contentFile('exam.json'));
  if (kind === 'score-calculator' || kind === 'rank-estimator' || kind === 'normalisation-calculator' || kind === 'salary-calculator') {
    return newest([dateForFile(contentFile('exam.json')), dateForFile(contentFile('cutoffs.json')), dateForFile(contentFile('weightage.json'))]);
  }
  return dateForFile(contentFile(`${kind}.json`));
}

function currentAffairsDate(parts) {
  const dir = path.join(CONTENT, 'core', 'current-affairs');
  if (parts[1] && /^\d{4}$/.test(parts[1])) return dateForFile(path.join(dir, `${parts[1]}.json`));
  if (!fs.existsSync(dir)) return undefined;
  return newestOfFiles(fs.readdirSync(dir).filter(f => /^\d{4}\.json$/.test(f)).map(f => path.join(dir, f)));
}

function shiftAnalysisDate(parts) {
  const root = path.join(CONTENT, 'shift-analysis');
  if (!fs.existsSync(root)) return undefined;
  const exam = parts[1];
  if (!exam) {
    const files = fs.readdirSync(root, { withFileTypes: true })
      .filter(e => e.isDirectory())
      .flatMap(e => fs.readdirSync(path.join(root, e.name)).filter(f => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).map(f => path.join(root, e.name, f)));
    return newest([dateForFile(path.join(root, 'exams.json')), ...files.map(dateForFile)]);
  }
  const dir = path.join(root, exam);
  if (!fs.existsSync(dir)) return undefined;
  const dayFiles = fs.readdirSync(dir).filter(f => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).map(f => path.join(dir, f));
  if (!parts[2]) return newest([dateForFile(path.join(root, 'exams.json')), ...dayFiles.map(dateForFile)]);

  const match = /^(\d{1,2})-([a-z]+)(?:-shift-\d+)?$/i.exec(parts[2]);
  const month = match ? monthNumber(match[2]) : 0;
  if (!month) return undefined;
  const matching = dayFiles.filter(file => {
    const [, mm, dd] = path.basename(file).slice(0, 10).split('-').map(Number);
    return mm === month && dd === Number(match[1]);
  });
  return newestOfFiles(matching);
}

/** Explicit date for the content that drives a route, when we can identify it. */
function contentDateFor(route) {
  const parts = route.split('/').filter(Boolean);
  if (!parts.length) return undefined;

  if (SECTION_IDS.has(parts[0])) {
    return parts[1]
      ? dateForFile(path.join(CONTENT, 'core', 'topics', parts[0], `${parts[1]}.json`))
      : dateForFile(path.join(CONTENT, 'core', 'sections', `${parts[0]}.json`));
  }
  if (parts[0] === 'current-affairs') return currentAffairsDate(parts);
  if (parts[0] === 'exam-analysis') return shiftAnalysisDate(parts);
  if (parts[0] === 'exams') {
    if (!parts[1]) {
      const dir = path.join(CONTENT, 'exams');
      const files = fs.existsSync(dir) ? fs.readdirSync(dir).map(e => path.join(dir, e, 'exam.json')).filter(f => fs.existsSync(f)) : [];
      return newest([...files.map(dateForFile), dateForFile(path.join(ROOT, 'src', 'lib', 'exams.ts'))]);
    }
    return examContentDate(parts);
  }
  if (parts[0] === 'study-guides') {
    // Study-guide copy lives in src/lib/studyGuides.ts, not in a JSON file.
    return dateForFile(path.join(ROOT, 'src', 'lib', 'studyGuides.ts'));
  }
  if (parts[0] === 'vocab') return dateForFile(path.join(ROOT, 'src', 'data', 'vocab.ts'));
  return undefined;
}

/* ------------------------------------------------------------------ source routes */
const sourceRoutes = [];
function scanRoutes(dir, rel = '') {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      scanRoutes(path.join(dir, entry.name), rel ? `${rel}/${entry.name}` : entry.name);
    } else if (entry.name === 'page.tsx') {
      const segments = rel ? rel.split('/') : [];
      let score = 0;
      const pattern = !segments.length ? '^/$' : '^/' + segments.map((seg) => {
        if (/^\[\[\.\.\..+\]\]$/.test(seg)) { score += 1; return '.*'; }
        if (/^\[\.\.\..+\]$/.test(seg)) { score += 1; return '.+'; }
        if (/^\[.+\]$/.test(seg)) return '[^/]+';
        score += 10;
        return seg.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      }).join('/') + '/$';
      sourceRoutes.push({ re: new RegExp(pattern), score, file: path.join(dir, entry.name) });
    }
  }
}
if (fs.existsSync(APP)) scanRoutes(APP);

/** mtime of the most specific page.tsx that produced the route. */
function sourceDateFor(route) {
  let best;
  for (const candidate of sourceRoutes) {
    if (!candidate.re.test(route)) continue;
    if (!best || candidate.score > best.score) best = candidate;
  }
  return best ? dateForFile(best.file) : undefined;
}

/* ------------------------------------------------------------------ crawl */
function walk(dir) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) { if (f !== '_next') walk(p); continue; }
    if (f !== 'index.html') continue;
    const route = ('/' + path.relative(OUT, p).replaceAll('\\', '/')).replace(/index\.html$/, '');
    // Legacy CGL URLs used to export mocks belonging to other exams. Their
    // replacement pages no longer exist, so derive redirects from the actual
    // destination exports, including review-held pages excluded from sitemaps.
    const mockRoute = /^\/exams\/([^/]+)\/mocks\/([^/]+)\/$/.exec(route);
    if (mockRoute && mockRoute[1] !== 'ssc-cgl') {
      const legacy = `/exams/ssc-cgl/mocks/${mockRoute[2]}`;
      redirects.add(`${legacy}/ ${route} 301`);
      redirects.add(`${legacy} ${route} 301`);
    }
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
      if (canonical[1].startsWith(BASE + '/')) redirects.add(`${route} ${canonical[1].slice(BASE.length)} 301`);
      continue;
    }
    if (/<meta\b[^>]*name="robots"[^>]*content="[^"]*noindex/.test(head)) { noindex++; continue; }

    const declared = head.match(/<meta\b[^>]*property="article:modified_time"[^>]*content="([^"]+)"/)?.[1]
      ?? head.match(/<meta\b[^>]*content="([^"]+)"[^>]*property="article:modified_time"/)?.[1];
    // Explicit content dates win; otherwise the generating page's mtime. The build
    // date is only the last resort for a page whose source cannot be identified.
    const lastmod = isoDate(declared) ?? contentDateFor(route) ?? sourceDateFor(route) ?? BUILD_DATE;
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
if (redirects.size) {
  const file = path.join(OUT, '_redirects');
  const existing = fs.readFileSync(file, 'utf8');
  const marker = '\n# Generated canonical route redirects\n';
  fs.writeFileSync(file, existing.split(marker)[0] + marker + [...redirects].sort().join('\n') + '\n');
}
