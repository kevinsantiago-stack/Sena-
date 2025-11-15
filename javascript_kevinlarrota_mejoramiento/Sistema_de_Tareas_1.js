let tareas = [];

function agregarTarea(lista, tarea) {
  const nuevaLista = [...lista, tarea];
  console.log(`Tarea agregada: "${tarea}"`);
  return nuevaLista;
}

function completarTarea(lista, indice) {
  if (indice >= 0 && indice < lista.length) {
    const nuevaLista = lista.map((t, i) =>
      i === indice ? "7 " + t : t
    );
    console.log("Tarea marcada como completada");
    return nuevaLista;
  } else {
    console.log("Índice inválido");
    return lista;
  }
}


function obtenerEstadisticas(lista) {
  const total = lista.length;
  const completadas = lista.filter(t => t.startsWith("7")).length;
  const pendientes = total - completadas;
  return { total, completadas, pendientes };
}


function mostrarTareas(lista) {
  console.log("\n=== LISTA DE TAREAS ===");
  lista.forEach((tarea, i) => {
    console.log(`${i}. ${tarea}`);
  });
}


tareas = agregarTarea(tareas, "Estudiar JavaScript");
tareas = agregarTarea(tareas, "Hacer ejercicio");
tareas = agregarTarea(tareas, "Preparar presentación");

mostrarTareas(tareas);

tareas = completarTarea(tareas, 0);

mostrarTareas(tareas);

const stats = obtenerEstadisticas(tareas);
console.log("\n=== ESTADÍSTICAS ===");
console.log(`Total: ${stats.total}`);
console.log(`Completadas: ${stats.completadas}`);
console.log(`Pendientes: ${stats.pendientes}`);