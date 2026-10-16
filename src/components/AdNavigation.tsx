'use client';

import { usePathname } from 'next/navigation';
import { useEffect, useRef } from 'react';
import { isPublicAdPage } from '@/lib/advertising';

export function AdNavigation() {
  const pathname = usePathname() || '';
  const firstPath = useRef(pathname);
  const eligible = isPublicAdPage(pathname);

  useEffect(() => {
    if (!['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
    // Ad SDKs mutate the document and have no shared SPA reset API.
    // A fresh document clears the ad SDK before entering an account or form page.
    if (pathname !== firstPath.current && (eligible || isPublicAdPage(firstPath.current))) {
      location.replace(location.href);
      return;
    }
    function navigate(event: MouseEvent) {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      const link = event.target instanceof Element ? event.target.closest('a[href]') : null;
      if (!(link instanceof HTMLAnchorElement) || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
      const destination = new URL(link.href, location.href);
      if (destination.origin !== location.origin || destination.pathname === pathname) return;
      if (!eligible && !isPublicAdPage(destination.pathname)) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      location.assign(destination.href);
    }
    document.addEventListener('click', navigate, true);
    return () => document.removeEventListener('click', navigate, true);
  }, [pathname, eligible]);

  return null;
}
