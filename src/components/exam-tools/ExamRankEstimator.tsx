'use client';
import Link from 'next/link';
import { useMemo, useState } from 'react';
import { RANK_CFG, normCdf, normInv, type CutRef } from '@/lib/examTools';

/* Scenario estimator, not a prediction. The user fixes three things: how many appeared, how many were
   shortlisted (the anchor rank) and what score that last shortlisted candidate had. Scores are then assumed
   to follow a bell curve in percent-of-max terms, with the spread set by a slider. The default spread (about
   11.5% of max marks) is borrowed from the shape of the CGL curve already on this site, so it is an
   assumption and it is shown as one. */

const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };
const fmt = (n: number) => Math.round(n).toLocaleString('en-IN');
const r1 = (n: number) => Math.round(n * 10) / 10;

interface Point { key: string; label: string; marks: number }

export function ExamRankEstimator({ id, cuts }: { id: string; cuts: CutRef[] }) {
  const cfg = RANK_CFG[id];
  const max = cfg.maxMarks;

  // reference points: the UR (or first listed) cut-off of every year and list on file, scaled to this paper
  const points: Point[] = useMemo(() => {
    const out: Point[] = [];
    for (const r of cuts) {
      for (const s of r.scopes) {
        const k = s.values.UR !== undefined ? 'UR' : Object.keys(s.values)[0];
        if (!k) continue;
        const scaled = (s.values[k] / r.maxMarks) * max;
        const same = Math.abs(r.maxMarks - max) < 0.01;
        out.push({
          key: `${r.id}|${s.name}`,
          label: `${r.label} · ${s.name} · ${k} ${s.values[k]}${same ? '' : ` of ${r.maxMarks}`}`,
          marks: Math.round(scaled * 100) / 100,
        });
      }
    }
    return out;
  }, [cuts, max]);

  const defaultAppeared = cfg.appearedFixed ?? Math.round((cfg.applicants * cfg.appearedPct) / 100);
  const defaultShortlist = cfg.shortlistFixed ?? Math.round(cfg.vacancies * cfg.ratio);

  const [appeared, setAppeared] = useState(defaultAppeared);
  const [shortlist, setShortlist] = useState(defaultShortlist);
  const [pointKey, setPointKey] = useState(points[0]?.key ?? 'custom');
  const [anchor, setAnchor] = useState<number | ''>(points[0]?.marks ?? '');
  const [marks, setMarks] = useState<number | ''>('');
  const [spread, setSpread] = useState(11.5);

  const pickPoint = (k: string) => {
    setPointKey(k);
    const p = points.find((x) => x.key === k);
    if (p) setAnchor(p.marks);
  };

  const calc = useMemo(() => {
    if (anchor === '' || marks === '' || appeared <= 0 || shortlist <= 0 || shortlist >= appeared) return null;
    const c = (anchor / max) * 100;
    const m = (marks / max) * 100;
    const pc = 1 - shortlist / appeared;
    const run = (sd: number, mk: number) => {
      const mu = c - normInv(pc) * sd;
      const p = normCdf((mk - mu) / sd);
      return { p, rank: Math.max(1, Math.round(appeared * (1 - p))) };
    };
    const mid = run(spread, m);
    const a = run(Math.max(4, spread - 3), m).rank;
    const b = run(spread + 3, m).rank;
    const rows = [-10, -5, -2, 0, 2, 5, 10].map((d) => ({ d, m: marks + d })).filter((x) => x.m >= 0 && x.m <= max)
      .map((x) => ({ ...x, ...run(spread, (x.m / max) * 100) }));
    return { pct: mid.p * 100, rank: mid.rank, lo: Math.min(a, b, mid.rank), hi: Math.max(a, b, mid.rank), rows };
  }, [anchor, marks, appeared, shortlist, spread, max]);

  const gap = anchor !== '' && marks !== '' ? marks - anchor : null;
  const bad = shortlist >= appeared;

  return (
    <div className="mt-6">
      <div className="card p-5">
        <div className="grid sm:grid-cols-2 gap-4">
          <label className="text-xs font-semibold faint uppercase">
            Your expected {cfg.stageLabel} marks (out of {max})
            <input type="number" inputMode="decimal" min={0} max={max} value={marks} placeholder="e.g. enter your score"
              onChange={(e) => setMarks(e.target.value === '' ? '' : Math.max(0, Math.min(max, Number(e.target.value))))}
              className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
          </label>
          <label className="text-xs font-semibold faint uppercase">
            Candidates who appear
            <input type="number" inputMode="numeric" min={1} value={appeared} onChange={(e) => setAppeared(Math.max(0, Number(e.target.value) || 0))}
              className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
            <span className="block text-xs font-normal normal-case mt-1 faint">
              {cfg.appearedFixed
                ? (cfg.appearedNote ?? 'Matches the number reported for the 2025-26 cycle.')
                : `Default is about ${fmt(cfg.applicants)} applicants × ${cfg.appearedPct}% attendance. ${cfg.appearedVerified ? '' : 'Both are assumptions, so edit them.'}`}
            </span>
          </label>
          <label className="text-xs font-semibold faint uppercase">
            Candidates shortlisted (anchor rank)
            <input type="number" inputMode="numeric" min={1} value={shortlist} onChange={(e) => setShortlist(Math.max(0, Number(e.target.value) || 0))}
              className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
            <span className="block text-xs font-normal normal-case mt-1 faint">
              {cfg.shortlistFixed ? '' : `${fmt(cfg.vacancies)} vacancies × ${cfg.ratio}. `}{cfg.ratioVerified ? 'Ratio from the notice or result.' : 'The ratio is an assumption.'}
            </span>
          </label>
          <label className="text-xs font-semibold faint uppercase">
            Score of the last shortlisted candidate (out of {max})
            <input type="number" inputMode="decimal" min={0} max={max} value={anchor} placeholder="enter the cut-off you expect"
              onChange={(e) => { setAnchor(e.target.value === '' ? '' : Math.max(0, Math.min(max, Number(e.target.value)))); setPointKey('custom'); }}
              className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
          </label>
        </div>

        {points.length > 0 && (
          <label className="block text-xs font-semibold faint uppercase mt-4">
            Or start from a past cut-off on file
            <select value={pointKey} onChange={(e) => pickPoint(e.target.value)} className="w-full mt-1 p-2 rounded-lg border text-sm font-semibold normal-case" style={input}>
              {points.map((p) => <option key={p.key} value={p.key}>{p.label}</option>)}
              <option value="custom">My own number</option>
            </select>
          </label>
        )}

        <label className="block text-xs font-semibold faint uppercase mt-4">
          How spread out scores are: {r1(spread)}% of the maximum marks
          <input type="range" min={6} max={20} step={0.5} value={spread} onChange={(e) => setSpread(Number(e.target.value))} className="w-full mt-2" aria-label="spread of scores" />
          <span className="block text-xs font-normal normal-case mt-1 faint">A smaller spread means scores bunch together, so a few marks move your rank a lot. The default is borrowed from the shape of the CGL curve, not measured for this exam.</span>
        </label>
      </div>

      {bad && <p className="text-sm mt-4" style={{ color: 'var(--bad)' }}>The shortlist has to be smaller than the number who appear. Check the two numbers.</p>}

      {calc && marks !== '' && (
        <div className="card p-5 mt-5" aria-live="polite">
          <div className="grid grid-cols-3 gap-3 text-center">
            <div><div className="text-3xl font-extrabold">{r1(calc.pct)}</div><div className="text-xs faint font-semibold uppercase">Percentile (est.)</div></div>
            <div><div className="text-2xl sm:text-3xl font-extrabold">{fmt(calc.rank)}</div><div className="text-xs faint font-semibold uppercase">Rank (est.)</div></div>
            <div>
              <div className="text-3xl font-extrabold" style={{ color: gap !== null && gap >= 0 ? 'var(--ok)' : 'var(--bad)' }}>{gap !== null ? (gap >= 0 ? '+' : '') + r1(gap) : '·'}</div>
              <div className="text-xs faint font-semibold uppercase">vs anchor score</div>
            </div>
          </div>
          <p className="text-sm mt-3">
            Plausible range for your rank with this spread: <b>{fmt(calc.lo)}</b> to <b>{fmt(calc.hi)}</b>.{' '}
            {calc.rank <= shortlist
              ? <b style={{ color: 'var(--ok)' }}>That is inside a shortlist of {fmt(shortlist)}.</b>
              : <b style={{ color: 'var(--warn)' }}>That is outside a shortlist of {fmt(shortlist)}.</b>}
          </p>

          <div className="tbl-wrap mt-4">
            <table className="tbl">
              <thead><tr><th>Marks</th><th className="text-right">Percentile</th><th className="text-right">Est. rank</th></tr></thead>
              <tbody>
                {calc.rows.map((r) => (
                  <tr key={r.d} style={r.d === 0 ? { fontWeight: 700, background: 'var(--surface-2)' } : {}}>
                    <td>{r1(r.m)}{r.d === 0 ? ' (your input)' : ` (${r.d > 0 ? '+' : ''}${r.d})`}</td>
                    <td className="text-right">{r1(r.p * 100)}</td>
                    <td className="text-right">{fmt(r.rank)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
      {!calc && !bad && <p className="text-sm muted mt-4">Enter your marks and the cut-off you want to anchor on to see the estimate.</p>}

      <div className="card p-4 mt-5 text-xs faint space-y-2">
        <p><b>How this works.</b> The last shortlisted candidate is placed at rank {fmt(shortlist)} out of {fmt(appeared)}. Scores are assumed to follow a bell curve, so every other mark gets a percentile and a rank from that one anchor. Rank = candidates appeared × (1 − percentile).</p>
        <p>{cfg.ratioNote}</p>
        <p>{cfg.caveat}</p>
        <p>This is a planning estimate. The official body does not publish all-India ranks, and your normalised score decides the real outcome. For a go or no-go call, use the <Link href={`/exams/${id}/score-calculator/`} className="underline decoration-dotted">score calculator</Link> and the <Link href={`/exams/${id}/cutoffs/`} className="underline decoration-dotted">cutoffs page</Link>.</p>
      </div>
    </div>
  );
}
