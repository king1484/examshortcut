import type { Metadata } from 'next';
import Link from 'next/link';
import { contentStats } from '@/lib/content';

export const dynamic = 'force-static';
export const metadata: Metadata = { title: 'About ExamShortcut & disclaimer' };

export default function AboutPage() {
  const stats = contentStats();
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">About ExamShortcut</h1>
      <p className="mt-3">
        ExamShortcut is a free, no-login preparation site for Indian government exams, starting with SSC CGL.
        Everything runs in your browser: your mock attempts, mistake notebook and progress live on your device —
        there is no account and nothing is uploaded.
      </p>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6 text-center">
        {[['Topics', stats.topics], ['Questions', stats.questions], ['Formulas', stats.formulas], ['Shortcut tricks', stats.tricks]].map(([k, v]) => (
          <div key={k as string} className="card p-4"><div className="text-2xl font-extrabold">{v as number}</div><div className="text-xs faint font-semibold uppercase mt-0.5">{k}</div></div>
        ))}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Where the content comes from</h2>
      <ul className="list-disc pl-5 mt-3 space-y-1.5 text-sm">
        <li><b>Exam data &amp; cutoffs</b> — official SSC notifications and result notices at <a className="underline" href="https://ssc.gov.in" target="_blank" rel="noopener noreferrer">ssc.gov.in</a>, linked on every data page.</li>
        <li><b>Notes, formulas, shortcuts</b> — original explanations written for this site.</li>
        <li><b>Practice questions &amp; mocks</b> — original questions modelled on the recurring patterns of real SSC papers; every quantitative answer is computed and verified by code before publishing. We deliberately do not republish copyrighted papers or coaching material.</li>
        <li><b>Current affairs</b> — compiled from government sources such as PIB releases.</li>
      </ul>

      <h2 className="text-2xl font-extrabold mt-10">Disclaimer</h2>
      <div className="card p-5 mt-3 text-sm space-y-2">
        <p>ExamShortcut is an <b>independent learning platform</b>. We are not affiliated with, endorsed by, or connected to the Staff Selection Commission, any other examining body, or any Government of India entity.</p>
        <p>Exam patterns, dates, vacancies and cutoffs change. Always confirm on the official website{' '}
          <a className="underline" href="https://ssc.gov.in" target="_blank" rel="noopener noreferrer">ssc.gov.in</a> before acting on anything you read here.</p>
        <p>Mock scores, normalisation bands and safe-score estimates are approximations for guidance, not predictions.</p>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Roadmap</h2>
      <ul className="list-disc pl-5 mt-3 space-y-1.5 text-sm">
        <li><b>Now</b> — SSC CGL: notes, shortcuts, topic tests, mocks, cutoffs, current affairs.</li>
        <li><b>Next</b> — SSC CHSL, MTS, GD and RRB NTPC / Group D on the same engine (they share most of the syllabus).</li>
        <li><b>Later</b> — Hindi medium, error reporting on every question, spaced-repetition revision.</li>
      </ul>

      <p className="text-sm muted mt-8">Found a wrong answer or a bug? It happens — <Link className="underline" href="/revision/">your data stays local</Link> while we keep improving. A report-an-error button is on the roadmap.</p>
    </div>
  );
}
