import fs from 'node:fs';
import { buildExamUpdateRss } from './exam-update-feeds.mjs';
const items = JSON.parse(fs.readFileSync('content/exam-updates.json', 'utf8'));
fs.writeFileSync('out/exam-updates.xml', buildExamUpdateRss(items));
console.log(`Exam update RSS: ${items.filter(item => item.published).length} articles.`);
