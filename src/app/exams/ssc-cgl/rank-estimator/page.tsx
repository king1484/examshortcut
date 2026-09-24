import type { Metadata } from 'next';
import { getCutoffs } from '@/lib/content';
import { RankEstimator } from '@/components/RankEstimator';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL rank & percentile estimator',
  description: 'Enter your expected SSC CGL Tier 1 marks to get an estimated percentile and all-India rank, anchored on official category-wise cutoffs, plus how far you are from the shortlist.',
};

export default function RankEstimatorPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">Rank &amp; percentile estimator</h1>
      <p className="muted mt-2">Tier 1 marks → estimated percentile and all-India rank, anchored on official cutoffs, with the marks-vs-cutoff call for your category.</p>
      <RankEstimator cutoffs={getCutoffs()} />
    </div>
  );
}
