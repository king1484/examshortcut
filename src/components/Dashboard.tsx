'use client';
import { useEffect, useMemo, useState } from 'react';
import Link from 'next/link';
import { SECTION_META, SECTION_ORDER, type SectionId } from '@/lib/sections';
import { store, useStore, type MockAttempt, type SavedQ } from '@/lib/store';
import { CountdownChip } from './CountdownChip';

type TopicDoc = { t: string; title: string; url: string; section: string };
type TopicScore = { best: number; last: number; total: number; at: number };
type ToolState = {
  planDone: number | null; planTotal: number | null;
  dest: { kd: number; errPct: number; pass: boolean } | null;
  prefSaved: boolean;
};

const DAY = 86400000;
const istDay = (ts: number) => Math.floor((ts + 5.5 * 3600000) / DAY);

function Ring({ value, max, label, sub, color = 'var(--brand)' }: { value: number; max: number; label: string; sub: string; color?: string }) {
  const pct = max > 0 ? value / max : 0;
  const R = 26, C = 2 * Math.PI * R;
  return (
    <div className="card p-4 flex items-center gap-3">
      <svg width="64" height="64" viewBox="0 0 64 64" aria-hidden>
        <circle cx="32" cy="32" r={R} fill="none" stroke="var(--line)" strokeWidth="7" />
        <circle cx="32" cy="32" r={R} fill="none" stroke={color} strokeWidth="7" strokeLinecap="round"
          strokeDasharray={`${(pct * C).toFixed(1)} ${C.toFixed(1)}`} transform="rotate(-90 32 32)" />
        <text x="32" y="36" textAnchor="middle" fontSize="13" fontWeight="800" fill="var(--ink)">{max > 0 ? `${Math.round(pct * 100)}%` : '—'}</text>
      </svg>
      <div className="min-w-0">
        <div className="font-bold text-sm">{label}</div>
        <div className="text-xs faint mt-0.5">{sub}</div>
      </div>
    </div>
  );
}

