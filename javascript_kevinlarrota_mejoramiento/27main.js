import {
  LARROTA_VERSION,
  saludarLarrotaUsuario
} from './27.js';

console.log("Versión Larrota:", LARROTA_VERSION);
console.log(saludarLarrotaUsuario("Larrota Ana"));

//Diferencias clave: Las exportaciones nombradas requieren usar el nombre exacto al importar y deben ir
//entre llaves {}. Puedes tener tantas como necesites en un solo archivo.