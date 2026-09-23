import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, SECTION_ORDER, getSection, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { Md } from '@/components/Md';

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
    title: `SSC CGL ${sec.name} — strategy, topics & free tests`,
    description: `How to prepare ${sec.name} for SSC CGL Tier 1 & Tier 2: topic priority, ${sec.tier1.questions}Q/${sec.tier1.marks} marks in Tier 1, shortcut tricks and free topic-wise tests.`,
  };
}

const IMP_CHIP: Record<string, string> = { high: 'chip-high', medium: 'chip-medium', low: 'chip-low' };

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
      <p className="text-xs font-bold uppercase tracking-wide" style={{ color: meta.color }}>{meta.short} · SSC CGL</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">{sec.name}</h1>
      <div className="flex gap-2 mt-3 flex-wrap text-sm">
        <span className="chip">Tier 1: {sec.tier1.questions} Q · {sec.tier1.marks} marks</span>
        <span className="chip">Tier 2: {sec.tier2.questions} Q · {sec.tier2.marks} marks</span>
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
      <div className="grid sm:grid-cols-2 gap-3 mt-4">
        {topics.map((t, i) => (
          <Link key={t.id} href={`/ssc-cgl/${sec.id}/${t.id}/`} className="card p-4 hover:-translate-y-0.5 transition-transform flex flex-col">
            <div className="flex items-center gap-2">
              <span className="text-xs faint font-bold">#{i + 1}</span>
              <span className="font-bold">{t.title}</span>
              {t.importance && <span className={`chip ml-auto ${IMP_CHIP[t.importance]}`}>{t.importance}</span>}
            </div>
            <p className="text-sm muted mt-1.5 line-clamp-2">{t.summary}</p>
            <div className="text-xs faint mt-2 flex gap-3 flex-wrap">
              <span>{t.subtopics.length} subtopics</span>
              {t.avgQuestions?.tier1 ? <span>~{t.avgQuestions.tier1} Q/Tier 1</span> : null}
              {t.practice?.length ? <span>{t.practice.length}-Q test</span> : null}
              {t.solvedExamples?.length ? <span>{t.solvedExamples.length} solved</span> : null}
            </div>
          </Link>
        ))}
      </div>
      {topics.length === 0 && <p className="card p-6 mt-4 text-center muted">Notes for this section are being compiled — check back shortly.</p>}
    </div>
  );
}
