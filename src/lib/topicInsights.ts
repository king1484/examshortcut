/* Server-side helpers that turn a topic's own data (lessons, patterns, practice and solved
   questions) into the facts the practice / formulas / examples helper pages write about.
   Pure functions, no node imports: every sentence on those pages is derived from content, so it
   differs from topic to topic. */
import type { Mistake, Question, QuestionPattern, Subtopic, Topic, WorkedExample } from './types';
import patternNames from '../data/pattern-names.json';

const NAMES = patternNames as Record<string, string>;
export const LETTERS = ['A', 'B', 'C', 'D', 'E'];
export const FREQ_ORDER: Record<string, number> = { 'very common': 0, common: 1, occasional: 2 };
export const FREQ_CHIP: Record<string, string> = { 'very common': 'chip-high', common: 'chip-medium', occasional: 'chip-low' };

const hash = (s: string) => { let h = 2166136261; for (const c of s) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619); } return h >>> 0; };

/** Fill in `passage` for grouped RC / cloze questions that only carry it on the first member. */
export function withPassages(qs: Question[]): Question[] {
  const byGroup: Record<string, string> = {};
  for (const q of qs) if (q.group && q.passage) byGroup[q.group] = q.passage;
  return qs.map((q) => (q.group && !q.passage && byGroup[q.group] ? { ...q, passage: byGroup[q.group] } : q));
}

/** Readable name of a PYQ pattern tag; raw ids that have no name are hidden. */
export function patternLabel(raw?: string | null): string | null {
  if (!raw) return null;
  if (NAMES[raw]) return NAMES[raw];
  if (/^[a-z0-9]+(-[a-z0-9]+)+$/.test(raw) && /\d/.test(raw)) return null;
  return raw;
}

export function difficultyMix(qs: Question[]) {
  const d = { easy: 0, medium: 0, hard: 0 };
  for (const q of qs) if (q.difficulty && q.difficulty in d) d[q.difficulty]++;
  return d;
}

/** Same budget rule the timed test uses: each question's `timeSec`, 45 s when untagged. */
export const budgetSeconds = (qs: Question[]) => qs.reduce((n, q) => n + (typeof q.timeSec === 'number' ? q.timeSec : 45), 0);

export function timeRange(qs: Question[]): { min: number; max: number } | null {
  const t = qs.map((q) => q.timeSec).filter((x): x is number => typeof x === 'number');
  return t.length ? { min: Math.min(...t), max: Math.max(...t) } : null;
}

export const plural = (n: number, one: string, many = `${one}s`) => `${n} ${n === 1 ? one : many}`;

export function joinList(items: string[]): string {
  if (items.length <= 1) return items.join('');
  return `${items.slice(0, -1).join(', ')} and ${items[items.length - 1]}`;
}

/** Practice questions per subtopic, biggest first (subtopics with no questions are dropped). */
export function subtopicCounts(t: Topic, qs: Question[] = t.practice ?? []) {
  return t.subtopics
    .map((s, order) => ({ sub: s, order, n: qs.filter((q) => q.subtopic === s.id).length }))
    .filter((x) => x.n > 0)
    .sort((a, b) => b.n - a.n || a.order - b.order);
}

export interface PatternRef { pattern: QuestionPattern; sub: Subtopic }
export function patternIndex(t: Topic): Map<string, PatternRef> {
  const m = new Map<string, PatternRef>();
  for (const s of t.subtopics) for (const p of s.patterns ?? []) m.set(p.id, { pattern: p, sub: s });
  return m;
}

export interface QuestionType { key: string; label: string; n: number; sample: Question; ref?: PatternRef; sub?: Subtopic }

/** The question types the practice set is made of, most-represented first. */
export function questionTypes(t: Topic): QuestionType[] {
  const idx = patternIndex(t);
  const subs = new Map(t.subtopics.map((s) => [s.id, s]));
  const groups = new Map<string, QuestionType>();
  for (const q of t.practice ?? []) {
    const label = patternLabel(q.pattern);
    if (!label || !q.pattern) continue;
    const g = groups.get(q.pattern);
    if (g) g.n++;
    else groups.set(q.pattern, { key: q.pattern, label, n: 1, sample: q, ref: idx.get(q.pattern), sub: (q.subtopic ? subs.get(q.subtopic) : undefined) ?? idx.get(q.pattern)?.sub });
  }
  return [...groups.values()].sort((a, b) => b.n - a.n);
}

