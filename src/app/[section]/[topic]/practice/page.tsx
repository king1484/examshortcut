import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, getTopic } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { TopicQuiz } from '@/components/TopicQuiz';
import { TopicPracticeGuide } from '@/components/topic-pages/TopicPracticeGuide';
import { cap } from '@/lib/seo';

export const dynamic = 'force-static';
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string }> }): Promise<Metadata> {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) return {};
  return {
    title: { absolute: cap(`${t.title} — practice & timed test (${t.practice?.length ?? 0} Q)`, 60) },
    description: cap(`Practice ${t.title} questions: untimed mode with instant explanations, or exam-mode with a per-question time budget, scoring and weakness analysis.`, 160),
    robots: !t.practice?.length ? { index: false, follow: true } : undefined,
  };
}

export default async function PracticePage({ params }: { params: Promise<{ section: string; topic: string }> }) {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();
  const meta = SECTION_META[t.sectionId as SectionId];
  const perSub = t.subtopics
    .map((s) => ({ id: s.id, title: s.title, n: (t.practice ?? []).filter((q) => q.subtopic === s.id).length }))
    .filter((s) => s.n > 0);

  return (
    <div>
      {perSub.length > 1 && (
        <section className="card p-4 mt-4">
          <h2 className="font-extrabold">Practice one subtopic at a time</h2>
          <p className="text-xs muted mt-0.5">Each subtopic has its own practice sets of 10, next to its notes and question types.</p>
          <div className="flex flex-wrap gap-2 mt-3">
            {perSub.map((s) => (
              <Link key={s.id} href={`/${t.sectionId}/${t.id}/learn/${s.id}/#practice`} className="btn text-sm" style={{ padding: '.35rem .75rem' }}>
                {s.title} <span className="faint text-xs ml-1">{s.n} Q</span>
              </Link>
            ))}
          </div>
        </section>
      )}
      <h2 className="text-lg font-extrabold mt-6">Full topic test — all {t.practice?.length ?? 0} questions</h2>
      <p className="muted text-sm mt-1">Two modes: <b>Practice</b> reveals the explanation after each question; <b>Test</b> uses a per-question time budget like the real exam and saves your score.</p>
      {(t.practice?.length ?? 0) > 0 ? (
        <div className="mt-4">
          <TopicQuiz questions={t.practice!} storageKey={`${t.sectionId}/${t.id}`} href={`/${t.sectionId}/${t.id}/practice/`} section={t.sectionId} title={`${meta.short} · ${t.title}`} />
        </div>
      ) : (
        <p className="card p-6 mt-4 text-center muted">Questions for this topic are being written — check back shortly.</p>
      )}
      <TopicPracticeGuide topic={t} />
    </div>
  );
}
