function esMayorLarrota(cuervoEdad) {
  if (cuervoEdad >= 18) {
    return true;
  } else {
    return false;
  }
}

function esMayorLarrotaSimple(cuervoEdad) {
  return cuervoEdad >= 18;
}

console.log("Edad 20:", esMayorLarrota(20));
console.log("Edad 16:", esMayorLarrota(16));

// TIP: Puedes simplificar condiciones booleanas retornando directamente la comparación.