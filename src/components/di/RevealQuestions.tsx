'use client';
import { useId, useState } from 'react';

export type RevealItem = { q: string; a: string; sol: string };

/* Reveal-on-click practice questions. Answers are computed by the (server) caller
   from the same data that draws the chart, then passed in as plain strings. */
export function RevealQuestions({ items }: { items: RevealItem[] }) {
  const base = useId();
  const [open, setOpen] = useState<Record<number, boolean>>({});

  return (
    <ol className="mt-3 space-y-2.5 list-none p-0">
      {items.map((it, i) => {
        const isOpen = !!open[i];
        const panelId = `${base}-${i}`;
        return (
          <li key={i} className="rounded-xl p-3.5" style={{ background: 'var(--surface-2)', border: '1px solid var(--line)' }}>
            <p className="text-sm font-semibold">
              <span style={{ color: 'var(--brand-text)' }}>Q{i + 1}.</span> {it.q}
            </p>
            <button
              type="button"
              className="btn mt-2 text-xs"
              aria-expanded={isOpen}
              aria-controls={panelId}
              onClick={() => setOpen((o) => ({ ...o, [i]: !o[i] }))}
            >
              {isOpen ? 'Hide answer' : 'Show answer'}
            </button>
            <div id={panelId} hidden={!isOpen} className="mt-2.5 text-sm">
              {isOpen && (
                <>
                  <p>
                    <span className="font-bold" style={{ color: 'var(--ok)' }}>Answer: </span>
                    <span className="font-semibold">{it.a}</span>
                  </p>
                  <p className="muted mt-1">
                    <span className="font-bold">Shortcut: </span>{it.sol}
                  </p>
                </>
              )}
            </div>
          </li>
        );
      })}
    </ol>
  );
}
