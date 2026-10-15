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

/** RRB JE keys its flat cutoffs as `cat6_JE_Civil_PWay_Bridge_UR`: post category, then community. Split those into
    one scope per post category. Other exams keep their old reading. */
const CAT_PREFIXED = new Set(['rrb-je']);
/** UP Police nests `{ UR: { male, female } }`. Turn that into one Male and one Female scope with a value per category. */
const BY_GENDER = new Set(['up-police']);

function build(data: any, stage: string, stateWise: boolean, catPrefixed = false, byGender = false): CutRef[] {
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
        const cp = catPrefixed ? k.match(/^cat(\d+)_(.+)_(UR|EWS|OBC|SC|ST)$/) : null;
        if (stateWise) add(k, { UR: v });
        else if (m) add(`${spaced(m[1])} (example zone)`, { [m[2]]: v });
        else if (cp) add(`Cat. ${cp[1]} ${cp[2].replace(/_/g, ' ')}`, { [cp[3]]: v });
        else add(gender, { [k]: v });
      } else if (v && typeof v === 'object' && byGender) {
        for (const g of ['male', 'female'] as const) {
          const x = (v as Record<string, unknown>)[g];
          if (isNum(x)) add(g === 'male' ? 'Male' : 'Female', { [k]: x });
        }
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
  for (const st of stages) {
    // "cbt1@75" = the cutoff list "cbt1", keeping only entries whose maxMarks is 75 (a list can mix papers of different totals)
    const [list, only] = st.split('@');
    const refs = build(data, list, (STATE_WISE[id] ?? []).includes(list), CAT_PREFIXED.has(id), BY_GENDER.has(id));
    out[st] = only ? refs.filter((r) => r.maxMarks === Number(only)) : refs;
  }
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

/** Bank posts quote "Basic ₹X (scale ₹X - ₹Y) plus DA, HRA and other allowances" (IBPS). SBI quotes "Starting basic pay ₹X ... in the
    scale 48480-2000/7-...-85920" or "Pay scale ₹24,050-1,340/3-...-64,480 · starting basic pay ₹26,730", so those are read as a fallback. */
export function bankPay(exam: any): { name: string; basic: number; scaleMax: number | null }[] {
  const out: { name: string; basic: number; scaleMax: number | null }[] = [];
  for (const p of exam?.posts ?? []) {
    const s = String(p.payLevel ?? '');
    const b = s.match(/Basic ₹\s*([\d,]+)/) ?? s.match(/starting basic pay\s*₹\s*([\d,]+)/i);
    if (!b) continue;
    const sc = s.match(/scale ₹\s*[\d,]+\s*[–-]\s*₹\s*([\d,]+)/);
    // last figure of a scale written as 48480-2000/7-62480-2340/2-...-85920
    const slab = sc ? null : s.match(/scale\s*₹?\s*([\d,]+(?:-[\d,]+(?:\/\d+)?)+)/i);
    const top = sc ? sc[1] : slab ? slab[1].split('-').pop() : null;
    out.push({ name: String(p.name), basic: Number(b[1].replace(/,/g, '')), scaleMax: top ? Number(top.replace(/,/g, '')) : null });
  }
  return out;
}

/** State government posts quote "Level 3 · ₹21,700–69,100 (pay band ...)". Returns the entry pay and the top of the range. */
export function statePay(exam: any): { name: string; basic: number; scaleMax: number | null }[] {
  const out: { name: string; basic: number; scaleMax: number | null }[] = [];
  for (const p of exam?.posts ?? []) {
    const m = String(p.payLevel ?? '').match(/Level \d+[^₹]*₹\s*([\d,]+)\s*(?:[–-]\s*₹?\s*([\d,]+))?/);
    if (!m) continue;
    out.push({ name: String(p.name), basic: Number(m[1].replace(/,/g, '')), scaleMax: m[2] ? Number(m[2].replace(/,/g, '')) : null });
  }
  return out;
}

export type { CutScope };
