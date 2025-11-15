
const { Pool } = require('pg');
const dotenv = require('dotenv');
dotenv.config();

const larrotaPool = new Pool({
  host: process.env.PGHOST,
  user: process.env.PGUSER,
  password: process.env.PGPASSWORD,
  database: process.env.PGDATABASE,
  port: process.env.PGPORT ? parseInt(process.env.PGPORT) : 5432
});

module.exports = larrotaPool;
