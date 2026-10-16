'use client';

import Script from 'next/script';
import { usePathname } from 'next/navigation';
import { isPublicAdPage } from '@/lib/advertising';
import { monetagBootstrap } from '@/lib/monetag';

export function Monetag() {
  const pathname = usePathname() || '';
  if (!isPublicAdPage(pathname)) return null;
  return <Script id="monetag-vignette-bootstrap" strategy="lazyOnload">{monetagBootstrap}</Script>;
}
