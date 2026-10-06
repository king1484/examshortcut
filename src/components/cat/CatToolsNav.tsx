import Link from 'next/link';

export const CAT_TOOLS: { href: string; title: string; sub: string; label: string }[] = [
  { href: '/exams/cat/score-calculator/', title: '🧮 Score calculator', sub: 'Sectional + total raw score, accuracy, attempts', label: 'Score calculator' },
  { href: '/exams/cat/study-plan/', title: '🗓️ Study plan', sub: 'Countdown + phase-wise plan by weeks left', label: 'Study plan' },
  { href: '/exams/cat/syllabus/', title: '📚 Syllabus & strategy', sub: 'Section-wise topics and approach', label: 'Syllabus' },
];

/** Tools block for the CAT hub (rendered only when exam id is "cat"). */
export function CatToolsBlock() {
  return (
    <section className="mt-6" aria-labelledby="cat-tools">
      <h2 id="cat-tools" className="text-lg font-extrabold">CAT tools</h2>
      <div className="grid sm:grid-cols-3 gap-3 mt-3">
        {CAT_TOOLS.map((t) => (
          <Link key={t.href} href={t.href} className="card p-4 hover:-translate-y-0.5 transition-transform">
            <div className="font-bold text-sm">{t.title}</div>
            <div className="text-xs faint mt-0.5">{t.sub}</div>
          </Link>
        ))}
      </div>
    </section>
  );
}

/** Breadcrumb + sibling tool nav shown at the top of each CAT tool page. */
export function CatToolHeader({ current, h1, intro }: { current: string; h1: string; intro: React.ReactNode }) {
  return (
    <>
      <nav aria-label="Breadcrumb" className="text-xs faint">
        <Link href="/exams/" className="underline decoration-dotted">Exams</Link> / <Link href="/exams/cat/" className="underline decoration-dotted">CAT</Link> / {CAT_TOOLS.find((t) => t.href === current)?.label}
      </nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-2">{h1}</h1>
      <div className="muted mt-3 text-[15px]">{intro}</div>
      <nav aria-label="CAT tools" className="flex flex-wrap gap-2 mt-4 text-sm">
        <Link href="/exams/cat/" className="chip hover:underline">← CAT guide</Link>
        {CAT_TOOLS.map((t) => t.href === current
          ? <span key={t.href} className="chip chip-brand" aria-current="page">{t.label}</span>
          : <Link key={t.href} href={t.href} className="chip hover:underline">{t.label}</Link>)}
        <Link href="/exams/cat/cutoffs/" className="chip hover:underline">Cutoffs</Link>
      </nav>
    </>
  );
}
