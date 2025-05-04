from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, types
#Esta Clase nos va ayudar a poder gestionar las migraciones de nuestro proyecto con la BD
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2029@localhost:5432/prueba_flask'
#al usar flask-sqlalchemy necesita de la instancia de flask la conexion a la base de datos
db = SQLAlchemy(app=app)

#ya con la instanciacion de la clase ya podemos comenzar a utilizar nuestras migraciones
Migrate(app, db)

class Usuario(db.Model):
    #
    #
    #
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    correo = Column(type_=types.Text, nullable=False, unique=True)
    fechaNacimiento = Column(name='fecha_nacimiento', type_=types.DateTime)
    habilitado = Column(type_=types.Boolean, default=True)

    #para modificar el nombre de la tabla en la BD
    __tablename__ = 'usuarios'

@app.route('/')
def inicio():
    hobbies = ['Ir a Pasear', 'Montar Bici', 'Programar', 'Caminar']
    
    return render_template('prueba.html', nombre_desarrollador = 'Esteban AT',
                                            hobbies = hobbies)

@app.route('/usuario', methods = ['POST'])
def crearUsuario():
    data = request.get_json()
    data.get('nombre') #el metodo get en los diccionarios retornoara el valor, y si no existe la llave retornoara None
    #creamos la instancia de un nuevo usuario
    nuevo_usuario = Usuario(nombre = data.get('nombre'),
                            correo = data.get('correo'),
                            fechaNacimiento = data.get('fechaNacimiento'))
    #ahora llamamos a la conexion con la BD para crear una sesion
    db.session.add(nuevo_usuario)
    #para confirmar los cambios que sea de manera permanente
    db.session.commit()

    return{
        'message': 'Usuario creado exitosamente'
    }, 201 #created


@app.route('/usuarios', methods =['GET'])
def listarUsuarios():
    #creamos una nueva sesion para poder conectarnos ala BD
    #SELECT * FROM  usuarios;
    resultado =db.session.query(Usuario).all()

    usuarios = []
    for usuario in resultado:
        usuarios.append({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "fechaNacimiento": usuario.fechaNacimiento.strftime('%Y-%m-%d'),
            "habilitado": usuario.habilitado
        })

    print(usuarios)

    return{
        'message': 'Usuarios encontrados exitosamente',
        'content': usuarios
    }

#para tener una mayor seguridad de que la instancia esta en el archivo principal
if __name__ == '__main__':
    app.run(debug=True)