// Crear Set
let colores = new Set();
// Agregar elementos
colores.add("rojo");
colores.add("azul");
colores.add("verde");
colores.add("rojo"); // ¡No se agrega! Ya existe
console.log(colores.size); // 3 (no 4)
// Verificar existencia
console.log(colores.has("rojo")); // true
// Convertir array con duplicados a único
let numerosConDuplicados = [1, 2, 2, 3, 3, 3, 4];
let numerosUnicos = [...new
Set(numerosConDuplicados)];
console.log(numerosUnicos); // [1, 2, 3, 4]
// Iterar
colores.forEach(color => {
console.log(color);
});
// Eliminar
colores.delete("azul");
console.log([...colores]); // ["rojo", "verde"]