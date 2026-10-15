// Server-only analysis of one mock paper, used to render the crawlable "about this paper"
// section under the (client-side) CBT start screen. Everything here is computed from the
// paper's own question data; nothing is invented. Imports node fs via content.ts.
import type { Mock, Question } from './types';
import { SECTION_ORDER, listTopics, MOCK_DEFS, getMock } from './content';
import type { SectionId } from './sections';
import { getExamInfo } from './exams';
import { wrongAnswerPenalty } from './questionScore';

export interface MockTopicCount { label: string; count: number; link?: { section: SectionId; id: string } }

export interface MockSeoSection {
  sectionId: SectionId;
  name: string;
  count: number;
  marks: number;
  sharePct: number;
  /** average of the per-question time estimates in the data; null when the section has none */
  avgTimeSec: number | null;
  estSec: number | null;
  topics: MockTopicCount[];
  distinctTopics: number;
  taggedCount: number;
  passageQs: number;
  figureQs: number;
  numericQs: number;
  difficulty: { easy: number; medium: number; hard: number } | null;
}

export interface MockSeoSample { sectionId: SectionId; sectionName: string; number: number; q: Question; showSolution: boolean }

export interface MockSeoData {
  examId: string;
  examName: string;
  total: number;
  maxMarks: number;
  durationMin: number;
  secPerQuestion: number;
  penalties: { value: number; count: number }[];
  optionCount: number | null;
  answerSpread: { letter: string; count: number }[];
  estMinutes: number | null;
  difficulty: { easy: number; medium: number; hard: number } | null;
  passageQs: number;
  figureQs: number;
  numericQs: number;
  shortcutQs: number;
  sections: MockSeoSection[];
  topics: MockTopicCount[];
  distinctTopics: number;
  taggedTotal: number;
  dateLabel: string | null;
  shiftLabel: string | null;
  samples: MockSeoSample[];
}

// ---------------------------------------------------------------- topic resolution
type TopicRef = { section: SectionId; id: string; title: string };
let topicIdx: { byTopic: Map<string, TopicRef>; bySub: Map<string, TopicRef>; byId: Map<string, TopicRef> } | null = null;

function index() {
  if (topicIdx) return topicIdx;
  const byTopic = new Map<string, TopicRef>(), bySub = new Map<string, TopicRef>(), byId = new Map<string, TopicRef>();
  for (const sid of SECTION_ORDER) {
    for (const t of listTopics(sid)) {
      const ref = { section: sid, id: t.id, title: t.title };
      byTopic.set(`${sid}/${t.id}`, ref);
      if (!byId.has(t.id)) byId.set(t.id, ref);
      for (const s of t.subtopics ?? []) if (!bySub.has(`${sid}/${s.id}`)) bySub.set(`${sid}/${s.id}`, ref);
    }
  }
  return (topicIdx = { byTopic, bySub, byId });
}

const PLACEHOLDER = /^(unidentified|unknown|misc(ellaneous)?|other|mixed)$/i;
const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);

function topicOf(q: Question, sid: SectionId): { key: string; label: string; link?: { section: SectionId; id: string } } | null {
  const sub = (q as { subtopic?: string }).subtopic?.trim();
  const concept = (q as { concept?: string }).concept?.trim();
  if (sub) {
    const { byTopic, bySub, byId } = index();
    const ref = byTopic.get(`${sid}/${sub}`) ?? bySub.get(`${sid}/${sub}`) ?? byId.get(sub);
    if (ref) return { key: `${ref.section}/${ref.id}`, label: ref.title, link: { section: ref.section, id: ref.id } };
  }
  if (concept && !PLACEHOLDER.test(concept)) return { key: concept.toLowerCase(), label: cap(concept) };
  // free-text tags ("Physics", "algebra - identities") are readable; kebab slugs and "mixed" are not
  if (sub && sub.toLowerCase() !== 'mixed' && /[\sA-Z]/.test(sub)) return { key: sub.toLowerCase(), label: cap(sub) };
  return null;
}

function topTopics(map: Map<string, MockTopicCount>, limit: number): MockTopicCount[] {
  return [...map.values()].sort((a, b) => b.count - a.count || a.label.localeCompare(b.label)).slice(0, limit);
}

