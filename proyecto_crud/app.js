class UserManager {
  constructor() {
    this.baseUrl = 'http://localhost:3000/api/usuarios';
    this.form = document.getElementById('user-form');
    this.usersList = document.getElementById('users-list');
    this.cancelBtn = document.getElementById('cancel-btn');
    this.isEditing = false;
    this.currentId = null;

    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    this.cancelBtn.addEventListener('click', () => this.resetForm());

    this.loadUsers();
  }

  async loadUsers() {
    const res = await fetch(this.baseUrl);
    const users = await res.json();
    this.usersList.innerHTML = '';
    users.forEach(u => {
      const div = document.createElement('div');
      div.className = 'user-card';
      div.innerHTML = `
        <div>
          <h3>${u.nombre}</h3>
          <p><strong>Email:</strong> ${u.email}</p>
          <p><strong>Edad:</strong> ${u.edad || '-'}</p>
        </div>
        <div>
          <button onclick="manager.editUser(${u.id})">Editar</button>
          <button onclick="manager.deleteUser(${u.id})">Eliminar</button>
        </div>
      `;
      this.usersList.appendChild(div);
    });
  }

  async handleSubmit(e) {
    e.preventDefault();
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    const edad = document.getElementById('edad').value;

    if (this.isEditing) {
      await fetch(`${this.baseUrl}/${this.currentId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre, email, edad })
      });
    } else {
      await fetch(this.baseUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre, email, edad })
      });
    }
    this.resetForm();
    this.loadUsers();
  }

  editUser(id) {
    const card = [...this.usersList.children].find(c => c.querySelector('button').onclick.toString().includes(id));
    const nombre = card.querySelector('h3').textContent;
    const email = card.querySelector('p:nth-child(2)').textContent.split(': ')[1];
    const edad = card.querySelector('p:nth-child(3)').textContent.split(': ')[1];

    document.getElementById('nombre').value = nombre;
    document.getElementById('email').value = email;
    document.getElementById('edad').value = edad;
    this.isEditing = true;
    this.currentId = id;
    this.cancelBtn.style.display = 'inline-block';
  }

  async deleteUser(id) {
    await fetch(`${this.baseUrl}/${id}`, { method: 'DELETE' });
    this.loadUsers();
  }

  resetForm() {
    this.form.reset();
    this.isEditing = false;
    this.currentId = null;
    this.cancelBtn.style.display = 'none';
  }
}

const manager = new UserManager();