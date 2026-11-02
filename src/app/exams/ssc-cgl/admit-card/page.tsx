import Link from 'next/link';
import type { Metadata } from 'next';
import { getExam } from '@/lib/content';
import { getProcess } from '@/lib/examPages';
import { Md } from '@/components/Md';
import { DatePhases } from '@/components/DatePhases';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL 2026 admit card and answer key: release status and next steps',
  description: 'Checked CGL 2026 release status, official admission and response-sheet steps, challenge-notice checks and raw-score calculation. Unknown release dates are not predicted.',
};

export default function AdmitCardPage() {
  const exam = getExam('ssc-cgl');
  const process = getProcess('ssc-cgl')!;
  const cycle = exam.latestCycle;
  const phases = [
    { node: <Md>{cycle.status}</Md> },
    ...(cycle.statusPhases ?? []).map((phase: { from: string; status: string }) => ({
      from: phase.from, node: <Md>{phase.status}</Md>,
    })),
  ];
  return (
    <div className="max-w-3xl mx-auto">
      <nav className="text-xs faint"><Link href="/exams/ssc-cgl/" className="underline">SSC CGL</Link> / Admit card &amp; answer key</nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-2">SSC CGL 2026 admit card &amp; answer key</h1>
      <p className="muted mt-3 text-[15px]">Official release checks and practical next steps. Last verified: {process.lastVerified}.</p>
      <div className="status-callout mt-6">
        <span className="status-kicker">Latest status</span>
        <DatePhases phases={phases} />
      </div>
      <p className="mt-4"><a className="underline font-semibold" href="https://ssc.gov.in/" target="_blank" rel="noopener noreferrer">Check SSC notices and candidate login ↗</a></p>
      <h2 className="text-2xl font-extrabold mt-8">Admission certificates for each stage</h2>
      <div className="card p-5 mt-3 text-[15px]">
        <p>{process.admitCard.when}</p>
        <p className="mt-2"><b>Where:</b> {process.admitCard.where}</p>
        <ol className="list-decimal pl-5 space-y-2 mt-4">{process.admitCard.steps.map(step => <li key={step}>{step}</li>)}</ol>
        <h3 className="font-bold mt-5">Check the document before travelling</h3>
        <p className="mt-2">Follow your own certificate for the date, reporting and gate-closing times, original identity documents, photographs, permitted items and any scribe-related requirements. A city slip does not replace an admission certificate.</p>
      </div>
      <h2 className="text-2xl font-extrabold mt-8">Answer key, response sheet and objections</h2>
      <div className="card p-5 mt-3 text-[15px]">
        <p>{process.answerKey.summary}</p>
        <ol className="list-decimal pl-5 space-y-2 mt-4">{process.answerKey.steps.map(step => <li key={step}>{step}</li>)}</ol>
        <p className="mt-4"><b>Challenge fee:</b> {process.answerKey.fee}</p>
        <p className="muted mt-3">{process.answerKey.note}</p>
      </div>
      <h2 className="text-2xl font-extrabold mt-8">Estimate a raw score</h2>
      <p className="muted mt-3">For the Tier 1 marking scheme, correct answers earn 2 marks and wrong answers lose 0.50; unanswered questions score zero. A personal raw-score estimate is separate from SSC’s normalised marks, shortlist and final allocation.</p>
      <div className="grid sm:grid-cols-3 gap-3 mt-5">
        <Link href="/exams/ssc-cgl/calendar/" className="card p-4 font-semibold">Published dates</Link>
        <Link href="/exams/ssc-cgl/score-calculator/" className="card p-4 font-semibold">Score calculator</Link>
        <Link href="/exams/ssc-cgl/guides/" className="card p-4 font-semibold">Revision guides</Link>
      </div>
    </div>
  );
}
