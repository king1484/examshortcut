'use client';
import { Spinner } from './Spinner';
import { useEffect, useMemo, useState } from 'react';
import { store, useStore } from '@/lib/store';
import { SECTION_META, type SectionId } from '@/lib/sections';
import { useSelectedExam } from '@/lib/useExam';
import { examHasSection } from '@/lib/exams';
import { TopicQuiz } from './TopicQuiz';
import type { Question } from '@/lib/types';

interface Bucket { n: number; sections: { section: string; name: string; questions: Question[] }[] }
const BUCKETS = 30;

/** Today's mix: bucket = days-since-epoch % BUCKETS, trimmed to the chosen exam's subjects. */
export function DailyQuiz() {
  const [dayIndex, setDayIndex] = useState<number | null>(null);
  const [bucket, setBucket] = useState<Bucket | null>(null);
  const [err, setErr] = useState(false);
  const [tab, setTab] = useState(0);
  const exam = useSelectedExam();
  const scores = useStore(store.topicScores, {});

  useEffect(() => {
    const d = Math.floor(Date.now() / 86400000);
    setDayIndex(d);
    fetch(`/data/daily/${d % BUCKETS}.json`).then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status))))).then(setBucket).catch(() => setErr(true));
  }, []);

  const secs = useMemo(
    () => (bucket?.sections ?? []).filter((s) => examHasSection(exam, s.section)),
    [bucket, exam],
  );

  const dayDone = (d: number) => secs.some((s) => scores[`daily/${d}/${s.section}`]);
  const streak = useMemo(() => {
    if (dayIndex == null || !secs.length) return 0;
    let d = dayDone(dayIndex) ? dayIndex : dayIndex - 1; // today not finished yet? count from yesterday
    let n = 0;
    while (dayDone(d)) { n++; d--; }
    return n;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dayIndex, secs, scores]);

  if (dayIndex == null || (!bucket && !err)) return <div className="card"><Spinner label="Loading today's quiz" /></div>;
  if (err || !secs.length) {
    return (
      <div className="card p-6 text-center">
        <p className="text-sm muted">Today's quiz isn't ready in this browser copy. Try a refresh — if it still doesn't load, the next site update will bring it.</p>
      </div>
    );
  }

  const label = new Date().toLocaleDateString('en-IN', { timeZone: 'Asia/Kolkata', weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
  const active = secs[Math.min(tab, secs.length - 1)];
  const totalQ = secs.reduce((n, s) => n + s.questions.length, 0);

  return (
    <div>
      <div className="card p-4 sm:p-5 flex flex-wrap items-center gap-3">
        <div className="flex-1 min-w-[200px]">
          <h2 className="text-lg font-extrabold">Today's mix — {totalQ} questions</h2>
          <p className="text-xs muted mt-0.5">{label}{exam ? <> · tuned for <b>{exam.name}</b></> : null} · a new set every day at midnight</p>
        </div>
        {streak > 0 && <span className="chip chip-high">🔥 {streak}-day streak</span>}
      </div>

      <div className="flex gap-2 mt-4 flex-wrap" role="tablist">
        {secs.map((s, i) => {
          const meta = SECTION_META[s.section as SectionId];
          const done = !!scores[`daily/${dayIndex}/${s.section}`];
          return (
            <button key={s.section} role="tab" aria-selected={i === tab} onClick={() => setTab(i)}
              className={`btn ${i === tab ? 'btn-brand' : ''}`} style={{ padding: '.35rem .8rem' }}>
              <span style={{ color: i === tab ? undefined : meta?.color }}>{meta?.emoji}</span> {meta?.short ?? s.name}
              {done && <span className="ml-1" style={{ color: 'var(--ok)' }}>✓</span>}
            </button>
          );
        })}
      </div>

      <div className="mt-3" key={active.section}>
        <TopicQuiz questions={active.questions} storageKey={`daily/${dayIndex}/${active.section}`} href="/daily-quiz/" section={active.section} title={`Daily · ${active.name}`} />
      </div>

      <p className="text-xs faint mt-6">Missed a day? The mix rotates every day — play today's to keep your streak. Questions come from the practice sets of every subject{exam ? ' in your exam' : ''}.</p>
    </div>
  );
}