// ---------------------------------------------------------------- sample questions
const GENERIC_SOLUTION = /stem against|verified key is option|only choice satisfying|stated requirement/i;
const strip = (s: string) => s.replace(/\*\*\s*answer\s*:[^*]*\*\*/gi, '').trim();

// stems that lean on context (a para, table, chart, puzzle set) we cannot show next to a single question
const NEEDS_CONTEXT = /\bpara(graph)?\s*\d|\b(passage|author|writer)\b|\b(table|chart|graph|diagram|pie|histogram|caption)\b|\b(above|below|given (data|information|statements?|arrangement|series))\b|\bfollowing (data|information|arrangement|puzzle)\b/i;

function usable(q: Question): boolean {
  if (q.passage || q.group || !q.q || q.q.length < 40 || q.q.length > 700 || NEEDS_CONTEXT.test(q.q)) return false;
  if (q.type === 'numeric') return true;
  return Array.isArray(q.options) && q.options.length >= 2 && q.answer >= 0 && q.answer < q.options.length;
}
function substantive(q: Question): boolean {
  const s = strip(q.solution ?? '');
  return s.length >= 60 && s.length <= 1400 && !GENERIC_SOLUTION.test(q.solution);
}

function pickSamples(mock: Mock): MockSeoSample[] {
  const secs = mock.sections;
  if (!secs.length) return [];
  const good = secs.map((s) => s.questions.map((q, i) => ({ q, i })).filter((x) => usable(x.q) && substantive(x.q)));
  const thin = secs.map((s) => s.questions.map((q, i) => ({ q, i })).filter((x) => usable(x.q) && !substantive(x.q) && x.q.q.length >= 60 && x.q.q.length <= 400));
  // spread the three picks over the sections: first, middle, last
  const want = [0, 1, 2].map((k) => (secs.length === 1 ? 0 : Math.round((k * (secs.length - 1)) / 2)));
  const out: MockSeoSample[] = [];
  const used = new Set<string>();
  const take = (pool: typeof good, showSolution: boolean, preferred: number) => {
    const order = [preferred, ...secs.map((_, i) => i).filter((i) => i !== preferred)];
    for (const si of order) {
      const left = pool[si].filter((x) => !used.has(x.q.id));
      if (!left.length) continue;
      const m = want.filter((w) => w === si).length;
      const nth = out.filter((o) => o.sectionId === secs[si].sectionId).length;
      const pos = Math.min(left.length - 1, Math.floor((left.length * (nth + 1)) / (m + 1)));
      const pick = left[Math.max(0, pos)];
      used.add(pick.q.id);
      out.push({ sectionId: secs[si].sectionId, sectionName: secs[si].name, number: pick.i + 1, q: pick.q, showSolution });
      return true;
    }
    return false;
  };
  for (const w of want) { if (out.length >= 3) break; take(good, true, w); }
  for (const w of want) { if (out.length >= 3) break; take(thin, false, w); }
  return out.slice(0, 3).sort((a, b) => secs.findIndex((s) => s.sectionId === a.sectionId) - secs.findIndex((s) => s.sectionId === b.sectionId) || a.number - b.number);
}

// ---------------------------------------------------------------- main
const MONTHS = /(\d{1,2})(?:st|nd|rd|th)?\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?,?\s+(\d{4})/i;

