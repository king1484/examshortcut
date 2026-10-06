'use client';
import { useState } from 'react';
import { CENTRAL, type SalaryPost } from '@/lib/examTools';

/* Two modes. "central" follows the 7th CPC rules for central government and railway posts, with the DA and
   the other rates editable. "bank" is for IBPS posts: banks pay DA, HRA and special allowance by circular,
   and we could not confirm current official values, so those stay blank for the reader to fill in. */

const input = { borderColor: 'var(--line)', background: 'var(--surface)', color: 'var(--ink)' };
const on = { background: 'var(--ink)', color: 'var(--bg)' };
const inr = (n: number) => '₹' + Math.round(n).toLocaleString('en-IN');
const num = (v: string) => (v === '' ? 0 : Math.max(0, Number(v) || 0));

function Field({ label, value, onChange, hint, step = 1 }: { label: string; value: string; onChange: (v: string) => void; hint?: string; step?: number }) {
  return (
    <label className="text-xs font-semibold faint uppercase">
      {label}
      <input type="number" inputMode="decimal" min={0} step={step} value={value} onChange={(e) => onChange(e.target.value)}
        className="w-full mt-1 p-2 rounded-lg border text-base font-bold" style={input} />
      {hint && <span className="block text-xs font-normal normal-case mt-1 faint">{hint}</span>}
    </label>
  );
}

