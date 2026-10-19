'use client';
import { Spinner } from './Spinner';
import { canTrack } from '@/lib/store';
import Link from 'next/link';
import { useEffect, useMemo, useState } from 'react';

export type PlanTopic = { section: string; sectionShort: string; color: string; id: string; title: string; importance?: string; nSub: number; nPractice: number };
export type PlanMock = { id: string; title: string; tier: number; available: boolean };

type Level = 'weak' | 'avg' | 'strong';
type Config = { target: 'tier1' | 'tier2'; t1Date: string; t2Date: string; hours: number; levels: Record<string, Level>; start?: string };
type Item = { key: string; kind: 'topic' | 'mock' | 'revise'; label: string; sub: string; hours: number; href?: string; color: string };

const KEY = 'es-study-plan';
const IMP_W: Record<string, number> = { high: 1.3, medium: 1, low: 0.7 };
const LVL_W: Record<Level, number> = { weak: 1.4, avg: 1, strong: 0.6 };
const T1_SECTIONS = ['quant', 'reasoning', 'english', 'ga'];

function isoDay(d: Date) { return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; }
function addDays(d: Date, n: number) { const x = new Date(d); x.setDate(x.getDate() + n); return x; }
const round = (h: number) => Math.round(h * 2) / 2;

/**
 * Turns (days left × hours/day) into a dated plan: topics interleaved across sections,
 * a full mock every 7th day, and the last ~20% of days reserved for mocks + revision.
 * When time is short, low-importance topics are dropped and the rest compressed.
 */
