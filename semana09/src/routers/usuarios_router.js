
import { Router } from "express";
import * as UsuarioController from "../controllers/usuarios_controller.js";
import { validarAdmin, validarToken } from "../utils/validar_Token.js";

export const usuarioRouter = Router();


//Podemos tneer tantos middlewares que ncesitamos pero estos siempre tienen que tener una orden en especifico
usuarioRouter.post("/registro", validarToken, validarAdmin, UsuarioController.registroUsuario);

usuarioRouter.post("/login", UsuarioController.login);