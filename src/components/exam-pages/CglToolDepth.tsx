import Link from 'next/link';
import { Md } from '@/components/Md';
import { getCutoffs, getExam } from '@/lib/content';
import { RelatedCards, show, type LinkCard } from './ExamDepth';

/* eslint-disable @typescript-eslint/no-explicit-any */
/* Server-rendered explanation that sits below the SSC CGL marks / score / rank tools. All numbers come
   from content/exams/ssc-cgl/{exam,cutoffs}.json at build time; the advice is general and points back to
   the official SSC notice. Additive: it renders under the existing interactive tool. */

type Kind = 'marks' | 'score' | 'rank';
const MAIN = 'all posts except AAO/JSO';
const CATS = ['UR', 'EWS', 'OBC', 'SC', 'ST'];

function facts() {
  const exam = getExam('ssc-cgl') as any;
  const t1 = (exam?.stages ?? []).find((s: any) => s.id === 'tier1');
  const questions: number = t1?.totalQuestions ?? 100;
  const total: number = t1?.totalMarks ?? 200;
  const plus = total / questions;
  const m = String(t1?.negative ?? '').match(/[−-]\s*([\d.]+)/);
  const minus = m ? Number(m[1]) : 0.5;
  const sections: { name: string; questions: number; marks: number }[] = t1?.sections ?? [];
  const lists = (((getCutoffs('ssc-cgl') as any)?.tier1 ?? []) as any[]).filter((l) => l.cutoffs && String(l.list).includes(MAIN)).sort((a, b) => a.year - b.year);
  return { exam, t1, questions, total, plus, minus, sections, lists, minutes: t1?.durationMin ?? 60 };
}

const raw = (attempts: number, acc: number, plus: number, minus: number) => attempts * acc * plus - attempts * (1 - acc) * minus;

const INTRO: Record<Kind, string> = {
  marks: 'This tool reads a response sheet you have saved yourself. What follows explains how the marks are worked out, what the totals mean, and what the tool cannot tell you.',
  score: 'The score calculator is plain arithmetic on your correct and wrong counts. What follows explains the marking rules it uses and how to read the result against past cutoffs.',
  rank: 'The estimator turns a Tier 1 score into an approximate position. What follows explains what it is anchored on and why the number should be treated as a range of outcomes, not a prediction.',
};

const SPECIFIC: Record<Kind, { h: string; paras: string[] }> = {
  marks: {
    h: 'Using your response sheet',
    paras: [
      'Download or save the response sheet from the candidate login while it is available, and keep the file as it was saved. The tool reads it inside your browser; nothing is uploaded, so there is no account to create and nothing to delete afterwards.',
      'Marks are counted from the response and the answer key in the sheet: a correct answer adds the full mark, a wrong one subtracts the penalty, and a question left unanswered scores nothing. Check that the question count and section totals match the paper you wrote before trusting the total.',
      'If the figures differ from the official result, look at questions that were challenged or dropped, because the final key can change after the first release. The marks you see here are raw. Normalisation across shifts, described below, is applied by the commission to the raw figure.',
    ],
  },
  score: {
    h: 'Reading your result',
    paras: [
      'Enter whole numbers of correct and wrong answers in each section. Skipped questions need no entry. Tier 1 awards 2 marks per correct answer and deducts 0.5 per wrong answer. Tier 2 Paper 1 awards 3 and deducts 1. Whether to guess depends on your confidence and the time available; eliminating an option does not guarantee a correct answer.',
      'Compare the net score with the cutoff table, not with a single number. Cutoffs differ by category and by post list, and they moved noticeably between years, which is why the figure to track is the gap, not the absolute value.',
      'Use the section split to decide what to practise. Review wrong answers for concept errors and rushed calculation. Check skipped questions separately: missing knowledge, low confidence and lack of time need different fixes. A historical cutoff comparison does not predict qualification.',
    ],
  },
  rank: {
    h: 'What the estimate is anchored on',
    paras: [
      'The estimator anchors on published cutoffs, which are points where the commission drew a line for shortlisting, not points on a full rank list. Between those anchors the percentile is interpolated, so the further your score is from a cutoff, the looser the estimate.',
      'Ranks also depend on how many candidates appear, how hard your shift was, and how marks are normalised across shifts. Two candidates with the same raw score in different shifts can end up with different normalised scores and different ranks.',
      'Treat the output as a way to see which side of the shortlist line you probably sit on and by how much. If you are within a few marks of the cutoff for your category, the estimate cannot tell you which way it will fall.',
    ],
  },
};

