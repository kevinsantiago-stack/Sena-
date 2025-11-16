// Fecha actual
let ahora = new Date();
console.log(ahora); // Fecha y hora completa
// Fecha específica
let navidad = new Date(2024, 11, 25); // Año, mes (0-11), día
let cumpleanos = new Date("2024-07-15");
// Partes de la fecha
console.log(ahora.getFullYear()); // 2024
console.log(ahora.getMonth()); // 0-11 (enero = 0)
console.log(ahora.getDate()); // Día del mes
console.log(ahora.getDay()); // Día semana (0=domingo)


//Formatear Fechas
let fecha = new Date();
// Formato legible
let opciones = {
year: 'numeric',
month: 'long',
day: 'numeric'
};
console.log(fecha.toLocaleDateString('es-ES', opciones));
// "15 de marzo de 2024"
// Solo la hora
console.log(fecha.toLocaleTimeString('es-ES'));
// "14:30:25"