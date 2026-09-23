import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, SECTION_ORDER, getTopic, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { Md, Tex } from '@/components/Md';
import { TopicQuiz } from '@/components/TopicQuiz';
import { StudiedToggle } from '@/components/StudiedToggle';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** listTopics returns lightweight cards; subtopic routes need full topics. */
function allFullTopics(section: string) {
  return listTopics(section as never)
    .map((c) => getTopic(section as never, c.id))
    .filter(Boolean) as NonNullable<ReturnType<typeof getTopic>>[];
}

export function generateStaticParams() {
  return SECTION_ORDER.flatMap((section) =>
    allFullTopics(section).flatMap((t) => t.subtopics.map((s) => ({ section, topic: t.id, subtopic: s.id }))),
  );
}

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string; subtopic: string }> }): Promise<Metadata> {
  const { section, topic, subtopic } = await params;
  const t = getTopic(section as never, topic);
  const s = t?.subtopics.find((x) => x.id === subtopic);
  if (!t || !s) return {};
  return {
    title: `${s.title} — ${t.title} · SSC CGL`,
    description: `${s.title} explained for SSC CGL: concept, all formulas, shortcut tricks, common mistakes and a mini-quiz. Part of our free ${t.title} guide.`,
  };
}

export default async function SubtopicPage({ params }: { params: Promise<{ section: string; topic: string; subtopic: string }> }) {
  const { section, topic, subtopic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();
  const si = t.subtopics.findIndex((x) => x.id === subtopic);
  if (si < 0) notFound();
  const s = t.subtopics[si];
  const meta = SECTION_META[t.sectionId as SectionId];
  const prev = si > 0 ? t.subtopics[si - 1] : null;
  const next = si < t.subtopics.length - 1 ? t.subtopics[si + 1] : null;
  const questions = (t.practice ?? []).filter((q) => q.subtopic === s.id);
  const learnBase = `/ssc-cgl/${t.sectionId}/${t.id}/learn`;

  return (
    <div>
      <div className="flex items-center gap-2 mt-4 flex-wrap text-xs faint">
        <span>Subtopic {si + 1} of {t.subtopics.length}</span>
        {prev && <><span>·</span><Link href={`${learnBase}/${prev.id}/`} className="underline decoration-dotted">← {prev.title}</Link></>}
        {next && <><span>·</span><Link href={`${learnBase}/${next.id}/`} className="underline decoration-dotted">{next.title} →</Link></>}
      </div>
      <div className="flex items-start gap-3 mt-1">
        <h2 className="text-2xl font-extrabold flex-1">{s.title}</h2>
        <StudiedToggle storeKey={`${t.sectionId}/${t.id}/${s.id}`} />
      </div>

      <Md className="mt-3 text-[15px]">{s.concept}</Md>

      {s.formulas && s.formulas.length > 0 && (
        <div className="mt-5">
          <h3 className="text-xs font-bold uppercase tracking-wide faint">Formulas</h3>
          <div className="grid sm:grid-cols-2 gap-2.5 mt-2">
            {s.formulas.map((f, k) => (
              <div key={k} className="card p-3.5">
                <div className="text-sm font-bold">{f.name}</div>
                <div className="my-1.5 overflow-x-auto"><Tex tex={f.tex} display /></div>
                {f.note && <p className="text-xs muted">{f.note}</p>}
              </div>
            ))}
          </div>
        </div>
      )}

      {s.tricks && s.tricks.length > 0 && (
        <div className="mt-6">
          <h3 className="text-xs font-bold uppercase tracking-wide faint">Shortcut tricks</h3>
          <div className="space-y-2.5 mt-2">
            {s.tricks.map((k, ki) => (
              <details key={ki} className="card p-4" open={ki === 0}>
                <summary className="font-bold text-sm cursor-pointer">⚡ {k.title}</summary>
                <Md className="mt-2 text-[15px]">{k.body}</Md>
                {k.example && (
                  <div className="mt-3 rounded-xl p-3.5 text-sm" style={{ background: 'var(--surface-2)' }}>
                    <p className="font-semibold">Example: {k.example.q}</p>
                    <Md className="mt-1.5">{k.example.solution}</Md>
                  </div>
                )}
              </details>
            ))}
          </div>
        </div>
      )}

      {s.mistakes && s.mistakes.length > 0 && (
        <div className="mt-5 rounded-xl p-4" style={{ background: 'var(--bad-soft)' }}>
          <h3 className="text-xs font-bold uppercase tracking-wide" style={{ color: 'var(--bad)' }}>Where students lose marks</h3>
          <ul className="list-disc pl-5 text-sm mt-1.5 space-y-1">
            {s.mistakes.map((m, k) => <li key={k}>{m}</li>)}
          </ul>
        </div>
      )}

      {questions.length > 0 && (
        <div className="mt-8">
          <h3 className="text-lg font-extrabold">Lock it in — {questions.length}-question mini-quiz</h3>
          <div className="mt-3"><TopicQuiz questions={questions} storageKey={`${t.sectionId}/${t.id}/${s.id}`} href={`${learnBase}/${s.id}/`} section={t.sectionId} title={`${meta.short} · ${t.title} · ${s.title}`} /></div>
        </div>
      )}

      <nav className="flex justify-between gap-3 mt-10 text-sm">
        {prev ? <Link className="card p-3 flex-1 hover:-translate-y-0.5 transition-transform" href={`${learnBase}/${prev.id}/`}>← {prev.title}</Link> : <Link className="card p-3 flex-1" href={`${learnBase}/`}>↑ All subtopics</Link>}
        {next ? <Link className="card p-3 flex-1 text-right hover:-translate-y-0.5 transition-transform" href={`${learnBase}/${next.id}/`}>{next.title} →</Link> : <Link className="card p-3 flex-1 text-right" href={`/ssc-cgl/${t.sectionId}/${t.id}/practice/`}>Take the full topic test →</Link>}
      </nav>
    </div>
  );
}
