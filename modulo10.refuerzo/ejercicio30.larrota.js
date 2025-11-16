let texto = "Mi email es juan@ejemplo.com y mi teléfono es 123-456-7890";
// Buscar email
let regexEmail = /\w+@\w+\.\w+/;
let email = texto.match(regexEmail);
console.log(email[0]); // "juan@ejemplo.com"
// Buscar números de teléfono
let regexTelefono = /\d{3}-\d{3}-\d{4}/;
let telefono = texto.match(regexTelefono);
console.log(telefono[0]); // "123-456-7890"
// Buscar todas las coincidencias
let regexNumeros = /\d+/g; // g = global
let numeros = texto.match(regexNumeros);
console.log(numeros); // ["123", "456", "7890"]

// Validar email
function validarEmail(email) {
let regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
return regex.test(email);
}
console.log(validarEmail("test@ejemplo.com")); // true
console.log(validarEmail("email_inválido")); // false
// Validar contraseña (8+ chars, 1 mayúscula, 1 número)
function validarPassword(password) {
let regex = /^(?=.*[A-Z])(?=.*\d).{8,}$/;
return regex.test(password);
}
console.log(validarPassword("MiPass123")); // true
console.log(validarPassword("débil")); // false
// Limpiar número de teléfono
function limpiarTelefono(telefono) {
return telefono.replace(/\D/g, ''); // Quitar todo lo que no sea dígito
}
console.log(limpiarTelefono("(123) 456-7890")); // "1234567890"