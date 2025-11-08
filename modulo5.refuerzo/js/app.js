import { Gift } from './clases.js';
import datosInit from '../Data/Data.json' assert { type: 'json' };

// usamos una copia mutable en memoria
let datos = Array.isArray(datosInit) ? datosInit : [];

let idGiftUpdate = null;
const cuerpoTabla = document.querySelector('#cuerpo-tabla');
const myModal = new bootstrap.Modal(document.getElementById('modal-gift'));

// Chart.js instance placeholder
let chartTipos = null;

const calcularEstadisticas = () => {
  const estadisticas = datos.reduce((acc, item) => {
    acc[item.tipo] = (acc[item.tipo] || 0) + 1;
    return acc;
  }, {});
  return estadisticas;
};

const actualizarChart = () => {
  const ctx = document.getElementById('chartTipos').getContext('2d');
  const estad = calcularEstadisticas();
  const labels = Object.keys(estad);
  const values = labels.map(l => estad[l]);
  if (chartTipos) { chartTipos.destroy(); chartTipos = null; }
  chartTipos = new Chart(ctx, {
    type: 'pie',
    data: { labels, datasets: [{ data: values }] },
    options: { responsive: true }
  });
};

const cargarTabla = () => {
  cuerpoTabla.innerHTML = '';
  datos.map((item) => {
    const fila = document.createElement('tr');
    const celdas = `
      <td>${item.gift}</td>
      <td>${item.tipo}</td>
      <td>${item.tiempo}</td>
      <td>$${item.precio}</td>
      <td>
        <div class="d-flex gap-2">
          <button class="btn btn-outline-warning" onclick="window.MostrarModal(${item.id})">
            <i class="fas fa-pencil-alt"></i>
          </button>
          <button class="btn btn-outline-danger" onclick="window.BorrarGift(${item.id})">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </td>
    `;
    fila.innerHTML = celdas;
    cuerpoTabla.appendChild(fila);
  });
  actualizarChart();
};

// DELETE
window.BorrarGift = (id) => {
  const index = datos.findIndex((item) => item.id === id);
  if (index === -1) return;
  const validar = confirm(`¿Está seguro que quiere eliminar la gift Card ${datos[index].gift}?`);
  if (validar) {
    datos.splice(index, 1);
    cargarTabla();
    // persistir en localStorage opcional
    localStorage.setItem('misGifts', JSON.stringify(datos));
  }
};

// CREATE
const formAgregar = document.querySelector('#form-gift');
formAgregar.addEventListener('submit', agregarGift);

function agregarGift(e) {
  e.preventDefault();
  const id = (datos.at(-1)?.id || 0) + 1;
  const gift = document.querySelector('#gift').value;
  const tipo = document.querySelector('#tipo').value;
  const tiempo = document.querySelector('#tiempo').value;
  const precio = document.querySelector('#precio').value;
  const imagen = document.querySelector('#imagen').value;
  datos.push(new Gift(id, gift, tipo, tiempo, precio, imagen));
  formAgregar.reset();
  cargarTabla();
  localStorage.setItem('misGifts', JSON.stringify(datos));
}

// UPDATE - Mostrar modal
window.MostrarModal = (id) => {
  idGiftUpdate = id;
  const index = datos.findIndex((item) => item.id === id);
  if (index === -1) return;
  document.querySelector('#gift-modal').value = datos[index].gift;
  document.querySelector('#tipo-modal').value = datos[index].tipo;
  document.querySelector('#tiempo-modal').value = datos[index].tiempo;
  document.querySelector('#precio-modal').value = datos[index].precio;
  document.querySelector('#imagen-modal').value = datos[index].imagen;
  myModal.show();
};

// UPDATE - Guardar cambios
const formModal = document.querySelector('#form-modal');
formModal.addEventListener('submit', giftUpdate);

function giftUpdate(e) {
  e.preventDefault();
  const index = datos.findIndex((item) => item.id === idGiftUpdate);
  if (index === -1) return;
  datos[index].gift = document.querySelector('#gift-modal').value;
  datos[index].tipo = document.querySelector('#tipo-modal').value;
  datos[index].tiempo = document.querySelector('#tiempo-modal').value;
  datos[index].precio = document.querySelector('#precio-modal').value;
  datos[index].imagen = document.querySelector('#imagen-modal').value;
  cargarTabla();
  myModal.hide();
  localStorage.setItem('misGifts', JSON.stringify(datos));
}

// Inicializar datos desde localStorage si existe
const datosGuardados = localStorage.getItem('misGifts');
if (datosGuardados) {
  try { datos = JSON.parse(datosGuardados); } catch (e) { datos = datos; }
}

// Ejecutar carga inicial
cargarTabla();
