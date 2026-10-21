import test from 'node:test';
import assert from 'node:assert/strict';
import { archiveDates } from '../src/lib/shiftArchive.ts';
import { allShiftParams, resolveSlug, shiftLabel, difficultyColor } from '../src/lib/shifts.ts';

test('the full archive starts on September 30 and exposes gaps without inventing reports', () => {
  const dates = archiveDates('2026-09-30', ['2026-10-21', '2026-09-30', '2026-10-19']);
  assert.equal(dates[0], '2026-09-30');
  assert.equal(dates.at(-1), '2026-10-21');
  assert.equal(dates.length, 22);
  assert(dates.includes('2026-10-20'));
  assert.deepEqual(archiveDates('2026-09-30', []), []);
});

test('September 30 reports resolve and unknown difficulty stays readable', () => {
  assert(allShiftParams().some(route => route.slug === '30-september-shift-2'));
  assert.equal(resolveSlug('ssc-cgl-2026', '30-september-shift-2').shift.status, 'reported');
  assert.equal(shiftLabel({ status: 'pending' }), 'Awaiting sources');
  assert.equal(difficultyColor('Not reported'), 'var(--ink-2)');
});
