'use client';
import { useEffect, useState, type ReactNode } from 'react';

/* Date-aware content for a static site: the server renders every phase, this picks the one
   whose `from` date (IST) has passed. Before mount it shows phase 0 — the text as of build day. */
export function DatePhases({ phases }: { phases: { from?: string; node: ReactNode }[] }) {
  const [idx, setIdx] = useState(0);
  useEffect(() => {
    const now = Date.now();
    let i = 0;
    phases.forEach((p, n) => {
      if (p.from && new Date(`${p.from}T00:00:00+05:30`).getTime() <= now) i = n;
    });
    setIdx(i);
  }, [phases]);
  return <>{phases[idx]?.node}</>;
}
