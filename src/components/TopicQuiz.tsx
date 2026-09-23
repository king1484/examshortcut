'use client';
import { useEffect, useMemo, useRef, useState } from 'react';
import type { Question } from '@/lib/types';
import { store, useStore } from '@/lib/store';
import { Explanation, LETTERS, OptionButton, QuestionBody, withPassages } from './QuestionView';

type Mode = 'practice' | 'test';

function fmt(sec: number) {
  const m = Math.floor(sec / 60), s = sec % 60;
  return `${m}:${String(s).padStart(2, '0')}`;
}

export function TopicQuiz({ questions: raw, storageKey, href, section, title }: { questions: Question[]; storageKey: string; href: string; section: string; title: string }) {
  const questions = useMemo(() => withPassages(raw), [raw]);
  const [mode, setMode] = useState<Mode | null>(null);
  const [idx, setIdx] = useState(0);
  const [answers, setAnswers] = useState<(number | null)[]>(() => questions.map(() => null));
  const [revealed, setRevealed] = useState<boolean[]>(() => questions.map(() => false));
  const [times, setTimes] = useState<number[]>(() => questions.map(() => 0));
  const [done, setDone] = useState(false);
  const [elapsed, setElapsed] = useState(0);
  const tick = useRef<number | null>(null);
  const bookmarks = useStore(store.bookmarks, {});
  const scores = useStore(store.topicScores, {});

  const budget = questions.reduce((n, q) => n + (q.timeSec ?? 45), 0);

  useEffect(() => {
    if (!mode || done) return;
    tick.current = window.setInterval(() => {
      setElapsed((e) => e + 1);
      setTimes((t) => { const c = [...t]; c[idx] += 1; return c; });
    }, 1000);
    return () => { if (tick.current) window.clearInterval(tick.current); };
  }, [mode, done, idx]);

  useEffect(() => {
    if (mode === 'test' && !done && elapsed >= budget) finish();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [elapsed]);

  const q = questions[idx];
  const keyOf = (qq: Question) => `${storageKey}/${qq.id}`;

  function saveMistake(qq: Question, chosen: number | null) {
    store.addMistake({ key: keyOf(qq), question: qq, chosen, from: title, href, section, at: Date.now() });
  }

  function choose(i: number) {
    if (done) return;
    if (mode === 'practice' && revealed[idx]) return;
    const a = [...answers]; a[idx] = i; setAnswers(a);
    if (mode === 'practice') {
      const r = [...revealed]; r[idx] = true; setRevealed(r);
      if (i !== q.answer) saveMistake(q, i);
    }
  }

  function finish() {
    setDone(true);
    const correct = questions.filter((qq, i) => answers[i] === qq.answer).length;
    questions.forEach((qq, i) => { if (answers[i] !== null && answers[i] !== qq.answer) saveMistake(qq, answers[i]); });
    store.saveTopicScore(storageKey, correct, questions.length);
    setIdx(0);
  }

  function reset(m: Mode) {
    setMode(m); setIdx(0); setDone(false); setElapsed(0);
    setAnswers(questions.map(() => null)); setRevealed(questions.map(() => false)); setTimes(questions.map(() => 0));
  }

  if (!questions.length) return null;

  const prev = scores[storageKey];
  if (!mode) {
    return (
      <div className="card p-5 sm:p-6">
        <h3 className="text-lg font-bold">Topic test · {questions.length} questions</h3>
        <p className="muted text-sm mt-1">Suggested time {Math.round(budget / 60)} min · wrong answers go to your mistake notebook automatically.
          {prev && <> Your best: <b>{prev.best}/{prev.total}</b>.</>}</p>
        <div className="grid sm:grid-cols-2 gap-3 mt-4">
          <button className="btn btn-brand" onClick={() => reset('practice')}>Practice mode — instant answers</button>
          <button className="btn" onClick={() => reset('test')}>Timed test — {Math.round(budget / 60)} min</button>
        </div>
      </div>
    );
  }

  const correctCount = questions.filter((qq, i) => answers[i] === qq.answer).length;
  const wrongCount = questions.filter((qq, i) => answers[i] !== null && answers[i] !== qq.answer).length;
  const showAnswer = done || (mode === 'practice' && revealed[idx]);
  const bmKey = keyOf(q);

  return (
    <div className="card p-4 sm:p-6" id="quiz">
      {done && (
        <div className="mb-5 rounded-xl p-4" style={{ background: 'var(--brand-soft)' }}>
          <div className="text-2xl font-extrabold">{correctCount}/{questions.length} correct</div>
          <div className="text-sm muted mt-1">
            {wrongCount} wrong · {questions.length - correctCount - wrongCount} skipped · time {fmt(elapsed)} (target {fmt(budget)}) ·
            accuracy {correctCount + wrongCount ? Math.round((100 * correctCount) / (correctCount + wrongCount)) : 0}%
          </div>
          <div className="flex gap-2 mt-3 flex-wrap">
            <button className="btn" onClick={() => reset('practice')}>Retry in practice mode</button>
            <button className="btn" onClick={() => reset('test')}>Retake timed test</button>
          </div>
        </div>
      )}

      <div className="flex items-center justify-between gap-3 mb-4 text-sm">
        <span className="font-semibold">Question {idx + 1} of {questions.length}
          {q.difficulty && <span className={`chip ml-2 ${q.difficulty === 'hard' ? 'chip-high' : q.difficulty === 'medium' ? 'chip-medium' : 'chip-low'}`}>{q.difficulty}</span>}
        </span>
        <span className="flex items-center gap-2">
          {!done && <span className="font-mono tabular-nums" title="Elapsed">{mode === 'test' ? `⏱ ${fmt(Math.max(0, budget - elapsed))} left` : `⏱ ${fmt(times[idx])}`}</span>}
          <button className="chip" onClick={() => store.toggleBookmark({ key: bmKey, question: q, chosen: answers[idx], from: title, href, section, at: Date.now() })}>
            {bookmarks[bmKey] ? '★ Saved' : '☆ Save'}
          </button>
        </span>
      </div>

      <QuestionBody q={q} index={idx} />

      <div className="grid gap-2 mt-4">
        {q.options.map((o, i) => {
          let state: 'idle' | 'selected' | 'correct' | 'wrong' | 'missed' = answers[idx] === i ? 'selected' : 'idle';
          if (showAnswer) {
            if (i === q.answer) state = answers[idx] === i ? 'correct' : 'missed';
            else if (answers[idx] === i) state = 'wrong';
            else state = 'idle';
          }
          return <OptionButton key={i} label={LETTERS[i]} text={o} state={state} disabled={showAnswer} onClick={() => choose(i)} />;
        })}
      </div>

      {showAnswer && (
        <>
          {done && <p className="text-xs faint mt-3">You spent {fmt(times[idx])} · target {fmt(q.timeSec ?? 45)}</p>}
          <Explanation q={q} />
        </>
      )}

      <div className="flex items-center justify-between gap-2 mt-5">
        <button className="btn" disabled={idx === 0} onClick={() => setIdx(idx - 1)}>← Prev</button>
        {!done && mode === 'test' && <button className="btn" onClick={finish}>Submit test</button>}
        {idx < questions.length - 1 ? (
          <button className="btn btn-brand" onClick={() => setIdx(idx + 1)}>Next →</button>
        ) : !done ? (
          <button className="btn btn-brand" onClick={finish}>{mode === 'practice' ? 'Finish' : 'Submit'}</button>
        ) : (
          <span />
        )}
      </div>

      <div className="flex flex-wrap gap-1.5 mt-5">
        {questions.map((qq, i) => {
          const a = answers[i];
          const graded = done || (mode === 'practice' && revealed[i]);
          const bg = graded && a !== null ? (a === qq.answer ? 'var(--ok)' : 'var(--bad)') : a !== null ? 'var(--info)' : 'var(--surface-2)';
          const fg = a !== null ? '#fff' : 'var(--ink-2)';
          return (
            <button key={qq.id} onClick={() => setIdx(i)} className="w-8 h-8 rounded-lg text-xs font-bold"
              style={{ background: bg, color: fg, outline: i === idx ? '2px solid var(--brand)' : 'none', outlineOffset: 1 }}>{i + 1}</button>
          );
        })}
      </div>
    </div>
  );
}
