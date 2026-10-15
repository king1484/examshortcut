import Link from 'next/link';
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getCutoffs } from '@/lib/content';
import { CglExpectedDepth, CglFinalDepth, CglYearDepth } from '@/components/exam-pages/CglDepth';

export const dynamic = 'force-static';
export const dynamicParams = false;

/* eslint-disable @typescript-eslint/no-explicit-any */

interface CutoffList { year: number; list: string; maxMarks: number; cutoffs: Record<string, number> }

const MAIN_LIST = 'all posts except AAO/JSO';
const CAT_ORDER = ['UR', 'EWS', 'OBC', 'SC', 'ST'];

function data() {
  const d = getCutoffs() as any;
  const tier1 = ((d?.tier1 ?? []) as CutoffList[]).filter((l) => l.cutoffs);
  const final = ((d?.final ?? []) as CutoffList[]).filter((l) => l.cutoffs);
  return { tier1, final };
}

function slugs(): string[] {
  const { tier1, final } = data();
  const years = [...new Set(tier1.map((l) => l.year))].sort((a, b) => b - a).map(String);
  return [...years, ...(final.length ? ['final-merit'] : []), ...(tier1.some((l) => l.list.includes(MAIN_LIST)) ? ['expected-2026'] : [])];
}

export function generateStaticParams() {
  return slugs().map((slug) => ({ slug }));
}

const fmt = (n: number) => String(Math.round(n * 100) / 100);
const cats = (c: Record<string, number>) => [...CAT_ORDER.filter((k) => k in c), ...Object.keys(c).filter((k) => !CAT_ORDER.includes(k))];

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  if (slug === 'final-merit') {
    return {
      title: 'SSC CGL final merit cutoff (out of 390) — post-wise, category-wise',
      description: 'SSC CGL final selection cutoffs out of 390 marks for AAO and ASO by category, how Tier 2 Paper 1 decides merit, and how far Tier 1 scores matter.',
    };
  }
  if (slug === 'expected-2026') {
    return {
      title: 'SSC CGL 2026 expected Tier 1 cutoff — range from the last 3 years',
      description: 'Expected SSC CGL 2026 Tier 1 cutoff band for UR, EWS, OBC, SC and ST, built from the official 2023, 2024 and 2025 cutoffs, with what moves the number each year.',
    };
  }
  return {
    title: `SSC CGL ${slug} Tier 1 cutoff — UR, EWS, OBC, SC, ST (category-wise)`,
    description: `Official SSC CGL ${slug} Tier 1 cutoff marks for UR, EWS, OBC, SC and ST, how they changed from the previous year, and the safe score to aim for in your mocks.`,
  };
}

