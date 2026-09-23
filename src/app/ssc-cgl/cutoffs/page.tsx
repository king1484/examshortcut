import type { Metadata } from 'next';
import { getCutoffs } from '@/lib/content';
import { Md } from '@/components/Md';
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
  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">SSC CGL cutoffs, year by year</h1>
      <Md className="mt-2 text-[15px]">{data.notes}</Md>
      <CutoffExplorer data={data} />
    </div>
  );
}
