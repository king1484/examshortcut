/** Loading indicator: a spinning ring (screen readers still get the label). `block` centres it in its card. */
export function Spinner({ label = 'Loading', block = true }: { label?: string; block?: boolean }) {
  const ring = <span className="spinner" role="status" aria-label={label} />;
  return block ? <div className="spinner-block">{ring}</div> : ring;
}