function buildPlan(topics: PlanTopic[], mocks: PlanMock[], cfg: Config, today: Date) {
  // The plan is anchored to the day it was started, so ticks and topic order don't shift day to day.
  const start = cfg.start ? new Date(`${cfg.start}T00:00:00`) : today;
  const examDate = new Date(`${cfg.target === 'tier1' ? cfg.t1Date : cfg.t2Date}T00:00:00`);
  const days = Math.round((examDate.getTime() - start.getTime()) / 86400000);
  if (!(days > 0)) return { days, plan: [] as { date: Date; items: Item[] }[], dropped: [] as PlanTopic[], ratio: 1, start };

  const sections = cfg.target === 'tier1' ? T1_SECTIONS : [...T1_SECTIONS, 'computer'];
  const pool = topics.filter((t) => sections.includes(t.section));
  const need = (t: PlanTopic) => (1 + 0.5 * t.nSub + (t.nPractice ? 0.5 : 0)) * (IMP_W[t.importance ?? 'medium'] ?? 1) * LVL_W[cfg.levels[t.section] ?? 'avg'];

  const reserve = days >= 5 ? Math.max(1, Math.round(days * 0.2)) : 0;
  const studyDays = days - reserve;
  const mockEvery = 7;
  const mockDays = Math.floor(studyDays / mockEvery);
  const available = (studyDays - mockDays) * cfg.hours;

  let chosen = pool;
  let totalNeed = chosen.reduce((a, t) => a + need(t), 0);
  const dropped: PlanTopic[] = [];
  // Short on time: drop low, then medium importance topics, until the need is under 2× what fits.
  for (const imp of ['low', 'medium']) {
    if (totalNeed <= available * 2) break;
    const drop = chosen.filter((t) => (t.importance ?? 'medium') === imp);
    dropped.push(...drop);
    chosen = chosen.filter((t) => (t.importance ?? 'medium') !== imp);
    totalNeed = chosen.reduce((a, t) => a + need(t), 0);
  }
  const ratio = Math.min(1, available / Math.max(1, totalNeed));

  // Interleave sections (round-robin, keeping each section's study order).
  const queues = sections.map((s) => chosen.filter((t) => t.section === s));
  const ordered: PlanTopic[] = [];
  while (queues.some((q) => q.length)) for (const q of queues) { const t = q.shift(); if (t) ordered.push(t); }
  const work = ordered.map((t) => ({ t, left: Math.max(0.5, round(need(t) * ratio)), started: false }));

  const tierMocks = mocks.filter((m) => m.available && m.tier === (cfg.target === 'tier1' ? 1 : 2));
  const anyMocks = tierMocks.length ? tierMocks : mocks.filter((m) => m.available);
  let mockIdx = 0;
  const nextMock = (iso: string): Item => {
    const m = anyMocks[mockIdx++ % Math.max(1, anyMocks.length)];
    return { key: `mock@${iso}`, kind: 'mock', label: m ? m.title : 'Full-length mock', sub: 'Full mock in exam conditions + 45 min reviewing every wrong and skipped question', hours: cfg.hours, href: m ? `/exams/ssc-cgl/mocks/${m.id}/` : '/exams/ssc-cgl/mocks/', color: 'var(--brand)' };
  };

  const plan: { date: Date; items: Item[] }[] = [];
  let wi = 0;
  for (let d = 0; d < days; d++) {
    const date = addDays(start, d);
    const iso = isoDay(date);
    const items: Item[] = [];
    const inReserve = d >= studyDays;
    if (inReserve || ((d + 1) % mockEvery === 0 && d > 0)) {
      if (inReserve && (d - studyDays) % 2 === 1) {
        items.push({ key: `rev@${iso}`, kind: 'revise', label: 'Revision day', sub: 'Formula sheet, your mistakes notebook, and the topics where your topic-test score was under 60%', hours: cfg.hours, href: '/revision/', color: 'var(--info)' });
      } else items.push(nextMock(iso));
    } else {
      let cap = cfg.hours;
      while (cap > 0.25 && wi < work.length) {
        const w = work[wi];
        const h = Math.min(cap, w.left);
        const finishing = h >= w.left;
        items.push({
          key: `${w.t.section}/${w.t.id}@${iso}`, kind: 'topic', label: `${w.t.sectionShort} · ${w.t.title}${w.started ? ' (contd.)' : ''}`,
          sub: ratio < 0.4 ? (finishing ? 'Quick pass: Formulas tab + shortcut tricks, then the topic test' : 'Quick pass: Overview + Formulas tab')
            : finishing ? 'Finish Learn + Formulas, then take the topic test' : 'Learn pages + solved examples',
          hours: round(h), href: `/${w.t.section}/${w.t.id}/${finishing ? 'practice/' : 'learn/'}`, color: w.t.color,
        });
        w.left = round(w.left - h); cap -= h; w.started = true;
        if (w.left <= 0) wi++;
      }
      if (wi >= work.length && cap > 0.25) items.push({ key: `slack@${iso}`, kind: 'revise', label: 'Sectional practice / weak topics', sub: 'Redo topic tests where you scored under 70%', hours: round(cap), href: '/dashboard/', color: 'var(--info)' });
    }
    plan.push({ date, items });
  }
  return { days, plan, dropped, ratio, start };
}

