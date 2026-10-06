import fs from 'node:fs';
import path from 'node:path';
import { getCutoffs, getExam, type SectionId } from './content';
import { EXAMS } from './exams';

/* Data for the generic per-exam info pages: syllabus, admit card / answer key / result,
   exam calendar and expected cut-off. Files live in content/exams/<id>/ next to exam.json.
   Server-only (reads the file system). */

/* eslint-disable @typescript-eslint/no-explicit-any */
const EXAMS_DIR = path.join(process.cwd(), 'content', 'exams');

function read<T>(id: string, file: string): T | null {
  const p = path.join(EXAMS_DIR, id, file);
  if (!fs.existsSync(p)) return null;
  return JSON.parse(fs.readFileSync(p, 'utf-8')) as T;
}

export type PageKind = 'syllabus' | 'admit-card' | 'calendar' | 'expected-cutoff';

export interface SyllabusSection {
  name: string;
  sectionId?: SectionId;
  stage: string;
  topics: string[];
  tip?: string;
}
export interface SyllabusData {
  lastVerified: string;
  source: string;
  intro: string;
  note?: string;
  sections: SyllabusSection[];
}

export interface ProcessData {
  lastVerified: string;
  portal: string;
  sources: string[];
  admitCard: { where: string; when: string; steps: string[]; carry: string[]; note?: string };
  answerKey: { released: boolean; summary: string; steps: string[]; fee: string; note?: string };
  result: { summary: string; stages: { stage: string; what: string }[]; scorecard: string };
}

export interface CalEvent {
  id: string; title: string; start: string; end?: string;
  status: 'done' | 'confirmed' | 'expected'; note?: string;
}
export interface CalendarData { cycle: number; note?: string; events: CalEvent[] }

export interface SeriesSpec {
  id: string; label: string; section: string; category: string;
  agg: 'value' | 'median'; listIncludes?: string;
}
export interface ExpectedSpec {
  lastVerified: string;
  intro: string;
  series: SeriesSpec[];
  factors: string[];
  caveat: string;
  target: string;
  scaleTo?: number;
}

export const getSyllabus = (id: string) => read<SyllabusData>(id, 'syllabus.json');
export const getProcess = (id: string) => read<ProcessData>(id, 'process.json');
export const getExpectedSpec = (id: string) => read<ExpectedSpec>(id, 'expected-cutoff.json');
export function getCalendar(id: string): CalendarData | null {
  const cal = getExam(id)?.calendar;
  return cal && Array.isArray(cal.events) && cal.events.length ? (cal as CalendarData) : null;
}

/** ssc-cgl has its own hand-built pages for all of these. CAT keeps its own syllabus page. */
const SKIP: Record<PageKind, string[]> = {
  syllabus: ['ssc-cgl', 'cat'],
  'admit-card': ['ssc-cgl'],
  calendar: ['ssc-cgl'],
  'expected-cutoff': ['ssc-cgl'],
};

export function hasPage(id: string, kind: PageKind): boolean {
  if (SKIP[kind].includes(id) || !EXAMS.some((e) => e.id === id)) return false;
  if (kind === 'syllabus') return !!getSyllabus(id);
  if (kind === 'admit-card') return !!getProcess(id);
  if (kind === 'calendar') return !!getCalendar(id);
  return !!getExpectedSpec(id) && !!getCutoffs(id) && computeSeries(id).length > 0;
}

export function idsWithPage(kind: PageKind): { exam: string }[] {
  return EXAMS.filter((e) => hasPage(e.id, kind)).map((e) => ({ exam: e.id }));
}

// ---------------------------------------------------------------- expected cut-off
export interface SeriesPoint { year: number; value: number }
export interface SeriesResult {
  id: string; label: string; maxMarks: number | null;
  points: SeriesPoint[];
  last: SeriesPoint;
  swing: number;
  low: number; high: number;
  scaled?: { to: number; low: number; high: number; last: number };
}

const r2 = (n: number) => Math.round(n * 100) / 100;
const median = (a: number[]) => {
  const s = [...a].sort((x, y) => x - y);
  const m = Math.floor(s.length / 2);
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
};

export function computeSeries(id: string): SeriesResult[] {
  const spec = getExpectedSpec(id);
  const data = getCutoffs(id);
  if (!spec || !data) return [];
  const out: SeriesResult[] = [];
  for (const s of spec.series) {
    const rows: any[] = Array.isArray(data[s.section]) ? data[s.section] : [];
    const byYear = new Map<number, number>();
    let maxMarks: number | null = null;
    for (const r of rows) {
      if (typeof r.year !== 'number' || byYear.has(r.year)) continue;
      if (s.listIncludes && !String(r.list ?? '').includes(s.listIncludes)) continue;
      const c = r.cutoffs ?? {};
      let v: number | undefined;
      if (s.agg === 'median') {
        const nums = Object.values(c).filter((x): x is number => typeof x === 'number');
        if (nums.length >= 5) v = median(nums);
      } else if (typeof c[s.category] === 'number') v = c[s.category];
      if (v === undefined) continue;
      byYear.set(r.year, v);
      maxMarks = typeof r.maxMarks === 'number' ? r.maxMarks : maxMarks;
    }
    const points = [...byYear.entries()].sort((a, b) => a[0] - b[0]).map(([year, value]) => ({ year, value: r2(value) }));
    if (points.length < 2) continue;
    const diffs = points.slice(1).map((p, i) => Math.abs(p.value - points[i].value));
    const swing = r2(diffs.reduce((a, b) => a + b, 0) / diffs.length);
    const last = points[points.length - 1];
    const res: SeriesResult = { id: s.id, label: s.label, maxMarks, points, last, swing, low: r2(last.value - swing), high: r2(last.value + swing) };
    if (spec.scaleTo && maxMarks) {
      const f = spec.scaleTo / maxMarks;
      res.scaled = { to: spec.scaleTo, low: r2(res.low * f), high: r2(res.high * f), last: r2(last.value * f) };
    }
    out.push(res);
  }
  return out;
}

/** Pages that exist for an exam, in the order they are shown on the hub. */
export function pagesFor(id: string): PageKind[] {
  return (['syllabus', 'admit-card', 'calendar', 'expected-cutoff'] as PageKind[]).filter((k) => hasPage(id, k));
}
