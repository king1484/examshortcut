import Link from 'next/link';
import type { Metadata } from 'next';
import { availableSections, SECTION_META, listTopics, getSection } from '@/lib/content';
import { Md } from '@/components/Md';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL syllabus 2026 — topic-wise, with free notes & shortcut tricks',
  description: 'Complete SSC CGL Tier 1 + Tier 2 syllabus organised topic by topic: Quant, Reasoning, English, General Awareness and Computer. Each topic has formulas, shortcuts, tricks and a free topic test.',
};

export default function SyllabusPage() {
  const sections = availableSections();

  return (
    <div className="max-w-5xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">SSC CGL syllabus, topic by topic</h1>
      <p className="muted mt-2 max-w-3xl">
        The exact topics SSC asks, ordered by what gives the most marks for your time. Every topic page has:
        concept notes → all formulas → <b>shortcut tricks with worked examples</b> → mistakes to avoid → the recurring
        question patterns → a free topic test.
      </p>

      {sections.map((sid) => {
        const sec = getSection(sid);
        const topics = listTopics(sid);
        const meta = SECTION_META[sid];
        return (
          <section key={sid} className="mt-8">
            <div className="flex items-baseline justify-between flex-wrap gap-2">
              <h2 className="text-2xl font-extrabold" style={{ color: meta.color }}>{meta.name}</h2>
              <Link href={`/${sid}/`} className="text-sm underline decoration-dotted">Section strategy →</Link>
            </div>
            {sec && <p className="text-xs faint mt-0.5">Tier 1: {sec.tier1.questions}Q · {sec.tier1.marks} marks · Tier 2: {sec.tier2.questions}Q · {sec.tier2.marks} marks</p>}
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-2.5 mt-3">
              {topics.map((t) => (
                <Link key={t.id} href={`/${sid}/${t.id}/`} className="card p-3.5 flex flex-col hover:-translate-y-0.5 transition-transform">
                  <div className="flex items-center gap-2">
                    <span className="font-bold text-sm">{t.title}</span>
                    {t.importance && <span className={`chip ml-auto ${t.importance === 'high' ? 'chip-high' : t.importance === 'medium' ? 'chip-medium' : 'chip-low'}`}>{t.importance}</span>}
                  </div>
                  <Md inline className="text-xs muted mt-1 line-clamp-2 [&_p]:text-xs">{t.summary}</Md>
                  <span className="text-xs faint mt-2">
                    {t.subtopics.length} subtopics
                    {t.avgQuestions?.tier1 ? ` · ~${t.avgQuestions.tier1} Q in Tier 1` : ''}
                    {t.practice?.length ? ` · ${t.practice.length}-Q test` : ''}
                  </span>
                </Link>
              ))}
            </div>
          </section>
        );
      })}
      {sections.length === 0 && <p className="card p-6 mt-6 text-center muted">Notes are being compiled right now — check back shortly.</p>}
    </div>
  );
}
