import type { Metadata } from 'next';
import Link from 'next/link';
import { availableSections, listTopics } from '@/lib/content';
import { RevisionPlanner } from '@/components/RevisionPlanner';
import { ShareResource } from '@/components/ShareResource';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Free revision planner for competitive exams',
  description: 'Plan topic reviews after 1, 3, 7 and 14 days. Save your topics in your browser and download a free calendar schedule. No login required.',
  alternates: { canonical: '/revision-planner/' },
};

export default function RevisionPlannerPage() {
  const suggestions = availableSections().flatMap((s) => listTopics(s).map((t) => t.title));
  return (
    <div className="max-w-3xl mx-auto">
      <Link href="/study-guides/" className="text-sm underline muted">← Study guides</Link>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-4">Free revision planner</h1>
      <p className="muted mt-3">Add a topic and the day you learned it. Get suggested reviews after 1, 3, 7 and 14 days, then download them to your calendar.</p>
      <p className="text-sm muted mt-3">These intervals are a starting routine. Review difficult topics sooner and adjust around your exam date. Your topic list stays in this browser; it is separate from your account progress.</p>
      <RevisionPlanner suggestions={suggestions} />
      <section className="card p-5 mt-8">
        <h2 className="text-xl font-extrabold">What to do at each review</h2>
        <ol className="list-decimal pl-5 mt-3 space-y-2 text-sm">
          <li>Close your notes and recall the method or key facts.</li>
          <li>Try a few questions or explain a worked example yourself.</li>
          <li>Check the answers and repair the specific gap.</li>
        </ol>
        <p className="text-sm mt-4">Read <Link href="/study-guides/revision-without-forgetting/" className="underline">the revision guide</Link> or open your <Link className="underline" href="/learn/">next lesson</Link>.</p>
        <p className="text-xs muted mt-3">Calendar entries are all-day events. Notifications depend on your calendar settings. Reimporting the same file may create duplicates in some calendar apps.</p>
      </section>
      <ShareResource title="Free revision planner for competitive exams" path="/revision-planner/" />
    </div>
  );
}
