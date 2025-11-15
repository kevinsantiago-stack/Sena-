import fs from 'fs';

const larrotaFecha = new Date().toISOString();
const larrotaContenido = `Larrota log creado a las: ${larrotaFecha}\n`;

fs.writeFile('larrota_log.txt', larrotaContenido, (larrotaError) => {
  if (larrotaError) {
    console.error("Error Larrota:", larrotaError);
    return;
  }
  console.log("Archivo Larrota creado exitosamente (CREATE)");
});