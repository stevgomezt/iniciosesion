# Importaciones necesarias de Flask y otras librerías.
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
import basedatos
from basedatos import count_asesores, listar_asesores_pages, insertar_asesor
import math
from math import ceil
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
import pandas as pd
from io import BytesIO
import requests

# Importación de modelos y entidades para la gestión de usuarios.
from models.ModelUser import ModelUser
from models.entities.User import User

# Inicialización de la aplicación Flask.
app = Flask(__name__)

# URL de Docker donde se debe enviar la solicitud
DOCKER_URL = 'http://localhost:8000/ocr/api/v1/read_pdf/'

# Inicialización de la protección CSRF para la aplicación.
csrf = CSRFProtect()

# Configuración de MySQL para la aplicación Flask.
db = MySQL(app)

# Configuración del gestor de inicio de sesión para Flask.
login_manager_app = LoginManager(app)


# Decorador que registra la función con Flask-Login para cargar un usuario.
@login_manager_app.user_loader
def load_user(id):
    # Obtiene y retorna un usuario por su ID utilizando un modelo de usuario.
    return ModelUser.get_by_id(db, id)


# Define una ruta en la aplicación web para la URL raíz ('/').
@app.route('/')
def index():
    # Redirige al usuario a la página de login.
    return redirect(url_for('login'))


# Define una ruta para '/login' que acepta métodos GET y POST.
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Verifica si la solicitud actual es un POST (indicando que el usuario está intentando iniciar sesión).
    if request.method == 'POST':
        # Crea una instancia del modelo User usando los datos proporcionados en el formulario de inicio de sesión.
        user = User(0, request.form['username'], request.form['password'])

        # Intenta autenticar al usuario con los datos proporcionados.
        logged_user = ModelUser.login(db, user)

        # Si se encontró un usuario en la base de datos y se autenticó correctamente.
        if logged_user:
            # Verifica si la contraseña proporcionada coincide con la contraseña del usuario en la base de datos.
            if logged_user.password:
                # Utiliza la función 'login_user' de Flask-Login para registrar al usuario como logueado.
                login_user(logged_user)
                # Redirige al usuario a la página de inicio después de un inicio de sesión exitoso.
                return redirect(url_for('home'))
            else:
                # Si la contraseña no es correcta, muestra un mensaje de error.
                flash("Error de contraseña...")
        else:
            # Si no se encuentra el usuario en la base de datos, muestra un mensaje indicando que el usuario no existe.
            flash("El usuario no existe...")

    # Si la solicitud es de tipo GET (el usuario está accediendo a la página de inicio de sesión)
    # o si el inicio de sesión falló, muestra la página de inicio de sesión nuevamente.
    return render_template('auth/login.html')


# Define una ruta para '/logout'.
@app.route('/logout')
def logout():
    # Utiliza la función 'logout_user' de Flask-Login para cerrar la sesión del usuario actual.
    # Esto eliminará la sesión del usuario del servidor, desautenticándolo.
    logout_user()
    # Redirige al usuario a la página de inicio de sesión después de cerrar la sesión.
    # Esto previene que el usuario acceda a áreas restringidas sin estar autenticado.
    return redirect(url_for('login'))

# Define una ruta para '/home' que requiere que el usuario esté autenticado para acceder.


@app.route('/home')
# Esta decorador asegura que solo los usuarios autenticados puedan acceder a esta ruta.
@login_required
def home():
    # Si el usuario está autenticado (gracias al decorador 'login_required'),
    # muestra la página principal de la aplicación.
    # 'home.html' es una plantilla que usualmente muestra el contenido principal de la aplicación o sitio web.
    return render_template('home.html')


