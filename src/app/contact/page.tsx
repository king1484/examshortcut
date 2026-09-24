import type { Metadata } from 'next';
import Link from 'next/link';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Contact',
  description: 'Report a wrong answer, a bug, or a suggestion on ExamShortcut. Content-error reports are the fastest to fix — include the page and question.',
};

export default function ContactPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">Contact</h1>
      <p className="muted mt-2">Found a wrong answer, a broken page, or want a topic added? Tell us — corrections go out fast.</p>

      <div className="card p-5 mt-6 text-sm space-y-3">
        <p className="text-base">Email: <a className="underline font-bold" href="mailto:contact@examshortcut.in">contact@examshortcut.in</a></p>
        <p>For a content correction, include:</p>
        <ul className="list-disc pl-5 space-y-1">
          <li>The page URL (or the exam, section and topic name)</li>
          <li>The question text or question ID (shown during a mock review, e.g. <code>q-t1-pyq-2025-reasoning-14</code>)</li>
          <li>What you think is wrong and, ideally, the correct working</li>
        </ul>
        <p>
          Suggestions for new topics, posts, or features are equally welcome — the roadmap is driven by what aspirants ask for.
        </p>
      </div>

      <div className="card p-5 mt-4 text-sm">
        <p className="font-bold">Please don&apos;t ask us about:</p>
        <p className="mt-1">
          Application status, admit-card problems, exam-centre changes or result grievances — these are handled only by the exam body.
          Raise them with the exam's official website or regional office;
          we cannot act on them.
        </p>
      </div>

      <p className="text-sm muted mt-6">
        Before writing, the <Link className="underline" href="/about/">about page</Link> explains where our data comes from, and the{' '}
        <Link className="underline" href="/privacy/">privacy policy</Link> explains why we never ask for your personal details.
      </p>
    </div>
  );
}
