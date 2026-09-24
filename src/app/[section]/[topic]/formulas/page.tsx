import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getTopic } from '@/lib/content';
import { LazyTex } from '@/components/LazyTex';
import { PrintButton } from '@/components/TopicTabs';

export const dynamic = 'force-static';
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string }> }): Promise<Metadata> {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) return {};
  const n = t.subtopics.reduce((acc, s) => acc + (s.formulas?.length ?? 0), 0);
  return {
    title: `${t.title} — all ${n} formulas (printable)`,
    description: `Every ${t.title} formula for competitive exams on one printable page, grouped by subtopic with usage notes.`,
  };
}

export default async function FormulasPage({ params }: { params: Promise<{ section: string; topic: string }> }) {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();
  const groups = t.subtopics.filter((s) => (s.formulas?.length ?? 0) > 0);

  return (
    <div>
      <div className="flex items-center justify-between gap-3 mt-4 flex-wrap">
        <p className="muted text-sm">Every formula in this topic, grouped by subtopic. Print it and pin it above your desk.</p>
        <PrintButton />
      </div>
      {groups.length === 0 && <p className="card p-6 mt-4 text-center muted">No formulas in this topic — it's a technique/logic topic. Head to <Link className="underline" href={`/${t.sectionId}/${t.id}/learn/`}>Learn</Link> instead.</p>}
      {groups.map((s) => (
        <section key={s.id} className="mt-6">
          <h2 className="font-extrabold">{s.title}</h2>
          <div className="grid sm:grid-cols-2 gap-2.5 mt-2.5">
            {s.formulas!.map((f, k) => (
              <div key={k} className="card p-3.5">
                <div className="text-sm font-bold">{f.name}</div>
                <div className="my-1.5 overflow-x-auto overflow-y-hidden py-0.5"><LazyTex tex={f.tex} display /></div>
                {f.note && <p className="text-xs muted">{f.note}</p>}
              </div>
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}
