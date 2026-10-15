import { CglToolDepth } from '@/components/exam-pages/CglToolDepth';
import type { Metadata } from 'next';
import Link from 'next/link';
import { getCutoffs } from '@/lib/content';
import { MarksCalculator } from '@/components/MarksCalculator';

export const dynamic = 'force-static';
const TITLE = 'SSC CGL marks calculator from response sheet (private, in your browser)';
const DESC = 'Read your saved SSC CGL response sheet in the browser: marks with negative marking, section-wise correct, wrong and skipped, and a question-by-question view. Nothing is uploaded.';
export const metadata: Metadata = { title: TITLE, description: DESC, openGraph: { title: TITLE, description: DESC } };

export default function MarksCalculatorPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL marks calculator from your response sheet</h1>
      <p className="muted mt-2">
        Save your response sheet, choose the file here, and get your marks, section-wise correct, wrong and skipped counts, and a question-by-question view. The file is read inside your browser and never leaves your device.
      </p>
      <MarksCalculator cutoffs={getCutoffs()} />
      <div className="card p-4 sm:p-5 mt-6">
        <div className="kicker">No response sheet?</div>
        <p className="text-sm muted mt-1">
          Use the <Link className="underline" href="/exams/ssc-cgl/score-calculator/">score calculator</Link> to enter your counts by hand, or check <Link className="underline" href="/exams/ssc-cgl/cutoffs/">past cutoffs</Link>. The <Link className="underline" href="/exam-analysis/">shift-wise analysis</Link> shows how hard each shift was.
        </p>
      </div>
      <CglToolDepth kind="marks" />
    </div>
  );
}
