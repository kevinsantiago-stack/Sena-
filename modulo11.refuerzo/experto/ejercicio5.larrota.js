class UserRepository {
  constructor() {
    this.users = new Map();
    this.nextId = 1;
  }

  async create(userData) {
    const user = {
      id: this.nextId++,
      ...userData,
      createdAt: new Date(),
      updatedAt: new Date()
    };
    this.users.set(user.id, user);
    return user;
  }

  async findById(id) {
    return this.users.get(id) || null;
  }

  async update(id, updateData) {
    if (!this.users.has(id)) return null;
    const user = { ...this.users.get(id), ...updateData, updatedAt: new Date() };
    this.users.set(id, user);
    return user;
  }

  async delete(id) {
    return this.users.delete(id);
  }
}

(async () => {
  const repo = new UserRepository();
  const user = await repo.create({ name: "Ana", email: "ana@example.com" });
  console.log("Creado:", user);

  const found = await repo.findById(user.id);
  console.log("Encontrado:", found);

  const updated = await repo.update(user.id, { name: "Ana María" });
  console.log("Actualizado:", updated);

  await repo.delete(user.id);
  console.log("Eliminado:", user.id);
})();