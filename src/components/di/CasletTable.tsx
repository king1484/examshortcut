import { CASELET, DATA_LABEL, casletQuestions, casletRows, casletText, fmt } from './data';
import { RevealQuestions } from './RevealQuestions';

/* Caselet (paragraph data) converted into a working table, then three questions. */
export function CasletTable() {
  const rows = casletRows();
  const sum = (k: 'size' | 'girls' | 'boys') => rows.reduce((s, r) => s + r[k], 0);

  return (
    <div className="card p-4 sm:p-5">
      <div className="flex items-start justify-between gap-2 flex-wrap">
        <h3 className="font-extrabold text-lg">4. Caselet to table</h3>
        <span className="chip">{DATA_LABEL}</span>
      </div>

      <p className="text-sm font-semibold mt-3">{CASELET.title}</p>
      <blockquote className="text-sm muted mt-1.5 pl-3" style={{ borderLeft: '3px solid var(--brand)', margin: 0 }}>
        {casletText()}
      </blockquote>
      <p className="text-xs faint mt-3">Step 1 of a caselet: turn the paragraph into a table before you read any question.</p>

      <div className="tbl-wrap mt-2">
        <table className="tbl">
          <caption className="text-xs faint text-left px-2 py-1.5">The caselet above, converted to a table. {DATA_LABEL}.</caption>
          <thead>
            <tr>
              <th scope="col">Batch</th><th scope="col">Ratio part</th><th scope="col">Students</th>
              <th scope="col">Girls %</th><th scope="col">Girls</th><th scope="col">Boys</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r.name}>
                <th scope="row">{r.name}</th>
                <td>{r.part}</td><td>{fmt(r.size)}</td><td>{r.girlsPct}%</td><td>{fmt(r.girls)}</td><td>{fmt(r.boys)}</td>
              </tr>
            ))}
            <tr style={{ background: 'var(--surface-2)' }}>
              <th scope="row">Total</th>
              <td>{rows.reduce((s, r) => s + r.part, 0)}</td><td className="font-bold">{fmt(sum('size'))}</td><td>–</td>
              <td className="font-bold">{fmt(sum('girls'))}</td><td className="font-bold">{fmt(sum('boys'))}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <RevealQuestions items={casletQuestions()} />
    </div>
  );
}
