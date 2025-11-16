// Suma total de salarios
let totalSalarios = empleados.reduce((total, emp) =>
total + emp.salario, 0
);
console.log(totalSalarios); // 295000
// Agrupar por departamento
let porDepartamento = empleados.reduce((grupos,
emp) => {
grupos[emp.departamento] =
grupos[emp.departamento] || [];
grupos[emp.departamento].push(emp);
return grupos;
}, {});