export function StudyPlanner({ topics, mocks, t1Default, t2Default }: { topics: PlanTopic[]; mocks: PlanMock[]; t1Default: string; t2Default: string }) {
  const [cfg, setCfg] = useState<Config>({ target: 'tier1', t1Date: t1Default, t2Date: t2Default, hours: 6, levels: {} });
  const [done, setDone] = useState<Record<string, boolean>>({});
  const [today, setToday] = useState<Date | null>(null);

  useEffect(() => {
    const n = new Date(); const t = new Date(n.getFullYear(), n.getMonth(), n.getDate());
    const todayIso = isoDay(t);
    /* The page supplies Tier 1's last exam date as the default. Once that date is past,
       start on Tier 2 instead of opening on a plan that immediately says the date has passed. */
    const defaultTarget: Config['target'] = t1Default < todayIso ? 'tier2' : 'tier1';
    try {
      const s = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (s?.cfg) {
        const saved = s.cfg as Partial<Config>;
        setCfg((c) => ({
          ...c,
          ...saved,
          target: saved.target ?? defaultTarget,
          t1Date: saved.t1Date || t1Default,
          t2Date: saved.t2Date || t2Default,
        }));
      } else {
        setCfg((c) => ({ ...c, target: defaultTarget }));
      }
      if (s?.done) setDone(s.done);
    } catch {}
    setToday(t);
    setCfg((c) => (c.start ? c : { ...c, start: isoDay(t) }));
  }, [t1Default, t2Default]);
  const result = useMemo(() => (today ? buildPlan(topics, mocks, cfg, today) : null), [topics, mocks, cfg, today]);

  useEffect(() => {
    if (!today || !result) return;
    if (!canTrack()) return;
    try { localStorage.setItem(KEY, JSON.stringify({ cfg, done, total: result.plan.flatMap((p) => p.items).length })); window.dispatchEvent(new Event('es-store')); } catch {}
  }, [cfg, done, today, result]);
  const set = <K extends keyof Config>(k: K, v: Config[K]) => setCfg((c) => ({ ...c, [k]: v }));
  const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };
  const sections = cfg.target === 'tier1' ? T1_SECTIONS : [...T1_SECTIONS, 'computer'];
  const secMeta = (s: string) => topics.find((t) => t.section === s);

  const allItems = result?.plan.flatMap((p) => p.items) ?? [];
  const doneCount = allItems.filter((i) => done[i.key]).length;

  return (
    <div>
      <div className="card p-5 print:hidden">
        <div className="grid sm:grid-cols-3 gap-3 text-sm">
          <label className="font-semibold">Preparing for
            <select value={cfg.target} onChange={(e) => set('target', e.target.value as Config['target'])} className="w-full mt-1 p-2 rounded-lg border" style={input}>
              <option value="tier1">Tier 1</option>
              <option value="tier2">Tier 2 (Paper 1 + Computer)</option>
            </select>
          </label>
          <label className="font-semibold">Exam date
            {cfg.target === 'tier1'
              ? <input type="date" value={cfg.t1Date} onChange={(e) => set('t1Date', e.target.value)} className="w-full mt-1 p-2 rounded-lg border" style={input} />
              : <input type="date" value={cfg.t2Date} onChange={(e) => set('t2Date', e.target.value)} className="w-full mt-1 p-2 rounded-lg border" style={input} />}
          </label>
          <label className="font-semibold">Study hours per day: {cfg.hours}
            <input type="range" min={1} max={12} step={0.5} value={cfg.hours} onChange={(e) => set('hours', Number(e.target.value))} className="w-full mt-3" />
          </label>
        </div>
        <div className="mt-4 text-sm">
          <div className="font-semibold">How strong are you in each section?</div>
          <div className="grid sm:grid-cols-2 gap-2 mt-2">
            {sections.map((s) => (
              <div key={s} className="flex items-center gap-2 rounded-lg p-2" style={{ background: 'var(--surface-2)' }}>
                <span className="font-bold w-24" style={{ color: secMeta(s)?.color }}>{secMeta(s)?.sectionShort ?? s}</span>
                {(['weak', 'avg', 'strong'] as Level[]).map((l) => (
                  <button key={l} className="btn text-xs flex-1" style={{ padding: '.25rem .4rem', ...((cfg.levels[s] ?? 'avg') === l ? { background: 'var(--brand)', color: 'var(--brand-ink)', borderColor: 'var(--brand)' } : {}) }}
                    onClick={() => set('levels', { ...cfg.levels, [s]: l })}>{l === 'avg' ? 'average' : l}</button>
                ))}
              </div>
            ))}
          </div>
        </div>
        {cfg.target === 'tier2' && <p className="text-xs faint mt-3">SSC announces Tier 2 dates after Tier 1 ends. The default date is only an estimate based on last year&apos;s gap, so set your own once dates are announced.</p>}
      </div>

      {!result ? <div className="card mt-5"><Spinner label="Building your plan" /></div> :
        result.days <= 0 ? <p className="card p-6 mt-5 text-center muted">That exam date has passed. Pick a future date above.</p> : (
        <>
          <div className="card p-5 mt-5">
            <div className="flex items-center justify-between flex-wrap gap-2">
              <h2 className="text-lg font-extrabold">{result.days} days · {Math.round(result.days * cfg.hours)} study hours</h2>
              <span className="flex gap-2 items-center print:hidden">
                <span className="chip">{doneCount}/{allItems.length} done</span>
                <button className="btn text-sm" onClick={() => window.print()}>🖨️ Print</button>
                {today && cfg.start !== isoDay(today) && <button className="btn text-sm" title="Re-plan the remaining syllabus starting today" onClick={() => { setDone({}); set('start', isoDay(today)); }}>↻ Restart from today</button>}
                {doneCount > 0 && <button className="btn text-sm" onClick={() => setDone({})}>Clear ticks</button>}
              </span>
            </div>
            <div className="h-2 rounded-full overflow-hidden mt-3" style={{ background: 'var(--surface-2)' }}>
              <div className="h-full" style={{ width: `${(100 * doneCount) / Math.max(1, allItems.length)}%`, background: 'var(--ok)' }} />
            </div>
            {(result.ratio < 1 || result.dropped.length > 0) && (
              <div className="mt-3 text-sm rounded-lg p-3" style={{ background: 'var(--warn-soft)', color: 'var(--warn)' }}>
                <b>Compressed plan.</b> There isn&apos;t enough time to cover everything properly, so topic time is cut to about {Math.round(result.ratio * 100)}% of normal.
                {result.dropped.length > 0 && <> {result.dropped.length} lower-weightage topics are left out: {result.dropped.slice(0, 8).map((t) => t.title).join(', ')}{result.dropped.length > 8 ? '…' : ''}. Use the <Link className="underline" href="/formula-sheet/">formula sheet</Link> for these.</>}
              </div>
            )}
          </div>

          <ol className="mt-4 space-y-3">
            {result.plan.map((day, di) => {
              const isToday = !!today && isoDay(day.date) === isoDay(today);
              const isPast = !!today && day.date < today;
              const dayDone = day.items.every((i) => done[i.key]);
              return (
                <li key={di} className="card p-4" style={isToday ? { borderColor: 'var(--brand)', borderWidth: 2 } : isPast ? { opacity: 0.7 } : undefined}>
                  <div className="flex items-center gap-2 text-sm">
                    <span className="font-extrabold">Day {di + 1}</span>
                    <span className="faint">{day.date.toLocaleDateString('en-IN', { weekday: 'short', day: 'numeric', month: 'short' })}</span>
                    {isToday && <span className="chip chip-high text-xs">today</span>}
                    {dayDone && <span className="chip text-xs" style={{ background: 'var(--ok-soft)', color: 'var(--ok)', borderColor: 'transparent' }}>✓ done</span>}
                  </div>
                  <ul className="mt-2 space-y-1.5">
                    {day.items.map((it) => (
                      <li key={it.key} className="flex items-start gap-2.5 text-sm">
                        <input type="checkbox" className="mt-1 w-4 h-4 shrink-0" checked={!!done[it.key]} aria-label={`Mark ${it.label} done`}
                          onChange={() => setDone((d) => { const n = { ...d }; if (n[it.key]) delete n[it.key]; else n[it.key] = true; return n; })} />
                        <span className="w-1 self-stretch rounded-full shrink-0" style={{ background: it.color }} />
                        <span className="flex-1 min-w-0" style={{ textDecoration: done[it.key] ? 'line-through' : undefined, opacity: done[it.key] ? 0.6 : 1 }}>
                          {it.href ? <Link href={it.href} className="font-semibold hover:underline">{it.label}</Link> : <span className="font-semibold">{it.label}</span>}
                          <span className="block text-xs faint">{it.sub}</span>
                        </span>
                        <span className="text-xs faint shrink-0">{it.hours}h</span>
                      </li>
                    ))}
                  </ul>
                </li>
              );
            })}
          </ol>
        </>
      )}
    </div>
  );
}
