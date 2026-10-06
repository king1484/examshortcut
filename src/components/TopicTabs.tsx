'use client';
import { useEffect, useRef } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

export function TopicTabs({ base, nLearn, nFormulas, nExamples, nPractice }: {
  base: string; nLearn: number; nFormulas: number; nExamples: number; nPractice: number;
}) {
  const raw = usePathname() || '';
  const path = raw.endsWith('/') ? raw : `${raw}/`;
  const strip = useRef<HTMLDivElement>(null);
  const tabs = [
    { seg: '', label: 'Overview' },
    { seg: 'learn/', label: `Learn (${nLearn})` },
    { seg: 'formulas/', label: `Formulas (${nFormulas})` },
    { seg: 'examples/', label: `Examples (${nExamples})` },
    { seg: 'practice/', label: `Practice (${nPractice})` },
  ];

  // On a narrow screen the strip scrolls sideways: bring the current tab into view.
  useEffect(() => {
    const el = strip.current?.querySelector<HTMLElement>('[aria-current="page"]');
    const box = strip.current;
    if (!el || !box) return;
    box.scrollLeft = Math.max(0, el.offsetLeft - (box.clientWidth - el.offsetWidth) / 2);
  }, [path]);

  return (
    <div ref={strip} className="flex gap-1 mt-5 overflow-x-auto" style={{ borderBottom: '1px solid var(--line)', scrollbarWidth: 'none' }}>
      {tabs.map((t) => {
        const href = `${base}/${t.seg}`;
        const active = t.seg === '' ? path === `${base}/` : path.startsWith(href);
        return (
          <Link key={t.seg} href={href} aria-current={active ? 'page' : undefined}
            className="px-3.5 py-2 text-sm font-bold whitespace-nowrap transition-colors"
            style={{
              // inset shadow, not a negative-margin border, so the scroll container can't clip the underline
              boxShadow: active ? 'inset 0 -3px 0 var(--brand)' : 'none',
              color: active ? 'var(--ink)' : 'var(--ink-2)',
            }}>
            {t.label}
          </Link>
        );
      })}
    </div>
  );
}
