import Link from 'next/link';
import type { Metadata } from 'next';
import { SECTION_META, SECTION_ORDER, listTopics, listMocks } from '@/lib/content';
import { StudyPlanner, type PlanTopic, type PlanMock } from '@/components/StudyPlanner';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL study plan generator — day-by-day timetable till exam day',
  description: 'SSC CGL study plan: enter your exam date, daily study hours and weak sections to get a day-by-day timetable covering every topic, with weekly full mocks and a revision block. You can tick off progress, and it saves on your device.',
};

export default function StudyPlanPage() {
  const topics: PlanTopic[] = SECTION_ORDER.flatMap((s) =>
    listTopics(s).map((t) => ({
      section: s, sectionShort: SECTION_META[s].short, color: SECTION_META[s].color, id: t.id, title: t.title,
      importance: t.importance, nSub: t.subtopics.length, nPractice: t.practice?.length ?? 0,
    })),
  );
  const mocks: PlanMock[] = listMocks().map((m) => ({ id: m.id, title: m.title, tier: m.tier, available: m.available }));

  return (
    <div className="max-w-3xl mx-auto">
      <nav className="text-xs faint"><Link href="/exams/ssc-cgl/" className="underline decoration-dotted">SSC CGL</Link> / Study plan</nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-2">Your SSC CGL study plan</h1>
      <p className="muted mt-3 text-[15px]">
        A day-by-day plan over all {topics.length} topics, built from your exam date, daily hours and strong and weak sections.
      </p>
      <div className="mt-6"><StudyPlanner topics={topics} mocks={mocks} t1Default="2026-09-30" t2Default="2027-01-10" /></div>

      <h2 className="text-2xl font-extrabold mt-10">How the plan works</h2>
      <ul className="card p-5 mt-3 text-sm muted list-disc pl-9 space-y-1.5">
        <li>You enter your exam date, daily study hours and how strong you are in each section.</li>
        <li>Sections are mixed every day, so none gets neglected.</li>
        <li>There is a full mock every 7th day, and the last stretch is kept for mocks and revision.</li>
        <li>If time is short, lower-weightage topics are dropped first.</li>
        <li>Every item links to its notes or test. Tick items as you go; the plan is saved in this browser.</li>
      </ul>
    </div>
  );
}
