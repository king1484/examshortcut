'use client';
import { useEffect } from 'react';

export function SwRegister() {
  useEffect(() => {
    if (process.env.NODE_ENV !== 'production') return;
    // One root registration imports both the offline worker and Monetag's push code.
    // Registering /offline-sw.js separately would replace the same root scope.
    if ('serviceWorker' in navigator) navigator.serviceWorker.register('/sw.js').catch(() => {});
  }, []);
  return null;
}
