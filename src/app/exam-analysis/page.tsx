import type { Metadata } from 'next';
import Link from 'next/link';
import { ExamAnalysisGuide } from '@/components/ExamAnalysisGuide';
import { AnalysisArchive } from '@/components/AnalysisArchive';
import { dayLabel, daySlug, listShiftDays, listShiftExams } from '@/lib/shifts';

export const dynamic = 'force-static';

export const metadata: Metadata = {
  title: 'Exam Analysis Today — Shift-wise Difficulty, Good Attempts, Questions Asked',
  description: 'Shift-wise exam analysis for SSC and other government exams: difficulty level, good attempts, section-wise topics and memory-based questions, updated after every shift.',
};

export default function ExamAnalysisIndex() {
  const exams = listShiftExams().map((e) => ({ e, days: listShiftDays(e.slug) }));
  return (
    <div className="max-w-3xl mx-auto analysis-page">
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-4">Exam analysis — shift by shift</h1>
      <p className="muted mt-2 text-[15px]">Candidate-reported difficulty, attempt ranges and recalled topics, added as sources become available. These are unofficial study references, not safe-score predictions.</p>
      <div className="space-y-4 mt-6">
        {exams.map(({ e, days }) => (
          <section key={e.slug} className="card p-5">
            <h2 className="text-xl font-extrabold"><Link href={`/exam-analysis/${e.slug}/`} className="hover:underline">{e.name}</Link></h2>
            <p className="text-xs faint mt-0.5">{dayLabel(e.window.start)} – {dayLabel(e.window.end)}</p>
            {days[0] && <Link className="btn btn-brand mt-4" href={`/exam-analysis/${e.slug}/${daySlug(days[0].date)}/`}>Latest report · {dayLabel(days[0].date, false)} →</Link>}
            <AnalysisArchive exam={e} days={days} />
            <Link className="text-sm font-bold underline mt-5 inline-block" href={`/exam-analysis/${e.slug}/`}>View the full shift archive →</Link>
          </section>
        ))}
      </div>
      <ExamAnalysisGuide />
    </div>
  );
}
