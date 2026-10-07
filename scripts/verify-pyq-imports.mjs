import assert from 'node:assert/strict';
import fs from 'node:fs';
import ts from 'typescript';

const moduleUrl = code => `data:text/javascript;base64,${Buffer.from(code).toString('base64')}`;
const transpile = path => ts.transpileModule(fs.readFileSync(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const sectionsUrl = moduleUrl(transpile('src/lib/sections.ts'));
const content = await import(moduleUrl(transpile('src/lib/content.ts').replaceAll("'./sections'", JSON.stringify(sectionsUrl))));

const imports = JSON.parse(fs.readFileSync('content/pyq-imports-2026-10-07.json', 'utf8'));
const allIds = new Set();
let total = 0;
// Held back: explanations are near-verbatim from the source site; rewrite before registering.
const HELD = new Set(['cat-real-2025-1130-s2', 'cat-real-2025-1130-s3']);
for (const paper of imports) {
  if (HELD.has(paper.id ?? paper.mockId)) continue;
  assert.notEqual(paper.readyForRegistration, false);
  const exam = paper.exam ?? paper.examId ?? 'ssc-cgl';
  const id = paper.id ?? paper.mockId;
  const sections = paper.sections?.map(s => typeof s === 'string' ? s : s.id) ?? Object.keys(paper.counts);
  let count = 0;
  for (const section of sections) {
    const path = `content/exams/${exam}/mocks/parts/${id}--${section}.json`;
    const part = JSON.parse(fs.readFileSync(path, 'utf8'));
    assert.equal(part.mockId, id, path);
    assert.equal(part.sectionId, section, path);
    assert.ok(part.questions.length > 0, path);
    for (const q of part.questions) {
      assert.ok(!allIds.has(q.id), `Duplicate question ID: ${q.id}`);
      allIds.add(q.id);
      assert.ok(q.q.trim() && q.solution.trim(), q.id);
      if (q.type === 'numeric') {
        assert.deepEqual(q.options, [], q.id);
        assert.ok(Number.isFinite(q.answer), q.id);
      } else {
        assert.ok([4, 5].includes(q.options.length), q.id);
        assert.ok(Number.isInteger(q.answer) && q.answer >= 0 && q.answer < q.options.length, q.id);
        assert.equal(new Set(q.options.map(s => s.trim())).size, q.options.length, q.id);
        assert.ok(q.options.every(s => s.trim()), q.id);
      }
      assert.ok(!/(?<![\\a-z])(?:sqrt|frac)\{|\bTODO\b|\bplaceholder\b/i.test(q.q), q.id);
      if (exam === 'ssc-mts') {
        assert.equal(q.negativeMarks, ['quant', 'reasoning'].includes(section) ? 0 : 1, q.id);
      }
    }
    count += part.questions.length;
  }
  assert.equal(count, paper.importedQuestionCount, id);
  const mock = content.getMock(id);
  assert.ok(mock, `Import missing from website registry: ${id}`);
  assert.equal(mock.sections.length, sections.length, id);
  assert.equal(mock.sections.reduce((n, s) => n + s.questions.length, 0), count, id);
  assert.ok(content.listMocks(exam).find(m => m.id === id)?.available, id);
  total += count;
}
for (const def of content.MOCK_DEFS) {
  const mock = content.getMock(def.id);
  if (mock) assert.equal(mock.sections.length, def.sections.length, `Partial paper exposed: ${def.id}`);
}
console.log(`Verified ${imports.length} registered imports: ${total} questions, complete sections, unique IDs, valid keys and MTS penalties.`);
