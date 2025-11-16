function* fibonacci() {
let a = 0, b = 1;
while (true) {
yield a;
[a, b] = [b, a + b]; // Intercambio elegante
}
}
// Tomar solo los primeros 10 números
let fib = fibonacci();
let primeros10 = [];
for (let i = 0; i < 10; i++) {
primeros10.push(fib.next().value);
}
console.log(primeros10); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]