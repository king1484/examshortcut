'use client';

import { usePathname } from 'next/navigation';
import { isPublicAdPage } from '@/lib/advertising';
import { monetagBootstrap } from '@/lib/monetag';

export function Monetag() {
  const pathname = usePathname() || '';
  if (!isPublicAdPage(pathname)) return null;
  // Run the issued tag from the head to match Monetag's installation instructions.
  // Its documented Cloudflare attribute keeps Rocket Loader from deferring it.
  return <script data-cfasync="false" id="monetag-vignette-bootstrap" dangerouslySetInnerHTML={{ __html: monetagBootstrap }} />;
}
