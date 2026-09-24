'use client';
import { useEffect, useRef } from 'react';

/* Browser-rendered KaTeX for formula-dense pages. Server-rendered KaTeX costs
   ~4 KB of markup per formula, and Next serialises it a second time into the
   RSC payload — the full formula sheet came out at 12 MB and its header-link
   prefetch stalled navigation site-wide. Here only the TeX source ships; each
   formula renders when it nears the viewport, and everything renders before print. */

type Katex = typeof import('katex').default;
let katex: Katex | null = null;
let katexLoad: Promise<Katex> | null = null;
const loadKatex = () => (katexLoad ??= import('katex').then((m) => (katex = m.default)));

type Job = { tex: string; display: boolean };
const pending = new Map<HTMLElement, Job>();
let io: IntersectionObserver | null = null;

function render(el: HTMLElement) {
  const job = pending.get(el);
  if (!job || !katex) return;
  pending.delete(el);
  io?.unobserve(el);
  el.innerHTML = katex.renderToString(job.tex, { displayMode: job.display, throwOnError: false, output: 'html' });
  el.classList.remove('ktex-pending');
}

function observer() {
  if (io) return io;
  io = new IntersectionObserver(
    (entries) => {
      for (const e of entries) if (e.isIntersecting) render(e.target as HTMLElement);
    },
    { rootMargin: '800px 0px' }
  );
  window.addEventListener('beforeprint', () => { for (const el of [...pending.keys()]) render(el); });
  return io;
}

export function LazyTex({ tex, display = false }: { tex: string; display?: boolean }) {
  const ref = useRef<HTMLSpanElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    pending.set(el, { tex, display });
    loadKatex().then(() => { if (pending.has(el)) observer().observe(el); });
    return () => { pending.delete(el); io?.unobserve(el); };
  }, [tex, display]);
  return (
    <span ref={ref} className={`ktex ktex-pending ${display ? 'block' : ''}`} aria-label={tex}>
      {tex}
    </span>
  );
}
