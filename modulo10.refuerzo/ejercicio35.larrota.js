// Crear el worker
let worker = new Worker('worker.js');

// Actualizar el reloj cada segundo
setInterval(() => {
  document.getElementById('reloj').textContent = new Date().toLocaleTimeString();
}, 1000);

// Función para iniciar el cálculo
function calcularEnWorker() {
  let numero = parseInt(document.getElementById('numero').value);
  if (isNaN(numero) || numero < 0) {
    alert("Por favor ingresa un número válido");
    return;
  }

  console.log('Enviando trabajo al worker...');

  // Enviar tarea al worker
  worker.postMessage({
    comando: 'calcular_factorial',
    datos: numero
  });

  console.log('Interfaz libre para otras tareas');
}

// Escuchar mensajes del worker
worker.addEventListener('message', function(e) {
  let { comando, resultado } = e.data;
  if (comando === 'factorial_completo') {
    console.log('Factorial recibido:', resultado);
    document.getElementById('resultado').textContent = resultado;
  }
});