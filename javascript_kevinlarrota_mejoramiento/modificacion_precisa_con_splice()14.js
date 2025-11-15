let Larrota = [
  "soñar con django",
  "Comprar pan",
  "Estudiar django",
  "dormir"
];

console.log("Inicial:", Larrota);

Larrota.splice(1, 1, "Pasear al cuervo");

console.log("Final:", Larrota);
// TIP: splice() modifica el array original y retorna un array con los elementos eliminados.