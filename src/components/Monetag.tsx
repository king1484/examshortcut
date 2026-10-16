'use client';

import { usePathname } from 'next/navigation';
import { isPublicAdPage } from '@/lib/advertising';
import { monetagBootstrap } from '@/lib/monetag';

export function Monetag() {
  const pathname = usePathname() || '';
  if (!isPublicAdPage(pathname)) return null;
  // Keep the vendor tag in the exported head so installation scanners can find it.
  // The bootstrap itself waits for page load and idle time before requesting ads.
  return <script id="monetag-vignette-bootstrap" dangerouslySetInnerHTML={{ __html: monetagBootstrap }} />;
}
