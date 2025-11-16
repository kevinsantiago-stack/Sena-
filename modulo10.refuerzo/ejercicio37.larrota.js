// Verificar soporte
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
        console.log('SW registrado:', registration);
      })
      .catch(error => {
        console.log('SW falló:', error);
      });
  });
}

// Función para mostrar notificaciones
async function mostrarNotificacion() {
  if ('Notification' in window) {
    let permiso = await Notification.requestPermission();
    if (permiso === 'granted') {
      let registro = await navigator.serviceWorker.ready;
      registro.showNotification('¡Hola!', {
        body: 'Esta es una notificación desde tu PWA',
        icon: '/icon-192x192.png',
        badge: '/badge-72x72.png'
      });
    }
  }
}

// Asignar evento al botón
document.getElementById('notificar').addEventListener('click', mostrarNotificacion);