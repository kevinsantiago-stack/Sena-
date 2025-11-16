const CACHE_NAME = 'mi-app-v1';
const URLS_CACHE = [
  '/',
  '/index.html',
  '/main.js',
  '/styles.css'
];

// Instalar Service Worker
self.addEventListener('install', event => {
  console.log('Service Worker: Instalando...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Service Worker: Cacheando archivos');
        return cache.addAll(URLS_CACHE);
      })
  );
});

// Interceptar peticiones de red
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Si está en cache, devolverlo
        if (response) {
          return response;
        }
        // Si no, ir a la red
        return fetch(event.request);
      })
  );
});