function Sparkline({ pts }: { pts: Array<{ at: number; pct: number; label: string }> }) {
  if (pts.length < 2) return null;
  const W = 560, H = 130, P = 26;
  const x = (i: number) => P + (i * (W - 2 * P)) / (pts.length - 1);
  const y = (v: number) => H - P - (v * (H - 2 * P)) / 100;
  const path = pts.map((p, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)},${y(p.pct).toFixed(1)}`).join(' ');
  const avg = pts.reduce((s, p) => s + p.pct, 0) / pts.length;
  return (
    <svg viewBox={`0 0 ${W} ${H}`} className="w-full mt-2" role="img" aria-label="Score trend">
      <line x1={P} x2={W - P / 2} y1={y(avg)} y2={y(avg)} stroke="var(--line)" strokeDasharray="4 4" />
      <text x={W - P / 2} y={y(avg) - 4} fontSize="10" fill="var(--ink-3)" textAnchor="end">avg {Math.round(avg)}%</text>
      <path d={path} fill="none" stroke="var(--brand)" strokeWidth="2.5" strokeLinecap="round" />
      {pts.map((p, i) => (
        <g key={i}>
          <circle cx={x(i)} cy={y(p.pct)} r="4" fill={p.label.includes('Mock') ? 'var(--brand)' : 'var(--info)'} />
          {(i === pts.length - 1 || pts.length <= 8) && (
            <text x={x(i)} y={y(p.pct) - 9} fontSize="10" fontWeight="700" fill="var(--ink)" textAnchor="middle">{Math.round(p.pct)}</text>
          )}
        </g>
      ))}
    </svg>
  );
}

function accuracyColor(pct: number | null): { bg: string; fg: string } {
  if (pct === null) return { bg: 'var(--surface-2)', fg: 'var(--ink-3)' };
  if (pct >= 80) return { bg: 'var(--ok-soft)', fg: 'var(--ok)' };
  if (pct >= 50) return { bg: 'var(--warn-soft)', fg: 'var(--warn)' };
  return { bg: 'var(--bad-soft)', fg: 'var(--bad)' };
}

export function Dashboard() {
  const [catalog, setCatalog] = useState<TopicDoc[] | null>(null);
  const [tools, setTools] = useState<ToolState>({ planDone: null, planTotal: null, dest: null, prefSaved: false });
  const studied = useStore(store.studied, {});
  const topicScores = useStore(store.topicScores, {} as Record<string, TopicScore>);
  const attempts = useStore(store.attempts, {} as Record<string, MockAttempt[]>);
  const mistakes = useStore(store.mistakes, {} as Record<string, SavedQ>);
  const bookmarks = useStore(store.bookmarks, {} as Record<string, SavedQ>);

  useEffect(() => {
    fetch('/search-index.json')
      .then((r) => r.json())
      .then((d: TopicDoc[]) => setCatalog(d.filter((x) => x.t === 'topic')))
      .catch(() => setCatalog([]));
  }, []);

  useEffect(() => {
    try {
      const plan = JSON.parse(localStorage.getItem('es-study-plan') ?? 'null');
      if (plan?.done) setTools((t) => ({ ...t, planDone: Object.keys(plan.done).length, planTotal: plan.total ?? null }));
      const dest = JSON.parse(localStorage.getItem('es-dest-history') ?? '[]');
      if (Array.isArray(dest) && dest[0]) setTools((t) => ({ ...t, dest: { kd: dest[0].kd, errPct: dest[0].errPct, pass: dest[0].pass } }));
      const pref = JSON.parse(localStorage.getItem('es-post-planner') ?? 'null');
      if (pref?.dob) setTools((t) => ({ ...t, prefSaved: true }));
    } catch {}
  }, []);

  const model = useMemo(() => {
    const topics = catalog ?? [];
    const allAttempts = Object.entries(attempts).flatMap(([mockId, list]) => list.map((a) => ({ ...a, mockId })));
    const mockPct = (a: MockAttempt) => (a.max > 0 ? (a.score / a.max) * 100 : 0);
    const bestMock = allAttempts.reduce((b, a) => Math.max(b, mockPct(a)), 0);
    const testedKeys = Object.keys(topicScores);

    // Activity days → streak (any studied/score/attempt/mistake write counts)
    const stamps = [
      ...Object.values(studied), ...testedKeys.map((k) => topicScores[k].at),
      ...allAttempts.map((a) => a.at), ...Object.values(mistakes).map((m) => m.at),
    ].map(istDay);
    const activeDays = new Set(stamps);
    let streak = 0;
    for (let d = istDay(Date.now()); activeDays.has(d); d--) streak++;

    // Trend: mocks + last topic-test per topic, chronological
    const trend = [
      ...allAttempts.map((a) => ({ at: a.at, pct: mockPct(a), label: `Mock ${a.mockId}` })),
      ...testedKeys.map((k) => ({ at: topicScores[k].at, pct: (topicScores[k].last / Math.max(1, topicScores[k].total)) * 100, label: `Test ${k}` })),
    ].sort((a, b) => a.at - b.at).slice(-14);

    // Strength per section + weakest topics
    const perSection = SECTION_ORDER.map((sid) => {
      const list = topics.filter((t) => t.section === sid);
      const studiedCount = list.filter((t) => studied[`${sid}/${t.url.split('/').slice(-2, -1)[0]}`]).length;
      return { sid, total: list.length, studiedCount };
    });

    const strength = topics.map((t) => {
      const key = `${t.section}/${t.url.split('/').slice(-2, -1)[0]}`;
      const s = topicScores[key];
      return { ...t, key, pct: s ? Math.round((s.last / Math.max(1, s.total)) * 100) : null, best: s?.best ?? null };
    });
    const weakest = strength.filter((t) => t.pct !== null && t.pct < 75).sort((a, b) => (a.pct ?? 0) - (b.pct ?? 0)).slice(0, 3);

    const nextTopic = strength.find((t) => !studied[t.key] && t.pct === null);
    const mockCount = allAttempts.length;
    const lastMockAt = allAttempts.reduce((m, a) => Math.max(m, a.at), 0);
    const mistakeCount = Object.keys(mistakes).length;

    const plan: Array<{ icon: string; title: string; body: string; href: string; cta: string }> = [];
    if (mockCount === 0) plan.push({ icon: '🖥️', title: 'Take your first full mock', body: 'The single best calibration: 100 questions, 60 minutes, real interface.', href: '/ssc-cgl/mocks/', cta: 'Start mock' });
    else if (Date.now() - lastMockAt > 2 * DAY) plan.push({ icon: '🖥️', title: 'Mock day', body: 'Your last mock was over 48h ago. In the final week, alternate mocks and revision days.', href: '/ssc-cgl/mocks/', cta: 'Take a mock' });
    if (mistakeCount >= 5) plan.push({ icon: '📕', title: `Clear ${mistakeCount} mistakes`, body: 'Re-solve your logged mistakes — the cheapest marks you will ever earn.', href: '/revision/', cta: 'Open notebook' });
    if (nextTopic) plan.push({ icon: '📚', title: `Study: ${nextTopic.title}`, body: `Next untouched topic in ${SECTION_META[nextTopic.section as SectionId]?.name}. Notes → formulas → tricks, then a 12-question test.`, href: nextTopic.url, cta: 'Start topic' });
    plan.push({ icon: '📰', title: 'Daily current affairs', body: '10 minutes of GA every day beats 2 hours the night before.', href: '/ssc-cgl/ga/current-affairs/', cta: 'Read today' });

    const activity = [
      ...allAttempts.map((a) => ({ at: a.at, icon: '🖥️', title: `Mock — ${a.score}/${a.max}`, sub: `${a.correct}✓ ${a.wrong}✗ ${a.skipped}— · ${Math.round(a.timeSec / 60)} min`, href: '/ssc-cgl/mocks/', pct: mockPct(a) })),
      ...testedKeys.map((k) => ({ at: topicScores[k].at, icon: '📝', title: `Topic test — ${k.split('/')[1].replace(/-/g, ' ')}`, sub: `last ${topicScores[k].last}/${topicScores[k].total} · best ${topicScores[k].best}/${topicScores[k].total}`, href: `/ssc-cgl/${k}/`, pct: Math.round((topicScores[k].last / Math.max(1, topicScores[k].total)) * 100) })),
    ].sort((a, b) => b.at - a.at).slice(0, 6);

    return { topics, testedKeys, bestMock, streak, trend, perSection, strength, weakest, nextTopic, mockCount, mistakeCount, plan, activity, bookmarkCount: Object.keys(bookmarks).length };
  }, [catalog, studied, topicScores, attempts, mistakes, bookmarks]);

  const isEmpty = model.testedKeys.length === 0 && model.mockCount === 0 && Object.keys(studied).length === 0;

  return (
    <div>
      <div className="flex items-center justify-between flex-wrap gap-2">
        <div>
          <h1 className="text-3xl font-extrabold">Your dashboard</h1>
          <p className="muted text-sm mt-1">Everything you've done on this device, and what to do next.</p>
        </div>
        <CountdownChip date="2026-09-30" />
      </div>

      {isEmpty && catalog !== null && (
        <div className="card p-6 mt-5 text-center">
          <div className="text-3xl">🚀</div>
          <h2 className="font-extrabold text-lg mt-1">Three steps to get going</h2>
          <div className="grid sm:grid-cols-3 gap-3 mt-4 text-sm">
            {[
              ['1', 'Study a topic', 'Notes → formulas → shortcut tricks', '/ssc-cgl/syllabus/', 'Browse syllabus'],
              ['2', 'Pass its topic test', '12–15 questions, instant explanations', '/ssc-cgl/syllabus/', 'Pick a topic'],
              ['3', 'Take a full mock', 'Real CBT interface + analysis', '/ssc-cgl/mocks/', 'Start a mock'],
            ].map(([n, t, b, href, cta]) => (
              <div key={n} className="rounded-xl p-4" style={{ background: 'var(--surface-2)' }}>
                <div className="w-7 h-7 mx-auto rounded-full font-extrabold flex items-center justify-center" style={{ background: 'var(--brand)', color: '#fff' }}>{n}</div>
                <div className="font-bold mt-2">{t}</div>
                <div className="faint text-xs mt-1">{b}</div>
                <Link className="btn text-xs mt-3 self-start" href={href} style={{ padding: '.3rem .7rem' }}>{cta}</Link>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mt-5">
        <Ring value={Object.keys(studied).length} max={model.topics.length} label="Syllabus studied" sub={`${Object.keys(studied).length} of ${model.topics.length || '…'} topics`} />
        <Ring value={model.testedKeys.length} max={model.topics.length} label="Topics tested" sub={`${model.testedKeys.length} topic tests passed`} color="var(--info)" />
        <Ring value={model.bestMock} max={100} label="Best mock score" sub={`${model.mockCount} mock${model.mockCount === 1 ? '' : 's'} attempted`} color="var(--ok)" />
        <div className="card p-4 flex items-center gap-3">
          <div className="text-3xl">🔥</div>
          <div>
            <div className="text-2xl font-extrabold leading-none">{model.streak}</div>
            <div className="text-xs faint mt-1">day streak{model.streak > 0 ? ' — keep it alive' : ' — study something today'}</div>
            <div className="text-xs faint mt-0.5">📕 {model.mistakeCount} mistakes · 🔖 {model.bookmarkCount} bookmarks</div>
          </div>
        </div>
      </div>

      {model.perSection.some((s) => s.total > 0) && (
        <section className="mt-6">
          <h2 className="font-extrabold text-lg">Section progress</h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-5 gap-3 mt-3">
            {model.perSection.filter((s) => s.total > 0).map((s) => {
              const pct = s.total ? Math.round((s.studiedCount / s.total) * 100) : 0;
              return (
                <Link key={s.sid} href={`/ssc-cgl/${s.sid}/`} className="card p-4 block">
                  <div className="text-xs font-bold" style={{ color: SECTION_META[s.sid].color }}>{SECTION_META[s.sid].name}</div>
                  <div className="text-xl font-extrabold mt-1">{s.studiedCount}<span className="text-sm faint">/{s.total}</span></div>
                  <div className="h-2 rounded-full mt-2" style={{ background: 'var(--surface-2)' }}>
                    <div className="h-2 rounded-full" style={{ width: `${pct}%`, background: SECTION_META[s.sid].color }} />
                  </div>
                </Link>
              );
            })}
          </div>
        </section>
      )}

      <section className="mt-6">
        <h2 className="font-extrabold text-lg">Your tools</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mt-3">
          <Link href="/ssc-cgl/study-plan/" className="card p-4">
            <div className="font-bold text-sm">🗓️ Study plan</div>
            <div className="text-xs muted mt-1">{tools.planDone !== null ? `${tools.planDone} step${tools.planDone === 1 ? '' : 's'} ticked off${tools.planTotal ? ` · ${tools.planTotal} planned` : ''}` : 'Build a day-by-day timetable to exam day'}</div>
          </Link>
          <Link href="/ssc-cgl/typing-test/" className="card p-4">
            <div className="font-bold text-sm">⌨️ DEST typing test</div>
            <div className="text-xs muted mt-1">{tools.dest ? `Last: ${tools.dest.kd} KD · ${tools.dest.errPct}% errors ${tools.dest.pass ? '✓' : '✗'}` : '15-min simulator with SSC error marking'}</div>
          </Link>
          <Link href="/ssc-cgl/posts/" className="card p-4">
            <div className="font-bold text-sm">🏛️ Posts &amp; eligibility</div>
            <div className="text-xs muted mt-1">{tools.prefSaved ? 'Preference order saved on this device ✓' : 'Age checker + build your post preference'}</div>
          </Link>
          <Link href="/ssc-cgl/calendar/" className="card p-4">
            <div className="font-bold text-sm">⏳ Exam calendar</div>
            <div className="text-xs muted mt-1">Every 2026 date, add to your phone calendar</div>
          </Link>
        </div>
      </section>

      <div className="grid lg:grid-cols-2 gap-4 mt-6">
        {model.trend.length >= 2 && (
          <section className="card p-4">
            <h2 className="font-extrabold text-lg">Score trend</h2>
            <p className="text-xs faint">Last {model.trend.length} tests · orange = full mocks, blue = topic tests</p>
            <Sparkline pts={model.trend} />
          </section>
        )}

        {model.weakest.length > 0 && (
          <section className="card p-4">
            <h2 className="font-extrabold text-lg">Fix these first</h2>
            <p className="text-xs faint">Lowest last-test accuracy — retake after revising the notes.</p>
            <div className="mt-3 space-y-2">
              {model.weakest.map((t) => {
                const c = accuracyColor(t.pct);
                return (
                  <Link key={t.key} href={t.url} className="flex items-center gap-3 rounded-xl px-3 py-2.5" style={{ background: c.bg }}>
                    <span className="font-bold text-sm w-10 text-center rounded-lg py-0.5" style={{ color: c.fg }}>{t.pct}%</span>
                    <span className="text-sm font-semibold flex-1 min-w-0 truncate">{t.title}</span>
                    <span className="text-xs faint">{SECTION_META[t.section as SectionId]?.short}</span>
                  </Link>
                );
              })}
            </div>
          </section>
        )}
      </div>

      {catalog !== null && model.strength.some((t) => t.pct !== null) && (
        <section className="mt-6">
          <h2 className="font-extrabold text-lg">Strength map</h2>
          <p className="text-xs faint">Green ≥ 80% · amber 50–79% · red &lt; 50% · grey = not tested yet</p>
          {SECTION_ORDER.map((sid) => {
            const rows = model.strength.filter((t) => t.section === sid);
            if (!rows.length) return null;
            return (
              <div key={sid} className="mt-3">
                <div className="text-xs font-bold uppercase" style={{ color: SECTION_META[sid].color }}>{SECTION_META[sid].short}</div>
                <div className="flex flex-wrap gap-1.5 mt-1.5">
                  {rows.map((t) => {
                    const c = accuracyColor(t.pct);
                    return (
                      <Link key={t.key} href={t.url} className="chip" style={{ background: c.bg, color: c.fg, borderColor: 'transparent' }} title={t.pct === null ? 'Not tested' : `Last: ${t.pct}% · best: ${t.best}%`}>
                        {t.title}{t.pct !== null ? ` ${t.pct}%` : ''}
                      </Link>
                    );
                  })}
                </div>
              </div>
            );
          })}
        </section>
      )}

      {model.plan.length > 0 && (
        <section className="mt-6">
          <h2 className="font-extrabold text-lg">Today's plan</h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mt-3">
            {model.plan.slice(0, 4).map((p) => (
              <div key={p.title} className="card p-4 flex flex-col">
                <div className="text-2xl">{p.icon}</div>
                <div className="font-bold text-sm mt-1">{p.title}</div>
                <p className="text-xs muted mt-1 flex-1">{p.body}</p>
                <Link className="btn btn-brand text-xs mt-3 self-start" href={p.href} style={{ padding: '.35rem .8rem' }}>{p.cta}</Link>
              </div>
            ))}
          </div>
        </section>
      )}

      {model.activity.length > 0 && (
        <section className="card p-4 mt-6">
          <h2 className="font-extrabold text-lg">Recent activity</h2>
          <div className="mt-2">
            {model.activity.map((a, i) => {
              const days = Math.floor((Date.now() - a.at) / DAY);
              const when = days === 0 ? 'today' : days === 1 ? 'yesterday' : `${days}d ago`;
              return (
                <Link key={i} href={a.href} className="flex items-center gap-3 py-2.5 border-b last:border-0 text-sm" style={{ borderColor: 'var(--line)' }}>
                  <span>{a.icon}</span>
                  <span className="flex-1 min-w-0">
                    <span className="font-semibold block truncate">{a.title}</span>
                    <span className="text-xs faint">{a.sub}</span>
                  </span>
                  <span className="chip text-[10px]">{when}</span>
                </Link>
              );
            })}
          </div>
        </section>
      )}

      <p className="text-[11px] faint mt-6">All progress lives in this browser (localStorage) — private by design, no account needed. Don't clear site data, or your notebook and scores reset.</p>
    </div>
  );
}
