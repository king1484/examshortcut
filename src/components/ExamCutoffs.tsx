'use client';
import { useMemo, useState } from 'react';
import { Md } from '@/components/Md';

/* eslint-disable @typescript-eslint/no-explicit-any */

/**
 * Cutoff explorer for every exam except SSC CGL (which keeps CutoffExplorer).
 * The cutoff files are not uniform, so this handles four shapes:
 *  - category cutoffs (UR/OBC/SC…)            → stat cards + trend + table
 *  - state-wise cutoffs (one value per state)  → searchable cards
 *  - state × category cutoffs                  → searchable table
 *  - institute rows (CAT)                      → one card per institute
 */

const CAT_COLORS: Record<string, string> = {
  UR: 'var(--brand)', EWS: 'var(--info)', OBC: 'var(--ok)', SC: 'var(--c-reasoning)', ST: 'var(--warn)',
};

const HEADINGS: Record<string, string> = {
  iims: 'IIMs',
  otherColleges: 'Other top colleges',
  tier1: 'Tier 1',
  tier2: 'Tier 2',
  paper1: 'Paper 1',
  paper2: 'Paper 2',
  prelims: 'Prelims',
  mains: 'Mains',
  final: 'Final selection',
  cbt: 'CBT',
  cbt1: 'CBT 1',
  cbt2: 'CBT 2',
  pet: 'PET',
  qualifying: 'Qualifying marks',
  reserveList: 'Reserve list',
};

function humanize(key: string) {
  if (HEADINGS[key]) return HEADINGS[key];
  return key.replace(/_/g, ' ').replace(/([a-z])([A-Z])/g, '$1 $2').replace(/^./, (c) => c.toUpperCase());
}

const isObj = (v: unknown) => typeof v === 'object' && v !== null;
const show = (n: number) => (Number.isInteger(n) ? String(n) : String(Math.round(n * 100) / 100));
const rowLabel = (r: any) => [r.year ?? r.cycle, r.list ?? r.stage].filter(Boolean).join(' — ');

export function ExamCutoffs({ data }: { data: Record<string, any> }) {
  const sections = useMemo(
    () => Object.entries(data).filter(([k, v]) => k !== 'notes' && k !== 'sources' && Array.isArray(v) && v.length > 0) as [string, any[]][],
    [data],
  );
  const [active, setActive] = useState(0);
  if (sections.length === 0) return <p className="card p-6 mt-6 text-center muted">No cutoff entries yet.</p>;
  const [key, rows] = sections[Math.min(active, sections.length - 1)];

  return (
    <div className="mt-6">
      {sections.length > 1 && (
        <div className="flex gap-2 flex-wrap">
          {sections.map(([k], i) => (
            <button
              key={k}
              className="chip"
              style={i === active ? { background: 'var(--ink)', color: 'var(--bg)' } : {}}
              onClick={() => setActive(i)}
            >
              {humanize(k)}
            </button>
          ))}
        </div>
      )}
      {rows.some((r) => r.institute) ? <InstituteCards key={key} rows={rows} /> : <ListSection key={key} rows={rows} />}
    </div>
  );
}

/* ───────────────────────── list-style sections ───────────────────────── */

