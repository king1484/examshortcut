import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getCaYear, listCaYears } from '@/lib/content';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return listCaYears().map((year) => ({ year: String(year) }));
}

export async function generateMetadata({ params }: { params: Promise<{ year: string }> }): Promise<Metadata> {
  const { year } = await params;
  const data = getCaYear(Number(year));
  if (!data) return {};
  const nItems = data.months.reduce((n, m) => n + m.items.length, 0);
  return {
    title: `Current affairs ${year} — month-wise for govt exams (${nItems} headlines)`,
    description: `Every exam-relevant headline from ${year} in simple English, month by month — appointments, awards, sports, schemes, summits, reports, defence, science and economy — with a quiz per month.`,
  };
}

export default async function CaYearPage({ params }: { params: Promise<{ year: string }> }) {
  const { year } = await params;
  const data = getCaYear(Number(year));
  if (!data) notFound();

  return (
    <div className="max-w-3xl mx-auto">
      <div className="text-xs faint mt-4"><Link href="/current-affairs/" className="underline decoration-dotted">Current affairs</Link> / {year}</div>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">Current affairs {year}</h1>
      <p className="muted mt-2 text-[15px]">Pick a month — each page has every exam-relevant headline in simple English, the facts exams repeat, and a short quiz.</p>

      <div className="space-y-3 mt-6">
        {data.months.map((m) => (
          <Link key={m.month} href={`/current-affairs/${m.month.slice(0, 4)}/${m.month.slice(5)}/`} className="card p-4 block hover:-translate-y-0.5 transition-transform">
            <div className="flex items-baseline gap-2 flex-wrap">
              <h2 className="text-lg font-extrabold">{m.label}</h2>
              <span className="text-xs faint">{m.items.length} headlines{m.quiz?.length ? ` · ${m.quiz.length}-question quiz` : ''}</span>
            </div>
            <ul className="mt-1.5 text-sm muted space-y-0.5">
              {m.items.slice(0, 3).map((it, i) => <li key={i} className="truncate">• {it.headline}</li>)}
              {m.items.length > 3 && <li className="faint text-xs">+ {m.items.length - 3} more</li>}
            </ul>
          </Link>
        ))}
      </div>
    </div>
  );
}
