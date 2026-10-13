import type { Metadata } from 'next';
import Link from 'next/link';
import { FeedbackForm } from '@/components/FeedbackForm';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Feedback & corrections',
  description: 'Report a bug, unclear explanation or wrong answer on ExamShortcut. Send private feedback without creating an account.',
};

export default function FeedbackPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">Help us improve ExamShortcut</h1>
      <p className="muted mt-3">A missing step in a solution, a wrong answer or a page that does not work can interrupt your preparation. Tell us which page needs attention and what you noticed.</p>
      <nav aria-label="Feedback options" className="flex flex-wrap gap-3 mt-5">
        <Link href="/feedback/" className="btn btn-brand" aria-current="page">Feedback & corrections</Link>
        <Link href="/feature-requests/" className="btn">Request a feature</Link>
      </nav>
      <FeedbackForm kind="feedback" />
      <p className="text-sm muted mt-5">We review reports for accuracy and learning impact. For how corrections are handled, read our <Link className="underline" href="/editorial-policy/">content and corrections policy</Link>. Exam applications, admit cards and results must be handled by the official exam body.</p>
    </div>
  );
}
