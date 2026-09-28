'use client';
import { useEffect, useState } from 'react';

/* Countdown to a fixed date string like "2026-09-30". Renders nothing until
   mounted so the static build never bakes a stale day count. With `end`, shows
   "underway" between the dates and disappears once the window is over. */
export function CountdownChip({ date, end, label = 'Tier 1' }: { date: string; end?: string; label?: string }) {
  const [text, setText] = useState<string | null>(null);
  useEffect(() => {
    const ist = (d: string) => new Date(`${d}T00:00:00+05:30`).getTime();
    const now = Date.now();
    const days = Math.ceil((ist(date) - now) / 86400000);
    if (days > 0) setText(`⏳ ${label} starts ${days === 1 ? 'tomorrow' : `in ${days} days`}`);
    else if (end && now < ist(end) + 86400000) setText(`🟢 ${label} underway`);
    else if (!end && days === 0) setText(`🟢 ${label} starts today`);
    else setText(null);
  }, [date, end, label]);
  if (!text) return null;
  return <span className="chip chip-brand" suppressHydrationWarning>{text}</span>;
}
