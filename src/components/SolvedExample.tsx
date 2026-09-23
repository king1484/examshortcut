'use client';
import { useState } from 'react';
import type { Question } from '@/lib/types';
import { Explanation, LETTERS, OptionButton, QuestionBody, withPassages } from './QuestionView';
import { store } from '@/lib/store';

export function SolvedExample({ q, n }: { q: Question; n: number }) {
  const [chosen, setChosen] = useState<number | null>(null);
  const [show, setShow] = useState(false);
  const qs = withPassages([q])[0];
  const revealed = show || chosen !== null;

  return (
    <div className="card p-4 sm:p-5">
      <QuestionBody q={qs} index={n - 1} />
      <div className="grid gap-2 mt-3">
        {qs.options.map((o, i) => {
          let state: 'idle' | 'selected' | 'correct' | 'wrong' | 'missed' = 'idle';
          if (revealed) {
            if (i === qs.answer) state = chosen === i ? 'correct' : 'missed';
            else if (chosen === i) state = 'wrong';
          } else if (chosen === i) state = 'selected';
          return <OptionButton key={i} label={LETTERS[i]} text={o} state={state} disabled={revealed}
            onClick={() => { setChosen(i); if (i !== qs.answer) store.addMistake({ key: `solved/${q.id}`, question: qs, chosen: i, from: 'Worked example', href: '', section: '', at: Date.now() }); }} />;
        })}
      </div>
      {!revealed ? (
        <button className="btn mt-3 text-sm" onClick={() => setShow(true)}>Show solution</button>
      ) : (
        <Explanation q={qs} />
      )}
    </div>
  );
}
