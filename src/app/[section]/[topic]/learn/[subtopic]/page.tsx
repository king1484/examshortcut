import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, SECTION_ORDER, getTopic, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { Md, Tex } from '@/components/Md';
import { PracticeSets } from '@/components/PracticeSets';
import { StudiedToggle } from '@/components/StudiedToggle';

export const dynamic = 'force-static';
export const dynamicParams = false;

const FREQ_CHIP: Record<string, string> = { 'very common': 'chip-high', common: 'chip-medium', occasional: 'chip-low' };

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
    title: `${s.title} — notes, question types & practice · ${t.title}`,
    description: `${s.title} explained in simple English: detailed notes, every question type asked in SSC, Railway, Banking and other exams with formulas and logic, shortcut tricks and free practice sets.`,
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
  const learnBase = `/${t.sectionId}/${t.id}/learn`;
  const byPattern: Record<string, number> = {};
  questions.forEach((q) => { if (q.pattern) byPattern[q.pattern] = (byPattern[q.pattern] ?? 0) + 1; });

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

      {(s.patterns?.length || questions.length > 0) ? (
        <div className="flex flex-wrap gap-2 mt-4 text-xs">
          {s.notes && <a href="#notes" className="chip">📖 Notes</a>}
          {s.patterns && s.patterns.length > 0 && <a href="#types" className="chip">🧩 {s.patterns.length} question types</a>}
          {s.formulas && s.formulas.length > 0 && <a href="#formulas" className="chip">⚡ Formulas</a>}
          {questions.length > 0 && <a href="#practice" className="chip">🎯 {questions.length} practice Q</a>}
        </div>
      ) : null}

      {s.notes && (
        <section id="notes" className="mt-6 scroll-mt-20">
          <h3 className="text-xl font-extrabold">Detailed notes</h3>
          <Md className="mt-2 text-[15px] notes">{s.notes}</Md>
        </section>
      )}

      {s.patterns && s.patterns.length > 0 && (
        <section id="types" className="mt-8 scroll-mt-20">
          <h3 className="text-xl font-extrabold">Types of questions asked</h3>
          <p className="text-sm muted mt-1">Every way this subtopic shows up in exams — how to recognise it, the formula or logic to use, and a solved example.</p>
          <div className="space-y-3 mt-3">
            {s.patterns.map((p, k) => (
              <details key={p.id} className="card p-4" open={k < 2}>
                <summary className="cursor-pointer flex items-center gap-2 flex-wrap">
                  <span className="font-bold text-sm">Type {k + 1}: {p.name}</span>
                  {p.frequency && <span className={`chip ${FREQ_CHIP[p.frequency] ?? ''}`}>{p.frequency}</span>}
                  {byPattern[p.id] ? <span className="chip">{byPattern[p.id]} practice Q</span> : null}
                </summary>
                {p.howToSpot && <div className="text-sm mt-2.5"><b>How to spot it:</b> <Md inline>{p.howToSpot}</Md></div>}
                {p.formula && <div className="mt-2 overflow-x-auto rounded-lg px-3 py-2" style={{ background: 'var(--surface-2)' }}><Tex tex={p.formula} display /></div>}
                {p.logic && <Md className="mt-2 text-[15px]">{p.logic}</Md>}
                {p.example && (
                  <div className="mt-3 rounded-xl p-3.5 text-sm" style={{ background: 'var(--surface-2)' }}>
                    <Md className="font-semibold">{`**Example:** ${p.example.q}`}</Md>
                    <Md className="mt-1.5">{p.example.solution}</Md>
                  </div>
                )}
              </details>
            ))}
          </div>
        </section>
      )}

      {s.formulas && s.formulas.length > 0 && (
        <div id="formulas" className="mt-8 scroll-mt-20">
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
                    <Md inline className="font-semibold [&_p]:font-semibold">{`Example: ${k.example.q}`}</Md>
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
            {s.mistakes.map((m, k) => <li key={k}><Md inline>{m}</Md></li>)}
          </ul>
        </div>
      )}

      {questions.length > 0 && (
        <section id="practice" className="mt-10 scroll-mt-20">
          <h3 className="text-xl font-extrabold">Practice sets — {questions.length} questions</h3>
          <p className="text-sm muted mt-1">Sets of 10, mixed across the question types above. Each answer comes with a step-by-step explanation.</p>
          <div className="mt-3"><PracticeSets questions={questions} storageKey={`${t.sectionId}/${t.id}/${s.id}`} href={`${learnBase}/${s.id}/`} section={t.sectionId} title={`${meta.short} · ${t.title} · ${s.title}`} /></div>
        </section>
      )}

      <nav className="flex justify-between gap-3 mt-10 text-sm">
        {prev ? <Link className="card p-3 flex-1 hover:-translate-y-0.5 transition-transform" href={`${learnBase}/${prev.id}/`}>← {prev.title}</Link> : <Link className="card p-3 flex-1" href={`${learnBase}/`}>↑ All subtopics</Link>}
        {next ? <Link className="card p-3 flex-1 text-right hover:-translate-y-0.5 transition-transform" href={`${learnBase}/${next.id}/`}>{next.title} →</Link> : <Link className="card p-3 flex-1 text-right" href={`/${t.sectionId}/${t.id}/practice/`}>Take the full topic test →</Link>}
      </nav>
    </div>
  );
}
