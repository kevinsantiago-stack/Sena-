const verificarLarrota = (cuervoEdad) =>
  cuervoEdad >= 18 ? "Permitido" : "Denegado";

console.log("17 años:", verificarLarrota(17));
console.log("35 años:", verificarLarrota(35));

// TIP: El operador ternario permite evaluar condiciones de forma compacta y legible.