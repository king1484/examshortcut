'use client';

import { useEffect, useRef, useState } from 'react';
import { usePathname } from 'next/navigation';
import { ADCASH_ZONE_ID, ADCASH_LIBRARY_URL, ADCASH_BANNER_SCRIPT, canRequestAdcash } from '@/lib/adcash';
import { isPublicAdPage } from '@/lib/advertising';

let library: Promise<void> | null = null;

function loadLibrary(): Promise<void> {
  if (!library) {
    library = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.id = 'aclib';
      script.type = 'text/javascript';
      script.src = ADCASH_LIBRARY_URL;
      script.async = true;
      script.onload = () => resolve();
      script.onerror = () => {
        script.remove();
        library = null;
        reject(new Error('Display advertising unavailable'));
      };
      document.head.appendChild(script);
    });
  }
  return library;
}

export function DisplayBanner() {
  const pathname = usePathname() || '';
  const slot = useRef<HTMLDivElement>(null);
  const [unavailable, setUnavailable] = useState(false);

  useEffect(() => {
    const element = slot.current;
    if (!element || !canRequestAdcash(location.hostname, pathname)) return;
    let active = true;
    let requested = false;
    setUnavailable(false);

    const requestBanner = () => {
      if (requested) return;
      requested = true;
      observer?.disconnect();
      // The issued runBanner script must be a child of its intended slot.
      // A separate iframe wrapper requires provider approval, so use its normal integration.
      loadLibrary().then(() => {
        if (!active || !element.isConnected) return;
        const script = document.createElement('script');
        script.type = 'text/javascript';
        script.textContent = ADCASH_BANNER_SCRIPT;
        element.appendChild(script);
      }).catch(() => { if (active) setUnavailable(true); });
    };

    const observer = 'IntersectionObserver' in window
      ? new IntersectionObserver((entries) => {
        if (entries.some((entry) => entry.isIntersecting)) requestBanner();
      }, { rootMargin: '200px' })
      : null;
    if (observer) observer.observe(element);
    else requestBanner();

    return () => {
      active = false;
      observer?.disconnect();
      element.replaceChildren();
    };
  }, [pathname]);

  if (!isPublicAdPage(pathname)) return null;
  return (
    <aside aria-label="Advertisement" className="my-10 mx-auto print:hidden" hidden={unavailable}
      style={{ width: 300, maxWidth: '100%' }}>
      <p className="text-[11px] faint text-center mb-2">Advertisement</p>
      <div key={pathname} ref={slot} data-adcash-zone={ADCASH_ZONE_ID}
        style={{ width: 300, height: 250, maxWidth: '100%' }} />
    </aside>
  );
}
