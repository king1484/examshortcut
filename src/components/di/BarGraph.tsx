import { BAR, DATA_LABEL, barQuestions, fmt } from './data';
import { RevealQuestions } from './RevealQuestions';

/* Grouped (multi-series) bar graph, inline SVG, theme colours via CSS variables. */
export function BarGraph() {
  const { title, unit, years, series } = BAR;
  const W = 400, H = 250, L = 34, R = 8, T = 14, B = 30;
  const plotW = W - L - R, plotH = H - T - B;
  const maxV = Math.max(...series.flatMap((s) => s.values));
  const step = 20;
  const top = Math.ceil(maxV / step) * step;
  const ticks = Array.from({ length: top / step + 1 }, (_, i) => i * step);
  const y = (v: number) => T + plotH - (v / top) * plotH;
  const groupW = plotW / years.length;
  const gap = groupW * 0.18;
  const barW = (groupW - gap) / series.length;

  const id = 'di-bar';
  return (
    <div className="card p-4 sm:p-5">
      <div className="flex items-start justify-between gap-2 flex-wrap">
        <h3 className="font-extrabold text-lg">1. Bar graph</h3>
        <span className="chip">{DATA_LABEL}</span>
      </div>

      <figure className="mt-2" style={{ margin: 0 }}>
        <figcaption id={`${id}-cap`} className="text-sm font-semibold mt-2">{title}</figcaption>
        <div className="flex gap-3 flex-wrap mt-1.5 text-xs muted">
          {series.map((s) => (
            <span key={s.name} className="inline-flex items-center gap-1.5">
              <span aria-hidden="true" style={{ width: 10, height: 10, borderRadius: 2, background: s.color, display: 'inline-block' }} />
              {s.name}
            </span>
          ))}
        </div>
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full mt-2 mx-auto" style={{ height: 'auto', display: 'block', maxWidth: 560 }} role="img" aria-labelledby={`${id}-cap ${id}-desc`}>
          <desc id={`${id}-desc`}>
            Grouped bar graph of production in {unit} for {series.map((s) => s.name).join(', ')} from {years[0]} to {years[years.length - 1]}. The full values are in the data table below.
          </desc>
          {ticks.map((t) => (
            <g key={t}>
              <line x1={L} x2={W - R} y1={y(t)} y2={y(t)} stroke="var(--line)" strokeWidth="1" />
              <text x={L - 5} y={y(t) + 3.5} fontSize="10" fill="var(--ink-3)" textAnchor="end">{t}</text>
            </g>
          ))}
          {years.map((yr, gi) => {
            const gx = L + gi * groupW + gap / 2;
            return (
              <g key={yr}>
                {series.map((s, si) => {
                  const v = s.values[gi];
                  const bx = gx + si * barW;
                  return (
                    <g key={s.name}>
                      <rect x={bx + 0.75} y={y(v)} width={barW - 1.5} height={y(0) - y(v)} rx="1.5" fill={s.color} />
                      <text x={bx + barW / 2} y={y(v) - 3} fontSize="8.5" fontWeight="700" fill="var(--ink-2)" textAnchor="middle">{v}</text>
                    </g>
                  );
                })}
                <text x={L + gi * groupW + groupW / 2} y={H - 11} fontSize="10.5" fill="var(--ink-3)" textAnchor="middle">{yr}</text>
              </g>
            );
          })}
          <line x1={L} x2={W - R} y1={y(0)} y2={y(0)} stroke="var(--ink-3)" strokeWidth="1" />
          <text x={L} y={8} fontSize="9.5" fill="var(--ink-3)">{unit}</text>
        </svg>

        <details className="mt-2">
          <summary className="text-xs font-semibold cursor-pointer" style={{ color: 'var(--brand-text)' }}>View the same data as a table</summary>
          <div className="tbl-wrap mt-2">
            <table className="tbl">
              <caption className="text-xs faint text-left px-2 py-1.5">{title}. {DATA_LABEL}.</caption>
              <thead>
                <tr><th scope="col">Plant</th>{years.map((yr) => <th scope="col" key={yr}>{yr}</th>)}</tr>
              </thead>
              <tbody>
                {series.map((s) => (
                  <tr key={s.name}>
                    <th scope="row">{s.name}</th>
                    {s.values.map((v, i) => <td key={i}>{fmt(v)}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </details>
      </figure>

      <RevealQuestions items={barQuestions()} />
    </div>
  );
}