export function CglToolDepth({ kind }: { kind: Kind }) {
  const f = facts();
  if (!f.t1) return null;
  const latest = f.lists[f.lists.length - 1];
  const prev = f.lists[f.lists.length - 2];
  const cats = latest ? [...CATS.filter((c) => c in latest.cutoffs)] : [];
  const scen = [
    { a: 70, acc: 0.9 }, { a: 80, acc: 0.9 }, { a: 90, acc: 0.8 }, { a: 100, acc: 0.8 },
  ].filter((s) => s.a <= f.questions);

  const links: LinkCard[] = [
    ...(kind !== 'score' ? [{ href: '/exams/ssc-cgl/score-calculator/', title: 'Score calculator', sub: 'Enter correct and wrong counts by hand' }] : []),
    ...(kind !== 'marks' ? [{ href: '/exams/ssc-cgl/marks-calculator/', title: 'Marks from your response sheet', sub: 'Read a saved sheet privately in the browser' }] : []),
    ...(kind !== 'rank' ? [{ href: '/exams/ssc-cgl/rank-estimator/', title: 'Rank and percentile estimator', sub: 'Approximate position from Tier 1 marks' }] : []),
    { href: '/exams/ssc-cgl/cutoffs/', title: 'SSC CGL cutoffs', sub: 'Category-wise cutoffs for every year' },
    { href: '/exams/ssc-cgl/exam-pattern/', title: 'Exam pattern', sub: 'Stages, sections and marking' },
    { href: '/exam-analysis/', title: 'Shift-wise analysis', sub: 'How hard each shift was reported to be' },
  ];

  return (
    <div className="mt-10">
      <section aria-labelledby="ct-marking">
        <h2 id="ct-marking" className="text-2xl font-extrabold">How Tier 1 marking works</h2>
        <p className="mt-2 text-[15px] muted max-w-3xl">
          {INTRO[kind]} Tier 1 has {f.questions} questions for {f.total} marks in {f.minutes} minutes. A correct answer earns +{show(f.plus)} and a wrong answer costs −{show(f.minus)}; an unanswered question scores zero.
        </p>
        {f.sections.length > 0 && (
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Section</th><th className="text-right">Questions</th><th className="text-right">Marks</th></tr></thead>
              <tbody>
                {f.sections.map((s) => <tr key={s.name}><td>{s.name}</td><td className="text-right">{s.questions}</td><td className="text-right">{s.marks}</td></tr>)}
              </tbody>
            </table>
          </div>
        )}
        {f.t1.notes && <div className="text-sm muted mt-3 max-w-3xl"><Md>{f.t1.notes}</Md></div>}
      </section>

      <section className="mt-9" aria-labelledby="ct-worked">
        <h2 id="ct-worked" className="text-2xl font-extrabold">Worked examples: attempts and accuracy</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          The same arithmetic the tools use, for four common ways of attempting the paper. Raw marks are the right answers times {show(f.plus)}, minus the wrong answers times {show(f.minus)}.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Attempts</th><th className="text-right">Accuracy</th><th className="text-right">Correct</th><th className="text-right">Wrong</th><th className="text-right">Raw marks</th></tr></thead>
            <tbody>
              {scen.map((s) => {
                const ok = Math.round(s.a * s.acc);
                return <tr key={`${s.a}-${s.acc}`}><td>{s.a}</td><td className="text-right">{show(s.acc * 100)}%</td><td className="text-right">{ok}</td><td className="text-right">{s.a - ok}</td><td className="text-right font-bold">{show(raw(s.a, s.acc, f.plus, f.minus))}</td></tr>;
              })}
            </tbody>
          </table>
        </div>
        <p className="text-sm muted mt-3 max-w-3xl">
          Compare the second and third rows: ten more attempts at lower accuracy score less ({show(raw(90, 0.8, f.plus, f.minus))} against {show(raw(80, 0.9, f.plus, f.minus))}). A wrong answer costs {show(f.minus)} directly and also gives up the {show(f.plus)} a correct answer would have earned, so a drop in accuracy hurts more than it looks.</p>
      </section>

      {latest && cats.length > 0 && (
        <section className="mt-9" aria-labelledby="ct-cut">
          <h2 id="ct-cut" className="text-2xl font-extrabold">Where recent cutoffs sat</h2>
          <p className="text-sm muted mt-2 max-w-3xl">
            Tier 1 to Tier 2 cutoffs for the main post list in {latest.year}{prev ? ` against ${prev.year}` : ''}, out of {latest.maxMarks}. Cutoffs are declared per post list and per category, and the commission&apos;s own notice is the authority.
          </p>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Category</th>{prev && <th className="text-right">{prev.year}</th>}<th className="text-right">{latest.year}</th>{prev && <th className="text-right">Change</th>}</tr></thead>
              <tbody>
                {cats.map((c) => {
                  const d = prev && c in prev.cutoffs ? latest.cutoffs[c] - prev.cutoffs[c] : null;
                  return (
                    <tr key={c}>
                      <td>{c}</td>
                      {prev && <td className="text-right">{c in prev.cutoffs ? show(prev.cutoffs[c]) : '-'}</td>}
                      <td className="text-right font-bold">{show(latest.cutoffs[c])}</td>
                      {prev && <td className="text-right">{d === null ? '-' : `${d > 0 ? '+' : d < 0 ? '−' : ''}${show(Math.abs(d))}`}</td>}
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
          <p className="text-sm muted mt-3 max-w-3xl">
            The category order can change from year to year, and the movement between years is large enough that last year&apos;s number is a reference, not a target. See the <Link className="underline" href="/exams/ssc-cgl/cutoffs/">full cutoff history</Link> for every list.
          </p>
        </section>
      )}

      <section className="mt-9" aria-labelledby="ct-specific">
        <h2 id="ct-specific" className="text-2xl font-extrabold">{SPECIFIC[kind].h}</h2>
        <div className="mt-2 space-y-3 max-w-3xl text-[15px]">
          {SPECIFIC[kind].paras.map((p, i) => <p key={i}>{p}</p>)}
        </div>
      </section>

      {f.exam?.normalization && (
        <section className="mt-9" aria-labelledby="ct-norm">
          <h2 id="ct-norm" className="text-2xl font-extrabold">Why raw marks are not the final word</h2>
          <div className="mt-2 text-[15px] muted max-w-3xl"><Md>{String(f.exam.normalization)}</Md></div>
        </section>
      )}

      <RelatedCards cards={links} heading="Related tools and pages" id="ct-related" />
    </div>
  );
}
