'use client';
import { useEffect } from 'react';

export function SwRegister() {
  useEffect(() => {
    if (process.env.NODE_ENV !== 'production') return;
    // /sw.js is Monetag's ownership file. Keep the app's offline worker separate.
    if ('serviceWorker' in navigator) navigator.serviceWorker.register('/offline-sw.js').catch(() => {});
  }, []);
  return null;
}
