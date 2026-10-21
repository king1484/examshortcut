import type { Metadata } from 'next';
import Link from 'next/link';
import { listExamUpdates } from '@/lib/examUpdates';
import { ExamUpdateBrowser } from '@/components/ExamUpdateBrowser';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Latest exam updates: results, admit cards, answer keys and dates',
  description: 'Verified exam results and notices for SSC, SBI, IBPS, Railways, CAT and UP Police. Find the recruitment cycle, official source, next steps and checked date.',
  alternates: { canonical: '/exam-updates/', types: { 'application/rss+xml': '/exam-updates.xml' } },
};
export default function ExamUpdatesPage() {
  const items = listExamUpdates();
  return <div className="max-w-5xl mx-auto exam-updates">
    <p className="font-bold text-sm" style={{ color: 'var(--brand-text)' }}>Results &amp; notices</p>
    <h1 className="text-3xl sm:text-5xl font-extrabold mt-2">What changed in your exam?</h1>
    <p className="muted mt-4 max-w-3xl">Results, official exam dates and the next step to take. Every update names the recruitment cycle, links to its official notice and shows when we checked it.</p>
    <nav className="flex flex-wrap gap-3 mt-5" aria-label="Exam update sections"><Link className="btn" href="/results/">Published results →</Link><Link className="btn" href="/answer-keys/">Answer keys &amp; response sheets</Link><Link className="btn" href="/exam-analysis/">Shift analysis</Link><a className="btn" href="/exam-updates.xml">RSS feed</a></nav>
    <ExamUpdateBrowser items={items} />
    <p className="text-sm muted mt-8">We publish an update after finding usable official evidence. A future date is a schedule, not proof that a result or download is available. <Link href="/editorial-policy/" className="underline">How we check content</Link>.</p>
  </div>;
}
