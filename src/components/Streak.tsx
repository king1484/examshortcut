'use client';
import Link from 'next/link';
import { useProgress, type StreakInfo } from '@/lib/streak';
import { useAuth } from './Auth';

const MILESTONES = [3, 7, 14, 30, 60, 100, 200, 365];
const nextMilestone = (n: number) => MILESTONES.find((m) => m > n) ?? n + 100;

/** Flame glyph drawn as SVG so it stays crisp and follows the theme (replaces the emoji). */
function Flame({ size = 16, on = true }: { size?: number; on?: boolean }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" aria-hidden focusable="false" style={{ flex: 'none' }}>
      <path d="M12.6 2.2c.4 3-1 4.7-2.5 6.5C8.5 10.6 7 12.5 7 15.2a5.5 5.5 0 0 0 11 0c0-2.3-1-4-2.1-5.3-.3 1.3-1 2.2-2 2.7.6-3.6-.1-7.6-1.3-10.4z"
        fill={on ? 'var(--brand)' : 'none'} stroke={on ? 'none' : 'currentColor'} strokeWidth={on ? 0 : 1.6} strokeLinejoin="round" />
      {on && <path d="M12.3 20.2a2.6 2.6 0 0 1-2.6-2.6c0-1.4.9-2.2 1.6-3 .3 1 .8 1.4 1.4 1.7-.2-1 .1-2 .6-2.8.8.9 1.6 1.9 1.6 3.1a2.6 2.6 0 0 1-2.6 3.6z" fill="var(--brand-ink)" opacity=".85" />}
    </svg>
  );
}

/** Small header chip: shows once the visitor has a live streak. */
export function StreakChip() {
  const { streak } = useProgress();
  const { user, configured } = useAuth();
  if (streak.current < 1 || (configured && !user)) return null;
  const done = streak.todayDone;
  return (
    <Link href="/daily-quiz/" className="chip"
      title={done ? `${streak.current}-day streak — done for today` : `${streak.current}-day streak — do something today to keep it`}
      style={{ padding: '.28rem .6rem .28rem .45rem', gap: '.25rem', color: done ? 'var(--brand-text)' : 'var(--ink-2)', background: done ? 'var(--brand-soft)' : 'var(--surface-2)' }}>
      <Flame size={15} on={done} />
      <span className="font-extrabold">{streak.current}</span>
    </Link>
  );
}

function Check() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden focusable="false">
      <path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" strokeWidth="3.4" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

function Week({ week }: { week: StreakInfo['week'] }) {
  const SIZE = 34;
  return (
    <div className="grid grid-cols-7" aria-label="Last 7 days">
      {week.map((d, i) => {
        const joinL = d.done && week[i - 1]?.done;
        const joinR = d.done && week[i + 1]?.done;
        return (
          <div key={d.day} className="flex flex-col items-center">
            <div className={d.today ? 'font-bold' : 'faint'} style={{ fontSize: '.68rem', marginBottom: 6, color: d.today ? 'var(--brand-text)' : undefined }}>{d.today ? 'Today' : d.label}</div>
            <div className="relative w-full flex justify-center" style={{ height: SIZE }}>
              {joinL && <span className="absolute" style={{ left: 0, right: '50%', top: SIZE / 2 - 3, height: 6, background: 'var(--brand)', opacity: .35 }} />}
              {joinR && <span className="absolute" style={{ left: '50%', right: 0, top: SIZE / 2 - 3, height: 6, background: 'var(--brand)', opacity: .35 }} />}
              <span className="relative flex items-center justify-center rounded-full"
                style={{
                  width: SIZE, height: SIZE,
                  background: d.done ? 'var(--brand)' : 'var(--surface)',
                  color: d.done ? 'var(--brand-ink)' : 'var(--ink-3)',
                  border: d.done ? '2px solid var(--brand)' : d.today ? '2px dashed var(--brand)' : '2px solid var(--line)',
                }}>
                {d.done ? <Check /> : null}
              </span>
            </div>
          </div>
        );
      })}
    </div>
  );
}

