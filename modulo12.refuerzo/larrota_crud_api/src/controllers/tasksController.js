// src/controllers/tasksController.js
const TaskRepository = require('../models/taskRepository');

const tasksController = {
  async list(req, res) {
    try {
      const rows = await TaskRepository.findAll();
      res.json(rows);
    } catch (err) {
      console.error('larrota:list:error', err);
      res.status(500).json({ error: 'Error al listar tareas' });
    }
  },
  async get(req, res) {
    try {
      const task = await TaskRepository.findById(req.params.id);
      if (!task) return res.status(404).json({ error: 'Tarea no encontrada' });
      res.json(task);
    } catch (err) {
      console.error('larrota:get:error', err);
      res.status(500).json({ error: 'Error al obtener tarea' });
    }
  },
  async create(req, res) {
    try {
      const { title, description } = req.body;
      if (!title) return res.status(400).json({ error: 'title es requerido' });
      const created = await TaskRepository.create({ title, description });
      res.status(201).json(created);
    } catch (err) {
      console.error('larrota:create:error', err);
      res.status(500).json({ error: 'Error al crear tarea' });
    }
  },
  async update(req, res) {
    try {
      const { title, description, completed } = req.body;
      const updated = await TaskRepository.update(req.params.id, { title, description, completed });
      if (!updated) return res.status(404).json({ error: 'Tarea no encontrada' });
      res.json(updated);
    } catch (err) {
      console.error('larrota:update:error', err);
      res.status(500).json({ error: 'Error al actualizar tarea' });
    }
  },
  async remove(req, res) {
    try {
      await TaskRepository.remove(req.params.id);
      res.status(204).send();
    } catch (err) {
      console.error('larrota:remove:error', err);
      res.status(500).json({ error: 'Error al eliminar tarea' });
    }
  }
};

module.exports = tasksController;
