'use client';
import { useMemo, useState } from 'react';
import { interp, normCdf } from '@/lib/examTools';

/* Both modes are estimates. The boards publish the method, not a calculator, and they use the full score
   distribution of every shift, which candidates do not have. Mode 1 assumes a bell curve in each shift.
   Mode 2 matches percentiles using a short table the reader fills in, which is the idea behind both the
   SSC equipercentile method and the RRB percentile method. */

const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };
const on = { background: 'var(--ink)', color: 'var(--bg)' };
const r2 = (n: number) => Math.round(n * 100) / 100;
const PCTS = [10, 25, 50, 75, 90, 95, 99];
const SAMPLE_MINE = [0.3, 0.4, 0.52, 0.64, 0.74, 0.8, 0.88];
const SAMPLE_BASE = [0.34, 0.44, 0.56, 0.68, 0.78, 0.84, 0.91];

function Field({ label, value, onChange, hint }: { label: string; value: string; onChange: (v: string) => void; hint?: string }) {
  return (
    <label className="text-xs font-semibold faint uppercase">
      {label}
      <input type="number" inputMode="decimal" value={value} onChange={(e) => onChange(e.target.value)}
        className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
      {hint && <span className="block text-xs font-normal normal-case mt-1 faint">{hint}</span>}
    </label>
  );
}

