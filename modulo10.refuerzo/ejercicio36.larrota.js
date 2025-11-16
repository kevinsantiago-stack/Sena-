class BaseDatos {
  constructor() {
    this.db = null;
    this.version = 1;
    this.nombre = 'MiAppDB';
  }

  async inicializar() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.nombre, this.version);

      request.onerror = () => reject(request.error);

      request.onsuccess = () => {
        this.db = request.result;
        resolve(this.db);
      };

      // Configurar estructura la primera vez
      request.onupgradeneeded = (event) => {
        this.db = event.target.result;

        // Crear almacén de objetos (como una tabla)
        if (!this.db.objectStoreNames.contains('usuarios')) {
          const store = this.db.createObjectStore('usuarios', {
            keyPath: 'id',
            autoIncrement: true
          });

          // Crear índices para búsquedas rápidas
          store.createIndex('email', 'email', { unique: true });
          store.createIndex('nombre', 'nombre', { unique: false });
        }
      };
    });
  }
}