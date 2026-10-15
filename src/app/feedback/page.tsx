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
      <section className="card p-5 mt-6 text-sm space-y-3" aria-labelledby="fb-good">
        <h2 id="fb-good" className="font-extrabold text-base">What makes a report easy to act on</h2>
        <ul className="list-disc pl-5 space-y-1.5">
          <li><b>Say where.</b> The page address, or the exam, section and topic name. For a mock test question, the question ID shown in the review screen is the fastest route to the exact item.</li>
          <li><b>Say what is wrong.</b> A wrong option marked correct, a step that does not follow, a typo in the stem, a figure that does not load, or a page that will not open each need a different fix.</li>
          <li><b>Share your working.</b> If you think the answer is different, write the steps you used. Two worked solutions that disagree show quickly which one has the slip.</li>
          <li><b>Mention your device if the problem is visual.</b> Phone or laptop, and the browser, helps when a formula runs off the screen or a table is cut.</li>
        </ul>
      </section>

      <section className="card p-5 mt-4 text-sm space-y-3" aria-labelledby="fb-after">
        <h2 id="fb-after" className="font-extrabold text-base">What happens after you send it</h2>
        <p>
          Your message is saved privately and read by Vinay, who maintains the site himself. A report about an answer or a solution is checked against the question and its working before anything is changed, so a confirmed mistake is fixed at the source and the page you were on shows the corrected version on the next update.
          Fixes are written up on the <Link className="underline" href="/updates/">updates log</Link>. If the page was right, you are told why, because an explanation of the method is often more useful than a bare reply.
        </p>
        <p>
          Reports are read as time allows. This is a one-person project, so there is no fixed turnaround, and urgent exam-day questions about notices or dates should always be checked on the official website of the exam body.
        </p>
      </section>

      <section className="card p-5 mt-4 text-sm space-y-2" aria-labelledby="fb-types">
        <h2 id="fb-types" className="font-extrabold text-base">Questions imported from past papers</h2>
        <p>
          Many mock tests are built from past-paper questions that candidates remembered and published, so a wording slip or a disputed key can happen even when the source is careful. If you spot one, send the question ID and what you believe the key should be. These reports are the most valuable ones, because every learner who takes that mock sees the same item.
        </p>
      </section>

      <p className="text-sm muted mt-5">We review reports for accuracy and learning impact. For how corrections are handled, read our <Link className="underline" href="/editorial-policy/">content and corrections policy</Link>. Exam applications, admit cards and results must be handled by the official exam body.</p>
    </div>
  );
}
