import { CglToolDepth } from '@/components/exam-pages/CglToolDepth';
import type { Metadata } from 'next';
import { getCutoffs } from '@/lib/content';
import { ScoreCalculator } from '@/components/ScoreCalculator';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL score calculator & historical cutoff comparison',
  description: 'Enter your correct/wrong counts per section to get your SSC CGL score with negative marking, compare against official cutoffs by category, and see what to push.',
};

export default function ScoreCalculatorPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">Score calculator &amp; cutoff comparison</h1>
      <p className="muted mt-2">Counts per section → your net score with negative marking, your attempt strategy, and how far you are from recent official cutoffs.</p>
      <ScoreCalculator cutoffs={getCutoffs()} />
      <CglToolDepth kind="score" />
    </div>
  );
}
