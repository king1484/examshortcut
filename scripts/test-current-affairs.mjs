import test from 'node:test';
import assert from 'node:assert/strict';
import { changedCurrentAffairsRoutes } from './current-affairs-routes.mjs';

test('discovery covers edited and new months without resubmitting unchanged months', () => {
  const september = { month: '2026-09', items: [{ headline: 'Existing fact' }] };
  const october = { month: '2026-10', items: [{ headline: 'New fact' }], quiz: [] };
  const previous = { year: 2026, months: [september, october] };
  const current = structuredClone(previous);
  current.months[1].quiz.push({ id: 'new-question' });
  assert.deepEqual(changedCurrentAffairsRoutes(current, previous), ['/current-affairs/', '/current-affairs/2026/', '/current-affairs/2026/10/']);
  assert.deepEqual(changedCurrentAffairsRoutes(previous, previous), []);
  assert.deepEqual(changedCurrentAffairsRoutes({ year: 2026, months: [october] }), ['/current-affairs/', '/current-affairs/2026/', '/current-affairs/2026/10/']);
  assert.deepEqual(changedCurrentAffairsRoutes({ year: 2026, months: [{ month: '2026-11', items: [] }] }), []);
});
