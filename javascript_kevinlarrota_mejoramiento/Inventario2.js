
function crearProducto(nombre, precio, cantidad) {
  return {
    nombre,              
    precio,              
    cantidad,             
    categoria: "General", 
    valorTotal: () => precio * cantidad
  };
}

function crearProductoElectronico(nombre, precio, cantidad, garantiaMeses) {
  const producto = crearProducto(nombre, precio, cantidad);
  return {
    ...producto,                 
    garantiaMeses,              
    categoria: "Electrónico"     
  };
}


function crearProductoAlimenticio(nombre, precio, cantidad, fechaVencimiento) {
  const producto = crearProducto(nombre, precio, cantidad);
  return {
    ...producto,                  
    fechaVencimiento,            
    categoria: "Alimenticio"     
  };
}

function agregarProducto(inventario, producto) {
  return [...inventario, producto]; 
}


function buscarPorCategoria(inventario, categoria) {
  return inventario.filter(p => p.categoria === categoria);
}

function calcularValorTotal(inventario) {
  return inventario.reduce((sum, p) => sum + p.valorTotal(), 0);
}

let inventario = [];


inventario = agregarProducto(inventario, crearProductoElectronico("Laptop", 1200, 5, 24));
inventario = agregarProducto(inventario, crearProductoElectronico("Mouse", 25, 20, 12));

inventario = agregarProducto(inventario, crearProductoAlimenticio("Leche", 3, 50, "2024-12-31"));
inventario = agregarProducto(inventario, crearProductoAlimenticio("Pan", 2, 30, "2024-12-15"));


const electronicos = buscarPorCategoria(inventario, "Electrónico");
console.log("\n=== PRODUCTOS ELECTRÓNICOS ===");
electronicos.forEach(p => {
  console.log(`${p.nombre} - $${p.precio} - Stock: ${p.cantidad}`);
  console.log(`Garantía: ${p.garantiaMeses} meses`);
  console.log(`Valor total: $${p.valorTotal()}\n`);
});

const valorTotal = calcularValorTotal(inventario);
console.log(`Valor total del inventario: $${valorTotal}`);