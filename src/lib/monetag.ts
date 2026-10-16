// Issued by the verified ExamShortcut Vignette zone on 16 October 2026.
export const MONETAG_VIGNETTE_ZONE = '12047445';
export const MONETAG_VIGNETTE_SRC = 'https://n6wxm.com/vignette.min.js';

// Preserve the issued embed verbatim for Monetag's installation detector.
export const monetagIssuedTag = `(function(s){s.dataset.zone='${MONETAG_VIGNETTE_ZONE}',s.src='${MONETAG_VIGNETTE_SRC}'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))`;

export const monetagBootstrap = `
(function () {
  if (!['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
  function loadAds() {
    if (document.getElementById('monetag-vignette-sdk')) return;
    ${monetagIssuedTag};
    var script = document.querySelector('script[data-zone="${MONETAG_VIGNETTE_ZONE}"][src="${MONETAG_VIGNETTE_SRC}"]');
    script.id = 'monetag-vignette-sdk';
    script.dataset.loadState = 'loading';
    script.onload = function () { script.dataset.loadState = 'loaded'; };
    script.onerror = function () { script.dataset.loadState = 'error'; };
  }
  function scheduleAds() {
    if (window.requestIdleCallback) window.requestIdleCallback(loadAds);
    else window.setTimeout(loadAds, 1);
  }
  if (document.readyState === 'complete') scheduleAds();
  else window.addEventListener('load', scheduleAds, { once: true });
})();`;
