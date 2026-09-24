'use client';
import { useMemo, useState, type ReactNode } from 'react';
import { STATIC_GK } from '@/data/staticGk';

const escapeRe = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function Hl({ text, q }: { text: string; q: string }): ReactNode {
  if (!q) return text;
  const parts = text.split(new RegExp(`(${escapeRe(q)})`, 'ig'));
  if (parts.length === 1) return text;
  return parts.map((p, i) =>
    i % 2 === 1
      ? <mark key={i} style={{ background: 'var(--warn-soft)', color: 'inherit', borderRadius: 3, padding: '0 1px' }}>{p}</mark>
      : p);
}

const TOTAL_ROWS = STATIC_GK.reduce((n, t) => n + t.rows.length, 0);

export function StaticGk() {
  const [query, setQuery] = useState('');
  const q = query.trim().toLowerCase();

  const tables = useMemo(
    () =>
      STATIC_GK.map((t) => ({
        ...t,
        // A search that matches the table title keeps the whole table.
        rows: !q || t.title.toLowerCase().includes(q)
          ? t.rows
          : t.rows.filter((r) => r.some((c) => c.toLowerCase().includes(q))),
      })),
    [q],
  );
  const matchRows = tables.reduce((n, t) => n + t.rows.length, 0);
  const shown = tables.filter((t) => t.rows.length > 0);

  return (
    <div className="mt-6">
      <div className="sticky top-14 z-20 -mx-4 px-4 sm:-mx-6 sm:px-6 py-2.5 border-b backdrop-blur"
        style={{ background: 'color-mix(in srgb, var(--bg) 90%, transparent)', borderColor: 'var(--line)' }}>
        <input type="search" value={query} onChange={(e) => setQuery(e.target.value)}
          placeholder="Search any state, park, river, day, author…" aria-label="Search static GK"
          className="w-full p-2 rounded-lg border text-base"
          style={{ borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' }} />
        <nav className="flex gap-2 overflow-x-auto pb-1 mt-2" aria-label="Jump to table">
          {tables.map((t) => {
            const off = q && t.rows.length === 0;
            return (
              <a key={t.id} href={`#${t.id}`} className="chip shrink-0 whitespace-nowrap px-3 py-1.5 text-sm no-underline"
                style={off ? { opacity: 0.4 } : {}} aria-disabled={off || undefined}>
                {t.title.replace(/^Important days — /, 'Days: ').replace(/^Sports: /, '')}
                {q && <span className="opacity-70">{t.rows.length}</span>}
              </a>
            );
          })}
        </nav>
      </div>

      {q && (
        <p className="text-sm muted mt-4">
          {matchRows === 0
            ? <>Nothing matches “{query.trim()}”. Try a shorter word, e.g. a state name.</>
            : <><b>{matchRows}</b> matching rows in <b>{shown.length}</b> {shown.length === 1 ? 'table' : 'tables'}.</>}
        </p>
      )}

      {shown.map((t) => (
        <section key={t.id} id={t.id} className="mt-8 scroll-mt-44">
          <h2 className="text-2xl font-extrabold">
            {t.title} <span className="text-base font-bold faint">({t.rows.length})</span>
          </h2>
          {t.note && <p className="text-sm muted mt-1">{t.note}</p>}
          <div className="tbl-wrap mt-3">
            <table className="tbl text-sm">
              <thead>
                <tr>{t.columns.map((c) => <th key={c} className="whitespace-nowrap">{c}</th>)}</tr>
              </thead>
              <tbody>
                {t.rows.map((r, i) => (
                  <tr key={`${r[0]}-${i}`}>
                    {r.map((c, j) => (
                      <td key={j} className={j === 0 ? 'font-semibold min-w-[8rem]' : 'min-w-[7rem]'}>
                        <Hl text={c} q={q} />
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      ))}

      <p className="text-[11px] faint mt-8">
        {STATIC_GK.length} tables, {TOTAL_ROWS} rows. Static facts only — no office-holders or current affairs, so nothing here goes out of date between notifications. Where sources disagree we left the entry out rather than guess.
      </p>
    </div>
  );
}
