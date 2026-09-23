'use client';
import { useEffect, useState } from 'react';

/* Countdown to a fixed date string like "2026-09-30". Renders nothing until
   mounted so the static build never bakes a stale day count. */
export function CountdownChip({ date, label = 'Tier 1 starts' }: { date: string; label?: string }) {
  const [text, setText] = useState<string | null>(null);
  useEffect(() => {
    const target = new Date(`${date}T00:00:00+05:30`).getTime();
    const days = Math.ceil((target - Date.now()) / 86400000);
    setText(days > 1 ? `in ${days} days` : days === 1 ? 'tomorrow' : days === 0 ? 'is today' : 'is on');
  }, [date]);
  if (!text) return null;
  return (
    <span className="chip chip-high" suppressHydrationWarning>
      ⏳ {label} {text}
    </span>
  );
}
