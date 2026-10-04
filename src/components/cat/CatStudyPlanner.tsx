'use client';
import Link from 'next/link';
import { useEffect, useMemo, useState } from 'react';
import { CAT_SECS, CONCEPT_ROTATION, type CatSecId } from '@/lib/catSyllabus';

export interface CatEvent { id: string; title: string; start: string; status?: string }

type Level = 'weak' | 'avg' | 'strong';
type PhaseId = 'concepts' | 'sectional' | 'mocks' | 'final';
type Cfg = { hours: number; levels: Record<string, Level>; date?: string };

const KEY = 'es-cat-study-plan';
const LVL_W: Record<Level, number> = { weak: 1.4, avg: 1, strong: 0.6 };
const PHASES: Record<PhaseId, { label: string; blurb: string; color: string }> = {
  concepts: { label: 'Concepts', blurb: 'Build and fix the fundamentals topic by topic.', color: 'var(--c-english)' },
  sectional: { label: 'Sectional practice', blurb: 'Timed 40-minute sectionals, one section at a time.', color: 'var(--c-reasoning)' },
  mocks: { label: 'Full mocks', blurb: 'Full 120-minute papers in the real section order.', color: 'var(--brand)' },
  final: { label: 'Analysis & final revision', blurb: 'No new topics. Consolidate, analyse, rest.', color: 'var(--ok)' },
};
const ORDER: PhaseId[] = ['concepts', 'sectional', 'mocks', 'final'];

const iso = (d: Date) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
const parse = (s: string) => new Date(`${s}T00:00:00`);
const addDays = (d: Date, n: number) => { const x = new Date(d); x.setDate(x.getDate() + n); return x; };
const fmt = (d: Date) => d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short' });

/** Weeks-left -> how many of the remaining weeks go to each phase. Illustrative heuristic, not an official schedule. */
function allocate(W: number): Record<PhaseId, number> {
  const f: [number, number, number, number] = W >= 16 ? [0.4, 0.25, 0.25, 0.1] : W >= 8 ? [0.25, 0.25, 0.35, 0.15] : W >= 4 ? [0.15, 0.25, 0.45, 0.15] : [0, 0.2, 0.55, 0.25];
  let rem = W;
  const take = (n: number) => { const v = Math.max(0, Math.min(rem, n)); rem -= v; return v; };
  const final = take(Math.max(1, Math.round(W * f[3])));
  const mocks = take(Math.round(W * f[2]));
  const sectional = take(Math.round(W * f[1]));
  const left = rem;
  return f[0] > 0 ? { concepts: left, sectional, mocks, final } : { concepts: 0, sectional, mocks: mocks + left, final };
}

interface Week { n: number; start: Date; end: Date; days: number; phase: PhaseId; idxInPhase: number; tasks: string[]; key: string }

function build(exam: Date, today: Date, hours: number, levels: Record<string, Level>) {
  const days = Math.round((exam.getTime() - today.getTime()) / 86400000);
  if (days <= 0) return { days, weeks: [] as Week[], alloc: null as Record<PhaseId, number> | null, split: [] as { id: CatSecId; h: number }[] };
  const W = Math.ceil(days / 7);
  const alloc = allocate(W);
  const seq: PhaseId[] = ORDER.flatMap((p) => Array<PhaseId>(alloc[p]).fill(p));
  const seen: Record<string, number> = {};
  const wt = CAT_SECS.map((s) => LVL_W[levels[s.id] ?? 'avg']);
  const wsum = wt.reduce((a, b) => a + b, 0);
  const weeks: Week[] = seq.map((phase, i) => {
    const start = addDays(today, 7 * i);
    const end = addDays(exam, -1) < addDays(start, 6) ? addDays(exam, -1) : addDays(start, 6);
    const nDays = Math.round((end.getTime() - start.getTime()) / 86400000) + 1;
    const j = (seen[phase] = (seen[phase] ?? -1) + 1);
    const n = W - i; // weeks to exam, counting this one
    const wh = (id: CatSecId) => { const k = CAT_SECS.findIndex((s) => s.id === id); return Math.round((hours * nDays * wt[k]) / wsum * 2) / 2; };
    let tasks: string[] = [];
    if (phase === 'concepts') {
      tasks = [
        `QA: ${CONCEPT_ROTATION.qa[j % CONCEPT_ROTATION.qa.length]}. Learn the method, then solve problems on it.`,
        `DILR: ${CONCEPT_ROTATION.dilr[j % CONCEPT_ROTATION.dilr.length]}. Solve sets untimed first, then timed.`,
        `VARC: ${CONCEPT_ROTATION.varc[j % CONCEPT_ROTATION.varc.length]}, with daily reading and 1–2 passages a day.`,
        `Keep a mistake notebook: every wrong or skipped question gets a line on why.`,
        ...(W < 8 ? ['Short on time: treat this as a fast gap-fill on your weakest topics rather than a full first pass.'] : []),
      ];
    } else if (phase === 'sectional') {
      tasks = [
        'Take 3–4 timed 40-minute sectionals this week, rotating VARC, DILR and QA (more of your weaker ones).',
        'DILR: practise scanning all sets first and choosing which to attempt.',
        'Practise TITA: they carry no negative marking, so always type an answer.',
        'Review each sectional the same day and log errors by topic.',
      ];
    } else if (phase === 'mocks') {
      tasks = [
        'Take 2–3 full 120-minute mocks in the real order (VARC → DILR → QA, 40 minutes locked per section).',
        'Analyse each mock before the next one. Budget about as long for analysis as for the mock itself.',
        'Track attempts, accuracy and sectional score per mock; work on the section dragging you down.',
        'Between mocks, do short topic drills only for the errors the analysis found.',
      ];
    } else {
      tasks = n <= 1
        ? ['Last week: no new topics. Light revision from your mistake notebook and formula sheet.', 'Do at most one light mock or sectional early in the week, then rest.', 'Check admit card, exam city, slot and travel plan; fix your sleep schedule to the slot time.']
        : ['No new topics. Revise formulas, RC technique and DILR set-selection from your mistake notebook.', 'One full mock every 2–3 days, each with analysis.', 'Check iimcat.ac.in for the admit card and your slot as soon as they are out.'];
    }
    return { n, start, end, days: nDays, phase, idxInPhase: j, tasks, key: `T-${n}` };
  });
  const split = CAT_SECS.map((s, k) => ({ id: s.id, h: Math.round((hours * 7 * wt[k]) / wsum * 2) / 2 }));
  return { days, weeks, alloc, split };
}

