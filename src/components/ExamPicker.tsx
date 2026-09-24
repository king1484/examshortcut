'use client';
import Link from 'next/link';
import { EXAMS, EXAM_CATEGORIES } from '@/lib/exams';
import { SECTION_META } from '@/lib/sections';
import { setSelectedExam, useSelectedExam } from '@/lib/useExam';

/** Exam chooser. Picking an exam tailors the home page, daily quiz and dashboard to its subjects. */
export function ExamPicker({ heading = 'Which exam are you preparing for?' }: { heading?: string }) {
  const selected = useSelectedExam();
  return (
    <section>
      <div className="flex items-baseline justify-between flex-wrap gap-2">
        <h2 className="text-xl font-extrabold">{heading}</h2>
        {selected && (
          <button className="text-xs underline decoration-dotted faint" onClick={() => setSelectedExam(null)}>
            Clear selection
          </button>
        )}
      </div>
      {EXAM_CATEGORIES.map((cat) => {
        const list = EXAMS.filter((e) => e.category === cat);
        if (!list.length) return null;
        return (
          <div key={cat} className="mt-4">
            <p className="text-xs font-bold uppercase tracking-wide faint">{cat}</p>
            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2 mt-1.5">
              {list.map((e) => {
                const on = selected?.id === e.id;
                return (
                  <button key={e.id} onClick={() => setSelectedExam(e.id)} aria-pressed={on}
                    className="card p-3 text-left transition-transform hover:-translate-y-0.5"
                    style={on ? { borderColor: 'var(--brand)', boxShadow: '0 0 0 2px var(--brand)' } : undefined}>
                    <span className="flex items-center gap-1.5">
                      <span className="font-bold text-sm">{e.name}</span>
                      {e.status === 'soon' && <span className="chip chip-low ml-auto" style={{ fontSize: 10 }}>hub soon</span>}
                      {on && <span className="ml-auto text-xs font-bold" style={{ color: 'var(--brand)' }}>✓</span>}
                    </span>
                    <span className="text-[11px] muted mt-1 block line-clamp-2">{e.blurb}</span>
                  </button>
                );
              })}
            </div>
          </div>
        );
      })}
    </section>
  );
}

/** What the chosen exam covers, with links into the shared subjects. */
export function SelectedExamPanel() {
  const exam = useSelectedExam();
  if (!exam) return null;
  return (
    <div className="card p-4 sm:p-5">
      <div className="flex items-center gap-2 flex-wrap">
        <span className="text-xs font-bold uppercase tracking-wide faint">Preparing for</span>
        <span className="text-lg font-extrabold">{exam.name}</span>
        {exam.status === 'live'
          ? <Link href={`/exams/${exam.id}/`} className="btn btn-brand ml-auto" style={{ padding: '.35rem .8rem' }}>Open {exam.short} hub →</Link>
          : <span className="chip chip-low ml-auto">Exam hub (pattern, cutoffs, mocks) coming next</span>}
      </div>
      <p className="text-sm muted mt-2">Subjects in this exam — notes, question types and practice are ready now:</p>
      <div className="flex flex-wrap gap-2 mt-2">
        {exam.sections.map((s) => (
          <Link key={s} href={`/${s}/`} className="btn" style={{ padding: '.35rem .75rem' }}>
            <span style={{ color: SECTION_META[s].color }} className="font-bold mr-1">{SECTION_META[s].emoji}</span>
            {SECTION_META[s].name}
          </Link>
        ))}
        <Link href="/daily-quiz/" className="btn" style={{ padding: '.35rem .75rem' }}>🗓 Daily quiz</Link>
      </div>
    </div>
  );
}
