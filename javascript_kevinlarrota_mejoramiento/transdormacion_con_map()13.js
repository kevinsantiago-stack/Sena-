let Larrota = [100, 250, 399, 75];

let cuervo = Larrota.map(Larrota => Larrota * 1.10);

console.log("Originales:", Larrota);
console.log("Con 10% aumento:", cuervo);

//map() - Crear un nuevo arrayAplicar una función a cada elemento de un array y devolver un nuevo array con los resultados.
//Diferencia con filter() filter(): Selecciona elementos (puede haber menos) map(): Transforma todos los elementos (misma cantidad)