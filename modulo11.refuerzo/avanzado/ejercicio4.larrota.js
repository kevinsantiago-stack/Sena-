function* rango(inicio, fin, paso = 1) {
  for (let i = inicio; i <= fin; i += paso) {
    yield i;
  }
}
console.log([...rango(1, 5)]);

function* fibonacci(limite) {
  let [a, b] = [0, 1];
  for (let i = 0; i < limite; i++) {
    yield a;
    [a, b] = [b, a + b];
  }
}
console.log([...fibonacci(10)]);