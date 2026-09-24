/* Builds public/data/daily/<n>.json — N rotating day-buckets mixing every section's
   practice questions. The /daily-quiz/ page picks bucket = daysSinceEpoch % N, so each
   day serves a fresh mix with zero server cost. Run before `next build`. */
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const CORE = path.join(ROOT, 'content', 'core', 'topics');
const OUT = path.join(ROOT, 'public', 'data', 'daily');
const BUCKETS = 30; // ~1 month before the cycle repeats
const PER_SECTION = 4; // questions per section per day

function seededShuffle(arr, seed) {
  let s = seed >>> 0;
  const rand = () => { s = (s + 0x6d2b79f5) | 0; let t = Math.imul(s ^ (s >>> 15), 1 | s); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rand() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
const hash = (str) => { let h = 2166136261; for (const c of str) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619); } return h >>> 0; };

const sections = fs.readdirSync(CORE).filter((d) => fs.statSync(path.join(CORE, d)).isDirectory());
const perSection = {}; // section -> shuffled question pool (with topic tags)
for (const sec of sections) {
  const pool = [];
  const dir = path.join(CORE, sec);
  for (const f of fs.readdirSync(dir).filter((f) => f.endsWith('.json'))) {
    const t = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    (t.practice ?? []).forEach((q, i) => pool.push({ ...q, id: `${t.id}/${q.id ?? i}`, topic: t.title }));
  }
  if (pool.length) perSection[sec] = seededShuffle(pool, hash(sec));
}

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });
const names = { quant: 'Quantitative Aptitude', reasoning: 'Reasoning', english: 'English', ga: 'General Awareness', computer: 'Computer' };
let total = 0;
for (let b = 0; b < BUCKETS; b++) {
  const secs = Object.entries(perSection).map(([section, pool]) => {
    const questions = [];
    for (let i = 0; i < PER_SECTION; i++) questions.push(pool[(b * PER_SECTION + i) % pool.length]);
    total += questions.length;
    return { section, name: names[section] ?? section, questions };
  }).filter((s) => s.questions.length);
  fs.writeFileSync(path.join(OUT, `${b}.json`), JSON.stringify({ n: b, sections: secs }));
}
console.log(`daily-quiz: wrote ${BUCKETS} buckets × ${Object.keys(perSection).length} sections × ${PER_SECTION} Q = ${total} slots`);
