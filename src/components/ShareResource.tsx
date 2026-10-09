'use client';
import { useState } from 'react';

export function ShareResource({ title, path }: { title: string; path: string }) {
  const [status, setStatus] = useState('');
  const url = `https://examshortcut.in${path}`;
  const text = `${title} — free on ExamShortcut`;
  async function copy() {
    try { await navigator.clipboard.writeText(url); setStatus('Link copied'); }
    catch { setStatus(`Copy this link: ${url}`); }
  }
  async function share() {
    if (!navigator.share) { await copy(); return; }
    try { await navigator.share({ title, text, url }); }
    catch { /* Closing the native share sheet needs no error message. */ }
  }
  return (
    <div className="card p-4 mt-6 flex flex-wrap gap-2 items-center resource-share">
      <p className="font-semibold text-sm mr-auto">Help a study partner find this</p>
      <button className="btn" onClick={share}>Share</button>
      <a className="btn" href={`https://wa.me/?text=${encodeURIComponent(`${text}\n${url}`)}`} target="_blank" rel="noopener noreferrer">WhatsApp</a>
      <a className="btn" href={`https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`} target="_blank" rel="noopener noreferrer">Telegram</a>
      <button className="btn" onClick={copy}>Copy link</button>
      <p className="text-xs muted w-full break-words" role="status">{status}</p>
    </div>
  );
}
