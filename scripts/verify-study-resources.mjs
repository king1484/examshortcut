import assert from 'node:assert/strict';
import fs from 'node:fs';
import ts from 'typescript';

async function readModule(file) {
  const code = ts.transpileModule(fs.readFileSync(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
}
const { STUDY_GUIDES } = await readModule('src/lib/studyGuides.ts');
const { reviewDates, isCalendarDate, revisionCalendar } = await readModule('src/lib/revisionSchedule.ts');

assert.deepEqual(reviewDates('2028-02-28'), ['2028-02-29', '2028-03-02', '2028-03-06', '2028-03-13']);
assert.deepEqual(reviewDates('2026-12-31'), ['2027-01-01', '2027-01-03', '2027-01-07', '2027-01-14']);
assert.equal(isCalendarDate('2026-02-29'), false);
assert.throws(() => reviewDates('invalid'));
const calendar = revisionCalendar([{ id: 'topic-1', title: 'Ratio, प्रतिशत; revision\\check', start: '2026-10-09' }], new Date('2026-10-09T12:00:00Z'));
assert.equal((calendar.match(/BEGIN:VEVENT/g) ?? []).length, 4);
assert.ok(calendar.includes('DTSTART;VALUE=DATE:20261010'));
assert.ok(calendar.includes('DTSTAMP:20261009T120000Z'));
assert.ok(calendar.includes('Ratio\\, प्रतिशत\\; revision\\\\check'));
for (const line of calendar.split('\r\n')) assert.ok(Buffer.byteLength(line, 'utf8') <= 75);

const slugs = new Set(STUDY_GUIDES.map(g => g.slug));
assert.equal(slugs.size, STUDY_GUIDES.length);
let links = 0;
for (const guide of STUDY_GUIDES) {
  assert.ok(guide.sections.length >= 4 && guide.checklist.length >= 4, guide.slug);
  assert.equal(new Set(guide.sections.map(s => s.id)).size, guide.sections.length, guide.slug);
  for (const slug of guide.related) assert.ok(slugs.has(slug), `Missing related guide ${slug}`);
  const htmlFile = `out/study-guides/${guide.slug}/index.html`;
  assert.ok(fs.existsSync(htmlFile), `Missing exported guide ${guide.slug}`);
  const html = fs.readFileSync(htmlFile, 'utf8');
  assert.ok(html.includes(`rel="canonical" href="https://examshortcut.in/study-guides/${guide.slug}/"`), guide.slug);
  for (const section of guide.sections) {
    for (const match of section.body.matchAll(/\]\((\/[^)]+)\)/g)) {
      const url = match[1];
      assert.ok(fs.existsSync(`out${url}index.html`), `Broken guide link ${guide.slug}: ${url}`);
      links++;
    }
  }
}
const sitemap = fs.readFileSync('out/sitemap.xml', 'utf8');
for (const slug of slugs) assert.ok(sitemap.includes(`/study-guides/${slug}/`), slug);
assert.ok(sitemap.includes('/revision-planner/'));
const search = JSON.parse(fs.readFileSync('public/search-index.json', 'utf8'));
assert.ok(search.every(doc => typeof doc.title === 'string' && !doc.text.includes('[object Object]')));
for (const slug of slugs) assert.ok(search.some(doc => doc.url === `/study-guides/${slug}/`), slug);
console.log(`Verified ${STUDY_GUIDES.length} exported guides, ${links} lesson links, search and sitemap entries, leap-year review dates and calendar export.`);
