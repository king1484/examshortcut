'use client';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';
import {
  isSignInWithEmailLink, sendSignInLinkToEmail, signInWithEmailLink, signInWithPopup,
} from 'firebase/auth';
import { auth, googleProvider } from '@/lib/firebase';
import { useAuth } from './Auth';

function nextPath() {
  try {
    const n = new URLSearchParams(location.search).get('next');
    return n && n.startsWith('/') && !n.startsWith('//') ? n : '/dashboard/';
  } catch { return '/dashboard/'; }
}

const EMAIL_KEY = 'es-email-for-login';

export function LoginForm() {
  const { user, configured, loading, signOut } = useAuth();
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [state, setState] = useState<'idle' | 'sending' | 'sent' | 'error'>('idle');
  const [err, setErr] = useState('');

  const finish = () => { try { localStorage.removeItem(EMAIL_KEY); } catch {} router.replace(nextPath()); };

  // Coming back from the email link: complete sign-in from the URL, then move on.
  useEffect(() => {
    if (!auth || !isSignInWithEmailLink(auth, window.location.href)) return;
    let saved: string | null = null;
    try { saved = localStorage.getItem(EMAIL_KEY); } catch {}
    if (saved) void signInWithEmailLink(auth, saved, window.location.href).then(finish).catch((e) => { setState('error'); setErr(String(e?.message ?? e)); });
  }, [ ]);

  // Coming back from Google (or any already-live session): go straight on.
  useEffect(() => { if (user) finish(); /* eslint-disable-next-line react-hooks/exhaustive-deps */ }, [user]);

  const redirectTo = () => `${location.origin}/login/?next=${encodeURIComponent(nextPath())}`;

  const google = async () => {
    if (!auth) return;
    try { await signInWithPopup(auth, googleProvider); } catch (e) { setState('error'); setErr(String((e as Error).message)); }
  };

  const magic = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!auth || !email) return;
    setState('sending');
    try {
      await sendSignInLinkToEmail(auth, email, { url: redirectTo(), handleCodeInApp: true });
      try { localStorage.setItem(EMAIL_KEY, email); } catch {}
      setState('sent');
    } catch (e2) { setState('error'); setErr(String((e2 as Error).message)); }
  };

  return (
    <div className="card p-6 sm:p-8">
      <h1 className="text-2xl font-extrabold">Log in to ExamShortcut</h1>
      <p className="muted text-sm mt-2">
        Log in to sync your scores and progress across devices.
        Log in only to <b>save and sync</b> your revision list, studied topics, daily-quiz streak and test scores.
      </p>

      {!configured ? (
        <p className="card p-3 mt-5 text-sm muted">
          Accounts are being switched on shortly. Until then, your progress is saved in this browser automatically.
        </p>
      ) : loading ? (
        <p className="mt-6 muted">Checking your session…</p>
      ) : user ? (
        <div className="mt-6 space-y-3">
          <p className="text-sm">Logged in as <b>{user.email}</b>. Taking you back…</p>
          <button className="btn" onClick={() => void signOut()}>Log out</button>
        </div>
      ) : (
        <div className="mt-6 space-y-4">
          <button onClick={google} className="btn w-full justify-center" style={{ padding: '.7rem 1rem' }}>
            <svg width="18" height="18" viewBox="0 0 48 48" aria-hidden className="mr-2">
              <path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/>
              <path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/>
              <path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/>
              <path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/>
            </svg>
            Continue with Google
          </button>
          <div className="flex items-center gap-3 text-xs faint"><span className="flex-1 border-t" style={{ borderColor: 'var(--line)' }} />or<span className="flex-1 border-t" style={{ borderColor: 'var(--line)' }} /></div>
          {state === 'sent' ? (
            <p className="card p-3 text-sm">Check <b>{email}</b> — we sent a one-tap login link. Open it in this browser.</p>
          ) : (
            <form onSubmit={magic} className="space-y-2">
              <label className="text-sm font-semibold block" htmlFor="email">Email me a login link</label>
              <input id="email" type="email" required value={email} onChange={(e) => setEmail(e.target.value)} placeholder="you@example.com"
                className="w-full rounded-lg border px-3 py-2 bg-transparent" style={{ borderColor: 'var(--line)' }} autoComplete="email" />
              <button type="submit" disabled={state === 'sending'} className="btn btn-brand w-full justify-center">
                {state === 'sending' ? 'Sending…' : 'Send login link'}
              </button>
            </form>
          )}
          {state === 'error' && <p className="text-sm" style={{ color: 'var(--bad, #d33)' }}>{err}</p>}
          <p className="text-xs faint">No password to remember. New here? The same buttons create your free account.</p>
        </div>
      )}
      <p className="text-xs faint mt-6">By continuing you agree to our <Link href="/privacy/" className="underline">privacy policy</Link>.</p>
    </div>
  );
}
