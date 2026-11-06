'use client';

import { createContext, useContext, useEffect, useRef, useState, type ReactNode } from 'react';
import { usePathname } from 'next/navigation';
import { ADSTERRA_ENABLED, ADSTERRA_CATEGORY_CONFIRMATION, ADSTERRA_SERVE_AFTER, ADSTERRA_FRAME_ORIGIN, ADSTERRA_UNITS,
  canServeAdsterra, chooseAdsterraUnit, isAdsterraReadingPage, type AdsterraUnit } from '@/lib/adsterra';

const AdPreferences = createContext({ hidden: false, ready: false, hide: () => {} });
const HIDE_KEY = 'es-hide-ads-this-session';

export function AdsterraProvider({ children }: { children: ReactNode }) {
  const [hidden, setHidden] = useState(false);
  const [ready, setReady] = useState(false);
  useEffect(() => {
    try { setHidden(sessionStorage.getItem(HIDE_KEY) === '1'); } catch { /* Storage may be unavailable. */ }
    const delay = process.env.NODE_ENV === 'development' ? 0 : Math.max(0, Date.parse(ADSTERRA_SERVE_AFTER) - Date.now());
    const timer = window.setTimeout(() => setReady(true), delay);
    return () => window.clearTimeout(timer);
  }, []);
  const hide = () => {
    setHidden(true);
    try { sessionStorage.setItem(HIDE_KEY, '1'); } catch { /* The current page still hides ads. */ }
  };
  return <AdPreferences.Provider value={{ hidden, ready, hide }}>{children}</AdPreferences.Provider>;
}

export function AdsterraPageEnd() {
  const pathname = usePathname();
  return pathname === '/' ? null : <AdsterraBanner />;
}

export function AdsterraBanner({ position = 'reading' }: { position?: 'reading' | 'article' }) {
  const pathname = usePathname() || '';
  const preferences = useContext(AdPreferences);
  const enabled = ADSTERRA_ENABLED && Boolean(ADSTERRA_CATEGORY_CONFIRMATION);
  // Development preview reserves real sizes but never requests an advertisement.
  const preview = process.env.NODE_ENV === 'development';
  if ((!enabled && !preview) || preferences.hidden || !isAdsterraReadingPage(pathname)) return null;
  return <BannerSlot key={`${pathname}:${position}`} position={position} preview={preview} />;
}

function BannerSlot({ position, preview }: { position: 'reading' | 'article'; preview: boolean }) {
  const { ready, hide } = useContext(AdPreferences);
  const slot = useRef<HTMLElement>(null);
  const [unit, setUnit] = useState<AdsterraUnit | null>(null);
  const [availableWidth, setAvailableWidth] = useState(0);
  const [visible, setVisible] = useState(false);
  const [idle, setIdle] = useState(false);
  useEffect(() => {
    const element = slot.current;
    if (!element) return;
    const resize = new ResizeObserver(entries => {
      setAvailableWidth(entries[0].contentRect.width);
      // Once loaded, keep the same creative; resizing must not manufacture impressions.
      setUnit(previous => previous ?? chooseAdsterraUnit(entries[0].contentRect.width, position));
    });
    const observer = new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) { setVisible(true); observer.disconnect(); }
    }, { rootMargin: '100px' });
    resize.observe(element); observer.observe(element);
    const idleCallback = () => setIdle(true);
    const hasIdleCallback = typeof window.requestIdleCallback === 'function';
    const handle = hasIdleCallback ? window.requestIdleCallback(idleCallback, { timeout: 3000 }) : window.setTimeout(idleCallback, 1500);
    return () => {
      resize.disconnect(); observer.disconnect();
      if (hasIdleCallback) window.cancelIdleCallback(handle); else window.clearTimeout(handle);
    };
  }, [position]);
  const banner = unit ? ADSTERRA_UNITS[unit] : null;
  const load = ready && idle && visible && unit && !preview && canServeAdsterra(location.hostname);
  return <aside ref={slot} className={`adsterra-placement adsterra-${position}`} aria-label="Advertisement">
    <div className="adsterra-panel" style={banner && availableWidth < banner.width ? { display: 'none' } : undefined}>
      <div className="adsterra-caption"><span>Advertisement{preview ? ' · layout preview' : ''}</span><button type="button" onClick={hide}>Hide ads while studying</button></div>
      <div className="adsterra-space" style={banner ? { maxWidth: banner.width, minHeight: banner.height } : undefined}>
        {load && banner && <iframe key={unit} title="Advertisement from Adsterra"
          src={`${ADSTERRA_FRAME_ORIGIN}/advertising/display?unit=${unit}`}
          width={banner.width} height={banner.height} scrolling="no" referrerPolicy="origin"
          sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"
          allow="autoplay 'none'; camera 'none'; microphone 'none'; geolocation 'none'" />}
      </div>
    </div>
  </aside>;
}
