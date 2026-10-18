'use client';

import { useEffect, useRef, useState } from 'react';
import { usePathname } from 'next/navigation';

const BANNERS = {
  '300x250': { zone: '31786624', width: 300, height: 250 },
  '468x60': { zone: '31792395', width: 468, height: 60 },
  '160x300': { zone: '31792396', width: 160, height: 300 },
  '160x600': { zone: '31792397', width: 160, height: 600 },
  '320x50': { zone: '31792398', width: 320, height: 50 },
  '728x90': { zone: '31792399', width: 728, height: 90 },
} as const;

function useVisibleAd(media: string) {
  const slot = useRef<HTMLDivElement>(null);
  const [ready, setReady] = useState(false);
  useEffect(() => {
    const element = slot.current;
    if (!element || !['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
    const screen = window.matchMedia(media);
    let inView = false;
    const update = () => setReady(screen.matches && inView);
    const observer = new IntersectionObserver((entries) => {
      inView = entries.some((entry) => entry.isIntersecting);
      if (inView && screen.matches) {
        setReady(true);
        // No refresh when visitors scroll away and return to a loaded slot.
        observer.disconnect();
      }
    }, { rootMargin: '100px' });
    screen.addEventListener('change', update);
    observer.observe(element);
    return () => {
      observer.disconnect();
      screen.removeEventListener('change', update);
    };
  }, [media]);
  return { slot, ready };
}

// Each format has its own document: vendor globals cannot collide or reach
// authentication, form inputs or the application DOM.
function BannerSlot({ size, media, className }: {
  size: keyof typeof BANNERS; media: string; className: string;
}) {
  const { zone, width, height } = BANNERS[size];
  const { slot, ready } = useVisibleAd(media);
  return (
    <aside aria-label="Advertisement" className={`ad-placement ${className}`}
      style={{ width, maxWidth: '100%' }}>
      <p className="text-[11px] faint text-center mb-2">Advertisement</p>
      <div ref={slot} data-adsterra-zone={zone} style={{ width, height, maxWidth: '100%' }}>
        {ready && <iframe title={`Adsterra ${size} display advertisement`}
          src={`/advertising/display.html?size=${size}`} width={width} height={height}
          scrolling="no" referrerPolicy="origin"
          sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox"
          style={{ border: 0, display: 'block', maxWidth: '100%' }} />}
      </div>
    </aside>
  );
}

export function DisplayBanner({ position = 'top' }: { position?: 'top' | 'bottom' | 'left' | 'right' }) {
  const pathname = usePathname();
  if (position === 'left' || position === 'right') {
    return <BannerSlot key={pathname} size={position === 'left' ? '160x300' : '160x600'}
      media="(min-width: 1600px)" className="ad-rail" />;
  }
  return <div key={pathname} className="ad-horizontal">
    {position === 'top' ? <>
      <BannerSlot size="728x90" media="(min-width: 768px)" className="ad-top-desktop" />
      <BannerSlot size="320x50" media="(max-width: 767px)" className="ad-top-mobile" />
    </> : <>
      <BannerSlot size="468x60" media="(min-width: 600px)" className="ad-bottom-desktop" />
      <BannerSlot size="300x250" media="(max-width: 599px)" className="ad-bottom-mobile" />
    </>}
  </div>;
}

function NativeSlot() {
  const { slot, ready } = useVisibleAd('all');
  const frame = useRef<HTMLIFrameElement>(null);
  const [height, setHeight] = useState(160);
  useEffect(() => {
    const resize = (event: MessageEvent) => {
      if (event.source !== frame.current?.contentWindow || event.data?.type !== 'examshortcut-native-height') return;
      const value = event.data.height;
      if (typeof value === 'number' && Number.isFinite(value)) {
        setHeight(Math.max(100, Math.min(1800, Math.ceil(value))));
      }
    };
    window.addEventListener('message', resize);
    return () => window.removeEventListener('message', resize);
  }, []);
  return <aside aria-label="Sponsored advertisements" className="ad-placement ad-native">
    <p className="text-[11px] faint text-center mb-2">Advertisement</p>
    <div ref={slot} data-adsterra-zone="31792392" style={{ minHeight: height }}>
      {ready && <iframe ref={frame} title="Adsterra native banner advertisements"
        src="/advertising/native.html" width="100%" height={height} scrolling="no"
        referrerPolicy="origin" sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox"
        style={{ border: 0, display: 'block' }} />}
    </div>
  </aside>;
}

export function NativeBanner() {
  const pathname = usePathname();
  return <NativeSlot key={pathname} />;
}

export function SponsoredOffers() {
  return <p className="ad-sponsored text-sm faint text-center mb-6">
    Advertisement · <a href="https://araplhn.org/4/2030aeb2a6b6a453f627153d8cb02b50"
      data-adsterra-smartlink="31792393" target="_blank" rel="sponsored noopener noreferrer"
      className="underline">Sponsored offers</a>
  </p>;
}
