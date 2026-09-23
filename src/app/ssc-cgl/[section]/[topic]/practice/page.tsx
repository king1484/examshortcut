import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, getTopic } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { TopicQuiz } from '@/components/TopicQuiz';

export const dynamic = 'force-static';
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string }> }): Promise<Metadata> {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) return {};
  return {
    title: `${t.title} — free practice & timed test (${t.practice?.length ?? 0} Q) · SSC CGL`,
    description: `Practice ${t.title} questions free: untimed mode with instant explanations, or exam-mode with a per-question time budget, scoring and weakness analysis.`,
  };
}

export default async function PracticePage({ params }: { params: Promise<{ section: string; topic: string }> }) {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();
  const meta = SECTION_META[t.sectionId as SectionId];

  return (
    <div>
      <p className="muted text-sm mt-4">Two modes: <b>Practice</b> reveals the explanation after each question; <b>Test</b> uses a per-question time budget like the real exam and saves your score.</p>
      {(t.practice?.length ?? 0) > 0 ? (
        <div className="mt-4">
          <TopicQuiz questions={t.practice!} storageKey={`${t.sectionId}/${t.id}`} href={`/ssc-cgl/${t.sectionId}/${t.id}/practice/`} section={t.sectionId} title={`${meta.short} · ${t.title}`} />
        </div>
      ) : (
        <p className="card p-6 mt-4 text-center muted">Questions for this topic are being written — check back shortly.</p>
      )}
    </div>
  );
}