export function NormalisationCalculator({ family, maxDefault }: { family: 'ssc' | 'rrb'; maxDefault: number }) {
  const [mode, setMode] = useState<'bell' | 'table'>('bell');
  const [max, setMax] = useState(String(maxDefault));
  const [raw, setRaw] = useState('');
  const [m1, setM1] = useState(''); const [s1, setS1] = useState('');
  const [m2, setM2] = useState(''); const [s2, setS2] = useState('');
  const [mine, setMine] = useState<string[]>(PCTS.map(() => ''));
  const [base, setBase] = useState<string[]>(PCTS.map(() => ''));

  const mx = Number(max) || 0;
  const x = raw === '' ? null : Number(raw);

  const bell = useMemo(() => {
    if (x === null || !mx || m1 === '' || s1 === '' || m2 === '' || s2 === '') return null;
    const sd1 = Number(s1), sd2 = Number(s2);
    if (sd1 <= 0 || sd2 <= 0) return null;
    const z = (x - Number(m1)) / sd1;
    const out = Math.max(0, Math.min(mx, Number(m2) + z * sd2));
    return { z, pct: normCdf(z) * 100, out };
  }, [x, mx, m1, s1, m2, s2]);

  const table = useMemo((): { err: string } | { pct: number; out: number } | null => {
    if (x === null || !mx) return null;
    const a = mine.map(Number), b = base.map(Number);
    if (mine.some((v) => v === '') || base.some((v) => v === '')) return { err: 'Fill every row for both shifts.' };
    const inc = (arr: number[]) => arr.every((v, i) => i === 0 || v >= arr[i - 1]);
    if (!inc(a) || !inc(b)) return { err: 'Marks must not fall as the percentile rises. Check the rows.' };
    const mineLine: [number, number][] = [[0, 0], ...a.map((m, i) => [m, PCTS[i]] as [number, number]), [mx, 100]];
    const baseLine: [number, number][] = [[0, 0], ...b.map((m, i) => [PCTS[i], m] as [number, number]), [100, mx]];
    const pct = interp(mineLine, x);
    return { pct, out: Math.max(0, Math.min(mx, interp(baseLine, pct))) };
  }, [x, mx, mine, base]);

  const sample = () => {
    if (mode === 'bell') {
      setRaw(String(Math.round(mx * 0.6))); setM1(String(Math.round(mx * 0.48))); setS1(String(Math.round(mx * 0.14)));
      setM2(String(Math.round(mx * 0.53))); setS2(String(Math.round(mx * 0.15)));
    } else {
      setRaw(String(Math.round(mx * 0.6)));
      setMine(SAMPLE_MINE.map((f) => String(Math.round(f * mx)))); setBase(SAMPLE_BASE.map((f) => String(Math.round(f * mx))));
    }
  };

  const result = mode === 'bell' ? (bell ? { pct: bell.pct, out: bell.out } : null) : (table && 'out' in table ? { pct: table.pct, out: table.out } : null);
  const err = mode === 'table' && table && 'err' in table ? table.err : null;
  const baseName = family === 'ssc' ? 'the reference shift' : 'the base shift';

  return (
    <div className="mt-6">
      <div className="flex gap-2 flex-wrap">
        <button className="chip" style={mode === 'bell' ? on : {}} onClick={() => setMode('bell')}>Mean and SD (quick)</button>
        <button className="chip" style={mode === 'table' ? on : {}} onClick={() => setMode('table')}>Percentile table (closer to the real method)</button>
      </div>

      <div className="card p-5 mt-4">
        <div className="grid sm:grid-cols-2 gap-4">
          <Field label="Maximum marks of the paper" value={max} onChange={setMax} />
          <Field label="Your raw marks" value={raw} onChange={setRaw} hint="Net of negative marking, before normalisation." />
        </div>

        {mode === 'bell' ? (
          <div className="grid sm:grid-cols-2 gap-4 mt-4">
            <Field label="Your shift: average marks" value={m1} onChange={setM1} />
            <Field label="Your shift: standard deviation" value={s1} onChange={setS1} />
            <Field label={`${family === 'ssc' ? 'Reference' : 'Base'} shift: average marks`} value={m2} onChange={setM2} />
            <Field label={`${family === 'ssc' ? 'Reference' : 'Base'} shift: standard deviation`} value={s2} onChange={setS2} />
          </div>
        ) : (
          <div className="mt-4">
            <p className="text-sm muted">For each percentile, enter the marks that candidate would have in each shift. Shift-wise toppers and averages shared by coaching analyses can help you fill this in.</p>
            <div className="tbl-wrap mt-3">
              <table className="tbl">
                <thead><tr><th>Percentile</th><th>Your shift (marks)</th><th>{family === 'ssc' ? 'Reference' : 'Base'} shift (marks)</th></tr></thead>
                <tbody>
                  {PCTS.map((p, i) => (
                    <tr key={p}>
                      <td>{p}th</td>
                      {[mine, base].map((arr, k) => (
                        <td key={k}>
                          <input type="number" inputMode="decimal" aria-label={`${p}th percentile marks, ${k ? 'base' : 'your'} shift`} value={arr[i]}
                            onChange={(e) => (k ? setBase : setMine)((prev) => prev.map((v, j) => (j === i ? e.target.value : v)))}
                            className="w-24 p-1.5 rounded-lg border text-sm font-bold" style={input} />
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
        <button className="btn mt-4" onClick={sample}>Fill with sample numbers</button>
        <span className="text-xs faint ml-2">Sample numbers only, to show how it works.</span>
      </div>

      {err && <p className="text-sm mt-4" style={{ color: 'var(--warn)' }}>{err}</p>}

      {result && x !== null && (
        <div className="card p-5 mt-5" aria-live="polite">
          <div className="grid grid-cols-3 gap-3 text-center">
            <div><div className="text-3xl font-extrabold">{r2(x)}</div><div className="text-xs faint font-semibold uppercase">Raw marks</div></div>
            <div><div className="text-3xl font-extrabold">{r2(result.pct)}</div><div className="text-xs faint font-semibold uppercase">Percentile in your shift</div></div>
            <div><div className="text-3xl font-extrabold" style={{ color: 'var(--brand)' }}>{r2(result.out)}</div><div className="text-xs faint font-semibold uppercase">Normalised (estimate)</div></div>
          </div>
          <p className="text-sm mt-3">
            Your raw score sits at about the {r2(result.pct)}th percentile of your shift. The same percentile in {baseName} is worth about <b>{r2(result.out)}</b>, a change of {result.out - x >= 0 ? '+' : ''}{r2(result.out - x)} marks.
          </p>
          <p className="text-xs faint mt-2">
            Estimate only. {mode === 'bell' ? 'It assumes marks in each shift follow a bell curve, which real score distributions only roughly do.' : 'It joins your table points with straight lines.'}{' '}
            The official normalised score uses the full score distribution of every shift, so it can differ.
          </p>
        </div>
      )}
      {!result && !err && <p className="text-sm muted mt-4">Enter your marks and the shift numbers, or use the sample button, to see the estimate.</p>}
    </div>
  );
}
