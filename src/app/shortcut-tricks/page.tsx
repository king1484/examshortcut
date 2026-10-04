import Link from 'next/link';
import type { Metadata } from 'next';
import { availableSections, listTopics, listMocks, SECTION_META, sectionIntro, topicBlurb } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import type { Topic, Trick } from '@/lib/types';
import { MathText } from '@/components/MathText';

export const dynamic = 'force-static';

const PAGE_URL = 'https://examshortcut.in/shortcut-tricks/';

/** Every trick in the notes, with where it lives. */
function collect() {
  return availableSections().map((sid) => {
    const topics = listTopics(sid)
      .map((t) => ({
        t,
        count: t.subtopics.reduce((n, s) => n + (s.tricks?.length ?? 0), 0),
      }))
      .filter((x) => x.count > 0);
    return { sid, topics, count: topics.reduce((n, x) => n + x.count, 0) };
  });
}

export function generateMetadata(): Metadata {
  const total = collect().reduce((n, s) => n + s.count, 0);
  const floor = Math.floor(total / 100) * 100;
  return {
    title: `SSC shortcut tricks: ${floor}+ maths, reasoning & GK tricks`,
    description: `Free SSC CGL shortcut tricks, organised by subject and topic: ${total} short, checkable tricks for Quant, Reasoning, English, GA and Computer, with previews, worked examples and links to the full notes and practice.`,
    alternates: { canonical: '/shortcut-tricks/' },
  };
}

/** A "top trick" is the first trick with a compact worked example in a high-importance topic, one per topic. */
function topTricks(): { topic: Topic; sub: string; subTitle: string; trick: Trick }[] {
  const out: { topic: Topic; sub: string; subTitle: string; trick: Trick }[] = [];
  for (const sid of ['quant', 'reasoning'] as SectionId[]) {
    for (const t of listTopics(sid)) {
      if (t.importance !== 'high') continue;
      let found = false;
      for (const s of t.subtopics) {
        for (const k of s.tricks ?? []) {
          const ex = k.example;
          if (!found && ex?.answer && ex.q.length <= 150 && !ex.q.includes('\n') && k.body.length <= 220) {
            out.push({ topic: t, sub: s.id, subTitle: s.title, trick: k });
            found = true;
          }
        }
        if (found) break;
      }
    }
  }
  // Spread across the most-asked topics rather than taking the first twelve alphabetically
  const FIRST = ['percentage', 'profit-loss-discount', 'time-work', 'time-speed-distance', 'ratio-proportion', 'average',
    'number-system', 'interest', 'blood-relations', 'coding-decoding', 'syllogism', 'series'];
  const rank = (id: string) => { const i = FIRST.indexOf(id); return i === -1 ? FIRST.length : i; };
  return out.sort((a, b) => rank(a.topic.id) - rank(b.topic.id)).slice(0, 12);
}

