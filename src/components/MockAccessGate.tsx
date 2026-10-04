'use client';

/** Every mock is open to everyone, no account needed. Scores are saved on the device; logging in only adds sync. */
export function MockAccessGate({ children }: { open?: boolean; title?: string; children: React.ReactNode }) {
  return <>{children}</>;
}
