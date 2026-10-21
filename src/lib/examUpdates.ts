import fs from 'node:fs';
import path from 'node:path';
import type { ExamUpdate } from './examUpdateRules';

export function listExamUpdates(): ExamUpdate[] {
  const data = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'content/exam-updates.json'), 'utf8')) as ExamUpdate[];
  return data.filter(item => item.published).sort((a, b) => b.publishedAt.localeCompare(a.publishedAt));
}
export function getExamUpdate(slug: string): ExamUpdate | undefined {
  return listExamUpdates().find(item => item.slug === slug);
}
