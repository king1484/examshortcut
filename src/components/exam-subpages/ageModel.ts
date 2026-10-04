// Client-safe (no node imports): turns an exam's eligibility JSON into the numbers the
// age calculator needs. Everything is read from the data; a row that does not parse
// cleanly is dropped (and shown in the "not calculated" list) instead of being guessed.

export interface AgeBand { label: string; min: number; max: number; range: string }
export interface AgeCategory { id: string; label: string; years: number }
export interface ManualRelaxation { category: string; years: string }
export interface AgeModel {
  /** ISO date taken from eligibility.ageCutoffDate, or '' when the data has no clean date */
  cutoff: string;
  bands: AgeBand[];
  categories: AgeCategory[];
  manual: ManualRelaxation[];
}

/* eslint-disable @typescript-eslint/no-explicit-any */
export function buildAgeModel(exam: any): AgeModel | null {
  const el = exam?.eligibility;
  if (!el) return null;

  const bands: AgeBand[] = [];
  for (const a of el.age ?? []) {
    const m = String(a.range ?? '').match(/(\d{1,2})\s*[–-]\s*(\d{1,2})\s*years/);
    if (!m) continue;
    const min = Number(m[1]), max = Number(m[2]);
    if (min >= max) continue;
    bands.push({ label: String(a.posts), min, max, range: String(a.range) });
  }
  if (!bands.length) return null;

  const categories: AgeCategory[] = [{ id: 'ur', label: 'General / UR / EWS (no relaxation)', years: 0 }];
  const manual: ManualRelaxation[] = [];
  const seen = new Set<string>(['ur']);
  const add = (label: string, years: number) => {
    const id = label.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    if (seen.has(id)) return;
    seen.add(id);
    categories.push({ id, label, years });
  };

  for (const r of el.ageRelaxation ?? []) {
    const cat = String(r.category ?? '');
    const yrs = String(r.years ?? '');
    // Ex-servicemen relaxation depends on the service actually rendered, so it is never auto-calculated.
    if (/ex-?\s?servicem[ae]n|\bESM\b/i.test(cat)) { manual.push({ category: cat, years: yrs }); continue; }
    const single = yrs.match(/^\+(\d{1,2})\s*years?$/);
    if (single) { add(cat, Number(single[1])); continue; }
    // "PwD (UR / OBC / SC-ST)" + "+10 / +13 / +15 years" — one number per listed sub-category
    const paren = cat.match(/^(.*?)\s*\(([^)]+)\)\s*$/);
    const nums = yrs.match(/\d{1,2}/g);
    if (paren && nums && /^[+\d\s/,]+years?$/.test(yrs)) {
      const parts = paren[2].includes(',') ? paren[2].split(/\s*,\s*/) : paren[2].split(/\s*\/\s*/);
      if (parts.length === nums.length && parts.length > 1) {
        parts.forEach((p, i) => add(`${paren[1]} (${p.trim()})`, Number(nums[i])));
        continue;
      }
    }
    manual.push({ category: cat, years: yrs });
  }

  const cutoff = /^\d{4}-\d{2}-\d{2}$/.test(String(el.ageCutoffDate ?? '')) ? String(el.ageCutoffDate) : '';
  return { cutoff, bands, categories, manual };
}

// ---- date maths (UTC, ISO strings compare correctly as text) ----
const iso = (d: Date) => d.toISOString().slice(0, 10);

/** cutoff minus N years, same month/day (Feb 29 falls to 1 March in non-leap years) */
export function minusYears(cutoffIso: string, years: number): string {
  const [y, m, d] = cutoffIso.split('-').map(Number);
  return iso(new Date(Date.UTC(y - years, m - 1, d)));
}
export function plusDays(isoDate: string, days: number): string {
  const [y, m, d] = isoDate.split('-').map(Number);
  return iso(new Date(Date.UTC(y, m - 1, d + days)));
}

/**
 * Eligible date-of-birth window for a band: born on or after (cutoff − (max + relaxation) years + 1 day)
 * and on or before (cutoff − min years). This matches the "born between …" ranges printed in the data
 * (e.g. 18–27 as on 1 Aug 2026 → born 2 Aug 1999 to 1 Aug 2008).
 */
export function dobWindow(cutoffIso: string, band: { min: number; max: number }, relaxation: number) {
  return {
    earliest: plusDays(minusYears(cutoffIso, band.max + relaxation), 1),
    latest: minusYears(cutoffIso, band.min),
  };
}

/** Completed years / months / days between dob and the cutoff date. */
export function ageOn(dobIso: string, onIso: string) {
  const [by, bm, bd] = dobIso.split('-').map(Number);
  const [oy, om, od] = onIso.split('-').map(Number);
  let y = oy - by, m = om - bm, d = od - bd;
  if (d < 0) { m--; d += new Date(Date.UTC(oy, om - 1, 0)).getUTCDate(); }
  if (m < 0) { y--; m += 12; }
  return { y, m, d };
}

export function fmtDate(isoDate: string): string {
  const [y, m, d] = isoDate.split('-').map(Number);
  return new Date(Date.UTC(y, m - 1, d)).toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
}
