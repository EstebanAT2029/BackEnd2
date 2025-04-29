from flask import Flask, request


# __name__ > devolvera el valor de '__main__' si el archivo en el cual nos encontramos es el archivo principal del proyecto, si no lo es devolvera otro valor y esto le sirve a Flask para poder inicializar correctamente el proyecto
app = Flask(__name__)

#un decorador en Python sirve para poder modificar el comportamiento de un metodo o funcion sin la ncesidad de editarlo de raiz sino que se le agrega a su logica ya creada un adicional, adicional a ello se le puede pasar parametros y en el caso del metodo 'route' se le pasa el endpoint

@app.route('/')
def inicio():
        #return 'Bienvenido a mi primera API de Flask'
        # Status por defecto es el 200 => OK
        return{
                'message': 'Bienvenido a mi API de Flask'
        }, 200
@app.route('/crear-usuario', methods = ['POST'])
def crearUsuario():
        #request es toda la informacion que me envia el cliente
        data = request.get_json()
        print(data)
        
        #Status 201 => Created
        return{
                'message': 'Usuario creado exitosamente'
        }, 201
# debug => cada vez que la aplicacion cambie automaticamente se reinicie y no tendremos que hacerlo manualmente
app.run(debug=True)
