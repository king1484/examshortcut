/* After deployment, notify only changed analysis pages that are publicly indexable. */
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
const BASE = 'https://examshortcut.in';
const KEY = '538756d8d399f34c2bb5583accbce022';
const months = ['january','february','march','april','may','june','july','august','september','october','november','december'];
const changed = execFileSync('git', ['diff', '--name-only', 'HEAD^', 'HEAD'], {encoding:'utf8'}).trim().split('\n');
const urls = new Set();
for (const file of changed) {
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
const urlList = [...urls].filter(url=>indexable.has(url)).sort();
if (!urlList.length) {
  console.log('IndexNow: no changed indexable analysis pages to submit.');
} else if (process.argv.includes('--dry-run')) {
  console.log(JSON.stringify({urlCount:urlList.length,urlList},null,2));
} else {
  // Wait for the advertised content timestamps to be live before notifying engines.
  const response = await fetch(`${BASE}/sitemap.xml`, {signal:AbortSignal.timeout(30000)});
  if (!response.ok) throw new Error(`Live sitemap returned HTTP ${response.status}`);
  const liveXml = await response.text();
  for (const url of urlList) {
    const tag = `<loc>${url}</loc>`;
    const localEntry = fs.readFileSync('out/sitemap.xml','utf8').split('<url>').find(entry=>entry.includes(tag))?.split('</url>')[0];
    const liveEntry = liveXml.split('<url>').find(entry=>entry.includes(tag))?.split('</url>')[0];
    if (!liveEntry || (localEntry?.match(/<lastmod>.*?<\/lastmod>/)?.[0] !== liveEntry.match(/<lastmod>.*?<\/lastmod>/)?.[0])) {
      throw new Error(`Updated sitemap entry is not live yet: ${url}`);
    }
  }
  const result = await fetch('https://api.indexnow.org/indexnow', {
    method:'POST', headers:{'Content-Type':'application/json'}, signal:AbortSignal.timeout(30000),
    body:JSON.stringify({host:'examshortcut.in',key:KEY,keyLocation:`${BASE}/${KEY}.txt`,urlList}),
  });
  if (![200,202].includes(result.status)) throw new Error(`IndexNow rejected submission: HTTP ${result.status}`);
  console.log(JSON.stringify({submittedAt:new Date().toISOString(),urlCount:urlList.length,status:result.status,urlList}));
}
