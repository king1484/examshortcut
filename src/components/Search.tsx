'use client';
import { useEffect, useMemo, useRef, useState } from 'react';
import Link from 'next/link';
import { SECTION_META, type SectionId } from '@/lib/sections';

type Doc = { t: string; title: string; url: string; text: string; section?: string };
const TYPE_META: Record<string, { icon: string; label: string }> = {
  topic: { icon: '📘', label: 'Topic' },
  formula: { icon: '⚡', label: 'Formula' },
  trick: { icon: '🧠', label: 'Shortcut trick' },
  mistake: { icon: '⚠️', label: 'Common mistake' },
  mock: { icon: '🖥️', label: 'Mock test' },
  page: { icon: '📄', label: 'Page' },
};

function score(doc: Doc, q: string): number {
  const t = doc.title.toLowerCase();
  if (t === q) return 6;
  if (t.startsWith(q)) return 5;
  if (new RegExp(`\\b${q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`).test(t)) return 4;
  if (t.includes(q)) return 3;
  const txt = doc.text.toLowerCase();
  if (txt.includes(q)) return 1;
  return 0;
}

function Highlight({ text, q }: { text: string; q: string }) {
  const i = q ? text.toLowerCase().indexOf(q) : -1;
  if (i < 0) return <>{text}</>;
  return (
    <>
      {text.slice(0, i)}
      <mark style={{ background: 'color-mix(in srgb, var(--brand) 22%, transparent)', borderRadius: 3 }}>
        {text.slice(i, i + q.length)}
      </mark>
      {text.slice(i + q.length)}
    </>
  );
}

let cache: Doc[] | null = null;

export function Search() {
  const [q, setQ] = useState('');
  const [section, setSection] = useState<'all' | SectionId>('all');
  const [docs, setDocs] = useState<Doc[] | null>(cache);
  const [sel, setSel] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
    const initial = new URLSearchParams(window.location.search).get('q');
    if (initial) setQ(initial);
    if (cache) return;
    fetch('/search-index.json')
      .then((r) => r.json())
      .then((d: Doc[]) => { cache = d; setDocs(d); })
      .catch(() => setDocs([]));
  }, []);

  const results = useMemo(() => {
    if (!docs || q.trim().length < 2) return [];
    const query = q.trim().toLowerCase();
    return docs
      .map((d) => ({ d, s: score(d, query) }))
      .filter(({ s }) => s > 0)
      .sort((a, b) => b.s - a.s || a.d.title.localeCompare(b.d.title))
      .map(({ d }) => d);
  }, [docs, q]);

  const filtered = useMemo(
    () => (section === 'all' ? results : results.filter((d) => d.section === section || d.t === 'page' || d.t === 'mock')),
    [results, section]
  );
  const shown = filtered.slice(0, 30);

  useEffect(() => setSel(0), [q, section]);

  const onKey = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); setSel((s) => Math.min(s + 1, shown.length - 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setSel((s) => Math.max(s - 1, 0)); }
    else if (e.key === 'Enter' && shown[sel]) window.location.href = shown[sel].url;
  };
  useEffect(() => {
    listRef.current?.querySelector('[data-sel="1"]')?.scrollIntoView({ block: 'nearest' });
  }, [sel]);

  const sections: Array<'all' | SectionId> = ['all', 'quant', 'reasoning', 'english', 'ga', 'computer'];

  return (
    <div>
      <div className="sticky top-14 z-10 py-3" style={{ background: 'var(--bg)' }}>
        <input
          ref={inputRef}
          value={q}
          onChange={(e) => setQ(e.target.value)}
          onKeyDown={onKey}
          placeholder="Search topics, formulas, tricks, mocks…  (e.g. alligation, syllogism, cutoff)"
          className="w-full card px-4 py-3 text-base outline-none"
          style={{ borderWidth: 2, borderColor: q ? 'var(--brand)' : 'var(--line)' }}
          aria-label="Search ExamShortcut"
        />
        <div className="flex gap-1.5 mt-2 overflow-x-auto text-xs font-semibold" style={{ scrollbarWidth: 'none' }}>
          {sections.map((s) => (
            <button key={s} onClick={() => setSection(s)}
              className="chip whitespace-nowrap" style={section === s ? { background: 'var(--brand)', color: '#fff', borderColor: 'var(--brand)' } : undefined}>
              {s === 'all' ? 'All' : SECTION_META[s].short}
            </button>
          ))}
        </div>
      </div>

      {docs === null && <p className="muted mt-6 text-sm">Loading index…</p>}
      {docs !== null && q.trim().length >= 2 && shown.length === 0 && (
        <div className="card p-8 text-center mt-6">
          <p className="font-bold">No matches for “{q}”</p>
          <p className="muted text-sm mt-1">Try a shorter word — e.g. “pipe”, “si”, “venn”, “clock”.</p>
        </div>
      )}
      {q.trim().length < 2 && (
        <p className="muted text-sm mt-6">Type at least 2 letters. Every topic, formula, shortcut and common mistake across all sections is indexed.</p>
      )}

      <div ref={listRef} className="mt-3 space-y-1.5" role="listbox">
        {shown.map((d, i) => {
          const tm = TYPE_META[d.t] ?? TYPE_META.page;
          return (
            <Link key={`${d.t}-${d.title}-${i}`} href={d.url} data-sel={i === sel ? '1' : undefined}
              onMouseEnter={() => setSel(i)}
              className="card px-4 py-3 flex items-center gap-3 block"
              style={i === sel ? { borderColor: 'var(--brand)' } : undefined}>
              <span aria-hidden className="text-lg shrink-0">{tm.icon}</span>
              <span className="flex-1 min-w-0">
                <span className="font-semibold text-sm block truncate"><Highlight text={d.title} q={q.trim()} /></span>
                {d.section && <span className="text-xs faint">{SECTION_META[d.section as SectionId]?.name ?? d.section}</span>}
              </span>
              <span className="chip shrink-0 text-[10px]">{tm.label}</span>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
