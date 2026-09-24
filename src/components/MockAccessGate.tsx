'use client';
import { usePathname } from 'next/navigation';
import { LoginPrompt, useAuth } from './Auth';

/** Open mocks run for everyone (and stay crawlable); the rest ask for a free login so scores can be tracked. */
export function MockAccessGate({ open, title, children }: { open?: boolean; title: string; children: React.ReactNode }) {
  const { user, loading, configured } = useAuth();
  const path = usePathname() || '/';
  if (configured && !open) {
    if (loading) return <div className="card p-8 text-center muted">Checking your account…</div>;
    if (!user) return <LoginPrompt what={`attempt “${title}” — it's free`} next={path} />;
  }
  return <>{children}</>;
}
