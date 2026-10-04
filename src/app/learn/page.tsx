import Link from 'next/link';
import type { Metadata } from 'next';
import { availableSections, SECTION_META, listTopics, topicBlurb, sectionIntro } from '@/lib/content';
import { LearnExamFilter } from '@/components/LearnExamFilter';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'All subjects — topic-wise notes, question types, formulas & practice',
  description:
    'Quantitative Aptitude, Reasoning, English, General Awareness and Computer — the common subjects of SSC, Railway, teaching and entrance exams. Every topic has detailed notes, every question type with its formula and logic, and practice sets.',
  alternates: { canonical: '/learn/' },
};

export default function LearnPage() {
  const sections = availableSections();
  return (
    <div className="max-w-5xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">Subjects &amp; notes</h1>
      <p className="muted mt-2 max-w-3xl">
        These subjects are common to almost every government and entrance exam. Learn them once, well: every topic
        breaks into subtopics, and every subtopic has <b>detailed notes in simple English</b>, <b>every question type</b>{' '}
        with its own formula and logic, worked examples and <b>practice sets</b>.
      </p>
      <LearnExamFilter />
      <p className="text-sm muted mt-4 max-w-3xl">
        Short on time? Go straight to the{' '}
        <Link href="/shortcut-tricks/" className="underline decoration-dotted">shortcut tricks index</Link>,{' '}
        <Link href="/quant-formulas/" className="underline decoration-dotted">Quant formulas by topic</Link>,{' '}
        <Link href="/data-interpretation/" className="underline decoration-dotted">data interpretation formulas &amp; tricks</Link> or the{' '}
        <Link href="/formula-sheet/" className="underline decoration-dotted">full formula sheet</Link>.
      </p>

      {sections.map((sid) => {
        const topics = listTopics(sid);
        const meta = SECTION_META[sid];
        const subs = topics.reduce((n, t) => n + t.subtopics.length, 0);
        const qs = topics.reduce((n, t) => n + (t.practice?.length ?? 0), 0);
        return (
          <section key={sid} id={sid} data-section={sid} className="mt-8 scroll-mt-24">
            <div className="flex items-baseline justify-between flex-wrap gap-2">
              <h2 className="text-2xl font-extrabold" style={{ color: meta.color }}>{meta.name}</h2>
              <Link href={`/${sid}/`} className="text-sm underline decoration-dotted">Subject overview &amp; strategy →</Link>
            </div>
            <p className="text-xs faint mt-0.5">{topics.length} topics · {subs} subtopics · {qs} practice questions</p>
            {sectionIntro(sid) && <p className="text-sm muted mt-1 max-w-3xl">{sectionIntro(sid)}</p>}
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-2.5 mt-3">
              {topics.map((t) => (
                <Link key={t.id} href={`/${sid}/${t.id}/`} className="card p-3.5 flex flex-col hover:-translate-y-0.5 transition-transform">
                  <div className="flex items-center gap-2">
                    <span className="font-bold text-sm">{t.title}</span>
                    {t.importance && <span className={`chip ml-auto ${t.importance === 'high' ? 'chip-high' : t.importance === 'medium' ? 'chip-medium' : 'chip-low'}`}>{t.importance}</span>}
                  </div>
                  <p className="text-xs muted mt-1 line-clamp-2">{topicBlurb(t)}</p>
                  <span className="text-xs faint mt-2">
                    {t.subtopics.length} subtopics
                    {t.subtopics.some((s) => s.patterns?.length) ? ` · ${t.subtopics.reduce((n, s) => n + (s.patterns?.length ?? 0), 0)} question types` : ''}
                    {t.practice?.length ? ` · ${t.practice.length} practice Qs` : ''}
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