# Define la clase FormAdd
class FormAdd(FlaskForm):
    tipo_documento = StringField('tipo_documento', validators=[DataRequired()])
    numero_documento = StringField(
        'numero_documento', validators=[DataRequired()])
    nombre = StringField('nombre', validators=[DataRequired()])
    edad = StringField('edad', validators=[DataRequired()])
    genero = StringField('genero', validators=[DataRequired()])
    estado_civil = StringField('estado_civil', validators=[DataRequired()])
    correo = StringField('correo', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    nivel_estudios = StringField('nivel_estudios', validators=[DataRequired()])
    tipo_vivienda = StringField('tipo_vivienda', validators=[DataRequired()])
    estrato = StringField('estrato', validators=[DataRequired()])
    num_hijos = StringField('num_hijos', validators=[DataRequired()])
    personas_cargo = StringField('personas_cargo', validators=[DataRequired()])
    experiencia = StringField('experiencia', validators=[DataRequired()])
    area_experiencia = StringField(
        'area_experiencia', validators=[DataRequired()])
    tiempo_ventas = StringField('tiempo_ventas', validators=[DataRequired()])
    experiencia_general = StringField(
        'experiencia_general', validators=[DataRequired()])
    otra_area_experiencia = StringField(
        'otra_area_experiencia', validators=[DataRequired()])


# Define una ruta para '/agregar_asesor' que requiere que el usuario esté autenticado para acceder.
@app.route('/agregar_asesor')
# Este decorador asegura que solo los usuarios autenticados puedan acceder a esta ruta.
@login_required
def agregar_asesor():
    # Crea una instancia del formulario 'FormAdd'. Este formulario es probablemente utilizado
    # para recopilar la información necesaria para agregar un nuevo asesor a la base de datos.
    form = FormAdd()

    # Renderiza y devuelve la plantilla 'agregar_asesor.html', pasando el formulario al contexto de la plantilla.
    # Esto permite que la plantilla genere los campos del formulario adecuadamente para la entrada del usuario.
    return render_template("agregar_asesor.html", form=form)


# Define una ruta para '/guardar_asesor' que acepta solo métodos POST.
@app.route('/guardar_asesor', methods=['POST'])
def guardar_asesor():
    # Verifica si el formulario de carga incluye un campo de archivo.
    if 'file' not in request.files:
        # Retorna un mensaje si no se encuentra la parte del archivo en el formulario.
        return 'No file part'

    file = request.files['file']  # Obtiene el archivo del formulario.

    # Verifica si se seleccionó un archivo.
    if file.filename == '':
        # Retorna un mensaje si no se seleccionó ningún archivo.
        return 'No selected file'

    # Obtiene el número de documento del formulario.
    numero_documento = request.form['numero_documento']

    # Verifica si el número de documento ya existe en la base de datos.
    if basedatos.existe_numero_documento(numero_documento):
        # Muestra un mensaje indicando que el documento ya está registrado.
        flash('El número de documento ya está registrado')
        # Redirige al usuario a la lista de asesores.
        return redirect(url_for('asesores'))

    # Procede a procesar el archivo si este existe.
    if file:
        # Extrae el resto de los datos del formulario.
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        nombre = request.form['nombre']
        edad = request.form['edad']
        genero = request.form['genero']
        estado_civil = request.form['estado_civil']
        correo = request.form['correo']
        telefono = request.form['telefono']
        nivel_estudios = request.form['nivel_estudios']
        tipo_vivienda = request.form['tipo_vivienda']
        estrato = request.form['estrato']
        num_hijos = request.form['num_hijos']
        personas_cargo = request.form['personas_cargo']
        experiencia = request.form['experiencia']
        area_experiencia = request.form['area_experiencia']
        tiempo_ventas = request.form['tiempo_ventas']
        experiencia_general = request.form['experiencia_general']
        otra_area_experiencia = request.form['otra_area_experiencia']

        # Define los encabezados para la solicitud POST.
        headers = {'accept': 'application/json'}

        # Define los datos del archivo para la solicitud POST.
        files = {'file': (file.filename, file.stream, 'application/pdf')}

        # Envía una solicitud POST a la URL especificada de Docker con los encabezados y el archivo.
        response = requests.post(DOCKER_URL, headers=headers, files=files)

        # Guardar la respuesta en la base de datos MySQL
        # Verifica el código de estado de la respuesta.
        if response.status_code == 200:
            # Convierte la respuesta JSON en datos.
            json_data = response.json()

            # Verifica si el JSON no está vacío.
            if json_data:
                # Extrae los datos necesarios del JSON.
                # Suponiendo que el JSON contiene la información relevante en la primera posición.
                data = json_data[0]

                # Inserta los datos en la base de datos.
                basedatos.insertar_asesor(tipo_documento, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, tipo_vivienda,
                                          estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, data)

                # Notifica al usuario que la información se ha guardado correctamente.
                flash('Información guardada en la base de datos')
                # Redirige al usuario a la lista de asesores.
                return redirect(url_for('asesores'))
        else:
            # Retorna un mensaje de error si la solicitud POST no fue exitosa.
            return 'Error al procesar el archivo: {}'.format(response.text)


@app.route("/editar_asesor/<int:id>")
def editar_asesor(id):
    try:
        # Intenta obtener los detalles del asesor por su ID utilizando la función 'obtener_asesor' del módulo 'basedatos'.
        # Esto se hace para llenar previamente el formulario de edición con los datos actuales del asesor.
        asesor = basedatos.obtener_asesor(id)
    except Exception as e:
        # Si ocurre un error durante la obtención de los datos del asesor (por ejemplo, problema de conexión a la base de datos),
        # imprime el mensaje de error en la consola del servidor para propósitos de depuración.
        print(f"Ha ocurrido el error {e}")
        # Podrías manejar esto de manera diferente, como redirigir al usuario a otra página o mostrar un mensaje de error específico.
    finally:
        # Independientemente de si la operación anterior fue exitosa o no, renderiza la plantilla 'editar_asesor.html'.
        # Si hubo un error, 'asesor' podría no estar definido, así que asegúrate de manejar eso en tu plantilla HTML.
        # En el escenario exitoso, 'asesor' contendrá los datos del asesor que se pueden utilizar para llenar el formulario de edición.
        return render_template("editar_asesor.html", asesor=asesor)


@app.route("/ver_asesor/<int:id>")
def ver_asesor(id):
    try:
        # Intenta obtener los detalles del asesor por su ID utilizando la función 'obtener_asesor' del módulo 'basedatos'.
        # Esto se hace para llenar previamente el formulario de edición con los datos actuales del asesor.
        asesor = basedatos.obtener_asesor(id)
    except Exception as e:
        # Si ocurre un error durante la obtención de los datos del asesor (por ejemplo, problema de conexión a la base de datos),
        # imprime el mensaje de error en la consola del servidor para propósitos de depuración.
        print(f"Ha ocurrido el error {e}")
        # Podrías manejar esto de manera diferente, como redirigir al usuario a otra página o mostrar un mensaje de error específico.
    finally:
        # Independientemente de si la operación anterior fue exitosa o no, renderiza la plantilla 'ver_asesor.html'.
        # Si hubo un error, 'asesor' podría no estar definido, así que asegúrate de manejar eso en tu plantilla HTML.
        # En el escenario exitoso, 'asesor' contendrá los datos del asesor que se pueden utilizar para llenar el formulario de edición.
        return render_template("ver_asesor.html", asesor=asesor)


@app.route("/actualizar_asesor", methods=['POST'])
def actualizar_asesor():
    # Recupera el ID del asesor desde el formulario, necesario para identificar cuál registro actualizar.
    id = request.form["id"]

    # Recupera el número de documento del asesor desde el formulario.
    numero_documento = request.form['numero_documento']

    # Verifica si el número de documento ya está registrado bajo un asesor diferente para evitar duplicados.
    if basedatos.existe_otro_numero_documento(numero_documento, id):
        # Notifica al usuario que el número de documento ya está en uso y redirige a la página de edición.
        flash('El número de documento ya está registrado con otro asesor')
        # Redirige al usuario a la página de la lista de asesores para que intente de nuevo.
        return redirect(url_for('asesores', id=id))

    try:
        # Intenta actualizar los detalles del asesor en la base de datos usando los datos proporcionados.
        # Se llama a la función de actualización de la base de datos y se pasan todos los campos del formulario.
        basedatos.actualizar_asesor(
            id,
            request.form['tipo_documento'],
            numero_documento,
            request.form['nombre'],
            request.form['edad'],
            request.form['genero'],
            request.form['estado_civil'],
            request.form['tipo_vivienda'],
            request.form['correo'],
            request.form['telefono'],
            request.form['nivel_estudios'],
            request.form['estrato'],
            request.form['num_hijos'],
            request.form['personas_cargo'],
            request.form['experiencia'],
            request.form['area_experiencia'],
            request.form['tiempo_ventas'],
            request.form['experiencia_general'],
            request.form['otra_area_experiencia']
        )
        # Notifica al usuario que los datos se actualizaron exitosamente.
        flash('Información de asesor actualizada')
    except Exception as e:
        # Si ocurre algún error durante la actualización, imprime el error y notifica al usuario.
        print(f"Ha ocurrido el error {e}")
        flash('No se pudo actualizar la información del asesor')

    # Redirige al usuario a la página de listado de asesores después de intentar la actualización.
    return redirect(url_for('asesores'))


@app.route("/eliminar_asesor", methods=['POST'])
def eliminar_asesor():
    try:
        # Intenta eliminar un asesor específico usando la función 'eliminar_asesor' del módulo 'basedatos'.
        # El ID del asesor a eliminar se recupera del formulario enviado con la solicitud POST.
        basedatos.eliminar_asesor(request.form['id'])
    except Exception as e:
        # Si ocurre un error durante el proceso de eliminación, imprime el mensaje de error.
        # Esto es útil para la depuración y para entender qué fue mal durante la operación de eliminación.
        print(f"Ha ocurrido el error {e}")
    finally:
        # Redirige al usuario a la página que lista la información de los asesores, '/asesores_info',
        # donde puede ver el estado actualizado de los asesores tras la eliminación.
        return redirect("/asesores_info")


@app.route('/asesores')
# Requiere que el usuario esté autenticado para acceder a esta ruta.
@login_required
def asesores():
    # Obtiene parámetros de la URL para controlar la paginación y los filtros de búsqueda.
    # Obtiene la página actual de los parámetros de la URL, con un valor predeterminado de 1.
    page = int(request.args.get('page', 1))
    # Obtiene el término de búsqueda, si existe.
    search = request.args.get('search', None)
    # Obtiene una lista de estados civiles para filtrar, si se proporcionan.
    estados_civiles = request.args.getlist('estado_civil')
    # Obtiene una lista de niveles de estudios para filtrar.
    niveles_estudios = request.args.getlist('nivel_estudios')
    # Obtiene una lista de géneros para filtrar.
    generos = request.args.getlist('genero')
    # Obtiene una lista de áreas de experiencia para filtrar.
    areas_experiencia = request.args.getlist('area_experiencia')
    # Comprueba si el usuario ha solicitado exportar los datos.
    export = request.args.get('export', None)

    # Define la cantidad de registros por página para la paginación.
    per_page = 11

    # Si el usuario solicitó la exportación, ejecuta la función de exportación y devuelve el resultado.
    if export:
        return export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula el número total de asesores que coinciden con los filtros de búsqueda.
    total_asesores = basedatos.count_asesores(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)
    # Calcula el número total de páginas necesarias.
    total_pages = math.ceil(total_asesores / per_page)

    # Si la página solicitada es mayor que el número total de páginas, redirige al usuario a la última página.
    if page > total_pages:
        return redirect(url_for('asesores', page=total_pages, search=search, estado_civil=estados_civiles, nivel_estudios=niveles_estudios, genero=generos, area_experiencia=areas_experiencia))

    # Obtiene la lista de asesores para la página actual, aplicando los filtros especificados.
    asesores = basedatos.listar_asesores_pages(
        page, per_page, search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula los números de los registros inicial y final que se están mostrando en la página actual.
    start_record = ((page - 1) * per_page) + 1
    end_record = min(page * per_page, total_asesores)

    # Renderiza y devuelve la plantilla 'asesores.html', pasando todos los datos necesarios para mostrar la lista de asesores y los controles de paginación.
    return render_template('asesores.html', asesores=asesores, page=page, total_pages=total_pages, per_page=per_page, start_record=start_record, end_record=end_record, total_records=total_asesores, search=search, estados_civiles=estados_civiles, niveles_estudios=niveles_estudios, generos=generos, areas_experiencia=areas_experiencia)


def export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia):
    # Obtiene una lista de asesores aplicando los filtros especificados.
    # Esta lista se recupera desde la base de datos utilizando la función 'listar_asesores_excel' del módulo 'basedatos'.
    asesores = basedatos.listar_asesores_excel(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Convierte la lista de asesores en un DataFrame de Pandas para facilitar la manipulación de datos y la exportación.
    # Cada elemento de la lista (asesor) se convierte en una fila en el DataFrame.
    df = pd.DataFrame(asesores)

    # (En esta parte del código, podrías añadir personalizaciones adicionales al DataFrame si es necesario.
    # Por ejemplo, podrías cambiar nombres de columnas, formatear datos, etc.)

    # Crea un buffer de memoria para el archivo Excel. Esto permite generar el archivo en la memoria sin necesidad de guardarlo en disco.
    output = BytesIO()

    # Utiliza un gestor de contexto para escribir el DataFrame a un archivo Excel.
    # 'pd.ExcelWriter' se utiliza junto con el buffer y se especifica 'openpyxl' como motor de escritura.
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Escribe el DataFrame al archivo Excel, sin incluir el índice de Pandas.
        df.to_excel(writer, index=False, sheet_name='Asesores')

    # Mueve el puntero del archivo al inicio del buffer. Esto es necesario porque la escritura del archivo
    # Excel deja el puntero al final del archivo, y necesitamos empezar desde el principio para enviar el archivo.
    output.seek(0)

    # Envía el archivo Excel generado como una respuesta descargable en el navegador del usuario.
    # 'attachment_filename' especifica el nombre del archivo que verá el usuario al descargarlo.
    return send_file(output, attachment_filename="asesores.xlsx", as_attachment=True)


# Define una ruta para '/asesores_info' que requiere que el usuario esté autenticado.
@app.route('/asesores_info')
# Asegura que solo usuarios autenticados puedan acceder a esta página.
@login_required
def asesores_info():
    # Obtiene parámetros de la URL utilizados para la paginación y los filtros de búsqueda.
    # Número de página actual con valor predeterminado de 1.
    page = int(request.args.get('page', 1))
    # Término de búsqueda si se proporcionó alguno.
    search = request.args.get('search', None)
    # Filtro por estado civil.
    estados_civiles = request.args.getlist('estado_civil')
    # Filtro por nivel de estudios.
    niveles_estudios = request.args.getlist('nivel_estudios')
    generos = request.args.getlist('genero')  # Filtro por género.
    # Filtro por área de experiencia.
    areas_experiencia = request.args.getlist('area_experiencia')
    # Verifica si se ha solicitado exportación de datos.
    export = request.args.get('export', None)

    # Define la cantidad de registros que se muestran por página.
    per_page = 11

    # Verifica si se debe realizar una exportación en base a los filtros aplicados.
    if export:
        # Llama a la función 'export_asesores' para exportar los datos según los filtros aplicados.
        return export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula el total de asesores que coinciden con los filtros de búsqueda para determinar la paginación.
    total_asesores = basedatos.count_asesores(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)
    # Total de páginas necesarias.
    total_pages = math.ceil(total_asesores / per_page)

    # Si la página actual es mayor que el total de páginas, redirecciona a la última página disponible.
    if page > total_pages:
        return redirect(url_for('asesores_info', page=total_pages, search=search, estado_civil=estados_civiles, nivel_estudios=niveles_estudios, genero=generos, area_experiencia=areas_experiencia))

    # Obtiene la lista de asesores para la página actual aplicando los filtros de búsqueda.
    asesores = basedatos.listar_asesores_pages(
        page, per_page, search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula el número del primer y último registro mostrado en la página actual.
    start_record = ((page - 1) * per_page) + 1
    end_record = min(page * per_page, total_asesores)

    # Renderiza la página 'asesores_info.html', pasando todos los datos y parámetros necesarios para la vista.
    return render_template('asesores_info.html', asesores=asesores, page=page, total_pages=total_pages, per_page=per_page, start_record=start_record, end_record=end_record, total_records=total_asesores, search=search, estados_civiles=estados_civiles, niveles_estudios=niveles_estudios, generos=generos, areas_experiencia=areas_experiencia)


def status_401(error):
    # Esta función maneja los errores de tipo 401, que ocurren cuando un usuario intenta acceder a un recurso para el cual no está autorizado.
    # Redirige al usuario a la página de inicio de sesión, lo que puede ayudar en casos donde la sesión ha expirado o no se ha iniciado sesión.
    return redirect(url_for('login'))


def status_404(error):
    # Esta función maneja los errores de tipo 404, que ocurren cuando se solicita una página o recurso que no existe en el servidor.
    # Devuelve una respuesta HTML simple que indica que la página solicitada no se pudo encontrar.
    # El '404' al final especifica el código de estado HTTP que se debe enviar junto con la respuesta.
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    # Este bloque de código se ejecuta si este script se está ejecutando como el programa principal (es decir, no se importa desde otro script).

    # Configura la aplicación Flask para usar la configuración especificada en el objeto 'config' bajo la clave 'development'.
    # Esto generalmente incluye configuraciones como la cadena de conexión a la base de datos, secretos de la aplicación, etc.
    app.config.from_object(config['development'])

    # Inicializa la protección contra Cross-Site Request Forgery (CSRF) para la aplicación.
    # Esto es importante para la seguridad de la aplicación, evitando ataques donde un sitio malicioso puede realizar solicitudes no autorizadas.
    csrf.init_app(app)

    # Registra funciones de manejo de errores personalizadas para los códigos de estado 401 y 404.
    # Esto asegura que los usuarios reciban respuestas más amigables o útiles cuando encuentren estos errores.
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)

    # Ejecuta la aplicación Flask, iniciando el servidor web integrado.
    # Por defecto, Flask escuchará en el puerto 5000 y solo será accesible localmente ('localhost').
    # Puedes pasar argumentos adicionales a 'run()' para cambiar la configuración predeterminada, como 'host' o 'port'.
    app.run()
