import type { Metadata } from 'next';
import Link from 'next/link';
import { ExamPicker } from '@/components/ExamPicker';
import { EXAMS } from '@/lib/exams';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: "Choose your exam — SSC, Railway, Banking & CAT",
  description: 'SSC CGL, CHSL, MTS, GD, CPO, RRB NTPC, RRB Group D, IBPS PO, IBPS Clerk and CAT — pattern, eligibility, posts, selection process and FAQs, with shared maths, reasoning, English and GA notes, practice and tracking.',
  alternates: { canonical: '/exams/' },
};

export default function ExamsPage() {
  const live = EXAMS.filter((e) => e.status === 'live');
  return (
    <div className="max-w-5xl mx-auto space-y-6">
      <div>
        <h1 className="text-2xl sm:text-4xl font-extrabold">Exams</h1>
        <p className="muted mt-2 max-w-3xl">
          Choose your exam to see the subjects it tests and track your preparation.
        </p>
      </div>
      <ExamPicker />
      <section>
        <h2 className="text-xl font-extrabold">Full exam hubs</h2>
        <p className="text-sm muted">Pattern, eligibility, posts and pay, selection process, FAQs and mocks.</p>
        <div className="grid sm:grid-cols-2 gap-2.5 mt-3">
          {live.map((e) => (
            <Link key={e.id} href={`/exams/${e.id}/`} className="card p-4 hover:-translate-y-0.5 transition-transform">
              <span className="font-extrabold">{e.name} →</span>
              <span className="block text-sm muted mt-1">{e.blurb}</span>
            </Link>
          ))}
        </div>
      </section>
      <section>
        <h2 className="text-xl font-extrabold">One syllabus, many exams</h2>
        <p className="text-sm muted mt-1 max-w-3xl">
          SSC, Railway, Banking and CAT exams mostly test the same core subjects: maths, reasoning, English and general
          awareness. Notes and practice are shared, so what you study for one exam counts for the others.
        </p>
      </section>
    </div>
  );
}
