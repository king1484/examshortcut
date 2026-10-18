'use client';

import { useEffect, useState } from 'react';
import Script from 'next/script';

// Adsterra support configured unit 31792394 for interstitials only.
// This is a single root-layout script; route changes must not reload it.
export function AdsterraInterstitial() {
  const [production, setProduction] = useState(false);
  useEffect(() => {
    setProduction(['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname));
  }, []);

  return <>
    <span hidden data-adsterra-interstitial="31792394" />
    {production && <Script id="adsterra-interstitial" data-cfasync="false"
      src="https://bauval.org/14/fddeed3afc5be59e6049e19c4d7ffb40" strategy="afterInteractive" />}
  </>;
}
