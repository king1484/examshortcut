'use client';
import Link from 'next/link';
import { useState } from 'react';

export interface CatCalcSection { id: string; short: string; name: string; questions: number; color: string }

interface St { mc: number; mw: number; tc: number; tw: number }
type Field = keyof St;

const PLUS = 3;
const MINUS = 1;
const FIELDS: { k: Field; label: string; hint: string }[] = [
  { k: 'mc', label: 'MCQ correct', hint: `+${PLUS} each` },
  { k: 'mw', label: 'MCQ wrong', hint: `−${MINUS} each` },
  { k: 'tc', label: 'TITA correct', hint: `+${PLUS} each` },
  { k: 'tw', label: 'TITA wrong', hint: 'no penalty' },
];

const raw = (s: St) => PLUS * (s.mc + s.tc) - MINUS * s.mw;

export function CatScoreCalculator({ sections, minutesPerSection = 40 }: { sections: CatCalcSection[]; minutesPerSection?: number }) {
  const [st, setSt] = useState<Record<string, St>>(() => Object.fromEntries(sections.map((s) => [s.id, { mc: 0, mw: 0, tc: 0, tw: 0 }])));

  const update = (id: string, f: Field, val: number, cap: number) => {
    setSt((p) => {
      const cur = p[id];
      const others = cur.mc + cur.mw + cur.tc + cur.tw - cur[f];
      const v = Math.max(0, Math.min(Math.floor(val) || 0, cap - others));
      return { ...p, [id]: { ...cur, [f]: v } };
    });
  };

  const rows = sections.map((s) => {
    const x = st[s.id];
    const correct = x.mc + x.tc;
    const attempted = correct + x.mw + x.tw;
    return { s, x, correct, attempted, wrong: x.mw + x.tw, score: raw(x), max: s.questions * PLUS, neg: x.mw * MINUS };
  });
  const tot = rows.reduce((a, r) => ({ correct: a.correct + r.correct, attempted: a.attempted + r.attempted, score: a.score + r.score, max: a.max + r.max, neg: a.neg + r.neg, q: a.q + r.s.questions }),
    { correct: 0, attempted: 0, score: 0, max: 0, neg: 0, q: 0 });
  const acc = (c: number, a: number) => (a ? `${Math.round((100 * c) / a)}%` : '—');
  const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };

  return (
    <div className="mt-6">
      <div className="space-y-3">
        {rows.map(({ s, x, attempted, score, max }) => (
          <div key={s.id} className="card p-4" style={{ borderTop: `3px solid ${s.color}` }}>
            <div className="flex items-center justify-between gap-2 flex-wrap">
              <span className="font-bold text-sm"><span style={{ color: s.color }}>{s.short}</span> <span className="faint font-normal">· {s.questions} Q · {minutesPerSection} min</span></span>
              <span className="text-xs faint">{attempted}/{s.questions} attempted</span>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-2">
              {FIELDS.map((f) => (
                <label key={f.k} className="text-xs font-semibold faint uppercase">
                  {f.label}
                  <input type="number" inputMode="numeric" min={0} max={s.questions} placeholder="0" value={x[f.k] === 0 ? '' : x[f.k]}
                    onChange={(e) => update(s.id, f.k, Number(e.target.value), s.questions)}
                    className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
                  <span className="block normal-case font-normal mt-0.5">{f.hint}</span>
                </label>
              ))}
            </div>
            <p className="text-sm mt-2">Section score <b>{score}</b><span className="faint"> / {max}</span></p>
          </div>
        ))}
      </div>

      <div className="card p-5 mt-5">
        <div className="grid grid-cols-3 gap-3 text-center">
          <div><div className="text-3xl font-extrabold">{tot.score}</div><div className="text-xs faint font-semibold uppercase">Raw score / {tot.max}</div></div>
          <div><div className="text-3xl font-extrabold">{acc(tot.correct, tot.attempted)}</div><div className="text-xs faint font-semibold uppercase">Accuracy</div></div>
          <div><div className="text-3xl font-extrabold">{tot.attempted}<span className="text-base faint">/{tot.q}</span></div><div className="text-xs faint font-semibold uppercase">Attempts</div></div>
        </div>

        <div className="tbl-wrap mt-4">
          <table className="tbl">
            <thead><tr><th>Section</th><th>Attempts</th><th>Correct</th><th>Accuracy</th><th>Raw score</th></tr></thead>
            <tbody>
              {rows.map(({ s, attempted, correct, score, max }) => (
                <tr key={s.id}>
                  <td className="font-semibold" style={{ color: s.color }}>{s.short}</td>
                  <td>{attempted}/{s.questions}</td><td>{correct}</td><td>{acc(correct, attempted)}</td><td>{score} <span className="faint">/ {max}</span></td>
                </tr>
              ))}
              <tr>
                <td className="font-bold">Total</td>
                <td className="font-bold">{tot.attempted}/{tot.q}</td><td className="font-bold">{tot.correct}</td><td className="font-bold">{acc(tot.correct, tot.attempted)}</td><td className="font-bold">{tot.score} <span className="faint font-normal">/ {tot.max}</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p className="text-sm mt-3">
          Marks lost to wrong MCQs: <b style={{ color: 'var(--bad)' }}>{'−'}{tot.neg}</b>. Wrong TITA answers cost nothing, and unattempted questions score 0.
        </p>
      </div>

      <div className="card p-4 mt-5" style={{ background: 'var(--warn-soft)', borderColor: 'var(--warn)' }}>
        <div className="font-bold text-sm" style={{ color: 'var(--warn)' }}>This is a raw score, not a percentile</div>
        <p className="text-sm mt-1.5">
          CAT percentiles are computed from <b>scaled scores</b>. The IIMs equate the three slots for difficulty, and the result changes with the slot, the paper and the year. We therefore do not convert raw marks into a percentile; any such mapping would be invented. For real numbers, see the{' '}
          <Link href="/exams/cat/cutoffs/" className="underline font-semibold">CAT cut-offs page</Link> (institute qualifying percentiles and typical shortlist bands), and read{' '}
          <Link href="/exams/cat/exam-pattern/" className="underline font-semibold">how normalisation works</Link>.
        </p>
      </div>
    </div>
  );
}
