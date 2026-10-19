import type { Metadata } from 'next';
import { getExam } from '@/lib/content';
import { CAT_SECS } from '@/lib/catSyllabus';
import { CatScoreCalculator, type CatCalcSection } from '@/components/cat/CatScoreCalculator';
import { CatToolHeader } from '@/components/cat/CatToolsNav';

export const dynamic = 'force-static';

const TITLE = 'CAT score calculator: raw score, accuracy & attempts by section';
const DESC = 'CAT raw-score calculator: enter MCQ and TITA correct/wrong counts for VARC, DILR and QA (+3 correct, −1 wrong MCQ, no negative for TITA) to get sectional and total raw score, accuracy and attempts.';
export const metadata: Metadata = {
  title: TITLE,
  description: DESC,
  alternates: { canonical: '/exams/cat/score-calculator/' },
  openGraph: { title: TITLE, description: DESC, images: ['/og.png'] },
};

/* eslint-disable @typescript-eslint/no-explicit-any */
export default function CatScoreCalculatorPage() {
  const exam = getExam('cat');
  const stage = (exam?.stages ?? []).find((s: any) => s.id === 'cat-cbt');
  const fromJson: any[] = stage?.sections ?? [];
  // Question counts come from content/exams/cat/exam.json (CAT 2025 baseline); fall back to 24/22/22 only if missing.
  const fallback: Record<string, number> = { english: 24, reasoning: 22, quant: 22 };
  const sections: CatCalcSection[] = CAT_SECS.map((c) => ({
    id: c.id, short: c.short, name: c.name, color: c.color,
    questions: Number(fromJson.find((s) => s.sectionId === c.sectionId)?.questions) || fallback[c.sectionId],
  }));
  const minutes = Math.round((Number(stage?.durationMin) || 120) / 3);

  return (
    <div className="max-w-3xl mx-auto">
      <CatToolHeader
        current="/exams/cat/score-calculator/"
        h1="CAT score calculator"
        intro={<>Enter your counts for each section and get your raw score, accuracy and attempts. CAT gives <b>+3</b> for a correct answer and <b>{'−'}1</b> for a wrong MCQ. <b>TITA</b> (type-in-the-answer) questions have <b>no negative marking</b>. Each section is {minutes} minutes. The question counts below are the CAT 2025 paper ({sections.map((s) => `${s.short} ${s.questions}`).join(', ')}); the IIMs do not announce counts in advance.</>}
      />
      <CatScoreCalculator sections={sections} minutesPerSection={minutes} />
    </div>
  );
}
