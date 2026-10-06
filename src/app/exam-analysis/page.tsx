import type { Metadata } from 'next';
import Link from 'next/link';
import { dayLabel, daySlug, listShiftDays, listShiftExams } from '@/lib/shifts';

export const dynamic = 'force-static';

export const metadata: Metadata = {
  title: 'Exam Analysis Today — Shift-wise Difficulty, Good Attempts, Questions Asked',
  description: 'Shift-wise exam analysis for SSC and other government exams: difficulty level, good attempts, section-wise topics and memory-based questions, updated after every shift.',
};

export default function ExamAnalysisIndex() {
  const exams = listShiftExams().map((e) => ({ e, days: listShiftDays(e.slug) }));
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-4">Exam analysis — shift by shift</h1>
      <p className="muted mt-2 text-[15px]">How each shift went, straight after it ends: difficulty, safe attempts, and the topics and questions candidates recall. Use it to calibrate before your own shift.</p>
      <div className="space-y-4 mt-6">
        {exams.map(({ e, days }) => (
          <section key={e.slug} className="card p-5">
            <h2 className="text-xl font-extrabold"><Link href={`/exam-analysis/${e.slug}/`} className="hover:underline">{e.name}</Link></h2>
            <p className="text-xs faint mt-0.5">{dayLabel(e.window.start)} – {dayLabel(e.window.end)}</p>
            {days.length > 0 && (
              <div className="flex flex-wrap gap-2 mt-3">
                {days.slice(0, 8).map((d) => <Link key={d.date} className="chip hover:underline" href={`/exam-analysis/${e.slug}/${daySlug(d.date)}/`}>{dayLabel(d.date, false)}</Link>)}
              </div>
            )}
          </section>
        ))}
      </div>
    </div>
  );
}
