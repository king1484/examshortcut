#!/usr/bin/env node
/* Builds public/search-index.json from content/ for the client-side search page. */
import fs from 'node:fs';
import path from 'node:path';
import ts from 'typescript';

const ROOT = process.cwd();
const CORE = path.join(ROOT, 'content', 'core');
const EXAMS = path.join(ROOT, 'content', 'exams');
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
  ['/exams/', 'All exams SSC Railway Banking entrance choose exam'],
  ['/results/', 'Exam results official SSC SBI IBPS UP Police shortlist selection lists'],
  ['/answer-keys/', 'Answer keys response sheets objection windows deadlines fees official releases'],
  ['/exam-updates/', 'Latest exam updates official notices admit cards answer keys dates applications'],
  ['/exams/ssc-cgl/', 'SSC CGL exam guide pattern eligibility posts salary selection process'],
  ['/exams/ssc-chsl/', 'SSC CHSL exam guide pattern eligibility posts salary selection process'],
  ['/exams/ssc-mts/', 'SSC MTS Havaldar exam guide pattern eligibility posts salary selection process'],
  ['/exams/ssc-gd/', 'SSC GD Constable exam guide pattern eligibility posts salary selection process'],
  ['/exams/rrb-ntpc/', 'RRB NTPC exam guide pattern eligibility posts salary selection process'],
  ['/exams/rrb-group-d/', 'RRB Group D exam guide pattern eligibility posts salary selection process'],
  ['/exams/ssc-cpo/', 'SSC CPO Sub Inspector exam guide pattern eligibility posts salary selection process'],
  ['/exams/rrb-alp/', 'RRB ALP Technician Assistant Loco Pilot exam guide pattern eligibility posts salary selection process'],
  ['/exams/rrb-je/', 'RRB JE Junior Engineer exam guide pattern eligibility posts salary selection process'],
  ['/exams/ibps-po/', 'IBPS PO exam guide pattern eligibility posts salary selection process'],
  ['/exams/ibps-clerk/', 'IBPS Clerk exam guide pattern eligibility posts salary selection process'],
  ['/exams/sbi-po/', 'SBI PO exam guide pattern eligibility posts salary selection process'],
  ['/exams/sbi-clerk/', 'SBI Clerk Junior Associate exam guide pattern eligibility posts salary selection process'],
  ['/exams/up-police/', 'UP Police Constable exam guide pattern eligibility posts salary selection process'],
  ['/exams/cat/', 'CAT MBA exam guide pattern eligibility posts salary selection process'],
  ['/learn/', 'Subjects notes syllabus all sections topics list'],
  ['/study-guides/', 'Study guides beginners weak maths English job college revision current affairs preparation'],
  ['/editorial-policy/', 'Content sources corrections automatic shift analysis original lessons imported questions policy'],
  ['/revision-planner/', 'Free revision planner calendar spaced reviews schedule study topics reminders'],
  ['/daily-quiz/', 'Daily quiz today streak practice'],
  ['/exams/ssc-cgl/mocks/', 'Mock tests free CBT full paper previous year'],
  ['/formula-sheet/', 'Formula sheet printable all formulas'],
  ['/exams/ssc-cgl/cutoffs/', 'Cutoff previous years category OBC SC ST EWS trend'],
  ['/exams/ssc-cgl/score-calculator/', 'Score calculator marks normalization safe score'],
  ['/exams/ssc-cgl/weightage/', 'Topic weightage important topics questions per shift'],
  ['/current-affairs/', 'Current affairs monthly yearly quiz GK'],
  ['/login/', 'Login sign in track progress'],
  ['/revision/', 'My revision mistakes bookmarks progress'],
].forEach(([url, text]) => push({ t: 'page', title: clean(text).split(' ').slice(0, 4).join(' '), url, text }));

// Every published notice is searchable; drafts never enter the public index.
const updateFile = path.join(ROOT, 'content/exam-updates.json');
if (fs.existsSync(updateFile)) {
  for (const item of read(updateFile).filter(item => item.published)) {
    push({ t: 'page', title: item.title, url: `/exam-updates/${item.slug}/`, text: clean(`${item.title} ${item.summary} ${item.cycle} ${item.kind}`) });
  }
}

