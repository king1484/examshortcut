import type { Metadata } from 'next';
import Link from 'next/link';
import { getWeightage, SECTION_META, type SectionId } from '@/lib/content';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL topic-wise weightage — which topics are asked how often',
  description: 'Topic-wise question counts from recent SSC CGL Tier 1 shift analyses: which Quant, Reasoning, English and GA topics appear in every shift and how many questions they carry.',
};

export default function WeightagePage() {
  const w = getWeightage();
  if (!w) {
    return <div className="card p-8 text-center max-w-2xl mx-auto"><h1 className="text-2xl font-extrabold">Weightage data is being compiled</h1><p className="muted mt-2">Check back shortly.</p></div>;
  }

  const years = Object.keys(w.sections?.quant?.[0]?.counts ?? {}).sort();

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">Topic-wise weightage, from real shifts</h1>
      <p className="muted mt-2">Average questions per shift by topic, compiled from public post-exam analyses of recent CGL Tier 1 papers. Use it to decide what to study first — it's also why every topic page shows an importance tag.</p>
      <Md text={w.notes} />

      {(Object.keys(w.sections ?? {}) as SectionId[]).map((sid) => {
        const rows = (w.sections[sid] ?? []).slice().sort((a: any, b: any) => (b.avg ?? 0) - (a.avg ?? 0));
        if (!rows.length) return null;
        const maxAvg = Math.max(...rows.map((r: any) => r.avg ?? 0), 1);
        return (
          <section key={sid} className="mt-8">
            <h2 className="text-2xl font-extrabold" style={{ color: SECTION_META[sid].color }}>{SECTION_META[sid].name}</h2>
            <div className="tbl-wrap mt-3">
              <table className="tbl">
                <thead><tr><th>Topic</th>{years.map((y) => <th key={y} className="text-center">{y}</th>)}<th>Avg/shift</th><th></th></tr></thead>
                <tbody>
                  {rows.map((r: any) => (
                    <tr key={r.topicId}>
                      <td><Link className="underline decoration-dotted" href={`/${sid}/${r.topicId}/`}>{r.topicId.replace(/-/g, ' ')}</Link></td>
                      {years.map((y) => <td key={y} className="text-center">{r.counts?.[y] ?? '—'}</td>)}
                      <td className="font-bold">{r.avg != null ? r.avg.toFixed(1) : '—'}</td>
                      <td style={{ minWidth: 90 }}>
                        <div className="h-2.5 rounded-full" style={{ width: `${Math.round(((r.avg ?? 0) / maxAvg) * 100)}%`, minWidth: (r.avg ?? 0) > 0 ? 6 : 0, background: SECTION_META[sid].color }} />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        );
      })}

      {w.analysis && (
        <section className="mt-8 card p-5">
          <h2 className="font-extrabold text-lg">Shift difficulty & good attempts</h2>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Year</th><th>Quant</th><th>Reasoning</th><th>English</th><th>GA</th></tr></thead>
              <tbody>
                {Object.entries(w.analysis.difficulty ?? {}).map(([y, secs]: any) => (
                  <tr key={y}><td className="font-bold">{y}</td>{['quant', 'reasoning', 'english', 'ga'].map((s) => <td key={s}>{secs[s] ?? '—'}</td>)}</tr>
                ))}
                {w.analysis.goodAttempts && Object.entries(w.analysis.goodAttempts).map(([y, v]: any) => (
                  <tr key={`g${y}`}><td>{y} good attempts</td><td colSpan={4}>{typeof v === 'string' ? v : JSON.stringify(v)}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

    </div>
  );
}

function Md({ text }: { text?: string }) {
  if (!text) return null;
  return <div className="text-sm muted mt-2" dangerouslySetInnerHTML={{ __html: text.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br/>') }} />;
}
