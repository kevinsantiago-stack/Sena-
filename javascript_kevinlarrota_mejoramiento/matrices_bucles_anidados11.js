let Larrota = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

function imprimirLarrota(cuervo) {
  for (let Larrota = 0; Larrota < cuervo.length; Larrota++) {
    for (let cuervoIndex = 0; cuervoIndex < cuervo[Larrota].length; cuervoIndex++) {
      console.log(`[${Larrota}][${cuervoIndex}] = ${cuervo[Larrota][cuervoIndex]}`);
    }
  }
}

imprimirLarrota(Larrota);