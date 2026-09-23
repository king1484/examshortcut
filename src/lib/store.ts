'use client';
import type { Question } from './types';

// Per-device progress. localStorage can be unavailable (private mode) — every access is guarded.
function read<T>(key: string, fallback: T): T {
  try { const v = localStorage.getItem(key); return v ? (JSON.parse(v) as T) : fallback; } catch { return fallback; }
}
function write(key: string, value: unknown) {
  try { localStorage.setItem(key, JSON.stringify(value)); window.dispatchEvent(new Event('es-store')); } catch {}
}

export interface SavedQ { key: string; question: Question; chosen: number | null; from: string; href: string; section: string; at: number }

export interface MockAttempt {
  at: number; score: number; max: number; correct: number; wrong: number; skipped: number; timeSec: number;
  sections: Record<string, { score: number; max: number; correct: number; wrong: number; total: number }>;
}

export const store = {
  mistakes: () => read<Record<string, SavedQ>>('es-mistakes', {}),
  addMistake(s: SavedQ) { const m = store.mistakes(); m[s.key] = s; write('es-mistakes', m); },
  removeMistake(key: string) { const m = store.mistakes(); delete m[key]; write('es-mistakes', m); },

  bookmarks: () => read<Record<string, SavedQ>>('es-bookmarks', {}),
  toggleBookmark(s: SavedQ) { const b = store.bookmarks(); if (b[s.key]) delete b[s.key]; else b[s.key] = s; write('es-bookmarks', b); return !!b[s.key]; },
  removeBookmark(key: string) { const b = store.bookmarks(); delete b[key]; write('es-bookmarks', b); },

  topicScores: () => read<Record<string, { best: number; last: number; total: number; at: number }>>('es-topic-scores', {}),
  saveTopicScore(key: string, score: number, total: number) {
    const all = store.topicScores(); const prev = all[key];
    all[key] = { best: Math.max(prev?.best ?? 0, score), last: score, total, at: Date.now() };
    write('es-topic-scores', all);
  },

  studied: () => read<Record<string, number>>('es-studied', {}),
  toggleStudied(key: string) { const s = store.studied(); if (s[key]) delete s[key]; else s[key] = Date.now(); write('es-studied', s); return !!s[key]; },

  attempts: () => read<Record<string, MockAttempt[]>>('es-attempts', {}),
  saveAttempt(mockId: string, a: MockAttempt) { const all = store.attempts(); (all[mockId] ??= []).push(a); write('es-attempts', all); },

  // In-progress CBT state so a refresh doesn't lose the attempt
  draft: <T,>(mockId: string) => read<T | null>(`es-draft-${mockId}`, null),
  saveDraft(mockId: string, d: unknown) { try { localStorage.setItem(`es-draft-${mockId}`, JSON.stringify(d)); } catch {} },
  clearDraft(mockId: string) { try { localStorage.removeItem(`es-draft-${mockId}`); } catch {} },
};

import { useEffect, useState } from 'react';
/** Re-reads a store selector whenever any store write happens (this tab or another). */
export function useStore<T>(select: () => T, fallback: T): T {
  const [v, setV] = useState<T>(fallback);
  useEffect(() => {
    const update = () => setV(select());
    update();
    window.addEventListener('es-store', update);
    window.addEventListener('storage', update);
    return () => { window.removeEventListener('es-store', update); window.removeEventListener('storage', update); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return v;
}
