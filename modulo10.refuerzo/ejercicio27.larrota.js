// Solo los nombres
let nombres = empleados.map(emp => emp.nombre);
console.log(nombres);
// ["Ana", "Carlos", "María", "Juan", "Laura"]
// Salarios con aumento del 10%
let nuevosSalarios = empleados.map(emp => ({
...emp,
salario: emp.salario * 1.1
}));