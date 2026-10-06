import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { ExamRankEstimator } from '@/components/exam-tools/ExamRankEstimator';
import { ToolPageFrame } from '@/components/exam-tools/ToolPageFrame';
import { VerifiedChip, loadExamPage, type Faq } from '@/components/exam-subpages/common';
import { RANK_CFG, examsWith, hasTool } from '@/lib/examTools';
import { cutRefsFor } from '@/lib/examToolsServer';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** ssc-cgl keeps its own hand-built rank estimator; cat has no rank tool here. */
export function generateStaticParams() {
  return examsWith('rank-estimator').map((exam) => ({ exam }));
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const page = hasTool(id, 'rank-estimator') ? loadExamPage(id) : null;
  if (!page) return {};
  return {
    title: `${page.info.name} rank estimator: percentile and rank from your marks`,
    description: `A planning estimate of your ${page.info.name} percentile and rank, built from applicants, vacancies and past cut-offs. Every assumption is shown and editable.`,
    alternates: { canonical: `/exams/${id}/rank-estimator/` },
  };
}

export default async function RankEstimatorPage({ params }: { params: Params }) {
  const { exam: id } = await params;
  const page = hasTool(id, 'rank-estimator') ? loadExamPage(id) : null;
  if (!page) notFound();
  const { info, exam } = page;
  const cfg = RANK_CFG[id];
  const cuts = cutRefsFor(id)[cfg.cutStage] ?? [];

  const faqs: Faq[] = [
    { q: 'Does the board publish an all-India rank?', a: 'The boards publish result lists and scorecards, but they do not generally publish an all-India rank for the first stage. So any rank shown here is an estimate, not a fact.' },
    { q: 'How is the rank worked out?', a: `You give the number who appear, the number shortlisted and the score of the last shortlisted candidate. The estimator places that candidate at the shortlist rank, assumes scores follow a bell curve, and reads your percentile off it. Rank is candidates appeared times one minus the percentile.` },
    { q: 'Which numbers are assumptions?', a: `${cfg.ratioNote} ${cfg.caveat}` },
    { q: 'What should I use this for?', a: 'For planning and motivation, for example to see how many marks move your rank by thousands. For a go or no-go call, compare your marks with past cut-offs in the score calculator.' },
  ];

  return (
    <ToolPageFrame
      id={id}
      kind="rank-estimator"
      h1={`${info.name} rank estimator`}
      faqs={faqs}
      intro={
        <>
          <p>Enter your expected {cfg.stageLabel} marks to get an estimated percentile and rank. This is a scenario tool: you can change the number of candidates, the shortlist size and the cut-off it is anchored on, and see how the rank moves.</p>
          <p>It is clearly an estimate. The first stage of {info.name} has no published all-India rank, and your normalised score decides the real result.</p>
          <p><VerifiedChip exam={exam} /></p>
        </>
      }
    >
      <ExamRankEstimator id={id} cuts={cuts} />
    </ToolPageFrame>
  );
}
