const express = require('express');
const cors = require('cors');
const pool = require('./database');

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

// Crear tabla si no existe
const createTable = async () => {
  await pool.query(`
    CREATE TABLE IF NOT EXISTS usuarios (
      id SERIAL PRIMARY KEY,
      nombre VARCHAR(100) NOT NULL,
      email VARCHAR(100) UNIQUE NOT NULL,
      edad INTEGER,
      creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
  `);
};
createTable();

// Endpoints CRUD
app.get('/api/usuarios', async (req, res) => {
  const result = await pool.query('SELECT * FROM usuarios ORDER BY id DESC');
  res.json(result.rows);
});

app.get('/api/usuarios/:id', async (req, res) => {
  const { id } = req.params;
  const result = await pool.query('SELECT * FROM usuarios WHERE id = $1', [id]);
  if (result.rows.length === 0) return res.status(404).json({ error: 'Usuario no encontrado' });
  res.json(result.rows[0]);
});

app.post('/api/usuarios', async (req, res) => {
  const { nombre, email, edad } = req.body;
  try {
    const result = await pool.query(
      'INSERT INTO usuarios (nombre, email, edad) VALUES ($1, $2, $3) RETURNING *',
      [nombre, email, edad]
    );
    res.status(201).json(result.rows[0]);
  } catch (error) {
    if (error.code === '23505') {
      res.status(400).json({ error: 'El email ya existe' });
    } else {
      res.status(500).json({ error: error.message });
    }
  }
});

app.put('/api/usuarios/:id', async (req, res) => {
  const { id } = req.params;
  const { nombre, email, edad } = req.body;
  const result = await pool.query(
    'UPDATE usuarios SET nombre=$1, email=$2, edad=$3 WHERE id=$4 RETURNING *',
    [nombre, email, edad, id]
  );
  if (result.rows.length === 0) return res.status(404).json({ error: 'Usuario no encontrado' });
  res.json(result.rows[0]);
});

app.delete('/api/usuarios/:id', async (req, res) => {
  const { id } = req.params;
  const result = await pool.query('DELETE FROM usuarios WHERE id=$1 RETURNING *', [id]);
  if (result.rows.length === 0) return res.status(404).json({ error: 'Usuario no encontrado' });
  res.json({ message: 'Usuario eliminado', usuario: result.rows[0] });
});

app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});