import { LINE, DATA_LABEL, lineQuestions, fmt } from './data';
import { RevealQuestions } from './RevealQuestions';

/* Two-line graph over six periods, inline SVG, theme colours via CSS variables. */
export function LineGraph() {
  const { title, unit, periods, revenue, spend } = LINE;
  const lines = [revenue, spend];
  const W = 400, H = 250, L = 36, R = 14, T = 16, B = 30;
  const plotW = W - L - R, plotH = H - T - B;
  const all = lines.flatMap((l) => l.values);
  const step = 20;
  const lo = Math.floor(Math.min(...all) / step) * step - step;
  const hi = Math.ceil(Math.max(...all) / step) * step;
  const ticks: number[] = [];
  for (let t = lo; t <= hi; t += step) ticks.push(t);
  const x = (i: number) => L + (i * plotW) / (periods.length - 1);
  const y = (v: number) => T + plotH - ((v - lo) / (hi - lo)) * plotH;

  const id = 'di-line';
  return (
    <div className="card p-4 sm:p-5">
      <div className="flex items-start justify-between gap-2 flex-wrap">
        <h3 className="font-extrabold text-lg">2. Line graph</h3>
        <span className="chip">{DATA_LABEL}</span>
      </div>

      <figure className="mt-2" style={{ margin: 0 }}>
        <figcaption id={`${id}-cap`} className="text-sm font-semibold mt-2">{title}</figcaption>
        <div className="flex gap-3 flex-wrap mt-1.5 text-xs muted">
          {lines.map((l) => (
            <span key={l.name} className="inline-flex items-center gap-1.5">
              <span aria-hidden="true" style={{ width: 14, height: 3, borderRadius: 2, background: l.color, display: 'inline-block' }} />
              {l.name}
            </span>
          ))}
        </div>
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full mt-2 mx-auto" style={{ height: 'auto', display: 'block', maxWidth: 560 }} role="img" aria-labelledby={`${id}-cap ${id}-desc`}>
          <desc id={`${id}-desc`}>
            Line graph of {revenue.name.toLowerCase()} and {spend.name.toLowerCase()} in {unit} from {periods[0]} to {periods[periods.length - 1]}. The full values are in the data table below.
          </desc>
          {ticks.map((t) => (
            <g key={t}>
              <line x1={L} x2={W - R} y1={y(t)} y2={y(t)} stroke="var(--line)" strokeWidth="1" />
              <text x={L - 5} y={y(t) + 3.5} fontSize="10" fill="var(--ink-3)" textAnchor="end">{t}</text>
            </g>
          ))}
          {periods.map((p, i) => (
            <text key={p} x={x(i)} y={H - 11} fontSize="10.5" fill="var(--ink-3)" textAnchor="middle">{p}</text>
          ))}
          {lines.map((l, li) => {
            const d = l.values.map((v, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)},${y(v).toFixed(1)}`).join(' ');
            // revenue labels above its points, expenditure labels below (revenue is the upper line)
            const dy = li === 0 ? -8 : 15;
            return (
              <g key={l.name}>
                <path d={d} fill="none" stroke={l.color} strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                {l.values.map((v, i) => (
                  <g key={i}>
                    <circle cx={x(i)} cy={y(v)} r="3.5" fill={l.color} stroke="var(--surface)" strokeWidth="1.5" />
                    <text x={x(i)} y={y(v) + dy} fontSize="9" fontWeight="700" fill="var(--ink-2)" textAnchor="middle">{v}</text>
                  </g>
                ))}
              </g>
            );
          })}
          <text x={L} y={9} fontSize="9.5" fill="var(--ink-3)">{unit}</text>
        </svg>

        <details className="mt-2">
          <summary className="text-xs font-semibold cursor-pointer" style={{ color: 'var(--brand-text)' }}>View the same data as a table</summary>
          <div className="tbl-wrap mt-2">
            <table className="tbl">
              <caption className="text-xs faint text-left px-2 py-1.5">{title}. {DATA_LABEL}.</caption>
              <thead>
                <tr><th scope="col">Series</th>{periods.map((p) => <th scope="col" key={p}>{p}</th>)}</tr>
              </thead>
              <tbody>
                {lines.map((l) => (
                  <tr key={l.name}>
                    <th scope="row">{l.name}</th>
                    {l.values.map((v, i) => <td key={i}>{fmt(v)}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </details>
      </figure>

      <RevealQuestions items={lineQuestions()} />
    </div>
  );
}
