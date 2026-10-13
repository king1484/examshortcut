import type { Metadata } from 'next';
import Link from 'next/link';
import { FeedbackForm } from '@/components/FeedbackForm';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Request a feature',
  description: 'Suggest a study tool, topic or improvement for ExamShortcut. Explain your preparation needs and submit a private feature request without login.',
};

export default function FeatureRequestsPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">What would make studying easier?</h1>
      <p className="muted mt-3">Request a missing topic, a study tool or a better way to use existing notes and revision features. A useful request explains the study problem and how the change would help you solve it.</p>
      <nav aria-label="Feedback options" className="flex flex-wrap gap-3 mt-5">
        <Link href="/feedback/" className="btn">Feedback & corrections</Link>
        <Link href="/feature-requests/" className="btn btn-brand" aria-current="page">Request a feature</Link>
      </nav>
      <FeedbackForm kind="feature" />
      <div className="card p-5 mt-5 text-sm">
        <h2 className="font-extrabold">How we choose improvements</h2>
        <p className="muted mt-2">We look at how many students face the problem, whether the idea makes preparation clearer or more accessible, and what we can maintain well. Requests are reviewed privately; submitting one does not guarantee implementation or a release date.</p>
      </div>
    </div>
  );
}
