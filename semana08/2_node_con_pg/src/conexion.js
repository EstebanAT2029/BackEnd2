import { Client } from "pg";
import { config } from "dotenv";
config();
// Si queremos hacer solo una exportacion en nuestro archivo podemos hacer una exportacion x defecto para evitar hacer una destructuracion en la importacion
// import conexion from './conexion.js';

// Sin exportacion por defecto
// import {conexion} from './conexion.js';

export default new Client({
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
});