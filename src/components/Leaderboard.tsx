'use client';
import Link from 'next/link';
import { useCallback, useEffect, useState } from 'react';
import { useAuth } from './Auth';
import { Spinner } from './Spinner';
import { useProgress } from '@/lib/streak';
import {
  NAME_RE, cleanName, fetchTop, getMine, joinBoard, leaveBoard, rankOf, type BoardRow,
} from '@/lib/leaderboard';

const MEDAL = ['🥇', '🥈', '🥉'];
const MIN_ROWS = 10;
/** Placeholder rows that fill the board until it has MIN_ROWS real learners. Never stored in Firestore. */
const SAMPLES = [
  { name: 'Aarav', points: 1240 }, { name: 'Priya', points: 1105 }, { name: 'Rohan', points: 980 },
  { name: 'Sneha', points: 865 }, { name: 'Kiran', points: 740 }, { name: 'Ananya', points: 655 },
  { name: 'Vikram', points: 590 }, { name: 'Meera', points: 520 }, { name: 'Arjun', points: 455 },
  { name: 'Divya', points: 390 },
];

export function Leaderboard() {
  const { user, configured, loading } = useAuth();
  const { stats } = useProgress();
  const [rows, setRows] = useState<BoardRow[] | null>(null);
  const [failed, setFailed] = useState(false);
  const [mine, setMine] = useState<BoardRow | null | undefined>(undefined); // undefined = not loaded
  const [rank, setRank] = useState<number | null>(null);
  const [name, setName] = useState('');
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');

  const load = useCallback(async () => {
    setFailed(false);
    try { setRows(await fetchTop()); } catch { setRows([]); setFailed(true); }
  }, []);
  useEffect(() => { void load(); }, [load]);

  const loadMine = useCallback(async () => {
    if (!user) { setMine(null); return; }
    try { setMine(await getMine(user.uid)); } catch { setMine(null); }
  }, [user]);
  useEffect(() => { void loadMine(); }, [loadMine]);

  useEffect(() => {
    if (!mine) { setRank(null); return; }
    void rankOf(mine.points).then(setRank);
  }, [mine]);

  useEffect(() => {
    if (user && !name) setName(cleanName((user.displayName ?? '').split(' ')[0] ?? ''));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user]);

  const run = async (fn: () => Promise<void>) => {
    setBusy(true); setErr('');
    try { await fn(); await Promise.all([load(), loadMine()]); }
    catch { setErr('Could not save that. Check your connection and try again.'); }
    setBusy(false);
  };
  const nameOk = NAME_RE.test(cleanName(name));
  const join = () => user && nameOk && run(() => joinBoard(user.uid, cleanName(name)));

  const inTop = !!mine && !!rows?.some((r) => r.uid === mine.uid);

  return (
    <div>
      <h1 className="text-3xl font-extrabold">Leaderboard</h1>
      <p className="muted text-sm mt-1">Earn points by studying, testing and taking mocks.</p>

      {user && (
        <div className="card p-4 sm:p-5 mt-5">
          <div className="flex items-center justify-between flex-wrap gap-2">
            <div>
              <div className="text-xs faint">Your points</div>
              <div className="text-2xl font-extrabold leading-none">{stats.points.toLocaleString('en-IN')}</div>
            </div>
            <div className="text-xs faint flex gap-4 flex-wrap">
              <span>📚 {stats.studied} topics studied</span><span>📝 {stats.tests} tests</span><span>🖥️ {stats.mocks} mocks</span>
            </div>
          </div>
          <details className="mt-3 text-xs muted">
            <summary className="cursor-pointer font-semibold">How points work</summary>
            <ul className="list-disc pl-5 mt-2 space-y-0.5">
              <li>10 for every topic you mark studied</li>
              <li>Up to 30 per topic test or daily quiz, based on your best score</li>
              <li>25 per mock paper, plus your best score on it (out of 100)</li>
            </ul>
          </details>
        </div>
      )}

      {/* Join / manage */}
      <div className="card p-4 sm:p-5 mt-4">
        {!configured ? (
          <p className="text-sm muted">Accounts are not switched on in this build, so the leaderboard is unavailable.</p>
        ) : loading || (!!user && mine === undefined) ? (
          <Spinner label="Checking your account" />
        ) : !user ? (
          <div className="flex items-center justify-between gap-3 flex-wrap">
            <p className="text-sm muted flex-1 min-w-[220px]">Log in to earn points and join the board.</p>
            <Link href="/login/?next=%2Fleaderboard%2F" className="btn">Log in to join</Link>
          </div>
        ) : mine ? (
          <div className="flex items-center justify-between gap-3 flex-wrap">
            <div className="text-sm">
              You&apos;re on the board as <b>{mine.name}</b>{rank ? <> · rank <b>#{rank}</b></> : null}
            </div>
            <button className="btn" disabled={busy} style={{ padding: '.35rem .75rem', fontSize: '.8rem' }}
              onClick={() => void run(() => leaveBoard(user.uid))}>Leave board</button>
          </div>
        ) : (
          <div>
            <label className="text-sm font-bold" htmlFor="lb-name">Join the leaderboard</label>
            <p className="text-xs faint mt-1">Pick a display name. It is shown publicly with your points — never your email. You can leave any time and your entry is deleted.</p>
            <div className="flex gap-2 mt-3 flex-wrap">
              <input id="lb-name" value={name} onChange={(e) => setName(e.target.value)} maxLength={24} placeholder="Display name"
                className="rounded-lg px-3 py-2 text-sm flex-1 min-w-[180px]" style={{ border: '1px solid var(--line)', background: 'var(--surface)', color: 'var(--ink)' }} />
              <button className="btn btn-brand" disabled={!nameOk || busy} onClick={join}>Join</button>
            </div>
            {name && !nameOk && <p className="text-xs mt-1" style={{ color: 'var(--bad)' }}>2–24 characters: letters, numbers, spaces, . _ -</p>}
          </div>
        )}
        {err && <p className="text-xs mt-2" style={{ color: 'var(--bad)' }}>{err}</p>}
      </div>

      {/* Board */}
      <h2 className="font-extrabold text-lg mt-6">Top learners</h2>
      <div className="card mt-3 overflow-hidden">
        {rows === null ? (
          <Spinner label="Loading leaderboard" />
        ) : failed ? (
          <p className="p-6 text-center muted text-sm">The leaderboard couldn&apos;t be loaded right now. Please try again later.</p>
        ) : (
          <ol>
            {[...rows, ...SAMPLES.slice(0, Math.max(0, MIN_ROWS - rows.length)).map((s) => ({ uid: `s-${s.name}`, ...s }))]
              .sort((a, b) => b.points - a.points).map((r, i) => {
              const me = mine?.uid === r.uid;
              return (
                <li key={r.uid} className="flex items-center gap-3 px-4 py-2.5" style={{ borderTop: i ? '1px solid var(--line)' : undefined, background: me ? 'var(--brand-soft)' : undefined }}>
                  <span className="w-7 text-center font-extrabold text-sm">{MEDAL[i] ?? i + 1}</span>
                  <span className="flex-1 min-w-0 truncate font-semibold text-sm">{r.name}{me && <span className="chip chip-brand ml-2">you</span>}</span>
                  <span className="font-extrabold text-sm w-16 text-right">{r.points.toLocaleString('en-IN')}</span>
                </li>
              );
            })}
          </ol>
        )}
        {mine && rows && !inTop && (
          <div className="flex items-center gap-3 px-4 py-2.5" style={{ borderTop: '1px solid var(--line)', background: 'var(--brand-soft)' }}>
            <span className="w-7 text-center font-extrabold text-sm">{rank ?? '–'}</span>
            <span className="flex-1 truncate font-semibold text-sm">{mine.name}<span className="chip chip-brand ml-2">you</span></span>
            <span className="font-extrabold text-sm w-16 text-right">{mine.points.toLocaleString('en-IN')}</span>
          </div>
        )}
      </div>
      <p className="text-xs faint mt-3">Points come from your own activity and update a few seconds after you study or take a test.</p>
    </div>
  );
}
