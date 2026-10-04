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

/* Short plain-English copy for cards and the top of subject pages; the long
   summary/overview stays on the topic page and below the subject's topic grid. */
type Blurbs = { sections: Record<string, string>; topics: Record<string, string> };
let blurbs: Blurbs | null = null;
const getBlurbs = () => (blurbs ??= readJson<Blurbs>('blurbs.json') ?? { sections: {}, topics: {} });

export function topicBlurb(t: Pick<Topic, 'sectionId' | 'id' | 'summary'>): string {
  return getBlurbs().topics[`${t.sectionId}/${t.id}`] ?? t.summary;
}

export function sectionIntro(id: SectionId): string | undefined {
  return getBlurbs().sections[id];
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
  /** exam id; omitted = ssc-cgl */
  exam?: string;
  /** display names per section (e.g. CAT shows VARC / DILR / QA); default = subject name */
  sectionNames?: Partial<Record<SectionId, string>>;
}

export const MOCK_DEFS: MockDef[] = [
  {
    id: 't1-real-2025-0926-s3', title: 'CGL 2025 Tier 1 — real paper, 26 Sept Shift 3', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 26 Sept 2025 (Shift 3), official answers, original step-by-step solutions. 92 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0912-s1', title: 'CGL 2025 Tier 1 — real paper, 12 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 12 Sept 2025 (Shift 1), official answers, original step-by-step solutions. 90 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0912-s2', title: 'CGL 2025 Tier 1 — real paper, 12 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 12 Sept 2025 (Shift 2), official answers, original step-by-step solutions. 89 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0913-s1', title: 'CGL 2025 Tier 1 — real paper, 13 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 13 Sept 2025 (Shift 1), official answers, original step-by-step solutions. 92 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0913-s2', title: 'CGL 2025 Tier 1 — real paper, 13 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 13 Sept 2025 (Shift 2), official answers, original step-by-step solutions. 92 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0914-s1', title: 'CGL 2025 Tier 1 — real paper, 14 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 14 Sept 2025 (Shift 1), official answers, original step-by-step solutions. 94 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0914-s2', title: 'CGL 2025 Tier 1 — real paper, 14 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 14 Sept 2025 (Shift 2), official answers, original step-by-step solutions. 89 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0915-s1', title: 'CGL 2025 Tier 1 — real paper, 15 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 15 Sept 2025 (Shift 1), official answers, original step-by-step solutions. 92 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0915-s2', title: 'CGL 2025 Tier 1 — real paper, 15 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 15 Sept 2025 (Shift 2), official answers, original step-by-step solutions. 91 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0916-s1', title: 'CGL 2025 Tier 1 — real paper, 16 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 16 Sept 2025 (Shift 1), official answers, original step-by-step solutions. 84 questions — passage-based and a few unverifiable ones are left out.',
  },
  {
    id: 't1-real-2025-0916-s2', title: 'CGL 2025 Tier 1 — real paper, 16 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 16 Sept 2025 (Shift 2), official answers, original step-by-step solutions. 89 questions — passage-based and a few unverifiable ones are left out.',
  },
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
  // ---------- other exams ----------
  {
    id: 'chsl-t1-real-2025-1112-s2', title: 'CHSL 2025 Tier 1 — real paper, 12 Nov Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['english', 'reasoning', 'quant', 'ga'], open: true,
    exam: 'ssc-chsl',
    blurb: 'Real questions from the SSC CHSL 2025 Tier 1 paper held on 12 Nov 2025 (Shift 2), official answers, original step-by-step solutions. 95 questions — a few passage-based and unverifiable ones are left out.',
  },
  {
    id: 'chsl-t1-real-2025-1113-s1', title: 'CHSL 2025 Tier 1 — real paper, 13 Nov Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['english', 'ga', 'quant', 'reasoning'], open: true,
    exam: 'ssc-chsl',
    blurb: 'Real questions from the SSC CHSL 2025 Tier 1 paper held on 13 Nov 2025 (Shift 1), official answers, original step-by-step solutions. 95 questions — a few passage-based and unverifiable ones are left out.',
  },
  {
    id: 'gd-real-2026-0504-s1', title: 'GD Constable 2026 — real paper, 4 May Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 4 May 2026 (Shift 1), official answers, original step-by-step solutions. 80 questions · 160 marks.',
  },
  {
    id: 'gd-real-2026-0505-s1', title: 'GD Constable 2026 — real paper, 5 May Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['english', 'ga', 'quant', 'reasoning'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 5 May 2026 (Shift 1), official answers, original step-by-step solutions. 76 of the 80 questions — a few passage-based and unverifiable ones are left out.',
  },
  {
    id: 'mts-real-2025-0205-s1', title: 'MTS 2025 — real paper, 5 Feb 2026 Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 90, plus: 3, minus: 0, sections: ['quant', 'reasoning', 'ga', 'english'], open: true,
    exam: 'ssc-mts',
    blurb: 'Real questions from the SSC MTS 2025 paper held on 5 Feb 2026 (Shift 1) — Session 1 + Session 2 in one sitting, official answers, original solutions. 89 questions · 270 marks · no negative marking.',
  },
  {
    id: 'mts-real-2025-0205-s2', title: 'MTS 2025 — real paper, 5 Feb 2026 Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 90, plus: 3, minus: 0, sections: ['quant', 'reasoning', 'ga', 'english'], open: true,
    exam: 'ssc-mts',
    blurb: 'Real questions from the SSC MTS 2025 paper held on 5 Feb 2026 (Shift 2) — official answers, original step-by-step solutions. 87 questions · no negative marking.',
  },
  {
    id: 'ntpc-cbt1-mock-1', title: 'NTPC CBT 1 Full Mock 1', kind: 'full', tier: 1,
    durationMin: 90, plus: 1, minus: 0.33, sections: ['ga', 'quant', 'reasoning'], open: true,
    exam: 'rrb-ntpc',
    blurb: '100 questions · 100 marks · 90 minutes · −0.33 per wrong answer. GA 40, Maths 30, Reasoning 30 — real CBT-1 difficulty.',
  },
  {
    id: 'groupd-cbt-mock-1', title: 'Group D CBT Full Mock 1', kind: 'full', tier: 1,
    durationMin: 90, plus: 1, minus: 0.33, sections: ['quant', 'reasoning', 'ga'], open: true,
    exam: 'rrb-group-d',
    blurb: '100 questions · 100 marks · 90 minutes · −0.33 per wrong answer. Maths 25, Reasoning 30, General Science + GA 45.',
  },
  {
    id: 'cat-mock-1', title: 'CAT Full Mock 1', kind: 'full', tier: 1,
    durationMin: 120, plus: 3, minus: 1, sections: ['english', 'reasoning', 'quant'], open: true,
    exam: 'cat',
    sectionNames: { english: 'VARC', reasoning: 'DILR', quant: 'QA' },
    blurb: 'CAT pattern — VARC 24, DILR 22, QA 22 · 68 questions · 198 marks · +3 / −1 · 40 minutes per section (try keeping 40 each in this combined 120-minute run).',
  },
  {
    id: 'cpo-p1-real-2025-1209-s1', title: 'CPO 2025 Paper 1 — real paper, 9 Dec Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 1, minus: 0.25, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-cpo',
    blurb: 'Real questions from the SSC CPO 2025 Paper 1 held on 9 Dec 2025 (Shift 1) — the pre-2026 200-question pattern. Official answers, original step-by-step solutions. 195 questions · 200 marks · −0.25 per wrong answer.',
  },
  {
    id: 'ibps-po-pre-mock-1', title: 'IBPS PO Prelims Mock 1', kind: 'full', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['english', 'quant', 'reasoning'], open: true,
    exam: 'ibps-po',
    blurb: 'Prelims pattern — English 30, Quant 35, Reasoning 35 · 100 questions · 100 marks · +1 / −0.25 · 20 minutes per section (try keeping 20 each in this combined 60-minute run).',
  },
  {
    id: 'ibps-clerk-pre-mock-1', title: 'IBPS Clerk Prelims Mock 1', kind: 'full', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['english', 'quant', 'reasoning'], open: true,
    exam: 'ibps-clerk',
    blurb: 'Prelims pattern — English 30, Quant 35, Reasoning 35 · 100 questions · 100 marks · +1 / −0.25 · 20 minutes per section (try keeping 20 each in this combined 60-minute run).',
  },
];

export function getMock(id: string): Mock | null {
  const def = MOCK_DEFS.find((m) => m.id === id);
  if (!def) return null;
  const sections = def.sections
    .map((sid) => {
      const part = readExam<{ questions: Question[] }>(def.exam ?? 'ssc-cgl', `mocks/parts/${id}--${sid}.json`);
      if (!part) return null;
      return { sectionId: sid, name: def.sectionNames?.[sid] ?? SECTION_META[sid].name, questions: part.questions };
    })
    .filter((s): s is NonNullable<typeof s> => !!s && s.questions.length > 0);
  if (sections.length === 0) return null;
  const { sections: _unused, ...rest } = def;
  void _unused;
  return { ...rest, sections };
}

export function listMocks(examId = 'ssc-cgl'): (MockDef & { available: boolean; questionCount: number })[] {
  return MOCK_DEFS.filter((d) => (d.exam ?? 'ssc-cgl') === examId).map((d) => {
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
