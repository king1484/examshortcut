import Link from 'next/link';
import type { Metadata } from 'next';
import { getCutoffs } from '@/lib/content';
import { Md } from '@/components/Md';
import { splitLead } from '@/lib/lead';
import { CutoffExplorer } from '@/components/CutoffExplorer';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL cutoffs — year-wise & category-wise official trends',
  description: 'SSC CGL Tier 1, Tier 2 and final cutoffs year by year for UR, EWS, OBC, SC, ST and more, straight from SSC result notices — with trend charts and what score is actually safe.',
};

export default function CutoffsPage() {
  const data = getCutoffs();
  if (!data) {
    return <div className="card p-8 text-center max-w-2xl mx-auto"><h1 className="text-2xl font-extrabold">Cutoff data is being compiled</h1><p className="muted mt-2">Check back shortly.</p></div>;
  }
  const notes = splitLead(typeof data.notes === 'string' ? data.notes : '');
  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL cutoffs, year by year</h1>
      <Md className="mt-2 text-[15px]">{notes.lead}</Md>
      <CutoffExplorer data={data} />
      <div className="mt-8">
        <div className="kicker">Cutoff pages</div>
        <div className="flex flex-wrap gap-2 mt-2">
          {[...new Set(((data.tier1 ?? []) as { year: number }[]).map((l) => l.year))].sort((a, b) => b - a).map((y) => (
            <Link key={y} href={`/exams/ssc-cgl/cutoffs/${y}/`} className="chip">{y} Tier 1</Link>
          ))}
          {(data.final ?? []).length > 0 && <Link href="/exams/ssc-cgl/cutoffs/final-merit/" className="chip">Final merit (out of 390)</Link>}
          <Link href="/exams/ssc-cgl/cutoffs/expected-2026/" className="chip">Expected 2026</Link>
        </div>
      </div>
      {notes.rest && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">About these figures</h2>
          <Md className="mt-2 text-[15px] muted">{notes.rest}</Md>
        </>
      )}
    </div>
  );
}
