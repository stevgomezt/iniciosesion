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
    if request.method == 'POST':
        # Crea una instancia de usuario con los datos del formulario.
        user = User(0, request.form['username'], request.form['password'])
        # Intenta autenticar al usuario.
        logged_user = ModelUser.login(db, user)
        if logged_user:
            # Verifica si la contraseña es correcta.
            if logged_user.password:
                # Inicia sesión del usuario y redirige a la página de inicio.
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                # Muestra un mensaje de error si la contraseña es incorrecta.
                flash("Error de contraseña...")
        else:
            # Muestra un mensaje si el usuario no existe.
            flash("El usuario no existe...")
    # Muestra la plantilla de login para GET o si la autenticación falla.
    return render_template('auth/login.html')


# Define una ruta para '/logout'.
@app.route('/logout')
def logout():
    # Cierra la sesión del usuario actual.
    logout_user()
    # Redirige al usuario a la página de login.
    return redirect(url_for('login'))


# Define una ruta para '/home' que requiere que el usuario esté autenticado.
@app.route('/home')
@login_required
def home():
    # Muestra la plantilla de la página de inicio.
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


# Define una ruta para '/agregar_asesor' que requiere que el usuario esté autenticado.
@app.route('/agregar_asesor')
@login_required
def agregar_asesor():
    # Crea una instancia del formulario FormAdd.
    form = FormAdd()
    # Renderiza la plantilla 'agregar_asesor.html' pasando el formulario.
    return render_template("agregar_asesor.html", form=form)


# Define una ruta para '/guardar_asesor' que acepta solo métodos POST.
@app.route('/guardar_asesor', methods=['POST'])
def guardar_asesor():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Obtener los datos adicionales del formulario
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

        # Definir los encabezados
        headers = {
            'accept': 'application/json',
        }

        # Definir los datos del formulario
        files = {
            'file': (file.filename, file.stream, 'application/pdf')
        }

        # Realizar la solicitud POST a la URL de Docker
        response = requests.post(DOCKER_URL, headers=headers, files=files)

        # Guardar la respuesta en la base de datos MySQL
        if response.status_code == 200:
            # Obtener el JSON de la respuesta
            json_data = response.json()

            if json_data:  # Verificar si la lista no está vacía
                # Extraer el primer elemento del JSON (la respuesta es una lista con un solo diccionario)
                data = json_data[0]

                # Insertar los datos en la tabla MySQL
                insertar_asesor(tipo_documento, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, tipo_vivienda,
                                estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, data)

            message = 'Información guardada en la base de datos'
            return redirect(url_for('asesores', message=message))
        else:
            return 'Error al procesar el archivo: {}'.format(response.text)


@app.route("/editar_asesor/<int:id>")
def editar_asesor(id):
    try:
        # Intenta obtener los detalles del asesor por su ID.
        asesor = basedatos.obtener_asesor(id)
    except Exception as e:
        # Imprime el error si no se puede obtener la información del asesor.
        print(f"Ha ocurrido el error {e}")
    finally:
        # Renderiza la plantilla para editar el asesor, pasando los detalles del asesor.
        return render_template("editar_asesor.html", asesor=asesor)


