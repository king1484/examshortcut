import Link from 'next/link';
import type { Metadata } from 'next';
import { getExam } from '@/lib/content';
import { CAT_SECS } from '@/lib/catSyllabus';
import { CatToolHeader } from '@/components/cat/CatToolsNav';
import { Md } from '@/components/Md';

export const dynamic = 'force-static';

const TITLE = 'CAT syllabus: section-wise topics (VARC, DILR, QA) and strategy';
const DESC = 'CAT syllabus by section: commonly tested VARC, DILR and QA topics, the CAT 2025 composition (24/22/22 questions), marking scheme and an approach for each section.';
export const metadata: Metadata = {
  title: TITLE,
  description: DESC,
  alternates: { canonical: '/exams/cat/syllabus/' },
  openGraph: { title: TITLE, description: DESC, images: ['/og.png'] },
};

/* eslint-disable @typescript-eslint/no-explicit-any */
export default function CatSyllabusPage() {
  const exam = getExam('cat');
  const stage = (exam?.stages ?? []).find((s: any) => s.id === 'cat-cbt');
  const secs: any[] = stage?.sections ?? [];
  const mins = Math.round((Number(stage?.durationMin) || 120) / 3);

  return (
    <div className="max-w-4xl mx-auto">
      <CatToolHeader
        current="/exams/cat/syllabus/"
        h1="CAT syllabus, section by section"
        intro={<>CAT has <b>no official published syllabus</b>. The IIMs publish only the pattern. The topic lists below are the areas that recur in past papers and in prep-portal syllabus guides, so read them as <b>commonly tested areas</b>, not a guarantee. Counts and marks come from the CAT 2025 paper. Anything marked <span className="chip chip-low">illustrative</span> is our own suggestion, not an official rule.</>}
      />

      <div className="card p-4 mt-5 text-sm">
        <div className="font-bold">The frame (from the CAT 2025 paper)</div>
        <ul className="mt-1.5 space-y-1 list-disc pl-5 muted">
          <li>{stage?.totalQuestions ?? 68} questions, {stage?.totalMarks ?? 204} marks, {stage?.durationMin ?? 120} minutes. Fixed order VARC, then DILR, then QA, with {mins} minutes locked per section.</li>
          <li>+3 for a correct answer, {'−'}1 for a wrong MCQ. TITA (type-in-the-answer) questions appear in all three sections and have no negative marking.</li>
          <li>An on-screen basic calculator is provided. The IIMs do not announce question counts in advance.</li>
        </ul>
      </div>

      {CAT_SECS.map((c) => {
        const row = secs.find((s) => s.sectionId === c.sectionId);
        return (
          <section key={c.id} className="mt-8" aria-labelledby={`sec-${c.id}`}>
            <div className="flex items-baseline justify-between flex-wrap gap-2">
              <h2 id={`sec-${c.id}`} className="text-2xl font-extrabold" style={{ color: c.color }}>{c.short}: {c.name}</h2>
              <Link href={`/${c.sectionId}/`} className="text-sm underline decoration-dotted">Practice topics →</Link>
            </div>
            <p className="text-xs faint mt-0.5">{row ? `${row.questions} questions · ${row.marks} marks · ${mins} minutes` : `${mins} minutes`}</p>
            <p className="text-sm muted mt-2">{c.composition}</p>

            <div className="grid sm:grid-cols-2 gap-3 mt-3">
              {c.areas.map((a) => (
                <div key={a.name} className="card p-4" style={{ borderTop: `3px solid ${c.color}` }}>
                  <div className="font-bold text-sm">{a.name}</div>
                  <ul className="mt-1.5 space-y-0.5 text-sm muted list-disc pl-5">
                    {a.topics.map((t) => <li key={t}>{t}</li>)}
                  </ul>
                </div>
              ))}
            </div>

            <div className="card p-4 mt-3">
              <div className="flex items-center gap-2"><span className="font-bold text-sm">Strategy</span><span className="chip chip-low text-xs">illustrative</span></div>
              <ul className="mt-1.5 space-y-1 text-sm list-disc pl-5">
                {c.strategy.map((t) => <li key={t}>{t}</li>)}
              </ul>
            </div>
          </section>
        );
      })}

      {exam?.normalization && (
        <section className="mt-10" aria-labelledby="why">
          <h2 id="why" className="text-2xl font-extrabold">Why sectional balance matters</h2>
          <Md className="mt-2 text-sm muted">{exam.normalization}</Md>
        </section>
      )}

      <div className="grid sm:grid-cols-3 gap-3 mt-8">
        <Link href="/exams/cat/study-plan/" className="card p-4 hover:-translate-y-0.5 transition-transform"><div className="font-bold text-sm">🗓️ Build your study plan</div><div className="text-xs faint mt-0.5">Countdown and weekly phases</div></Link>
        <Link href="/exams/cat/score-calculator/" className="card p-4 hover:-translate-y-0.5 transition-transform"><div className="font-bold text-sm">🧮 Score calculator</div><div className="text-xs faint mt-0.5">Raw score, accuracy, attempts</div></Link>
        <Link href="/exams/cat/cutoffs/" className="card p-4 hover:-translate-y-0.5 transition-transform"><div className="font-bold text-sm">📈 Institute cut-offs</div><div className="text-xs faint mt-0.5">Qualifying and shortlist percentiles</div></Link>
      </div>
    </div>
  );
}
