'use client';
import { useState } from 'react';
import type { Question } from '@/lib/types';
import { Md, Figure, isSvg } from './Md';
import patternNames from '@/data/pattern-names.json';

/** Fill in `passage` for grouped RC / cloze questions that only carry it on the first member. */
export function withPassages(qs: Question[]): Question[] {
  const byGroup: Record<string, string> = {};
  for (const q of qs) if (q.group && q.passage) byGroup[q.group] = q.passage;
  return qs.map((q) => (q.group && !q.passage && byGroup[q.group] ? { ...q, passage: byGroup[q.group] } : q));
}

export function Passage({ text }: { text?: string }) {
  const [open, setOpen] = useState(true);
  if (!text) return null;
  return (
    <div className="card p-3 mb-3" style={{ background: 'var(--surface-2)' }}>
      <button className="text-xs font-bold faint uppercase tracking-wide mb-1" onClick={() => setOpen(!open)}>
        {open ? '▾' : '▸'} Passage
      </button>
      {open && <div className="max-h-72 overflow-y-auto pr-1"><Md>{text}</Md></div>}
    </div>
  );
}

type OptState = 'idle' | 'selected' | 'correct' | 'wrong' | 'missed';

export function OptionButton({ label, text, state, onClick, disabled }: { label: string; text: string; state: OptState; onClick?: () => void; disabled?: boolean }) {
  const styles: Record<OptState, React.CSSProperties> = {
    idle: {},
    selected: { borderColor: 'var(--info)', background: 'var(--info-soft)' },
    correct: { borderColor: 'var(--ok)', background: 'var(--ok-soft)' },
    wrong: { borderColor: 'var(--bad)', background: 'var(--bad-soft)' },
    missed: { borderColor: 'var(--ok)', borderStyle: 'dashed' },
  };
  return (
    <button disabled={disabled} onClick={onClick}
      className="w-full text-left flex items-start gap-3 p-3 rounded-xl border transition-colors disabled:cursor-default"
      style={{ borderColor: 'var(--line)', background: 'var(--surface)', ...styles[state] }}>
      <span className="shrink-0 w-7 h-7 rounded-full grid place-items-center text-sm font-bold border" style={{ borderColor: 'var(--line)' }}>
        {state === 'correct' ? '✓' : state === 'wrong' ? '✗' : label}
      </span>
      <span className={`flex-1 pt-0.5 ${isSvg(text) ? '' : ''}`}><Md inline>{text}</Md></span>
    </button>
  );
}

export function QuestionBody({ q, index }: { q: Question; index?: number }) {
  return (
    <div>
      <Passage text={q.passage} />
      <div className="flex gap-2 items-start">
        {index !== undefined && <span className="font-bold shrink-0">Q{index + 1}.</span>}
        <div className="flex-1 min-w-0"><Md>{q.q}</Md></div>
      </div>
      <Figure svg={q.figure} />
    </div>
  );
}

export function Explanation({ q }: { q: Question }) {
  const [tab, setTab] = useState<'shortcut' | 'solution'>(q.shortcut ? 'shortcut' : 'solution');
  return (
    <div className="mt-4 rounded-xl border p-4" style={{ borderColor: 'var(--line)', background: 'var(--surface-2)' }}>
      <div className="flex gap-2 mb-3 flex-wrap items-center">
        {q.shortcut && (
          <button className="chip" onClick={() => setTab('shortcut')} style={tab === 'shortcut' ? { background: 'var(--brand)', color: 'var(--brand-ink)', borderColor: 'var(--brand)' } : {}}>⚡ Shortcut</button>
        )}
        <button className="chip" onClick={() => setTab('solution')} style={tab === 'solution' ? { background: 'var(--ink)', color: 'var(--bg)', borderColor: 'var(--ink)' } : {}}>Full solution</button>
        {q.pattern && <span className="chip ml-auto" title="Recurring PYQ pattern">PYQ pattern: {(patternNames as Record<string, string>)[q.pattern] ?? q.pattern}</span>}
      </div>
      <Md>{tab === 'shortcut' && q.shortcut ? q.shortcut : q.solution}</Md>
    </div>
  );
}

export const LETTERS = ['A', 'B', 'C', 'D', 'E'];
