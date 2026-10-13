'use client';

import Link from 'next/link';
import { useRef, useState } from 'react';

export function FeedbackForm({ kind }: { kind: 'feedback' | 'feature' }) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const [receipt, setReceipt] = useState('');
  const requestId = useRef('');
  const feature = kind === 'feature';
  const inputClass = 'w-full rounded-lg border px-3 py-2 bg-transparent';
  const border = { borderColor: 'var(--line)' };

  async function submit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (busy) return;
    const fields = new FormData(event.currentTarget);
    requestId.current ||= crypto.randomUUID();
    const body = Object.fromEntries(fields.entries());
    setBusy(true); setError('');
    try {
      const response = await fetch('/api/feedback', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...body, kind, id: requestId.current }),
        signal: AbortSignal.timeout(20000),
      });
      const result = await response.json();
      if (!response.ok || result.id !== requestId.current) throw new Error(result.error || 'We could not save your request. Please try again.');
      setReceipt(result.id);
    } catch (e) {
      setError(e instanceof Error && e.name !== 'TimeoutError' && e.name !== 'TypeError'
        ? e.message : 'Could not confirm your submission. Check your connection and retry; your text is still here.');
    } finally { setBusy(false); }
  }

  if (receipt) return (
    <div className="card p-6 mt-6" role="status">
      <h2 className="font-extrabold text-xl">{feature ? 'Feature request received' : 'Feedback received'}</h2>
      <p className="muted mt-2">Thank you for helping improve ExamShortcut. Your submission is saved privately for review.</p>
      <p className="text-xs faint mt-3 break-all">Reference: {receipt}</p>
      <p className="text-sm mt-3">If you included an email, we can contact you for clarification. We cannot promise a reply or a release date for every suggestion.</p>
      <Link href="/learn/" className="btn btn-brand mt-5">Continue studying</Link>
      <button className="btn ml-2 mt-5" onClick={() => { setReceipt(''); requestId.current = ''; }}>Send another</button>
    </div>
  );

  return (
    <form onSubmit={submit} onChange={() => { requestId.current = ''; setError(''); }} className="card p-5 sm:p-7 mt-6 space-y-5">
      <fieldset disabled={busy} className="space-y-5">
        <div>
          <label htmlFor="request-title" className="block text-sm font-bold mb-1">{feature ? 'What would you like us to add?' : 'What needs attention?'}</label>
          <input id="request-title" name="title" required minLength={5} maxLength={100} className={inputClass} style={border}
            placeholder={feature ? 'For example: filter revision topics by exam' : 'For example: percentage solution skips a step'} />
        </div>
        <div>
          <label htmlFor="request-message" className="block text-sm font-bold mb-1">{feature ? 'How would this help your preparation?' : 'Tell us what happened'}</label>
          <p id="message-help" className="text-xs muted mb-2">{feature
            ? 'Describe the problem you face, what you want to do, and how you manage it today.'
            : 'For a bug, include the steps and what you expected. For a correction, include the question ID and your working.'} Use 20–3,000 characters.</p>
          <textarea id="request-message" name="message" required minLength={20} maxLength={3000} rows={6} aria-describedby="message-help"
            className={inputClass} style={border} />
        </div>
        <div className="grid sm:grid-cols-2 gap-4">
          <div>
            <label htmlFor="request-exam" className="block text-sm font-bold mb-1">Your exam <span className="font-normal muted">(optional)</span></label>
            <select id="request-exam" name="exam" className={inputClass} style={border} defaultValue="">
              <option value="">Choose an exam</option>
              {['SSC CGL', 'SSC CHSL', 'SSC CPO', 'SSC GD', 'SSC MTS', 'IBPS PO', 'IBPS Clerk', 'RRB NTPC', 'RRB Group D', 'CAT', 'Other'].map(exam => <option key={exam}>{exam}</option>)}
            </select>
          </div>
          <div>
            <label htmlFor="request-email" className="block text-sm font-bold mb-1">Reply email <span className="font-normal muted">(optional)</span></label>
            <input id="request-email" name="email" type="email" maxLength={254} autoComplete="email" className={inputClass} style={border} placeholder="Only if you want us to contact you" />
          </div>
        </div>
        <div>
          <label htmlFor="request-page" className="block text-sm font-bold mb-1">Related page URL <span className="font-normal muted">(optional)</span></label>
          <input id="request-page" name="page" type="url" maxLength={500} className={inputClass} style={border} placeholder="https://examshortcut.in/…" />
        </div>
        <div hidden aria-hidden="true"><label htmlFor="request-website">Leave this blank</label><input id="request-website" name="website" tabIndex={-1} autoComplete="off" /></div>
        <p className="text-xs muted">No login needed. Submissions are private. Please do not include passwords, admit cards, identity documents or other sensitive information. See our <Link className="underline" href="/privacy/">privacy policy</Link>.</p>
        <button type="submit" className="btn btn-brand" disabled={busy}>{busy ? 'Saving…' : feature ? 'Submit feature request' : 'Send feedback'}</button>
      </fieldset>
      {error && <p role="alert" className="text-sm" style={{ color: 'var(--bad, #b91c1c)' }}>{error}</p>}
      <p className="text-xs faint">Prefer email? Write to <a className="underline" href="mailto:singirikonda3@gmail.com">singirikonda3@gmail.com</a>.</p>
    </form>
  );
}
