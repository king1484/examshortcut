'use client';
import { useEffect, useState } from 'react';

export type CalEvent = {
  id: string; title: string; start: string; end?: string;
  status: 'done' | 'confirmed' | 'expected'; note?: string; countdown?: boolean;
};

const DAY = 86400000;
const d = (iso: string) => new Date(`${iso}T00:00:00`);
const fmt = (iso: string) => d(iso).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
const ymd = (iso: string) => iso.replaceAll('-', '');
const nextDay = (iso: string) => new Date(d(iso).getTime() + DAY + 12 * 3600000).toISOString().slice(0, 10);

function ics(events: CalEvent[]) {
  const stamp = new Date().toISOString().replace(/[-:]/g, '').slice(0, 15) + 'Z';
  const lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//ExamShortcut//SSC CGL//EN', 'CALSCALE:GREGORIAN'];
  for (const e of events) {
    lines.push(
      'BEGIN:VEVENT',
      `UID:ssc-cgl-${e.id}@examshortcut.in`,
      `DTSTAMP:${stamp}`,
      `DTSTART;VALUE=DATE:${ymd(e.start)}`,
      `DTEND;VALUE=DATE:${ymd(nextDay(e.end ?? e.start))}`,
      `SUMMARY:SSC CGL: ${e.title}${e.status === 'expected' ? ' (expected)' : ''}`,
      `DESCRIPTION:${(e.note ?? '').replace(/[,;]/g, (c) => '\\' + c)} Check ssc.gov.in for the official notice.`,
      'END:VEVENT',
    );
  }
  lines.push('END:VCALENDAR');
  return lines.join('\r\n');
}

function download(events: CalEvent[], name: string) {
  const url = URL.createObjectURL(new Blob([ics(events)], { type: 'text/calendar' }));
  const a = document.createElement('a'); a.href = url; a.download = name; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function gcal(e: CalEvent) {
  const q = new URLSearchParams({
    action: 'TEMPLATE', text: `SSC CGL: ${e.title}`,
    dates: `${ymd(e.start)}/${ymd(nextDay(e.end ?? e.start))}`,
    details: `${e.note ?? ''} Check ssc.gov.in for the official notice.`,
  });
  return `https://calendar.google.com/calendar/render?${q}`;
}

const STATUS = {
  done: { label: 'Done', color: 'var(--ink-3)' },
  confirmed: { label: 'Confirmed', color: 'var(--ok)' },
  expected: { label: 'Expected', color: 'var(--warn)' },
};

export function ExamCalendar({ events }: { events: CalEvent[] }) {
  const [now, setNow] = useState<number | null>(null);
  useEffect(() => {
    setNow(Date.now());
    const t = setInterval(() => setNow(Date.now()), 60000);
    return () => clearInterval(t);
  }, []);

  const today = now ? new Date(new Date(now).toDateString()).getTime() : null;
  const phase = (e: CalEvent) => {
    if (today == null) return e.status === 'done' ? 'past' : 'future';
    const s = d(e.start).getTime(), en = d(e.end ?? e.start).getTime();
    return en < today ? 'past' : s <= today ? 'live' : 'future';
  };
  const upcoming = events.filter((e) => e.countdown && phase(e) !== 'past');

  return (
    <div>
      {now != null && upcoming.length > 0 && (
        <div className="grid sm:grid-cols-2 gap-4">
          {upcoming.map((e) => {
            const days = Math.ceil((d(e.start).getTime() - (today as number)) / DAY);
            const live = phase(e) === 'live';
            return (
              <div key={e.id} className="card p-5 text-center">
                <div className="text-xs font-bold uppercase tracking-wide faint">{e.title}</div>
                <div className="text-5xl font-extrabold mt-2" style={{ color: 'var(--brand)' }}>{live ? 'LIVE' : days}</div>
                <div className="text-sm muted mt-1">
                  {live ? `Running till ${fmt(e.end as string)}` : `day${days === 1 ? '' : 's'} to go · ${fmt(e.start)}`}
                  {e.status === 'expected' && ' (expected)'}
                </div>
              </div>
            );
          })}
        </div>
      )}

      <div className="flex flex-wrap gap-2 mt-5">
        <button className="btn btn-brand text-sm" onClick={() => download(events.filter((e) => phase(e) !== 'past'), 'ssc-cgl-2026.ics')}>
          📅 Add all upcoming dates to my calendar (.ics)
        </button>
      </div>
      <p className="text-xs faint mt-1">Works with Google Calendar, Outlook and Apple Calendar. Re-download it when dates are confirmed. The same event IDs update the entries instead of duplicating them.</p>

      <ol className="mt-6 relative border-l-2 ml-2" style={{ borderColor: 'var(--line)' }}>
        {events.map((e) => {
          const ph = phase(e);
          const st = STATUS[e.status];
          return (
            <li key={e.id} className="ml-5 mb-5" style={{ opacity: ph === 'past' ? 0.6 : 1 }}>
              <span className="absolute -left-[7px] w-3 h-3 rounded-full mt-1.5"
                style={{ background: ph === 'live' ? 'var(--brand)' : ph === 'past' ? 'var(--line)' : st.color }} />
              <div className="text-xs font-semibold" style={{ color: st.color }}>
                {fmt(e.start)}{e.end ? ` – ${fmt(e.end)}` : ''} · {ph === 'live' ? 'Happening now' : st.label}
              </div>
              <div className="font-bold mt-0.5">{e.title}</div>
              {e.note && <div className="text-sm muted mt-0.5">{e.note}</div>}
              {ph !== 'past' && (
                <a className="text-xs underline decoration-dotted mt-1 inline-block" href={gcal(e)} target="_blank" rel="noopener noreferrer">+ Google Calendar</a>
              )}
            </li>
          );
        })}
      </ol>
    </div>
  );
}
