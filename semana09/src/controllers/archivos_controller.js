import { urlencoded } from "express";
import { devolverArchivoDelBucket, subirArchivoAlBucket } from "../utils/manejo_archivos_s3.js";

export const subirArchivo = async (req, res) => {

    const archivo = req.file;
    console.log(archivo);
    await subirArchivoAlBucket({
        archivo: archivo.buffer, 
        nombre: archivo.originalname, 
        extension: archivo.mimetype, 
        carpeta: 'productos',

    });

    return res.status(201).json({
        message: "Archivo subido exitosamente",
    });
};

export const devolverArchivo = async (req, res) => {
    const url = await devolverArchivoDelBucket({
        carpeta: 'productos', 
        archivo: "cena.webp"
    });
    return res.json({
        content: url,
    });
};