import Link from 'next/link';
import type { Metadata } from 'next';
import { contentStats, listMocks, listTopics, SECTION_META, availableSections } from '@/lib/content';
import { ExamPicker } from '@/components/ExamPicker';
import { ExamNotice } from '@/components/ExamNotice';
import { HomeMocks } from '@/components/HomeMocks';
import { EXAMS } from '@/lib/exams';
import { STUDY_GUIDES } from '@/lib/studyGuides';
import { listExamUpdates } from '@/lib/examUpdates';
import { ExamUpdateCards } from '@/components/ExamUpdateCards';

const BUILT_AT = Date.now();

const SITE_LD = {
  '@context': 'https://schema.org',
  '@graph': [
    { '@type': 'WebSite', '@id': 'https://examshortcut.in/#website', name: 'ExamShortcut', url: 'https://examshortcut.in/', inLanguage: 'en-IN',
      publisher: { '@id': 'https://examshortcut.in/#org' } },
    { '@type': 'Organization', '@id': 'https://examshortcut.in/#org', name: 'ExamShortcut', url: 'https://examshortcut.in/',
      logo: 'https://examshortcut.in/icon-512.png' },
  ],
};

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: { absolute: 'ExamShortcut: Free Notes & Study Guides for SSC, Banking, Railway & CAT' },
  description: 'Learn maths, reasoning, English and GK with free notes, worked examples and study guides. Plan your revision for SSC, Railway, Banking and CAT exams.',
  alternates: { canonical: '/' },
};

