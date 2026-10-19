'use client';
import { useEffect, useMemo, useRef, useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useAuth } from './Auth';
import type { Mock, Question } from '@/lib/types';
import { store, type MockAttempt } from '@/lib/store';
import { ShareScore } from './ShareScore';
import { Explanation, LETTERS, OptionButton, QuestionBody, withPassages } from './QuestionView';
import { questionScore, wrongAnswerPenalty } from '@/lib/questionScore';

// SSC-style palette states
type Status = 'not-visited' | 'not-answered' | 'answered' | 'marked' | 'answered-marked';
interface Flat { q: Question; s: number; n: number } // s = section index, n = number within section
interface Draft { answers: (number | null)[]; status: Status[]; times: number[]; remaining: number; cur: number; started: number }

const STATUS_STYLE: Record<Status, React.CSSProperties> = {
  'not-visited': { background: 'var(--surface-2)', color: 'var(--ink-2)', border: '1px solid var(--line)' },
  'not-answered': { background: 'var(--bad)', color: '#fff' },
  answered: { background: 'var(--ok)', color: '#fff' },
  marked: { background: '#7048e8', color: '#fff', borderRadius: '999px' },
  'answered-marked': { background: '#7048e8', color: '#fff', borderRadius: '999px', boxShadow: 'inset 0 -4px 0 var(--ok)' },
};

