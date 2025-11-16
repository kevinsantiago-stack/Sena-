let producto = "Laptop";
let precio = 899.99;
let descuento = 0.1;
// Texto multilínea con cálculos
let recibo = `
════════════════════════
RECIBO DE VENTA
════════════════════════
Producto: ${producto}
Precio original: $${precio}
Descuento (${descuento * 100}%): $${(precio * descuento).toFixed(2)}
Precio final: $${(precio * (1 - descuento)).toFixed(2)}
════════════════════════
¡Gracias por su compra!
`;
console.log(recibo);