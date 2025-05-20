// winget install jasongin.nvs
//para usar npm =>nvs use node/22.15.1/x64
const nombre = 'Esteban'
let edad = 32
edad = 31
edad =13
edad = 'cuarenta y dos'
edad = false

function sumar(numero1, numero2){
    // el uso del; es complementa opcional
    // variables locales que solo existen dentro de la funcion
    const resultado = numero1+numero2

    return resultado;
}

const sumatoria = sumar(10,5)

console.log(sumatoria)
//JS es recontra flexible tanto asi que si quieres 'sumar' un string y un numero hara la concatenacion y no la sumatoria
const sumatoria2 = sumar('a', 80)
console.log(sumatoria2)

//las funciones tambien pueden definirse de manera anonima!
//las funciones anonimas son de tipo flecha
const restar = (numero1, numero2) => {
    const resultado = numero1 - numero2
    return resultado
}
const resta = restar(20,2)
console.log(resta)

//hoisting > en las funciones 'tradcionales' son elevadas al inicio dek=l contecto de ejecucion (si primero)