export default function Home() {
  const stats = contentStats();
  const mocks = EXAMS.flatMap((e) => listMocks(e.id).filter((m) => m.available)
    .map((m) => ({ id: m.id, title: m.title, blurb: m.blurb, tier: m.tier, exam: e.id, available: m.available })));

  return (
    <div>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(SITE_LD) }} />
      <section className="text-center max-w-3xl mx-auto pt-4 pb-4 sm:pt-14">
        <ExamNotice exam="SSC CGL" stage="Tier 1" start="2026-09-30" end="2026-10-30" href="/exams/ssc-cgl/#status" builtAt={BUILT_AT} />
        <div className="flex justify-center gap-2 flex-wrap mt-3 sm:mt-4">
          <span className="chip chip-high">SSC · Railways · Banking · CAT</span>
        </div>
        <h1 className="text-[2rem] sm:text-6xl font-extrabold tracking-tight mt-3 sm:mt-4 leading-tight">
          Prepare for competitive exams<br /><span style={{ color: 'var(--brand)' }}>one clear topic at a time</span>
        </h1>
        <p className="muted text-[15px] sm:text-lg mt-3 sm:mt-4">
          Learn maths, reasoning, English and GK with simple notes, worked examples and topic practice.
          Follow a study guide for your weak areas, then build a revision routine you can keep.
        </p>
        <div className="flex flex-col items-center gap-3 mt-5 sm:mt-6">
          <Link href="/learn/" className="btn btn-brand px-8">Start learning</Link>
          <div className="flex justify-center gap-2 sm:gap-3 flex-wrap">
            <Link href="/daily-quiz/" className="btn">Today&apos;s quiz</Link>
            <Link href="/exams/ssc-cgl/mocks/" className="btn">Take a mock</Link>
            <Link href="/exam-analysis/" className="btn">📊 Exam analysis</Link>
          </div>
        </div>
        <p className="faint text-xs mt-3">
          {stats.questions > 0 ? `${stats.questions}+ questions · ${stats.formulas}+ formulas · ${stats.tricks}+ shortcut tricks` : 'Content is being compiled right now — refresh in a bit.'}
        </p>
      </section>

      <section className="mt-8 exam-updates" aria-labelledby="latest-exam-updates">
        <div className="flex flex-wrap justify-between gap-3 items-baseline"><h2 id="latest-exam-updates" className="text-2xl font-extrabold">Results, answer keys &amp; exam notices</h2><Link className="font-semibold underline text-sm" href="/exam-updates/">All exam updates →</Link></div>
        <p className="muted text-sm mt-2 mb-4">Official sources, the right recruitment cycle and what to do next.</p>
        <ExamUpdateCards items={listExamUpdates().filter(item => !item.status.startsWith('Archive:')).slice(0, 3)} />
        <div className="flex flex-wrap gap-3 mt-4"><Link className="btn" href="/results/">Published results →</Link><Link className="btn" href="/answer-keys/">Answer keys &amp; objection windows →</Link></div>
      </section>
      <div className="mt-8">
        <ExamPicker collapse />
      </div>

      <section className="mt-9">
        <div className="flex flex-wrap items-baseline justify-between gap-3">
          <h2 className="text-2xl font-extrabold">Find a better way to study</h2>
          <Link className="text-sm font-semibold underline" href="/study-guides/">All free study guides →</Link>
        </div>
        <p className="text-sm muted mt-2">Start from basics, fit preparation around your day, or fix the mistakes that keep returning.</p>
        <div className="grid sm:grid-cols-3 gap-3 mt-4">
          {STUDY_GUIDES.slice(0, 3).map((g) => <Link href={`/study-guides/${g.slug}/`} key={g.slug} className="card p-5">
            <span className="chip">{g.audience}</span>
            <h3 className="font-bold mt-3">{g.title}</h3>
            <p className="text-sm muted mt-2">{g.description}</p>
          </Link>)}
        </div>
        <Link className="btn mt-4" href="/revision-planner/">Make a free revision calendar</Link>
      </section>


      <section className="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 mt-10">
        {[
          { href: '/learn/', icon: '📚', title: 'Deep topic notes', body: 'Every subtopic explained in simple English, with all the question types asked from it.' },
          { href: '/daily-quiz/', icon: '🗓️', title: 'Daily quiz', body: 'A fresh mixed quiz every day from your exam’s subjects. Build a streak.' },
          { href: '/formula-sheet/', icon: '⚡', title: 'Shortcut-first', body: 'Every trick taught with a worked example. Printable formula sheet for revision.' },
          { href: '/current-affairs/', icon: '📰', title: '5 years of current affairs', body: 'Month-wise, exam-relevant events with quick facts and a quiz for each month.' },
        ].map((c) => (
          <Link key={c.href} href={c.href} className="card p-4 sm:p-5 hover:-translate-y-0.5 transition-transform">
            <div className="text-2xl">{c.icon}</div>
            <h2 className="font-bold mt-2 text-[15px] sm:text-base">{c.title}</h2>
            <p className="text-xs sm:text-sm muted mt-1">{c.body}</p>
          </Link>
        ))}
      </section>

      <HomeMocks mocks={mocks} />

      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Tools</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 mt-3">
          {[
            ['/exams/ssc-cgl/rank-estimator/', '🏅', 'Rank estimator'],
            ['/vocab/', '🔤', 'Vocab bank'],
            ['/static-gk/', '🗺️', 'Static GK tables'],
            ['/exams/ssc-cgl/study-plan/', '🗓️', 'Study plan'],
            ['/exams/ssc-cgl/typing-test/', '⌨️', 'Typing test (DEST)'],
            ['/current-affairs/', '📰', 'Current affairs'],
          ].map(([href, icon, label]) => (
            <Link key={href} href={href} className="card p-4 text-center hover:-translate-y-0.5 transition-transform">
              <div className="text-2xl">{icon}</div>
              <div className="text-sm font-semibold mt-1">{label}</div>
            </Link>
          ))}
        </div>
      </section>

      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Subjects</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-3">
          {availableSections().map((s) => {
            const topics = listTopics(s);
            const top = [...topics].sort((a, b) => (b.avgQuestions?.tier1 ?? 0) - (a.avgQuestions?.tier1 ?? 0)).slice(0, 4);
            return (
              <Link key={s} href={`/${s}/`} className="card p-5 flex flex-col hover:-translate-y-0.5 transition-transform" style={{ borderTop: `3px solid ${SECTION_META[s].color}` }}>
                <h3 className="font-bold">{SECTION_META[s].name}</h3>
                <p className="text-xs faint mt-1">{topics.length} topics · notes, question types &amp; practice</p>
                <p className="text-sm muted mt-2 flex-1">{top.map((t) => t.title).join(' · ')}{topics.length > 4 ? ' …' : ''}</p>
                <span className="text-sm font-semibold mt-3" style={{ color: SECTION_META[s].color }}>Open subject →</span>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}
