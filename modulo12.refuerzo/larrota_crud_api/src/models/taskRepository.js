const pool = require('../db');

const TaskRepository = {
  async findAll() {
    const res = await pool.query('SELECT * FROM tasks ORDER BY id');
    return res.rows;
  },
  async findById(id) {
    const res = await pool.query('SELECT * FROM tasks WHERE id = $1', [id]);
    return res.rows[0];
  },
  async create({ title, description }) {
    const res = await pool.query(
      'INSERT INTO tasks (title, description) VALUES ($1, $2) RETURNING *',
      [title, description]
    );
    return res.rows[0];
  },
  async update(id, { title, description, completed }) {
    const res = await pool.query(
      `UPDATE tasks SET title = $1, description = $2, completed = $3, updated_at = NOW()
       WHERE id = $4 RETURNING *`,
      [title, description, completed, id]
    );
    return res.rows[0];
  },
  async remove(id) {
    await pool.query('DELETE FROM tasks WHERE id = $1', [id]);
    return;
  }
};

module.exports = TaskRepository;
