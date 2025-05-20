import express from "express";
import { listen } from "express/lib/application";

const servidor = express();
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing
const PORT = process.env.PORT ?? 3000;

servidor/listen(PORT, (error) =>{
    if (error){
        throw error;
    }
    console.log(`Servidor correindo en http://127.0.0.1:${PORT}`)
       
}) ;