function ListSection({ rows }: { rows: any[] }) {
  const sorted = useMemo(() => {
    const hasYears = rows.every((r) => typeof r.year === 'number');
    return hasYears ? [...rows].sort((a, b) => b.year - a.year) : rows;
  }, [rows]);
  const [idx, setIdx] = useState(0);
  const sel = sorted[Math.min(idx, sorted.length - 1)];
  const entries = Object.entries(sel.cutoffs ?? {}) as [string, any][];
  const nested = entries.some(([, v]) => isObj(v));
  const many = entries.length > 8;

  // columns for the all-rows table / trend (category-style data only)
  const cats = useMemo(() => {
    const set = new Set<string>();
    sorted.forEach((r) => Object.keys(r.cutoffs ?? {}).forEach((c) => set.add(c)));
    return [...set];
  }, [sorted]);
  const categoryStyle = !nested && !many && cats.length <= 8;

  return (
    <div>
      {sorted.length > 1 && (
        <div className="mt-4">
          <label className="text-xs font-bold uppercase faint">Which list</label>
          <select className="btn w-full mt-1 text-sm" value={idx} onChange={(e) => setIdx(Number(e.target.value))}>
            {sorted.map((r, i) => <option key={i} value={i}>{rowLabel(r)}</option>)}
          </select>
        </div>
      )}
      {sorted.length === 1 && <p className="mt-4 text-sm font-semibold">{rowLabel(sel)}</p>}

      {nested ? <StateTable cutoffs={sel.cutoffs} /> : many ? <StateCards cutoffs={sel.cutoffs} maxMarks={sel.maxMarks} /> : <StatCards cutoffs={sel.cutoffs} maxMarks={sel.maxMarks} />}

      <RowNotes row={sel} />

      {categoryStyle && <Trend rows={sorted} cats={cats} />}

      {categoryStyle && sorted.length > 1 && (
        <>
          <h2 className="text-xl font-extrabold mt-8">All lists in one table</h2>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>List</th><th>Max</th>{cats.map((c) => <th key={c}>{humanize(c)}</th>)}</tr></thead>
              <tbody>
                {sorted.map((r, i) => (
                  <tr key={i}>
                    <td className="text-xs max-w-64"><b>{r.year ?? r.cycle}</b> · {r.list ?? r.stage}</td>
                    <td>{r.maxMarks ?? '—'}</td>
                    {cats.map((c) => <td key={c}>{r.cutoffs?.[c] ?? '—'}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  );
}

function StatCards({ cutoffs, maxMarks }: { cutoffs: Record<string, any> | undefined; maxMarks?: number | null }) {
  const entries = Object.entries(cutoffs ?? {});
  return (
    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-2.5 mt-4">
      {entries.map(([cat, val]) => {
        const long = typeof val === 'string' && val.length > 40;
        return (
          <div key={cat} className={`card p-4 ${long ? 'sm:col-span-2 lg:col-span-3' : ''}`}>
            <div className="flex items-center gap-2">
              <span className="w-2.5 h-2.5 rounded-full" style={{ background: CAT_COLORS[cat] ?? 'var(--ink-3)' }} />
              <span className="text-xs font-bold uppercase faint">{humanize(cat)}</span>
            </div>
            {typeof val === 'number' ? (
              <>
                <div className="text-2xl font-extrabold mt-1">{show(val)}</div>
                {maxMarks ? <div className="text-xs faint">out of {maxMarks}</div> : null}
              </>
            ) : long ? (
              <Md className="text-sm mt-1">{val}</Md>
            ) : (
              <div className="text-lg font-extrabold mt-1">{String(val)}</div>
            )}
          </div>
        );
      })}
    </div>
  );
}

function StateCards({ cutoffs, maxMarks }: { cutoffs: Record<string, any>; maxMarks?: number | null }) {
  const [q, setQ] = useState('');
  const entries = Object.entries(cutoffs).filter(([k]) => k.toLowerCase().includes(q.trim().toLowerCase()));
  return (
    <div className="mt-4">
      <input className="btn w-full text-sm text-left" placeholder="Search your state…" value={q} onChange={(e) => setQ(e.target.value)} aria-label="Search state" />
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2 mt-3">
        {entries.map(([state, val]) => (
          <div key={state} className="card p-3">
            <div className="text-xs font-bold faint">{state}</div>
            <div className="text-xl font-extrabold">{typeof val === 'number' ? show(val) : String(val)}</div>
            {maxMarks ? <div className="text-[11px] faint">out of {maxMarks}</div> : null}
          </div>
        ))}
        {entries.length === 0 && <p className="muted text-sm col-span-full">No state matches “{q}”.</p>}
      </div>
    </div>
  );
}

function StateTable({ cutoffs }: { cutoffs: Record<string, any> }) {
  const [q, setQ] = useState('');
  const cats = useMemo(() => {
    const set = new Set<string>();
    Object.values(cutoffs).forEach((v) => isObj(v) && Object.keys(v).forEach((c) => set.add(c)));
    return [...set];
  }, [cutoffs]);
  const entries = Object.entries(cutoffs).filter(([k]) => k.toLowerCase().includes(q.trim().toLowerCase()));
  return (
    <div className="mt-4">
      <input className="btn w-full text-sm text-left" placeholder="Search your state…" value={q} onChange={(e) => setQ(e.target.value)} aria-label="Search state" />
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>State / UT</th>{cats.map((c) => <th key={c}>{c}</th>)}</tr></thead>
          <tbody>
            {entries.map(([state, v]) => (
              <tr key={state}>
                <td className="font-bold">{state}</td>
                {cats.map((c) => <td key={c}>{(v as Record<string, any>)?.[c] ?? '—'}</td>)}
              </tr>
            ))}
            {entries.length === 0 && <tr><td colSpan={cats.length + 1} className="muted">No state matches “{q}”.</td></tr>}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function RowNotes({ row }: { row: any }) {
  const extra = row.reserveList as Record<string, any> | undefined;
  const text = [row.note, row.notes, typeof row.categoryNotes === 'string' ? row.categoryNotes : null].filter(Boolean) as string[];
  return (
    <>
      {extra && (
        <div className="card p-4 mt-3">
          <div className="text-xs font-bold uppercase faint">Reserve list</div>
          <div className="flex flex-wrap gap-x-5 gap-y-1 mt-1 text-sm">
            {Object.entries(extra).filter(([k, v]) => k !== 'notes' && typeof v === 'number').map(([k, v]) => (
              <span key={k}><b>{k}</b> {show(v as number)}</span>
            ))}
          </div>
          {extra.notes && <p className="text-xs faint mt-1">{extra.notes}</p>}
        </div>
      )}
      {isObj(row.categoryNotes) && (
        <div className="card p-4 mt-3 text-sm space-y-0.5">
          {Object.entries(row.categoryNotes).map(([k, v]) => <p key={k}><b>{humanize(k)}:</b> <Md inline>{String(v)}</Md></p>)}
        </div>
      )}
      {text.map((t, i) => <Md key={i} className="text-sm muted mt-3">{t}</Md>)}
      {row.source && <p className="text-[11px] faint mt-2">Source: {row.source}</p>}
    </>
  );
}

function Trend({ rows, cats }: { rows: any[]; cats: string[] }) {
  const [cat, setCat] = useState(cats.includes('UR') ? 'UR' : cats[0]);
  const years = rows.map((r) => r.year);
  const usable =
    rows.length >= 2 &&
    years.every((y) => typeof y === 'number') &&
    new Set(years).size === years.length &&
    new Set(rows.map((r) => r.maxMarks)).size === 1;
  if (!usable) return null;
  const pts = [...rows]
    .sort((a, b) => a.year - b.year)
    .filter((r) => typeof r.cutoffs?.[cat] === 'number')
    .map((r) => ({ year: r.year as number, v: r.cutoffs[cat] as number }));
  const maxMarks = rows[0].maxMarks;

  const W = 560, H = 200, P = 36;
  const minY = pts.length ? Math.min(...pts.map((p) => p.v)) - 5 : 0;
  const maxY = pts.length ? Math.max(...pts.map((p) => p.v)) + 5 : 1;
  const x = (i: number) => P + (i * (W - 2 * P)) / Math.max(1, pts.length - 1);
  const y = (v: number) => H - P - ((v - minY) * (H - 2 * P)) / (maxY - minY);
  const path = pts.map((p, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)},${y(p.v).toFixed(1)}`).join(' ');
  const color = CAT_COLORS[cat] ?? 'var(--brand)';

  return (
    <div className="card p-4 mt-6">
      <h3 className="font-bold text-sm">Trend across years (pick a category)</h3>
      <div className="flex gap-1.5 flex-wrap mt-3">
        {cats.map((c) => (
          <button key={c} className="chip" style={cat === c ? { background: CAT_COLORS[c] ?? 'var(--ink)', color: '#fff', borderColor: 'transparent' } : {}} onClick={() => setCat(c)}>{c}</button>
        ))}
      </div>
      {pts.length < 2 ? (
        <p className="text-sm muted mt-2">Not enough years of data for {cat}.</p>
      ) : (
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
              <text x={x(i)} y={y(p.v) - 9} fontSize="10" fontWeight="700" fill="var(--ink)" textAnchor="middle">{show(p.v)}</text>
            </g>
          ))}
        </svg>
      )}
      <p className="text-[11px] faint">Maximum marks in these lists: {maxMarks}. Marking schemes can change between cycles, so read the trend as a band, not a promise.</p>
    </div>
  );
}

/* ───────────────────────── institute rows (CAT) ───────────────────────── */

function KV({ obj }: { obj: Record<string, any> }) {
  const label = typeof obj.label === 'string' ? obj.label : null;
  const rest = Object.entries(obj).filter(([k, v]) => k !== 'label' && v !== null && v !== undefined && v !== '');
  return (
    <div>
      {label && <p className="text-xs font-bold uppercase faint">{label}</p>}
      <ul className="text-[13px] leading-snug space-y-1 mt-1">
        {rest.map(([k, v]) => (
          <li key={k}>
            <b>{humanize(k)}:</b> {isObj(v) ? <KV obj={v} /> : <Md inline>{String(v)}</Md>}
          </li>
        ))}
      </ul>
    </div>
  );
}

function InstituteCards({ rows }: { rows: any[] }) {
  const [q, setQ] = useState('');
  const shown = rows.filter((r) => String(r.institute).toLowerCase().includes(q.trim().toLowerCase()));
  return (
    <div className="mt-4">
      <input className="btn w-full text-sm text-left" placeholder="Search a college…" value={q} onChange={(e) => setQ(e.target.value)} aria-label="Search college" />
      <div className="grid md:grid-cols-2 gap-3 mt-3">
        {shown.map((r, i) => (
          <div key={i} className="card p-4 space-y-3">
            <div>
              <h3 className="font-extrabold text-base">{r.institute}</h3>
              <div className="flex gap-2 flex-wrap mt-1.5">
                {r.tier && <span className="chip">{r.tier}</span>}
              </div>
              {r.cycle && <p className="text-xs faint mt-1.5">{r.cycle}</p>}
            </div>
            {isObj(r.qualifying) && <KV obj={r.qualifying} />}
            {isObj(r.shortlist) && <KV obj={r.shortlist} />}
          </div>
        ))}
        {shown.length === 0 && <p className="muted text-sm col-span-full">No college matches “{q}”.</p>}
      </div>
    </div>
  );
}
