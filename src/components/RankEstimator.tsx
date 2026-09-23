'use client';
import { useMemo, useState } from 'react';

/* eslint-disable @typescript-eslint/no-explicit-any */

const CATS = ['UR', 'EWS', 'OBC', 'SC', 'ST'] as const;

/**
 * Marks → percentile curve, anchored on the official UR cutoff of the chosen year.
 * The cutoff sits near the 90th percentile of everyone who appeared (the Tier 1
 * shortlist is roughly the top fifth, and UR is the highest list). Anchors around
 * it shape a realistic bell; everything is piecewise-linear so the number is
 * reproducible rather than a black box.
 */
const ANCHORS: [number, number][] = [
  [-100, 0.3],
  [-65, 5],
  [-45, 25],
  [-30, 50],
  [-15, 75],
  [0, 90],
  [20, 97],
  [45, 99.5],
  [70, 99.9],
];

function percentileAt(marks: number, urCutoff: number) {
  const d = marks - urCutoff;
  if (d <= ANCHORS[0][0]) return ANCHORS[0][1];
  for (let i = 1; i < ANCHORS.length; i++) {
    const [d1, p1] = ANCHORS[i];
    if (d <= d1) {
      const [d0, p0] = ANCHORS[i - 1];
      return p0 + ((d - d0) / (d1 - d0)) * (p1 - p0);
    }
  }
  return ANCHORS[ANCHORS.length - 1][1];
}

const fmt = (n: number) => n.toLocaleString('en-IN', { maximumFractionDigits: 0 });

