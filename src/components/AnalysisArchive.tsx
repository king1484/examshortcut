import Link from 'next/link';
import { dayLabel, daySlug, type ShiftDay, type ShiftExam } from '@/lib/shifts';
import { archiveDates } from '@/lib/shiftArchive';

export function AnalysisArchive({ exam, days }: { exam: ShiftExam; days: ShiftDay[] }) {
  const byDate = new Map(days.map(day => [day.date, day]));
  const dates = archiveDates(exam.window.start, days.map(day => day.date));
  const months = [...new Set(dates.map(date => date.slice(0, 7)))];
  return <section className="analysis-archive" aria-label={`${exam.short} analysis archive`}>
    <div className="analysis-archive-heading">
      <div><p className="kicker">Browse by date</p><h2 className="text-xl font-extrabold">Every report, from {dayLabel(exam.window.start, false)}</h2></div>
      <span className="text-sm muted">{days.length} days with reports</span>
    </div>
    {months.map(month => <div key={month} className="mt-5">
      <h3 className="text-sm font-bold mb-2">{new Date(`${month}-01T00:00:00Z`).toLocaleDateString('en-IN', { month: 'long', year: 'numeric', timeZone: 'UTC' })}</h3>
      <div className="analysis-date-grid">
        {dates.filter(date => date.startsWith(month)).map(date => {
          const day = byDate.get(date);
          const reports = day?.shifts.filter(shift => shift.status === 'reported' || shift.status === 'partial').length ?? 0;
          const label = !day ? 'No report' : reports ? `${reports} shift${reports === 1 ? '' : 's'} covered` : day.shifts.every(shift => shift.status === 'not-held') ? 'Not held' : 'Awaiting sources';
          const content = <><span className="font-extrabold">{dayLabel(date, false)}</span><span className="text-xs muted">{label}</span></>;
          return day ? <Link key={date} href={`/exam-analysis/${exam.slug}/${daySlug(date)}/`} className="analysis-date" aria-label={`${dayLabel(date)} — ${label}`}>{content}</Link>
            : <div key={date} className="analysis-date analysis-date-empty">{content}</div>;
        })}
      </div>
    </div>)}
    <p className="text-xs muted mt-4">“No report” means there is no published coverage here. It does not confirm that an exam was held or cancelled.</p>
  </section>;
}
