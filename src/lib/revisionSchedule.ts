export const REVIEW_OFFSETS = [1, 3, 7, 14] as const;

export function isCalendarDate(value: string): boolean {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const date = new Date(`${value}T00:00:00Z`);
  return Number.isFinite(date.getTime()) && date.toISOString().slice(0, 10) === value;
}

export function reviewDates(start: string): string[] {
  if (!isCalendarDate(start)) throw new Error('Choose a valid study date.');
  return REVIEW_OFFSETS.map((days) => {
    const date = new Date(`${start}T00:00:00Z`);
    date.setUTCDate(date.getUTCDate() + days);
    return date.toISOString().slice(0, 10);
  });
}

export interface RevisionTopic { id: string; title: string; start: string }
const escapeIcs = (s: string) => s.replaceAll('\\', '\\\\').replace(/\r?\n/g, '\\n').replaceAll(';', '\\;').replaceAll(',', '\\,');

// Fold by UTF-8 bytes, including the continuation space, as required by iCalendar.
function fold(line: string): string {
  let part = '', size = 0;
  const parts: string[] = [];
  for (const char of line) {
    const bytes = new TextEncoder().encode(char).length;
    if (size + bytes > 75) { parts.push(part); part = ' '; size = 1; }
    part += char; size += bytes;
  }
  parts.push(part);
  return parts.join('\r\n');
}

export function revisionCalendar(topics: RevisionTopic[], stamp = new Date()): string {
  const lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//ExamShortcut//Revision Planner//EN', 'CALSCALE:GREGORIAN'];
  for (const topic of topics) {
    reviewDates(topic.start).forEach((date, i) => {
      lines.push('BEGIN:VEVENT', `UID:${topic.id}-${date}@examshortcut.in`,
        `DTSTAMP:${stamp.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}Z$/, 'Z')}`,
        `DTSTART;VALUE=DATE:${date.replaceAll('-', '')}`,
        `SUMMARY:${escapeIcs(`Review ${topic.title} (${i + 1}/4)`)}`,
        `DESCRIPTION:${escapeIcs('Recall the idea with notes closed. Retry a few questions, then check and repair gaps. Suggested review date; adjust to your needs.')}`,
        'URL:https://examshortcut.in/revision-planner/', 'END:VEVENT');
    });
  }
  lines.push('END:VCALENDAR');
  return lines.map(fold).join('\r\n') + '\r\n';
}
