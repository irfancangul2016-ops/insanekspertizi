const CACHE_NAME = 'kozmik-app-v1';
const urlsToCache = [
  '/',
  '/static/styles.css',
  '/static/manifest.json'
];

// Yükleme Anı (Install)
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// İstek Yakalama (Fetch)
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Cache'de varsa oradan ver, yoksa internetten çek
        return response || fetch(event.request);
      })
  );
});