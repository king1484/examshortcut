import Link from 'next/link';
import { contentStats, listMocks, listTopics, SECTION_META, availableSections } from '@/lib/content';
import { ExamPicker } from '@/components/ExamPicker';
import { ExamNotice } from '@/components/ExamNotice';

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

export default function Home() {
  const stats = contentStats();
  const mocks = listMocks();

  return (
    <div>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(SITE_LD) }} />
      <section className="text-center max-w-3xl mx-auto pt-8 pb-4 sm:pt-14">
        <ExamNotice exam="SSC CGL" stage="Tier 1" start="2026-09-30" end="2026-10-30" href="/exams/ssc-cgl/#status" builtAt={BUILT_AT} />
        <div className="flex justify-center gap-2 flex-wrap mt-4">
          <span className="chip chip-high">SSC · Railways · Banking · CAT</span>
        </div>
        <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight mt-4 leading-tight">
          Prepare for any exam with<br /><span style={{ color: 'var(--brand)' }}>shortcuts, not slog</span>
        </h1>
        <p className="muted text-lg mt-4">
          Maths, reasoning, English and GK are common to almost every government and entrance exam. Learn each topic
          in depth — simple notes, every question type with its formula, practice sets — then test yourself with a daily
          quiz and full mocks.
        </p>
        <div className="flex gap-3 justify-center flex-wrap mt-6">
          <Link href="/learn/" className="btn btn-brand">Start learning</Link>
          <Link href="/daily-quiz/" className="btn">Today&apos;s quiz</Link>
          <Link href="/exams/ssc-cgl/mocks/" className="btn">Take a mock test</Link>
          <Link href="/exam-analysis/" className="btn">📊 Today&apos;s exam analysis</Link>
        </div>
        <p className="faint text-xs mt-3">
          {stats.questions > 0 ? `${stats.questions}+ questions · ${stats.formulas}+ formulas · ${stats.tricks}+ shortcut tricks` : 'Content is being compiled right now — refresh in a bit.'}
        </p>
      </section>

      <div className="mt-8">
        <ExamPicker collapse />
      </div>

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

      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Mock tests <span className="text-sm font-semibold faint">· SSC CGL</span></h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-3">
          {mocks.map((m) => (
            <Link key={m.id} href={`/exams/ssc-cgl/mocks/${m.id}/`} className="card p-5 flex flex-col">
              <span className="flex gap-2"><span className={`chip ${m.available ? 'chip-low' : 'chip-medium'}`}>{m.available ? 'Ready' : 'Coming up'}</span><span className="chip">Tier {m.tier}</span><span className="chip">Free</span></span>
              <h3 className="font-bold mt-2">{m.title}</h3>
              <p className="text-sm muted mt-1 flex-1">{m.blurb}</p>
            </Link>
          ))}
        </div>
      </section>

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
