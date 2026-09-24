'use client';
import { useMemo, useState } from 'react';

/* eslint-disable @typescript-eslint/no-explicit-any */

const CAT_COLORS: Record<string, string> = {
  UR: 'var(--brand)', EWS: 'var(--info)', OBC: 'var(--ok)', SC: 'var(--c-reasoning)', ST: 'var(--warn)',
};

export function CutoffExplorer({ data }: { data: any }) {
  const [kind, setKind] = useState<'tier1' | 'final'>('tier1');
  const lists: any[] = data[kind] ?? [];
  const listsSorted = useMemo(() => [...lists].sort((a, b) => (a.year - b.year)), [lists]);
  const [listIdx, setListIdx] = useState(listsSorted.length - 1);
  const list = listsSorted[Math.min(listIdx, listsSorted.length - 1)];
  const cats = useMemo(() => {
    const set = new Set<string>();
    listsSorted.forEach((l) => Object.keys(l.cutoffs ?? {}).forEach((c) => set.add(c)));
    return [...set];
  }, [listsSorted]);

  if (listsSorted.length === 0) return <p className="card p-6 mt-6 text-center muted">No cutoff entries yet.</p>;

  return (
    <div className="mt-6">
      <div className="flex gap-2">
        {(['tier1', 'final'] as const).map((k) => (
          <button key={k} className="chip" style={kind === k ? { background: 'var(--ink)', color: 'var(--bg)' } : {}}
            onClick={() => { setKind(k); const l = (data[k] ?? []).sort((a: any, b: any) => a.year - b.year); setListIdx(l.length - 1); }}>
            {k === 'tier1' ? 'Tier 1 (→ Tier 2)' : 'Final selection'}
          </button>
        ))}
      </div>

      <div className="mt-4">
        <label className="text-xs font-bold uppercase faint">Which list</label>
        <select className="btn w-full mt-1 text-sm" value={listIdx} onChange={(e) => setListIdx(Number(e.target.value))}>
          {listsSorted.map((l, i) => <option key={i} value={i}>{l.year} — {l.list}</option>)}
        </select>
      </div>

      {list?.cutoffs && (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-2.5 mt-4">
          {Object.entries(list.cutoffs as Record<string, number>).map(([cat, val]) => (
            <div key={cat} className="card p-4">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full" style={{ background: CAT_COLORS[cat] ?? 'var(--ink-3)' }} />
                <span className="text-xs font-bold uppercase faint">{cat}</span>
              </div>
              <div className="text-2xl font-extrabold mt-1">{val}</div>
              <div className="text-xs faint">out of {list.maxMarks}</div>
            </div>
          ))}
        </div>
      )}

      <div className="card p-4 mt-6">
        <h3 className="font-bold text-sm">Trend across years (pick a category)</h3>
        <Trend lists={listsSorted} cats={cats} maxMarks={list?.maxMarks ?? 200} />
      </div>

      <h2 className="text-xl font-extrabold mt-8">Full table</h2>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>Year</th><th>List</th>{cats.map((c) => <th key={c}>{c}</th>)}</tr></thead>
          <tbody>
            {listsSorted.slice().reverse().map((l, i) => (
              <tr key={i}>
                <td className="font-bold">{l.year}</td>
                <td className="text-xs max-w-56">{l.list}</td>
                {cats.map((c) => <td key={c}>{(l.cutoffs ?? {})[c] ?? '—'}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
  );
}

function Trend({ lists, cats, maxMarks }: { lists: any[]; cats: string[]; maxMarks: number }) {
  const [cat, setCat] = useState(cats.includes('UR') ? 'UR' : cats[0]);
  const pts = lists.filter((l) => typeof l.cutoffs?.[cat] === 'number').map((l) => ({ year: l.year, v: l.cutoffs[cat] }));
  if (pts.length < 2) return <p className="text-sm muted mt-2">Not enough years of data for a trend line.</p>;
  const W = 560, H = 200, P = 36;
  const years = pts.map((p) => p.year);
  const minY = Math.min(...pts.map((p) => p.v)) - 5, maxY = Math.max(...pts.map((p) => p.v)) + 5;
  const x = (i: number) => P + (i * (W - 2 * P)) / (pts.length - 1);
  const y = (v: number) => H - P - ((v - minY) * (H - 2 * P)) / (maxY - minY);
  const path = pts.map((p, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)},${y(p.v).toFixed(1)}`).join(' ');
  const color = CAT_COLORS[cat] ?? 'var(--brand)';
  return (
    <div className="mt-3">
      <div className="flex gap-1.5 flex-wrap">
        {cats.map((c) => <button key={c} className="chip" style={cat === c ? { background: CAT_COLORS[c] ?? 'var(--ink)', color: '#fff', borderColor: 'transparent' } : {}} onClick={() => setCat(c)}>{c}</button>)}
      </div>
      <svg viewBox={`0 0 ${W} ${H}`} className="w-full mt-2" role="img" aria-label={`Cutoff trend for ${cat}`}>
        {[0, 0.25, 0.5, 0.75, 1].map((f) => {
          const v = minY + f * (maxY - minY);
          return (
            <g key={f}>
              <line x1={P} x2={W - P / 2} y1={y(v)} y2={y(v)} stroke="var(--line)" strokeWidth="1" />
              <text x={4} y={y(v) + 4} fontSize="10" fill="var(--ink-3)">{Math.round(v)}</text>
            </g>
          );
        })}
        <path d={path} fill="none" stroke={color} strokeWidth="2.5" strokeLinecap="round" />
        {pts.map((p, i) => (
          <g key={i}>
            <circle cx={x(i)} cy={y(p.v)} r="4" fill={color} />
            <text x={x(i)} y={H - 12} fontSize="10" fill="var(--ink-3)" textAnchor="middle">{p.year}</text>
            <text x={x(i)} y={y(p.v) - 9} fontSize="10" fontWeight="700" fill="var(--ink)" textAnchor="middle">{p.v}</text>
          </g>
        ))}
      </svg>
      <p className="text-[11px] faint">Maximum marks in these lists: {maxMarks}. Values are official cutoffs, pre-normalisation basis as published by SSC.</p>
    </div>
  );
}
