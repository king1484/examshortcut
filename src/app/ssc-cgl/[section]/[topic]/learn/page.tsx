import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getTopic } from '@/lib/content';
import { StudiedToggle } from '@/components/StudiedToggle';

export const dynamic = 'force-static';
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string }> }): Promise<Metadata> {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) return {};
  return {
    title: `${t.title} — learn: ${t.subtopics.map((s) => s.title).join(', ')}`,
    description: `Learn ${t.title} for SSC CGL subtopic by subtopic: concepts, formulas, shortcut tricks and common mistakes, each on its own page with a quick quiz.`,
  };
}

export default async function LearnIndexPage({ params }: { params: Promise<{ section: string; topic: string }> }) {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();
  const base = `/ssc-cgl/${t.sectionId}/${t.id}/learn`;

  return (
    <div>
      <p className="muted text-sm mt-4">The learning path, in order. Each subtopic is its own page — concept first, then formulas, shortcut tricks, traps to avoid, and a mini-quiz to lock it in.</p>
      <div className="mt-4 space-y-2.5">
        {t.subtopics.map((s, i) => {
          const nF = s.formulas?.length ?? 0;
          const nT = s.tricks?.length ?? 0;
          const nQ = (t.practice ?? []).filter((q) => q.subtopic === s.id).length;
          return (
            <div key={s.id} className="card p-4 flex items-center gap-3">
              <div className="w-8 h-8 rounded-full shrink-0 font-extrabold text-sm flex items-center justify-center" style={{ background: 'var(--surface-2)', color: 'var(--ink-2)' }}>{i + 1}</div>
              <div className="flex-1 min-w-0">
                <Link href={`${base}/${s.id}/`} className="font-bold hover:underline">{s.title}</Link>
                <div className="text-xs faint mt-0.5 flex gap-2.5 flex-wrap">
                  {nF > 0 && <span>{nF} formulas</span>}
                  {nT > 0 && <span>⚡ {nT} tricks</span>}
                  {nQ > 0 && <span>{nQ}-Q quiz</span>}
                </div>
              </div>
              <StudiedToggle storeKey={`${t.sectionId}/${t.id}/${s.id}`} />
              <Link href={`${base}/${s.id}/`} className="btn btn-brand text-xs shrink-0" style={{ padding: '.35rem .7rem' }}>Open</Link>
            </div>
          );
        })}
      </div>
    </div>
  );
}
