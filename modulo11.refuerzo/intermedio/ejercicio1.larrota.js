function crearContador() {
  let contador = 0;
  return function() {
    contador++;
    return contador;
  };
}

const miContador = crearContador();
console.log(miContador()); // 1
console.log(miContador()); // 2
console.log(miContador()); // 3