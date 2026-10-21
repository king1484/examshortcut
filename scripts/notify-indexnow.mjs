/* After deployment, notify changed indexable analysis, notice and exam pages. */
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
const BASE = 'https://examshortcut.in';
const KEY = '538756d8d399f34c2bb5583accbce022';
const months = ['january','february','march','april','may','june','july','august','september','october','november','december'];
const baseIndex = process.argv.indexOf('--base');
const base = baseIndex === -1 ? 'HEAD^' : process.argv[baseIndex + 1];
if (!base) throw new Error('--base requires a Git revision');
const changed = execFileSync('git', ['diff', '--name-only', base, 'HEAD'], {encoding:'utf8'}).trim().split('\n');
const urls = new Set();
for (const file of changed) {
  const examChange = /^content\/exams\/([^/]+)\/(exam|process)\.json$/.exec(file);
  if (examChange) {
    const exam = examChange[1];
    for (const suffix of ['', 'calendar/', 'admit-card/']) urls.add(`${BASE}/exams/${exam}/${suffix}`);
  }
  if (file === 'content/exam-updates.json') {
    const current = JSON.parse(fs.readFileSync(file, 'utf8'));
    let previous = [];
    try { previous = JSON.parse(execFileSync('git', ['show', `${base}:${file}`], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] })); } catch { /* first publication */ }
    const before = new Map(previous.map(item => [item.slug, JSON.stringify(item)]));
    for (const item of current) if (item.published && before.get(item.slug) !== JSON.stringify(item)) urls.add(`${BASE}/exam-updates/${item.slug}/`);
    for (const route of ['/', '/results/', '/answer-keys/', '/exam-updates/']) urls.add(BASE + route);
  }
  const match = /^content\/shift-analysis\/([^/]+)\/(\d{4})-(\d{2})-(\d{2})\.json$/.exec(file);
  if (!match || !fs.existsSync(file)) continue;
  const [, exam, , month, day] = match;
  const slug = `${Number(day)}-${months[Number(month)-1]}`;
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  urls.add(`${BASE}/exam-analysis/`);
  urls.add(`${BASE}/exam-analysis/${exam}/`);
  urls.add(`${BASE}/exam-analysis/${exam}/${slug}/`);
  for (const shift of data.shifts) urls.add(`${BASE}/exam-analysis/${exam}/${slug}-shift-${shift.shift}/`);
}
const indexable = new Set([...fs.readFileSync('out/sitemap.xml','utf8').matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>m[1]));
const localXml = fs.readFileSync('out/sitemap.xml','utf8');
const urlList = [...urls].filter(url=>indexable.has(url)).sort();
if (!urlList.length) {
  console.log('IndexNow: no changed indexable pages to submit.');
} else if (process.argv.includes('--dry-run')) {
  console.log(JSON.stringify({urlCount:urlList.length,urlList},null,2));
} else {
  // Wait for the advertised content timestamps to be live before notifying engines.
  let pending = [...urlList];
  for (let check = 0; check < 7; check++) {
    const response = await fetch(`${BASE}/sitemap.xml`, {signal:AbortSignal.timeout(30000),headers:{'Cache-Control':'no-cache'}});
    if (!response.ok) throw new Error(`Live sitemap returned HTTP ${response.status}`);
    const liveXml = await response.text();
    pending = urlList.filter(url => {
      const tag = `<loc>${url}</loc>`;
      const localEntry = localXml.split('<url>').find(entry=>entry.includes(tag))?.split('</url>')[0];
      const liveEntry = liveXml.split('<url>').find(entry=>entry.includes(tag))?.split('</url>')[0];
      return !liveEntry || localEntry?.match(/<lastmod>.*?<\/lastmod>/)?.[0] !== liveEntry.match(/<lastmod>.*?<\/lastmod>/)?.[0];
    });
    if (!pending.length) break;
    if (check < 6) {
      console.log(`IndexNow: waiting for ${pending.length} updated sitemap entries to propagate.`);
      await new Promise(resolve=>setTimeout(resolve,10000));
    }
  }
  if (pending.length) throw new Error(`Updated sitemap entry is not live yet: ${pending[0]}`);
  const result = await fetch('https://api.indexnow.org/indexnow', {
    method:'POST', headers:{'Content-Type':'application/json'}, signal:AbortSignal.timeout(30000),
    body:JSON.stringify({host:'examshortcut.in',key:KEY,keyLocation:`${BASE}/${KEY}.txt`,urlList}),
  });
  if (![200,202].includes(result.status)) throw new Error(`IndexNow rejected submission: HTTP ${result.status}`);
  console.log(JSON.stringify({submittedAt:new Date().toISOString(),urlCount:urlList.length,status:result.status,urlList}));
}
