// Build pattern-id -> human name registry for the Explanation chip.
// QuestionView imports src/data/pattern-names.json (bundled, tiny).
import fs from 'node:fs';
import path from 'node:path';

const CORE = path.join(process.cwd(), 'content', 'core', 'topics');
const map = {};
let n = 0;
for (const section of fs.readdirSync(CORE)) {
  const dir = path.join(CORE, section);
  if (!fs.statSync(dir).isDirectory()) continue;
  for (const f of fs.readdirSync(dir)) {
    if (!f.endsWith('.json')) continue;
    const t = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    for (const s of t.subtopics ?? []) {
      for (const p of s.patterns ?? []) {
        if (!p?.id) continue;
        n++;
        if (!map[p.id]) map[p.id] = p.name || p.id;
        else if (map[p.id] !== (p.name || p.id)) map[p.id] = map[p.id]; // first wins
      }
    }
  }
}
const out = path.join(process.cwd(), 'src', 'data', 'pattern-names.json');
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify(map, null, 0));
console.log(`pattern-names.json: ${Object.keys(map).length} unique ids (${n} declarations)`);
