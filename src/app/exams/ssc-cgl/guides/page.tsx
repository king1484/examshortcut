import Link from 'next/link';
import type { Metadata } from 'next';
import { listGuides } from '@/lib/content';
import { CglGuidesDepth } from '@/components/exam-pages/PlanDepth';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL preparation guides: strategy, study plans, books, Tier 2',
  description: 'Free SSC CGL preparation guides: overall strategy, 30, 60 and 90 day study plans, best books by section, Tier 2 strategy and CGL vs CHSL.',
};

export default function GuidesIndex() {
  const guides = listGuides();
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL preparation guides</h1>
      <p className="muted mt-2">Plans and strategy that link straight to the notes, formula sheets and mocks on this site.</p>
      <div className="grid sm:grid-cols-2 gap-3 mt-6">
        {guides.map((g) => (
          <Link key={g.id} href={`/exams/ssc-cgl/guides/${g.id}/`} className="card p-4 sm:p-5 hover:-translate-y-0.5 transition-transform">
            <h2 className="font-bold leading-snug">{g.title}</h2>
            <p className="text-sm muted mt-1">{g.description}</p>
          </Link>
        ))}
      </div>
      {guides.length === 0 && <p className="card p-6 mt-6 muted">Guides are being written. Check back shortly.</p>}
      <CglGuidesDepth />
    </div>
  );
}
