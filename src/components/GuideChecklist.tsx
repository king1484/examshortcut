'use client';
import { useEffect, useState } from 'react';

export function GuideChecklist({ guideKey, items }: { guideKey: string; items: string[] }) {
  const [done, setDone] = useState<string[]>([]);
  const [ready, setReady] = useState(false);
  const [saved, setSaved] = useState(true);
  const storageKey = `examshortcut:guide:${guideKey}`;
  useEffect(() => {
    try {
      const stored: unknown = JSON.parse(localStorage.getItem(storageKey) ?? '[]');
      if (Array.isArray(stored)) setDone(stored.filter((value): value is string => typeof value === 'string' && items.includes(value)));
    } catch { setSaved(false); }
    setReady(true);
  }, [storageKey, items]);
  function change(next: string[]) {
    setDone(next);
    try { localStorage.setItem(storageKey, JSON.stringify(next)); setSaved(true); } catch { setSaved(false); }
  }
  return <section className="card p-5 mt-8" aria-label="My action checklist">
    <h2 className="text-xl font-bold">Make this your next step</h2>
    <p className="text-sm muted mt-2" role="status">{done.length} of {items.length} complete. {saved ? 'Saved on this browser only.' : 'Storage is unavailable; checks last for this visit.'}</p>
    <ul className="mt-3 space-y-1">{items.map(item => <li key={item}>
      <label className="flex items-start gap-3 min-h-11 py-2 cursor-pointer">
        <input type="checkbox" className="mt-1 size-5 shrink-0 accent-blue-700" checked={done.includes(item)} disabled={!ready} onChange={event => change(event.target.checked ? [...done, item] : done.filter(value => value !== item))} />
        <span>{item}</span>
      </label>
    </li>)}</ul>
    <button className="btn mt-3" disabled={!ready || !done.length} onClick={() => change([])}>Clear my checks</button>
  </section>;
}
