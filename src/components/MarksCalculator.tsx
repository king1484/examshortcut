'use client';
import { useMemo, useState } from 'react';
import Link from 'next/link';
import { parseSheet, scoreSheet, type SheetParse } from '@/lib/responseSheet';

/* eslint-disable @typescript-eslint/no-explicit-any */

const num = (n: number) => String(Math.round(n * 100) / 100);

export function MarksCalculator({ cutoffs }: { cutoffs: any }) {
  const [sheet, setSheet] = useState<SheetParse | null>(null);
  const [error, setError] = useState('');
  const [fileName, setFileName] = useState('');
  const [paste, setPaste] = useState('');
  const [plus, setPlus] = useState(2);
  const [minus, setMinus] = useState(0.5);
  const [filter, setFilter] = useState<'all' | 'correct' | 'wrong' | 'skipped'>('all');
  const [cat, setCat] = useState('UR');

  const latest = useMemo(() => {
    const lists = ((cutoffs?.tier1 ?? []) as any[]).filter((l) => l.cutoffs && String(l.list).includes('all posts except'));
    return lists.sort((a, b) => b.year - a.year)[0] ?? null;
  }, [cutoffs]);

  const load = (html: string, name: string) => {
    setError('');
    try {
      const r = parseSheet(html);
      setSheet(r.questions.length ? r : null);
      setFileName(name);
      if (!r.questions.length) setError(r.warnings[0] ?? 'Could not read this file.');
      if (r.scheme) { setPlus(r.scheme.plus); setMinus(r.scheme.minus); }
      else { setPlus(2); setMinus(0.5); }
    } catch {
      setSheet(null);
      setError('Could not read this file. Save the response sheet page as "Webpage, HTML only" and try again.');
    }
  };

  const onFile = async (f: File | undefined) => {
    if (!f) return;
    load(await f.text(), f.name);
  };

  const scored = useMemo(() => (sheet ? scoreSheet(sheet.questions, plus, minus) : null), [sheet, plus, minus]);
  const maxMarks = scored ? (scored.all.total - scored.all.unscored) * plus : 0;
  const attempted = scored ? scored.all.correct + scored.all.wrong : 0;
  const accuracy = attempted ? Math.round((100 * scored!.all.correct) / attempted) : 0;
  const total = scored?.all.marks ?? 0;
  const cutoff = latest?.cutoffs?.[cat] as number | undefined;
  const showCutoff = scored && cutoff != null && Math.abs(scored.all.total * plus - (latest?.maxMarks ?? 200)) < 1;

  const rows = useMemo(() => {
    if (!sheet) return [];
    return sheet.questions.filter((q) => {
      if (q.correct == null) return filter === 'all';
      if (filter === 'all') return true;
      if (filter === 'skipped') return q.chosen == null;
      if (filter === 'correct') return q.chosen === q.correct;
      return q.chosen != null && q.chosen !== q.correct;
    });
  }, [sheet, filter]);

  return (
    <div className="mt-6">
      <div className="card p-4 sm:p-5">
        <div className="kicker">How to use</div>
        <ol className="list-decimal pl-5 mt-2 space-y-1 text-sm muted">
          <li>Open your response sheet on the SSC site (log in with your roll number and password).</li>
          <li>Save the page: Ctrl + S, choose <b>Webpage, HTML only</b>.</li>
          <li>Choose that file below. It is read in your browser and is <b>not uploaded</b> anywhere.</li>
        </ol>
        <label className="btn btn-brand mt-4 inline-block cursor-pointer">
          Choose saved response sheet
          <input type="file" accept=".html,.htm,text/html" className="sr-only" onChange={(e) => onFile(e.target.files?.[0])} />
        </label>
        {fileName && <span className="text-xs faint ml-3">{fileName}</span>}
        <details className="mt-4">
          <summary className="text-sm font-semibold cursor-pointer">Or paste the page source</summary>
          <textarea value={paste} onChange={(e) => setPaste(e.target.value)} rows={4} placeholder="Paste the HTML source of the response sheet"
            className="w-full mt-2 p-2 rounded-lg border text-xs font-mono" style={{ borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' }} />
          <button className="btn mt-2" disabled={!paste.trim()} onClick={() => load(paste, 'pasted source')}>Read pasted source</button>
        </details>
        {error && <p className="text-sm mt-3" style={{ color: 'var(--bad)' }} role="alert">{error}</p>}
      </div>

      {sheet && scored && (
        <>
          {sheet.warnings.length > 0 && (
            <div className="card p-3 mt-4 text-sm" style={{ borderColor: 'var(--warn)' }}>
              {sheet.warnings.map((w) => <p key={w}>{w}</p>)}
            </div>
          )}

          <div className="card p-4 sm:p-5 mt-4">
            <div className="flex items-center justify-between gap-3 flex-wrap">
              <div className="text-sm">
                {sheet.candidate.subject && <b>{sheet.candidate.subject}</b>}
                {sheet.candidate.date && <span className="faint"> · {sheet.candidate.date} {sheet.candidate.time ?? ''}</span>}
              </div>
              <div className="flex items-center gap-3 text-xs font-semibold faint uppercase">
                <label>Correct +<input type="number" step="0.25" min={0} value={plus} onChange={(e) => setPlus(Number(e.target.value) || 0)} className="w-14 ml-1 p-1 rounded border text-sm font-bold" style={{ borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' }} /></label>
                <label>Wrong −<input type="number" step="0.25" min={0} value={minus} onChange={(e) => setMinus(Number(e.target.value) || 0)} className="w-14 ml-1 p-1 rounded border text-sm font-bold" style={{ borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' }} /></label>
              </div>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center mt-4">
              <div><div className="text-3xl font-extrabold">{num(total)}</div><div className="text-xs faint font-semibold uppercase">Marks / {num(maxMarks)}</div></div>
              <div><div className="text-3xl font-extrabold" style={{ color: 'var(--ok)' }}>{scored.all.correct}</div><div className="text-xs faint font-semibold uppercase">Correct</div></div>
              <div><div className="text-3xl font-extrabold" style={{ color: 'var(--bad)' }}>{scored.all.wrong}</div><div className="text-xs faint font-semibold uppercase">Wrong</div></div>
              <div><div className="text-3xl font-extrabold">{scored.all.skipped}</div><div className="text-xs faint font-semibold uppercase">Skipped</div></div>
            </div>
            <p className="text-sm muted mt-3">
              Accuracy <b>{accuracy}%</b> on {attempted} attempted. Negative marking cost you <b>{num(scored.all.wrong * minus)}</b> marks.
            </p>

            <div className="tbl-wrap mt-4">
              <table className="tbl">
                <thead><tr><th>Section</th><th className="text-right">Correct</th><th className="text-right">Wrong</th><th className="text-right">Skipped</th><th className="text-right">Marks</th></tr></thead>
                <tbody>
                  {scored.sections.map((s) => (
                    <tr key={s.name}><td className="font-semibold">{s.name}</td><td className="text-right">{s.correct}</td><td className="text-right">{s.wrong}</td><td className="text-right">{s.skipped}</td><td className="text-right font-bold">{num(s.marks)}</td></tr>
                  ))}
                </tbody>
              </table>
            </div>
            <p className="text-xs faint mt-3">
              This is your raw score. SSC normalises scores across shifts, so your official score can differ by several marks either way, and the shift-wise analysis shows how hard your shift was.
            </p>
          </div>

          {showCutoff && latest && (
            <div className="card p-4 sm:p-5 mt-4">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="text-sm font-bold">Against the {latest.year} cutoff:</span>
                {Object.keys(latest.cutoffs).map((c) => (
                  <button key={c} className="chip" style={cat === c ? { background: 'var(--ink)', color: 'var(--bg)' } : {}} onClick={() => setCat(c)}>{c}</button>
                ))}
              </div>
              <p className="text-sm mt-3">
                Cutoff <b>{num(cutoff!)}</b> · your raw marks <b>{num(total)}</b> ·{' '}
                <b style={{ color: total - cutoff! >= 0 ? 'var(--ok)' : 'var(--warn)' }}>{total - cutoff! >= 0 ? '+' : ''}{num(total - cutoff!)}</b>
              </p>
              <p className="text-xs faint mt-2">Compare with care: the cutoff is a normalised score, yours is raw. See <Link className="underline" href="/exams/ssc-cgl/cutoffs/expected-2026/">the expected 2026 band</Link>.</p>
            </div>
          )}

          <div className="card p-4 sm:p-5 mt-4">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-sm font-bold mr-1">Question by question</span>
              {(['all', 'correct', 'wrong', 'skipped'] as const).map((f) => (
                <button key={f} className="chip" style={filter === f ? { background: 'var(--ink)', color: 'var(--bg)' } : {}} onClick={() => setFilter(f)}>{f}</button>
              ))}
            </div>
            <div className="flex flex-wrap gap-1.5 mt-3">
              {rows.map((q) => {
                const state = q.correct == null ? 'none' : q.chosen == null ? 'skip' : q.chosen === q.correct ? 'ok' : 'bad';
                const bg = state === 'ok' ? 'var(--ok)' : state === 'bad' ? 'var(--bad)' : 'var(--surface-2)';
                return (
                  <span key={`${q.section}-${q.n}`} title={`${q.section} · Q${q.n} · your option ${q.chosen ?? 'none'}${q.correct ? ` · correct ${q.correct}` : ''}`}
                    className="w-8 h-8 inline-flex items-center justify-center rounded-md text-xs font-bold"
                    style={{ background: bg, color: state === 'ok' || state === 'bad' ? '#fff' : 'var(--ink-2)' }}>{q.n}</span>
                );
              })}
            </div>
            <p className="text-xs faint mt-3">Hover a number for your option and the correct one. Question numbers restart in each section.</p>
          </div>
        </>
      )}
    </div>
  );
}
