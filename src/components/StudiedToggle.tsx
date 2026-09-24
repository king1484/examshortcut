'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { store, useStore } from '@/lib/store';
import { useAuth } from './Auth';

export function StudiedToggle({ storeKey }: { storeKey: string }) {
  const studied = useStore(store.studied, {});
  const { user, configured } = useAuth();
  const path = usePathname() || '/';
  const done = !!studied[storeKey];
  if (configured && !user) {
    return (
      <Link href={`/login/?next=${encodeURIComponent(path)}`} className="btn shrink-0 mt-1" style={{ padding: '.35rem .7rem', fontSize: '.8rem' }} title="Tracking what you've studied needs a free account — notes stay open to everyone">
        🔒 Log in to track
      </Link>
    );
  }
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