export function analyseMock(mock: Mock): MockSeoData {
  const examId = mock.exam ?? 'ssc-cgl';
  const info = getExamInfo(examId);
  const all = mock.sections.flatMap((s) => s.questions);
  const total = all.length;
  const maxMarks = total * mock.plus;

  const penal = new Map<number, number>();
  for (const q of all) { const v = wrongAnswerPenalty(q, mock.minus); penal.set(v, (penal.get(v) ?? 0) + 1); }
  const penalties = [...penal.entries()].map(([value, count]) => ({ value, count })).sort((a, b) => b.count - a.count);

  const optLens = new Map<number, number>();
  const spread = new Map<string, number>();
  for (const q of all) {
    if (q.type === 'numeric' || !q.options?.length) continue;
    optLens.set(q.options.length, (optLens.get(q.options.length) ?? 0) + 1);
    const letter = 'ABCDEFGH'[q.answer];
    if (letter) spread.set(letter, (spread.get(letter) ?? 0) + 1);
  }
  const optionCount = optLens.size ? [...optLens.entries()].sort((a, b) => b[1] - a[1])[0][0] : null;

  const diffOf = (qs: Question[]) => {
    const d = { easy: 0, medium: 0, hard: 0 };
    for (const q of qs) if (q.difficulty && q.difficulty in d) d[q.difficulty]++;
    // a single level on every question (e.g. all "medium") carries no information
    return Object.values(d).filter((n) => n > 0).length >= 2 ? d : null;
  };

  const overall = new Map<string, MockTopicCount>();
  let taggedTotal = 0;
  const sections: MockSeoSection[] = mock.sections.map((s) => {
    const tmap = new Map<string, MockTopicCount>();
    let tagged = 0, est = 0, estN = 0;
    for (const q of s.questions) {
      const t = topicOf(q, s.sectionId);
      if (t) {
        tagged++;
        const e = tmap.get(t.key); if (e) e.count++; else tmap.set(t.key, { label: t.label, count: 1, link: t.link });
        const o = overall.get(t.key); if (o) o.count++; else overall.set(t.key, { label: t.label, count: 1, link: t.link });
      }
      if (typeof q.timeSec === 'number' && q.timeSec > 0) { est += q.timeSec; estN++; }
    }
    taggedTotal += tagged;
    const complete = estN === s.questions.length && estN > 0;
    return {
      sectionId: s.sectionId, name: s.name, count: s.questions.length, marks: s.questions.length * mock.plus,
      sharePct: total ? (s.questions.length / total) * 100 : 0,
      avgTimeSec: complete ? est / estN : null, estSec: complete ? est : null,
      topics: topTopics(tmap, 6), distinctTopics: tmap.size, taggedCount: tagged,
      passageQs: s.questions.filter((q) => q.passage || q.group).length,
      figureQs: s.questions.filter((q) => !!q.figure).length,
      numericQs: s.questions.filter((q) => q.type === 'numeric').length,
      difficulty: diffOf(s.questions),
    };
  });

  const estAll = sections.every((s) => s.estSec !== null) ? sections.reduce((n, s) => n + (s.estSec as number), 0) : null;
  const dm = MONTHS.exec(mock.title) ?? MONTHS.exec(mock.blurb);
  const sh = /\b(?:shift|slot)\s*(\d)/i.exec(mock.title);

  return {
    examId, examName: info?.name ?? examId.toUpperCase(),
    total, maxMarks, durationMin: mock.durationMin,
    secPerQuestion: total ? (mock.durationMin * 60) / total : 0,
    penalties, optionCount,
    answerSpread: [...spread.entries()].sort().map(([letter, count]) => ({ letter, count })),
    estMinutes: estAll === null ? null : estAll / 60,
    difficulty: diffOf(all),
    passageQs: all.filter((q) => q.passage || q.group).length,
    figureQs: all.filter((q) => !!q.figure).length,
    numericQs: all.filter((q) => q.type === 'numeric').length,
    shortcutQs: all.filter((q) => !!q.shortcut).length,
    sections, topics: topTopics(overall, 10), distinctTopics: overall.size, taggedTotal,
    dateLabel: dm ? `${Number(dm[1])} ${cap(dm[2].toLowerCase())} ${dm[3]}` : null,
    shiftLabel: sh ? `${/slot/i.test(sh[0]) ? 'Slot' : 'Shift'} ${sh[1]}` : null,
    samples: pickSamples(mock),
  };
}

// ---------------------------------------------------------------- sibling mocks (internal links)
const availability = new Map<string, boolean>();
const isAvailable = (id: string) => {
  let v = availability.get(id);
  if (v === undefined) { v = !!getMock(id); availability.set(id, v); }
  return v;
};

/** Up to `limit` other published papers of the same exam, taken from the paper's neighbours in the list. */
export function siblingMocks(mock: Mock, limit = 4): { id: string; title: string }[] {
  const examId = mock.exam ?? 'ssc-cgl';
  const same = MOCK_DEFS.filter((d) => (d.exam ?? 'ssc-cgl') === examId && !d.reviewHold);
  const at = same.findIndex((d) => d.id === mock.id);
  const out: { id: string; title: string }[] = [];
  for (let step = 1; step < same.length && out.length < limit; step++) {
    const d = same[(at + step + same.length) % same.length];
    if (d.id !== mock.id && isAvailable(d.id)) out.push({ id: d.id, title: d.title });
  }
  return out;
}
