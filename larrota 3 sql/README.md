![alt text](image.png)
![alt text](image-1.png)

// 1. Seleccionar la base de datos 
use Universidad



// 2. Insertar documentos en la colección "estudiantes"
db.estudiantes.insertMany([
{
    nombre: "Ana Pérez",
    edad: 21,
    carrera: "Ingeniería",
    notas: [4.5, 3.8, 4.2],
    direccion: { ciudad: "Bogotá", barrio: "Chapinero" }
},
{
    nombre: "Carlos Ruiz",
    edad: 23,
    carrera: "Administración",
    notas: [3.2, 3.5, 4.0],
    direccion: { ciudad: "Medellín", barrio: "Poblado" }
},
{
    nombre: "Laura Gómez",
    edad: 20,
    carrera: "Ingeniería",
    notas: [4.8, 4.9, 5.0],
    direccion: { ciudad: "Cali", barrio: "San Fernando" }
}
])



// 3. Consultas básicas

// Mostrar todos los estudiantes
db.estudiantes.find().pretty()

// Buscar un estudiante por nombre
db.estudiantes.find({ nombre: "Ana Pérez" })



// 4. Consultas usando operadores

// Estudiantes con edad mayor o igual a 21
db.estudiantes.find({ edad: { $gte: 21 } })

// Estudiantes cuya carrera no sea Ingeniería
db.estudiantes.find({ carrera: { $ne: "Ingeniería" } })

// Estudiantes con alguna nota mayor a 4.5
db.estudiantes.find({ notas: { $elemMatch: { $gt: 4.5 } } })



// 5. Proyección de campos

// Mostrar solo nombre y ciudad, ocultando el _id
db.estudiantes.find(
  {},
  { nombre: 1, "direccion.ciudad": 1, _id: 0 }
)



// 6. Ordenar resultados

// Ordenar estudiantes por edad (descendente)
db.estudiantes.find().sort({ edad: -1 })



// 7. Actualizar documentos

// Agregar un campo "promedio" a un estudiante
db.estudiantes.update(
  { nombre: "Ana Pérez" },
  { $set: { promedio: 4.1 } }
)

// Sumar 1 año a la edad de todos los estudiantes
db.estudiantes.update(
  {},
  { $inc: { edad: 1 } },
  { multi: true }
)

// Agregar una nueva nota en el array "notas" de Carlos Ruiz
db.estudiantes.update(
  { nombre: "Carlos Ruiz" },
  { $push: { notas: 4.4 } }
)



// 8. Eliminar documentos

// Eliminar estudiante por nombre
db.estudiantes.remove({ nombre: "Laura Gómez" })

// Eliminar estudiantes con promedio menor que 4
db.estudiantes.remove({ promedio: { $lt: 4 } })



// 9. Crear colección "cursos"

db.cursos.insertMany([
  { nombre: "Bases de Datos", creditos: 12 },
  { nombre: "Probabilidad", creditos: 8 },
  { nombre: "Programación", creditos: 10 }
])



// 10. Consultas entre colecciones (conceptual)

// Buscar un curso específico
db.cursos.findOne({ nombre: "Bases de Datos" })

// Ejemplo de consulta si existiera un campo cursosInscritos
db.estudiantes.find({
  cursosInscritos: { $in: [ObjectId("ID_DEL_CURSO")] }
})
