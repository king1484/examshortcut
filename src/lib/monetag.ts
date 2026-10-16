// Issued for the existing "Nice tag" MultiTag on 16 October 2026.
// Its four child zones are 12048480–12048483; the embed uses the bundle ID.
export const MONETAG_MULTITAG_ZONE = '296822';
export const MONETAG_MULTITAG_SRC = 'https://quge5.com/88/tag.min.js';

export const monetagBootstrap = `
(function () {
  if (!['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
  if (document.getElementById('monetag-multitag-sdk')) return;
  var script = document.createElement('script');
  script.id = 'monetag-multitag-sdk';
  script.setAttribute('data-cfasync', 'false');
  script.dataset.zone = '${MONETAG_MULTITAG_ZONE}';
  script.async = true;
  script.src = '${MONETAG_MULTITAG_SRC}';
  script.dataset.loadState = 'loading';
  script.onload = function () { script.dataset.loadState = 'loaded'; };
  script.onerror = function () { script.dataset.loadState = 'error'; };
  document.head.appendChild(script);
})();`;
