import express from "express"

const servidor = express();
const PORT = 3000;

// Asi podemos crear un nuevo controlador con su ruta
servidor.get("/", (req, res) => {
  console.log(req.body);
  return res.json({ message: "Bienvenido a mi API"});
});

servidor.listen(PORT, (error) =>{
    if (error){
        console.log("Hubo un error");

    } else{
        console.log(`Servidor corriendo http//:127.0.0.1:${PORT}`);
    }
});