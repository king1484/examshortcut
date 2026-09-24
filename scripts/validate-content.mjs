#!/usr/bin/env node
/* Validates every content JSON: parses, checks the Question contract, topic ids, options count.
   Run: npm run validate */
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.join(process.cwd(), 'content');
const errors = [];
let files = 0, questions = 0;

function walk(dir) {
  if (!fs.existsSync(dir)) return;
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) { if (f !== '_work') walk(p); }
    else if (f.endsWith('.json')) check(p);
  }
}

const seenIds = new Set();
function checkQ(q, where) {
  const id = q.id ?? '(no id)';
  const at = `${where} · ${id}`;
  if (!q.id) errors.push(`${at}: missing id`);
  if (!q.q) errors.push(`${at}: missing q`);
  if (!Array.isArray(q.options) || q.options.length !== 4) errors.push(`${at}: options must be exactly 4`);
  if (q.options && new Set(q.options).size !== q.options.length) errors.push(`${at}: duplicate options`);
  if (!Number.isInteger(q.answer) || q.answer < 0 || q.answer > 3) errors.push(`${at}: answer index out of range`);
  if (!q.solution) errors.push(`${at}: missing solution`);
  questions++;
}

function check(p) {
  files++;
  const full = path.relative(ROOT, p).split(path.sep).join('/');
  // strip the layer prefix: core/<x> or exams/<examId>/<x>
  const rel = full.replace(/^core\//, '').replace(/^exams\/[^/]+\//, '');
  let data;
  try { data = JSON.parse(fs.readFileSync(p, 'utf-8')); }
  catch (e) { errors.push(`${rel}: INVALID JSON — ${e.message}`); return; }

  if (rel.startsWith('topics')) {
    if (!data.id || !data.sectionId || !data.title) errors.push(`${rel}: topic needs id, sectionId, title`);
    if (seenIds.has(`${data.sectionId}/${data.id}`)) errors.push(`${rel}: duplicate topic id ${data.sectionId}/${data.id}`);
    seenIds.add(`${data.sectionId}/${data.id}`);
    for (const s of data.subtopics ?? []) {
      if (!s.id || !s.title || typeof s.concept !== 'string') errors.push(`${rel}: bad subtopic ${s.id ?? '?'}`);
    }
    (data.solvedExamples ?? []).forEach((q) => checkQ(q, `${rel}#solved`));
    (data.practice ?? []).forEach((q) => checkQ(q, `${rel}#practice`));
    const ids = new Set();
    for (const q of [...(data.solvedExamples ?? []), ...(data.practice ?? [])]) {
      if (ids.has(q.id)) errors.push(`${rel}: duplicate question id ${q.id}`);
      ids.add(q.id);
    }
  } else if (rel.startsWith('current-affairs')) {
    for (const m of data.months ?? []) {
      if (!/^\d{4}-\d{2}$/.test(m.month ?? '')) errors.push(`${rel}: bad month ${m.month}`);
      for (const it of m.items ?? []) if (!it.headline || !it.detail || !it.category) errors.push(`${rel}#${m.month}: item missing headline/detail/category`);
      (m.quiz ?? []).forEach((q) => checkQ(q, `${rel}#${m.month}`));
    }
  } else if (rel.startsWith('mocks')) {
    (data.questions ?? []).forEach((q) => checkQ(q, rel));
  } else if (['sections', 'topics'].includes(rel.split(path.sep)[0]) || rel.endsWith('.json')) {
    // exam.json / cutoffs.json / sections — structural checks are light
    if (typeof data !== 'object' || data === null) errors.push(`${rel}: not an object`);
  }
}

walk(ROOT);
console.log(`Checked ${files} JSON files, ${questions} questions.`);
if (errors.length) {
  console.error(`\n${errors.length} ERROR(S):`);
  for (const e of errors) console.error(' -', e);
  process.exit(1);
}
console.log('All content valid.');
