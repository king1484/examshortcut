'use client';

import { useEffect, useRef, useState } from 'react';
import { usePathname } from 'next/navigation';

// A fresh, isolated document keeps vendor globals and DOM changes away from
// authentication, form inputs and the application when routes change.
function BannerSlot() {
  const slot = useRef<HTMLDivElement>(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const element = slot.current;
    if (!element || !['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;

    const observer = 'IntersectionObserver' in window
      ? new IntersectionObserver((entries) => {
        if (entries.some((entry) => entry.isIntersecting)) {
          setReady(true);
          observer?.disconnect();
        }
      }, { rootMargin: '100px' })
      : null;
    if (observer) observer.observe(element);
    else setReady(true);
    return () => observer?.disconnect();
  }, []);

  return (
    <aside aria-label="Advertisement" className="my-5 mx-auto print:hidden"
      style={{ width: 300, maxWidth: '100%' }}>
      <p className="text-[11px] faint text-center mb-2">Advertisement</p>
      <div ref={slot} data-adsterra-zone="31786624" style={{ width: 300, height: 250, maxWidth: '100%' }}>
        {ready && <iframe title="Adsterra display advertisement" src="/advertising/display.html"
          width="300" height="250" scrolling="no" referrerPolicy="origin"
          sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox"
          style={{ border: 0, display: 'block', maxWidth: '100%' }} />}
      </div>
    </aside>
  );
}

export function DisplayBanner() {
  const pathname = usePathname();
  return <BannerSlot key={pathname} />;
}
