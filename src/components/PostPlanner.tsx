'use client';
import Link from 'next/link';
import { useEffect, useMemo, useState } from 'react';

export type PlannerPost = {
  id: string; name: string; department: string; group: string; payLevel: string; inHandApprox: string;
  ageMin: number; ageMax: number; paper2?: boolean; special?: string;
};

const RELAX: Record<string, { label: string; years: number }> = {
  UR: { label: 'UR / EWS', years: 0 },
  OBC: { label: 'OBC (NCL)', years: 3 },
  SCST: { label: 'SC / ST', years: 5 },
  PWD: { label: 'PwD (UR)', years: 10 },
  PWDOBC: { label: 'PwD (OBC)', years: 13 },
  PWDSCST: { label: 'PwD (SC / ST)', years: 15 },
};

const KEY = 'es-post-planner';
type Saved = { dob: string; cat: string; stats: boolean; order: string[] };

function read(): Saved | null {
  try { const v = localStorage.getItem(KEY); return v ? JSON.parse(v) : null; } catch { return null; }
}

/** Whole years + months + days between two dates (age "as on" the cutoff date). */
function ageOn(dob: Date, on: Date) {
  let y = on.getFullYear() - dob.getFullYear();
  let m = on.getMonth() - dob.getMonth();
  let d = on.getDate() - dob.getDate();
  if (d < 0) { m--; d += new Date(on.getFullYear(), on.getMonth(), 0).getDate(); }
  if (m < 0) { y--; m += 12; }
  return { y, m, d };
}

function fmt(d: Date) {
  return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
}

