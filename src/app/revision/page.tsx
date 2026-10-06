'use client';
import Link from 'next/link';
import { useState } from 'react';
import { store, useStore } from '@/lib/store';
import { SECTION_META, type SectionId } from '@/lib/sections';
import { Md, isSvg } from '@/components/Md';
import { AuthGate } from '@/components/Auth';

export default function RevisionPage() {
  const mistakes = useStore(store.mistakes, {});
  const bookmarks = useStore(store.bookmarks, {});
  const scores = useStore(store.topicScores, {});
  const studied = useStore(store.studied, {});
  const attempts = useStore(store.attempts, {});
  const [tab, setTab] = useState<'mistakes' | 'bookmarks' | 'progress'>('mistakes');
  const [section, setSection] = useState<SectionId | 'all'>('all');

  const mKeys = Object.keys(mistakes).filter((k) => section === 'all' || mistakes[k].section === section);
  const bKeys = Object.keys(bookmarks).filter((k) => section === 'all' || bookmarks[k].section === section);
  const sections = Array.from(new Set([...Object.values(mistakes), ...Object.values(bookmarks)].map((x) => x.section).filter(Boolean))) as SectionId[];

  const studiedCount = Object.keys(studied).length;
  const attemptList = Object.entries(attempts).flatMap(([id, list]) => list.map((a) => ({ id, ...a }))).sort((a, b) => b.at - a.at);

  const tabs = [
    ['mistakes', `Mistakes (${Object.keys(mistakes).length})`],
    ['bookmarks', `Saved (${Object.keys(bookmarks).length})`],
    ['progress', 'Progress'],
  ] as const;

  return (
    <AuthGate what="see your revision list">
    <div className="max-w-4xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">My revision</h1>
      <p className="muted mt-2">Everything you got wrong, saved, or studied — saved in this browser and synced to your account when you're logged in.</p>

      <div className="flex gap-2 mt-5 flex-wrap">
        {tabs.map(([k, label]) => (
          <button key={k} className="chip" style={tab === k ? { background: 'var(--ink)', color: 'var(--bg)', borderColor: 'var(--ink)' } : {}} onClick={() => setTab(k)}>{label}</button>
        ))}
        <span className="flex-1" />
        {(tab === 'mistakes' || tab === 'bookmarks') && sections.length > 1 && (
          <select className="btn text-sm" value={section} onChange={(e) => setSection(e.target.value as SectionId | 'all')} style={{ padding: '.3rem .5rem' }}>
            <option value="all">All sections</option>
            {sections.map((s) => <option key={s} value={s}>{SECTION_META[s]?.short ?? s}</option>)}
          </select>
        )}
      </div>

      {tab === 'mistakes' && (
        <div className="space-y-3 mt-5">
          <p className="text-sm muted">Every wrong or skipped question from topic tests, worked examples and mocks lands here automatically. Re-attempt each one: pick an answer to check yourself, then remove it once you've nailed it.</p>
          {mKeys.length === 0 && <Empty text="No mistakes yet — take a topic test or a mock." />}
          {mKeys.map((k) => <SavedCard key={k} sk={k} item={mistakes[k]} onRemove={() => store.removeMistake(k)} removeLabel="Got it — remove" />)}
        </div>
      )}

      {tab === 'bookmarks' && (
        <div className="space-y-3 mt-5">
          {bKeys.length === 0 && <Empty text="Nothing saved yet — tap ☆ Save on any question." />}
          {bKeys.map((k) => <SavedCard key={k} sk={k} item={bookmarks[k]} onRemove={() => store.removeBookmark(k)} removeLabel="Remove" />)}
        </div>
      )}

      {tab === 'progress' && (
        <div className="mt-5 space-y-8">
          <section>
            <h2 className="font-extrabold text-lg">Topic tests</h2>
            {Object.keys(scores).length === 0 && <Empty text="Take a topic test to see scores here." />}
            <div className="tbl-wrap mt-3">
              {Object.keys(scores).length > 0 && (
                <table className="tbl">
                  <thead><tr><th>Topic</th><th>Best</th><th>Last</th><th>When</th></tr></thead>
                  <tbody>
                    {Object.entries(scores).sort((a, b) => b[1].at - a[1].at).map(([k, s]) => (
                      <tr key={k}>
                        <td>{k.replace(/\//g, ' · ').replace(/-/g, ' ')}</td>
                        <td className="font-bold" style={{ color: s.best / s.total >= 0.8 ? 'var(--ok)' : s.best / s.total < 0.5 ? 'var(--bad)' : 'var(--warn)' }}>{s.best}/{s.total}</td>
                        <td>{s.last}/{s.total}</td>
                        <td className="faint text-xs">{new Date(s.at).toLocaleDateString('en-IN')}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          </section>
          <section>
            <h2 className="font-extrabold text-lg">Mock attempts</h2>
            {attemptList.length === 0 && <Empty text="No mock attempts yet." />}
            <div className="tbl-wrap mt-3">
              {attemptList.length > 0 && (
                <table className="tbl">
                  <thead><tr><th>Paper</th><th>Score</th><th>Accuracy</th><th>When</th></tr></thead>
                  <tbody>
                    {attemptList.slice(0, 20).map((a, i) => (
                      <tr key={i}>
                        <td><Link className="underline decoration-dotted" href={`/exams/ssc-cgl/mocks/${a.id}/`}>{a.id}</Link></td>
                        <td className="font-bold">{Number.isInteger(a.score) ? a.score : a.score.toFixed(2)}<span className="faint font-normal">/{a.max}</span></td>
                        <td>{a.correct + a.wrong ? Math.round((100 * a.correct) / (a.correct + a.wrong)) : 0}%</td>
                        <td className="faint text-xs">{new Date(a.at).toLocaleString('en-IN')}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          </section>
          <section>
            <h2 className="font-extrabold text-lg">Topics marked studied</h2>
            <p className="text-sm muted mt-1">{studiedCount} of ~72 topics done.</p>
            <div className="h-3 rounded-full mt-2 overflow-hidden" style={{ background: 'var(--surface-2)' }}>
              <div className="h-full rounded-full" style={{ width: `${Math.min(100, (studiedCount / 72) * 100)}%`, background: 'var(--ok)' }} />
            </div>
          </section>
        </div>
      )}
    </div>
    </AuthGate>
  );
}

function Empty({ text }: { text: string }) {
  return <div className="card p-6 text-center muted text-sm">{text}</div>;
}

function SavedCard({ sk, item, onRemove, removeLabel }: { sk: string; item: { question: { q: string; options: string[]; answer: number; solution: string; shortcut?: string | null }; chosen: number | null; from: string; href: string }; onRemove: () => void; removeLabel: string }) {
  const [chosen, setChosen] = useState<number | null>(null);
  const revealed = chosen !== null;
  const q = item.question;
  return (
    <div className="card p-4">
      <div className="flex items-center justify-between gap-2 text-xs faint">
        <span>{item.from}</span>
        <button className="underline" onClick={onRemove}>{removeLabel}</button>
      </div>
      <div className="mt-2"><Md>{q.q}</Md></div>
      {isSvg(q.q) || (q.options.length === 0) ? null : (
        <div className="grid gap-1.5 mt-2">
          {q.options.map((o, i) => {
            let state: 'idle' | 'selected' | 'correct' | 'wrong' | 'missed' = 'idle';
            if (revealed) { if (i === q.answer) state = chosen === i ? 'correct' : 'missed'; else if (chosen === i) state = 'wrong'; }
            else if (chosen === i) state = 'selected';
            return (
              <button key={i} disabled={revealed} onClick={() => setChosen(i)}
                className="text-left text-sm p-2 rounded-lg border transition-colors"
                style={{ borderColor: state === 'correct' ? 'var(--ok)' : state === 'wrong' ? 'var(--bad)' : state === 'selected' ? 'var(--info)' : 'var(--line)', background: state === 'correct' ? 'var(--ok-soft)' : state === 'wrong' ? 'var(--bad-soft)' : state === 'selected' ? 'var(--info-soft)' : 'transparent' }}>
                <b>{'ABCD'[i]}.</b> <Md inline>{o}</Md>
              </button>
            );
          })}
        </div>
      )}
      {revealed && (
        <details className="mt-2 text-sm">
          <summary className="cursor-pointer font-semibold">Solution</summary>
          <Md className="mt-1.5">{q.shortcut ? q.shortcut : q.solution}</Md>
        </details>
      )}
    </div>
  );
}
