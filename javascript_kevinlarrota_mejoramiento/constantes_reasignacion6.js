const PI = 3.14159;
// PI = 3.14; // ERROR!
console.log(PI); // 3.14159
//Las constantes NO pueden
//reasignarse después de
//declararse


let contador = 10;

contador = 20; // Válido
console.log(contador); // 20
//Las variables con let pueden
//cambiar de valor libremente

{
let temporal = 5;
const fija = 10;
console.log(temporal)
console.log(fija)
}
//Tanto let como const tienen ámbito
//de bloque (dentro de {})