export function CatStudyPlanner({ examDate, events }: { examDate: string; events: CatEvent[] }) {
  const [cfg, setCfg] = useState<Cfg>({ hours: 4, levels: {} });
  const [done, setDone] = useState<Record<string, boolean>>({});
  const [today, setToday] = useState<Date | null>(null);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    try {
      const s = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (s?.cfg) setCfg((c) => ({ ...c, ...s.cfg }));
      if (s?.done) setDone(s.done);
    } catch { /* storage unavailable: plan still works, just not saved */ }
    const n = new Date();
    setToday(new Date(n.getFullYear(), n.getMonth(), n.getDate()));
    setLoaded(true);
  }, []);
  useEffect(() => {
    if (!loaded) return;
    try { localStorage.setItem(KEY, JSON.stringify({ cfg, done })); } catch { /* ignore */ }
  }, [cfg, done, loaded]);

  const dateStr = cfg.date || examDate;
  const exam = useMemo(() => parse(dateStr), [dateStr]);
  const valid = !Number.isNaN(exam.getTime());
  const plan = useMemo(() => (today && valid ? build(exam, today, cfg.hours, cfg.levels) : null), [today, valid, exam, cfg.hours, cfg.levels]);
  const set = <K extends keyof Cfg>(k: K, v: Cfg[K]) => setCfg((c) => ({ ...c, [k]: v }));
  const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };
  const tickKey = (w: Week, i: number) => `${w.key}/${w.phase}/${i}`;

  const allKeys = plan?.weeks.flatMap((w) => w.tasks.map((_, i) => tickKey(w, i))) ?? [];
  const doneCount = allKeys.filter((k) => done[k]).length;

  return (
    <div>
      <div className="card p-5">
        <div className="grid sm:grid-cols-2 gap-3 text-sm">
          <label className="font-semibold">Exam date
            <input type="date" value={dateStr} onChange={(e) => set('date', e.target.value || undefined)} className="w-full mt-1 p-2 rounded-lg border" style={input} />
            <span className="block text-xs faint font-normal mt-1">
              {dateStr === examDate ? 'CAT 2026 date from the official schedule.' : 'Custom date.'}{' '}
              {cfg.date && cfg.date !== examDate && <button className="underline" onClick={() => set('date', undefined)}>Reset to {examDate}</button>}
            </span>
          </label>
          <label className="font-semibold">Study hours per day: {cfg.hours}
            <input type="range" min={1} max={10} step={0.5} value={cfg.hours} onChange={(e) => set('hours', Number(e.target.value))} className="w-full mt-3" />
          </label>
        </div>
        <div className="mt-4 text-sm">
          <div className="font-semibold">How strong are you in each section?</div>
          <div className="grid sm:grid-cols-3 gap-2 mt-2">
            {CAT_SECS.map((s) => (
              <div key={s.id} className="flex items-center gap-2 rounded-lg p-2" style={{ background: 'var(--surface-2)' }}>
                <span className="font-bold w-12" style={{ color: s.color }}>{s.short}</span>
                {(['weak', 'avg', 'strong'] as Level[]).map((l) => (
                  <button key={l} className="btn text-xs flex-1" style={{ padding: '.25rem .3rem', ...((cfg.levels[s.id] ?? 'avg') === l ? { background: 'var(--brand)', color: 'var(--brand-ink)', borderColor: 'var(--brand)' } : {}) }}
                    onClick={() => set('levels', { ...cfg.levels, [s.id]: l })}>{l === 'avg' ? 'avg' : l}</button>
                ))}
              </div>
            ))}
          </div>
        </div>
      </div>

      {!plan ? <p className="card p-6 mt-5 text-center muted">{valid ? 'Building your plan…' : 'Pick a valid exam date above.'}</p> :
        plan.days <= 0 ? (
          <p className="card p-6 mt-5 text-center muted">
            {plan.days === 0
              ? 'The exam is today. Trust your preparation, and good luck.'
              : <>That exam date has passed. Pick a future date above, or see <Link href="/exams/cat/cutoffs/" className="underline">what comes next: shortlists and cut-offs</Link>.</>}
          </p>
        ) : (
          <>
            <div className="card p-5 mt-5">
              <div className="grid grid-cols-3 gap-3 text-center">
                <div><div className="text-3xl font-extrabold">{plan.days}</div><div className="text-xs faint font-semibold uppercase">Days left</div></div>
                <div><div className="text-3xl font-extrabold">{plan.weeks.length}</div><div className="text-xs faint font-semibold uppercase">Weeks left</div></div>
                <div><div className="text-3xl font-extrabold">{Math.round(plan.days * cfg.hours)}</div><div className="text-xs faint font-semibold uppercase">Study hours</div></div>
              </div>
              <div className="flex flex-wrap gap-2 mt-4">
                {ORDER.filter((p) => plan.alloc![p] > 0).map((p) => (
                  <span key={p} className="chip" style={{ borderColor: PHASES[p].color }}><span className="w-2 h-2 rounded-full" style={{ background: PHASES[p].color }} />{PHASES[p].label}: {plan.alloc![p]} wk</span>
                ))}
              </div>
              <p className="text-xs faint mt-3">
                Weekly time split at {cfg.hours} h/day: {plan.split.map((s) => `${CAT_SECS.find((c) => c.id === s.id)!.short} ${s.h} h`).join(' · ')}. Weaker sections get more.
              </p>
              <div className="h-2 rounded-full overflow-hidden mt-3" style={{ background: 'var(--surface-2)' }}>
                <div className="h-full" style={{ width: `${(100 * doneCount) / Math.max(1, allKeys.length)}%`, background: 'var(--ok)' }} />
              </div>
              <div className="flex items-center justify-between mt-2 text-xs faint">
                <span>{doneCount}/{allKeys.length} tasks ticked. Saved only in this browser.</span>
                {doneCount > 0 && <button className="underline" onClick={() => setDone({})}>Clear ticks</button>}
              </div>
            </div>

            <p className="text-xs faint mt-3">
              How the weeks are split between phases is an illustrative heuristic based on how many weeks you have left. It is not an official or proven schedule. Adjust it to your mock results.
            </p>

            <ol className="mt-4 space-y-3">
              {plan.weeks.map((w, wi) => {
                const evs = events.filter((e) => e.start >= iso(w.start) && e.start <= iso(wi === plan.weeks.length - 1 ? exam : w.end));
                const ph = PHASES[w.phase];
                const isNow = wi === 0;
                return (
                  <li key={`${w.key}-${w.phase}`} className="card p-4" style={isNow ? { borderColor: 'var(--brand)', borderWidth: 2 } : undefined}>
                    <div className="flex items-center gap-2 flex-wrap text-sm">
                      <span className="font-extrabold">Week {wi + 1}</span>
                      <span className="faint">{fmt(w.start)} – {fmt(w.end)}</span>
                      <span className="chip" style={{ color: ph.color, borderColor: ph.color }}>{ph.label}</span>
                      {isNow && <span className="chip chip-high text-[10px]">this week</span>}
                      <span className="ml-auto text-xs faint">{w.n} wk to exam</span>
                    </div>
                    {evs.length > 0 && (
                      <ul className="mt-2 space-y-1">
                        {evs.map((e) => (
                          <li key={e.id} className="text-xs rounded-md px-2 py-1" style={{ background: 'var(--brand-soft)', color: 'var(--brand-text)' }}>
                            {new Date(`${e.start}T00:00:00`).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' })}: {e.title}{e.status === 'expected' ? ' (expected)' : ''}
                          </li>
                        ))}
                      </ul>
                    )}
                    <ul className="mt-2 space-y-1.5">
                      {w.tasks.map((t, i) => {
                        const k = tickKey(w, i);
                        return (
                          <li key={i} className="flex items-start gap-2.5 text-sm">
                            <input type="checkbox" className="mt-1 w-4 h-4 shrink-0" checked={!!done[k]} aria-label={`Mark done: ${t}`}
                              onChange={() => setDone((d) => { const n = { ...d }; if (n[k]) delete n[k]; else n[k] = true; return n; })} />
                            <span className="flex-1 min-w-0" style={{ textDecoration: done[k] ? 'line-through' : undefined, opacity: done[k] ? 0.6 : 1 }}>{t}</span>
                          </li>
                        );
                      })}
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
