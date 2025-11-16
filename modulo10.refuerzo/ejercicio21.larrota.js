let nombre = "María";
let edad = 28;
let ciudad = "Valencia";
// Forma antigua (concatenación)
let saludo1 = "Hola, soy " + nombre +
", tengo " + edad +
" años y vivo en " + ciudad;
// Con template literals
let saludo2 = `Hola, soy ${nombre}, tengo ${edad} años y vivo en ${ciudad}`;
console.log(saludo2);
// "Hola, soy María, tengo 28 años y vivo en Valencia"