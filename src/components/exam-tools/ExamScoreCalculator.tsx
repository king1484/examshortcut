'use client';
import Link from 'next/link';
import { useMemo, useState } from 'react';
import { SCORE_CFG, type CutRef, type StageDef } from '@/lib/examTools';

const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };
const on = { background: 'var(--ink)', color: 'var(--bg)' };
const r2 = (n: number) => Math.round(n * 100) / 100;
const show = (n: number) => String(r2(n));

interface Ans { c: number; w: number }

export function ExamScoreCalculator({ id, cuts }: { id: string; cuts: Record<string, CutRef[]> }) {
  const cfg = SCORE_CFG[id];
  const [si, setSi] = useState(0);
  const [ans, setAns] = useState<Record<string, Ans>>({});
  const [cat, setCat] = useState('UR');
  const [yi, setYi] = useState(0);
  const [sci, setSci] = useState(0);

  const stage: StageDef = cfg.stages[si];
  const get = (i: number): Ans => ans[`${stage.id}:${i}`] ?? { c: 0, w: 0 };
  const set = (i: number, field: 'c' | 'w', raw: number) => {
    const q = stage.sections[i].q;
    const v = Math.max(0, Math.min(q, Math.floor(raw) || 0));
    setAns((p) => {
      const cur = p[`${stage.id}:${i}`] ?? { c: 0, w: 0 };
      const next = { ...cur, [field]: v };
      if (next.c + next.w > q) { if (field === 'c') next.w = q - next.c; else next.c = q - next.w; }
      return { ...p, [`${stage.id}:${i}`]: next };
    });
  };

  const t = useMemo(() => {
    let merit = 0, meritMax = 0, qual = 0, qualMax = 0, correct = 0, wrong = 0, qs = 0;
    stage.sections.forEach((s, i) => {
      const a = ans[`${stage.id}:${i}`] ?? { c: 0, w: 0 };
      const net = a.c * s.mpq - a.w * s.neg;
      if (s.merit === false) { qual += net; qualMax += s.q * s.mpq; } else { merit += net; meritMax += s.q * s.mpq; }
      correct += a.c; wrong += a.w; qs += s.q;
    });
    return { merit, meritMax, qual, qualMax, correct, wrong, qs };
  }, [stage, ans]);

  const accuracy = t.correct + t.wrong ? Math.round((100 * t.correct) / (t.correct + t.wrong)) : 0;

  const refs = cuts[stage.cutStage ?? ''] ?? [];
  const ref = refs[Math.min(yi, Math.max(0, refs.length - 1))] as CutRef | undefined;
  const scope = ref?.scopes[Math.min(sci, Math.max(0, (ref?.scopes.length ?? 1) - 1))];
  const cats = scope ? Object.keys(scope.values) : [];
  const catKey = scope && scope.values[cat] !== undefined ? cat : cats[0];
  const cutRaw = scope && catKey ? scope.values[catKey] : null;
  const cutScaled = cutRaw !== null && ref ? (cutRaw / ref.maxMarks) * t.meritMax : null;
  const gap = cutScaled !== null ? t.merit - cutScaled : null;
  const sameMax = ref ? Math.abs(ref.maxMarks - t.meritMax) < 0.01 : true;

  const qp = stage.qualPct?.[cat];
  const qualMin = qp !== undefined ? (qp / 100) * t.meritMax : null;

  const changeStage = (i: number) => { setSi(i); setYi(0); setSci(0); };

  return (
    <div className="mt-6">
      {cfg.stages.length > 1 && (
        <div className="flex gap-2 flex-wrap">
          {cfg.stages.map((s, i) => (
            <button key={s.id} className="chip" style={si === i ? on : {}} onClick={() => changeStage(i)}>{s.label}</button>
          ))}
        </div>
      )}

      <div className="space-y-3 mt-5">
        {stage.sections.map((s, i) => {
          const a = get(i);
          return (
            <div key={`${stage.id}-${i}`} className="card p-4">
              <div className="flex items-center justify-between gap-2 flex-wrap">
                <span className="font-bold text-sm">{s.name}</span>
                <span className="text-xs faint">{s.q} Q · +{show(s.mpq)} / -{show(s.neg)}{s.mins ? ` · ${s.mins} min` : ''}</span>
              </div>
              <div className="grid grid-cols-2 gap-3 mt-2">
                {(['c', 'w'] as const).map((f) => (
                  <label key={f} className="text-xs font-semibold faint uppercase">
                    {f === 'c' ? 'Correct' : 'Wrong'}
                    <input type="number" inputMode="numeric" min={0} max={s.q} value={a[f]} onChange={(e) => set(i, f, Number(e.target.value))}
                      className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
                  </label>
                ))}
              </div>
              <p className="text-xs faint mt-2">{a.c + a.w} of {s.q} attempted · section score {show(a.c * s.mpq - a.w * s.neg)}</p>
            </div>
          );
        })}
      </div>

      <div className="card p-5 mt-5" aria-live="polite">
        <div className="grid grid-cols-3 gap-3 text-center">
          <div><div className="text-3xl font-extrabold">{show(t.merit)}</div><div className="text-xs faint font-semibold uppercase">Net marks / {show(t.meritMax)}</div></div>
          <div><div className="text-3xl font-extrabold">{accuracy}%</div><div className="text-xs faint font-semibold uppercase">Accuracy</div></div>
          <div><div className="text-3xl font-extrabold">{t.correct + t.wrong}<span className="text-base faint">/{t.qs}</span></div><div className="text-xs faint font-semibold uppercase">Attempted</div></div>
        </div>
        {t.qualMax > 0 && <p className="text-sm mt-3">Qualifying section score: <b>{show(t.qual)}</b> of {show(t.qualMax)} (not part of merit marks).</p>}
        <p className="text-sm mt-3 muted">Net marks = correct × marks per question − wrong × penalty. This is your raw score, before any normalisation.</p>

        {(stage.qualPct || refs.length > 0) && (
          <div className="mt-4">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-sm font-bold">Your category:</span>
              {['UR', 'EWS', 'OBC', 'SC', 'ST'].map((c) => (
                <button key={c} className="chip" style={cat === c ? on : {}} onClick={() => setCat(c)}>{c}</button>
              ))}
            </div>
          </div>
        )}

        {qualMin !== null && (
          <div className="mt-4">
            <p className="text-sm">
              Minimum qualifying marks for {cat}: <b>{qp}%</b> = <b>{show(qualMin)}</b> of {show(t.meritMax)}.{' '}
              <b style={{ color: t.merit >= qualMin ? 'var(--ok)' : 'var(--bad)' }}>
                {t.merit >= qualMin ? 'Your raw score is above this line.' : `Your raw score is ${show(qualMin - t.merit)} short of this line.`}
              </b>
            </p>
            {stage.qualNote && <p className="text-xs faint mt-1">{stage.qualNote}</p>}
          </div>
        )}

        {stage.qualPct && refs.length === 0 && (
          <p className="text-xs faint mt-3">Qualifying is the floor. The cut-off that actually shortlists candidates is higher and is announced with the result. See the <Link href={`/exams/${id}/cutoffs/`} className="underline decoration-dotted">cutoffs page</Link>.</p>
        )}

        {ref && scope && cutScaled !== null && (
          <div className="mt-5">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-sm font-bold">Compare with a past cut-off:</span>
              {refs.map((r, i) => (
                <button key={r.id} className="chip" style={yi === i ? on : {}} onClick={() => { setYi(i); setSci(0); }}>{r.label}</button>
              ))}
            </div>
            {ref.scopes.length > 1 && (
              <label className="block text-xs font-semibold faint uppercase mt-3">
                {ref.scopes.length > 6 ? 'State' : 'List'}
                <select value={sci} onChange={(e) => setSci(Number(e.target.value))} className="w-full sm:w-72 mt-1 p-2 rounded-lg border text-sm font-semibold normal-case" style={input}>
                  {ref.scopes.map((s, i) => <option key={s.name} value={i}>{s.name}</option>)}
                </select>
              </label>
            )}
            {cats.length > 1 && (
              <div className="flex items-center gap-2 flex-wrap mt-3">
                {cats.map((c) => (
                  <button key={c} className="chip" style={catKey === c ? on : {}} onClick={() => setCat(c)}>{c}</button>
                ))}
              </div>
            )}
            <div className="mt-3">
              <div className="h-4 rounded-full overflow-hidden relative" style={{ background: 'var(--surface-2)' }}>
                <div className="h-full" style={{ width: `${Math.max(0, Math.min(100, cutScaled ? (t.merit / cutScaled) * 100 : 0))}%`, background: gap !== null && gap >= 0 ? 'var(--ok)' : 'var(--warn)' }} />
                <div className="absolute top-0 bottom-0 w-0.5" style={{ right: 0, background: 'var(--ink)' }} />
              </div>
              <p className="text-sm mt-2">
                Cut-off <b>{show(cutRaw as number)}</b>{sameMax ? '' : <> out of {ref.maxMarks} (about <b>{show(cutScaled)}</b> on this paper&apos;s {show(t.meritMax)})</>} · your net <b>{show(t.merit)}</b> ·{' '}
                <b style={{ color: gap !== null && gap >= 0 ? 'var(--ok)' : 'var(--warn)' }}>{gap !== null && gap >= 0 ? '+' : ''}{gap !== null ? show(gap) : ''} vs cut-off</b>
              </p>
              <p className="text-xs faint mt-2">List used: {ref.list}. Past cut-offs are on normalised marks and move with paper difficulty, so use this as a rough gauge, not a result. {sameMax ? '' : 'The cut-off was scaled by percentage because the paper total changed. '}Full tables are on the <Link href={`/exams/${id}/cutoffs/`} className="underline decoration-dotted">cutoffs page</Link>.</p>
            </div>
          </div>
        )}
      </div>

      <p className="text-xs faint mt-3">{stage.note}</p>
    </div>
  );
}
