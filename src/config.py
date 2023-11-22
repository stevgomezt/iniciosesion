# Clase base para configuraciones
class Config:
    # La clave secreta se utiliza para la seguridad en sesiones y formularios, entre otros.
    # Es importante que esta clave sea difícil de adivinar y única para cada aplicación.
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

# Clase de configuración específica para el entorno de desarrollo


class DevelopmentConfig(Config):
    # DEBUG en True activa el modo de depuración de Flask. Esto es útil durante el desarrollo
    # ya que proporciona errores detallados en la página web si ocurren.
    DEBUG = True

    # Configuraciones para la conexión a la base de datos MySQL.
    # MYSQL_HOST es la dirección del servidor de la base de datos, en este caso, localhost.
    MYSQL_HOST = 'localhost'

    # MYSQL_USER es el nombre de usuario para acceder a la base de datos.
    MYSQL_USER = 'admin'

    # MYSQL_PASSWORD es la contraseña para el usuario especificado anteriormente.
    MYSQL_PASSWORD = 'admin'

    # MYSQL_DB es el nombre de la base de datos a la que se conectará la aplicación.
    MYSQL_DB = 'flask_login'


# Diccionario para mapear el nombre de la configuración a la clase de configuración correspondiente.
# Esto permite cambiar fácilmente entre diferentes configuraciones (por ejemplo, desarrollo, producción).
config = {
    'development': DevelopmentConfig
}
