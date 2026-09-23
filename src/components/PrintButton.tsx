'use client';
export function PrintButton() {
  return <button className="btn btn-brand" onClick={() => window.print()}>🖨 Print / save PDF</button>;
}
