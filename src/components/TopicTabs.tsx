'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

export function TopicTabs({ base, nLearn, nFormulas, nExamples, nPractice }: {
  base: string; nLearn: number; nFormulas: number; nExamples: number; nPractice: number;
}) {
  const path = usePathname() || '';
  const tabs = [
    { seg: '', label: 'Overview' },
    { seg: 'learn/', label: `Learn (${nLearn})` },
    { seg: 'formulas/', label: `Formulas (${nFormulas})` },
    { seg: 'examples/', label: `Examples (${nExamples})` },
    { seg: 'practice/', label: `Practice (${nPractice})` },
  ];
  return (
    <div className="flex gap-1 mt-5 border-b overflow-x-auto" style={{ borderColor: 'var(--line)', scrollbarWidth: 'none' }}>
      {tabs.map((t) => {
        const href = `${base}/${t.seg}`;
        const active = t.seg === '' ? path === base || path === base.slice(0, -1) : path.startsWith(href);
        return (
          <Link key={t.seg} href={href} className="px-3.5 py-2 text-sm font-bold whitespace-nowrap border-b-2 -mb-px transition-colors"
            style={{ borderColor: active ? 'var(--brand)' : 'transparent', color: active ? 'var(--ink)' : 'var(--ink-2)' }}>
            {t.label}
          </Link>
        );
      })}
    </div>
  );
}

export function PrintButton({ label = '🖨️ Print / save PDF' }: { label?: string }) {
  return (
    <button className="btn text-sm" onClick={() => window.print()}>{label}</button>
  );
}
