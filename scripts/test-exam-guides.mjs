import test from 'node:test';
import assert from 'node:assert/strict';
import { validateGuide, allExamGuides } from './validate-exam-guides.mjs';

test('all current guides satisfy their publication contracts', () => {
  for (const { guide, id } of allExamGuides()) validateGuide(guide, id);
});
test('published guides reject spoofed sources, future dates and duplicate anchors', () => {
  const guide = allExamGuides().find(item => item.guide.publishedAt).guide;
  const bad = structuredClone(guide); bad.sources[0].url = 'https://ssc.gov.in.example.com/key';
  assert.throws(() => validateGuide(bad, bad.id), /official/);
  const future = structuredClone(guide); future.publishedAt = '2099-01-01T00:00:00Z';
  assert.throws(() => validateGuide(future, future.id), /publication/);
  const duplicate = structuredClone(guide); duplicate.sections[1].id = duplicate.sections[0].id;
  assert.throws(() => validateGuide(duplicate, duplicate.id), /duplicate/);
});
