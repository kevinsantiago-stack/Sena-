
let temperaturas = [15, 22, 33, 45, 68, 82, 91];
let temperaturasAltas = temperaturas.filter(temp => temp > 50);
console.log("Originales:", temperaturas);
console.log("Mayores a 50:", temperaturasAltas);


//TIP: filter() es perfecto para buscar elementos que cumplan ciertos criterios sin modificar el array original.
//Úsalo cuando necesites extraer subconjuntos de datos basados en condiciones.