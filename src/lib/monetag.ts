// Issued by the verified ExamShortcut Vignette zone on 16 October 2026.
export const MONETAG_VIGNETTE_ZONE = '12047445';
export const MONETAG_VIGNETTE_SRC = 'https://n6wxm.com/vignette.min.js';

export const monetagBootstrap = `
(function () {
  if (!['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
  function loadAds() {
    if (document.getElementById('monetag-vignette-sdk')) return;
    var script = document.createElement('script');
    script.id = 'monetag-vignette-sdk';
    script.dataset.zone = '${MONETAG_VIGNETTE_ZONE}';
    script.dataset.loadState = 'loading';
    script.onload = function () { script.dataset.loadState = 'loaded'; };
    script.onerror = function () { script.dataset.loadState = 'error'; };
    script.async = true;
    script.src = '${MONETAG_VIGNETTE_SRC}';
    (document.body || document.documentElement).appendChild(script);
  }
  function scheduleAds() {
    if (window.requestIdleCallback) window.requestIdleCallback(loadAds);
    else window.setTimeout(loadAds, 1);
  }
  if (document.readyState === 'complete') scheduleAds();
  else window.addEventListener('load', scheduleAds, { once: true });
})();`;
