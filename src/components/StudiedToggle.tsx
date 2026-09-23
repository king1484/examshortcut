'use client';
import { store, useStore } from '@/lib/store';

export function StudiedToggle({ storeKey }: { storeKey: string }) {
  const studied = useStore(store.studied, {});
  const done = !!studied[storeKey];
  return (
    <button
      className="btn shrink-0 mt-1"
      style={{ padding: '.35rem .7rem', fontSize: '.8rem', background: done ? 'var(--ok-soft)' : undefined, color: done ? 'var(--ok)' : undefined, borderColor: done ? 'var(--ok)' : undefined }}
      onClick={() => store.toggleStudied(storeKey)}
      aria-pressed={done}
    >
      {done ? '✓ Studied' : 'Mark studied'}
    </button>
  );
}
