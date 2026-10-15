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
      <p className="muted mt-2">Found a wrong answer, a broken page, or want a topic added? Send the page and the details so we can review it.</p>

      <div className="flex flex-wrap gap-3 mt-5">
        <Link href="/feedback/" className="btn btn-brand">Send feedback or a correction</Link>
        <Link href="/feature-requests/" className="btn">Request a feature</Link>
      </div>

      <div className="card p-5 mt-6 text-sm space-y-3">
        <p className="text-base">Email: <a className="underline font-bold" href="mailto:singirikonda3@gmail.com">singirikonda3@gmail.com</a></p>
        <p>For a content correction, include:</p>
        <ul className="list-disc pl-5 space-y-1">
          <li>The page URL (or the exam, section and topic name)</li>
          <li>The question text or question ID (shown during a mock review, e.g. <code>q-t1-pyq-2025-reasoning-14</code>)</li>
          <li>What you think is wrong and, ideally, the correct working</li>
        </ul>
        <p>
          Suggestions for new topics, posts, or features are equally welcome — we build what aspirants ask for.
        </p>
      </div>

      <div className="card p-5 mt-4 text-sm space-y-2">
        <p className="font-bold">Who reads your message</p>
        <p>
          ExamShortcut is built and run by one person, Vinay, a software engineer. Messages go to him directly, not to a support team or a bot.
          Correction reports are reviewed first, because a wrong answer hurts every aspirant who reads it.
        </p>
        <p>
          When a report is confirmed, the page is fixed and the change is listed on the <Link className="underline" href="/updates/">updates log</Link>.
          If it is not a mistake, the reply explains why the page says what it says.        </p>
      </div>

      <div className="card p-5 mt-4 text-sm">
        <p>
          Prefer a quick message? Reach <b>Vinay</b>, who builds ExamShortcut, on{' '}
          <a className="underline font-bold" href="https://www.instagram.com/vinni1484" target="_blank" rel="noopener">Instagram @vinni1484</a>.
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
        Before writing, read our <Link className="underline" href="/editorial-policy/">content and corrections policy</Link> and{' '}
        <Link className="underline" href="/privacy/">privacy policy</Link>. Please do not send passwords, identity documents or admit cards.
      </p>
    </div>
  );
}
