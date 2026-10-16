'use client';

import Script from 'next/script';
import { usePathname } from 'next/navigation';
import { useEffect, useRef } from 'react';
import { infolinksBootstrap, isInfolinksPage } from '@/lib/infolinks';

export function Infolinks() {
  const pathname = usePathname() || '/';
  const firstPath = useRef(pathname);
  const eligible = isInfolinksPage(pathname);

  useEffect(() => {
    if (!['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
    // The vendor mutates the page DOM and has no documented SPA reset API.
    // A fresh document removes its ads/listeners before entering a form or account page.
    if (pathname !== firstPath.current && (eligible || isInfolinksPage(firstPath.current))) {
      location.replace(location.href);
      return;
    }
    function navigate(event: MouseEvent) {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      const link = event.target instanceof Element ? event.target.closest('a[href]') : null;
      if (!(link instanceof HTMLAnchorElement) || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
      const destination = new URL(link.href, location.href);
      if (destination.origin !== location.origin || destination.pathname === pathname) return;
      if (!eligible && !isInfolinksPage(destination.pathname)) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      location.assign(destination.href);
    }
    document.addEventListener('click', navigate, true);
    return () => document.removeEventListener('click', navigate, true);
  }, [pathname, eligible]);

  if (!eligible) return null;
  // Wait for hydration and browser idle so text ads cannot disturb initial rendering.
  return <Script id="infolinks-bootstrap" strategy="lazyOnload">{infolinksBootstrap}</Script>;
}

export function InfolinksTextBoundary({ mode }: { mode: 'on' | 'off' }) {
  // Official InText exclusions: https://www.infolinks.com/support/products/how-do-i-restrict-intext-ads-from-certain-areas/
  return <span hidden aria-hidden="true" dangerouslySetInnerHTML={{ __html: `<!--INFOLINKS_${mode.toUpperCase()}-->` }} />;
}
