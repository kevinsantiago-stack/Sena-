let productos = [
{id: 1, nombre: "Laptop", precio: 800, stock: 5},
{id: 2, nombre: "Mouse", precio: 25, stock: 50},
{id: 3, nombre: "Teclado", precio: 60, stock: 0},
{id: 4, nombre: "Monitor", precio: 300, stock: 8}
];
// Encontrar producto por ID
let laptop = productos.find(p => p.id === 1);
console.log(laptop.nombre); // "Laptop"
// Encontrar primer producto sin stock
let sinStock = productos.find(p => p.stock === 0);
console.log(sinStock.nombre); // "Teclado"
// Encontrar posición
let posicion = productos.findIndex(p => p.nombre === "Monitor");
console.log(posicion); // 3