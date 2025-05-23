import { Router } from "express";
import * as clienteController from "../controllers/clientes_controller.js";
import { validarToken } from "../utils/validar_Token.js"

export const clienteRouter = Router();

clienteRouter
    .route("/clientes")
    .post(validarToken, clienteController.registrarCliente);