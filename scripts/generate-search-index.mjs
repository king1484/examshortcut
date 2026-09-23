#!/usr/bin/env node
/* Builds public/search-index.json from content/ for the client-side search page. */
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const C = path.join(ROOT, 'content', 'ssc-cgl');
const OUT = path.join(ROOT, 'public', 'search-index.json');

const SECTION_NAMES = {
  quant: 'Quantitative Aptitude', reasoning: 'Reasoning', english: 'English Language',
  ga: 'General Awareness', computer: 'Computer',
};

const read = (p) => JSON.parse(fs.readFileSync(p, 'utf8'));
const clean = (s) => String(s ?? '').replace(/\\[\da-zA-Z]+(\{[^}]*\})*/g, ' ').replace(/[#*`$]/g, ' ').replace(/\s+/g, ' ').trim();

const docs = [];
const push = (doc) => docs.push(doc);

// Static pages
[
  ['/ssc-cgl/', 'SSC CGL exam guide pattern eligibility posts salary selection process'],
  ['/ssc-cgl/syllabus/', 'Syllabus all sections topics list'],
  ['/ssc-cgl/mocks/', 'Mock tests free CBT full paper previous year'],
  ['/ssc-cgl/formula-sheet/', 'Formula sheet printable all formulas'],
  ['/ssc-cgl/cutoffs/', 'Cutoff previous years category OBC SC ST EWS trend'],
  ['/ssc-cgl/score-calculator/', 'Score calculator marks normalization safe score'],
  ['/ssc-cgl/weightage/', 'Topic weightage important topics questions per shift'],
  ['/ssc-cgl/ga/current-affairs/', 'Current affairs latest'],
  ['/revision/', 'My revision mistakes bookmarks progress'],
].forEach(([url, text]) => push({ t: 'page', title: clean(text).split(' ').slice(0, 4).join(' '), url, text }));

// Mocks
const mocksDir = path.join(C, 'mocks');
if (fs.existsSync(mocksDir)) {
  for (const f of fs.readdirSync(mocksDir).filter((f) => f.endsWith('.json'))) {
    const m = read(path.join(mocksDir, f));
    push({ t: 'mock', title: m.title || m.id, url: `/ssc-cgl/mocks/${m.id}/`, text: clean(`${m.title} ${m.description || ''} ${m.id}`) });
  }
}

// Topics with formulas / tricks / mistakes as separate docs
const topicsDir = path.join(C, 'topics');
if (fs.existsSync(topicsDir)) {
  for (const sec of fs.readdirSync(topicsDir)) {
    const secDir = path.join(topicsDir, sec);
    if (!fs.statSync(secDir).isDirectory()) continue;
    for (const f of fs.readdirSync(secDir).filter((f) => f.endsWith('.json'))) {
      const tp = read(path.join(secDir, f));
      const url = `/ssc-cgl/${sec}/${tp.id}/`;
      const title = tp.title || tp.id.replace(/-/g, ' ');
      const bits = [title, SECTION_NAMES[sec], ...(tp.subtopics ?? []).map((s) => s.name),
        ...(tp.pyqPatterns ?? []).map((p) => p.pattern), ...(tp.tags ?? [])].map(clean).filter(Boolean);
      push({ t: 'topic', title, section: sec, url, text: bits.join(' · ') });

      for (const st of tp.subtopics ?? []) {
        for (const fo of st.formulas ?? []) {
          push({ t: 'formula', title: fo.name, section: sec, url, text: clean(`${fo.name} ${fo.note ?? ''} ${fo.tex ?? ''} ${title}`) });
        }
        for (const tr of st.tricks ?? []) {
          push({ t: 'trick', title: tr.title, section: sec, url, text: clean(`${tr.title} ${tr.body ?? ''} ${title}`) });
        }
        for (const mi of st.mistakes ?? []) {
          push({ t: 'mistake', title: mi, section: sec, url, text: clean(`${mi} ${title}`) });
        }
      }
    }
  }
}

fs.writeFileSync(OUT, JSON.stringify(docs));
console.log(`search-index.json: ${docs.length} docs`);
