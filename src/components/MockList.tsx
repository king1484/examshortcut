'use client';
import Link from 'next/link';
import { store, useStore } from '@/lib/store';

interface Row { id: string; title: string; blurb: string; available: boolean; questionCount: number; durationMin: number; tier: 1 | 2 }

export function MockList({ mocks, examId = 'ssc-cgl', showTier = true }: { mocks: Row[]; examId?: string; showTier?: boolean }) {
  const attempts = useStore(store.attempts, {});

  return (
    <div className="space-y-4 mt-6">
      {mocks.map((m) => {
        const hist = attempts[m.id] ?? [];
        const best = hist.length ? Math.max(...hist.map((h) => h.score)) : null;
        return (
          <div key={m.id} className="card p-5 flex flex-col sm:flex-row sm:items-center gap-4">
            <div className="flex-1">
              <div className="flex items-center gap-2 flex-wrap">
                <h2 className="font-extrabold text-lg">{m.title}</h2>
                <span className={`chip ${m.available ? 'chip-low' : 'chip-medium'}`}>{m.available ? 'Ready' : 'Coming up'}</span>
                {showTier && <span className="chip">Tier {m.tier}</span>}
                <span className="chip">Free</span>
              </div>
              <p className="text-sm muted mt-1.5">{m.blurb}</p>
              <p className="text-xs faint mt-2">
                {m.available ? `${m.questionCount} questions · ${m.durationMin} min` : 'Paper is being set'}
                {best !== null && <> · your best: <b>{Number.isInteger(best) ? best : best.toFixed(2)}</b> across {hist.length} attempt{hist.length > 1 ? 's' : ''}</>}
              </p>
            </div>
            <div className="flex gap-2 shrink-0">
              <Link href={`/exams/${examId}/mocks/${m.id}/`} className={`btn ${m.available ? 'btn-brand' : ''}`}>{m.available ? (hist.length ? 'Retake' : 'Start test') : 'Preview'}</Link>
            </div>
          </div>
        );
      })}
    </div>
  );
}