export function PostPlanner({ posts, cutoffDate }: { posts: PlannerPost[]; cutoffDate: string }) {
  const [dob, setDob] = useState('');
  const [cat, setCat] = useState('UR');
  const [stats, setStats] = useState(false);
  const [order, setOrder] = useState<string[]>(posts.map((p) => p.id));
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const s = read();
    if (s) {
      setDob(s.dob ?? ''); setCat(s.cat ?? 'UR'); setStats(!!s.stats);
      const known = (s.order ?? []).filter((id) => posts.some((p) => p.id === id));
      setOrder([...known, ...posts.map((p) => p.id).filter((id) => !known.includes(id))]);
    }
    setLoaded(true);
  }, [posts]);

  useEffect(() => {
    if (!loaded) return;
    try { localStorage.setItem(KEY, JSON.stringify({ dob, cat, stats, order } satisfies Saved)); window.dispatchEvent(new Event('es-store')); } catch {}
  }, [dob, cat, stats, order, loaded]);

  const on = useMemo(() => new Date(`${cutoffDate}T00:00:00`), [cutoffDate]);
  const born = dob ? new Date(`${dob}T00:00:00`) : null;
  const age = born && !isNaN(born.getTime()) ? ageOn(born, on) : null;
  const relax = RELAX[cat]?.years ?? 0;

  const status = (p: PlannerPost) => {
    if (!born || !age) return p.paper2 && !stats ? { ok: false, why: 'Needs Statistics in your degree' } : null;
    // Born not earlier than (cutoff − (max+relax) years + 1 day) and not later than (cutoff − min years).
    const earliest = new Date(on); earliest.setFullYear(on.getFullYear() - (p.ageMax + relax)); earliest.setDate(earliest.getDate() + 1);
    const latest = new Date(on); latest.setFullYear(on.getFullYear() - p.ageMin);
    if (born < earliest) return { ok: false, why: `Over age — born before ${fmt(earliest)}` };
    if (born > latest) return { ok: false, why: `Under age — born after ${fmt(latest)}` };
    if (p.paper2 && !stats) return { ok: false, why: 'Age is fine, but you need Statistics in your degree' };
    return { ok: true, why: `Eligible (born ${fmt(earliest)} – ${fmt(latest)})` };
  };

  const byId = Object.fromEntries(posts.map((p) => [p.id, p]));
  const ordered = order.map((id) => byId[id]).filter(Boolean);
  const move = (i: number, dir: -1 | 1) => setOrder((o) => {
    const j = i + dir; if (j < 0 || j >= o.length) return o;
    const n = [...o]; [n[i], n[j]] = [n[j], n[i]]; return n;
  });
  const eligibleCount = posts.filter((p) => status(p)?.ok).length;

  const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };

  return (
    <div>
      <div className="card p-5">
        <h2 className="text-lg font-extrabold">1 · Check your eligibility</h2>
        <p className="text-sm muted mt-1">Age is counted as on <b>{fmt(on)}</b> (the cut-off date for this cycle). Nothing leaves your browser.</p>
        <div className="grid sm:grid-cols-3 gap-3 mt-4 text-sm">
          <label className="font-semibold">Date of birth
            <input type="date" value={dob} onChange={(e) => setDob(e.target.value)} className="w-full mt-1 p-2 rounded-lg border" style={input} />
          </label>
          <label className="font-semibold">Category
            <select value={cat} onChange={(e) => setCat(e.target.value)} className="w-full mt-1 p-2 rounded-lg border" style={input}>
              {Object.entries(RELAX).map(([k, v]) => <option key={k} value={k}>{v.label}{v.years ? ` (+${v.years} yrs)` : ''}</option>)}
            </select>
          </label>
          <label className="font-semibold flex items-end gap-2 pb-2">
            <input type="checkbox" checked={stats} onChange={(e) => setStats(e.target.checked)} className="w-4 h-4" />
            Statistics was a subject in my degree
          </label>
        </div>
        {age && (
          <p className="mt-4 text-sm">
            Your age on {fmt(on)}: <b>{age.y} years {age.m} months {age.d} days</b>
            {relax > 0 && <> · upper limit relaxed by <b>{relax} years</b></>}
            {' '}→ <b style={{ color: eligibleCount ? 'var(--ok)' : 'var(--bad)' }}>{eligibleCount} of {posts.length} posts open to you</b>
          </p>
        )}
      </div>

      <div className="card p-5 mt-5">
        <div className="flex items-center justify-between flex-wrap gap-2">
          <h2 className="text-lg font-extrabold">2 · Build your post preference</h2>
          <button className="btn text-sm" onClick={() => setOrder(posts.map((p) => p.id))}>Reset order</button>
        </div>
        <p className="text-sm muted mt-1">
          SSC asks for your post preference order when you fill the option form, and you can&apos;t change it later. Put the post you want most at the top. A higher preference can only help: SSC gives you the highest-preference post your rank qualifies for. Your order is saved on this device.
        </p>
        <ol className="mt-4 space-y-2">
          {ordered.map((p, i) => {
            const s = status(p);
            return (
              <li key={p.id} className="rounded-xl p-3 flex gap-3 items-start" style={{ background: 'var(--surface-2)', opacity: s && !s.ok ? 0.55 : 1 }}>
                <span className="text-lg font-extrabold w-7 text-center shrink-0" style={{ color: 'var(--brand)' }}>{i + 1}</span>
                <div className="flex-1 min-w-0">
                  <div className="font-bold text-sm">
                    <Link href={`/exams/ssc-cgl/posts/${p.id}/`} className="hover:underline" style={{ color: 'var(--ink)' }}>{p.name}</Link>
                    <span className="chip ml-1.5 text-[10px]">Group {p.group}</span>
                    {p.paper2 && <span className="chip ml-1 text-[10px]">+ Paper 2</span>}
                  </div>
                  <div className="text-xs faint mt-0.5">{p.department} · {p.payLevel} · {p.inHandApprox} · age {p.ageMin}–{p.ageMax}</div>
                  {p.special && <div className="text-xs muted mt-0.5">{p.special}</div>}
                  {s && <div className="text-xs font-semibold mt-1" style={{ color: s.ok ? 'var(--ok)' : 'var(--bad)' }}>{s.ok ? '✓' : '✗'} {s.why}</div>}
                </div>
                <div className="flex flex-col gap-1 shrink-0">
                  <button className="btn text-xs" style={{ padding: '.2rem .5rem' }} onClick={() => move(i, -1)} disabled={i === 0} aria-label={`Move ${p.name} up`}>▲</button>
                  <button className="btn text-xs" style={{ padding: '.2rem .5rem' }} onClick={() => move(i, 1)} disabled={i === ordered.length - 1} aria-label={`Move ${p.name} down`}>▼</button>
                </div>
              </li>
            );
          })}
        </ol>
      </div>
    </div>
  );
}
