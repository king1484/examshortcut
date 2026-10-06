'use client';
import {
  collection, deleteDoc, doc, getCountFromServer, getDoc, getDocs, limit, orderBy, query, serverTimestamp, setDoc, where,
} from 'firebase/firestore';
import { db } from './firebase';
import { computeStats, readActivity, type Stats } from './streak';

/* Opt-in public leaderboard. One doc per joined user at leaderboard/{uid}: display name + the same
   progress numbers the dashboard shows. Nothing is written until the user joins; leaving deletes it. */

/** Only points are public. Streak stays a private, personal motivator. */
export interface BoardRow { uid: string; name: string; points: number; studied: number; tests: number; mocks: number }

export const NAME_RE = /^[\p{L}\p{N}][\p{L}\p{N} ._-]{1,23}$/u;
export const cleanName = (s: string) => s.replace(/\s+/g, ' ').trim();

let active: { uid: string; name: string } | null = null;
let lastBody = '';

const ref = (uid: string) => doc(db!, 'leaderboard', uid);

function payload(name: string, s: Stats) {
  return { name, points: s.points, studied: s.studied, tests: s.tests, mocks: s.mocks, updatedAt: serverTimestamp() };
}

async function publish() {
  if (!db || !active) return;
  const s = computeStats(readActivity());
  const body = JSON.stringify([active.name, s.points, s.studied, s.tests, s.mocks]);
  if (body === lastBody) return;
  try { await setDoc(ref(active.uid), payload(active.name, s), { merge: true }); lastBody = body; }
  catch (e) { console.warn('[leaderboard] publish failed', e); }
}

export async function getMine(uid: string): Promise<BoardRow | null> {
  if (!db) return null;
  const snap = await getDoc(ref(uid));
  return snap.exists() ? ({ uid, ...(snap.data() as Omit<BoardRow, 'uid'>) }) : null;
}

export async function joinBoard(uid: string, name: string) {
  if (!db) throw new Error('Accounts are not switched on.');
  active = { uid, name };
  lastBody = '';
  await setDoc(ref(uid), payload(name, computeStats(readActivity())));
  { const s = computeStats(readActivity()); lastBody = JSON.stringify([name, s.points, s.studied, s.tests, s.mocks]); }
  window.dispatchEvent(new Event('es-lb'));
}

export async function leaveBoard(uid: string) {
  if (!db) return;
  await deleteDoc(ref(uid));
  active = null; lastBody = '';
  window.dispatchEvent(new Event('es-lb'));
}

export async function renameOnBoard(uid: string, name: string) {
  if (!db) return;
  await setDoc(ref(uid), { name, updatedAt: serverTimestamp() }, { merge: true });
  if (active) active.name = name;
  lastBody = '';
  void publish();
  window.dispatchEvent(new Event('es-lb'));
}

export async function fetchTop(n = 50): Promise<BoardRow[]> {
  if (!db) return [];
  const q = query(collection(db, 'leaderboard'), orderBy('points', 'desc'), limit(n));
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ uid: d.id, ...(d.data() as Omit<BoardRow, 'uid'>) }));
}

/** 1-based rank of a points total among everyone on the board (count of strictly better rows + 1). */
export async function rankOf(value: number): Promise<number | null> {
  if (!db) return null;
  try {
    const c = await getCountFromServer(query(collection(db, 'leaderboard'), where('points', '>', value)));
    return c.data().count + 1;
  } catch { return null; }
}

/** Keep a joined user's row fresh. Called once per login; returns an unsubscribe. */
export function startLeaderboardPublish(uid: string) {
  let t: ReturnType<typeof setTimeout> | undefined;
  let alive = true;
  const schedule = () => { clearTimeout(t); t = setTimeout(() => void publish(), 4000); };
  void getMine(uid).then((row) => {
    if (!alive || !row) return;
    active = { uid, name: row.name };
    void publish();
  }).catch(() => {});
  window.addEventListener('es-store', schedule);
  return () => { alive = false; clearTimeout(t); window.removeEventListener('es-store', schedule); active = null; lastBody = ''; };
}
