// Empleados del departamento IT
let empleadosIT = empleados.filter(emp =>
emp.departamento === "IT"
);
console.log(empleadosIT); // Ana y María
// Empleados con salario > 55000
let salarioAlto = empleados.filter(emp =>
emp.salario > 55000
);
console.log(salarioAlto.length); // 3 empleados