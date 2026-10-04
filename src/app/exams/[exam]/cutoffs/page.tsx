import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getCutoffs } from '@/lib/content';
import { EXAMS, getExamInfo } from '@/lib/exams';
import { Md } from '@/components/Md';
import React from 'react';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** ssc-cgl keeps its own hand-built cutoffs page with trend charts. */
export function generateStaticParams() {
  return EXAMS.filter((e) => e.id !== 'ssc-cgl').map((e) => ({ exam: e.id }));
}

type Params = Promise<{ exam: string }>;

const HEADING_OVERRIDES: Record<string, string> = {
  iims: 'IIMs',
  otherColleges: 'Other top colleges',
  tier1: 'Tier 1',
  tier2: 'Tier 2',
  paper1: 'Paper 1',
  paper2: 'Paper 2',
  prelims: 'Prelims',
  mains: 'Mains',
  final: 'Final cutoffs',
  cbt1: 'CBT 1',
  cbt2: 'CBT 2',
  history: 'History',
};

function humanize(key: string) {
  if (HEADING_OVERRIDES[key]) return HEADING_OVERRIDES[key];
  return key.replace(/([a-z])([A-Z])/g, '$1 $2').replace(/^./, (c) => c.toUpperCase());
}

/** Render a cell: scalars as-is, objects/arrays as compact "key: value" lines. */
function Cell({ v }: { v: unknown }) {
  if (v === null || v === undefined || v === '') return <span className="faint">—</span>;
  if (typeof v === 'string' || typeof v === 'number' || typeof v === 'boolean') return <Md inline>{String(v)}</Md>;
  const entries = Array.isArray(v) ? v.map((x, i) => [String(i), x] as [string, unknown]) : Object.entries(v as Record<string, unknown>);
  return (
    <ul className="text-[13px] leading-snug space-y-0.5">
      {entries.map(([k, val]) => (
        <li key={k}>{val === null || val === undefined || val === '' ? null : <><b>{humanize(k)}:</b> <Md inline>{String(val)}</Md></>}</li>
      ))}
    </ul>
  );
}

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  if (!info) return {};
  return {
    title: `${info.name} cutoffs — official, category-wise`,
    description: `${info.name} cutoffs: official qualifying marks and typical shortlist levels, category-wise, with honest notes on what each row means.`,
    alternates: { canonical: `/exams/${id}/cutoffs/` },
  };
}

export default async function CutoffsPage({ params }: { params: Params }) {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  if (!info || id === 'ssc-cgl') notFound();
  const data = getCutoffs(id);
  if (!data) notFound();

  const sections = Object.entries(data).filter(
    ([k, v]) => k !== 'notes' && k !== 'sources' && Array.isArray(v) && v.length > 0,
  ) as [string, Record<string, unknown>[]][];

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">{info.name} cutoffs</h1>
      {'notes' in data && typeof data.notes === 'string' && (
        <Md className="muted mt-2 max-w-3xl">{data.notes}</Md>
      )}
      {sections.map(([key, rows]) => {
        const cols: string[] = [];
        for (const r of rows) for (const k of Object.keys(r)) if (!cols.includes(k)) cols.push(k);
        return (
          <section key={key} className="mt-8">
            <h2 className="text-xl font-extrabold">{humanize(key)}</h2>
            <div className="card mt-3 overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="text-left text-xs uppercase tracking-wide faint">
                    {cols.map((c) => <th key={c} className="py-2.5 px-3 font-semibold border-b" style={{ borderColor: 'var(--line)' }}>{humanize(c)}</th>)}
                  </tr>
                </thead>
                <tbody>
                  {rows.map((r, i) => (
                    <tr key={i} className="border-b last:border-0 align-top" style={{ borderColor: 'var(--line)' }}>
                      {cols.map((c) => <td key={c} className="py-2.5 px-3"><Cell v={r[c]} /></td>)}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        );
      })}
      <p className="faint text-xs mt-8">
        Cutoff rows are compiled from official result notices and reputable reproductions — see the notes above for what each row means.
      </p>
    </div>
  );
}
