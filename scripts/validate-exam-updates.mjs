import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { isOfficialUpdateUrl, UPDATE_KINDS } from '../src/lib/examUpdateRules.ts';

export function validateExamUpdates(items, now = Date.now()) {
  assert(Array.isArray(items), 'Exam updates must be an array');
  const slugs = new Set();
  for (const item of items) {
    assert(/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(item.slug), 'Invalid update slug');
    assert(!slugs.has(item.slug), `Duplicate article: ${item.slug}`); slugs.add(item.slug);
    assert(typeof item.published === 'boolean', `${item.slug}: explicit publication state required`);
    if (!item.published) continue;
    const at = `${item.slug}: `;
    assert(fs.existsSync(path.join('content/exams', item.examId, 'exam.json')), at + 'unknown exam');
    assert(UPDATE_KINDS.includes(item.kind), at + 'invalid update kind');
    for (const field of ['title', 'summary', 'cycle', 'status']) assert(typeof item[field] === 'string' && item[field].trim(), at + field + ' missing');
    for (const field of ['publishedAt', 'updatedAt', 'verifiedAt']) {
      assert(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})$/.test(item[field]), at + field + ' must include timezone');
      assert(Number.isFinite(Date.parse(item[field])) && Date.parse(item[field]) <= now, at + field + ' invalid or in future');
    }
    assert(Date.parse(item.updatedAt) >= Date.parse(item.publishedAt), at + 'modification predates publication');
    assert(Date.parse(item.verifiedAt) <= Date.parse(item.updatedAt), at + 'source check later than modification');
    if (item.noticeDate) assert(/^\d{4}-\d{2}-\d{2}$/.test(item.noticeDate) && Date.parse(item.noticeDate) <= now, at + 'invalid notice date');
    assert(Array.isArray(item.sources) && item.sources.length, at + 'official source required');
    for (const source of item.sources) assert(source.label && isOfficialUpdateUrl(source.url), at + 'untrusted or unlabelled official link');
    assert(Array.isArray(item.facts) && item.facts.length >= 3, at + 'at least three candidate facts required');
    for (const fact of item.facts) assert(fact.label && fact.value, at + 'empty fact');
    assert(Array.isArray(item.sections) && item.sections.length >= 2, at + 'explanation sections required');
    for (const section of item.sections) assert(section.title && section.body?.length > 50, at + 'empty explanation');
    assert(item.nextSteps?.length >= 2 && item.nextSteps.every(step => typeof step === 'string' && step.trim()), at + 'candidate next steps required');
  }
  return items.filter(item => item.published).length;
}
if (process.argv[1]?.endsWith('validate-exam-updates.mjs')) {
  const items = JSON.parse(fs.readFileSync('content/exam-updates.json', 'utf8'));
  console.log(`Exam notices: ${validateExamUpdates(items)} published articles passed source, cycle, date and content checks.`);
}