export default function ShortcutTricksPage() {
  const sections = collect();
  const total = sections.reduce((n, s) => n + s.count, 0);
  const topicCount = sections.reduce((n, s) => n + s.topics.length, 0);
  const top = topTricks();
  const mocks = listMocks().filter((m) => m.available);

  const ld = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
      { '@type': 'ListItem', position: 2, name: 'SSC shortcut tricks', item: PAGE_URL },
    ],
  };

  return (
    <div className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />

      <p className="text-xs font-bold uppercase tracking-wide faint">Shortcut tricks · all subjects</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">SSC shortcut tricks</h1>
      <div className="flex gap-2 mt-3 flex-wrap text-sm">
        <span className="chip chip-brand">{total} tricks</span>
        <span className="chip">{topicCount} topics</span>
        <span className="chip">{sections.length} subjects</span>
      </div>
      <p className="mt-4 text-[15px] muted">
        SSC CGL Tier 1 gives you 60 minutes for 100 questions, so the real skill is not solving a question, it is
        solving it in under a minute. This page collects every shortcut trick in the ExamShortcut notes in one place,
        grouped by subject and topic. Each trick is a small, checkable idea: a pattern to spot, a calculation you can do
        in your head, or an elimination rule that saves you a full working. Nothing here is a trick without a reason, and
        every one links back to the full subtopic page where it sits next to the formula it depends on and a worked
        example.
      </p>
      <p className="mt-3 text-[15px] muted">
        Use it two ways. If you have a weak topic, jump to that subject below and read the previews for it, then open the
        topic page for the full notes. If you are in the last two weeks, read the top tricks first, then drill the
        topics where you lose the most time in a timed mock. A shortcut only helps when you can recall it without
        thinking, so after reading one, solve three questions with it before moving on.
      </p>

      <nav aria-label="Jump to subject" className="card p-3.5 mt-6 flex flex-wrap gap-2 items-center text-sm">
        <span className="font-bold">Jump to:</span>
        <a href="#top-tricks" className="chip">Top tricks</a>
        {sections.map((s) => (
          <a key={s.sid} href={`#${s.sid}`} className="chip">{SECTION_META[s.sid].short} · {s.count}</a>
        ))}
        <a href="#practice" className="chip">Practise</a>
      </nav>

      <section id="top-tricks" className="mt-10 scroll-mt-24">
        <h2 className="text-2xl font-extrabold">Top shortcut tricks to learn first</h2>
        <p className="text-sm muted mt-1 max-w-3xl">
          One compact trick from each high-priority Quant and Reasoning topic (the ones asked in nearly every shift),
          each with a one-line check so you can see it work. Read the full topic for the rest of that topic&apos;s
          tricks.
        </p>
        <div className="grid sm:grid-cols-2 gap-2.5 mt-3">
          {top.map(({ topic, sub, subTitle, trick }) => (
            <div key={`${topic.id}-${trick.title}`} className="card p-3.5 text-sm">
              <div className="text-xs font-semibold faint">
                <Link href={`/${topic.sectionId}/${topic.id}/`} className="underline decoration-dotted">{topic.title}</Link>
                {' · '}{subTitle}
              </div>
              <div className="font-bold mt-1">⚡ {trick.title}</div>
              <p className="muted mt-1"><MathText text={trick.body} /></p>
              {trick.example && (
                <p className="text-xs mt-2">
                  <span className="font-semibold">Check: </span>
                  <MathText text={trick.example.q} /> <span className="font-semibold">Answer: </span>
                  <MathText text={trick.example.answer ?? ''} />
                </p>
              )}
              <Link href={`/${topic.sectionId}/${topic.id}/learn/${sub}/`} className="text-xs underline decoration-dotted mt-2 inline-block">
                Full notes for {subTitle} →
              </Link>
            </div>
          ))}
        </div>
      </section>

      {sections.map(({ sid, topics, count }) => {
        const meta = SECTION_META[sid];
        return (
          <section key={sid} id={sid} className="mt-12 scroll-mt-24">
            <h2 className="text-2xl font-extrabold pb-1 border-b-2" style={{ color: meta.color, borderColor: meta.color }}>
              {meta.name}
            </h2>
            <p className="text-xs faint mt-1">{count} tricks across {topics.length} topics</p>
            {sectionIntro(sid) && <p className="text-sm muted mt-2 max-w-3xl">{sectionIntro(sid)}</p>}
            <div className="grid gap-3 mt-4">
              {topics.map(({ t, count: n }) => {
                const flat = t.subtopics.flatMap((s) => (s.tricks ?? []).map((k) => ({ s, k })));
                const preview = flat.slice(0, 3);
                return (
                  <article key={t.id} className="card p-4">
                    <div className="flex items-baseline justify-between gap-2 flex-wrap">
                      <h3 className="font-extrabold text-lg">
                        <Link href={`/${sid}/${t.id}/`} className="hover:underline">{t.title}</Link>
                      </h3>
                      <span className="text-xs faint">
                        {n} tricks
                        {t.importance && <> · <span className={`chip ${t.importance === 'high' ? 'chip-high' : t.importance === 'medium' ? 'chip-medium' : 'chip-low'}`}>{t.importance} priority</span></>}
                      </span>
                    </div>
                    <p className="text-xs muted mt-1">{topicBlurb(t)}</p>
                    <ul className="mt-2.5 space-y-1.5 text-sm">
                      {preview.map(({ s, k }) => (
                        <li key={`${s.id}-${k.title}`}>
                          <span className="font-bold">⚡ {k.title}.</span>{' '}
                          <MathText text={k.body} max={150} className="muted" />{' '}
                          <Link href={`/${sid}/${t.id}/learn/${s.id}/`} className="text-xs underline decoration-dotted whitespace-nowrap">{s.title} →</Link>
                        </li>
                      ))}
                    </ul>
                    {flat.length > preview.length && (
                      <details className="mt-3 text-sm">
                        <summary className="cursor-pointer font-semibold">All {n} trick titles in {t.title}</summary>
                        <div className="mt-2 space-y-2">
                          {t.subtopics.filter((s) => s.tricks?.length).map((s) => (
                            <div key={s.id}>
                              <Link href={`/${sid}/${t.id}/learn/${s.id}/`} className="text-xs font-bold underline decoration-dotted">{s.title}</Link>
                              <ul className="list-disc pl-5 text-xs muted">
                                {s.tricks!.map((k) => <li key={k.title}>{k.title}</li>)}
                              </ul>
                            </div>
                          ))}
                        </div>
                      </details>
                    )}
                    <div className="flex gap-3 mt-3 text-xs flex-wrap">
                      <Link href={`/${sid}/${t.id}/learn/`} className="underline decoration-dotted">Learn</Link>
                      <Link href={`/${sid}/${t.id}/formulas/`} className="underline decoration-dotted">Formulas</Link>
                      <Link href={`/${sid}/${t.id}/practice/`} className="underline decoration-dotted">Practice &amp; test</Link>
                    </div>
                  </article>
                );
              })}
            </div>
          </section>
        );
      })}

      <section id="practice" className="card p-5 mt-12 scroll-mt-24">
        <h2 className="text-xl font-extrabold">Turn tricks into speed</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          Reading a trick is the easy half. Speed comes from using it under a clock, so pair this page with timed
          practice: a daily quiz to keep the habit, a topic test for each weak area, and full-length mocks to check that
          the tricks survive exam pressure. If a trick fails on a question, go back to the standard method for that
          topic; the notes show both.
        </p>
        <div className="flex gap-2 mt-3 flex-wrap">
          <Link href="/daily-quiz/" className="btn btn-brand">Daily quiz</Link>
          <Link href="/exams/ssc-cgl/mocks/" className="btn">Mock tests{mocks.length ? ` (${mocks.length})` : ''}</Link>
          <Link href="/formula-sheet/" className="btn">Formula sheet</Link>
          <Link href="/quant-formulas/" className="btn">Quant formulas</Link>
          <Link href="/data-interpretation/" className="btn">Data interpretation</Link>
          <Link href="/learn/" className="btn">All subjects</Link>
        </div>
      </section>
    </div>
  );
}
