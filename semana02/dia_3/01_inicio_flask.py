from flask import Flask, request


# __name__ > devolvera el valor de '__main__' si el archivo en el cual nos encontramos es el archivo principal del proyecto, si no lo es devolvera otro valor y esto le sirve a Flask para poder inicializar correctamente el proyecto
app = Flask(__name__)

usuarios = []
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
        #print(data)
        usuarios.append(data)
        #Status 201 => Created
        return{
                'message': 'Usuario creado exitosamente'
        }, 201

@app.route('/listar-usuarios', methods=['GET'])
def listarUsuarios():
        return{
                'message': 'Los usuarios son',
                'content': usuarios
        }#si no se coloca el status  su valor por defecto es 200 o sera siempre 200

@app.route('/devolver-usuario/<id>', methods=['GET'])
def devolverUsuario(id):
        #todos los parametros de la url seran string, por eso convertismos a entero ene ste caso
        id=int(id)
        total_usuarios = len(usuarios)
        if (total_usuarios - 1) < id:
            return{
               'message': 'Usuario no existe'
            }, 404 #Not Found (No encontrado)
        else:
            usuario_encontrado = usuarios[id]
            return{
               'message': 'Usuario Encontrado',
               'content': usuario_encontrado
            }
#Crear un endpoint para recibir el id por la url y usando el metodo PUT actualizar el contenido del usuario de esa posicion, si no existe emitir un mensaje de que no existe caso contrario, actualizado
@app.route('/actualizar-usuario/<id>', methods=['PUT'])
def actualizarUsuario(id):
    id = int(id)
    total_usuarios = len(usuarios)

    if (total_usuarios - 1) < id:
        return {
            'message': 'Usuario no encontrado'
        }, 404

    # obtenemos la informacion del body y la convertimos a un diccionario
    data = request.get_json()

    usuarios[id] = data

    return {
        'message': 'Usuario actualizado exitosamente',
        'content': usuarios[id]
    }

@app.route('/eliminar-usuario/<id>', methods = ['DELETE'])
def eliminarUsuario(id):
       id = int(id)
       #buscar el usuario si existe con ese id, y si existe eliminarlo
       total_usuarios = len(usuarios)
       if (total_usuarios - 1) < id:
              return{
                     'message': 'Usuario no existe'
              }, 404
       
       usuario_eliminado = usuarios.pop(id)

       return{
            'message': 'El usuario fue eliminado exitosamente',
            'content': usuario_eliminado
       }
# debug => cada vez que la aplicacion cambie automaticamente se reinicie y no tendremos que hacerlo manualmente
app.run(debug=True)
