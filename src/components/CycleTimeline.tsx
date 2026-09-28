'use client';
import { useEffect, useState } from 'react';

export interface Milestone {
  label: string;
  value: string;
  note?: string;
  /** ISO dates (IST). No `from` = not announced yet. */
  from?: string;
  to?: string;
}

type State = 'done' | 'live' | 'next' | 'tba';
const ist = (d: string) => new Date(`${d}T00:00:00+05:30`).getTime();
const DAY = 86400000;

function stateOf(m: Milestone, now: number): State {
  if (!m.from) return 'tba';
  const end = ist(m.to ?? m.from) + DAY;
  if (now >= end) return 'done';
  if (now >= ist(m.from)) return 'live';
  return 'next';
}

const TAG: Record<State, string> = { done: 'Done', live: 'Live now', next: 'Upcoming', tba: 'Awaited' };

/* Exam-cycle stepper. The static build renders states as of `builtAt`; after mount
   they are recomputed from the visitor's clock, so the page never goes stale. */
export function CycleTimeline({ milestones, builtAt }: { milestones: Milestone[]; builtAt: number }) {
  const [now, setNow] = useState(builtAt);
  useEffect(() => setNow(Date.now()), []);
  const states = milestones.map((m) => stateOf(m, now));
  // the first milestone not yet done is "current" even before it starts
  const cur = states.findIndex((s) => s !== 'done');

  return (
    <ol className="cycle mt-5">
      {milestones.map((m, i) => {
        const s = states[i];
        return (
          <li key={m.label} className={`cycle-step is-${s}${i === cur ? ' is-current' : ''}`}>
            <span className="cycle-dot" aria-hidden>{s === 'done' ? '✓' : ''}</span>
            <div className="cycle-body">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="cycle-label">{m.label}</span>
                <span className="cycle-tag">{TAG[s]}</span>
              </div>
              <div className="cycle-value">{m.value}</div>
              {m.note && <div className="text-xs faint mt-0.5">{m.note}</div>}
            </div>
          </li>
        );
      })}
    </ol>
  );
}
