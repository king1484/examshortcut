import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, SECTION_ORDER, getSection, getTopic, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { Md } from '@/components/Md';
import { TopicGrid } from '@/components/TopicGrid';
import type { GridTopic } from '@/components/TopicGrid';

export const dynamic = 'force-static';

export function generateStaticParams() {
  return SECTION_ORDER.map((section) => ({ section }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ section: string }> }): Promise<Metadata> {
  const { section } = await params;
  const sec = getSection(section as SectionId);
  if (!sec) return {};
  return {
    title: `${sec.name} for competitive exams — notes, topics & free tests`,
    description: `How to prepare ${sec.name} for SSC, Railway, Banking and other govt exams: topic priority, detailed notes, question types, shortcut tricks and free topic-wise tests.`,
  };
}

export default async function SectionPage({ params }: { params: Promise<{ section: string }> }) {
  const { section } = await params;
  const sec = getSection(section as SectionId);
  if (!sec) notFound();
  const meta = SECTION_META[section as SectionId];
  const topics = listTopics(section as SectionId);
  const weight = { high: 0, medium: 0, low: 0 } as Record<string, number>;
  topics.forEach((t) => { if (t.importance) weight[t.importance]++; });

  return (
    <div className="max-w-4xl mx-auto">
      <p className="text-xs font-bold uppercase tracking-wide" style={{ color: meta.color }}>{meta.short} · Subject</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">{sec.name}</h1>
      <div className="flex gap-2 mt-3 flex-wrap text-sm">
        <span className="chip">SSC CGL Tier 1: {sec.tier1.questions} Q · {sec.tier1.marks} marks</span>
        <span className="chip">{topics.length} topics</span>
      </div>
      <Md className="mt-4">{sec.overview}</Md>

      <div className="card p-5 mt-6">
        <h2 className="text-lg font-extrabold">How to prepare this section</h2>
        <Md className="mt-2 text-[15px]">{sec.strategy}</Md>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Topics in study order</h2>
      <p className="text-sm muted mt-1">High importance = asked in nearly every shift. Do these first.
        {weight.high > 0 && <> ({weight.high} high · {weight.medium} medium · {weight.low} low)</>}
      </p>
      {topics.length > 0 ? (
        <TopicGrid section={sec.id} topics={gridTopics(topics, section)} />
      ) : (
        <p className="card p-6 mt-4 text-center muted">Notes for this section are being compiled — check back shortly.</p>
      )}
    </div>
  );
}

/** Build the serializable per-topic payload the client grid renders (studied/test badges live in the browser). */
function gridTopics(cards: ReturnType<typeof listTopics>, section: string): GridTopic[] {
  return cards.map((c) => {
    const t = getTopic(section as SectionId, c.id);
    const practice = t?.practice ?? [];
    const diff = { easy: 0, medium: 0, hard: 0 };
    practice.forEach((q) => { if (q.difficulty && q.difficulty in diff) diff[q.difficulty as keyof typeof diff]++; });
    return {
      id: c.id,
      title: c.title,
      summary: c.summary,
      importance: c.importance,
      avgQ1: c.avgQuestions?.tier1 ?? undefined,
      avgQ2: c.avgQuestions?.tier2 ?? undefined,
      nSub: t?.subtopics.length ?? 0,
      nFormulas: t?.subtopics.reduce((a, s) => a + (s.formulas?.length ?? 0), 0) ?? 0,
      nTricks: t?.subtopics.reduce((a, s) => a + (s.tricks?.length ?? 0), 0) ?? 0,
      nPractice: practice.length,
      difficulty: diff,
    };
  });
}
