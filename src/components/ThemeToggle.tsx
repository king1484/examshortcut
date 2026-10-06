'use client';
import { useEffect, useState } from 'react';

type Mode = 'system' | 'light' | 'dark';
const NEXT: Record<Mode, Mode> = { system: 'light', light: 'dark', dark: 'system' };
const LABEL: Record<Mode, string> = { system: 'Auto', light: 'Light', dark: 'Dark' };

function Icon({ mode }: { mode: Mode }) {
  const p = { viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: 2, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const, 'aria-hidden': true };
  if (mode === 'dark') return <svg {...p}><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z" /></svg>;
  if (mode === 'light') {
    return (
      <svg {...p}>
        <circle cx="12" cy="12" r="4" />
        <path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" />
      </svg>
    );
  }
  return <svg {...p}><circle cx="12" cy="12" r="9" /><path d="M12 3v18a9 9 0 0 0 0-18z" fill="currentColor" /></svg>;
}

export function ThemeToggle() {
  const [mode, setMode] = useState<Mode>('system');
  useEffect(() => {
    try { const t = localStorage.getItem('es-theme'); if (t === 'light' || t === 'dark') setMode(t); } catch {}
  }, []);
  const cycle = () => {
    const m = NEXT[mode];
    setMode(m);
    const root = document.documentElement;
    if (m === 'system') delete root.dataset.theme; else root.dataset.theme = m;
    try { if (m === 'system') localStorage.removeItem('es-theme'); else localStorage.setItem('es-theme', m); } catch {}
  };
  return (
    <button className="btn icon-btn" style={{ fontSize: '.8rem' }} onClick={cycle} aria-label={`Theme: ${LABEL[mode]}. Click to change`}>
      <Icon mode={mode} /><span className="hidden min-[400px]:inline">{LABEL[mode]}</span>
    </button>
  );
}
