'use client';
import { useState } from 'react';
import type { Question } from '@/lib/types';
import { TopicQuiz } from './TopicQuiz';

/** Splits a question pool into numbered sets of `size`; one set is mounted at a time. */
export function PracticeSets({ questions, size = 10, storageKey, href, section, title }: {
  questions: Question[]; size?: number; storageKey: string; href: string; section: string; title: string;
}) {
  const sets: Question[][] = [];
  for (let i = 0; i < questions.length; i += size) sets.push(questions.slice(i, i + size));
  // fold a tiny last set into the previous one so no set is 1–3 questions
  if (sets.length > 1 && sets[sets.length - 1].length < 4) sets[sets.length - 2].push(...sets.pop()!);
  const [active, setActive] = useState(0);
  if (!sets.length) return null;
  return (
    <div>
      {sets.length > 1 && (
        <div className="flex flex-wrap gap-2" role="tablist">
          {sets.map((s, i) => (
            <button key={i} role="tab" aria-selected={i === active} onClick={() => setActive(i)}
              className={`btn ${i === active ? 'btn-brand' : ''}`} style={{ padding: '.35rem .8rem' }}>
              Set {i + 1} <span className="opacity-70 text-xs ml-1">{s.length} Q</span>
            </button>
          ))}
        </div>
      )}
      <div className="mt-3" key={active}>
        <TopicQuiz questions={sets[active]} storageKey={sets.length > 1 ? `${storageKey}/set-${active + 1}` : storageKey}
          href={href} section={section} title={sets.length > 1 ? `${title} · Set ${active + 1}` : title} />
      </div>
    </div>
  );
}
