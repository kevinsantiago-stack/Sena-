
const express = require('express');
const dotenv = require('dotenv');
const tasksRouter = require('./routes/tasks');
dotenv.config();

const app = express();
app.use(express.json());

app.get('/', (req, res) => res.json({ ok: true, message: 'Larrota CRUD API running' }));

app.use('/tasks', tasksRouter);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Larrota API listening on port ${PORT}`);
});
