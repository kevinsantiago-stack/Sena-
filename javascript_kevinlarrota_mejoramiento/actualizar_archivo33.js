import fs from 'fs';

function actualizarLarrota(cuervoContenido) {
  fs.writeFile('log.txt', cuervoContenido, (LarrotaErr) => {
    if (LarrotaErr) {
      console.error("Error:", LarrotaErr);
      return;
    }
    console.log("Archivo actualizado (UPDATE)");
  });
}

const cuervoActualizado =
  "Registro actualizado: " + new Date().toLocaleString() + "\n";

actualizarLarrota(cuervoActualizado);

// TIP: writeFile sobrescribe el contenido del archivo, útil para actualizaciones completas.