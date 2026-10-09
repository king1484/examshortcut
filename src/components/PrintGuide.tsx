'use client';
export function PrintGuide() {
  return <button className="btn" type="button" onClick={() => window.print()}>Print or save this guide</button>;
}
