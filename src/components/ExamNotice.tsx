'use client';
import Link from 'next/link';
import { useEffect, useState } from 'react';

const ist = (d: string) => new Date(`${d}T00:00:00+05:30`).getTime();
const DAY = 86400000;
const short = (d: string) => new Date(ist(d)).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', timeZone: 'Asia/Kolkata' });

function text(exam: string, stage: string, start: string, end: string, now: number): string | null {
  const days = Math.ceil((ist(start) - now) / DAY);
  if (days > 1) return `${exam} ${stage} starts in ${days} days`;
  if (days === 1) return `${exam} ${stage} starts tomorrow`;
  if (now < ist(end) + DAY) return `${exam} ${stage} is underway · till ${short(end)}`;
  if (now < ist(end) + 45 * DAY) return `${exam} ${stage} is over · result & next stage awaited`;
  return null;
}

/* One-line, date-aware exam alert for the homepage. Renders the build-day text, then
   recomputes from the visitor's clock; disappears 45 days after the window closes. */
export function ExamNotice({ exam, stage, start, end, href, builtAt, latest }: {
  exam: string; stage: string; start: string; end: string; href: string; builtAt: number;
  latest?: { message: string; afterMessage: string; endsAt: string; href: string };
}) {
  const [now, setNow] = useState(builtAt);
  useEffect(() => setNow(Date.now()), []);
  const t = text(exam, stage, start, end, now);
  if (!t) return null;
  const message = latest ? (now <= Date.parse(latest.endsAt) ? latest.message : latest.afterMessage) : t;
  return (
    <Link href={latest?.href ?? href} className="notice-pill">
      <span className="notice-dot" aria-hidden />
      <span className="notice-copy">{message}</span>
      <span className="notice-cta" aria-hidden="true"><span className="hidden sm:inline">{latest ? 'See notice' : 'See timeline'}</span><svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" /></svg></span>
    </Link>
  );
}