export interface Trap { sub: Subtopic; wrong: string; right?: string }

/** Mistakes from the lessons, taken round-robin across subtopics so one subtopic cannot crowd the list. */
export function trapList(subs: Subtopic[], max: number): Trap[] {
  const lists = subs.map((s) => (s.mistakes ?? []).map((m: string | Mistake): Trap => (typeof m === 'string' ? { sub: s, wrong: m } : { sub: s, wrong: m.wrong, right: m.right })));
  const out: Trap[] = [];
  for (let i = 0; out.length < max; i++) {
    let any = false;
    for (const l of lists) {
      if (i < l.length) { out.push(l[i]); any = true; if (out.length >= max) break; }
    }
    if (!any) break;
  }
  return out;
}

/** First readable line of a markdown snippet (for one-line statements in indexes). */
export function leadLine(text: string | null | undefined): string | null {
  if (!text || text.trimStart().startsWith('<svg')) return null;
  for (const raw of text.split('\n')) {
    const line = raw.trim();
    if (!line || line.startsWith('|') || line.startsWith('#') || line.startsWith('<') || line.startsWith('>') || line === '$$') continue;
    return line;
  }
  return null;
}

/** First prose paragraph of a lesson concept (skips tables, lists and headings). */
export function firstParagraph(text: string | null | undefined): string | null {
  for (const para of (text ?? '').split(/\n\s*\n/)) {
    const p = para.trim();
    if (!p || /^(\||#|-|\*|>|\d+\.|<|\$\$)/.test(p)) continue;
    return p.replace(/\n+/g, ' ');
  }
  return null;
}

export function exampleLines(ex: WorkedExample): string[] {
  if (ex.steps?.length) return ex.steps;
  return (ex.solution ?? '').split('\n').map((l) => l.trim()).filter(Boolean);
}

/* ---------- sample question selection ---------- */

const hasSvgOpt = (q: Question) => q.options.some((o) => o.trimStart().startsWith('<svg'));
function usable(q: Question, relaxed: boolean) {
  if (q.type === 'numeric' || q.options.length < 2) return false;
  if (q.solution.length > 1300 || q.q.length > 480) return false;
  if (!relaxed) return !q.figure && !q.passage && !q.group && !hasSvgOpt(q) && q.solution.length <= 1100;
  return (q.passage ?? '').length <= 1300;
}

/** A spread of `n` questions (easy, medium, hard, ...) from different subtopics, rotated per topic. */
export function pickSamples(topicId: string, qs: Question[], n: number): Question[] {
  const pool = withPassages(qs);
  let cand = pool.filter((q) => usable(q, false));
  if (cand.length < n) cand = cand.concat(pool.filter((q) => !cand.includes(q) && usable(q, true)));
  const out: Question[] = [];
  const subs = new Set<string>();
  const want = ['easy', 'medium', 'hard', 'medium', 'easy', 'hard'].slice(0, n);
  const h = hash(topicId);
  want.forEach((d, i) => {
    const bucket = cand.filter((q) => q.difficulty === d && !out.includes(q));
    const fresh = bucket.filter((q) => !q.subtopic || !subs.has(q.subtopic));
    const from = fresh.length ? fresh : bucket;
    if (!from.length) return;
    const q = from[(h + i * 7) % from.length];
    out.push(q);
    if (q.subtopic) subs.add(q.subtopic);
  });
  for (const q of cand) { if (out.length >= n) break; if (!out.includes(q)) out.push(q); }
  const rank: Record<string, number> = { easy: 0, medium: 1, hard: 2 };
  return out.sort((a, b) => (rank[a.difficulty ?? 'medium'] ?? 1) - (rank[b.difficulty ?? 'medium'] ?? 1));
}

/** Patterns of a subtopic that carry a worked example, most-asked first. */
export function patternsWithExample(s: Subtopic, needFormula = false): QuestionPattern[] {
  return (s.patterns ?? [])
    .filter((p) => p.example && (p.example.steps?.length || p.example.solution) && (!needFormula || p.formula))
    .sort((a, b) => (FREQ_ORDER[a.frequency ?? ''] ?? 3) - (FREQ_ORDER[b.frequency ?? ''] ?? 3));
}
