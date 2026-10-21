import fs from 'node:fs';
import path from 'node:path';
import type { SectionId } from './sections';

/* Shift-wise exam analysis: one JSON file per exam day under
   content/shift-analysis/<examSlug>/<YYYY-MM-DD>.json, plus an exams.json registry.
   URLs: /exam-analysis/<examSlug>/<d-month>/ (whole day) and /<d-month>-shift-<n>/ (one shift). */
const ROOT = path.join(process.cwd(), 'content', 'shift-analysis');

export interface ShiftExam {
  slug: string;            // e.g. "ssc-cgl-2026"
  name: string;            // "SSC CGL 2026 Tier 1"
  short: string;           // "SSC CGL"
  window: { start: string; end: string };
  guide?: string;          // internal link to the exam guide
  pattern?: { label: string; value: string }[];
  about?: string;
}

export interface TopicCount { topic: string; count?: string; link?: string }
export interface ShiftSection {
  id: SectionId; name: string; questions: number; marks: number;
  difficulty: string; goodAttempts?: string; topics?: TopicCount[]; notes?: string;
}
export interface AskedQuestion { section: SectionId; q: string; a?: string }
export interface Source { name: string; url: string }
export interface Shift {
  shift: number;
  time: string;                       // "9:00 AM – 10:00 AM IST"
  status: 'reported' | 'partial' | 'pending' | 'not-held';
  alsoCalled?: string;                 // how some sites label this slot, e.g. "Shift 1"
  note?: string;                       // shown instead of analysis when not held
  overall?: string;                    // "Easy to Moderate"
  goodAttempts?: string;               // "80–85"
  summary?: string;
  sections?: ShiftSection[];
  asked?: AskedQuestion[];
  observations?: string[];
  disagreements?: string[];
  sources?: Source[];
  qualityNotes?: string[];
  auto?: boolean;
}
export interface ShiftDay {
  exam: string; date: string; updatedAt: string;
  intro?: string; shifts: Shift[]; faqs?: { q: string; a: string }[];
  correctionNote?: string;
}

function read<T>(rel: string): T | null {
  const f = path.join(ROOT, rel);
  return fs.existsSync(f) ? (JSON.parse(fs.readFileSync(f, 'utf-8')) as T) : null;
}

export function listShiftExams(): ShiftExam[] {
  return read<ShiftExam[]>('exams.json') ?? [];
}
export function getShiftExam(slug: string): ShiftExam | null {
  return listShiftExams().find((e) => e.slug === slug) ?? null;
}
/** Days for one exam, newest first. */
export function listShiftDays(slug: string): ShiftDay[] {
  const dir = path.join(ROOT, slug);
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f))
    .map((f) => read<ShiftDay>(`${slug}/${f}`)!).filter(Boolean)
    .sort((a, b) => b.date.localeCompare(a.date));
}

const MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'];
const cap = (s: string) => s[0].toUpperCase() + s.slice(1);

/** "2026-09-30" → "30-september" */
export function daySlug(date: string) {
  const [, m, d] = date.split('-').map(Number);
  return `${d}-${MONTHS[m - 1]}`;
}
export const shiftSlug = (date: string, n: number) => `${daySlug(date)}-shift-${n}`;
/** "2026-09-30" → "30 September 2026" */
export function dayLabel(date: string, withYear = true) {
  const [y, m, d] = date.split('-').map(Number);
  return `${d} ${cap(MONTHS[m - 1])}${withYear ? ` ${y}` : ''}`;
}

/** Resolve a URL slug to a day (and optionally one shift). */
export function resolveSlug(examSlug: string, slug: string): { day: ShiftDay; shift: Shift | null } | null {
  const m = /^(.*?)(?:-shift-(\d+))?$/.exec(slug);
  if (!m) return null;
  const day = listShiftDays(examSlug).find((d) => daySlug(d.date) === m[1]);
  if (!day) return null;
  if (!m[2]) return { day, shift: null };
  const shift = day.shifts.find((s) => s.shift === Number(m[2]));
  return shift ? { day, shift } : null;
}

export function allShiftParams() {
  return listShiftExams().flatMap((e) => listShiftDays(e.slug).flatMap((d) => [
    { exam: e.slug, slug: daySlug(d.date) },
    ...d.shifts.map((s) => ({ exam: e.slug, slug: shiftSlug(d.date, s.shift) })),
  ]));
}

/** Chip text for a shift: its difficulty, or why there is none. */
export function shiftLabel(s: Shift) {
  if (s.status === 'pending') return 'Awaiting sources';
  if (s.status === 'not-held') return 'Not held';
  return s.overall;
}
export const hasAnalysis = (s: Shift) => s.status !== 'pending' && s.status !== 'not-held';

export function difficultyColor(label = '') {
  const l = label.toLowerCase();
  if (/difficult|tough|hard/.test(l) && !/moderate/.test(l)) return 'var(--bad)';
  if (/moderate to (difficult|tough)/.test(l)) return 'var(--bad)';
  if (/easy to moderate/.test(l)) return 'var(--info)';
  if (/moderate/.test(l)) return 'var(--warn)';
  if (/easy/.test(l)) return 'var(--ok)';
  return 'var(--ink-2)';
}
