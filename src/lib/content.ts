import fs from 'node:fs';
import path from 'node:path';
import type { Mock, Question, Section, Topic } from './types';
import { SECTION_META, SECTION_ORDER, type SectionId } from './sections';

export { SECTION_META, SECTION_ORDER };
export type { SectionId };

export function getSection(id: SectionId): Section | null {
  return readJson<Section>(`sections/${id}.json`);
}

/* Two layers: `content/core` holds exam-agnostic subjects (sections, topics, current
   affairs) shared by every exam; `content/exams/<examId>` holds one exam's own data
   (pattern, cutoffs, weightage, mocks). */
const CORE = path.join(process.cwd(), 'content', 'core');
const EXAMS = path.join(process.cwd(), 'content', 'exams');

function readFrom<T>(root: string, rel: string): T | null {
  const file = path.join(root, rel);
  if (!fs.existsSync(file)) return null;
  return JSON.parse(fs.readFileSync(file, 'utf-8')) as T;
}
const readJson = <T,>(rel: string) => readFrom<T>(CORE, rel);
const readExam = <T,>(examId: string, rel: string) => readFrom<T>(path.join(EXAMS, examId), rel);

export function listTopics(sectionId: SectionId): Topic[] {
  const dir = path.join(CORE, 'topics', sectionId);
  if (!fs.existsSync(dir)) return [];
  const topics = fs
    .readdirSync(dir)
    .filter((f) => f.endsWith('.json'))
    .map((f) => readJson<Topic>(`topics/${sectionId}/${f}`)!)
    .filter(Boolean);
  const section = getSection(sectionId);
  const order = section?.topics ?? [];
  return topics.sort((a, b) => {
    const ia = order.indexOf(a.id), ib = order.indexOf(b.id);
    if (ia !== -1 && ib !== -1) return ia - ib;
    if (ia !== -1) return -1;
    if (ib !== -1) return 1;
    return (a.order ?? 99) - (b.order ?? 99);
  });
}

export function getTopic(sectionId: SectionId, topicId: string): Topic | null {
  return readJson<Topic>(`topics/${sectionId}/${topicId}.json`);
}

export function availableSections(): SectionId[] {
  return SECTION_ORDER.filter((s) => listTopics(s).length > 0);
}

// ---------- exam / cutoffs / weightage (shapes are loose; rendered defensively) ----------
/* eslint-disable @typescript-eslint/no-explicit-any */
export function getExam(examId = 'ssc-cgl'): any | null { return readExam(examId, 'exam.json'); }
export function getCutoffs(examId = 'ssc-cgl'): any | null { return readExam(examId, 'cutoffs.json'); }
export function getWeightage(examId = 'ssc-cgl'): any | null { return readExam(examId, 'weightage.json'); }

// ---------- current affairs (core, month-wise per year) ----------
export interface CaItem { date: string; category: string; headline: string; detail: string; examFacts?: string[] }
export interface CaMonth { month: string; label: string; items: CaItem[]; quiz?: Question[] }
export interface CaYear { year: number; months: CaMonth[] }

export function listCaYears(): number[] {
  const dir = path.join(CORE, 'current-affairs');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((f) => /^\d{4}\.json$/.test(f)).map((f) => Number(f.slice(0, 4)))
    .filter((y) => (getCaYear(y)?.months.length ?? 0) > 0).sort((a, b) => b - a);
}
export function getCaYear(year: number): CaYear | null {
  const y = readJson<CaYear>(`current-affairs/${year}.json`);
  if (!y) return null;
  return { ...y, months: [...(y.months ?? [])].filter((m) => m.items?.length).sort((a, b) => b.month.localeCompare(a.month)) };
}

// ---------- mocks ----------
/* `open` mocks are free without an account (and crawlable); the rest need a login,
   which is only used to save attempts and scores. */
interface MockDef {
  id: string; title: string; kind: Mock['kind']; tier: 1 | 2; durationMin: number;
  plus: number; minus: number; blurb: string; sections: SectionId[]; open?: boolean;
}

export const MOCK_DEFS: MockDef[] = [
  {
    id: 't1-pyq-2025', title: 'CGL 2025 Tier 1 — PYQ-pattern paper', kind: 'pyq-pattern', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Same topic-wise distribution and difficulty as the actual CGL 2025 Tier 1 shifts, with freshly written questions.',
  },
  {
    id: 't1-mock-1', title: 'Tier 1 Full Mock 1', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer. Real CBT interface.',
  },
  {
    id: 't1-mock-2', title: 'Tier 1 Full Mock 2', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer. Fresh set, CGL 2025 difficulty.',
  },
  {
    id: 't1-mock-3', title: 'Tier 1 Full Mock 3', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer. Slightly tougher set for the final week.',
  },
  {
    id: 't2-mock-1', title: 'Tier 2 Paper 1 Full Mock 1', kind: 'full', tier: 2,
    durationMin: 135, plus: 3, minus: 1, sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: '150 questions · Maths, Reasoning, English, GA + Computer module · +3 / −1.',
  },
];

export function getMock(id: string): Mock | null {
  const def = MOCK_DEFS.find((m) => m.id === id);
  if (!def) return null;
  const sections = def.sections
    .map((sid) => {
      const part = readExam<{ questions: Question[] }>('ssc-cgl', `mocks/parts/${id}--${sid}.json`);
      if (!part) return null;
      return { sectionId: sid, name: SECTION_META[sid].name, questions: part.questions };
    })
    .filter((s): s is NonNullable<typeof s> => !!s && s.questions.length > 0);
  if (sections.length === 0) return null;
  const { sections: _unused, ...rest } = def;
  void _unused;
  return { ...rest, sections };
}

export function listMocks(): (MockDef & { available: boolean; questionCount: number })[] {
  return MOCK_DEFS.map((d) => {
    const m = getMock(d.id);
    return { ...d, available: !!m && m.sections.length === d.sections.length, questionCount: m ? m.sections.reduce((n, s) => n + s.questions.length, 0) : 0 };
  });
}

// ---------- aggregate ----------
export function allFormulas() {
  return availableSections().map((sid) => ({
    sectionId: sid,
    topics: listTopics(sid)
      .map((t) => ({
        id: t.id, title: t.title,
        subtopics: t.subtopics
          .filter((s) => (s.formulas?.length ?? 0) > 0 || (s.tricks?.length ?? 0) > 0)
          .map((s) => ({ id: s.id, title: s.title, formulas: s.formulas ?? [], tricks: (s.tricks ?? []).map((k) => ({ title: k.title, body: k.body })) })),
      }))
      .filter((t) => t.subtopics.length > 0),
  }));
}

export function contentStats() {
  let topics = 0, questions = 0, formulas = 0, tricks = 0;
  for (const sid of availableSections()) {
    for (const t of listTopics(sid)) {
      topics++;
      questions += (t.practice?.length ?? 0) + (t.solvedExamples?.length ?? 0);
      for (const s of t.subtopics) { formulas += s.formulas?.length ?? 0; tricks += s.tricks?.length ?? 0; }
    }
  }
  for (const m of MOCK_DEFS) { const mk = getMock(m.id); if (mk) questions += mk.sections.reduce((n, s) => n + s.questions.length, 0); }
  return { topics, questions, formulas, tricks };
}
