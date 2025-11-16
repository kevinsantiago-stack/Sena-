// Rest: recoger múltiples argumentos
function sumarTodos(...numeros) {
return numeros.reduce((total, n) => total + n, 0);
}
console.log(sumarTodos(1, 2, 3, 4, 5)); // 15
console.log(sumarTodos(10, 20)); // 30
// Primer argumento separado
function saludarGrupo(saludo, ...nombres) {
return nombres.map(nombre => `${saludo},
${nombre}!`);
}
console.log(saludarGrupo("Hola", "Ana", "Carlos",
"María"));
// ["Hola, Ana!", "Hola, Carlos!", "Hola, María!"]