export function RankEstimator({ cutoffs }: { cutoffs: any }) {
  const years = useMemo(() => {
    const lists = (cutoffs?.tier1 ?? []) as any[];
    return lists
      .filter((l) => l.cutoffs && /all posts/i.test(l.list ?? ''))
      .sort((a, b) => b.year - a.year);
  }, [cutoffs]);

  const [year, setYear] = useState<number | null>(null);
  const [marks, setMarks] = useState(140);
  const [cat, setCat] = useState<string>('UR');
  const [appeared, setAppeared] = useState(1200000);

  const activeYear = year ?? years[0]?.year ?? null;
  const entry = years.find((y) => y.year === activeYear) ?? null;
  const urCutoff: number | null = entry?.cutoffs?.UR ?? null;
  const catCutoff: number | null = entry?.cutoffs?.[cat] ?? null;

  const pct = urCutoff !== null ? percentileAt(marks, urCutoff) : null;
  const rank = pct !== null ? Math.max(1, Math.round(appeared * (1 - pct / 100))) : null;
  const gap = catCutoff !== null ? marks - catCutoff : null;

  const verdict =
    gap === null ? null :
    gap >= 20 ? { t: `Comfortably above the ${activeYear} ${cat} cutoff — a Tier 2 shortlist score in this band`, c: 'var(--ok)' } :
    gap >= 0 ? { t: `Above the ${activeYear} ${cat} cutoff — shortlist likely, keep the buffer on exam day`, c: 'var(--ok)' } :
    gap >= -15 ? { t: `Borderline — ${fmt(Math.abs(gap))} marks short; that is 3-6 more correct answers`, c: 'var(--warn)' } :
    { t: `Below the ${activeYear} ${cat} cutoff — target the weak sections before the exam`, c: 'var(--bad)' };

  const rows = useMemo(() => {
    if (urCutoff === null) return [];
    return [-20, -10, -5, 0, 5, 10, 20].map((d) => {
      const m = marks + d;
      const p = percentileAt(m, urCutoff);
      return { d, m, p, r: Math.max(1, Math.round(appeared * (1 - p / 100))) };
    }).filter((x) => x.m >= 0 && x.m <= 200);
  }, [marks, urCutoff, appeared]);

  const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };

  if (!entry) return <p className="muted mt-6">Cutoff data not found.</p>;

  return (
    <div className="mt-6">
      <div className="card p-5">
        <div className="flex items-center gap-2 flex-wrap">
          <span className="text-sm font-bold">Cutoff year:</span>
          {years.map((y) => (
            <button key={y.year} className="chip" style={activeYear === y.year ? { background: 'var(--ink)', color: 'var(--bg)' } : {}} onClick={() => setYear(y.year)}>
              {y.year}
            </button>
          ))}
        </div>
        <div className="flex items-center gap-2 flex-wrap mt-3">
          <span className="text-sm font-bold">Your category:</span>
          {CATS.map((c) => (
            <button key={c} className="chip" style={cat === c ? { background: 'var(--ink)', color: 'var(--bg)' } : {}} onClick={() => setCat(c)}>{c}</button>
          ))}
        </div>

        <div className="grid sm:grid-cols-2 gap-4 mt-4">
          <label className="text-xs font-semibold faint uppercase">
            Expected Tier 1 marks (out of 200)
            <input type="number" min={0} max={200} value={marks} onChange={(e) => setMarks(Math.max(0, Math.min(200, Number(e.target.value) || 0)))}
              className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
            <input type="range" min={0} max={200} value={marks} onChange={(e) => setMarks(Number(e.target.value))} className="w-full mt-2" aria-label="marks slider" />
          </label>
          <label className="text-xs font-semibold faint uppercase">
            Candidates appeared (approx)
            <select value={appeared} onChange={(e) => setAppeared(Number(e.target.value))} className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input}>
              <option value={1000000}>~10 lakh</option>
              <option value={1200000}>~12 lakh (recent typical)</option>
              <option value={1500000}>~15 lakh</option>
              <option value={2000000}>~20 lakh</option>
            </select>
            <span className="block text-[11px] font-normal normal-case mt-1 faint">Tier 1 has appeared 12-13 lakh candidates in recent cycles. The rank scales with this number; the percentile does not.</span>
          </label>
        </div>
      </div>

      {pct !== null && rank !== null && (
        <div className="card p-5 mt-5">
          <div className="grid grid-cols-3 gap-3 text-center">
            <div><div className="text-3xl font-extrabold">{pct.toFixed(1)}</div><div className="text-xs faint font-semibold uppercase">Percentile (est.)</div></div>
            <div><div className="text-3xl font-extrabold">{fmt(rank)}</div><div className="text-xs faint font-semibold uppercase">All-India rank (est.)</div></div>
            <div>
              <div className="text-3xl font-extrabold" style={{ color: gap !== null && gap >= 0 ? 'var(--ok)' : 'var(--bad)' }}>
                {gap !== null ? (gap >= 0 ? '+' : '') + gap.toFixed(2).replace(/\.00$/, '') : '—'}
              </div>
              <div className="text-xs faint font-semibold uppercase">vs {activeYear} {cat} cutoff ({catCutoff})</div>
            </div>
          </div>
          {verdict && <p className="text-sm font-semibold mt-3" style={{ color: verdict.c }}>{verdict.t}</p>}

          <div className="tbl-wrap mt-4">
            <table className="tbl">
              <thead>
                <tr><th>Marks</th><th className="text-right">Percentile</th><th className="text-right">Est. rank</th></tr>
              </thead>
              <tbody>
                {rows.map((r) => (
                  <tr key={r.d} style={r.d === 0 ? { fontWeight: 700, background: 'var(--surface-2)' } : {}}>
                    <td>{r.m}{r.d === 0 ? ' (your input)' : ` (${r.d > 0 ? '+' : ''}${r.d})`}</td>
                    <td className="text-right">{r.p.toFixed(1)}</td>
                    <td className="text-right">{fmt(r.r)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="text-[11px] faint mt-3">
            How this works: the curve is anchored on the official {activeYear} UR cutoff ({urCutoff} — roughly the 90th percentile of all candidates who appeared) and shaped like recent years' score distributions. SSC never publishes all-India ranks for CGL, so this is a planning estimate, not a prediction — your normalised score after shift normalisation decides the real outcome. Use the {activeYear} cutoff comparison in the score calculator for the go/no-go call.
          </p>
        </div>
      )}
    </div>
  );
}
