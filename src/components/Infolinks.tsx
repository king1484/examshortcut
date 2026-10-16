'use client';

import Script from 'next/script';
import { usePathname } from 'next/navigation';
import { infolinksBootstrap } from '@/lib/infolinks';
import { isPublicAdPage } from '@/lib/advertising';

export function Infolinks() {
  const pathname = usePathname() || '';
  if (!isPublicAdPage(pathname)) return null;
  // Wait for hydration and browser idle so text ads cannot disturb initial rendering.
  return <Script id="infolinks-bootstrap" strategy="lazyOnload">{infolinksBootstrap}</Script>;
}

export function InfolinksTextBoundary({ mode }: { mode: 'on' | 'off' }) {
  // Official InText exclusions: https://www.infolinks.com/support/products/how-do-i-restrict-intext-ads-from-certain-areas/
  return <span hidden aria-hidden="true" dangerouslySetInnerHTML={{ __html: `<!--INFOLINKS_${mode.toUpperCase()}-->` }} />;
}
