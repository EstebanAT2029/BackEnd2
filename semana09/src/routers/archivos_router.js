import { Router } from "express";
import multer from "multer";
import { devolverArchivo, eliminarArchivo, generarUrlDelBacket, subirArchivo, } from "../controllers/archivos_controller.js";

const middlewareArchivos = multer({
    storage: multer.memoryStorage(), 
    fileFilter: (req, file, cb) => {
        const tipoArchivo = file.mimetype;
        if (tipoArchivo === "aplication/pdf"){
            cb(new Error("El archivo no puede ser un PDF"));
        }

        cb(null, true);
    },
    limits: { fileSize: 10 * 1024 * 1024},

});

export const archivosRouter = Router();

archivosRouter.post("/subir-archivo", middlewareArchivos.single("archivo"), subirArchivo
);

archivosRouter.get("/devolver-archivo", devolverArchivo);

archivosRouter.post("/generar-url", generarUrlDelBacket);

archivosRouter.delete("/archivo/:id", eliminarArchivo);
