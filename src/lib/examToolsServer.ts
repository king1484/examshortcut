import { getCutoffs } from '@/lib/content';
import { SCORE_CFG, RANK_CFG, type CutRef, type CutScope, type PayOption, type SalaryPost } from '@/lib/examTools';

/* Server-side readers that turn content/exams/<id>/{cutoffs,exam}.json into the small typed props the
   client tools need. Cutoff files differ per exam (numeric, percent strings, state-wise, zone examples),
   so this only keeps numeric values and silently drops the rest. */

/* eslint-disable @typescript-eslint/no-explicit-any */

const spaced = (s: string) => s.replace(/([a-z0-9])([A-Z])/g, '$1 $2');
const isNum = (v: unknown): v is number => typeof v === 'number' && Number.isFinite(v);

/** Examples of a state-wise numeric layout: IBPS Clerk prelims maps state -> one UR number. */
const STATE_WISE: Record<string, string[]> = { 'ibps-clerk': ['prelims'] };

function build(data: any, stage: string, stateWise: boolean): CutRef[] {
  const list = data?.[stage];
  if (!Array.isArray(list)) return [];
  const refs = new Map<string, CutRef>();
  for (const e of list) {
    const max = Number(e?.maxMarks);
    if (!max || !e.cutoffs || typeof e.cutoffs !== 'object') continue;
    const label = String(e.year ?? e.cycle ?? e.list ?? '');
    const text = `${e.list ?? ''} ${e.stage ?? ''}`;
    const gender = /female/i.test(text) ? 'Female' : /\bmale\b/i.test(text) ? 'Male' : 'All India';
    const id = `${label}|${max}`;
    const ref = refs.get(id) ?? { id, label, list: String(e.list ?? e.stage ?? ''), maxMarks: max, scopes: [] };
    const add = (name: string, values: Record<string, number>) => {
      if (!Object.keys(values).length) return;
      const hit = ref.scopes.find((s) => s.name === name);
      if (hit) Object.assign(hit.values, values);
      else ref.scopes.push({ name, values });
    };
    for (const [k, v] of Object.entries(e.cutoffs as Record<string, unknown>)) {
      if (isNum(v)) {
        const m = k.match(/^example(.+?)_([A-Za-z]+)$/);
        if (stateWise) add(k, { UR: v });
        else if (m) add(`${spaced(m[1])} (example zone)`, { [m[2]]: v });
        else add(gender, { [k]: v });
      } else if (v && typeof v === 'object') {
        const inner: Record<string, number> = {};
        for (const [c, x] of Object.entries(v as Record<string, unknown>)) if (isNum(x)) inner[c] = x;
        add(k, inner);
      }
    }
    if (ref.scopes.length) refs.set(id, ref);
  }
  return [...refs.values()];
}

/** Cutoff reference points per stage key, latest first. Empty when the file has no numeric cutoffs for it. */
export function cutRefsFor(id: string): Record<string, CutRef[]> {
  const data = getCutoffs(id);
  const out: Record<string, CutRef[]> = {};
  const stages = new Set<string>();
  for (const s of SCORE_CFG[id]?.stages ?? []) if (s.cutStage) stages.add(s.cutStage);
  const rc = RANK_CFG[id]?.cutStage;
  if (rc && rc !== 'none') stages.add(rc);
  for (const st of stages) out[st] = build(data, st, (STATE_WISE[id] ?? []).includes(st));
  return out;
}

/** Posts with parsed pay levels, from exam.json. Posts whose pay string has no "Level N ... ₹basic" are skipped. */
export function salaryPosts(exam: any): SalaryPost[] {
  const out = new Map<string, SalaryPost>();
  for (const p of exam?.posts ?? []) {
    const options: PayOption[] = [];
    for (const m of String(p.payLevel ?? '').matchAll(/Level (\d+)[^₹]*₹\s*([\d,]+)/g)) {
      options.push({ level: Number(m[1]), basic: Number(m[2].replace(/,/g, '')) });
    }
    if (!options.length) continue;
    const key = `${p.name}|${options.map((o) => o.level).join(',')}`;
    if (!out.has(key)) out.set(key, { key, name: String(p.name), options });
  }
  return [...out.values()];
}

/** Bank posts quote "Basic ₹X (scale ₹X - ₹Y) plus DA, HRA and other allowances". */
export function bankPay(exam: any): { name: string; basic: number; scaleMax: number | null }[] {
  const out: { name: string; basic: number; scaleMax: number | null }[] = [];
  for (const p of exam?.posts ?? []) {
    const s = String(p.payLevel ?? '');
    const b = s.match(/Basic ₹\s*([\d,]+)/);
    if (!b) continue;
    const sc = s.match(/scale ₹\s*[\d,]+\s*[–-]\s*₹\s*([\d,]+)/);
    out.push({ name: String(p.name), basic: Number(b[1].replace(/,/g, '')), scaleMax: sc ? Number(sc[1].replace(/,/g, '')) : null });
  }
  return out;
}

export type { CutScope };
