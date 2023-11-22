# Importación de las funciones necesarias para la seguridad de las contraseñas y la autenticación de usuarios.
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

# Definición de la clase User, que hereda de UserMixin.
# UserMixin es una clase proporcionada por Flask-Login que incluye implementaciones
# genéricas de métodos necesarios para manejar sesiones de usuario.


class User(UserMixin):
    def __init__(self, id, username, password, fullname=""):
        # Constructor de la clase User.
        # Inicializa el objeto con id, nombre de usuario, contraseña y nombre completo.
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(cls, hashed_password, password):
        # Método de clase para verificar si una contraseña coincide con su versión hasheada.
        # Utiliza la función check_password_hash de Werkzeug para comparar.
        return check_password_hash(hashed_password, password)


# Generación de una contraseña hasheada.
# Esto es útil para almacenar contraseñas de manera segura en la base de datos.
# La contraseña 'admin' se hashea y se imprime su versión hasheada.
hashed_password = generate_password_hash('admin')
print(hashed_password)

# Generar contrasena 
# Detener servidor ir a archivo elegir contrasena y ejecutar
# Python .\src\models\entities\User.py