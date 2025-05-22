import { Router } from "express";
import * as clienteController from "../controllers/clientes_controller.js";

export const clienteRouter = Router();

clienteRouter.route("/clientes").post(clienteController.registrarCliente);