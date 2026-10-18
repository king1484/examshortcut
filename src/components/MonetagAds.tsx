'use client';

import { useEffect } from 'react';
import { usePathname } from 'next/navigation';
import { isPublicAdPage } from '@/lib/advertising';

const SDK_ID = 'monetag-onclick-sdk';

export function MonetagAds() {
  const pathname = usePathname();

  useEffect(() => {
    // The SDK installs document listeners. Enter protected pages in a fresh
    // document rather than carrying those listeners into Google login or tests.
    const protectNavigation = (event: MouseEvent) => {
      if (!document.getElementById(SDK_ID) || !(event.target instanceof Element)) return;
      const link = event.target.closest<HTMLAnchorElement>('a[href]');
      if (!link || link.target === '_blank' || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      const url = new URL(link.href, window.location.href);
      if (url.origin !== window.location.origin || isPublicAdPage(url.pathname)) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      window.location.assign(url.href);
    };
    window.addEventListener('click', protectNavigation, true);
    return () => window.removeEventListener('click', protectNavigation, true);
  }, []);

  useEffect(() => {
    if (window.location.hostname !== 'examshortcut.in' || !pathname) return;
    const existing = document.getElementById(SDK_ID);
    if (!isPublicAdPage(pathname)) {
      // Covers programmatic client navigation as well as ordinary links.
      if (existing) window.location.reload();
      return;
    }
    if (existing) return;
    const script = document.createElement('script');
    script.id = SDK_ID;
    script.dataset.zone = '12061370';
    script.src = 'https://al5sm.com/tag.min.js';
    script.async = true;
    document.head.appendChild(script);
  }, [pathname]);

  return null;
}
