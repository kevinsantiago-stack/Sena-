import fs from 'fs';

const archivoLarrota = "temporal.txt";

if (fs.existsSync(archivoLarrota)) {
  try {
    fs.unlinkSync(archivoLarrota);
    console.log(`Archivo '${archivoLarrota}' eliminado exitosamente`);
  } catch (cuervoErr) {
    console.error("Error al eliminar:", cuervoErr);
  }
} else {
  console.log(`El archivo '${archivoLarrota}' no existe`);
}

