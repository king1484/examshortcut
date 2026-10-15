import type { ReactNode } from 'react';
import type { Question } from '@/lib/types';
import { LETTERS } from '@/lib/topicInsights';
import { Md, Figure, isSvg } from '@/components/Md';

const DIFF_CHIP: Record<string, string> = { easy: 'chip-low', medium: 'chip-medium', hard: 'chip-high' };

/** A question with its options, answer, full solution and shortcut rendered as plain server HTML
    (no interaction, no hidden text), for pages where the questions themselves are the content. */
export function SampleQuestion({ q, label, tags, id }: { q: Question; label: string; tags?: ReactNode; id?: string }) {
  const right = q.options[q.answer];
  return (
    <article className="card p-4 sm:p-5" id={id}>
      <div className="flex gap-2 items-center flex-wrap text-xs">
        <span className="font-extrabold text-sm">{label}</span>
        {q.difficulty && <span className={`chip ${DIFF_CHIP[q.difficulty] ?? ''}`}>{q.difficulty}</span>}
        {tags}
        {q.timeSec ? <span className="faint">{q.timeSec}s exam budget</span> : null}
      </div>
      {q.passage && (
        <div className="mt-3 rounded-xl px-3 py-2.5 text-sm" style={{ background: 'var(--surface-2)' }}>
          <div className="faint text-xs font-semibold uppercase tracking-wide">Passage</div>
          <Md>{q.passage}</Md>
        </div>
      )}
      <div className="mt-3"><Md>{q.q}</Md></div>
      <Figure svg={q.figure} />
      <ol className="mt-3 grid gap-1.5 list-none p-0">
        {q.options.map((o, i) => (
          <li key={i} className="flex gap-2.5 items-start text-sm">
            <span className="shrink-0 font-bold w-5">{LETTERS[i]}.</span>
            <span className="min-w-0 flex-1"><Md inline>{o}</Md></span>
          </li>
        ))}
      </ol>
      <div className="mt-3 text-sm font-bold flex gap-1.5 items-baseline flex-wrap" style={{ color: 'var(--ok)' }}>
        <span>Correct answer: option {LETTERS[q.answer]}</span>
        {right && !isSvg(right) ? <><span aria-hidden>—</span><span className="min-w-0"><Md inline>{right}</Md></span></> : null}
      </div>
      <h4 className="mt-3 text-xs font-bold uppercase tracking-wide faint">Step-by-step solution</h4>
      <Md className="text-sm">{q.solution}</Md>
      {typeof q.shortcut === 'string' && q.shortcut && (
        <>
          <h4 className="mt-3 text-xs font-bold uppercase tracking-wide faint">Exam shortcut</h4>
          <Md className="text-sm">{q.shortcut}</Md>
        </>
      )}
    </article>
  );
}