// Use the same catalogue as the pages so guide titles and URLs stay aligned.
const guideCode = ts.transpileModule(fs.readFileSync(path.join(ROOT, 'src/lib/studyGuides.ts'), 'utf8'),
  { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const { STUDY_GUIDES } = await import(`data:text/javascript;base64,${Buffer.from(guideCode).toString('base64')}`);
for (const guide of STUDY_GUIDES) {
  push({ t: 'page', title: guide.title, url: `/study-guides/${guide.slug}/`,
    text: clean(`${guide.title} ${guide.description} ${guide.audience} ${guide.sections.map(s => s.title).join(' ')}`) });
}

// Exam-specific playbooks use the same JSON files as their static pages.
for (const exam of fs.readdirSync(EXAMS)) {
  const dir = path.join(EXAMS, exam, 'guides');
  if (!fs.existsSync(dir)) continue;
  const guides = fs.readdirSync(dir).filter(file => file.endsWith('.json')).map(file => read(path.join(dir, file)));
  if (guides.length) push({ t: 'page', title: `${exam.toUpperCase().replaceAll('-', ' ')} preparation guides`, url: `/exams/${exam}/guides/`, text: clean(guides.map(guide => guide.title).join(' ')) });
  for (const guide of guides) push({ t: 'page', title: guide.title, url: `/exams/${exam}/guides/${guide.id}/`, text: clean(`${guide.description} ${guide.intro} ${guide.sections.map(section => section.title).join(' ')}`) });
}

// Mocks
if (fs.existsSync(EXAMS)) {
  for (const exam of fs.readdirSync(EXAMS)) {
    const partsDir = path.join(EXAMS, exam, 'mocks', 'parts');
    if (!fs.existsSync(partsDir)) continue;
    const ids = [...new Set(fs.readdirSync(partsDir).filter((f) => f.endsWith('.json')).map((f) => f.split('--')[0]))];
    for (const id of ids) {
      const title = id.replace(/^t(\d)-/, 'Tier $1 ').replace(/-/g, ' ');
      push({ t: 'mock', title: `${exam.toUpperCase().replaceAll('-', ' ')} ${title}`, url: `/exams/${exam}/mocks/${id}/`, text: clean(`${exam} mock test ${title}`) });
    }
  }
}

// Current affairs months
const caDir = path.join(CORE, 'current-affairs');
if (fs.existsSync(caDir)) {
  for (const f of fs.readdirSync(caDir).filter((f) => /^\d{4}\.json$/.test(f))) {
    const y = read(path.join(caDir, f));
    for (const m of y.months ?? []) {
      if (!m.items?.length) continue;
      push({ t: 'page', title: `Current affairs ${m.label}`, url: `/current-affairs/${y.year}/${m.month.slice(5)}/`,
        text: clean(`${m.label} current affairs ${m.items.map((i) => i.headline).join(' ')}`).slice(0, 1500) });
    }
  }
}

// Topics with formulas / tricks / mistakes as separate docs
const topicsDir = path.join(CORE, 'topics');
if (fs.existsSync(topicsDir)) {
  for (const sec of fs.readdirSync(topicsDir)) {
    const secDir = path.join(topicsDir, sec);
    if (!fs.statSync(secDir).isDirectory()) continue;
    for (const f of fs.readdirSync(secDir).filter((f) => f.endsWith('.json'))) {
      const tp = read(path.join(secDir, f));
      const url = `/${sec}/${tp.id}/`;
      const title = tp.title || tp.id.replace(/-/g, ' ');
      const bits = [title, SECTION_NAMES[sec], ...(tp.subtopics ?? []).map((s) => s.title),
        ...(tp.pyqPatterns ?? []).map((p) => p.pattern), ...(tp.tags ?? [])].map(clean).filter(Boolean);
      push({ t: 'topic', title, section: sec, url, text: bits.join(' · ') });

      for (const st of tp.subtopics ?? []) {
        push({ t: 'topic', title: `${st.title} — ${title}`, section: sec, url: `${url}learn/${st.id}/`,
          text: clean(`${st.title} ${(st.patterns ?? []).map((p) => p.name).join(' ')} ${(st.concept ?? '').slice(0, 300)}`) });
        for (const fo of st.formulas ?? []) {
          push({ t: 'formula', title: fo.name, section: sec, url, text: clean(`${fo.name} ${fo.note ?? ''} ${fo.tex ?? ''} ${title}`) });
        }
        for (const tr of st.tricks ?? []) {
          push({ t: 'trick', title: tr.title, section: sec, url, text: clean(`${tr.title} ${tr.body ?? ''} ${title}`) });
        }
        for (const mi of st.mistakes ?? []) {
          const mistake = typeof mi === 'string' ? mi : `${mi.wrong} — ${mi.right}`;
          push({ t: 'mistake', title: mistake, section: sec, url, text: clean(`${mistake} ${title}`) });
        }
      }
    }
  }
}

fs.writeFileSync(OUT, JSON.stringify(docs));
console.log(`search-index.json: ${docs.length} docs`);
