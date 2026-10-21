import Link from 'next/link';
import type { Metadata } from 'next';
import { STUDY_GUIDES } from '@/lib/studyGuides';
import { AllExamPreparationLinks } from '@/components/ExamPreparationLinks';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Free study guides for competitive exam preparation',
  description: 'Free guides for all 15 portal exams: SSC, Railway, banking, CAT and UP Police. Worked learning checks, saved action checklists and beginner study routines.',
  alternates: { canonical: '/study-guides/' },
};

export default function StudyGuidesPage() {
  return (
    <div className="max-w-5xl mx-auto">
      <p className="kicker">Free resources · no login needed</p>
      <h1 className="text-3xl sm:text-5xl font-extrabold mt-2 leading-tight">Make your next study hour count</h1>
      <p className="muted mt-4 max-w-3xl">Pick the problem you face today. Each guide gives you a practical routine, small examples and a route into the lessons you need.</p>
      <a className="btn btn-brand mt-5" href="#exam-guides">Find my exam’s next-stage guide ↓</a>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-7">
        {STUDY_GUIDES.map((g) => (
          <Link href={`/study-guides/${g.slug}/`} key={g.slug} className="card p-5 flex flex-col hover:-translate-y-0.5 transition-transform">
            <span className="chip self-start">{g.audience}</span>
            <h2 className="text-lg font-bold mt-3 leading-snug">{g.title}</h2>
            <p className="text-sm muted mt-2 flex-1">{g.description}</p>
            <span className="text-sm font-semibold mt-4" style={{ color: 'var(--brand)' }}>Read the guide →</span>
          </Link>
        ))}
      </div>
      <AllExamPreparationLinks />
      <section className="card p-5 sm:p-7 mt-8">
        <h2 className="text-2xl font-extrabold">Turn a lesson into a revision schedule</h2>
        <p className="muted mt-2">Add topics you studied, get suggested review dates and download calendar reminders. Your saved list stays in this browser.</p>
        <Link className="btn btn-brand mt-4" href="/revision-planner/">Build my revision plan</Link>
      </section>
      <p className="text-sm muted mt-6">Already know your next topic? Open the <Link className="underline" href="/learn/">subject notes</Link> or the <Link className="underline" href="/exams/ssc-cgl/guides/">SSC CGL guides</Link>.</p>
    </div>
  );
}
