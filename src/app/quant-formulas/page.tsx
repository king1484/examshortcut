import Link from 'next/link';
import type { Metadata } from 'next';
import { listTopics, topicBlurb, sectionIntro } from '@/lib/content';
import { LazyTex } from '@/components/LazyTex';

export const dynamic = 'force-static';

const PAGE_URL = 'https://examshortcut.in/quant-formulas/';

function quantTopics() {
  return listTopics('quant')
    .map((t) => ({
      t,
      subs: t.subtopics.filter((s) => (s.formulas?.length ?? 0) > 0),
    }))
    .filter((x) => x.subs.length > 0)
    .map((x) => ({ ...x, count: x.subs.reduce((n, s) => n + s.formulas!.length, 0) }));
}

export function generateMetadata(): Metadata {
  const total = quantTopics().reduce((n, x) => n + x.count, 0);
  return {
    title: `SSC CGL maths formulas: ${total} Quant formulas by topic`,
    description: `All ${total} Quantitative Aptitude formulas for SSC CGL and other govt exams, grouped by topic and subtopic with usage notes: Number System, Percentage, Algebra, Geometry, Mensuration, Trigonometry and more.`,
    alternates: { canonical: '/quant-formulas/' },
  };
}

export default function QuantFormulasPage() {
  const topics = quantTopics();
  const total = topics.reduce((n, x) => n + x.count, 0);
  const intro = sectionIntro('quant');

  const ld = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
      { '@type': 'ListItem', position: 2, name: 'Quantitative Aptitude', item: 'https://examshortcut.in/quant/' },
      { '@type': 'ListItem', position: 3, name: 'Quant formulas', item: PAGE_URL },
    ],
  };

  return (
    <div className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />

      <p className="text-xs font-bold uppercase tracking-wide" style={{ color: 'var(--c-quant)' }}>Quant · Formulas by topic</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">SSC CGL maths formulas, topic-wise</h1>
      <div className="flex gap-2 mt-3 flex-wrap text-sm">
        <span className="chip chip-brand">{total} formulas</span>
        <span className="chip">{topics.length} topics</span>
      </div>

      <p className="mt-4 text-[15px] muted">
        This is the Quantitative Aptitude formula reference for SSC CGL, Railway and other government exams, organised the
        way you actually study: by topic, then by subtopic. Every topic below has its own anchor, so you can bookmark
        <span className="whitespace-nowrap"> /quant-formulas/#percentage</span> or any other topic and come straight back
        to it. Each formula has a name and, where the usage is not obvious, a one-line note on when to apply it.
      </p>
      <p className="mt-3 text-[15px] muted">
        {intro ? <>{intro} </> : null}
        Formulas are the cheapest marks in Quant: a question that takes three minutes without the right formula takes
        thirty seconds with it. But a formula you only recognise is not enough. You need to recall it, and to know which
        question types call for it. For that, each topic links to its notes (with every question type), a printable
        topic formula page, and a timed practice test. If you want these formulas together with shortcut tricks for
        Reasoning, English and GA on one printable page, use the <Link href="/formula-sheet/" className="underline decoration-dotted">full formula sheet</Link>;
        this page is the Quant-only, topic-first version.
      </p>

      <nav aria-label="Quant topics" className="card p-3.5 mt-6">
        <div className="font-bold text-sm mb-2">Jump to a topic</div>
        <div className="flex flex-wrap gap-2 text-sm">
          {topics.map(({ t, count }) => (
            <a key={t.id} href={`#${t.id}`} className="chip">{t.title} · {count}</a>
          ))}
        </div>
      </nav>

      {topics.map(({ t, subs, count }) => (
        <section key={t.id} id={t.id} className="mt-10 scroll-mt-24">
          <div className="flex items-baseline justify-between gap-2 flex-wrap pb-1 border-b-2" style={{ borderColor: 'var(--c-quant)' }}>
            <h2 className="text-2xl font-extrabold" style={{ color: 'var(--c-quant)' }}>{t.title}</h2>
            <span className="text-xs faint">
              {count} formulas
              {t.importance && <> · <span className={`chip ${t.importance === 'high' ? 'chip-high' : t.importance === 'medium' ? 'chip-medium' : 'chip-low'}`}>{t.importance} priority</span></>}
            </span>
          </div>
          <p className="text-sm muted mt-2">{topicBlurb(t)}</p>
          <div className="flex gap-3 mt-2 text-xs flex-wrap">
            <Link href={`/quant/${t.id}/`} className="underline decoration-dotted">Topic notes</Link>
            <Link href={`/quant/${t.id}/learn/`} className="underline decoration-dotted">Learn subtopic-wise</Link>
            <Link href={`/quant/${t.id}/formulas/`} className="underline decoration-dotted">Printable formulas</Link>
            <Link href={`/quant/${t.id}/practice/`} className="underline decoration-dotted">Practice &amp; test</Link>
          </div>

          {subs.map((s) => (
            <div key={s.id} className="mt-5">
              <h3 className="font-extrabold">
                <Link href={`/quant/${t.id}/learn/${s.id}/`} className="hover:underline">{s.title}</Link>
              </h3>
              <dl className="grid sm:grid-cols-2 gap-2.5 mt-2">
                {s.formulas!.map((f, i) => (
                  <div key={i} className="card p-3.5">
                    <dt className="text-sm font-bold">{f.name}</dt>
                    <dd className="mt-1">
                      <div className="overflow-x-auto overflow-y-hidden py-0.5"><LazyTex tex={f.tex} /></div>
                      {f.note && <p className="text-xs muted mt-1">{f.note}</p>}
                    </dd>
                  </div>
                ))}
              </dl>
            </div>
          ))}
        </section>
      ))}

      <section className="card p-5 mt-12">
        <h2 className="text-xl font-extrabold">Use the formulas, don&apos;t just read them</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          A good routine is to read one topic here, then solve ten questions from its practice set without looking at the
          formulas. Whatever you had to look up, write on a small revision card. Then check yourself under time pressure
          in a mock test, and keep the shortcut tricks handy for the questions where the standard method is too slow.
        </p>
        <div className="flex gap-2 mt-3 flex-wrap">
          <Link href="/shortcut-tricks/" className="btn btn-brand">Shortcut tricks</Link>
          <Link href="/data-interpretation/" className="btn">Data interpretation</Link>
          <Link href="/exams/ssc-cgl/mocks/" className="btn">Mock tests</Link>
          <Link href="/daily-quiz/" className="btn">Daily quiz</Link>
          <Link href="/formula-sheet/" className="btn">Full formula sheet</Link>
          <Link href="/quant/" className="btn">Quant overview</Link>
        </div>
      </section>
    </div>
  );
}
