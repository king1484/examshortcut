'use client';
import { useId, useMemo, useState } from 'react';
import { ageOn, dobWindow, fmtDate, type AgeModel } from './ageModel';

const isIso = (s: string) => /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(new Date(`${s}T00:00:00Z`).getTime());

/** Age eligibility calculator: DOB + category + cut-off date -> eligible or not, per post group. */
export function AgeCalculator({ model, examName }: { model: AgeModel; examName: string }) {
  const uid = useId();
  const [dob, setDob] = useState('');
  const [catId, setCatId] = useState(model.categories[0].id);
  const [cutoff, setCutoff] = useState(model.cutoff);

  const cat = model.categories.find((c) => c.id === catId) ?? model.categories[0];
  const cutoffOk = isIso(cutoff);
  const dobOk = isIso(dob);
  const age = useMemo(() => (dobOk && cutoffOk ? ageOn(dob, cutoff) : null), [dob, cutoff, dobOk, cutoffOk]);

  const rows = useMemo(() => {
    if (!cutoffOk) return [];
    return model.bands.map((b) => {
      const w = dobWindow(cutoff, b, cat.years);
      const ok = dobOk ? dob >= w.earliest && dob <= w.latest : null;
      let why = '';
      if (ok === false) why = dob < w.earliest ? 'Over the upper age limit' : 'Under the minimum age';
      return { b, w, ok, why };
    });
  }, [model.bands, cutoff, cutoffOk, cat.years, dob, dobOk]);

  const field = 'w-full rounded-lg border px-3 py-2 text-sm bg-transparent';
  const fieldStyle = { borderColor: 'var(--line)' };

  return (
    <section id="age-calculator" className="card p-5 mt-6 scroll-mt-28" aria-labelledby={`${uid}-h`}>
      <h2 id={`${uid}-h`} className="text-xl font-extrabold">Age eligibility calculator</h2>
      <p className="text-sm muted mt-1">
        Enter your date of birth and category to see, for each post group in {examName}, whether you are inside the age limit and the exact birth-date window that qualifies. Everything runs in your browser; nothing is stored or sent.
      </p>

      <div className="grid sm:grid-cols-3 gap-3 mt-4">
        <label className="text-sm font-semibold block">Date of birth
          <input type="date" value={dob} onChange={(e) => setDob(e.target.value)} className={`${field} mt-1 font-normal`} style={fieldStyle} />
        </label>
        <label className="text-sm font-semibold block">Category
          <select value={catId} onChange={(e) => setCatId(e.target.value)} className={`${field} mt-1 font-normal`} style={fieldStyle}>
            {model.categories.map((c) => (
              <option key={c.id} value={c.id}>{c.label}{c.years ? ` (+${c.years} yrs)` : ''}</option>
            ))}
          </select>
        </label>
        <label className="text-sm font-semibold block">Age counted as on
          <input type="date" value={cutoff} onChange={(e) => setCutoff(e.target.value)} className={`${field} mt-1 font-normal`} style={fieldStyle} />
        </label>
      </div>

      <p className="text-xs faint mt-2">
        {model.cutoff
          ? <>The cut-off date is pre-filled from this page&apos;s data: <b>{fmtDate(model.cutoff)}</b>. If the official notification gives a different date, type it above, and read the notes on this page to see whether this date belongs to the current or the previous cycle.</>
          : <>This exam&apos;s data does not state a single clean cut-off date, so enter the cut-off date from the official notification above.</>}
      </p>

      {!cutoffOk && <p className="text-sm mt-3 font-semibold" style={{ color: 'var(--warn)' }}>Enter a valid cut-off date to see results.</p>}

      {age && (
        <p className="text-sm mt-4">
          Your age on {fmtDate(cutoff)}: <b>{age.y} years, {age.m} months, {age.d} days</b>
          {cat.years > 0 && <> · relaxation applied: <b>+{cat.years} years</b></>}
        </p>
      )}

      {rows.length > 0 && (
        <div className="tbl-wrap mt-3" aria-live="polite">
          <table className="tbl">
            <thead><tr><th>Post group</th><th>Age limit</th><th>Born between</th>{dobOk && <th>Result</th>}</tr></thead>
            <tbody>
              {rows.map(({ b, w, ok, why }) => (
                <tr key={b.label}>
                  <td className="font-semibold">{b.label}</td>
                  <td>{b.min}–{b.max} yrs{cat.years > 0 ? ` (upper limit ${b.max + cat.years})` : ''}</td>
                  <td>{fmtDate(w.earliest)} to {fmtDate(w.latest)}</td>
                  {dobOk && (
                    <td>
                      <span className="chip" style={ok ? { background: 'var(--ok-soft)', color: 'var(--ok)', borderColor: 'transparent' } : { background: 'var(--bad-soft)', color: 'var(--bad)', borderColor: 'transparent' }}>
                        {ok ? 'Within age limit' : why}
                      </span>
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <div className="text-xs faint mt-3 space-y-1">
        <p>The window is: born on or after (cut-off date minus upper limit minus relaxation, plus one day) and on or before (cut-off date minus minimum age). It matches the &quot;born between&quot; ranges printed in the exam data where they are given.</p>
        {model.manual.length > 0 && (
          <p><b>Not calculated here</b> (these depend on individual circumstances; check the table below and the official notification): {model.manual.map((m) => `${m.category} — ${m.years}`).join('; ')}.</p>
        )}
        <p>Age eligibility is only one condition. Check education, nationality and any physical or post-specific requirements too. The official notification overrides this tool.</p>
      </div>
    </section>
  );
}