/** Progress ring toward the next milestone, with the current count in the middle. */
function Ring({ value, target, on }: { value: number; target: number; on: boolean }) {
  const r = 34, c = 2 * Math.PI * r, pct = Math.min(1, value / target);
  return (
    <div className="relative flex-none" style={{ width: 84, height: 84 }}>
      <svg width="84" height="84" viewBox="0 0 84 84" aria-hidden focusable="false" style={{ transform: 'rotate(-90deg)' }}>
        <circle cx="42" cy="42" r={r} fill="none" stroke="var(--surface-2)" strokeWidth="8" />
        <circle cx="42" cy="42" r={r} fill="none" stroke="var(--brand)" strokeWidth="8" strokeLinecap="round"
          strokeDasharray={c} strokeDashoffset={c * (1 - pct)} style={{ transition: 'stroke-dashoffset .5s ease' }} />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <Flame size={20} on={on} />
        <div className="text-2xl font-extrabold leading-none mt-0.5">{value}</div>
      </div>
    </div>
  );
}

/** Streak panel (personal only — never published to the leaderboard): current / longest / this week. Counts any study, test, mock or mistake logged that day. */
export function StreakCard({ compact = false }: { compact?: boolean }) {
  const { streak } = useProgress();
  const { user, configured, loading } = useAuth();
  if (configured && loading) return <div className="card" style={{ minHeight: 96 }} aria-hidden />;
  if (configured && !user) {
    return (
      <div className="card p-4 sm:p-5 flex items-center gap-4">
        <div className="flex-none flex items-center justify-center rounded-full" style={{ width: 56, height: 56, background: 'var(--surface-2)', color: 'var(--ink-3)' }}>
          <Flame size={26} on={false} />
        </div>
        <div className="min-w-0 flex-1">
          <div className="font-extrabold text-lg leading-tight">Daily streak &amp; points</div>
          <div className="text-xs muted mt-1">Log in to start your streak and compete on the leaderboard.</div>
        </div>
        <Link href="/login/?next=%2Fdashboard%2F" className="btn" style={{ padding: '.4rem .85rem', fontSize: '.8rem' }}>Log in</Link>
      </div>
    );
  }
  const target = nextMilestone(streak.current);
  const msg = streak.current === 0
    ? 'Start today — read one topic or take the daily quiz.'
    : streak.todayDone ? 'Done for today. Come back tomorrow to extend it.' : 'Do one thing today to keep it alive.';
  return (
    <div className="card p-4 sm:p-5">
      <div className="flex items-center gap-4">
        <Ring value={streak.current} target={target} on={streak.current > 0} />
        <div className="min-w-0 flex-1">
          <div className="font-extrabold text-lg leading-tight">{streak.current === 1 ? '1-day streak' : `${streak.current}-day streak`}</div>
          <div className="text-xs muted mt-1">{msg}</div>
          <div className="text-xs faint mt-1">{target - streak.current} more {target - streak.current === 1 ? 'day' : 'days'} to reach {target}</div>
        </div>
        {!compact && <Link href="/daily-quiz/" className="btn hidden sm:inline-flex" style={{ padding: '.4rem .85rem', fontSize: '.8rem' }}>Today&apos;s quiz</Link>}
      </div>

      <div className="mt-4"><Week week={streak.week} /></div>

      {!compact && (
        <div className="grid grid-cols-3 gap-2 mt-4">
          {[
            [streak.longest, 'longest streak'],
            [streak.activeDays, 'active days'],
            [streak.week.filter((d) => d.done).length, 'days this week'],
          ].map(([n, label]) => (
            <div key={label as string} className="rounded-lg px-3 py-2" style={{ background: 'var(--surface-2)' }}>
              <div className="font-extrabold text-lg leading-none">{n}</div>
              <div className="text-xs faint mt-1">{label}</div>
            </div>
          ))}
        </div>
      )}
      {!compact && <Link href="/daily-quiz/" className="btn w-full justify-center mt-3 sm:hidden" style={{ padding: '.45rem .85rem', fontSize: '.85rem' }}>Today&apos;s quiz</Link>}
    </div>
  );
}
