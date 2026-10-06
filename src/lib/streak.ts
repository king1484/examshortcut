'use client';
import { useMemo } from 'react';
import { store, useStore, type MockAttempt, type SavedQ } from './store';

/* Streak + points, derived purely from what the visitor already does (localStorage, synced to the
   cloud when logged in). A "day" is an IST calendar day, matching the daily-quiz rollover. */

export const DAY = 86400000;
export const istDay = (ts: number) => Math.floor((ts + 5.5 * 3600000) / DAY);

type Scores = Record<string, { best: number; last: number; total: number; at: number }>;
export interface Activity {
  studied: Record<string, number>;
  scores: Scores;
  attempts: Record<string, MockAttempt[]>;
  mistakes: Record<string, SavedQ>;
}

export interface StreakInfo {
  current: number;       // consecutive active days ending today (or yesterday, if today isn't done yet)
  longest: number;
  todayDone: boolean;
  activeDays: number;
  week: { day: number; done: boolean; label: string; today: boolean }[]; // last 7 days, oldest first
}

const WD = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'];

export function activeDaySet(a: Activity): Set<number> {
  const stamps: number[] = [
    ...Object.values(a.studied),
    ...Object.values(a.scores).map((s) => s.at),
    ...Object.values(a.attempts).flatMap((l) => l.map((x) => x.at)),
    ...Object.values(a.mistakes).map((m) => m.at),
  ];
  return new Set(stamps.filter((t) => Number.isFinite(t)).map(istDay));
}

export function computeStreak(days: Set<number>, now = Date.now()): StreakInfo {
  const today = istDay(now);
  const todayDone = days.has(today);
  let current = 0;
  for (let d = todayDone ? today : today - 1; days.has(d); d--) current++;

  let longest = 0, run = 0, prev = NaN;
  for (const d of [...days].sort((x, y) => x - y)) {
    run = d === prev + 1 ? run + 1 : 1;
    longest = Math.max(longest, run);
    prev = d;
  }

  const week = Array.from({ length: 7 }, (_, i) => {
    const day = today - 6 + i;
    return { day, done: days.has(day), today: day === today, label: WD[new Date(day * DAY).getUTCDay()] };
  });
  return { current, longest: Math.max(longest, current), todayDone, activeDays: days.size, week };
}

export interface Stats { points: number; streak: number; longest: number; studied: number; tests: number; mocks: number }

/** Points: 10 per studied topic, up to 30 per topic/daily test (best score), 25 + best-score% per mock paper. Streak is not scored. */
export function computeStats(a: Activity, now = Date.now()): Stats {
  const sk = computeStreak(activeDaySet(a), now);
  const studied = Object.keys(a.studied).length;
  const tests = Object.keys(a.scores).length;
  const testPts = Object.values(a.scores).reduce((n, s) => n + Math.round((Math.min(s.best, s.total) / Math.max(1, s.total)) * 30), 0);
  const mockIds = Object.keys(a.attempts).filter((id) => a.attempts[id]?.length);
  const mockPts = mockIds.reduce((n, id) => n + 25 + Math.max(0, ...a.attempts[id].map((m) => (m.max > 0 ? Math.max(0, m.score) / m.max : 0))) * 100, 0);
  const points = Math.round(studied * 10 + testPts + mockPts);
  return { points, streak: sk.current, longest: sk.longest, studied, tests, mocks: mockIds.length };
}

export function readActivity(): Activity {
  return { studied: store.studied(), scores: store.topicScores(), attempts: store.attempts(), mistakes: store.mistakes() };
}

/** Live streak + points for the current visitor (re-computes on every store write). */
export function useProgress() {
  const studied = useStore(store.studied, {} as Activity['studied']);
  const scores = useStore(store.topicScores, {} as Scores);
  const attempts = useStore(store.attempts, {} as Activity['attempts']);
  const mistakes = useStore(store.mistakes, {} as Activity['mistakes']);
  return useMemo(() => {
    const a = { studied, scores, attempts, mistakes };
    return { streak: computeStreak(activeDaySet(a)), stats: computeStats(a) };
  }, [studied, scores, attempts, mistakes]);
}
