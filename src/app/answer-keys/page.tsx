import type { Metadata } from 'next';
import Link from 'next/link';
import { listExamUpdates } from '@/lib/examUpdates';
import { ExamUpdateBrowser } from '@/components/ExamUpdateBrowser';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Exam answer keys and response sheets: releases and objection deadlines',
  description: 'Official answer-key release notices, response-sheet links, challenge windows, objection fees and next steps. Match your exam cycle and stage before downloading.',
  alternates: { canonical: '/answer-keys/' },
};
export default function AnswerKeysPage() {
  return <div className="max-w-5xl mx-auto exam-updates">
    <p className="text-sm font-bold" style={{ color: 'var(--brand-text)' }}>Response sheets &amp; challenges</p>
    <h1 className="text-3xl sm:text-5xl font-extrabold mt-2">Answer keys</h1>
    <p className="muted mt-4 max-w-3xl">Find the official release, compare your recorded answers and check the objection deadline. Each notice identifies the exam cycle and stage. A provisional key can change after challenges; a raw score is not a normalised result.</p>
    <nav className="flex flex-wrap gap-3 mt-5" aria-label="More exam releases"><Link href="/exam-updates/" className="btn">All exam updates</Link><Link href="/results/" className="btn">Published results</Link></nav>
    <ExamUpdateBrowser items={listExamUpdates().filter(item => item.kind === 'answer-key')} kindOnly="answer-key" />
    <section className="card p-5 mt-8"><h2 className="text-lg font-extrabold">Before you submit an objection</h2><ul className="list-disc pl-5 mt-3 space-y-2"><li>Match the exact CEN or advertisement, grade, paper and stage.</li><li>Save the official question ID, your response and the answer-key entry.</li><li>Use the official objection form, supporting evidence and fee specified in that notice.</li><li>A published window may have ended. Check for an official extension before attempting a late submission.</li></ul></section>
  </div>;
}
