'use client';
import Link from 'next/link';
import { useEffect, useRef, useState } from 'react';
import { EXAMS, EXAM_CATEGORIES, type ExamInfo } from '@/lib/exams';
import { SECTION_META } from '@/lib/sections';
import { setSelectedExam, useSelectedExam } from '@/lib/useExam';

/** Exam chooser. Picking an exam tailors the home page, daily quiz and dashboard to its subjects.
 *  The chosen exam's panel opens right where it was tapped (and scrolls into view), so on a phone the tap
 *  visibly leads somewhere. With `collapse`, a chosen exam folds the grid away behind a "Change exam" button. */
export function ExamPicker({ heading = 'Which exam are you preparing for?', collapse = false }: { heading?: string; collapse?: boolean }) {
  const selected = useSelectedExam();
  const [choosing, setChoosing] = useState(false);
  const [picked, setPicked] = useState(0);
  const rootRef = useRef<HTMLElement>(null);
  const panelRef = useRef<HTMLDivElement>(null);
  const folded = collapse && !!selected && !choosing;

  useEffect(() => {
    if (!picked) return;
    const el = folded ? rootRef.current : panelRef.current;
    el?.scrollIntoView({ behavior: 'smooth', block: folded ? 'start' : 'nearest' });
  }, [picked, folded]);

  const pick = (id: string) => {
    setSelectedExam(id);
    setChoosing(false);
    setPicked((n) => n + 1);
  };

  if (folded && selected) {
    return (
      <section ref={rootRef} style={{ scrollMarginTop: 112 }}>
        <SelectedExamPanel exam={selected} onChange={() => setChoosing(true)} />
      </section>
    );
  }

  return (
    <section ref={rootRef} className="card p-4 sm:p-5" style={{ scrollMarginTop: 112 }}>
      <div className="flex items-baseline justify-between flex-wrap gap-2">
        <h2 className="text-xl font-extrabold">{heading}</h2>
        {selected && (
          <button className="text-xs underline decoration-dotted faint" onClick={() => { setSelectedExam(null); setChoosing(false); }}>
            Clear selection
          </button>
        )}
      </div>
      <p className="text-sm muted mt-1">Tap your exam to see what it covers and where to start.</p>
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
                  <button key={e.id} onClick={() => pick(e.id)} aria-pressed={on}
                    className="card p-3 text-left transition-transform hover:-translate-y-0.5"
                    style={on ? { borderColor: 'var(--brand)', boxShadow: '0 0 0 2px var(--brand)' } : undefined}>
                    <span className="flex items-center gap-1.5">
                      <span className="font-bold text-sm">{e.name}</span>
                      {e.status === 'soon' && !on && <span className="chip chip-low ml-auto" style={{ fontSize: 10 }}>soon</span>}
                      {on && <span className="ml-auto text-xs font-bold" style={{ color: 'var(--brand)' }}>✓</span>}
                    </span>
                    <span className="text-[11px] muted mt-1 block line-clamp-2">{e.blurb}</span>
                  </button>
                );
              })}
            </div>
            {!collapse && selected?.category === cat && (
              <div ref={panelRef} className="mt-3" style={{ scrollMarginTop: 112, scrollMarginBottom: 16 }}>
                <SelectedExamPanel exam={selected} />
              </div>
            )}
          </div>
        );
      })}
    </section>
  );
}

/** Conducting body, eligibility, stages and applicant count — the basic facts shown for every exam. */
export function ExamBasicsList({ exam, className = '' }: { exam: ExamInfo; className?: string }) {
  const rows: [string, string][] = [
    ['Conducted by', exam.basics.conductingBody],
    ['Eligibility', exam.basics.eligibility],
    ['Stages', exam.basics.stages],
    ['Applicants', exam.basics.applicants],
  ];
  return (
    <dl className={`grid grid-cols-[6.5rem_1fr] gap-x-3 gap-y-1 text-sm ${className}`}>
      {rows.map(([k, v]) => (
        <div key={k} className="contents">
          <dt className="faint">{k}</dt>
          <dd>{v}</dd>
        </div>
      ))}
    </dl>
  );
}

/** What the chosen exam covers, with links into the shared subjects. */
export function SelectedExamPanel({ exam, onChange }: { exam: ExamInfo; onChange?: () => void }) {
  return (
    <div className="card p-4 sm:p-5" style={{ borderColor: 'var(--brand)' }}>
      <div className="flex items-center gap-2 flex-wrap">
        <span className="text-xs font-bold uppercase tracking-wide faint">Preparing for</span>
        <span className="text-lg font-extrabold">{exam.name}</span>
        {onChange && (
          <button className="text-xs underline decoration-dotted faint" onClick={onChange}>Change exam</button>
        )}
        {exam.status === 'live'
          ? <Link href={`/exams/${exam.id}/`} className="btn btn-brand ml-auto" style={{ padding: '.35rem .8rem' }}>Open {exam.short} hub →</Link>
          : <span className="chip chip-low ml-auto">Full hub coming soon</span>}
      </div>
      {exam.status === 'soon' && <ExamBasicsList exam={exam} className="mt-3" />}
      <p className="text-sm muted mt-3">
        {exam.sections.length
          ? 'Subjects in this exam — notes, question types and practice are ready now:'
          : `${exam.short} subjects aren't on ExamShortcut yet — meanwhile, sharpen speed and accuracy here:`}
      </p>
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
