'use client';
import { useMemo, useState } from 'react';

/* eslint-disable @typescript-eslint/no-explicit-any */

interface SecState { correct: number; wrong: number; total: number }
const T1: Record<string, number> = { quant: 25, reasoning: 25, english: 25, ga: 25 };

export function ScoreCalculator({ cutoffs, latestYear }: { cutoffs: any; latestYear: number }) {
  const [mode, setMode] = useState<'tier1' | 'tier2'>('tier1');
  const [sec, setSec] = useState<Record<string, SecState>>(() =>
    Object.fromEntries(Object.entries(T1).map(([k, v]) => [k, { correct: 0, wrong: 0, total: v }])));
  const [t2, setT2] = useState<SecState>({ correct: 0, wrong: 0, total: 150 });

  const cats = useMemo(() => {
    const lists = (cutoffs?.tier1 ?? []) as any[];
    const latest = lists.filter((l) => l.cutoffs).sort((a, b) => b.year - a.year)[0];
    return latest ? { year: latest.year, cutoffs: latest.cutoffs as Record<string, number>, list: latest.list } : null;
  }, [cutoffs]);

  const [cat, setCat] = useState('UR');
  const active = mode === 'tier1' ? sec : { all: t2 };
  const keys = Object.keys(active);

  const attempted = keys.reduce((n, k) => n + active[k].correct + active[k].wrong, 0);
  const totalQ = keys.reduce((n, k) => n + active[k].total, 0);
  const plus = mode === 'tier1' ? 2 : 3;
  const minus = mode === 'tier1' ? 0.5 : 1;
  const correct = keys.reduce((n, k) => n + active[k].correct, 0);
  const wrong = keys.reduce((n, k) => n + active[k].wrong, 0);
  const raw = correct * plus - wrong * minus;
  const accuracy = correct + wrong ? Math.round((100 * correct) / (correct + wrong)) : 0;

  // Normalisation heuristics (widely observed ranges, NOT official): typical normalised score
  // drifts ±5-10 marks from raw depending on shift difficulty. Show a band.
  const normLow = raw - 7, normHigh = raw + 5;
  const cutoff = cats?.cutoffs?.[cat] ?? null;
  const gap = cutoff !== null ? raw - cutoff : null;
  const verdict =
    gap === null ? null :
    gap >= 20 ? { t: 'Strong — this was a cutoff-clearing score in recent years', c: 'var(--ok)' } :
    gap >= 0 ? { t: 'Around the cutoff — borderline. Push accuracy and attempts', c: 'var(--warn)' } :
    gap >= -20 ? { t: 'Close — 10-20 more marks is very doable with 5-6 more correct answers', c: 'var(--warn)' } :
    { t: 'Well below the cutoff — rebuild weak topics before more mocks', c: 'var(--bad)' };

  const update = (k: string, field: keyof SecState, val: number) => {
    if (mode === 'tier1') {
      setSec((p) => {
        const s = { ...p[k] };
        (s[field] as number) = Math.max(0, Math.min(val, field === 'correct' || field === 'wrong' ? s.total : 400));
        if (s.correct + s.wrong > s.total) { if (field === 'correct') s.wrong = s.total - s.correct; else s.correct = s.total - s.wrong; }
        return { ...p, [k]: s };
      });
    } else {
      setT2((p) => {
        const s = { ...p };
        (s[field] as number) = Math.max(0, Math.min(val, field === 'correct' || field === 'wrong' ? s.total : 400));
        if (s.correct + s.wrong > s.total) { if (field === 'correct') s.wrong = s.total - s.correct; else s.correct = s.total - s.wrong; }
        return s;
      });
    }
  };

  const names: Record<string, string> = { quant: 'Quant', reasoning: 'Reasoning', english: 'English', ga: 'General Awareness', all: 'All sections (Paper 1)' };

  return (
    <div className="mt-6">
      <div className="flex gap-2">
        {(['tier1', 'tier2'] as const).map((m) => (
          <button key={m} className="chip" style={mode === m ? { background: 'var(--ink)', color: 'var(--bg)' } : {}} onClick={() => setMode(m)}>
            {m === 'tier1' ? 'Tier 1 (100 Q)' : 'Tier 2 Paper 1 (150 Q)'}
          </button>
        ))}
      </div>

      <div className="space-y-3 mt-5">
        {keys.map((k) => {
          const s = active[k];
          return (
            <div key={k} className="card p-4">
              <div className="flex items-center justify-between gap-2 flex-wrap">
                <span className="font-bold text-sm">{names[k] ?? k}</span>
                <span className="text-xs faint">{s.correct + s.wrong}/{s.total} attempted</span>
              </div>
              <div className="grid grid-cols-2 gap-3 mt-2">
                {(['correct', 'wrong'] as const).map((f) => (
                  <label key={f} className="text-xs font-semibold faint uppercase">
                    {f}
                    <input type="number" min={0} max={s.total} value={s[f]} onChange={(e) => update(k, f, Number(e.target.value) || 0)}
                      className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={{ borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' }} />
                  </label>
                ))}
              </div>
              <input type="range" min={0} max={s.total} value={s.correct + s.wrong} readOnly className="w-full mt-2" aria-label="attempted slider" />
            </div>
          );
        })}
      </div>

      <div className="card p-5 mt-5">
        <div className="grid grid-cols-3 gap-3 text-center">
          <div><div className="text-3xl font-extrabold">{raw.toFixed(mode === 'tier1' ? 2 : 0).replace(/\.00$/, '')}</div><div className="text-xs faint font-semibold uppercase">Net score / {totalQ * plus}</div></div>
          <div><div className="text-3xl font-extrabold">{accuracy}%</div><div className="text-xs faint font-semibold uppercase">Accuracy</div></div>
          <div><div className="text-3xl font-extrabold">{attempted}<span className="text-base faint">/{totalQ}</span></div><div className="text-xs faint font-semibold uppercase">Attempted</div></div>
        </div>

        <div className="tbl-wrap mt-4">
          <table className="tbl">
            <tbody>
              <tr><td>Correct × +{plus}</td><td className="text-right">+{(correct * plus).toFixed(2).replace(/\.00$/, '')}</td></tr>
              <tr><td>Wrong × −{minus}</td><td className="text-right" style={{ color: 'var(--bad)' }}>−{(wrong * minus).toFixed(2).replace(/\.00$/, '')}</td></tr>
              <tr><td className="font-bold">Net (before normalisation)</td><td className="text-right font-bold">{raw.toFixed(2).replace(/\.00$/, '')}</td></tr>
              <tr><td>Likely normalised band*</td><td className="text-right">{normLow.toFixed(1)} – {normHigh.toFixed(1)}</td></tr>
            </tbody>
          </table>
        </div>

        {cats && mode === 'tier1' && (
          <div className="mt-4">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-sm font-bold">Compare with {cats.year} cutoff:</span>
              {Object.keys(cats.cutoffs).map((c) => (
                <button key={c} className="chip" style={cat === c ? { background: 'var(--ink)', color: 'var(--bg)' } : {}} onClick={() => setCat(c)}>{c}</button>
              ))}
            </div>
            {(() => {
              const c = cats.cutoffs[cat];
              const pct = Math.max(0, Math.min(100, (raw / c) * 100));
              return (
                <div className="mt-3">
                  <div className="h-4 rounded-full overflow-hidden relative" style={{ background: 'var(--surface-2)' }}>
                    <div className="h-full" style={{ width: `${pct}%`, background: gap !== null && gap >= 0 ? 'var(--ok)' : 'var(--warn)' }} />
                    <div className="absolute top-0 bottom-0 w-0.5" style={{ left: '100%', background: 'var(--ink)' }} title={`cutoff ${c}`} />
                  </div>
                  <p className="text-sm mt-2">
                    Cutoff <b>{c}</b> · your net <b>{raw.toFixed(2).replace(/\.00$/, '')}</b> ·{' '}
                    {gap !== null && <b style={{ color: verdict?.c }}>{gap >= 0 ? '+' : ''}{gap.toFixed(2).replace(/\.00$/, '')} vs cutoff</b>}
                  </p>
                  {verdict && <p className="text-sm font-semibold mt-1" style={{ color: verdict.c }}>{verdict.t}</p>}
                  <p className="text-xs faint mt-2">List used: {cats.list}. *Normalisation band is an estimate based on typical year-to-year/shift-to-shift movement — SSC's exact normalised score depends on your shift's difficulty.</p>
                </div>
              );
            })()}
          </div>
        )}
      </div>
    </div>
  );
}
