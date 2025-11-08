const { Pool } = require('pg');

const pool = new Pool({
  user: 'tu_usuario',
  host: 'localhost',
  database: 'crud_db',
  password: 'tu_password',
  port: 5432,
});

module.exports = pool;