import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { isOfficialUpdateUrl } from '../src/lib/examUpdateRules.ts';

export function validateGuide(guide, id) {
  assert(guide.id === id && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(id), `Guide ID differs from filename: ${id}`);
  for (const key of ['title', 'description', 'intro']) assert(typeof guide[key] === 'string' && guide[key].trim(), `${id}: missing ${key}`);
  assert(guide.sections?.length >= 2, `${id}: sections missing`);
  const ids = new Set();
  for (const section of guide.sections) {
    assert(section.id && !ids.has(section.id), `${id}: duplicate or missing section ID`); ids.add(section.id);
    assert(section.title && section.body?.trim(), `${id}: empty section`);
  }
  if (!guide.publishedAt) return; // Existing legacy guides retain their original fields.
  assert(Number.isFinite(Date.parse(guide.publishedAt)) && Date.parse(guide.publishedAt) <= Date.now(), `${id}: invalid publication date`);
  assert(Date.parse(guide.updatedAt) >= Date.parse(guide.publishedAt) && Date.parse(guide.updatedAt) <= Date.now(), `${id}: invalid modification date`);
  assert(guide.sources?.length && guide.sources.every(source => source.label && isOfficialUpdateUrl(source.url)), `${id}: official labelled sources required`);
  assert(guide.checklist?.length >= 3 && new Set(guide.checklist).size === guide.checklist.length, `${id}: distinct action checklist required`);
  assert(guide.drills?.length >= 2 && guide.drills.every(drill => drill.prompt && drill.answer && drill.explanation), `${id}: worked learning checks required`);
}

export function allExamGuides() {
  return fs.readdirSync('content/exams').flatMap(exam => {
    const dir = path.join('content/exams', exam, 'guides');
    return fs.existsSync(dir) ? fs.readdirSync(dir).filter(file => file.endsWith('.json')).map(file => ({ exam, id: file.slice(0, -5), guide: JSON.parse(fs.readFileSync(path.join(dir, file), 'utf8')) })) : [];
  });
}
if (process.argv[1]?.endsWith('validate-exam-guides.mjs')) {
  const guides = allExamGuides();
  for (const { guide, id } of guides) validateGuide(guide, id);
  console.log(`Exam guides: ${guides.length} passed content and publication checks.`);
}
