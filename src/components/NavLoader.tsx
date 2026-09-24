'use client';
import { useEffect, useState } from 'react';
import { usePathname } from 'next/navigation';

/* Instant click feedback: a centred spinner from the moment an internal link is
   clicked until the new route renders. Capture phase, because next/link calls
   preventDefault in its own handler before a bubbling listener would run. */
export function NavLoader() {
  const path = usePathname();
  const [on, setOn] = useState(false);

  useEffect(() => { setOn(false); }, [path]);

  useEffect(() => {
    let timer: ReturnType<typeof setTimeout> | undefined;
    const onClick = (e: MouseEvent) => {
      if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      const a = (e.target as Element | null)?.closest?.('a');
      if (!a || !a.href || (a.target && a.target !== '_self') || a.hasAttribute('download')) return;
      const url = new URL(a.href, location.href);
      if (url.origin !== location.origin || url.pathname === location.pathname) return;
      setOn(true);
      clearTimeout(timer);
      timer = setTimeout(() => setOn(false), 15000); // never strand the spinner
    };
    document.addEventListener('click', onClick, true);
    return () => { document.removeEventListener('click', onClick, true); clearTimeout(timer); };
  }, []);

  if (!on) return null;
  return (
    <div className="nav-loader" role="status" aria-live="polite">
      <div className="nav-loader-bar" />
      <div className="nav-loader-spin"><span className="sr-only">Loading…</span></div>
    </div>
  );
}
