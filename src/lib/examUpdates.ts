import fs from 'node:fs';
import path from 'node:path';
import type { ExamUpdate } from './examUpdateRules';
import { sortExamUpdates } from './examUpdateRules';

export function listExamUpdates(): ExamUpdate[] {
  const data = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'content/exam-updates.json'), 'utf8')) as ExamUpdate[];
  return sortExamUpdates(data.filter(item => item.published));
}
export function getExamUpdate(slug: string): ExamUpdate | undefined {
  return listExamUpdates().find(item => item.slug === slug);
}
