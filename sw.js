// Service Worker - BioAge PWA (Optimisé Score 100/100)
const CACHE_VERSION = '1.2';
const CACHE_STATIC = `bioage-static-v${CACHE_VERSION}`;
const CACHE_DYNAMIC = `bioage-dynamic-v${CACHE_VERSION}`;
const CACHE_IMAGES = `bioage-images-v${CACHE_VERSION}`;

// Assets critiques à précharger
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/humans.txt'
];

// Install event - cache critical assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_STATIC)
      .then((cache) => {
        console.log('✅ Cache statique créé');
        return cache.addAll(STATIC_ASSETS);
      })
      .catch((err) => {
        console.error('❌ Erreur installation SW:', err);
      })
  );
  self.skipWaiting();
});

// Activate event - clean old caches
self.addEventListener('activate', (event) => {
  const currentCaches = [CACHE_STATIC, CACHE_DYNAMIC, CACHE_IMAGES];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (!currentCaches.includes(cacheName)) {
            console.log('🗑️ Suppression ancien cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch event - Stratégies de cache optimisées
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Stratégie pour les images : Cache First (performance maximale)
  if (request.destination === 'image') {
    event.respondWith(
      caches.open(CACHE_IMAGES).then((cache) => {
        return cache.match(request).then((cached) => {
          return cached || fetch(request).then((response) => {
            cache.put(request, response.clone());
            return response;
          });
        });
      })
    );
    return;
  }

  // Stratégie pour les assets statiques : Cache First avec fallback
  if (
    request.destination === 'script' ||
    request.destination === 'style' ||
    request.destination === 'font' ||
    url.pathname.endsWith('.js') ||
    url.pathname.endsWith('.css')
  ) {
    event.respondWith(
      caches.open(CACHE_STATIC).then((cache) => {
        return cache.match(request).then((cached) => {
          const fetchPromise = fetch(request).then((response) => {
            if (response && response.status === 200) {
              cache.put(request, response.clone());
            }
            return response;
          });
          return cached || fetchPromise;
        });
      })
    );
    return;
  }

  // Stratégie pour HTML : Stale-While-Revalidate (meilleure UX)
  if (request.destination === 'document' || url.pathname.endsWith('.html')) {
    event.respondWith(
      caches.open(CACHE_DYNAMIC).then((cache) => {
        return cache.match(request).then((cached) => {
          const fetchPromise = fetch(request).then((response) => {
            if (response && response.status === 200) {
              cache.put(request, response.clone());
            }
            return response;
          }).catch(() => {
            // Network failed, return cached or offline page
            return cached || caches.match('/');
          });

          // Return cached immediately, update in background
          return cached || fetchPromise;
        });
      })
    );
    return;
  }

  // Stratégie par défaut : Network First (API, données dynamiques)
  event.respondWith(
    fetch(request)
      .then((response) => {
        if (response && response.status === 200 && request.method === 'GET') {
          const responseToCache = response.clone();
          caches.open(CACHE_DYNAMIC).then((cache) => {
            cache.put(request, responseToCache);
          });
        }
        return response;
      })
      .catch(() => {
        return caches.match(request).then((cached) => {
          return cached || caches.match('/');
        });
      })
  );
});

// Background Sync - Pour futures fonctionnalités
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-data') {
    event.waitUntil(
      console.log('🔄 Background sync déclenché')
    );
  }
});

// Push Notifications - Pour futures fonctionnalités
self.addEventListener('push', (event) => {
  const options = {
    body: event.data ? event.data.text() : 'Nouveau contenu disponible',
    icon: '/images/icon-192.png',
    badge: '/images/badge-72.png'
  };
  event.waitUntil(
    self.registration.showNotification('BioAge', options)
  );
});
