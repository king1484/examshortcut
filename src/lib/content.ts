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

// ---------- strategy guides (content/exams/<exam>/guides/*.json) ----------
export interface Guide {
  id: string; title: string; description: string; intro: string;
  sections: { id: string; title: string; body: string }[];
  faqs?: { q: string; a: string }[];
  related?: string[];
  lastVerified?: string;
}
/** Display order for the guides index; anything not listed follows alphabetically. */
const GUIDE_ORDER = ['preparation-strategy', 'study-plan-30-days', 'study-plan-60-days', 'study-plan-90-days', 'best-books', 'tier-2-strategy', 'cgl-vs-chsl'];
export function listGuides(examId = 'ssc-cgl'): Guide[] {
  const dir = path.join(EXAMS, examId, 'guides');
  if (!fs.existsSync(dir)) return [];
  const rank = (id: string) => { const i = GUIDE_ORDER.indexOf(id); return i < 0 ? 99 : i; };
  return fs.readdirSync(dir).filter((f) => f.endsWith('.json'))
    .map((f) => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf-8')) as Guide)
    .sort((a, b) => rank(a.id) - rank(b.id) || a.id.localeCompare(b.id));
}
export function getGuide(id: string, examId = 'ssc-cgl'): Guide | null {
  return listGuides(examId).find((g) => g.id === id) ?? null;
}

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
// BEGIN VERIFIED PYQ IMPORTS
{
  "id": "up-police-real-2024-0823-s1",
  "title": "UP Police Constable — 23 Aug 2024 Shift 1 (verified subset)",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 120,
  "blurb": "120 source questions fully imported with answers and original explanations. Excludes 30 of the source's 150 questions: unavailable figures, ambiguous statements, suspect keys or insufficiently verified items. General Hindi is preserved in Hindi; this is a reduced-question practice test, not the full 150-question paper.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "quant",
    "reasoning",
    "english",
    "ga"
  ],
  "exam": "up-police",
  "sectionNames": {
    "english": "General Hindi"
  },
  "open": true
},
{
  "id": "ibps-po-pattern-2025-0817",
  "title": "IBPS PO Prelims — 17 Aug 2025 memory-based subset",
  "kind": "pyq-pattern",
  "tier": 1,
  "durationMin": 60,
  "blurb": "65 verified questions from a publicly published memory-based paper, with all five original options, imported answers and original explanations. Not an official question paper. 35 source questions are omitted: image-only data, unverified puzzles, ambiguous items and the longer reading passage. This is a reduced practice subset of the 100-question source.",
  "plus": 1,
  "minus": 0.25,
  "sections": [
    "reasoning",
    "quant",
    "english"
  ],
  "exam": "ibps-po",
  "open": true
},
{
  "id": "up-police-real-2024-0824-s1",
  "title": "UP Police Constable — 24 Aug 2024 Shift 1 (verified subset)",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 120,
  "blurb": "120 source questions imported with answers and original explanations. 30 of 150 source items are omitted because figures, passage context, wording, keys or facts could not be adequately verified. General Hindi is preserved. This is a reduced-question practice test, not the full 150-question paper.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "quant",
    "reasoning",
    "english",
    "ga"
  ],
  "exam": "up-police",
  "sectionNames": {
    "english": "General Hindi"
  },
  "open": true
},
{
  "id": "up-police-real-2024-0823-s2",
  "title": "UP Police Constable — 23 Aug 2024 Shift 2 (verified subset)",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 120,
  "blurb": "110 source questions fully imported with answers and original explanations. Omits 40 of 150 source items with unavailable figures, conflicting keys, ambiguous wording, unverified facts or passage requirements. Hindi is preserved; dated current affairs refer to the source exam context. This is a reduced-question practice test, not the full paper.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "quant",
    "reasoning",
    "english",
    "ga"
  ],
  "exam": "up-police",
  "sectionNames": {
    "english": "General Hindi"
  },
  "open": true
},
{
  "id": "ibps-po-pattern-2025-0824",
  "title": "IBPS PO Prelims — 24 Aug 2025 memory-based subset",
  "kind": "pyq-pattern",
  "tier": 1,
  "durationMin": 60,
  "blurb": "84 verified source questions from a publicly published memory-based paper, with all five original options, imported answers and original explanations. Not an official paper. Omits 16 of the source’s 100 questions with missing figures/context, malformed choices, conflicting keys or unresolved ambiguities. This is a reduced-question practice test with all three sections.",
  "plus": 1,
  "minus": 0.25,
  "sections": [
    "reasoning",
    "quant",
    "english"
  ],
  "exam": "ibps-po",
  "open": true
},
{
  "id": "ibps-po-pattern-2025-0823",
  "title": "IBPS PO Prelims — 23 Aug 2025 memory-based subset",
  "kind": "pyq-pattern",
  "tier": 1,
  "durationMin": 60,
  "blurb": "82 verified source questions from a publicly published memory-based paper, with all five original options, imported answers and original explanations. Not an official paper. Omits 18 of the source’s 100 questions with missing figures/context, malformed choices, conflicting keys or unresolved ambiguities. This is a reduced-question practice test with all three sections.",
  "plus": 1,
  "minus": 0.25,
  "sections": [
    "reasoning",
    "quant",
    "english"
  ],
  "exam": "ibps-po",
  "open": true
},
{
  "id": "cat-real-2025-1130-s2",
  "title": "CAT 2025 Slot 2 · complete verified paper",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 120,
  "blurb": "68 questions imported across VARC, DILR and QA, including genuine TITA numeric questions, with original worked explanations. This timed test uses the complete published slot structure.",
  "plus": 3,
  "minus": 1,
  "sections": [
    "english",
    "reasoning",
    "quant"
  ],
  "exam": "cat",
  "sectionNames": {
    "english": "VARC",
    "reasoning": "DILR",
    "quant": "QA"
  },
  "open": true
},
{
  "id": "cat-real-2025-1130-s3",
  "title": "CAT 2025 Slot 3 · complete verified paper",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 120,
  "blurb": "68 questions imported across VARC, DILR and QA, including genuine TITA numeric questions, with original worked explanations. This timed test uses the complete published slot structure.",
  "plus": 3,
  "minus": 1,
  "sections": [
    "english",
    "reasoning",
    "quant"
  ],
  "exam": "cat",
  "sectionNames": {
    "english": "VARC",
    "reasoning": "DILR",
    "quant": "QA"
  },
  "open": true
},
{
  "id": "t1-real-2025-0918-s1",
  "title": "SSC CGL 2025 (Held On: 18 Sept, 2025 Shift 1) (verified subset)",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "reasoning",
    "ga",
    "quant",
    "english"
  ],
  "exam": "ssc-cgl",
  "blurb": "81 verified source questions imported with answers and original explanations. 19 source questions omitted because passage or figure context, wording, keys or facts could not be adequately verified. This is a reduced-question timed practice test.",
  "open": true
},
{
  "id": "t1-real-2025-0919-s2",
  "title": "SSC CGL 2025 (Held On: 19 Sept, 2025 Shift 2) (verified subset)",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "reasoning",
    "ga",
    "quant",
    "english"
  ],
  "exam": "ssc-cgl",
  "blurb": "84 verified source questions imported with answers and original explanations. 16 source questions omitted because passage or figure context, wording, keys or facts could not be adequately verified. This is a reduced-question timed practice test.",
  "open": true
},
{
  "id": "t1-real-2025-0922-s3",
  "title": "SSC CGL 2025 (Held On: 22 Sept, 2025 Shift 3) (verified subset)",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "reasoning",
    "ga",
    "quant",
    "english"
  ],
  "exam": "ssc-cgl",
  "blurb": "82 verified source questions imported with answers and original explanations. 18 source questions omitted because passage or figure context, wording, keys or facts could not be adequately verified. This is a reduced-question timed practice test.",
  "open": true
},
{
  "id": "alp-real-2024-1125-s2",
  "title": "RRB ALP CBT 1 · 25 Nov 2024 Shift 2 · 66 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "66 actual questions imported from the 25 Nov 2024 Shift 2 response-paper PDF, with original worked solutions. This is a partial paper: Quant 17, Reasoning 21, Ga 28. Image-dependent, unreadable, incomplete or disputed items are omitted. The 60-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-alp",
  "open": true
},
{
  "id": "alp-real-2024-1126-s3",
  "title": "RRB ALP CBT 1 · 26 Nov 2024 Shift 3 · 71 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "71 actual questions imported from the 26 Nov 2024 Shift 3 response-paper PDF, with original worked solutions. This is a partial paper: Quant 20, Reasoning 23, Ga 28. Image-dependent, unreadable, incomplete or disputed items are omitted. The 60-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-alp",
  "open": true
},
{
  "id": "alp-real-2024-1127-s1",
  "title": "RRB ALP CBT 1 · 27 Nov 2024 Shift 1 · 70 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "70 actual questions imported from the 27 Nov 2024 Shift 1 response-paper PDF, with original worked solutions. This is a partial paper: Quant 16, Reasoning 24, Ga 30. Image-dependent, unreadable, incomplete or disputed items are omitted. The 60-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-alp",
  "open": true
},
{
  "id": "groupd-real-2025-1201-s1",
  "title": "RRB Group D CBT · 01 Dec 2025 Shift 1 · 95 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "95 actual questions imported from the 01 Dec 2025 Shift 1 response-paper PDF, with original worked solutions. This is a partial paper: Quant 22, Reasoning 29, Ga 44. Image-dependent, unreadable, incomplete or disputed items are omitted. The 90-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-group-d",
  "open": true
},
{
  "id": "je-real-2024-1216-s1",
  "title": "RRB JE CBT 1 · 16 Dec 2024 Shift 1 · 90 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "90 actual questions imported from the 16 Dec 2024 Shift 1 response-paper PDF, with original worked solutions. This is a partial paper: Quant 28, Reasoning 23, Ga 39. Image-dependent, unreadable, incomplete or disputed items are omitted. The 90-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-je",
  "open": true
},
{
  "id": "ntpc-g-real-2026-0317-s1",
  "title": "RRB NTPC Graduate CBT 1 · 17 Mar 2026 Shift 1 · 91 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "91 actual questions imported from the 17 Mar 2026 Shift 1 response-paper PDF, with original worked solutions. This is a partial paper: Quant 21, Reasoning 30, Ga 40. Image-dependent, unreadable, incomplete or disputed items are omitted. The 90-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-ntpc",
  "open": true
},
{
  "id": "ntpc-g-real-2026-0318-s1",
  "title": "RRB NTPC Graduate CBT 1 · 18 Mar 2026 Shift 1 · 84 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "84 actual questions imported from the 18 Mar 2026 Shift 1 response-paper PDF, with original worked solutions. This is a partial paper: Quant 19, Reasoning 30, Ga 35. Image-dependent, unreadable, incomplete or disputed items are omitted. The 90-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-ntpc",
  "open": true
},
{
  "id": "ntpc-g-real-2026-0319-s1",
  "title": "RRB NTPC Graduate CBT 1 · 19 Mar 2026 Shift 1 · 90 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "90 actual questions imported from the 19 Mar 2026 Shift 1 response-paper PDF, with original worked solutions. This is a partial paper: Quant 23, Reasoning 30, Ga 37. Image-dependent, unreadable, incomplete or disputed items are omitted. The 90-minute practice timer is the original paper duration despite the reduced question count.",
  "plus": 1,
  "minus": 0.33,
  "sections": [
    "quant",
    "reasoning",
    "ga"
  ],
  "exam": "rrb-ntpc",
  "open": true
},
{
  "id": "chsl-t1-real-2025-1114-s3",
  "title": "CHSL 2025 Tier 1 · 14 Nov 2025 Shift 3 · 72 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "72 verified text questions imported from the 14 Nov 2025 Shift 3 paper, with original worked solutions. This is a partial paper: English 16, Reasoning 16, Quant 24, GA 16. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. The 60-minute practice timer is the original paper duration, despite the reduced question count.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "english",
    "reasoning",
    "quant",
    "ga"
  ],
  "exam": "ssc-chsl",
  "open": true
},
{
  "id": "chsl-t1-real-2025-1115-s1",
  "title": "CHSL 2025 Tier 1 · 15 Nov 2025 Shift 1 · 81 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "81 verified text questions imported from the 15 Nov 2025 Shift 1 paper, with original worked solutions. This is a partial paper: English 16, Reasoning 24, Quant 21, GA 20. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. The 60-minute practice timer is the original paper duration, despite the reduced question count.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "english",
    "reasoning",
    "quant",
    "ga"
  ],
  "exam": "ssc-chsl",
  "open": true
},
{
  "id": "chsl-t1-real-2025-1118-s1",
  "title": "CHSL 2025 Tier 1 · 18 Nov 2025 Shift 1 · 85 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "85 verified text questions imported from the 18 Nov 2025 Shift 1 paper, with original worked solutions. This is a partial paper: English 20, Reasoning 22, Quant 25, GA 18. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. The 60-minute practice timer is the original paper duration, despite the reduced question count.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "english",
    "reasoning",
    "quant",
    "ga"
  ],
  "exam": "ssc-chsl",
  "open": true
},
{
  "id": "chsl-t1-real-2025-1119-s2",
  "title": "CHSL 2025 Tier 1 · 19 Nov 2025 Shift 2 · 86 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "86 verified text questions imported from the 19 Nov 2025 Shift 2 paper, with original worked solutions. This is a partial paper: English 16, Reasoning 25, Quant 25, GA 20. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. The 60-minute practice timer is the original paper duration, despite the reduced question count.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "english",
    "reasoning",
    "quant",
    "ga"
  ],
  "exam": "ssc-chsl",
  "open": true
},
{
  "id": "cpo-p1-real-2025-1211-s1",
  "title": "CPO 2025 Paper 1 · 11 Dec 2025 Shift 1 · 76 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 120,
  "blurb": "76 verified text questions imported from the 11 Dec 2025 Shift 1 paper, with original worked solutions. This is a partial paper: English 21, Reasoning 14, Quant 23, GA 18. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. The 120-minute practice timer is the original paper duration, despite the reduced question count.",
  "plus": 1,
  "minus": 0.25,
  "sections": [
    "reasoning",
    "ga",
    "quant",
    "english"
  ],
  "exam": "ssc-cpo",
  "open": true
},
{
  "id": "cpo-p1-real-2025-1211-s2",
  "title": "CPO 2025 Paper 1 · 11 Dec 2025 Shift 2 · 77 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 120,
  "blurb": "77 verified text questions imported from the 11 Dec 2025 Shift 2 paper, with original worked solutions. This is a partial paper: English 18, Reasoning 16, Quant 23, GA 20. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. The 120-minute practice timer is the original paper duration, despite the reduced question count.",
  "plus": 1,
  "minus": 0.25,
  "sections": [
    "reasoning",
    "ga",
    "quant",
    "english"
  ],
  "exam": "ssc-cpo",
  "open": true
},
{
  "id": "gd-real-2026-0429-s1",
  "title": "GD Constable 2026 · 29 Apr 2026 Shift 1 · 67 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 60,
  "blurb": "67 verified text questions imported from the 29 Apr 2026 Shift 1 paper, with original worked solutions. This is a partial paper: English 10, Reasoning 18, Quant 20, GA 19. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. The 60-minute practice timer is the original paper duration, despite the reduced question count.",
  "plus": 2,
  "minus": 0.5,
  "sections": [
    "reasoning",
    "ga",
    "quant",
    "english"
  ],
  "exam": "ssc-gd",
  "open": true
},
{
  "id": "mts-real-2025-0204-s3",
  "title": "MTS 2025 · 4 Feb 2026 Shift 3 · 73 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "73 verified text questions imported from the 4 Feb 2026 Shift 3 paper, with original worked solutions. This is a partial paper: English 18, Reasoning 17, Quant 15, GA 23. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. Scoring: +3 per correct answer; no penalty in Quant/Reasoning and −1 in GA/English. The practice uses a combined 90-minute timer; separate examination session timing is not simulated.",
  "plus": 3,
  "minus": 0,
  "sections": [
    "quant",
    "reasoning",
    "ga",
    "english"
  ],
  "exam": "ssc-mts",
  "open": true
},
{
  "id": "mts-real-2025-0205-s3",
  "title": "MTS 2025 · 5 Feb 2026 Shift 3 · 75 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "75 verified text questions imported from the 5 Feb 2026 Shift 3 paper, with original worked solutions. This is a partial paper: English 18, Reasoning 19, Quant 16, GA 22. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. Scoring: +3 per correct answer; no penalty in Quant/Reasoning and −1 in GA/English. The practice uses a combined 90-minute timer; separate examination session timing is not simulated.",
  "plus": 3,
  "minus": 0,
  "sections": [
    "quant",
    "reasoning",
    "ga",
    "english"
  ],
  "exam": "ssc-mts",
  "open": true
},
{
  "id": "mts-real-2025-0206-s2",
  "title": "MTS 2025 · 6 Feb 2026 Shift 2 · 71 imported questions",
  "kind": "real-pyq",
  "tier": 1,
  "durationMin": 90,
  "blurb": "71 verified text questions imported from the 6 Feb 2026 Shift 2 paper, with original worked solutions. This is a partial paper: English 19, Reasoning 18, Quant 13, GA 21. Missing passages, unreadable or incomplete items, duplicates and disputed answers are omitted. Scoring: +3 per correct answer; no penalty in Quant/Reasoning and −1 in GA/English. The practice uses a combined 90-minute timer; separate examination session timing is not simulated.",
  "plus": 3,
  "minus": 0,
  "sections": [
    "quant",
    "reasoning",
    "ga",
    "english"
  ],
  "exam": "ssc-mts",
  "open": true
},
// END VERIFIED PYQ IMPORTS
  {
    id: 't1-real-2025-0926-s3', title: 'CGL 2025 Tier 1 — real paper, 26 Sept Shift 3', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 26 Sept 2025 (Shift 3), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0912-s1', title: 'CGL 2025 Tier 1 — real paper, 12 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 12 Sept 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0912-s2', title: 'CGL 2025 Tier 1 — real paper, 12 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 12 Sept 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0913-s1', title: 'CGL 2025 Tier 1 — real paper, 13 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 13 Sept 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0913-s2', title: 'CGL 2025 Tier 1 — real paper, 13 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 13 Sept 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0914-s1', title: 'CGL 2025 Tier 1 — real paper, 14 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 14 Sept 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0914-s2', title: 'CGL 2025 Tier 1 — real paper, 14 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 14 Sept 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0915-s1', title: 'CGL 2025 Tier 1 — real paper, 15 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 15 Sept 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0915-s2', title: 'CGL 2025 Tier 1 — real paper, 15 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 15 Sept 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0916-s1', title: 'CGL 2025 Tier 1 — real paper, 16 Sept Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 16 Sept 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-real-2025-0916-s2', title: 'CGL 2025 Tier 1 — real paper, 16 Sept Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Real questions from the SSC CGL 2025 Tier 1 paper held on 16 Sept 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 't1-pyq-2025', title: 'CGL 2025 Tier 1 — PYQ-pattern paper', kind: 'pyq-pattern', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: 'Same topic-wise distribution and difficulty as the actual CGL 2025 Tier 1 shifts, with freshly written questions.',
  },
  {
    id: 't1-mock-1', title: 'Tier 1 Full Mock 1', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer.',
  },
  {
    id: 't1-mock-2', title: 'Tier 1 Full Mock 2', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer.',
  },
  {
    id: 't1-mock-3', title: 'Tier 1 Full Mock 3', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'],
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer.',
  },
  {
    id: 't1-mock-4', title: 'Tier 1 Full Mock 4', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer.',
  },
  {
    id: 't1-mock-5', title: 'Tier 1 Full Mock 5', kind: 'full', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    blurb: '100 questions · 200 marks · 60 minutes · −0.50 per wrong answer.',
  },
  {
    id: 't2-mock-1', title: 'Tier 2 Paper 1 Full Mock 1', kind: 'full', tier: 2,
    durationMin: 135, plus: 3, minus: 1, sections: ['quant', 'reasoning', 'english', 'ga', 'computer'],
    blurb: '150 questions · Maths, Reasoning, English, GA + Computer module · +3 / −1.',
  },
  {
    id: 't2-mock-2', title: 'Tier 2 Paper 1 Full Mock 2', kind: 'full', tier: 2,
    durationMin: 135, plus: 3, minus: 1, sections: ['quant', 'reasoning', 'english', 'ga', 'computer'], open: true,
    blurb: '150 questions · Maths, Reasoning, English, GA + Computer module · +3 / −1.',
  },
  // ---------- other exams ----------
  {
    id: 'chsl-t1-real-2025-1112-s2', title: 'CHSL 2025 Tier 1 — real paper, 12 Nov Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['english', 'reasoning', 'quant', 'ga'], open: true,
    exam: 'ssc-chsl',
    blurb: 'Real questions from the SSC CHSL 2025 Tier 1 paper held on 12 Nov 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 'chsl-t1-real-2025-1113-s1', title: 'CHSL 2025 Tier 1 — real paper, 13 Nov Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['english', 'ga', 'quant', 'reasoning'], open: true,
    exam: 'ssc-chsl',
    blurb: 'Real questions from the SSC CHSL 2025 Tier 1 paper held on 13 Nov 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'gd-real-2026-0504-s1', title: 'GD Constable 2026 — real paper, 4 May Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 4 May 2026 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'gd-real-2026-0505-s1', title: 'GD Constable 2026 — real paper, 5 May Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['english', 'ga', 'quant', 'reasoning'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 5 May 2026 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'gd-real-2026-0428-s1', title: 'GD Constable 2026 — real paper, 28 Apr Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 28 Apr 2026 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'gd-real-2026-0428-s2', title: 'GD Constable 2026 — real paper, 28 Apr Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 28 Apr 2026 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 'gd-real-2026-0506-s1', title: 'GD Constable 2026 — real paper, 6 May Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 6 May 2026 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'gd-real-2026-0506-s2', title: 'GD Constable 2026 — real paper, 6 May Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 2, minus: 0.5, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-gd',
    blurb: 'Real questions from the SSC GD Constable 2026 paper held on 6 May 2026 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 'mts-real-2025-0205-s1', title: 'MTS 2025 — real paper, 5 Feb 2026 Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 90, plus: 3, minus: 0, sections: ['quant', 'reasoning', 'ga', 'english'], open: true,
    exam: 'ssc-mts',
    blurb: 'Real questions from the SSC MTS 2025 paper held on 5 Feb 2026 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'mts-real-2025-0205-s2', title: 'MTS 2025 — real paper, 5 Feb 2026 Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 90, plus: 3, minus: 0, sections: ['quant', 'reasoning', 'ga', 'english'], open: true,
    exam: 'ssc-mts',
    blurb: 'Real questions from the SSC MTS 2025 paper held on 5 Feb 2026 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 'ntpc-cbt1-mock-1', title: 'NTPC CBT 1 Full Mock 1', kind: 'full', tier: 1,
    durationMin: 90, plus: 1, minus: 0.33, sections: ['ga', 'quant', 'reasoning'], open: true,
    exam: 'rrb-ntpc',
    blurb: '100 questions · 100 marks · 90 minutes · −0.33 per wrong answer. GA 40, Maths 30, Reasoning 30.',
  },
  {
    id: 'ntpc-g-real-2026-0316-s1', title: 'NTPC CBT 1 — real paper, 16 Mar 2026 Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 90, plus: 1, minus: 0.33, sections: ['ga', 'quant', 'reasoning'], open: true,
    exam: 'rrb-ntpc',
    blurb: 'Real questions from the RRB NTPC CBT 1 paper held on 16 Mar 2026 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'groupd-cbt-mock-1', title: 'Group D CBT Full Mock 1', kind: 'full', tier: 1,
    durationMin: 90, plus: 1, minus: 0.33, sections: ['quant', 'reasoning', 'ga'], open: true,
    exam: 'rrb-group-d',
    blurb: '100 questions · 100 marks · 90 minutes · −0.33 per wrong answer. Maths 25, Reasoning 30, General Science + GA 45.',
  },
  {
    id: 'groupd-real-2025-1127-s1', title: 'Group D CBT 1 — real paper, 27 Nov 2025 Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 90, plus: 1, minus: 0.33, sections: ['quant', 'reasoning', 'ga'], open: true,
    exam: 'rrb-group-d',
    blurb: 'Real questions from the RRB Group D CBT 1 held on 27 Nov 2025 (Shift 1) — memory-based, with answer keys and step-by-step solutions.',
  },
  {
    id: 'cat-mock-1', title: 'CAT Full Mock 1', kind: 'full', tier: 1,
    durationMin: 120, plus: 3, minus: 1, sections: ['english', 'reasoning', 'quant'], open: true,
    exam: 'cat',
    sectionNames: { english: 'VARC', reasoning: 'DILR', quant: 'QA' },
    blurb: 'CAT pattern — VARC 24, DILR 22, QA 22 · 68 questions · 204 marks · +3 / −1 · 40 minutes per section.',
  },
  {
    id: 'cat-real-2023-1126-s1', title: 'CAT 2023 Slot 1 — real paper', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 3, minus: 1, sections: ['english', 'reasoning', 'quant'], open: true,
    exam: 'cat',
    sectionNames: { english: 'VARC', reasoning: 'DILR', quant: 'QA' },
    blurb: 'Real questions from CAT 2023 Slot 1 (26 Nov 2023), official answer key, original step-by-step solutions.',
  },
  {
    id: 'cat-real-2024-1124-s1', title: 'CAT 2024 Slot 1 — real paper', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 3, minus: 1, sections: ['english', 'reasoning', 'quant'], open: true,
    exam: 'cat',
    sectionNames: { english: 'VARC', reasoning: 'DILR', quant: 'QA' },
    blurb: 'Real questions from CAT 2024 Slot 1 (24 Nov 2024), official answer key, original step-by-step solutions.',
  },
  {
    id: 'cat-real-2025-1130-s1', title: 'CAT 2025 Slot 1 — real paper', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 3, minus: 1, sections: ['english', 'reasoning', 'quant'], open: true,
    exam: 'cat',
    sectionNames: { english: 'VARC', reasoning: 'DILR', quant: 'QA' },
    blurb: 'Real questions from CAT 2025 Slot 1 (30 Nov 2025), official answer key, original step-by-step solutions.',
  },
  {
    id: 'cpo-p1-real-2025-1209-s1', title: 'CPO 2025 Paper 1 — real paper, 9 Dec Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 1, minus: 0.25, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-cpo',
    blurb: 'Real questions from the SSC CPO 2025 Paper 1 held on 9 Dec 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'cpo-p1-real-2025-1209-s2', title: 'CPO 2025 Paper 1 — real paper, 9 Dec Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 1, minus: 0.25, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-cpo',
    blurb: 'Real questions from the SSC CPO 2025 Paper 1 held on 9 Dec 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 'cpo-p1-real-2025-1210-s1', title: 'CPO 2025 Paper 1 — real paper, 10 Dec Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 1, minus: 0.25, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-cpo',
    blurb: 'Real questions from the SSC CPO 2025 Paper 1 held on 10 Dec 2025 (Shift 1), official answers, original step-by-step solutions.',
  },
  {
    id: 'cpo-p1-real-2025-1210-s2', title: 'CPO 2025 Paper 1 — real paper, 10 Dec Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 120, plus: 1, minus: 0.25, sections: ['reasoning', 'ga', 'quant', 'english'], open: true,
    exam: 'ssc-cpo',
    blurb: 'Real questions from the SSC CPO 2025 Paper 1 held on 10 Dec 2025 (Shift 2), official answers, original step-by-step solutions.',
  },
  {
    id: 'ibps-po-pre-mock-1', title: 'IBPS PO Prelims Mock 1', kind: 'full', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['english', 'quant', 'reasoning'], open: true,
    exam: 'ibps-po',
    blurb: 'Prelims pattern — English 30, Quant 35, Reasoning 35 · 100 questions · 60 minutes · +1 / −0.25.',
  },
  {
    id: 'ibps-po-real-2026-0822-s1', title: 'IBPS PO 2026 Prelims — real paper, 22 Aug Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['english', 'quant', 'reasoning'], open: true,
    exam: 'ibps-po',
    blurb: 'Real questions from the IBPS PO 2026 prelims held on 22 Aug 2026 (Shift 1) — memory-based, with answer keys and step-by-step solutions.',
  },
  {
    id: 'ibps-po-real-2026-0823-s1', title: 'IBPS PO 2026 Prelims — real paper, 23 Aug Shift 1', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['english', 'quant', 'reasoning'], open: true,
    exam: 'ibps-po',
    blurb: 'Real questions from the IBPS PO 2026 prelims held on 23 Aug 2026 (Shift 1) — memory-based, with answer keys and step-by-step solutions.',
  },
  {
    id: 'ibps-clerk-pre-mock-1', title: 'IBPS Clerk Prelims Mock 1', kind: 'full', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['english', 'quant', 'reasoning'], open: true,
    exam: 'ibps-clerk',
    blurb: 'Prelims pattern — English 30, Numerical Ability 35, Reasoning 35 · 100 questions · 60 minutes · +1 / −0.25.',
  },
  {
    id: 'ibps-clerk-real-2025-1004-s2', title: 'IBPS Clerk 2025 Prelims — real paper, 4 Oct Shift 2', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['quant', 'english', 'reasoning'], open: true,
    exam: 'ibps-clerk',
    blurb: 'Real questions from the IBPS Clerk 2025 prelims held on 4 Oct 2025 (Shift 2) — memory-based, with answer keys and step-by-step solutions.',
  },
  {
    id: 'ibps-clerk-real-2025-1004-s3', title: 'IBPS Clerk 2025 Prelims — real paper, 4 Oct Shift 3', kind: 'real-pyq', tier: 1,
    durationMin: 60, plus: 1, minus: 0.25, sections: ['english', 'quant', 'reasoning'], open: true,
    exam: 'ibps-clerk',
    blurb: 'Real questions from the IBPS Clerk 2025 prelims held on 4 Oct 2025 (Shift 3) — memory-based, with answer keys and step-by-step solutions.',
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
  if (sections.length !== def.sections.length) return null;
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