function CutoffTable({ l, prev }: { l: CutoffList; prev?: CutoffList }) {
  return (
    <div className="card p-4 sm:p-5 mt-4">
      <h3 className="font-extrabold leading-snug">{l.list}</h3>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>Category</th><th className="text-right">Cutoff (out of {l.maxMarks})</th>{prev && <th className="text-right">vs {prev.year}</th>}</tr></thead>
          <tbody>
            {cats(l.cutoffs).map((c) => {
              const was = prev?.cutoffs?.[c];
              const diff = was != null ? l.cutoffs[c] - was : null;
              return (
                <tr key={c}>
                  <td className="font-semibold">{c}</td>
                  <td className="text-right font-bold">{fmt(l.cutoffs[c])}</td>
                  {prev && <td className="text-right" style={{ color: diff == null ? 'var(--ink-3)' : diff >= 0 ? 'var(--bad)' : 'var(--ok)' }}>
                    {diff == null ? '—' : `${diff >= 0 ? '+' : ''}${fmt(diff)}`}
                  </td>}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function Footer({ current }: { current: string }) {
  const all = slugs().filter((s) => s !== current);
  const label = (s: string) => s === 'final-merit' ? 'Final merit (out of 390)' : s === 'expected-2026' ? 'Expected 2026' : `${s} Tier 1`;
  return (
    <>
      <div className="card p-4 sm:p-5 mt-8">
        <div className="kicker">Check your own score</div>
        <p className="text-sm muted mt-1">Enter your mock result in the <Link className="underline" href="/exams/ssc-cgl/score-calculator/">score calculator</Link> to see the gap to the cutoff by category, or read your response sheet in the <Link className="underline" href="/exams/ssc-cgl/marks-calculator/">marks calculator</Link>. Then take a <Link className="underline" href="/exams/ssc-cgl/mocks/">full mock</Link>.</p>
      </div>
      <div className="mt-6">
        <div className="kicker">More cutoff pages</div>
        <div className="flex flex-wrap gap-2 mt-2">
          <Link href="/exams/ssc-cgl/cutoffs/" className="chip">All cutoffs (explorer)</Link>
          {all.map((s) => <Link key={s} href={`/exams/ssc-cgl/cutoffs/${s}/`} className="chip">{label(s)}</Link>)}
        </div>
      </div>
    </>
  );
}

export default async function CutoffSlugPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  if (!slugs().includes(slug)) notFound();
  const { tier1, final } = data();

  if (slug === 'final-merit') {
    return (
      <div className="max-w-3xl mx-auto">
        <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL final merit cutoff</h1>
        <p className="muted mt-2 text-[15px]">
          Final selection is decided on <b>Tier 2 Paper 1 marks (out of 390)</b>, not on Tier 1. Tier 1 only decides who is called for Tier 2. The cutoffs below are post-wise and category-wise.
        </p>
        {final.map((l) => <CutoffTable key={l.list} l={l} />)}
        <p className="text-xs faint mt-4">Cutoffs differ post by post and list by list, and decimals can differ slightly between reproductions. The official SSC result PDF is always the final word.</p>
        <CglFinalDepth />
        <Footer current={slug} />
      </div>
    );
  }

  if (slug === 'expected-2026') {
    const rows = tier1.filter((l) => l.list.includes(MAIN_LIST)).sort((a, b) => a.year - b.year);
    const all = [...new Set(rows.flatMap((l) => cats(l.cutoffs)))];
    const years = rows.map((r) => r.year);
    return (
      <div className="max-w-3xl mx-auto">
        <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL 2026 expected Tier 1 cutoff</h1>
        <p className="muted mt-2 text-[15px]">
          SSC does not publish a cutoff in advance. This page is an <b>estimate</b>: the band is the lowest and highest official Tier 1 cutoff of {years.join(', ')} for the main list. Treat it as a target to beat in your mocks, not a prediction.
        </p>
        <div className="card p-4 sm:p-5 mt-4">
          <div className="tbl-wrap">
            <table className="tbl">
              <thead><tr><th>Category</th>{rows.map((r) => <th key={r.year} className="text-right">{r.year}</th>)}<th className="text-right">Band (low – high)</th></tr></thead>
              <tbody>
                {all.map((c) => {
                  const vals = rows.map((r) => r.cutoffs[c]).filter((v) => v != null);
                  return (
                    <tr key={c}>
                      <td className="font-semibold">{c}</td>
                      {rows.map((r) => <td key={r.year} className="text-right">{r.cutoffs[c] != null ? fmt(r.cutoffs[c]) : '—'}</td>)}
                      <td className="text-right font-bold">{vals.length ? `${fmt(Math.min(...vals))} – ${fmt(Math.max(...vals))}` : '—'}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
          <p className="text-xs faint mt-3">Out of 200 marks, after normalisation. List: {rows[rows.length - 1]?.list}.</p>
        </div>

        <h2 className="text-xl font-extrabold mt-8">What moves the cutoff</h2>
        <ul className="check mt-2 text-[15px]">
          <li><b>Paper difficulty.</b> A harder paper pushes normalised scores down. The drop from 2024 to 2025 in the UR column above is an example.</li>
          <li><b>Vacancies and candidates.</b> More posts for the same pool lets SSC call more candidates for Tier 2, which usually lowers the line.</li>
          <li><b>Shift-wise difficulty.</b> Marks are normalised across shifts, so your raw score and your normalised score can differ. See <Link className="underline" href="/exam-analysis/">shift-wise exam analysis</Link> for how each shift felt.</li>
          <li><b>Category.</b> Reserved-category lines sit well below UR, and the gap changes every year.</li>
        </ul>

        <h2 className="text-xl font-extrabold mt-8">How to use this</h2>
        <p className="text-[15px] muted mt-2">
          Aim for a mock score a comfortable margin above the <b>high end</b> of your category&apos;s band, because Tier 1 is only a screening round and a borderline score can miss. Remember Tier 1 marks do not count towards the final merit for most posts, so use the extra time in Tier 2 preparation too.
        </p>
        <CglExpectedDepth />
        <Footer current={slug} />
      </div>
    );
  }

  const year = Number(slug);
  const lists = tier1.filter((l) => l.year === year);
  if (!lists.length) notFound();
  const earlier = (l: CutoffList) => tier1.filter((x) => x.list === l.list && x.year < year).sort((a, b) => b.year - a.year)[0];
  const main = lists.find((l) => l.list.includes(MAIN_LIST)) ?? lists[0];
  const best = main.cutoffs.UR;

  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL {year} Tier 1 cutoff</h1>
      <p className="muted mt-2 text-[15px]">
        Category-wise Tier 1 cutoffs for CGL {year} (out of {main.maxMarks}, after normalisation). For the main list, <b>UR was {fmt(best)}</b>. Tier 1 is a screening round: it decides who is called for Tier 2.
      </p>
      {lists.map((l) => <CutoffTable key={l.list} l={l} prev={earlier(l)} />)}
      <p className="text-xs faint mt-4">Cutoffs are declared per post list. Decimals can differ slightly between reproductions of SSC result notices; the SSC PDF is canonical. A green change means the cutoff fell compared with the previous year.</p>
      <CglYearDepth year={year} />
      <Footer current={slug} />
    </div>
  );
}
