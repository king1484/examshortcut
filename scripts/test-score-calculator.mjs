import test from 'node:test';
import assert from 'node:assert/strict';
import { cutoffKey, tier1CutoffEntries, updateAnswerCounts } from '../src/lib/scoreCalculator.ts';

test('answer counts remain whole, finite, nonnegative and within the section size', () => {
  const counts = { correct: 10, wrong: 12, total: 25 };
  assert.deepEqual(updateAnswerCounts(counts, 'correct', 24.9), { correct: 24, wrong: 1, total: 25 });
  assert.deepEqual(updateAnswerCounts(counts, 'wrong', 100), { correct: 0, wrong: 25, total: 25 });
  for (const value of [-1, NaN, Infinity, -Infinity]) {
    assert.deepEqual(updateAnswerCounts(counts, 'wrong', value), { correct: 10, wrong: 0, total: 25 });
  }
  assert.deepEqual(counts, { correct: 10, wrong: 12, total: 25 });
});

test('latest general-post list defaults ahead of specialist lists without mutating input', () => {
  const specialist = { year: 2025, list: 'JSO', cutoffs: { UR: 160 } };
  const general = { year: 2025, list: 'All posts except JSO', cutoffs: { UR: 140 } };
  const older = { year: 2024, list: 'All posts except JSO', cutoffs: { UR: 150 } };
  const original = [specialist, older, general];
  assert.deepEqual(tier1CutoffEntries({ tier1: original }), [general, specialist, older]);
  assert.deepEqual(original, [specialist, older, general]);
  assert.notEqual(cutoffKey(general), cutoffKey(specialist));
  assert.notEqual(cutoffKey(general), cutoffKey(older));
});

test('missing or unpublished cutoff data offers no comparison', () => {
  assert.deepEqual(tier1CutoffEntries(null), []);
  assert.deepEqual(tier1CutoffEntries({ tier1: [{ year: 2026, list: 'Pending', cutoffs: {} }] }), []);
});
