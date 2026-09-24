'use client';
import Link from 'next/link';
import { useEffect } from 'react';
import { SECTION_META, SECTION_ORDER } from '@/lib/sections';
import { useSelectedExam } from '@/lib/useExam';

/* Everything is server-rendered for every visitor (and crawler); this only dims the
   subjects the chosen exam doesn't test. */
export function LearnExamFilter() {
  const exam = useSelectedExam();
  useEffect(() => {
    document.querySelectorAll<HTMLElement>('[data-section]').forEach((el) => {
      el.style.opacity = exam && !exam.sections.includes(el.dataset.section as never) ? '0.45' : '';
    });
  }, [exam]);
  return (
    <div className="card p-3 mt-5 flex flex-wrap items-center gap-2 text-sm">
      {exam ? <span><b>{exam.name}</b> tests:</span> : <span className="muted">Jump to:</span>}
      {SECTION_ORDER.filter((s) => !exam || exam.sections.includes(s)).map((s) => (
        <a key={s} href={`#${s}`} className="chip" style={{ color: SECTION_META[s].color }}>{SECTION_META[s].short}</a>
      ))}
      <Link href="/exams/" className="ml-auto text-xs underline decoration-dotted">{exam ? 'Change exam' : 'Choose your exam'}</Link>
    </div>
  );
}
