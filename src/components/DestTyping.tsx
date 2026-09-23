'use client';
import { useEffect, useMemo, useRef, useState } from 'react';
import type { DestPassage } from '@/lib/destPassages';

type Op = { kind: 'ok' | 'half' | 'full'; master?: string; typed?: string; why?: string };

const norm = (w: string) => w.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '');

/** Align typed words to the master passage using SSC DEST rules: full mistakes cost 1, half mistakes cost 0.5. The untyped tail is free. */
export function evaluate(master: string, typed: string) {
  const M = master.trim().split(/\s+/);
  const T = typed.trim() ? typed.trim().split(/\s+/) : [];
  const n = M.length, m = T.length, W = m + 1;
  const D = new Float32Array((n + 1) * W);
  const P = new Uint8Array((n + 1) * W); // 1 match/sub, 2 omit, 3 add, 4 join, 5 split, 6 transpose
  const at = (i: number, j: number) => i * W + j;
  for (let i = 1; i <= n; i++) { D[at(i, 0)] = i; P[at(i, 0)] = 2; }
  for (let j = 1; j <= m; j++) { D[at(0, j)] = j; P[at(0, j)] = 3; }
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      const a = M[i - 1], b = T[j - 1];
      const sc = a === b ? 0 : norm(a) === norm(b) && norm(a) ? 0.5 : 1;
      let best = D[at(i - 1, j - 1)] + sc, p = 1;
      if (D[at(i - 1, j)] + 1 < best) { best = D[at(i - 1, j)] + 1; p = 2; }
      if (D[at(i, j - 1)] + 1 < best) { best = D[at(i, j - 1)] + 1; p = 3; }
      if (i >= 2 && norm(b) && norm(b) === norm(M[i - 2] + M[i - 1]) && D[at(i - 2, j - 1)] + 0.5 < best) { best = D[at(i - 2, j - 1)] + 0.5; p = 4; }
      if (j >= 2 && norm(a) && norm(a) === norm(T[j - 2] + b) && D[at(i - 1, j - 2)] + 0.5 < best) { best = D[at(i - 1, j - 2)] + 0.5; p = 5; }
      if (i >= 2 && j >= 2 && b === M[i - 2] && T[j - 2] === a && a !== b && D[at(i - 2, j - 2)] + 0.5 < best) { best = D[at(i - 2, j - 2)] + 0.5; p = 6; }
      D[at(i, j)] = best; P[at(i, j)] = p;
    }
  }
  // Where in the passage did the candidate stop? Pick the cheapest end point (prefer further along on ties).
  let end = 0;
  for (let i = 0; i <= n; i++) if (D[at(i, m)] <= D[at(end, m)]) end = i;
  if (m === 0) end = 0;

  const ops: Op[] = [];
  let i = end, j = m;
  while (i > 0 || j > 0) {
    const p = P[at(i, j)];
    if (p === 1) {
      const a = M[i - 1], b = T[j - 1];
      if (a === b) ops.push({ kind: 'ok', master: a });
      else if (norm(a) === norm(b) && norm(a)) ops.push({ kind: 'half', master: a, typed: b, why: a.toLowerCase() === b.toLowerCase() ? 'Capitalisation' : 'Punctuation' });
      else ops.push({ kind: 'full', master: a, typed: b, why: 'Wrong word / spelling' });
      i--; j--;
    } else if (p === 2) { ops.push({ kind: 'full', master: M[i - 1], why: 'Word left out' }); i--; }
    else if (p === 3) { ops.push({ kind: 'full', typed: T[j - 1], why: 'Extra word' }); j--; }
    else if (p === 4) { ops.push({ kind: 'half', master: `${M[i - 2]} ${M[i - 1]}`, typed: T[j - 1], why: 'Missing space' }); i -= 2; j--; }
    else if (p === 5) { ops.push({ kind: 'half', master: M[i - 1], typed: `${T[j - 2]} ${T[j - 1]}`, why: 'Extra space' }); i--; j -= 2; }
    else { ops.push({ kind: 'half', master: `${M[i - 2]} ${M[i - 1]}`, typed: `${T[j - 2]} ${T[j - 1]}`, why: 'Words swapped' }); i -= 2; j -= 2; }
  }
  ops.reverse();
  const full = ops.filter((o) => o.kind === 'full').length;
  const half = ops.filter((o) => o.kind === 'half').length;
  return { ops, full, half, attemptedWords: end, totalWords: n };
}

const CATS = [
  { k: 'UR', label: 'UR', max: 20 },
  { k: 'OBC', label: 'OBC / EWS', max: 25 },
  { k: 'SCST', label: 'SC / ST / others', max: 30 },
];
const HIST = 'es-dest-history';
type Attempt = { at: string; passage: string; kd: number; secs: number; errPct: number; pass: boolean };

const mmss = (s: number) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

