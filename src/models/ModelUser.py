# Importación de la clase User desde el módulo entities.
from .entities.User import User

# Definición de la clase ModelUser.
# Esta clase actúa como una capa de modelo en el patrón MVC (Modelo-Vista-Controlador),
# interactuando con la base de datos para realizar operaciones relacionadas con los usuarios.


class ModelUser:

    @classmethod
    def login(cls, db, user):
        # Método de clase para manejar el inicio de sesión de un usuario.
        try:
            # Creación de un cursor para interactuar con la base de datos.
            cursor = db.connection.cursor()
            # Consulta SQL para buscar un usuario por su nombre de usuario.
            sql = f"SELECT id, username, password, fullname FROM user WHERE username = '{user.username}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                # Si se encuentra el usuario, se verifica la contraseña.
                # Se crea un objeto User con los datos obtenidos de la base de datos.
                user = User(row[0], row[1], User.check_password(
                    row[2], user.password), row[3])
                return user
            else:
                # Si no se encuentra el usuario, se devuelve None.
                return None
        except Exception as ex:
            # En caso de error, se lanza una excepción.
            raise Exception(ex)

    @classmethod
    def get_by_id(cls, db, id):
        # Método de clase para obtener un usuario por su ID.
        try:
            cursor = db.connection.cursor()
            # Consulta SQL para buscar un usuario por su ID.
            sql = f"SELECT id, username, fullname FROM user WHERE id = {id}"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                # Si se encuentra el usuario, se devuelve un objeto User con los datos.
                return User(row[0], row[1], None, row[2])
            else:
                # Si no se encuentra el usuario, se devuelve None.
                return None
        except Exception as ex:
            # En caso de error, se lanza una excepción.
            raise Exception(ex)
