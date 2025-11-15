import fs from 'fs';

fs.readFile('log.txt', 'utf8', (LarrotaErr, cuervoData) => {
  if (LarrotaErr) {
    console.error("Error al leer:", LarrotaErr);
    return;
  }

  console.log("=== Contenido de log.txt ===");
  console.log(cuervoData);
  console.log("============================");
});

// TIP: readFile permite leer archivos de forma asíncrona, útil para mostrar contenido sin bloquear el flujo.