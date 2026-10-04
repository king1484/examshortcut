import { PIE, DATA_LABEL, pieQuestions, fmt } from './data';
import { RevealQuestions } from './RevealQuestions';

/* Pie chart with sector angles in degrees, inline SVG, theme colours via CSS variables. */
export function PieGraph() {
  const { title, income, slices } = PIE;
  const S = 240, cx = S / 2, cy = S / 2, r = 100;
  const rad = (deg: number) => ((deg - 90) * Math.PI) / 180; // start at 12 o'clock
  const pt = (deg: number, rr: number) => [cx + rr * Math.cos(rad(deg)), cy + rr * Math.sin(rad(deg))] as const;

  let acc = 0;
  const wedges = slices.map((s) => {
    const a0 = acc;
    acc += s.deg;
    const a1 = acc;
    const [x0, y0] = pt(a0, r);
    const [x1, y1] = pt(a1, r);
    const large = s.deg > 180 ? 1 : 0;
    const d = `M${cx},${cy} L${x0.toFixed(2)},${y0.toFixed(2)} A${r},${r} 0 ${large} 1 ${x1.toFixed(2)},${y1.toFixed(2)} Z`;
    const [lx, ly] = pt((a0 + a1) / 2, r * 0.66);
    return { ...s, d, lx, ly };
  });

  const id = 'di-pie';
  return (
    <div className="card p-4 sm:p-5">
      <div className="flex items-start justify-between gap-2 flex-wrap">
        <h3 className="font-extrabold text-lg">3. Pie chart</h3>
        <span className="chip">{DATA_LABEL}</span>
      </div>

      <figure className="mt-2" style={{ margin: 0 }}>
        <figcaption id={`${id}-cap`} className="text-sm font-semibold mt-2">
          {title} (total monthly income ₹{fmt(income)}; sector angles in degrees)
        </figcaption>
        <div className="grid sm:grid-cols-[minmax(0,260px)_1fr] gap-3 items-center mt-2">
          <svg viewBox={`0 0 ${S} ${S}`} className="w-full mx-auto" style={{ height: 'auto', display: 'block', maxWidth: 260 }} role="img" aria-labelledby={`${id}-cap ${id}-desc`}>
            <desc id={`${id}-desc`}>
              Pie chart with {slices.length} sectors: {slices.map((s) => `${s.name} ${s.deg} degrees`).join(', ')}. The full values are in the data table below.
            </desc>
            {wedges.map((w) => (
              <path key={w.name} d={w.d} fill={w.color} stroke="var(--surface)" strokeWidth="2" strokeLinejoin="round" />
            ))}
            {wedges.map((w) => (
              <text key={w.name} x={w.lx} y={w.ly + 4} fontSize="12" fontWeight="800" fill="#fff" textAnchor="middle" stroke="rgba(0,0,0,.45)" strokeWidth="2.5" paintOrder="stroke">
                {w.deg}°
              </text>
            ))}
          </svg>
          <ul className="text-sm space-y-1.5 list-none p-0 m-0">
            {slices.map((s) => (
              <li key={s.name} className="flex items-center gap-2">
                <span aria-hidden="true" style={{ width: 12, height: 12, borderRadius: 3, background: s.color, display: 'inline-block', flexShrink: 0 }} />
                <span className="font-semibold">{s.name}</span>
                <span className="muted">{s.deg}°</span>
              </li>
            ))}
          </ul>
        </div>

        <details className="mt-3">
          <summary className="text-xs font-semibold cursor-pointer" style={{ color: 'var(--brand-text)' }}>View the same data as a table</summary>
          <div className="tbl-wrap mt-2">
            <table className="tbl">
              <caption className="text-xs faint text-left px-2 py-1.5">{title}. {DATA_LABEL}.</caption>
              <thead>
                <tr><th scope="col">Item</th><th scope="col">Angle</th><th scope="col">Percent</th><th scope="col">Amount</th></tr>
              </thead>
              <tbody>
                {slices.map((s) => (
                  <tr key={s.name}>
                    <th scope="row">{s.name}</th>
                    <td>{s.deg}°</td>
                    <td>{fmt(s.deg / 3.6)}%</td>
                    <td>₹{fmt((s.deg / 360) * income)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </details>
      </figure>

      <RevealQuestions items={pieQuestions()} />
    </div>
  );
}
