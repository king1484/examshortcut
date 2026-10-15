import Link from 'next/link';
import { getCaYear, listCaYears, type CaYear } from '@/lib/content';

/* Server-rendered digest for /current-affairs/<year>/ : which kinds of events the year's headlines
   cover, the exam facts attached to them (month by month), and how to revise. Everything is derived
   from the year's own headline data. */

const CAT_LABEL: Record<string, string> = {
  appointments: 'Appointments', awards: 'Awards', sports: 'Sports', schemes: 'Schemes', summits: 'Summits',
  reports: 'Reports and indices', defence: 'Defence', science: 'Science and technology', economy: 'Economy',
  international: 'International', national: 'National', environment: 'Environment', obituaries: 'Obituaries',
  books: 'Books and authors', banking: 'Banking', days: 'Important days', states: 'States and regions',
};
const label = (c: string) => CAT_LABEL[c] ?? c.replace(/[-_]/g, ' ').replace(/^./, (x) => x.toUpperCase());
const catKey = (c: string) => (c || 'other').toLowerCase();

export function CaYearDigest({ data, year }: { data: CaYear; year: number | string }) {
  const months = [...data.months].sort((a, b) => a.month.localeCompare(b.month));
  const items = months.flatMap((m) => m.items.map((it) => ({ it, m })));
  const nQuiz = months.reduce((n, m) => n + (m.quiz?.length ?? 0), 0);
  const byCat = new Map<string, number>();
  for (const { it } of items) byCat.set(catKey(it.category), (byCat.get(catKey(it.category)) ?? 0) + 1);
  const cats = [...byCat.entries()].sort((a, b) => b[1] - a[1]);
  const facts = items.flatMap(({ it, m }) => (it.examFacts ?? []).map((f) => ({ f, m, h: it.headline })));
  const busiest = [...months].sort((a, b) => b.items.length - a.items.length)[0];
  const first = months[0];
  const last = months[months.length - 1];
  const mHref = (m: { month: string }) => `/current-affairs/${m.month.slice(0, 4)}/${m.month.slice(5)}/`;

  if (!items.length) return null;
  return (
    <div className="mt-10 max-w-3xl">
      <section aria-labelledby="cy-about">
        <h2 id="cy-about" className="text-2xl font-extrabold">What the {year} headlines cover</h2>
        <p className="mt-2 text-[15px] muted">
          This page covers {months.length} {months.length === 1 ? 'month' : 'months'}
          {first && last && first.month !== last.month ? <>, {first.label} to {last.label}</> : first ? <>, {first.label}</> : null}, with {items.length} exam-relevant headlines
          {nQuiz > 0 && <> and {nQuiz} quiz questions</>}.
          {busiest && months.length > 1 && <> The fullest month is {busiest.label} with {busiest.items.length} headlines.</>}
          {' '}Only events that exams tend to ask about are kept, each written in plain English with the fact that is likely to be the answer.
        </p>
        {cats.length > 0 && (
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Kind of event</th><th className="text-right">Headlines</th></tr></thead>
              <tbody>{cats.map(([c, n]) => <tr key={c}><td>{label(c)}</td><td className="text-right">{n}</td></tr>)}</tbody>
            </table>
          </div>
        )}
      </section>

      {facts.length > 0 && (
        <section className="mt-9" aria-labelledby="cy-facts">
          <h2 id="cy-facts" className="text-2xl font-extrabold">Facts worth remembering from {year}</h2>
          <p className="text-sm muted mt-1">Each line is the specific fact attached to a headline, with the month page where the full note sits.</p>
          <ul className="mt-3 space-y-2 text-sm list-disc pl-5">
            {facts.slice(0, 24).map((x, i) => (
              <li key={i}>{x.f} <span className="faint">(<Link className="underline decoration-dotted" href={mHref(x.m)}>{x.m.label}</Link>)</span></li>
            ))}
          </ul>
          {facts.length > 24 && <p className="text-xs faint mt-2">{facts.length - 24} more facts are on the month pages.</p>}
        </section>
      )}

      <section className="mt-9" aria-labelledby="cy-use">
        <h2 id="cy-use" className="text-2xl font-extrabold">How to revise a year of current affairs</h2>
        <div className="mt-2 space-y-3 text-[15px]">
          <p>Read one month at a time and stop after the quiz instead of scrolling the whole year in a sitting. Facts that are linked, such as a person and the post they took, or an award and the field it is for, stay together better when they are read in the same sitting.</p>
          <p>Write the answer to the exam question, not the story: who, which post, which place, which number. A headline you can summarise in one line is one you can answer in a multiple-choice paper.</p>
          <p className="muted">Exam questions usually come from the last twelve months before the paper, so older years are best used for static context and for spotting which events repeat as themes.</p>
        </div>
      </section>
    </div>
  );
}

/** Overview block for /current-affairs/ : totals across all years and how the desk is organised. */
export function CaIndexGuide() {
  const years = listCaYears().map((y) => getCaYear(y)!).filter(Boolean);
  const months = years.flatMap((y) => y.months);
  const items = months.flatMap((m) => m.items);
  if (!items.length) return null;
  const byCat = new Map<string, number>();
  for (const it of items) byCat.set(catKey(it.category), (byCat.get(catKey(it.category)) ?? 0) + 1);
  const cats = [...byCat.entries()].sort((a, b) => b[1] - a[1]);
  const nQuiz = months.reduce((n, m) => n + (m.quiz?.length ?? 0), 0);
  const ys = years.map((y) => y.year).sort((a, b) => a - b);
  return (
    <div className="mt-2 max-w-3xl">
      <section className="mt-9" aria-labelledby="ci-numbers">
        <h2 id="ci-numbers" className="text-2xl font-extrabold">What is in the current-affairs section</h2>
        <p className="mt-2 text-[15px] muted">
          The section holds {items.length} headlines across {months.length} months{ys.length > 1 ? `, from ${ys[0]} to ${ys[ys.length - 1]}` : ys.length === 1 ? ` of ${ys[0]}` : ''}, with {nQuiz} quiz questions at the end of the month pages.
          Each headline is rewritten in plain English and carries the specific fact an exam question would use: a name, a post, a place, a figure.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Kind of event</th><th className="text-right">Headlines</th></tr></thead>
            <tbody>{cats.map(([c, n]) => <tr key={c}><td>{label(c)}</td><td className="text-right">{n}</td></tr>)}</tbody>
          </table>
        </div>
      </section>
      <section className="mt-9" aria-labelledby="ci-use">
        <h2 id="ci-use" className="text-2xl font-extrabold">How to use it</h2>
        <div className="mt-2 space-y-3 text-[15px]">
          <p>Start with the most recent months, because that is where most current-affairs questions in a paper come from. Read a month, take its quiz, and write down the questions you missed as one-line facts.</p>
          <p>Earlier years help for context and for recurring themes such as summits, indices and award cycles. They are also the better place to practise recall, since the facts have already settled.</p>
          <p className="muted">Headlines are summaries for revision. For dates, figures and names that decide an application or a result, check the original notice or the official source.</p>
        </div>
      </section>
    </div>
  );
}
