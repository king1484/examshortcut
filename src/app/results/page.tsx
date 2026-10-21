import type { Metadata } from 'next';
import Link from 'next/link';
import { listExamUpdates } from '@/lib/examUpdates';
import { ExamUpdateBrowser } from '@/components/ExamUpdateBrowser';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Latest exam results: SSC, SBI, IBPS and UP Police',
  description: 'Published exam results with official PDFs, recruitment-cycle details, shortlist versus final-selection status, and next steps for candidates.',
  alternates: { canonical: '/results/' },
};
export default function ResultsPage() {
  return <div className="max-w-5xl mx-auto exam-updates">
    <p className="text-sm font-bold" style={{ color: 'var(--brand-text)' }}>Official releases explained</p>
    <h1 className="text-3xl sm:text-5xl font-extrabold mt-2">Exam results</h1>
    <p className="muted mt-4 max-w-3xl">Check which stage you cleared, open the official result and understand what follows. A physical-test or interview shortlist is labelled separately from final selection. Match the recruitment year and advertisement number before checking your roll number.</p>
    <Link href="/exam-updates/" className="btn mt-5">All results, admit cards and exam notices →</Link>
    <ExamUpdateBrowser items={listExamUpdates().filter(item => item.kind === 'result')} resultsOnly />
  </div>;
}
