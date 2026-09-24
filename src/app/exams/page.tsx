import type { Metadata } from 'next';
import Link from 'next/link';
import { ExamPicker, SelectedExamPanel } from '@/components/ExamPicker';
import { EXAMS } from '@/lib/exams';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Choose your exam — SSC, Railway, Banking, Defence & entrance exams',
  description: 'Pick the exam you are preparing for: SSC CGL, CHSL, MTS, GD, CPO, RRB NTPC, Group D, IBPS PO, SBI PO, IBPS Clerk, CDS, CUET. Free notes, practice and tracking for each.',
  alternates: { canonical: '/exams/' },
};

export default function ExamsPage() {
  const live = EXAMS.filter((e) => e.status === 'live');
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
    </div>
  );
}
