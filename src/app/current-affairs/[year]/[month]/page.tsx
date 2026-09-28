import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getCaYear, listCaYears } from '@/lib/content';
import { TopicQuiz } from '@/components/TopicQuiz';

export const dynamic = 'force-static';
export const dynamicParams = false;

function allMonths() {
  return listCaYears().flatMap((y) => (getCaYear(y)?.months ?? []).map((m) => ({ year: String(y), month: m.month.slice(5) })));
}

export function generateStaticParams() {
  return allMonths();
}

export async function generateMetadata({ params }: { params: Promise<{ year: string; month: string }> }): Promise<Metadata> {
  const { year, month } = await params;
  const y = getCaYear(Number(year));
  const m = y?.months.find((x) => x.month === `${year}-${month}`);
  if (!m) return {};
  return {
    title: `Current affairs ${m.label} — exam headlines + quiz`,
    description: `${m.items.length} exam-relevant current-affairs headlines from ${m.label} in simple English — appointments, awards, sports, schemes, summits, defence, science and economy — with a ${m.quiz?.length ?? 0}-question quiz.`,
  };
}

const CAT_COLOR: Record<string, string> = {
  appointments: 'var(--info)', awards: 'var(--warn)', sports: 'var(--ok)', schemes: 'var(--brand)',
  defence: 'var(--bad)', science: 'var(--info)', economy: 'var(--warn)', reports: 'var(--info)', summits: 'var(--brand)',
};

export default async function CaMonthPage({ params }: { params: Promise<{ year: string; month: string }> }) {
  const { year, month } = await params;
  const y = getCaYear(Number(year));
  const m = y?.months.find((x) => x.month === `${year}-${month}`);
  if (!m) notFound();

  // prev/next by chronological order
  const all = allMonths().sort((a, b) => `${a.year}-${a.month}`.localeCompare(`${b.year}-${b.month}`));
  const idx = all.findIndex((x) => x.year === year && x.month === month);
  const prev = idx > 0 ? all[idx - 1] : null;
  const next = idx < all.length - 1 ? all[idx + 1] : null;
  const nav = (x: { year: string; month: string } | null, dir: 'prev' | 'next') => {
    if (!x) return <span />;
    const label = getCaYear(Number(x.year))?.months.find((mm) => mm.month === `${x.year}-${x.month}`)?.label ?? x.month;
    return <Link className="card p-3 flex-1 hover:-translate-y-0.5 transition-transform" style={dir === 'next' ? { textAlign: 'right' } : undefined} href={`/current-affairs/${x.year}/${x.month}/`}>{dir === 'prev' ? `← ${label}` : `${label} →`}</Link>;
  };

  return (
    <div className="max-w-3xl mx-auto">
      <div className="text-xs faint mt-4">
        <Link href="/current-affairs/" className="underline decoration-dotted">Current affairs</Link> /{' '}
        <Link href={`/current-affairs/${year}/`} className="underline decoration-dotted">{year}</Link> / {m.label}
      </div>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">Current affairs — {m.label}</h1>
      <p className="muted mt-2 text-[15px]">{m.items.length} exam-relevant headlines, written simply. Read the bold fact in each — that's what exams ask.</p>

      <div className="space-y-3 mt-6">
        {m.items.map((it, i) => (
          <article key={i} className="card p-4" style={{ borderLeft: `3px solid ${CAT_COLOR[it.category.toLowerCase()] ?? 'var(--line)'}` }}>
            <div className="flex items-center gap-2 flex-wrap text-[11px] faint">
              <span className="chip">{it.date}</span>
              <span className="chip capitalize">{it.category}</span>
            </div>
            <h2 className="font-bold mt-1.5">{it.headline}</h2>
            <p className="text-sm muted mt-1">{it.detail}</p>
            {it.examFacts && it.examFacts.length > 0 && (
              <ul className="mt-2 text-sm space-y-0.5" style={{ color: 'var(--ink)' }}>
                {it.examFacts.map((f, k) => <li key={k}>📌 {f}</li>)}
              </ul>
            )}
          </article>
        ))}
      </div>

      {m.quiz && m.quiz.length > 0 && (
        <section className="mt-10">
          <h2 className="text-xl font-extrabold">{m.label} quiz — {m.quiz.length} questions</h2>
          <p className="text-sm muted mt-1">From exactly the headlines above. If you read the month, you should score 8+.</p>
          <div className="mt-3"><TopicQuiz questions={m.quiz} storageKey={`ca/${m.month}`} href={`/current-affairs/${year}/${month}/`} section="ga" title={`Current affairs · ${m.label}`} /></div>
        </section>
      )}

      <nav className="flex gap-3 mt-10 text-sm">
        {nav(prev, 'prev')}
        {nav(next, 'next')}
      </nav>
    </div>
  );
}
