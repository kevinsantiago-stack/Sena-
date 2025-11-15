function clasificarLarrota(cuervoF) {
  if (cuervoF >= 14 && cuervoF < 32) {
    return "Temperatura baja";
  } else if (cuervoF >= 32 && cuervoF < 68) {
    return "Temperatura adecuada";
  } else if (cuervoF >= 68 && cuervoF < 96) {
    return "Temperatura alta";
  } else {
    return "Temperatura desconocida";
  }
}

console.log(clasificarLarrota(25));
console.log(clasificarLarrota(50));
console.log(clasificarLarrota(85));

// TIP: Usa rangos con operadores lógicos para clasificar valores dentro de categorías específicas.