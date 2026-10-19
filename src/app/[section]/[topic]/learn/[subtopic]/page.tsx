import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SECTION_META, SECTION_ORDER, getTopic, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { Md, Tex } from '@/components/Md';
import { PracticeSets } from '@/components/PracticeSets';
import { StudiedToggle } from '@/components/StudiedToggle';
import { Example, MistakeCard, SectionHead, Steps, pad2, readMinutes, splitLogic, splitNotes } from '@/components/Lesson';

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

/** Trim to Google's display limits at a word boundary (local, so other templates stay untouched). */
function cap(text: string, max: number) {
  const clean = text.replace(/\s+/g, ' ').trim();
  if (clean.length <= max) return clean;
  const cut = clean.slice(0, max - 1);
  const at = cut.lastIndexOf(' ');
  const base = at > Math.floor(max * 0.5) ? cut.slice(0, at) : cut;
  return `${base.replace(/[\s,;:·—–-]+$/, '')}…`;
}

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string; subtopic: string }> }): Promise<Metadata> {
  const { section, topic, subtopic } = await params;
  const t = getTopic(section as never, topic);
  const s = t?.subtopics.find((x) => x.id === subtopic);
  if (!t || !s) return {};
  const base = `${s.title} — notes & practice`;
  const withTopic = `${base} · ${t.title}`;
  return {
    title: { absolute: cap(withTopic.length <= 60 ? withTopic : base, 60) },
    description: cap(`${s.title} in ${t.title}: notes, worked question types, common mistakes and practice questions for competitive exams.`, 160),
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

  const { sections, traps, recap } = splitNotes(s.notes);
  const patterns = s.patterns ?? [];
  const mistakes = s.mistakes?.length ? s.mistakes : traps;
  const revision = s.revision?.length ? s.revision : recap;
  const minutes = readMinutes(s.concept, s.notes, ...patterns.map((p) => `${p.logic ?? ''} ${(p.steps ?? []).join(' ')} ${p.example?.q ?? ''}`));

  const pageUrl = `https://examshortcut.in/${t.sectionId}/${t.id}/learn/${s.id}/`;
  const lessonLd = [
    {
      '@context': 'https://schema.org', '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
        { '@type': 'ListItem', position: 2, name: meta.name, item: `https://examshortcut.in/${t.sectionId}/` },
        { '@type': 'ListItem', position: 3, name: t.title, item: `https://examshortcut.in/${t.sectionId}/${t.id}/` },
        { '@type': 'ListItem', position: 4, name: 'Learn', item: `https://examshortcut.in/${t.sectionId}/${t.id}/learn/` },
        { '@type': 'ListItem', position: 5, name: s.title, item: pageUrl },
      ],
    },
    {
      '@context': 'https://schema.org', '@type': 'LearningResource',
      name: s.title, url: pageUrl, inLanguage: 'en-IN', isAccessibleForFree: true,
      educationalLevel: 'Competitive exam preparation',
      teaches: patterns.map((p) => p.name),
      isPartOf: { '@type': 'Course', name: t.title, url: `https://examshortcut.in/${t.sectionId}/${t.id}/` },
      provider: { '@type': 'Organization', name: 'ExamShortcut', url: 'https://examshortcut.in/' },
    },
  ];

  // One numbered list drives both the "on this page" box and the section headings.
  const toc: { id: string; title: string }[] = [
    ...sections.map((x) => ({ id: x.id, title: x.title })),
    ...(patterns.length ? [{ id: 'types', title: `Question types (${patterns.length})` }] : []),
    ...(s.formulas?.length ? [{ id: 'formulas', title: 'Formula sheet' }] : []),
    ...(s.tricks?.length ? [{ id: 'shortcuts', title: 'Shortcuts' }] : []),
    ...(mistakes.length ? [{ id: 'mistakes', title: 'Mistakes to avoid' }] : []),
    ...(revision.length ? [{ id: 'revision', title: 'Quick revision' }] : []),
    ...(questions.length ? [{ id: 'practice', title: `Practice (${questions.length} questions)` }] : []),
  ];
  const num = (id: string) => toc.findIndex((x) => x.id === id) + 1;

  return (
    <div className="lesson">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(lessonLd) }} />
      <div className="flex items-center gap-2 mt-4 flex-wrap text-xs faint">
        <Link href={`${learnBase}/`} className="underline decoration-dotted">All subtopics</Link>
        <span>·</span><span>Subtopic {si + 1} of {t.subtopics.length}</span>
      </div>
      <div className="flex items-start gap-3 mt-1">
        <h2 className="text-2xl sm:text-3xl font-extrabold flex-1 leading-tight">{s.title}</h2>
        <StudiedToggle storeKey={`${t.sectionId}/${t.id}/${s.id}`} />
      </div>
      <div className="flex flex-wrap gap-2 mt-3 text-xs">
        <span className="chip">⏱ {minutes} min read</span>
        {patterns.length > 0 && <span className="chip">🧩 {patterns.length} question types</span>}
        {questions.length > 0 && <span className="chip">🎯 {questions.length} practice Q</span>}
      </div>
      <p className="text-xs faint mt-3">By <Link href="/about/" className="underline">Vinay</Link> · <Link href="/editorial-policy/" className="underline">How we check content</Link> · Spotted a mistake? <Link href="/feedback/" className="underline">Tell us</Link></p>

      <div className="card p-4 sm:p-5 mt-5" style={{ borderLeft: '4px solid var(--brand)' }}>
        <div className="kicker">The idea in one minute</div>
        <Md className="mt-1.5">{s.concept}</Md>
      </div>

      {toc.length > 2 && (
        <nav className="card p-3 sm:p-4 mt-4" aria-label="On this page">
          <div className="kicker px-2">On this page</div>
          <div className="toc mt-1.5 sm:grid-cols-2">
            {toc.map((x, k) => <a key={x.id} href={`#${x.id}`}><b>{pad2(k + 1)}</b><span>{x.title}</span></a>)}
          </div>
        </nav>
      )}

      {sections.map((x) => (
        <section key={x.id} id={x.id} className="lesson-sec">
          <SectionHead n={num(x.id)} title={x.title} />
          <Md className="mt-3">{x.body}</Md>
        </section>
      ))}

      {patterns.length > 0 && (
        <section id="types" className="lesson-sec">
          <SectionHead n={num('types')} title="Question types you will see" sub="Each type: how to recognise it, the method step by step, and one question to try." />
          <div className="space-y-4 mt-4">
            {patterns.map((p, k) => {
              const legacy = splitLogic(p.logic);
              const steps = p.steps?.length ? p.steps : legacy.steps;
              const why = p.why ?? legacy.why;
              return (
                <div key={p.id} id={`type-${p.id}`} className="card p-4 sm:p-5 scroll-mt-20">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="kicker" style={{ color: 'var(--brand-text)' }}>Type {k + 1}</span>
                    {p.frequency && <span className={`chip ${FREQ_CHIP[p.frequency] ?? ''}`}>{p.frequency}</span>}
                    {byPattern[p.id] ? <span className="chip">{byPattern[p.id]} practice Q</span> : null}
                  </div>
                  <h4 className="text-lg font-extrabold mt-1 leading-snug">{p.name}</h4>
                  {p.howToSpot && (
                    <div className="spot mt-3"><span aria-hidden>🔍</span><div><b>How to spot it: </b><Md inline>{p.howToSpot}</Md></div></div>
                  )}
                  {p.formula && <div className="formula-box mt-3"><Tex tex={p.formula} display /></div>}
                  {steps.length > 0 && (
                    <div className="mt-3.5">
                      <div className="kicker">Method</div>
                      <div className="mt-1.5"><Steps steps={steps} /></div>
                    </div>
                  )}
                  {legacy.rest && !p.steps?.length && <Md className="mt-2.5">{legacy.rest}</Md>}
                  {why && <div className="text-sm muted mt-3"><b>Why it works: </b><Md inline>{why}</Md></div>}
                  {p.example && <Example ex={p.example} />}
                </div>
              );
            })}
          </div>
        </section>
      )}

      {s.formulas && s.formulas.length > 0 && (
        <section id="formulas" className="lesson-sec">
          <SectionHead n={num('formulas')} title="Formula sheet" />
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mt-4">
            {s.formulas.map((f, k) => (
              <div key={k} className="card p-3.5 min-w-0">
                <div className="text-sm font-bold">{f.name}</div>
                <div className="my-1.5 overflow-x-auto"><Tex tex={f.tex} display /></div>
                {f.note && <p className="text-xs muted">{f.note}</p>}
              </div>
            ))}
          </div>
        </section>
      )}

      {s.tricks && s.tricks.length > 0 && (
        <section id="shortcuts" className="lesson-sec">
          <SectionHead n={num('shortcuts')} title="Shortcuts that save time" />
          <div className="space-y-3 mt-4">
            {s.tricks.map((k, ki) => (
              <div key={ki} className="card p-4 sm:p-5">
                <div className="font-extrabold">⚡ {k.title}</div>
                <Md className="mt-1.5">{k.body}</Md>
                {k.example && <Example ex={k.example} label="Example" />}
              </div>
            ))}
          </div>
        </section>
      )}

      {mistakes.length > 0 && (
        <section id="mistakes" className="lesson-sec">
          <SectionHead n={num('mistakes')} title="Mistakes to avoid" sub="Where most students lose marks on this subtopic." />
          <div className="grid sm:grid-cols-2 gap-2.5 mt-4">
            {mistakes.map((m, k) => <MistakeCard key={k} m={m} i={k} />)}
          </div>
        </section>
      )}

      {revision.length > 0 && (
        <section id="revision" className="lesson-sec">
          <SectionHead n={num('revision')} title="Quick revision" sub="Read this the night before the exam." />
          <div className="card p-4 sm:p-5 mt-4">
            <ul className="check">{revision.map((r, k) => <li key={k}><Md inline>{r}</Md></li>)}</ul>
          </div>
        </section>
      )}

      {questions.length > 0 && (
        <section id="practice" className="lesson-sec">
          <SectionHead n={num('practice')} title={`Practice: ${questions.length} questions`} sub="Sets of 10, mixed across the question types above. Every answer has a step-by-step explanation." />
          <div className="mt-4"><PracticeSets questions={questions} storageKey={`${t.sectionId}/${t.id}/${s.id}`} href={`${learnBase}/${s.id}/`} section={t.sectionId} title={`${meta.short} · ${t.title} · ${s.title}`} /></div>
        </section>
      )}

      <div className="lesson-sec">
        <div className="kicker">Continue learning</div>
        <nav className="grid sm:grid-cols-2 gap-3 mt-2.5 text-sm">
          {prev ? (
            <Link className="card p-4 hover:-translate-y-0.5 transition-transform" href={`${learnBase}/${prev.id}/`}><span className="faint text-xs">← Previous</span><div className="font-bold mt-0.5">{prev.title}</div></Link>
          ) : (
            <Link className="card p-4" href={`${learnBase}/`}><span className="faint text-xs">↑ Back</span><div className="font-bold mt-0.5">All {t.title} subtopics</div></Link>
          )}
          {next ? (
            <Link className="card p-4 sm:text-right hover:-translate-y-0.5 transition-transform" style={{ borderColor: 'var(--brand)' }} href={`${learnBase}/${next.id}/`}><span className="text-xs" style={{ color: 'var(--brand-text)' }}>Next up →</span><div className="font-bold mt-0.5">{next.title}</div></Link>
          ) : (
            <Link className="card p-4 sm:text-right" style={{ borderColor: 'var(--brand)' }} href={`/${t.sectionId}/${t.id}/practice/`}><span className="text-xs" style={{ color: 'var(--brand-text)' }}>Finished the topic →</span><div className="font-bold mt-0.5">Take the full {t.title} test</div></Link>
          )}
        </nav>
      </div>
    </div>
  );
}
