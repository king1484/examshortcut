import type { Metadata } from 'next';
import Link from 'next/link';
import { ExamBasicsList, ExamPicker, SelectedExamPanel } from '@/components/ExamPicker';
import { EXAMS } from '@/lib/exams';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: "Choose your exam — India's 10 most-applied govt & entrance exams",
  description: 'SSC CGL, CHSL, MTS, GD, RRB NTPC, Group D, CTET, NEET UG, JEE Main and CUET UG — conducting body, eligibility, stages and applicant numbers, with notes, practice and tracking.',
  alternates: { canonical: '/exams/' },
};

export default function ExamsPage() {
  const live = EXAMS.filter((e) => e.status === 'live');
  const soon = EXAMS.filter((e) => e.status === 'soon');
  return (
    <div className="max-w-5xl mx-auto space-y-6">
      <div>
        <h1 className="text-3xl sm:text-4xl font-extrabold">Exams</h1>
        <p className="muted mt-2 max-w-3xl">
          Most government and entrance exams test the same core subjects — maths, reasoning, English and general
          awareness. Choose your exam and ExamShortcut shows the subjects it tests, and tracks your preparation for it.
        </p>
      </div>
      <SelectedExamPanel />
      <ExamPicker />
      <section>
        <h2 className="text-xl font-extrabold">Full exam hubs</h2>
        <p className="text-sm muted">Pattern, cutoffs, full mocks, score calculator and planners.</p>
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
        <h2 className="text-xl font-extrabold">Coming soon</h2>
        <p className="text-sm muted">India&apos;s most-applied written exams. Full hubs (pattern, cutoffs, mocks) are on the way — the basics for now.</p>
        <div className="grid sm:grid-cols-2 gap-2.5 mt-3">
          {soon.map((e) => (
            <div key={e.id} className="card p-4">
              <span className="flex items-center gap-2">
                <span className="font-extrabold">{e.name}</span>
                <span className="chip chip-low ml-auto" style={{ fontSize: 10 }}>soon</span>
              </span>
              <span className="block text-sm muted mt-1">{e.blurb}</span>
              <ExamBasicsList exam={e} className="mt-3" />
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
