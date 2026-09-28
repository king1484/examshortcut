import type { Metadata } from 'next';
import Link from 'next/link';
import { getCaYear, listCaYears } from '@/lib/content';

export const dynamic = 'force-static';
export const dynamicParams = false;

export const metadata: Metadata = {
  title: 'Current affairs — month-wise, with a quiz | ExamShortcut',
  description: 'Current affairs for SSC, Railway and other govt exams, month by month: appointments, awards, sports, schemes, summits, reports, defence, science and economy — every month ends with a quiz.',
};

export default function CurrentAffairsPage() {
  const years = listCaYears().map((y) => ({ year: y, data: getCaYear(y)! }));

  return (
    <div className="max-w-3xl mx-auto">
      <p className="text-xs font-bold uppercase tracking-wide mt-4" style={{ color: 'var(--brand)' }}>General awareness · No login needed</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">Current affairs</h1>
      <p className="muted mt-2 text-[15px]">Month-wise, exam-relevant only — no news dump. Appointments, awards, sports, schemes, summits, reports, defence, science and the economy, in simple English. Every month ends with a quiz so the facts actually stick.</p>

      {years.length === 0 && <div className="card p-6 mt-6 text-center muted">The current-affairs desk is still verifying items. Check back shortly.</div>}

      {years.map(({ year, data }) => {
        const nItems = data.months.reduce((n, m) => n + m.items.length, 0);
        return (
          <section key={year} className="card p-5 mt-5">
            <div className="flex items-baseline gap-3 flex-wrap">
              <h2 className="text-2xl font-extrabold"><Link href={`/current-affairs/${year}/`} className="hover:underline">{year}</Link></h2>
              <span className="text-xs faint">{data.months.length} months · {nItems} headlines · {data.months.reduce((n, m) => n + (m.quiz?.length ?? 0), 0)} quiz Q</span>
            </div>
            <div className="flex flex-wrap gap-2 mt-3">
              {data.months.map((m) => (
                <Link key={m.month} href={`/current-affairs/${m.month.slice(0, 4)}/${m.month.slice(5)}/`} className="btn text-sm" style={{ padding: '.3rem .7rem' }}>
                  {m.label} <span className="faint text-xs ml-1">{m.items.length}</span>
                </Link>
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}
