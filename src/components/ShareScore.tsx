'use client';
import { useState } from 'react';

interface Props {
  title: string;
  score: number;
  max: number;
  accuracy: number;
  correct: number;
  wrong: number;
  skipped: number;
  url: string; // absolute URL of the paper, so a friend can take the same test
}

const num = (n: number) => n.toFixed(2).replace(/\.00$/, '').replace(/(\.\d)0$/, '$1');

/** Draws a 1080x1080 score card. Colours are fixed (not theme vars) so the image looks the same everywhere. */
function drawCard({ title, score, max, accuracy, correct, wrong, skipped }: Props): Promise<Blob | null> {
  const c = document.createElement('canvas');
  c.width = 1080; c.height = 1080;
  const g = c.getContext('2d');
  if (!g) return Promise.resolve(null);
  const font = 'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif';

  g.fillStyle = '#111318'; g.fillRect(0, 0, 1080, 1080);
  g.fillStyle = '#e8590c'; g.fillRect(0, 0, 1080, 18);

  g.fillStyle = '#e8590c'; g.font = `800 44px ${font}`; g.textAlign = 'left';
  g.fillText('ExamShortcut', 80, 130);

  g.fillStyle = '#b4bac6'; g.font = `600 36px ${font}`;
  let t = title;
  while (g.measureText(t).width > 920 && t.length > 4) t = t.slice(0, -2);
  if (t !== title) t = t.trimEnd() + '…';
  g.fillText(t, 80, 215);

  g.fillStyle = '#858c9a'; g.font = `600 34px ${font}`;
  g.fillText('MY SCORE', 80, 400);
  g.fillStyle = '#eceef2'; g.font = `800 210px ${font}`;
  g.fillText(num(score), 80, 590);
  const w = g.measureText(num(score)).width;
  g.fillStyle = '#858c9a'; g.font = `700 80px ${font}`;
  g.fillText(`/ ${max}`, 100 + w, 590);

  const stats: [string, string, string][] = [
    ['Accuracy', `${accuracy}%`, '#eceef2'],
    ['Correct', String(correct), '#4ade80'],
    ['Wrong', String(wrong), '#f87171'],
    ['Skipped', String(skipped), '#b4bac6'],
  ];
  stats.forEach(([k, v, col], i) => {
    const x = 80 + i * 235;
    g.fillStyle = '#191c23'; g.fillRect(x, 690, 215, 170);
    g.fillStyle = '#858c9a'; g.font = `600 28px ${font}`; g.fillText(k, x + 24, 740);
    g.fillStyle = col; g.font = `800 66px ${font}`; g.fillText(v, x + 24, 825);
  });

  g.fillStyle = '#eceef2'; g.font = `700 42px ${font}`;
  g.fillText('Can you beat it? Take the same test free:', 80, 960);
  g.fillStyle = '#e8590c'; g.font = `800 48px ${font}`;
  g.fillText('examshortcut.in', 80, 1025);

  return new Promise((res) => c.toBlob((b) => res(b), 'image/png'));
}

export function ShareScore(props: Props) {
  const [busy, setBusy] = useState(false);
  const text = `I scored ${num(props.score)}/${props.max} (${props.accuracy}% accuracy) on ${props.title} at ExamShortcut. Can you beat it? Take the same test free: ${props.url}`;
  const wa = `https://wa.me/?text=${encodeURIComponent(text)}`;
  const tg = `https://t.me/share/url?url=${encodeURIComponent(props.url)}&text=${encodeURIComponent(text.replace(props.url, '').trim())}`;

  async function share() {
    setBusy(true);
    try {
      const blob = await drawCard(props);
      const file = blob ? new File([blob], 'my-score.png', { type: 'image/png' }) : null;
      if (file && navigator.canShare?.({ files: [file] })) {
        await navigator.share({ files: [file], text });
      } else if (navigator.share) {
        await navigator.share({ text });
      } else {
        window.open(wa, '_blank', 'noopener');
      }
    } catch { /* user cancelled the share sheet */ }
    setBusy(false);
  }

  async function save() {
    setBusy(true);
    const blob = await drawCard(props);
    if (blob) {
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'my-score.png';
      a.click();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
    }
    setBusy(false);
  }

  return (
    <div className="card p-4 mt-4 flex flex-wrap items-center gap-2">
      <p className="text-sm font-bold mr-auto">Challenge a friend to beat {num(props.score)}</p>
      <button className="btn btn-brand" onClick={share} disabled={busy}>Share score</button>
      <a className="btn" href={wa} target="_blank" rel="noopener">WhatsApp</a>
      <a className="btn" href={tg} target="_blank" rel="noopener">Telegram</a>
      <button className="btn" onClick={save} disabled={busy}>Save image</button>
    </div>
  );
}
