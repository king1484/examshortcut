import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { filterExamUpdates, isOfficialUpdateUrl } from '../src/lib/examUpdateRules.ts';
import { validateExamUpdates } from './validate-exam-updates.mjs';
import { buildExamUpdateRss } from './exam-update-feeds.mjs';
const items = JSON.parse(fs.readFileSync('content/exam-updates.json', 'utf8'));

test('official links reject spoofed hosts, credentials and unsafe protocols', () => {
  assert(isOfficialUpdateUrl('https://rrb.digialm.com//EForms/configuredHtml/33244/102815/login.html'));
  assert(isOfficialUpdateUrl('https://ibpsreg.ibps.in/csaxvijul26/'));
  assert(isOfficialUpdateUrl('https://ibpsreg.ibps.in/sbijasrdjl26/oecla_oct26/login.php?appid=public-link'));
  for (const url of ['https://ibpsreg.ibps.in/unverified/', 'https://ibpsreg.ibps.in.evil.example/csaxvijul26/', 'https://ibpsreg.ibps.in/csaxvijul26/extra', 'https://user:pass@ibpsreg.ibps.in/csaxvijul26/']) assert(!isOfficialUpdateUrl(url), url);
  for (const url of ['https://ssc.gov.in/a.pdf', 'https://sbi.bank.in/web/careers/current-openings', 'https://www.ibps.in/', 'https://rrb.digialm.com/EForms/configuredHtml/33128/102593/login.html']) assert(isOfficialUpdateUrl(url));
  for (const url of ['javascript:alert(1)', 'http://ssc.gov.in/', 'https://ssc.gov.in.evil.example/a', 'https://ssc.gov.in@evil.example/', 'https://user:password@ssc.gov.in/', '//ssc.gov.in/', 'https://ssc.gov.in:8443/', 'https://rrb.digialm.com/unverified', 'https://rrb.digialm.com.evil.example/EForms/configuredHtml/']) assert(!isOfficialUpdateUrl(url), url);
});
test('search combines exam, update type and words; drafts remain hidden', () => {
  const fixture = { ...items[0], examId: 'ssc-chsl', kind: 'result', title: 'CHSL 2025 final result', slug: 'example-result', published: true };
  const draft = { ...fixture, published: false, slug: 'hidden-draft' };
  const data = [fixture, { ...fixture, kind: 'schedule', slug: 'example-schedule' }, draft];
  assert(filterExamUpdates(data).every(item => item.published));
  const selected = filterExamUpdates(data, '2025 final', 'ssc-chsl', 'result');
  assert.equal(selected.length, 1);
  assert.equal(selected[0].slug, 'example-result');
  assert.equal(filterExamUpdates(data, 'nonexistent-search').length, 0);
  assert.equal(filterExamUpdates(data, '', '', 'admit-card').length, 0);
});
test('publication requires official evidence and consistent dates', () => {
  assert.equal(validateExamUpdates(items), items.filter(item => item.published).length);
  const bad = structuredClone(items);
  bad[0].publishedAt = '2099-01-01T00:00:00Z';
  assert.throws(() => validateExamUpdates(bad), /future/);
  const unsourced = structuredClone(items); unsourced[0].sources = [];
  assert.throws(() => validateExamUpdates(unsourced), /source required/);
  assert.throws(() => validateExamUpdates([...items, items[0]]), /Duplicate/);
});
test('RSS escapes copy, excludes drafts and keeps original publication dates', () => {
  const story = { ...items[0], title: 'A & B <result>', summary: '"Check" & confirm' };
  const feed = buildExamUpdateRss([story, { ...story, slug: 'draft', published: false }]);
  assert(feed.includes('A &amp; B &lt;result&gt;'));
  assert(feed.includes('&quot;Check&quot; &amp; confirm'));
  assert(feed.includes(`<pubDate>${new Date(story.publishedAt).toUTCString()}</pubDate>`));
  assert(!feed.includes('/draft/'));
  assert.equal((feed.match(/<item>/g) ?? []).length, 1);
  assert.equal(feed, buildExamUpdateRss([story]));
});
