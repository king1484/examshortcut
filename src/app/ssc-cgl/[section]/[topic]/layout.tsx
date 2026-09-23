import Link from 'next/link';
import { notFound } from 'next/navigation';
import { SECTION_META, SECTION_ORDER, getSection, getTopic, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { TopicTabs } from '@/components/TopicTabs';
import { StudiedToggle } from '@/components/StudiedToggle';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return SECTION_ORDER.flatMap((section) =>
    listTopics(section).map((t) => ({ section, topic: t.id })),
  );
}

export default async function TopicLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ section: string; topic: string }>;
}) {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();
  const meta = SECTION_META[section as SectionId];
  const topics = listTopics(section as SectionId);
  const i = topics.findIndex((x) => x.id === t.id);
  const prev = i > 0 ? topics[i - 1] : null;
  const next = i >= 0 && i < topics.length - 1 ? topics[i + 1] : null;
  const nFormulas = t.subtopics.reduce((n, s) => n + (s.formulas?.length ?? 0), 0);
  const nTricks = t.subtopics.reduce((n, s) => n + (s.tricks?.length ?? 0), 0);
  const base = `/ssc-cgl/${t.sectionId}/${t.id}`;

  return (
    <div className="max-w-3xl mx-auto" key={`${t.sectionId}/${t.id}`}>
      <nav className="text-xs faint flex items-center gap-1.5 flex-wrap">
        <Link href="/ssc-cgl/syllabus/" className="underline decoration-dotted">Syllabus</Link> /
        <Link href={`/ssc-cgl/${t.sectionId}/`} className="underline decoration-dotted">{meta.short}</Link> /
        <span>{t.title}</span>
      </nav>

      <div className="flex items-start gap-3 mt-2">
        <h1 className="text-3xl sm:text-4xl font-extrabold flex-1">{t.title}</h1>
        <StudiedToggle storeKey={`${t.sectionId}/${t.id}`} />
      </div>
      <div className="flex gap-2 mt-3 flex-wrap text-sm">
        {t.importance && <span className="chip">{t.importance} importance</span>}
        {t.avgQuestions?.tier1 ? <span className="chip">~{t.avgQuestions.tier1} Q in Tier 1</span> : null}
        {nFormulas > 0 && <span className="chip">{nFormulas} formulas</span>}
        {nTricks > 0 && <span className="chip">⚡ {nTricks} shortcuts</span>}
        <span className="chip">{t.subtopics.length} subtopics</span>
      </div>

      <TopicTabs base={base} nLearn={t.subtopics.length} nFormulas={nFormulas} nExamples={t.solvedExamples?.length ?? 0} nPractice={t.practice?.length ?? 0} />

      {children}

      <nav className="flex justify-between gap-3 mt-12 text-sm">
        {prev ? <Link className="card p-3 flex-1 hover:-translate-y-0.5 transition-transform" href={`/ssc-cgl/${t.sectionId}/${prev.id}/`}>← {prev.title}</Link> : <span className="flex-1" />}
        {next ? <Link className="card p-3 flex-1 text-right hover:-translate-y-0.5 transition-transform" href={`/ssc-cgl/${t.sectionId}/${next.id}/`}>{next.title} →</Link> : <span className="flex-1" />}
      </nav>
    </div>
  );
}
