// WeakMap solo acepta objetos como claves
let metadatos = new WeakMap();
let elemento1 = {id: 1};
let elemento2 = {id: 2};
// Asociar metadatos a objetos
metadatos.set(elemento1, {
fechaCreacion: new Date(),
clicks: 0
});
metadatos.set(elemento2, {
fechaCreacion: new Date(),
clicks: 5
});
// Acceder a metadatos
console.log(metadatos.get(elemento1));
// Cuando elemento1 se elimina, sus metadatos también
elemento1 = null; // El recolector puede eliminar la entrada









