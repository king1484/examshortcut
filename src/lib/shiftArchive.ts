/** Include gaps explicitly without inventing reports or claiming an exam was held. */
export function archiveDates(start: string, publishedDates: string[]): string[] {
  const latest = [...publishedDates].sort().at(-1);
  if (!latest || start > latest) return [];
  const dates: string[] = [];
  const day = new Date(`${start}T00:00:00Z`);
  while (Number.isFinite(day.getTime()) && day.toISOString().slice(0, 10) <= latest) {
    dates.push(day.toISOString().slice(0, 10));
    day.setUTCDate(day.getUTCDate() + 1);
  }
  return dates;
}
