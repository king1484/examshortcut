// Keep offline handlers if the advertising worker cannot load.
importScripts('/offline-sw.js');

if (['examshortcut.in', 'www.examshortcut.in'].includes(self.location.hostname)) try {
  self.options = {
      "domain": "3nbf4.com",
      "zoneId": 12048483
  }
  self.lary = ""
  importScripts('https://3nbf4.com/act/files/service-worker.min.js?r=sw')
} catch (error) {
  console.warn('Monetag push worker could not load; offline support remains available.', error);
}
