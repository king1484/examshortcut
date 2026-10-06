'use client';

export type EventRow = {
  id: string; title: string; start: string; end?: string;
  status: 'done' | 'confirmed' | 'expected'; note?: string;
};

const DAY = 86400000;
const d = (iso: string) => new Date(`${iso}T00:00:00Z`);
const fmt = (iso: string) => d(iso).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' });
const ymd = (iso: string) => iso.replaceAll('-', '');
const nextDay = (iso: string) => new Date(d(iso).getTime() + DAY).toISOString().slice(0, 10);
const range = (e: EventRow) => (e.end && e.end !== e.start ? `${fmt(e.start)} to ${fmt(e.end)}` : fmt(e.start));

const STATUS = {
  done: { label: 'Done', color: 'var(--ink-3)' },
  confirmed: { label: 'Confirmed', color: 'var(--ok)' },
  expected: { label: 'Expected', color: 'var(--warn)' },
};

function gcal(name: string, portal: string, e: EventRow) {
  const q = new URLSearchParams({
    action: 'TEMPLATE',
    text: `${name}: ${e.title}${e.status === 'expected' ? ' (expected)' : ''}`,
    dates: `${ymd(e.start)}/${ymd(nextDay(e.end ?? e.start))}`,
    details: `${e.note ?? ''} Check ${portal} for the official notice.`.trim(),
  });
  return `https://calendar.google.com/calendar/render?${q}`;
}

function ics(name: string, slug: string, portal: string, events: EventRow[]) {
  const stamp = new Date().toISOString().replace(/[-:]/g, '').slice(0, 15) + 'Z';
  const lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', `PRODID:-//ExamShortcut//${name}//EN`, 'CALSCALE:GREGORIAN'];
  for (const e of events) {
    lines.push(
      'BEGIN:VEVENT',
      `UID:${slug}-${e.id}@examshortcut.in`,
      `DTSTAMP:${stamp}`,
      `DTSTART;VALUE=DATE:${ymd(e.start)}`,
      `DTEND;VALUE=DATE:${ymd(nextDay(e.end ?? e.start))}`,
      `SUMMARY:${name}: ${e.title}${e.status === 'expected' ? ' (expected)' : ''}`,
      `DESCRIPTION:${(e.note ?? '').replace(/[,;]/g, (c) => '\\' + c)} Check ${portal} for the official notice.`,
      'END:VEVENT',
    );
  }
  lines.push('END:VCALENDAR');
  return lines.join('\r\n');
}

function download(name: string, slug: string, portal: string, events: EventRow[]) {
  const url = URL.createObjectURL(new Blob([ics(name, slug, portal, events)], { type: 'text/calendar' }));
  const a = document.createElement('a');
  a.href = url;
  a.download = `${slug}-dates.ics`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

/** Dates table with one-click add to Google Calendar and a .ics download. Rendered on the server too, so the table is in the HTML. */
export function ExamEvents({ name, slug, portal, events }: { name: string; slug: string; portal: string; events: EventRow[] }) {
  const upcoming = events.filter((e) => e.status !== 'done');
  return (
    <div className="mt-6">
      <div className="tbl-wrap">
        <table className="tbl">
          <thead><tr><th>Date</th><th>Event</th><th>Status</th><th className="text-right">Reminder</th></tr></thead>
          <tbody>
            {events.map((e) => (
              <tr key={e.id}>
                <td className="whitespace-nowrap font-semibold">{range(e)}</td>
                <td>
                  {e.title}
                  {e.note && <div className="text-xs faint mt-0.5">{e.note.replaceAll('*', '')}</div>}
                </td>
                <td><span className="chip" style={{ color: STATUS[e.status].color }}>{STATUS[e.status].label}</span></td>
                <td className="text-right">
                  {e.status !== 'done' && (
                    <a href={gcal(name, portal, e)} target="_blank" rel="noopener noreferrer" className="text-xs underline decoration-dotted">Add to Google Calendar</a>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {upcoming.length > 0 && (
        <button type="button" className="chip chip-brand mt-3" onClick={() => download(name, slug, portal, upcoming)}>
          Download upcoming dates (.ics)
        </button>
      )}
    </div>
  );
}
