import express from "express"

const servidor = express();
//Validara si existe la variable de entorno y si no usaremos el numero 3000
const PORT = process.env.PORT ?? 3000;

servidor.get('/status',(req, res)=>{
    const horaServidor = new Date();

    res.json({
        status: "Activo",
        hora: horaServidor,
    });
});

servidor.listen(PORT, (error) => {
    if (error) {
        console.error(error);
    } else {
        console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
    }
});