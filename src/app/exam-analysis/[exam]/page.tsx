import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { dayLabel, daySlug, difficultyColor, getShiftExam, hasAnalysis, listShiftDays, listShiftExams, shiftLabel, shiftSlug } from '@/lib/shifts';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return listShiftExams().map((e) => ({ exam: e.slug }));
}

type Params = { params: Promise<{ exam: string }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { exam: slug } = await params;
  const exam = getShiftExam(slug);
  if (!exam) return {};
  const title = `${exam.name} Exam Analysis — Shift-wise Difficulty, Good Attempts, Questions Asked`;
  const description = `Day-by-day, shift-by-shift ${exam.name} exam analysis (${dayLabel(exam.window.start)} – ${dayLabel(exam.window.end)}): difficulty level, good attempts, section-wise topics and memory-based questions, updated after every shift.`;
  return { title: { absolute: title }, description, openGraph: { title, description }, twitter: { card: 'summary_large_image', title, description } };
}

export default async function ExamShiftHub({ params }: Params) {
  const { exam: slug } = await params;
  const exam = getShiftExam(slug);
  if (!exam) notFound();
  const days = listShiftDays(slug);

  return (
    <div className="max-w-3xl mx-auto">
      <nav className="text-xs faint mt-4"><Link href="/exam-analysis/" className="underline decoration-dotted">Exam analysis</Link> / {exam.short}</nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-1">{exam.name} Exam Analysis — Shift-wise</h1>
      <p className="muted mt-2 text-[15px]">
        Reports from {dayLabel(exam.window.start)} to {dayLabel(exam.window.end)}: difficulty, unofficial attempt ranges and topics candidates remember. Updates depend on relevant sources being available.
        {exam.guide && <> New to the exam? Read the <Link href={exam.guide} className="underline">complete {exam.short} guide</Link>.</>}
      </p>

      {!!exam.pattern?.length && (
        <div className="card p-4 mt-5 grid grid-cols-2 sm:grid-cols-3 gap-3 text-sm">
          {exam.pattern.map((p) => <div key={p.label}><div className="text-xs uppercase faint font-bold">{p.label}</div><div className="font-semibold">{p.value}</div></div>)}
        </div>
      )}

      <div className="space-y-4 mt-8">
        {days.map((d) => (
          <section key={d.date} className="card p-4">
            <div className="flex items-baseline justify-between gap-2 flex-wrap">
              <h2 className="text-lg font-extrabold"><Link href={`/exam-analysis/${slug}/${daySlug(d.date)}/`} className="hover:underline">{dayLabel(d.date)}</Link></h2>
              <Link href={`/exam-analysis/${slug}/${daySlug(d.date)}/`} className="text-xs underline decoration-dotted">All shifts →</Link>
            </div>
            <div className="grid sm:grid-cols-3 gap-2 mt-3">
              {d.shifts.map((s) => (
                <Link key={s.shift} href={`/exam-analysis/${slug}/${shiftSlug(d.date, s.shift)}/`} className="p-3 rounded-lg border text-sm hover:-translate-y-0.5 transition-transform" style={{ borderColor: 'var(--line)', borderLeft: `3px solid ${hasAnalysis(s) ? difficultyColor(s.overall) : 'var(--line)'}` }}>
                  <div className="font-bold">Shift {s.shift}</div>
                  <div className="text-xs faint">{s.time}</div>
                  <div className="text-xs mt-1 font-semibold">{hasAnalysis(s) ? `${s.overall} · ${s.goodAttempts ?? '—'} attempts` : shiftLabel(s)}</div>
                </Link>
              ))}
            </div>
          </section>
        ))}
      </div>
      {exam.about && <p className="text-sm muted mt-8">{exam.about}</p>}
    </div>
  );
}
