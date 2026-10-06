'use client';
import Link from 'next/link';
import { store, useStore } from '@/lib/store';
import { Md } from './Md';

export type GridTopic = {
  id: string; title: string; summary: string; importance?: string;
  avgQ1?: number; avgQ2?: number; nSub: number; nFormulas: number; nTricks: number;
  nPractice: number; difficulty: { easy: number; medium: number; hard: number };
};

const IMP_CHIP: Record<string, string> = { high: 'chip-high', medium: 'chip-medium', low: 'chip-low' };
const DIFF_COLORS: Record<string, string> = { easy: 'var(--ok)', medium: 'var(--warn)', hard: 'var(--bad)' };

export function TopicGrid({ section, topics }: { section: string; topics: GridTopic[] }) {
  const studied = useStore(store.studied, {});
  const scores = useStore(store.topicScores, {});

  return (
    <div className="grid sm:grid-cols-2 gap-3 mt-4">
      {topics.map((t, i) => {
        const key = `${section}/${t.id}`;
        const isStudied = !!studied[key];
        const s = scores[key];
        const pct = s ? Math.round((s.last / Math.max(1, s.total)) * 100) : null;
        const total = t.difficulty.easy + t.difficulty.medium + t.difficulty.hard;
        return (
          <Link key={t.id} href={`/${section}/${t.id}/`} className="card p-4 hover:-translate-y-0.5 transition-transform flex flex-col">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-xs faint font-bold">#{i + 1}</span>
              <span className="font-bold">{t.title}</span>
              {isStudied && <span className="chip chip-low text-xs">✓ studied</span>}
              {pct !== null && (
                <span className="chip text-xs" style={{
                  background: pct >= 80 ? 'var(--ok-soft)' : pct >= 50 ? 'var(--warn-soft)' : 'var(--bad-soft)',
                  color: pct >= 80 ? 'var(--ok)' : pct >= 50 ? 'var(--warn)' : 'var(--bad)', borderColor: 'transparent',
                }}>{pct}%</span>
              )}
              {t.importance && <span className={`chip ml-auto ${IMP_CHIP[t.importance]}`}>{t.importance}</span>}
            </div>
            <Md inline className="text-sm muted mt-1.5 line-clamp-2 flex-1">{t.summary}</Md>
            {total > 0 && (
              <div className="flex h-1.5 rounded-full overflow-hidden mt-2.5" style={{ background: 'var(--surface-2)' }}>
                <div style={{ width: `${(t.difficulty.easy / total) * 100}%`, background: DIFF_COLORS.easy }} />
                <div style={{ width: `${(t.difficulty.medium / total) * 100}%`, background: DIFF_COLORS.medium }} />
                <div style={{ width: `${(t.difficulty.hard / total) * 100}%`, background: DIFF_COLORS.hard }} />
              </div>
            )}
            <div className="text-xs faint mt-2 flex gap-3 flex-wrap">
              <span>{t.nSub} subtopics</span>
              {t.nFormulas > 0 && <span>{t.nFormulas} formulas</span>}
              {t.nTricks > 0 && <span>⚡{t.nTricks}</span>}
              {t.avgQ1 ? <span>~{t.avgQ1} Q/T1</span> : null}
              {t.nPractice > 0 && <span>{t.nPractice}-Q test</span>}
            </div>
          </Link>
        );
      })}
    </div>
  );
}
