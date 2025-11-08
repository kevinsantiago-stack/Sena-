const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const resultado = numeros
  .filter(num => num > 5)   // [6, 7, 8, 9, 10]
  .map(num => num * 2)      // [12, 14, 16, 18, 20]
  .reduce((sum, num) => sum + num, 0); // 80

console.log(resultado); // 80