const fmt = (sec: number) => {
  const h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60), s = sec % 60;
  return `${h ? `${h}:` : ''}${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
};

export function MockCBT({ mock }: { mock: Mock }) {
  const flat: Flat[] = useMemo(
    () => mock.sections.flatMap((sec, s) => withPassages(sec.questions).map((q, n) => ({ q, s, n }))),
    [mock],
  );
  const total = flat.length;
  const [phase, setPhase] = useState<'intro' | 'test' | 'result'>('intro');
  const [st, setSt] = useState<Draft>(() => ({
    answers: Array(total).fill(null), status: Array(total).fill('not-visited'), times: Array(total).fill(0),
    remaining: mock.durationMin * 60, cur: 0, started: 0,
  }));
  const [pending, setPending] = useState<number | null>(null); // selected but not yet "Save & Next"
  const [hasDraft, setHasDraft] = useState(false);
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [confirmSubmit, setConfirmSubmit] = useState(false);
  const stRef = useRef(st); stRef.current = st;

  useEffect(() => { setHasDraft(!!store.draft<Draft>(mock.id)); }, [mock.id]);

  // timer
  useEffect(() => {
    if (phase !== 'test') return;
    const t = window.setInterval(() => {
      setSt((p) => {
        const times = [...p.times]; times[p.cur] += 1;
        const next = { ...p, times, remaining: p.remaining - 1 };
        if (next.remaining % 5 === 0) store.saveDraft(mock.id, next);
        return next;
      });
    }, 1000);
    return () => window.clearInterval(t);
  }, [phase, mock.id]);

  useEffect(() => { if (phase === 'test' && st.remaining <= 0) submit(); /* eslint-disable-next-line react-hooks/exhaustive-deps */ }, [st.remaining, phase]);

  // warn before leaving mid-test
  useEffect(() => {
    if (phase !== 'test') return;
    const h = (e: BeforeUnloadEvent) => { store.saveDraft(mock.id, stRef.current); e.preventDefault(); };
    window.addEventListener('beforeunload', h);
    return () => window.removeEventListener('beforeunload', h);
  }, [phase, mock.id]);

  function start(resume: boolean) {
    const d = resume ? store.draft<Draft>(mock.id) : null;
    const base = d && d.answers.length === total ? d : { ...st, started: Date.now() };
    const status = [...base.status]; if (status[base.cur] === 'not-visited') status[base.cur] = 'not-answered';
    setSt({ ...base, status });
    setPending(base.answers[base.cur]);
    setPhase('test');
    window.scrollTo(0, 0);
  }

  function go(i: number) {
    setSt((p) => {
      const status = [...p.status];
      if (status[i] === 'not-visited') status[i] = 'not-answered';
      return { ...p, cur: i, status };
    });
    setPending(st.answers[i]);
    setPaletteOpen(false);
  }

  function commit(mark: boolean) {
    setSt((p) => {
      const answers = [...p.answers]; const status = [...p.status];
      answers[p.cur] = pending;
      status[p.cur] = pending !== null ? (mark ? 'answered-marked' : 'answered') : mark ? 'marked' : 'not-answered';
      const next = { ...p, answers, status };
      store.saveDraft(mock.id, next);
      return next;
    });
    if (st.cur < total - 1) {
      const i = st.cur + 1;
      setSt((p) => { const status = [...p.status]; if (status[i] === 'not-visited') status[i] = 'not-answered'; return { ...p, cur: i, status }; });
      setPending(st.answers[i]);
    }
  }

  function clear() {
    setPending(null);
    setSt((p) => { const answers = [...p.answers]; const status = [...p.status]; answers[p.cur] = null; status[p.cur] = 'not-answered'; return { ...p, answers, status }; });
  }

  function submit() {
    // fold the current question's un-saved selection into the answers, as the real CBT does on submit
    const answers = [...stRef.current.answers];
    if (pending !== null) answers[st.cur] = pending;
    setPhase('result');
    setConfirmSubmit(false);
    const res = score(answers);
    store.saveAttempt(mock.id, res);
    store.clearDraft(mock.id);
    flat.forEach((f, i) => {
      const a = answers[i];
      if (a !== null && a !== f.q.answer)
        store.addMistake({ key: `mock/${mock.id}/${f.q.id}`, question: f.q, chosen: a, from: mock.title, href: `/exams/${mock.exam ?? 'ssc-cgl'}/mocks/${mock.id}/`, section: mock.sections[f.s].sectionId, at: Date.now() });
    });
    setSt((p) => ({ ...p, answers }));
    window.scrollTo(0, 0);
  }

  function score(answers: (number | null)[]): MockAttempt {
    const sections: MockAttempt['sections'] = {};
    let correct = 0, wrong = 0;
    flat.forEach((f, i) => {
      const sid = mock.sections[f.s].sectionId;
      const s = (sections[sid] ??= { score: 0, max: 0, correct: 0, wrong: 0, total: 0 });
      s.total++; s.max += mock.plus;
      const a = answers[i];
      if (a === null) return;
      s.score += questionScore(f.q, a, mock.plus, mock.minus);
      if (a === f.q.answer) { s.correct++; correct++; } else { s.wrong++; wrong++; }
    });
    const scoreVal = Object.values(sections).reduce((n, s) => n + s.score, 0);
    const meritSections = Object.entries(sections).filter(([sid]) => !(mock.tier === 2 && sid === 'computer'));
    const meritScoreVal = meritSections.reduce((n, [, s]) => n + s.score, 0);
    const meritMax = meritSections.reduce((n, [, s]) => n + s.max, 0);
    const meritCorrect = meritSections.reduce((n, [, s]) => n + s.correct, 0);
    const meritWrong = meritSections.reduce((n, [, s]) => n + s.wrong, 0);
    const meritTotal = meritSections.reduce((n, [, s]) => n + s.total, 0);
    const timeSec = mock.durationMin * 60 - Math.max(0, stRef.current.remaining);
    return {
      at: Date.now(),
      score: mock.tier === 2 ? meritScoreVal : scoreVal,
      max: mock.tier === 2 ? meritMax : total * mock.plus,
      correct: mock.tier === 2 ? meritCorrect : correct,
      wrong: mock.tier === 2 ? meritWrong : wrong,
      skipped: mock.tier === 2 ? meritTotal - meritCorrect - meritWrong : total - correct - wrong,
      timeSec,
      sections,
    };
  }

  // ---------------- INTRO ----------------
  if (phase === 'intro') {
    return (
      <div className="max-w-3xl mx-auto">
        <Link href={`/exams/${mock.exam ?? "ssc-cgl"}/mocks/`} className="text-sm faint">← All mock tests</Link>
        <h1 className="text-2xl sm:text-3xl font-extrabold mt-2">{mock.title}</h1>
        <p className="muted mt-2">{mock.blurb}</p>
        <div className="tbl-wrap mt-5">
          <table className="tbl">
            <thead><tr><th>Section</th><th>Questions</th><th>Marks</th></tr></thead>
            <tbody>
              {mock.sections.map((s) => (
                <tr key={s.sectionId}><td>{s.name}</td><td>{s.questions.length}</td><td>{s.questions.length * mock.plus}</td></tr>
              ))}
              <tr><td className="font-bold">Total</td><td className="font-bold">{total}</td><td className="font-bold">{total * mock.plus}</td></tr>
            </tbody>
          </table>
        </div>
        <div className="card p-5 mt-5 text-sm space-y-2">
          <h2 className="font-bold text-base">Instructions (same as the real CBT)</h2>
          <ul className="list-disc pl-5 space-y-1 muted">
            <li>Total time: <b>{mock.durationMin} minutes</b>. The clock at the top counts down; the test submits automatically at 00:00.</li>
            <li>+{mock.plus} for every correct answer. {flat.some((f) => f.q.negativeMarks !== undefined) ? 'Wrong-answer penalties depend on the session and are shown with each question.' : `−${mock.minus} for every wrong MCQ answer.`} No marks deducted for unattempted questions.</li>
            {flat.some((f) => f.q.type === 'numeric') && <li>For TITA questions, type the numerical answer. Wrong TITA answers carry no negative marks.</li>}
            <li>Click an option, then <b>Save &amp; Next</b>. An option clicked without saving is not counted — just like the real exam.</li>
            <li><b>Mark for Review &amp; Next</b> flags a question. A marked question that has an answer <i>is</i> evaluated.</li>
            <li>You can jump between sections and questions using the palette. Your progress is saved on this device if you close the tab.</li>
          </ul>
          <div className="flex flex-wrap gap-3 pt-2 text-xs">
            {(['not-visited', 'not-answered', 'answered', 'marked', 'answered-marked'] as Status[]).map((k) => (
              <span key={k} className="flex items-center gap-1.5"><span className="w-6 h-6 rounded-md grid place-items-center" style={STATUS_STYLE[k]}>1</span>{k.replace('-', ' ')}</span>
            ))}
          </div>
        </div>
        <div className="flex gap-3 mt-6 flex-wrap">
          <button className="btn btn-brand" onClick={() => start(false)}>{hasDraft ? 'Start fresh' : 'I am ready — start test'}</button>
          {hasDraft && <button className="btn" onClick={() => start(true)}>Resume saved attempt</button>}
        </div>
      </div>
    );
  }

  // ---------------- RESULT ----------------
  if (phase === 'result') return <MockResult mock={mock} flat={flat} answers={st.answers} times={st.times} attempt={score(st.answers)} />;

  // ---------------- TEST ----------------
  const cur = flat[st.cur];
  const counts = st.status.reduce((m, s) => { m[s] = (m[s] ?? 0) + 1; return m; }, {} as Record<Status, number>);
  const lowTime = st.remaining <= 300;

  const palette = (
    <div className="flex flex-col h-full">
      <div className="grid grid-cols-2 gap-2 text-xs p-3 border-b" style={{ borderColor: 'var(--line)' }}>
        {(['answered', 'not-answered', 'not-visited', 'marked', 'answered-marked'] as Status[]).map((k) => (
          <span key={k} className="flex items-center gap-1.5"><span className="w-6 h-6 rounded-md grid place-items-center font-bold" style={STATUS_STYLE[k]}>{counts[k] ?? 0}</span>{k.replace('-', ' ')}</span>
        ))}
      </div>
      <div className="overflow-y-auto p-3 space-y-4">
        {mock.sections.map((sec, si) => (
          <div key={sec.sectionId}>
            <div className="text-xs font-bold faint uppercase mb-2">{sec.name}</div>
            <div className="grid grid-cols-6 gap-1.5">
              {flat.map((f, i) => f.s !== si ? null : (
                <button key={i} onClick={() => go(i)} className="h-9 rounded-md text-xs font-bold"
                  style={{ ...STATUS_STYLE[st.status[i]], outline: i === st.cur ? '2px solid var(--brand)' : 'none', outlineOffset: 1 }}>{f.n + 1}</button>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  return (
    <div className="fixed inset-0 z-40 flex flex-col" style={{ background: 'var(--bg)' }}>
      <div className="flex items-center justify-between gap-2 px-3 sm:px-5 h-14 border-b shrink-0" style={{ borderColor: 'var(--line)', background: 'var(--surface)' }}>
        <div className="font-bold text-sm sm:text-base truncate">{mock.title}</div>
        <div className="flex items-center gap-2">
          <span className="font-mono tabular-nums font-bold px-3 py-1 rounded-lg text-sm sm:text-base"
            style={{ background: lowTime ? 'var(--bad-soft)' : 'var(--surface-2)', color: lowTime ? 'var(--bad)' : 'var(--ink)' }}>⏱ {fmt(Math.max(0, st.remaining))}</span>
          <button className="btn lg:hidden" style={{ padding: '.35rem .6rem' }} onClick={() => setPaletteOpen(true)}>☰</button>
          <button className="btn btn-brand hidden sm:inline-flex" style={{ padding: '.35rem .8rem' }} onClick={() => setConfirmSubmit(true)}>Submit</button>
        </div>
      </div>
      <div className="flex gap-1 px-2 sm:px-4 overflow-x-auto border-b shrink-0" style={{ borderColor: 'var(--line)', background: 'var(--surface)' }}>
        {mock.sections.map((sec, si) => {
          const first = flat.findIndex((f) => f.s === si);
          return (
            <button key={sec.sectionId} onClick={() => go(first)} className="px-3 py-2 text-xs sm:text-sm font-semibold whitespace-nowrap border-b-2"
              style={{ borderColor: cur.s === si ? 'var(--brand)' : 'transparent', color: cur.s === si ? 'var(--ink)' : 'var(--ink-2)' }}>{sec.name}</button>
          );
        })}
      </div>
      <div className="flex flex-1 min-h-0">
        <div className="flex-1 overflow-y-auto">
          <div className="max-w-3xl mx-auto p-4 sm:p-6">
            <div className="flex justify-between text-sm mb-3">
              <span className="font-bold">Question {cur.n + 1}</span>
              <span className="faint">+{mock.plus} / −{wrongAnswerPenalty(cur.q, mock.minus)}</span>
            </div>
            <QuestionBody q={cur.q} />
            <div className="grid gap-2 mt-4">
              {cur.q.type === 'numeric' && (
                <label className="font-semibold text-sm">Numerical answer (TITA)
                  <input key={st.cur} type="number" step="any" aria-label="Numerical answer" className="block w-full mt-2 rounded-xl border p-3" style={{ borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' }} value={pending ?? ''} onChange={(e) => setPending(e.target.value === '' || !Number.isFinite(e.target.valueAsNumber) ? null : e.target.valueAsNumber)} />
                </label>
              )}
              {cur.q.options.map((o, i) => (
                <OptionButton key={i} label={LETTERS[i]} text={o} state={pending === i ? 'selected' : 'idle'} onClick={() => setPending(i)} />
              ))}
            </div>
          </div>
        </div>
        <aside className="hidden lg:block w-80 border-l shrink-0" style={{ borderColor: 'var(--line)', background: 'var(--surface)' }}>{palette}</aside>
      </div>
      <div className="flex flex-wrap items-center gap-2 px-3 sm:px-5 py-2.5 border-t shrink-0" style={{ borderColor: 'var(--line)', background: 'var(--surface)' }}>
        <button className="btn text-sm" onClick={() => commit(true)}>Mark for Review &amp; Next</button>
        <button className="btn text-sm" onClick={clear}>Clear</button>
        <span className="flex-1" />
        <button className="btn text-sm" disabled={st.cur === 0} onClick={() => go(st.cur - 1)}>← Back</button>
        <button className="btn btn-brand text-sm" onClick={() => commit(false)}>Save &amp; Next</button>
        <button className="btn btn-brand sm:hidden text-sm" onClick={() => setConfirmSubmit(true)}>Submit</button>
      </div>

      {paletteOpen && (
        <div className="fixed inset-0 z-50 flex justify-end" style={{ background: 'rgba(0,0,0,.4)' }} onClick={() => setPaletteOpen(false)}>
          <div className="w-80 max-w-[85vw] h-full" style={{ background: 'var(--surface)' }} onClick={(e) => e.stopPropagation()}>{palette}</div>
        </div>
      )}
      {confirmSubmit && (
        <div className="fixed inset-0 z-50 grid place-items-center p-4" style={{ background: 'rgba(0,0,0,.45)' }}>
          <div className="card p-5 w-full max-w-md">
            <h3 className="font-bold text-lg">Submit the test?</h3>
            <div className="tbl-wrap mt-3">
              <table className="tbl">
                <thead><tr><th>Section</th><th>Answered</th><th>Marked</th><th>Not answered</th></tr></thead>
                <tbody>
                  {mock.sections.map((sec, si) => {
                    const idx = flat.map((f, i) => (f.s === si ? i : -1)).filter((i) => i >= 0);
                    const ans = idx.filter((i) => st.answers[i] !== null).length;
                    const mk = idx.filter((i) => st.status[i] === 'marked' || st.status[i] === 'answered-marked').length;
                    return <tr key={sec.sectionId}><td>{sec.name}</td><td>{ans}</td><td>{mk}</td><td>{idx.length - ans}</td></tr>;
                  })}
                </tbody>
              </table>
            </div>
            <p className="text-sm muted mt-3">Time left: {fmt(Math.max(0, st.remaining))}</p>
            <div className="flex gap-2 justify-end mt-4">
              <button className="btn" onClick={() => setConfirmSubmit(false)}>Keep going</button>
              <button className="btn btn-brand" onClick={submit}>Yes, submit</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

// ---------------- RESULT VIEW ----------------
function MockResult({ mock, flat, answers, times, attempt }: { mock: Mock; flat: Flat[]; answers: (number | null)[]; times: number[]; attempt: MockAttempt }) {
  const [filter, setFilter] = useState<'all' | 'wrong' | 'skipped' | 'correct' | 'slow'>('wrong');
  const [open, setOpen] = useState<number | null>(null);
  const { user, configured } = useAuth();
  const path = usePathname() || '/';
  const history = store.attempts()[mock.id] ?? [];
  const computer = mock.tier === 2 ? attempt.sections['computer'] : undefined;
  /* Tier 2 merit excludes the 20-question Computer module (60 qualifying marks). */
  const meritEntries = Object.entries(attempt.sections).filter(([sid]) => !(mock.tier === 2 && sid === 'computer'));
  const meritScore = meritEntries.reduce((n, [, s]) => n + s.score, 0);
  const meritCorrect = meritEntries.reduce((n, [, s]) => n + s.correct, 0);
  const meritWrong = meritEntries.reduce((n, [, s]) => n + s.wrong, 0);
  const meritTotal = meritEntries.reduce((n, [, s]) => n + s.total, 0);
  const displayScore = mock.tier === 2 ? meritScore : attempt.score;
  const displayMax = mock.tier === 2 ? 390 : attempt.max;
  const displayCorrect = mock.tier === 2 ? meritCorrect : attempt.correct;
  const displayWrong = mock.tier === 2 ? meritWrong : attempt.wrong;
  const displaySkipped = mock.tier === 2 ? meritTotal - meritCorrect - meritWrong : attempt.skipped;
  const accuracy = displayCorrect + displayWrong ? Math.round((100 * displayCorrect) / (displayCorrect + displayWrong)) : 0;

  // topic-level weakness from subtopic tags
  const topics: Record<string, { c: number; w: number; s: number }> = {};
  flat.forEach((f, i) => {
    const t = f.q.subtopic || 'other';
    const r = (topics[t] ??= { c: 0, w: 0, s: 0 });
    if (answers[i] === null) r.s++; else if (answers[i] === f.q.answer) r.c++; else r.w++;
  });
  const weak = Object.entries(topics).filter(([, r]) => r.w + r.s > 0).sort((a, b) => (b[1].w * 2 + b[1].s) - (a[1].w * 2 + a[1].s)).slice(0, 8);

  const avgTime = flat.length ? Math.round(times.reduce((a, b) => a + b, 0) / flat.length) : 0;
  const list = flat.map((f, i) => ({ f, i })).filter(({ f, i }) => {
    const a = answers[i];
    if (filter === 'wrong') return a !== null && a !== f.q.answer;
    if (filter === 'skipped') return a === null;
    if (filter === 'correct') return a === f.q.answer;
    if (filter === 'slow') return times[i] > Math.max(60, avgTime * 1.6);
    return true;
  });

  return (
    <div className="max-w-5xl mx-auto">
      <Link href={`/exams/${mock.exam ?? "ssc-cgl"}/mocks/`} className="text-sm faint">← All mock tests</Link>
      <h1 className="text-2xl sm:text-3xl font-extrabold mt-2">Result · {mock.title}</h1>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-5">
        {[
          [mock.tier === 2 ? 'Merit score' : 'Score', `${displayScore.toFixed(2).replace(/\.00$/, '')} / ${displayMax}`],
          ['Accuracy', `${accuracy}%`],
          ['Correct · Wrong · Skipped', `${displayCorrect} · ${displayWrong} · ${displaySkipped}`],
          ['Time used', fmt(attempt.timeSec)],
        ].map(([k, v]) => (
          <div key={k} className="card p-4"><div className="text-xs faint font-semibold">{k}</div><div className="text-xl font-extrabold mt-1">{v}</div></div>
        ))}
      </div>
      {mock.tier === 2 && (
        <div className="card p-4 mt-3" style={{ borderStyle: 'dashed' }}>
          <div className="text-xs faint font-semibold">Computer Knowledge (Session-I Section-III)</div>
          <div className="text-xl font-extrabold mt-1">
            Computer Knowledge (qualifying): {computer ? `${computer.score.toFixed(2).replace(/\.00$/, '')} / 60` : '— / 60'}
          </div>
          <p className="text-xs faint mt-1">
            {computer
              ? 'These 60 marks are qualifying only and are not part of the 390-mark merit score.'
              : 'This attempt has no separate Computer section score, so only the merit score above is shown.'}
          </p>
        </div>
      )}
      {displayScore > 0 && (
        <ShareScore
          title={mock.title} score={displayScore} max={displayMax} accuracy={accuracy}
          correct={displayCorrect} wrong={displayWrong} skipped={displaySkipped}
          url={`https://examshortcut.in/exams/${mock.exam ?? 'ssc-cgl'}/mocks/${mock.id}/`}
        />
      )}
      {configured && !user && (
        <p className="text-xs muted mt-3">
          This score isn&apos;t saved yet.{' '}
          <Link href={`/login/?next=${encodeURIComponent(path)}`} className="btn" style={{ padding: '.2rem .65rem', fontSize: '.75rem', marginLeft: '.25rem' }}>Log in to save</Link>
        </p>
      )}
      {mock.tier === 1 && (
        <p className="text-sm muted mt-3">Compare your score with the <Link className="underline" href={`/exams/${mock.exam ?? 'ssc-cgl'}/cutoffs/`}>year-wise official cutoffs</Link> for your category
          (remember real scores are normalised across shifts).</p>
      )}

      <h2 className="font-bold text-lg mt-8 mb-3">Section-wise</h2>
      <div className="tbl-wrap">
        <table className="tbl">
          <thead><tr><th>Section</th><th>Score</th><th>Correct</th><th>Wrong</th><th>Skipped</th><th>Accuracy</th><th>Avg time/Q</th></tr></thead>
          <tbody>
            {mock.sections.map((sec, si) => {
              const s = attempt.sections[sec.sectionId];
              const idx = flat.map((f, i) => (f.s === si ? i : -1)).filter((i) => i >= 0);
              const t = idx.length ? Math.round(idx.reduce((n, i) => n + times[i], 0) / idx.length) : 0;
              if (!s) {
                return (
                  <tr key={sec.sectionId}>
                    <td className="font-semibold">{sec.name}</td>
                    <td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>{t}s</td>
                  </tr>
                );
              }
              return (
                <tr key={sec.sectionId}>
                  <td className="font-semibold">{sec.name}</td>
                  <td>{s.score.toFixed(2).replace(/\.00$/, '')} / {s.max}</td><td>{s.correct}</td><td>{s.wrong}</td><td>{s.total - s.correct - s.wrong}</td>
                  <td>{s.correct + s.wrong ? Math.round((100 * s.correct) / (s.correct + s.wrong)) : 0}%</td><td>{t}s</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {weak.length > 0 && (
        <>
          <h2 className="font-bold text-lg mt-8 mb-3">Topics to fix first</h2>
          <div className="flex flex-wrap gap-2">
            {weak.map(([t, r]) => {
              const sec = flat.find((f) => (f.q.subtopic || 'other') === t);
              const sid = sec ? mock.sections[sec.s].sectionId : '';
              return (
                <Link key={t} href={`/${sid}/${t}/`} className="chip" style={{ padding: '.35rem .7rem', fontSize: '.8rem' }}>
                  {t.replace(/-/g, ' ')} · <span style={{ color: 'var(--bad)' }}>{r.w} wrong</span> · {r.s} skipped
                </Link>
              );
            })}
          </div>
        </>
      )}

      {history.length > 1 && (
        <p className="text-sm muted mt-6">Your attempts on this paper: {history.map((h) => h.score.toFixed(1).replace(/\.0$/, '')).join(' → ')}</p>
      )}

      <h2 className="font-bold text-lg mt-8 mb-3">Solutions</h2>
      <div className="flex flex-wrap gap-2 mb-4">
        {(['wrong', 'skipped', 'slow', 'correct', 'all'] as const).map((k) => (
          <button key={k} className="chip" onClick={() => setFilter(k)} style={filter === k ? { background: 'var(--ink)', color: 'var(--bg)' } : {}}>
            {k === 'slow' ? 'Took too long' : k[0].toUpperCase() + k.slice(1)}
          </button>
        ))}
      </div>
      <div className="space-y-3">
        {list.length === 0 && <p className="faint text-sm">Nothing here.</p>}
        {list.map(({ f, i }) => {
          const a = answers[i];
          const verdict = a === null ? 'Skipped' : a === f.q.answer ? 'Correct' : 'Wrong';
          return (
            <div key={i} className="card p-4">
              <button className="w-full text-left flex items-center justify-between gap-2 text-sm" onClick={() => setOpen(open === i ? null : i)}>
                <span className="font-semibold">{mock.sections[f.s].name} · Q{f.n + 1}</span>
                <span className="flex gap-2 items-center">
                  <span className="faint">{times[i]}s</span>
                  <span className="chip" style={{ color: verdict === 'Correct' ? 'var(--ok)' : verdict === 'Wrong' ? 'var(--bad)' : 'var(--ink-2)' }}>{verdict}</span>
                  <span>{open === i ? '▾' : '▸'}</span>
                </span>
              </button>
              {open === i && (
                <div className="mt-3">
                  <QuestionBody q={f.q} />
                  <div className="grid gap-2 mt-3">
                    {f.q.type === 'numeric' && <p className="text-sm">Your answer: <b>{a ?? 'Skipped'}</b> · Correct answer: <b>{f.q.answer}</b></p>}
                    {f.q.options.map((o, k) => (
                      <OptionButton key={k} label={LETTERS[k]} text={o} disabled
                        state={k === f.q.answer ? (a === k ? 'correct' : 'missed') : a === k ? 'wrong' : 'idle'} />
                    ))}
                  </div>
                  <Explanation q={f.q} />
                </div>
              )}
            </div>
          );
        })}
      </div>
      <div className="flex gap-3 mt-8 flex-wrap">
        <Link className="btn btn-brand" href="/revision/">Open mistake notebook</Link>
        <button className="btn" onClick={() => location.reload()}>Retake this paper</button>
      </div>
    </div>
  );
}
