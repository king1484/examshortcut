import type { Metadata } from 'next';
import { getExam } from '@/lib/content';
import { CatStudyPlanner, type CatEvent } from '@/components/cat/CatStudyPlanner';
import { CatToolHeader } from '@/components/cat/CatToolsNav';
import { CatStudyPlanDepth } from '@/components/exam-pages/PlanDepth';

export const dynamic = 'force-static';

const TITLE = 'CAT study plan: countdown and phase-wise plan by weeks left';
const DESC = 'CAT preparation plan: a countdown to the exam date and a week-by-week plan (concepts, sectional practice, full mocks, analysis) driven by how many weeks you have left. Tick off tasks; progress saves in your browser.';
export const metadata: Metadata = {
  title: TITLE,
  description: DESC,
  alternates: { canonical: '/exams/cat/study-plan/' },
  openGraph: { title: TITLE, description: DESC },
};

/* eslint-disable @typescript-eslint/no-explicit-any */
export default function CatStudyPlanPage() {
  const exam = getExam('cat');
  const lc = exam?.latestCycle ?? {};
  // Exam date: the milestone flagged as the countdown (else the calendar event); both live in exam.json.
  const examDate: string =
    lc.milestones?.find((m: any) => m.countdown)?.from ??
    exam?.calendar?.events?.find((e: any) => e.id === 'exam')?.start ??
    '2026-11-29';
  const events: CatEvent[] = (exam?.calendar?.events ?? [])
    .filter((e: any) => e.start <= examDate)
    .map((e: any) => ({ id: e.id, title: e.title, start: e.start, status: e.status }));
  const year = lc.year ?? 2026;

  return (
    <div className="max-w-3xl mx-auto">
      <CatToolHeader
        current="/exams/cat/study-plan/"
        h1={`CAT ${year} study plan`}
        intro={<>The countdown runs to the CAT {year} exam date ({new Date(`${examDate}T00:00:00+05:30`).toLocaleDateString('en-IN', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Kolkata' })}). Your remaining weeks are split into four phases: concepts, then sectional practice, then full mocks, then analysis and final revision. The fewer weeks you have, the earlier you move to mocks. No login is needed; your ticks and settings are saved only in this browser.</>}
      />
      <div className="mt-6"><CatStudyPlanner examDate={examDate} events={events} /></div>
      <CatStudyPlanDepth />
    </div>
  );
}
