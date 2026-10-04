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
      <Link
        href={`/login/?next=${encodeURIComponent(path)}`}
        className="shrink-0 mt-1 inline-flex items-center gap-1 rounded-full font-bold whitespace-nowrap"
        style={{ padding: '.3rem .75rem', fontSize: '.78rem', color: '#fff', background: 'linear-gradient(135deg,#f97316,#ec4899 55%,#8b5cf6)', boxShadow: '0 2px 10px rgba(236,72,153,.35)' }}
        title="Log in to track your progress across devices"
      >
        ✨ Login to track
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
