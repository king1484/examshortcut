'use client';
import { Spinner } from './Spinner';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { createContext, useContext, useEffect, useState } from 'react';
import { onAuthStateChanged, signOut as fbSignOut, type User } from 'firebase/auth';
import { auth, authConfigured } from '@/lib/firebase';
import { pullAndMerge, resetSyncState, startAutoPush } from '@/lib/sync';
import { startLeaderboardPublish } from '@/lib/leaderboard';
import { setTracking } from '@/lib/store';

interface AuthState { user: User | null; loading: boolean; configured: boolean; signOut: () => Promise<void> }

const AuthCtx = createContext<AuthState>({ user: null, loading: false, configured: false, signOut: async () => {} });
export const useAuth = () => useContext(AuthCtx);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(authConfigured);

  useEffect(() => {
    if (!auth) return;
    let stopPush: (() => void) | undefined;
    let stopLb: (() => void) | undefined;
    let syncedFor: string | null = null;
    let active = true;
    const unsub = onAuthStateChanged(auth, (u) => {
      setUser(u);
      setLoading(false);
      if (u && syncedFor !== u.uid) {
        syncedFor = u.uid;
        stopPush?.(); stopLb?.();
        void pullAndMerge(u.uid).then(() => {
          if (!active || syncedFor !== u.uid) return;
          stopPush = startAutoPush(u.uid); stopLb = startLeaderboardPublish(u.uid);
        }).catch(() => {
          // A database outage must not reject login or start sync for a previous account.
          console.warn('[sync] Account signed in; cloud progress could not be loaded.');
        });
      }
      if (!u) { syncedFor = null; stopPush?.(); stopPush = undefined; stopLb?.(); stopLb = undefined; resetSyncState(); }
    }, () => { setLoading(false); });
    return () => { active = false; syncedFor = null; unsub(); stopPush?.(); stopLb?.(); };
  }, []);

  // Track progress only once logged in (or when accounts aren't configured, i.e. preview mode).
  setTracking(!authConfigured || !!user);

  const signOut = async () => { if (auth) await fbSignOut(auth); };

  return <AuthCtx.Provider value={{ user, loading, configured: authConfigured, signOut }}>{children}</AuthCtx.Provider>;
}

/** Wraps personal/tracking screens. Public content never goes through this. */
export function AuthGate({ children, what = 'track your progress' }: { children: React.ReactNode; what?: string }) {
  const { user, loading, configured } = useAuth();
  const path = usePathname() || '/';
  if (!configured) {
    return (
      <>
        <p className="card p-3 text-xs muted mb-4">
          Preview mode: accounts are not switched on yet, so your progress is saved in this browser only.
        </p>
        {children}
      </>
    );
  }
  if (loading) return <div className="card"><Spinner label="Checking your account" /></div>;
  if (!user) return <LoginPrompt what={what} next={path} />;
  return <>{children}</>;
}

export function LoginPrompt({ what, next }: { what: string; next: string }) {
  return (
    <div className="card p-6 sm:p-8 text-center max-w-xl mx-auto">
      <p className="text-2xl">☁️</p>
      <h2 className="text-xl font-extrabold mt-1">Log in to {what}</h2>
      <p className="muted text-sm mt-2">
        Saves your progress and syncs it across devices.
      </p>
      <Link href={`/login/?next=${encodeURIComponent(next)}`} className="btn btn-brand mt-4 inline-flex">Log in / Sign up</Link>
    </div>
  );
}

/** Header control: avatar + menu when logged in, "Log in" otherwise. */
export function AccountButton() {
  const { user, configured, signOut } = useAuth();
  const [open, setOpen] = useState(false);
  if (!configured || !user) {
    return <Link href="/login/" className="btn icon-btn">Log in</Link>;
  }
  const name = user.displayName || user.email || 'Account';
  const initial = name.trim()[0]?.toUpperCase() ?? 'U';
  return (
    <div className="relative">
      <button onClick={() => setOpen((o) => !o)} aria-label="Account menu" aria-expanded={open}
        className="w-9 h-9 rounded-full font-extrabold text-sm" style={{ background: 'var(--brand)', color: 'var(--brand-ink)' }}>
        {initial}
      </button>
      {open && (
        <div className="card absolute right-0 mt-2 p-2 w-56 text-sm z-40" onClick={() => setOpen(false)}>
          <p className="px-2 py-1 faint text-xs truncate">{user.email}</p>
          <Link href="/dashboard/" className="block px-2 py-1.5 rounded hover:underline">My dashboard</Link>
          <Link href="/revision/" className="block px-2 py-1.5 rounded hover:underline">My revision</Link>
          <button onClick={() => void signOut()} className="block w-full text-left px-2 py-1.5 rounded hover:underline">Log out</button>
        </div>
      )}
    </div>
  );
}
