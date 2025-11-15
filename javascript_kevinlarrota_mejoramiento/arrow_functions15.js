const areaLarrota = (cuervoBase, cuervoAltura) => {
  return (cuervoBase * cuervoAltura) / 2;
};

const areaLarrotaCorto = (cuervoBase, cuervoAltura) =>
  (cuervoBase * cuervoAltura) / 2;

console.log("Área:", areaLarrota(8, 5));

// TIP: Puedes usar funciones flecha con return implícito para simplificar cálculos como este.