export function DestTyping({ passages }: { passages: DestPassage[] }) {
  const [pid, setPid] = useState(passages[0].id);
  const [mins, setMins] = useState(15);
  const [cat, setCat] = useState('UR');
  const [typed, setTyped] = useState('');
  const [startAt, setStartAt] = useState<number | null>(null);
  const [now, setNow] = useState(0);
  const [done, setDone] = useState<null | { secs: number; typed: string }>(null);
  const [hist, setHist] = useState<Attempt[]>([]);
  const ta = useRef<HTMLTextAreaElement>(null);

  const passage = passages.find((p) => p.id === pid) ?? passages[0];
  const limit = mins * 60;
  const elapsed = startAt ? Math.min(limit, (now - startAt) / 1000) : 0;

  useEffect(() => { try { setHist(JSON.parse(localStorage.getItem(HIST) ?? '[]')); } catch {} }, []);
  useEffect(() => {
    if (!startAt || done) return;
    const t = setInterval(() => setNow(Date.now()), 250);
    return () => clearInterval(t);
  }, [startAt, done]);
  useEffect(() => { if (startAt && !done && elapsed >= limit) finish(); }); // eslint-disable-line react-hooks/exhaustive-deps

  const reset = (id = pid) => { setPid(id); setTyped(''); setStartAt(null); setDone(null); setNow(0); };

  function finish() {
    const secs = startAt ? Math.min(limit, (Date.now() - startAt) / 1000) : 0;
    setDone({ secs, typed });
  }

  const result = useMemo(() => (done ? evaluate(passage.text, done.typed) : null), [done, passage.text]);
  const maxErr = CATS.find((c) => c.k === cat)!.max;
  const kd = (done?.typed ?? typed).length;
  const projected = elapsed > 5 ? Math.round((kd / elapsed) * 900) : 0;

  const summary = result && done ? (() => {
    const mistakes = result.full + result.half / 2;
    const errPct = result.attemptedWords ? (mistakes / result.attemptedWords) * 100 : 100;
    const kd15 = done.secs ? Math.round((kd / done.secs) * 900) : 0;
    const speedOk = mins === 15 ? kd >= 2000 || result.attemptedWords >= result.totalWords : kd15 >= 2000;
    return { mistakes, errPct, kd15, speedOk, pass: speedOk && errPct <= maxErr };
  })() : null;

  useEffect(() => {
    if (!summary || !done) return;
    const a: Attempt = { at: new Date().toISOString(), passage: passage.title, kd, secs: Math.round(done.secs), errPct: +summary.errPct.toFixed(1), pass: summary.pass };
    setHist((h) => {
      const n = [a, ...h].slice(0, 10);
      try { localStorage.setItem(HIST, JSON.stringify(n)); } catch {}
      return n;
    });
  }, [done]); // eslint-disable-line react-hooks/exhaustive-deps

  const box = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };

  return (
    <div>
      <div className="card p-4 flex flex-wrap gap-3 items-end text-sm">
        <label className="font-semibold">Passage
          <select value={pid} onChange={(e) => reset(e.target.value)} className="block mt-1 p-2 rounded-lg border" style={box} disabled={!!startAt && !done}>
            {passages.map((p) => <option key={p.id} value={p.id}>{p.title} ({p.text.length} KD)</option>)}
          </select>
        </label>
        <label className="font-semibold">Time
          <select value={mins} onChange={(e) => { setMins(+e.target.value); reset(); }} className="block mt-1 p-2 rounded-lg border" style={box} disabled={!!startAt && !done}>
            <option value={15}>15 min (real DEST)</option>
            <option value={5}>5 min (quick drill)</option>
          </select>
        </label>
        <label className="font-semibold">Category
          <select value={cat} onChange={(e) => setCat(e.target.value)} className="block mt-1 p-2 rounded-lg border" style={box}>
            {CATS.map((c) => <option key={c.k} value={c.k}>{c.label} (≤{c.max}% errors)</option>)}
          </select>
        </label>
        <div className="ml-auto flex gap-4 items-center">
          <div className="text-center"><div className="text-2xl font-extrabold tabular-nums" style={{ color: limit - elapsed < 60 && startAt && !done ? 'var(--bad)' : 'var(--brand)' }}>{mmss(limit - elapsed)}</div><div className="text-[11px] faint">left</div></div>
          <div className="text-center"><div className="text-2xl font-extrabold tabular-nums">{kd}</div><div className="text-[11px] faint">key depressions</div></div>
          {!done && projected > 0 && (
            <div className="text-center"><div className="text-2xl font-extrabold tabular-nums" style={{ color: projected >= 2000 ? 'var(--ok)' : 'var(--warn)' }}>{projected}</div><div className="text-[11px] faint">pace / 15 min</div></div>
          )}
        </div>
      </div>

      <div className="card p-4 mt-3 max-h-56 overflow-y-auto text-[15px] leading-relaxed select-none" style={{ userSelect: 'none' }} onCopy={(e) => e.preventDefault()}>
        {passage.text}
      </div>

      {!done ? (
        <>
          <textarea
            ref={ta}
            value={typed}
            onChange={(e) => { if (!startAt) { setStartAt(Date.now()); setNow(Date.now()); } setTyped(e.target.value); }}
            onPaste={(e) => e.preventDefault()} onDrop={(e) => e.preventDefault()}
            spellCheck={false} autoCorrect="off" autoCapitalize="off" autoComplete="off"
            placeholder="Start typing the passage here. The timer starts with your first key."
            className="w-full mt-3 p-3 rounded-xl border text-[15px] leading-relaxed font-mono"
            style={{ ...box, minHeight: '14rem' }}
          />
          <div className="flex gap-2 mt-2">
            <button className="btn btn-brand text-sm" disabled={!typed.trim()} onClick={finish}>Submit</button>
            <button className="btn text-sm" onClick={() => reset()}>Restart</button>
          </div>
          <p className="text-xs faint mt-2">Like the real DEST: copy-paste is disabled and there is no spell-check. Backspace and arrow keys are allowed. The test submits itself when the time runs out.</p>
        </>
      ) : result && summary && (
        <div className="mt-4">
          <div className="card p-5" style={{ borderColor: summary.pass ? 'var(--ok)' : 'var(--bad)', borderWidth: 2 }}>
            <div className="text-xl font-extrabold" style={{ color: summary.pass ? 'var(--ok)' : 'var(--bad)' }}>
              {summary.pass ? '✓ Qualified at this level' : '✗ Would not qualify yet'}
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-3 text-sm">
              <div><div className="faint text-xs">Error %</div><b style={{ color: summary.errPct <= maxErr ? 'var(--ok)' : 'var(--bad)' }}>{summary.errPct.toFixed(1)}%</b> <span className="faint text-xs">(limit {maxErr}%)</span></div>
              <div><div className="faint text-xs">Mistakes</div><b>{result.full}</b> full + <b>{result.half}</b> half = <b>{summary.mistakes}</b></div>
              <div><div className="faint text-xs">Key depressions</div><b>{kd}</b> in {mmss(done.secs)}{mins !== 15 && <> · pace <b>{summary.kd15}</b>/15 min</>}</div>
              <div><div className="faint text-xs">Passage covered</div><b>{result.attemptedWords}</b> / {result.totalWords} words</div>
            </div>
            {!summary.speedOk && <p className="text-sm mt-3" style={{ color: 'var(--bad)' }}>Speed: you need about 2000 key depressions in 15 minutes (≈ 27 words a minute). Build speed first, then work on accuracy.</p>}
            <p className="text-xs faint mt-3">Error % = (full + ½ × half mistakes) ÷ words in the part of the passage you typed. Full mistakes: a word left out, an extra word, a wrong word or a spelling error. Half mistakes: spacing, capitalisation, punctuation or two words swapped.</p>
            <div className="flex gap-2 mt-3">
              <button className="btn btn-brand text-sm" onClick={() => reset()}>Try again</button>
              <button className="btn text-sm" onClick={() => reset(passages[(passages.indexOf(passage) + 1) % passages.length].id)}>Next passage →</button>
            </div>
          </div>

          <h3 className="font-extrabold mt-6">Your mistakes, marked on the passage</h3>
          <div className="card p-4 mt-2 text-[15px] leading-loose">
            {result.ops.map((o, k) => o.kind === 'ok' ? <span key={k}>{o.master} </span> : (
              <span key={k} title={`${o.why}${o.typed ? ` — you typed “${o.typed}”` : ''}`}
                className="rounded px-0.5 mr-1"
                style={{ background: o.kind === 'full' ? 'color-mix(in srgb, var(--bad) 18%, transparent)' : 'color-mix(in srgb, var(--warn) 20%, transparent)' }}>
                {o.master && <span style={{ textDecoration: o.typed ? 'line-through' : 'underline wavy' }}>{o.master}</span>}
                {o.typed && <b style={{ color: o.kind === 'full' ? 'var(--bad)' : 'var(--warn)' }}> {o.typed}</b>}
                <sup className="text-[10px] faint ml-0.5">{o.why}</sup>
              </span>
            ))}
            {result.attemptedWords < result.totalWords && <span className="faint">… (not reached)</span>}
          </div>
        </div>
      )}

      {hist.length > 0 && (
        <>
          <h3 className="font-extrabold mt-8">Your last attempts</h3>
          <div className="tbl-wrap mt-2"><table className="tbl text-sm">
            <thead><tr><th>When</th><th>Passage</th><th>KD</th><th>Time</th><th>Error %</th><th></th></tr></thead>
            <tbody>{hist.map((h) => (
              <tr key={h.at}><td>{new Date(h.at).toLocaleString('en-IN', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}</td><td>{h.passage}</td><td>{h.kd}</td><td>{mmss(h.secs)}</td><td>{h.errPct}%</td><td>{h.pass ? '✓' : '✗'}</td></tr>
            ))}</tbody>
          </table></div>
        </>
      )}
    </div>
  );
}
