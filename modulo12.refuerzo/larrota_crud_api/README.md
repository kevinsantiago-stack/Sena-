# Larrota CRUD API (Node.js + PostgreSQL)

Proyecto ejemplo generado a partir de la guía "Transforma tus ideas..." (SENA).
Entrega: API REST mínima para gestionar **tasks** (tareas) con operaciones CRUD.

## Archivos incluidos
- `package.json` — dependencias y scripts.
- `src/index.js` — servidor Express.
- `src/db.js` — conexión a PostgreSQL (usa la variable `larrotaPool`).
- `src/routes/tasks.js` — rutas REST para /tasks.
- `src/controllers/tasksController.js` — lógica de controladores.
- `src/models/taskRepository.js` — consultas SQL al modelo `tasks`.
- `migrations/create_tasks.sql` — script SQL para crear la tabla `tasks`.
- `.env.example` — variables de entorno de ejemplo.

## Requisitos
- Node.js (>=16)
- PostgreSQL (local o remoto)

## Uso (local)
1. Copia `.env.example` a `.env` y ajusta las credenciales.
2. Instala dependencias: `npm install`
3. Crea la base de datos y la tabla:
   - Con psql: `createdb larrota_db` (si usa same PGUSER) y luego `psql -d larrota_db -f migrations/create_tasks.sql`
4. Ejecuta en modo desarrollo: `npm run dev` o `npm start`
5. Endpoints:
   - `GET /tasks` — listar tareas
   - `GET /tasks/:id` — obtener tarea
   - `POST /tasks` — crear tarea `{ "title": "...", "description": "..." }`
   - `PUT /tasks/:id` — actualizar tarea
   - `DELETE /tasks/:id` — eliminar tarea

## Notas
- Este proyecto usa variables y nombres relacionados con "larrota" por preferencia del usuario.
- Código didáctico: las consultas son simples y claras para facilitar el aprendizaje.