@app.route("/actualizar_asesor", methods=['POST'])
def actualizar_asesor():
    # Obtiene el ID del asesor desde el formulario.
    id = request.form["id"]
    try:
        # Intenta actualizar los detalles del asesor con la información proporcionada.
        basedatos.actualizar_asesor(
            id,
            request.form['tipo_documento'],
            request.form['numero_documento'],
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
    except Exception as e:
        # Imprime el error si no se puede actualizar la información del asesor.
        print(f"Ha ocurrido el error {e}")
    finally:
        # Redirige a la página de lista de asesores después de intentar la actualización.
        return redirect("/asesores")


@app.route("/eliminar_asesor", methods=['POST'])
def eliminar_asesor():
    try:
        basedatos.eliminar_asesor(request.form['id'])
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect("/asesores_info")


# Define una ruta para '/asesores' que requiere que el usuario esté autenticado.
@app.route('/asesores')
@login_required
def asesores():
    # Obtiene parámetros de la URL para la paginación y filtros de búsqueda.
    page = int(request.args.get('page', 1))
    search = request.args.get('search', None)
    estados_civiles = request.args.getlist('estado_civil')
    niveles_estudios = request.args.getlist('nivel_estudios')
    generos = request.args.getlist('genero')
    areas_experiencia = request.args.getlist('area_experiencia')
    export = request.args.get('export', None)
    per_page = 5  # Cantidad de registros por página.

    # Si se solicita exportar, llama a la función de exportación.
    if export:
        return export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula el total de asesores y páginas necesarias según los filtros.
    total_asesores = basedatos.count_asesores(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)
    total_pages = math.ceil(total_asesores / per_page)

    # Redirige a la última página si la página solicitada es mayor.
    if page > total_pages:
        return redirect(url_for('asesores', page=total_pages, search=search, estado_civil=estados_civiles, nivel_estudios=niveles_estudios, genero=generos, area_experiencia=areas_experiencia))

    # Obtiene los asesores para la página actual con los filtros aplicados.
    asesores = basedatos.listar_asesores_pages(
        page, per_page, search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula los registros inicial y final en la página actual.
    start_record = ((page - 1) * per_page) + 1
    end_record = min(page * per_page, total_asesores)

    # Renderiza la plantilla 'asesores.html' con los datos de los asesores y parámetros de paginación.
    return render_template('asesores.html', asesores=asesores, page=page, total_pages=total_pages, per_page=per_page, start_record=start_record, end_record=end_record, total_records=total_asesores, search=search, estados_civiles=estados_civiles, niveles_estudios=niveles_estudios, generos=generos, areas_experiencia=areas_experiencia)


def export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia):
    # Obtiene una lista de asesores según los filtros proporcionados, para exportar.
    asesores = basedatos.listar_asesores_excel(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Convierte la lista de asesores a un DataFrame de Pandas.
    df = pd.DataFrame(asesores)

    # Aquí se pueden realizar personalizaciones adicionales en el DataFrame si es necesario.

    # Crea un archivo Excel en memoria.
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Escribe el DataFrame en una hoja de Excel.
        df.to_excel(writer, index=False, sheet_name='Asesores')

    # Mueve el puntero al inicio del archivo en memoria.
    output.seek(0)

    # Envía el archivo Excel generado como respuesta para su descarga.
    return send_file(output, attachment_filename="asesores.xlsx", as_attachment=True)


# Define una ruta para '/asesores_info' que requiere que el usuario esté autenticado.
@app.route('/asesores_info')
@login_required
def asesores_info():
    # Obtiene parámetros de la URL para la paginación y filtros de búsqueda.
    page = int(request.args.get('page', 1))
    search = request.args.get('search', None)
    estados_civiles = request.args.getlist('estado_civil')
    niveles_estudios = request.args.getlist('nivel_estudios')
    generos = request.args.getlist('genero')
    areas_experiencia = request.args.getlist('area_experiencia')
    export = request.args.get('export', None)
    per_page = 5  # Cantidad de registros por página.

    # Si se solicita exportar, llama a la función de exportación.
    if export:
        return export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula el total de asesores y páginas necesarias según los filtros.
    total_asesores = basedatos.count_asesores(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)
    total_pages = math.ceil(total_asesores / per_page)

    # Redirige a la última página si la página solicitada es mayor.
    if page > total_pages:
        return redirect(url_for('asesores_info', page=total_pages, search=search, estado_civil=estados_civiles, nivel_estudios=niveles_estudios, genero=generos, area_experiencia=areas_experiencia))

    # Obtiene los asesores para la página actual con los filtros aplicados.
    asesores = basedatos.listar_asesores_pages(
        page, per_page, search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Calcula los registros inicial y final en la página actual.
    start_record = ((page - 1) * per_page) + 1
    end_record = min(page * per_page, total_asesores)

    # Renderiza la plantilla 'asesores_info.html' con los datos de los asesores y parámetros de paginación.
    return render_template('asesores_info.html', asesores=asesores, page=page, total_pages=total_pages, per_page=per_page, start_record=start_record, end_record=end_record, total_records=total_asesores, search=search, estados_civiles=estados_civiles, niveles_estudios=niveles_estudios, generos=generos, areas_experiencia=areas_experiencia)


def status_401(error):
    # Redirecciona al usuario a la página de inicio de sesión cuando ocurre un error 401 (no autorizado).
    return redirect(url_for('login'))


def status_404(error):
    # Devuelve un mensaje personalizado cuando se encuentra un error 404 (página no encontrada).
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    # Configura la aplicación con la configuración de 'development'.
    app.config.from_object(config['development'])

    # Inicializa CSRF (Cross-Site Request Forgery) protection para la aplicación.
    csrf.init_app(app)

    # Registra manejadores de errores personalizados para errores 401 y 404.
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)

    # Ejecuta la aplicación.
    app.run()