function Result({ rows, inHand, gross }: { rows: [string, number, boolean?][]; inHand: number; gross: number }) {
  return (
    <div className="card p-5 mt-5" aria-live="polite">
      <div className="grid grid-cols-2 gap-3 text-center">
        <div><div className="text-3xl font-extrabold">{inr(inHand)}</div><div className="text-xs faint font-semibold uppercase">Approx. in-hand per month</div></div>
        <div><div className="text-3xl font-extrabold">{inr(gross)}</div><div className="text-xs faint font-semibold uppercase">Gross per month</div></div>
      </div>
      <div className="tbl-wrap mt-4">
        <table className="tbl">
          <tbody>
            {rows.map(([k, v, minus]) => (
              <tr key={k}><td>{k}</td><td className="text-right" style={minus ? { color: 'var(--bad)' } : {}}>{minus ? '-' : ''}{inr(v)}</td></tr>
            ))}
            <tr><td className="font-bold">In-hand (before income tax)</td><td className="text-right font-bold">{inr(inHand)}</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export function SalaryCalculator({ mode, posts, bank }: { mode: 'central' | 'bank'; posts: SalaryPost[]; bank: { name: string; basic: number; scaleMax: number | null }[] }) {
  return mode === 'central' ? <Central posts={posts} /> : <Bank posts={bank} />;
}

function Central({ posts }: { posts: SalaryPost[] }) {
  const [pi, setPi] = useState(0);
  const [oi, setOi] = useState(0);
  const post = posts[Math.min(pi, posts.length - 1)];
  const opt = post.options[Math.min(oi, post.options.length - 1)];
  const [basicEdit, setBasicEdit] = useState<string | null>(null);
  const [da, setDa] = useState(String(CENTRAL.da));
  const [city, setCity] = useState<'X' | 'Y' | 'Z'>('X');
  const [high, setHigh] = useState(true);
  const [nps, setNps] = useState(String(CENTRAL.nps));
  const [health, setHealth] = useState<string | null>(null);
  const [other, setOther] = useState('');

  const basic = basicEdit !== null ? num(basicEdit) : opt.basic;
  const daPct = num(da);
  const daAmt = (basic * daPct) / 100;
  const hraAmt = (basic * CENTRAL.hra[city]) / 100;
  const [tHigh, tLow] = CENTRAL.transport(opt.level);
  const taBase = high ? tHigh : tLow;
  const taAmt = taBase * (1 + daPct / 100);
  const gross = basic + daAmt + hraAmt + taAmt;
  const npsAmt = ((basic + daAmt) * num(nps)) / 100;
  const healthAmt = health !== null ? num(health) : CENTRAL.cghs(opt.level);
  const ded = npsAmt + healthAmt + num(other);
  const inHand = gross - ded;

  const pickPost = (i: number) => { setPi(i); setOi(0); setBasicEdit(null); setHealth(null); };
  const pickOpt = (i: number) => { setOi(i); setBasicEdit(null); setHealth(null); };

  return (
    <div className="mt-6">
      <div className="card p-5">
        <label className="text-xs font-semibold faint uppercase block">
          Post
          <select value={pi} onChange={(e) => pickPost(Number(e.target.value))} className="w-full mt-1 p-2 rounded-lg border text-sm font-semibold normal-case" style={input}>
            {posts.map((p, i) => <option key={p.key} value={i}>{p.name}</option>)}
          </select>
        </label>
        {post.options.length > 1 && (
          <div className="flex items-center gap-2 flex-wrap mt-3">
            <span className="text-sm font-bold">Pay level:</span>
            {post.options.map((o, i) => <button key={o.level} className="chip" style={oi === i ? on : {}} onClick={() => pickOpt(i)}>Level {o.level}</button>)}
          </div>
        )}
        <div className="flex items-center gap-2 flex-wrap mt-3">
          <span className="text-sm font-bold">City class (HRA):</span>
          {(['X', 'Y', 'Z'] as const).map((c) => <button key={c} className="chip" style={city === c ? on : {}} onClick={() => setCity(c)}>{c} · {CENTRAL.hra[c]}%</button>)}
        </div>
        <label className="flex items-center gap-2 mt-3 text-sm">
          <input type="checkbox" checked={high} onChange={(e) => setHigh(e.target.checked)} />
          Posted in a higher transport-allowance city (the larger metros)
        </label>

        <div className="grid sm:grid-cols-2 gap-4 mt-4">
          <Field label={`Basic pay (Level ${opt.level})`} value={basicEdit ?? String(opt.basic)} onChange={setBasicEdit} hint="Starts at the entry pay for the level. Change it if you are past the first increment." />
          <Field label="DA (% of basic)" value={da} onChange={setDa} step={0.5} hint={`${CENTRAL.da}% from ${CENTRAL.daAsOf}. The government revises DA twice a year, so update it when a new rate is notified.`} />
          <Field label="NPS (% of basic + DA)" value={nps} onChange={setNps} hint="Employee share under NPS. Check your service rules, as pension scheme options differ." />
          <Field label="Health scheme (₹ per month)" value={health ?? String(CENTRAL.cghs(opt.level))} onChange={setHealth} hint="CGHS band for your level. Railway staff use their own scheme, so check your payslip." />
          <Field label="Other deductions (₹ per month)" value={other} onChange={setOther} hint="Group insurance, licence fee, and so on." />
        </div>
      </div>

      <Result gross={gross} inHand={inHand} rows={[
        [`Basic pay`, basic],
        [`Dearness allowance (${daPct}%)`, daAmt],
        [`House rent allowance (${CENTRAL.hra[city]}%)`, hraAmt],
        [`Transport allowance (${inr(taBase)} plus DA on it)`, taAmt],
        [`NPS (${num(nps)}% of basic + DA)`, npsAmt, true],
        [`Health scheme`, healthAmt, true],
        ...(num(other) ? [[`Other deductions`, num(other), true] as [string, number, boolean]] : []),
      ]} />
      <p className="text-xs faint mt-3">
        Not included: income tax, risk, ration, uniform, night duty, running and other post-specific allowances, and the DA rate that applies after the date above. The transport rate assumes the larger-city or other-place band for the pay level, and the exact list of larger cities is in the government order. Your payslip is the final word.
      </p>
    </div>
  );
}

function Bank({ posts }: { posts: { name: string; basic: number; scaleMax: number | null }[] }) {
  const [pi, setPi] = useState(0);
  const post = posts[Math.min(pi, posts.length - 1)];
  const [basicEdit, setBasicEdit] = useState<string | null>(null);
  const [da, setDa] = useState('');
  const [hra, setHra] = useState('');
  const [special, setSpecial] = useState('');
  const [nps, setNps] = useState('');
  const [other, setOther] = useState('');

  const basic = basicEdit !== null ? num(basicEdit) : post.basic;
  const daAmt = (basic * num(da)) / 100;
  const hraAmt = (basic * num(hra)) / 100;
  const spAmt = num(special);
  const gross = basic + daAmt + hraAmt + spAmt;
  const npsAmt = ((basic + daAmt) * num(nps)) / 100;
  const inHand = gross - npsAmt - num(other);
  const filled = da !== '' && hra !== '';

  return (
    <div className="mt-6">
      <div className="card p-5">
        <p className="text-sm">
          Banks set DA, HRA and special allowance through circulars that change often, and we could not confirm current official values.
          So those boxes start empty. Fill them from your bank&apos;s latest circular or offer letter.
        </p>
        {posts.length > 1 && (
          <label className="text-xs font-semibold faint uppercase block mt-3">
            Post
            <select value={pi} onChange={(e) => { setPi(Number(e.target.value)); setBasicEdit(null); }} className="w-full mt-1 p-2 rounded-lg border text-sm font-semibold normal-case" style={input}>
              {posts.map((p, i) => <option key={p.name} value={i}>{p.name}</option>)}
            </select>
          </label>
        )}
        <div className="grid sm:grid-cols-2 gap-4 mt-4">
          <Field label="Basic pay (₹ per month)" value={basicEdit ?? String(post.basic)} onChange={setBasicEdit} hint={`Starting basic${post.scaleMax ? ` on a scale up to ${inr(post.scaleMax)}` : ''}. Increments raise it.`} />
          <Field label="DA (% of basic)" value={da} onChange={setDa} step={0.01} hint="Taken from the bank's current circular." />
          <Field label="HRA (% of basic)" value={hra} onChange={setHra} step={0.5} hint="Depends on the centre. Use the rate for your posting." />
          <Field label="Special allowance and others (₹ per month)" value={special} onChange={setSpecial} hint="Total of the fixed allowances on the offer letter." />
          <Field label="NPS (% of basic + DA)" value={nps} onChange={setNps} step={0.5} hint="Your bank's employee contribution rate." />
          <Field label="Other deductions (₹ per month)" value={other} onChange={setOther} hint="Union fee, loans, insurance and so on." />
        </div>
      </div>

      {!filled && <p className="text-sm mt-4" style={{ color: 'var(--warn)' }}>DA and HRA are empty, so the figures below only count what you have entered.</p>}
      <Result gross={gross} inHand={inHand} rows={[
        ['Basic pay', basic],
        [`Dearness allowance (${num(da)}%)`, daAmt],
        [`House rent allowance (${num(hra)}%)`, hraAmt],
        ['Special allowance and others', spAmt],
        [`NPS (${num(nps)}% of basic + DA)`, npsAmt, true],
        ...(num(other) ? [['Other deductions', num(other), true] as [string, number, boolean]] : []),
      ]} />
      <p className="text-xs faint mt-3">Not included: income tax, perquisites, and any bank-specific allowances. Check the official recruitment notice and your bank&apos;s circular for the real structure.</p>
    </div>
  );
}
