import Link from 'next/link';
import { contentStats, getExam, listMocks, SECTION_META, availableSections } from '@/lib/content';
import { CountdownChip } from '@/components/CountdownChip';

export const dynamic = 'force-static';

export default function Home() {
  const stats = contentStats();
  const exam = getExam();
  const mocks = listMocks();

  return (
    <div>
      <section className="text-center max-w-3xl mx-auto pt-8 pb-4 sm:pt-16">
        <div className="flex justify-center gap-2 flex-wrap">
          <CountdownChip date="2026-09-30" />
          <span className="chip chip-high">100% free · no login · no ads in the test engine</span>
        </div>
        <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight mt-4 leading-tight">
          Crack SSC CGL with<br /><span style={{ color: 'var(--brand)' }}>shortcuts, not slog</span>
        </h1>
        <p className="muted text-lg mt-4">
          Every topic with formulas, shortcut tricks and mistakes to avoid. Topic tests and full mocks in a
          real exam interface. Cutoff trends and a safe-score estimator. All free, all offline-capable.
        </p>
        <div className="flex gap-3 justify-center flex-wrap mt-6">
          <Link href="/ssc-cgl/mocks/" className="btn btn-brand">Take a free mock test</Link>
          <Link href="/ssc-cgl/syllabus/" className="btn">Browse the syllabus</Link>
        </div>
        <p className="faint text-xs mt-3">
          {stats.questions > 0 ? `${stats.questions}+ questions · ${stats.formulas}+ formulas · ${stats.tricks}+ shortcut tricks` : 'Content is being compiled right now — refresh in a bit.'}
        </p>
      </section>

      <section className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-10">
        {[
          { href: '/ssc-cgl/syllabus/', icon: '📚', title: 'Topic-wise notes', body: 'Concept → all formulas → shortcut tricks → common mistakes, for every topic in the syllabus.' },
          { href: '/ssc-cgl/mocks/', icon: '🖥️', title: 'Real CBT mocks', body: 'The exact SSC test interface: palette, mark-for-review, auto-submit — plus per-question time analysis.' },
          { href: '/ssc-cgl/formula-sheet/', icon: '⚡', title: 'Shortcut-first', body: 'Every trick taught with a worked example. Printable formula sheet for last-minute revision.' },
          { href: '/ssc-cgl/cutoffs/', icon: '📈', title: 'Cutoffs & safe score', body: 'Year-wise official cutoffs, trend charts, and a normalisation-aware score estimator.' },
        ].map((c) => (
          <Link key={c.href} href={c.href} className="card p-5 hover:-translate-y-0.5 transition-transform">
            <div className="text-2xl">{c.icon}</div>
            <h2 className="font-bold mt-2">{c.title}</h2>
            <p className="text-sm muted mt-1">{c.body}</p>
          </Link>
        ))}
      </section>

      {exam?.latestCycle && (
        <section className="card p-5 sm:p-6 mt-10">
          <h2 className="text-xl font-extrabold">SSC CGL {exam.latestCycle.year}: latest status</h2>
          <p className="muted mt-2">{exam.latestCycle.status}</p>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mt-4 text-sm">
            {[['Notification', exam.latestCycle.notificationDate], ['Apply window', exam.latestCycle.applicationWindow], ['Tier 1', exam.latestCycle.tier1], ['Tier 2', exam.latestCycle.tier2]].map(([k, v]) => (
              <div key={k} className="rounded-xl p-3" style={{ background: 'var(--surface-2)' }}>
                <div className="text-xs faint font-semibold uppercase">{k}</div>
                <div className="mt-1 font-medium">{v ?? 'To be announced'}</div>
              </div>
            ))}
          </div>
          <Link href="/ssc-cgl/" className="btn mt-4">Full exam guide →</Link>
        </section>
      )}

      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Mock tests</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-3">
          {mocks.map((m) => (
            <Link key={m.id} href={`/ssc-cgl/mocks/${m.id}/`} className="card p-5 flex flex-col">
              <span className={`chip ${m.available ? 'chip-low' : 'chip-medium'}`}>{m.available ? 'Ready' : 'Coming up'}</span>
              <h3 className="font-bold mt-2">{m.title}</h3>
              <p className="text-sm muted mt-1 flex-1">{m.blurb}</p>
            </Link>
          ))}
        </div>
      </section>

      <section className="mt-10">
        <h2 className="text-xl font-extrabold">Sections</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-3">
          {availableSections().map((s) => (
            <Link key={s} href={`/ssc-cgl/${s}/`} className="card p-5" style={{ borderTop: `3px solid ${SECTION_META[s].color}` }}>
              <h3 className="font-bold">{SECTION_META[s].name}</h3>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
