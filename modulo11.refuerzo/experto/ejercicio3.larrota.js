function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const clave = JSON.stringify(args);
    if (cache.has(clave)) {
      console.log("Retornando resultado cacheado");
      return cache.get(clave);
    }
    const resultado = fn(...args);
    cache.set(clave, resultado);
    return resultado;
  };
}

function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

const factorialMemo = memoize(factorial);

console.log(factorialMemo(5)); 
console.log(factorialMemo(5)); 