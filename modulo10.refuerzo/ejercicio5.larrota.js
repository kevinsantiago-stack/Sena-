let x = 5;
let y = "5";
// Comparación de valor (evitar)
console.log(x == y); // true
// Comparación estricta (recomendado)
console.log(x === y); // false
// Mayor y menor
console.log(x > 3);
// true
console.log(x <= 10); // true

//Operadores Lógicos
let llueve = true;
let tengoSombrilla = false;
// AND (&&) - ambas condiciones deben ser true
let salgoSin = llueve && tengoSombrilla; // false
// OR (||) - al menos una condición true
let meMojo = llueve || !tengoSombrilla; // true
// NOT (!) - invierte el valor
let noLlueve = !llueve; // false