'use client';
export function PrintButton() {
  return <button className="btn btn-brand" onClick={() => window.print()}>⬇ Download PDF</button>;
}
