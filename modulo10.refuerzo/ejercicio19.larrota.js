// Parámetros destructurados
function presentar({nombre, edad, ciudad}) {
return `Soy ${nombre}, tengo ${edad} años y vivo
en ${ciudad}`;
}
let usuario = {
nombre: "Ana",
edad: 25,
ciudad: "Barcelona"
};
console.log(presentar(usuario));
// "Soy Ana, tengo 25 años y vivo en Barcelona"