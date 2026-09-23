import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, SECTION_ORDER, getSection, getTopic, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { Md, Tex } from '@/components/Md';
import { SolvedExample } from '@/components/SolvedExample';
import { TopicQuiz } from '@/components/TopicQuiz';
import { StudiedToggle } from '@/components/StudiedToggle';

export const dynamic = 'force-static';

export function generateStaticParams() {
  return SECTION_ORDER.flatMap((section) =>
    listTopics(section).map((t) => ({ section, topic: t.id })),
  );
}
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string }> }): Promise<Metadata> {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) return {};
  const nFormulas = t.subtopics.reduce((n, s) => n + (s.formulas?.length ?? 0), 0);
  const nTricks = t.subtopics.reduce((n, s) => n + (s.tricks?.length ?? 0), 0);
  return {
    title: `SSC CGL ${t.title}: formulas, shortcut tricks & free test`,
    description: `${t.title} for SSC CGL: ${nFormulas}+ formulas, ${nTricks} shortcut tricks with examples, recurring PYQ patterns, solved questions and a free ${t.practice?.length ?? 0}-question topic test.`,
  };
}

const IMP_CHIP: Record<string, string> = { high: 'chip-high', medium: 'chip-medium', low: 'chip-low' };
const FREQ_CHIP: Record<string, string> = { 'very common': 'chip-high', common: 'chip-medium', occasional: 'chip-low' };

export default async function TopicPage({ params }: { params: Promise<{ section: string; topic: string }> }) {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();
  const sec = getSection(section as SectionId);
  const meta = SECTION_META[section as SectionId];
  const topics = listTopics(section as SectionId);
  const i = topics.findIndex((x) => x.id === t.id);
  const prev = i > 0 ? topics[i - 1] : null;
  const next = i >= 0 && i < topics.length - 1 ? topics[i + 1] : null;
  const nFormulas = t.subtopics.reduce((n, s) => n + (s.formulas?.length ?? 0), 0);
  const nTricks = t.subtopics.reduce((n, s) => n + (s.tricks?.length ?? 0), 0);
  const storeKey = `${t.sectionId}/${t.id}`;

  return (
    <div className="max-w-3xl mx-auto">
      <nav className="text-xs faint flex items-center gap-1.5 flex-wrap">
        <Link href="/ssc-cgl/syllabus/" className="underline decoration-dotted">Syllabus</Link> /
        <Link href={`/ssc-cgl/${t.sectionId}/`} className="underline decoration-dotted">{meta.short}</Link> /
        <span>{t.title}</span>
      </nav>

      <div className="flex items-start gap-3 mt-2">
        <h1 className="text-3xl sm:text-4xl font-extrabold flex-1">{t.title}</h1>
        <StudiedToggle storeKey={storeKey} />
      </div>
      <div className="flex gap-2 mt-3 flex-wrap text-sm">
        {t.importance && <span className={`chip ${IMP_CHIP[t.importance]}`}>{t.importance} importance</span>}
        {t.avgQuestions?.tier1 ? <span className="chip">~{t.avgQuestions.tier1} Q in Tier 1</span> : null}
        {t.avgQuestions?.tier2 ? <span className="chip">~{t.avgQuestions.tier2} Q in Tier 2</span> : null}
        {nFormulas > 0 && <span className="chip">{nFormulas} formulas</span>}
        {nTricks > 0 && <span className="chip">⚡ {nTricks} shortcuts</span>}
        {t.practice?.length ? <span className="chip">{t.practice.length}-Q test</span> : null}
      </div>
      <Md className="mt-3 text-[15px]">{t.summary}</Md>

      {t.pyqPatterns && t.pyqPatterns.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Question patterns SSC repeats</h2>
          <div className="space-y-2.5 mt-3">
            {t.pyqPatterns.map((p, k) => (
              <div key={k} className="card p-4">
                <div className="flex items-center gap-2 flex-wrap">
                  <h3 className="font-bold text-sm">{p.pattern}</h3>
                  {p.frequency && <span className={`chip ${FREQ_CHIP[p.frequency] ?? ''}`}>{p.frequency}</span>}
                </div>
                {p.howToSpot && <p className="text-sm mt-1.5"><b>Spot it:</b> {p.howToSpot}</p>}
                {p.approach && <p className="text-sm mt-1"><b>Attack:</b> {p.approach}</p>}
              </div>
            ))}
          </div>
        </>
      )}

      {t.subtopics.map((s, si) => (
        <section key={s.id} id={s.id} className="mt-10 scroll-mt-24">
          <h2 className="text-2xl font-extrabold">{si + 1}. {s.title}</h2>
          <Md className="mt-2 text-[15px]">{s.concept}</Md>

          {s.formulas && s.formulas.length > 0 && (
            <div className="mt-4">
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
            <div className="mt-5">
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
            <div className="mt-4 rounded-xl p-4" style={{ background: 'var(--bad-soft)' }}>
              <h3 className="text-xs font-bold uppercase tracking-wide" style={{ color: 'var(--bad)' }}>Where students lose marks</h3>
              <ul className="list-disc pl-5 text-sm mt-1.5 space-y-1">
                {s.mistakes.map((m, k) => <li key={k}>{m}</li>)}
              </ul>
            </div>
          )}
        </section>
      ))}

      {t.solvedExamples && t.solvedExamples.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-12">Worked examples</h2>
          <div className="mt-3 space-y-3">
            {t.solvedExamples.map((q, k) => <SolvedExample key={q.id} q={q} n={k + 1} />)}
          </div>
        </>
      )}

      {t.practice && t.practice.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-12">Topic test</h2>
          <div className="mt-3"><TopicQuiz questions={t.practice} storageKey={storeKey} href={`/ssc-cgl/${t.sectionId}/${t.id}/`} section={t.sectionId} title={`${meta.short} · ${t.title}`} /></div>
        </>
      )}

      <nav className="flex justify-between gap-3 mt-12 text-sm">
        {prev ? <Link className="card p-3 flex-1 hover:-translate-y-0.5 transition-transform" href={`/ssc-cgl/${t.sectionId}/${prev.id}/`}>← {prev.title}</Link> : <span className="flex-1" />}
        {next ? <Link className="card p-3 flex-1 text-right hover:-translate-y-0.5 transition-transform" href={`/ssc-cgl/${t.sectionId}/${next.id}/`}>{next.title} →</Link> : <span className="flex-1" />}
      </nav>
      {sec && <p className="text-xs faint mt-6">Part of <Link className="underline" href={`/ssc-cgl/${sec.id}/`}>{sec.name}</Link> · <Link className="underline" href="/revision/">your progress</Link></p>}
    </div>
  );
}
