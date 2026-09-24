import Link from 'next/link';
import { contentStats, getExam, listMocks, listTopics, SECTION_META, availableSections } from '@/lib/content';
import { Md } from '@/components/Md';
import { ExamPicker, SelectedExamPanel } from '@/components/ExamPicker';

export const dynamic = 'force-static';

export default function Home() {
  const stats = contentStats();
  const exam = getExam();
  const mocks = listMocks();

  return (
    <div>
      <section className="text-center max-w-3xl mx-auto pt-8 pb-4 sm:pt-14">
        <div className="flex justify-center gap-2 flex-wrap">
          <span className="chip chip-high">Free · SSC · Railways · Banking · Defence · Entrance</span>
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
          <Link href="/learn/" className="btn btn-brand">Start learning — free</Link>
          <Link href="/daily-quiz/" className="btn">Today&apos;s quiz</Link>
          <Link href="/exams/ssc-cgl/mocks/" className="btn">Free mock test</Link>
        </div>
        <p className="faint text-xs mt-3">
          {stats.questions > 0 ? `${stats.questions}+ questions · ${stats.formulas}+ formulas · ${stats.tricks}+ shortcut tricks` : 'Content is being compiled right now — refresh in a bit.'}
        </p>
      </section>

      <section className="mt-8 space-y-4">
        <SelectedExamPanel />
        <div className="card p-4 sm:p-5">
          <ExamPicker />
        </div>
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

      {exam?.latestCycle && (
        <section className="card p-5 sm:p-6 mt-10">
          <h2 className="text-xl font-extrabold">Exam update — SSC CGL {exam.latestCycle.year}</h2>
          <Md className="muted mt-2">{exam.latestCycle.status}</Md>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mt-4 text-sm">
            {[['Notification', exam.latestCycle.notificationDate], ['Apply window', exam.latestCycle.applicationWindow], ['Tier 1', exam.latestCycle.tier1], ['Tier 2', exam.latestCycle.tier2]].map(([k, v]) => (
              <div key={k} className="rounded-xl p-3" style={{ background: 'var(--surface-2)' }}>
                <div className="text-xs faint font-semibold uppercase">{k}</div>
                <div className="mt-1 font-medium">{v ?? 'To be announced'}</div>
              </div>
            ))}
          </div>
          <Link href="/exams/ssc-cgl/" className="btn mt-4">SSC CGL exam hub →</Link>
        </section>
      )}

      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Mock tests <span className="text-sm font-semibold faint">· SSC CGL</span></h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-3">
          {mocks.map((m) => (
            <Link key={m.id} href={`/exams/ssc-cgl/mocks/${m.id}/`} className="card p-5 flex flex-col">
              <span className="flex gap-2"><span className={`chip ${m.available ? 'chip-low' : 'chip-medium'}`}>{m.available ? 'Ready' : 'Coming up'}</span><span className="chip">Tier {m.tier}</span><span className="chip">{m.open ? 'Open to all' : '🔒 Free login'}</span></span>
              <h3 className="font-bold mt-2">{m.title}</h3>
              <p className="text-sm muted mt-1 flex-1">{m.blurb}</p>
            </Link>
          ))}
        </div>
      </section>

      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Free tools</h2>
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
