import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { ExamScoreCalculator } from '@/components/exam-tools/ExamScoreCalculator';
import { ToolPageFrame } from '@/components/exam-tools/ToolPageFrame';
import { VerifiedChip, loadExamPage, type Faq } from '@/components/exam-subpages/common';
import { NORMALISING, SCORE_CFG, examsWith, hasTool } from '@/lib/examTools';
import { cutRefsFor } from '@/lib/examToolsServer';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** ssc-cgl and cat keep their own hand-built calculators. */
export function generateStaticParams() {
  return examsWith('score-calculator').map((exam) => ({ exam }));
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const page = hasTool(id, 'score-calculator') ? loadExamPage(id) : null;
  if (!page) return {};
  return {
    title: `${page.info.name} score calculator: marks from your attempts`,
    description: `Work out your ${page.info.name} marks from correct and wrong answers using the real marking scheme, then compare with past cut-offs. Free, runs in your browser.`,
    alternates: { canonical: `/exams/${id}/score-calculator/` },
  };
}

export default async function ScoreCalculatorPage({ params }: { params: Params }) {
  const { exam: id } = await params;
  const page = hasTool(id, 'score-calculator') ? loadExamPage(id) : null;
  if (!page) notFound();
  const { info, exam } = page;
  const cfg = SCORE_CFG[id];
  const cuts = cutRefsFor(id);
  const normalises = id in NORMALISING;

  const faqs: Faq[] = [
    { q: `What is the ${info.name} marking scheme?`, a: cfg.schemeLine },
    {
      q: 'Is this my final score?',
      a: normalises
        ? 'No. It is your raw score. The exam runs in several shifts, so the board normalises marks across shifts, and your final score can move up or down a little. The normalisation calculator on this site gives an estimate.'
        : 'It is your raw score. Check the exam notice for sectional cut-offs and how the final merit is built from each stage.',
    },
    { q: 'How should I read the cut-off comparison?', a: 'Past cut-offs are a rough guide. They move every year with the difficulty of the paper and the number of vacancies, so being above one is encouraging but never a guarantee.' },
    { q: 'Is anything here unconfirmed?', a: cfg.checkOfficial },
  ];

  return (
    <ToolPageFrame
      id={id}
      kind="score-calculator"
      h1={`${info.name} score calculator`}
      faqs={faqs}
      intro={
        <>
          <p>Enter how many questions you got right and wrong in each section. The calculator applies the {info.name} marking scheme and shows your net marks, accuracy and how you stand against past cut-offs.</p>
          <p>{cfg.schemeLine} {cfg.checkOfficial}</p>
          <p><VerifiedChip exam={exam} /></p>
        </>
      }
    >
      <ExamScoreCalculator id={id} cuts={cuts} />
    </ToolPageFrame>
  );
}
