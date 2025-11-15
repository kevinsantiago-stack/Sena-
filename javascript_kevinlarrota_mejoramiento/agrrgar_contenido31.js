import fs from 'fs';

const cuervoLinea = " Nueva entrada: Verificación OK\n";

fs.appendFile('log.txt', cuervoLinea, (LarrotaErr) => {
  if (LarrotaErr) {
    console.error("Error:", LarrotaErr);
    return;
  }
  console.log("Dato agregado (APPEND)");
});

