'use client';
import { useEffect, useState } from 'react';

type Mode = 'system' | 'light' | 'dark';
const NEXT: Record<Mode, Mode> = { system: 'light', light: 'dark', dark: 'system' };
const LABEL: Record<Mode, string> = { system: 'Auto', light: 'Light', dark: 'Dark' };

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
    <button className="btn" style={{ padding: '.4rem .7rem', fontSize: '.8rem' }} onClick={cycle} aria-label={`Theme: ${LABEL[mode]}. Click to change`}>
      {mode === 'dark' ? '☾' : mode === 'light' ? '☀' : '◐'}<span className="hidden min-[400px]:inline ml-1">{LABEL[mode]}</span>
    </button>
  );
}
