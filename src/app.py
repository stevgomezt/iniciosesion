from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
import basedatos
from basedatos import count_asesores, listar_asesores_pages
import math
from math import ceil
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
import pandas as pd
from io import BytesIO

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
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
    numero_documento = IntegerField(
        'numero_documento', validators=[DataRequired()])
    nombre = StringField('nombre', validators=[DataRequired()])
    edad = IntegerField('edad', validators=[DataRequired()])
    genero = StringField('genero', validators=[DataRequired()])
    estado_civil = StringField('estado_civil', validators=[DataRequired()])
    correo = StringField('correo', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    nivel_estudios = StringField('nivel_estudios', validators=[DataRequired()])
    estrato = IntegerField('estrato', validators=[DataRequired()])
    num_hijos = IntegerField('num_hijos', validators=[DataRequired()])
    personas_cargo = IntegerField(
        'personas_cargo', validators=[DataRequired()])
    experiencia = IntegerField('experiencia', validators=[DataRequired()])
    area_experiencia = StringField(
        'area_experiencia', validators=[DataRequired()])
    tiempo_ventas = IntegerField('tiempo_ventas', validators=[DataRequired()])
    experiencia_general = IntegerField(
        'experiencia_general', validators=[DataRequired()])
    otra_area_experiencia = StringField(
        'otra_area_experiencia', validators=[DataRequired()])
    perfil_natural_r = IntegerField(
        'perfil_natural_r', validators=[DataRequired()])
    perfil_natural_e = IntegerField(
        'perfil_natural_e', validators=[DataRequired()])
    perfil_natural_p = IntegerField(
        'perfil_natural_p', validators=[DataRequired()])
    perfil_natural_n = IntegerField(
        'perfil_natural_n', validators=[DataRequired()])
    perfil_natural_a = IntegerField(
        'perfil_natural_a', validators=[DataRequired()])
    perfil_natural_r_ie = IntegerField(
        'perfil_natural_r_ie', validators=[DataRequired()])
    perfil_natural_e_ie = IntegerField(
        'perfil_natural_e_ie', validators=[DataRequired()])
    perfil_natural_p_ie = IntegerField(
        'perfil_natural_p_ie', validators=[DataRequired()])
    perfil_natural_n_ie = IntegerField(
        'perfil_natural_n_ie', validators=[DataRequired()])
    perfil_natural_a_ie = IntegerField(
        'perfil_natural_a_ie', validators=[DataRequired()])
    intensidad_perfil_natural = IntegerField(
        'intensidad_perfil_natural', validators=[DataRequired()])
    energia_natural = IntegerField(
        'energia_natural', validators=[DataRequired()])
    perfil_adaptado_r = IntegerField(
        'perfil_adaptado_r', validators=[DataRequired()])
    perfil_adaptado_e = IntegerField(
        'perfil_adaptado_e', validators=[DataRequired()])
    perfil_adaptado_p = IntegerField(
        'perfil_adaptado_p', validators=[DataRequired()])
    perfil_adaptado_n = IntegerField(
        'perfil_adaptado_n', validators=[DataRequired()])
    perfil_adaptado_a = IntegerField(
        'perfil_adaptado_a', validators=[DataRequired()])
    perfil_adaptado_r_ie = IntegerField(
        'perfil_adaptado_r_ie', validators=[DataRequired()])
    perfil_adaptado_e_ie = IntegerField(
        'perfil_adaptado_e_ie', validators=[DataRequired()])
    perfil_adaptado_p_ie = IntegerField(
        'perfil_adaptado_p_ie', validators=[DataRequired()])
    perfil_adaptado_n_ie = IntegerField(
        'perfil_adaptado_n_ie', validators=[DataRequired()])
    perfil_adaptado_a_ie = IntegerField(
        'perfil_adaptado_a_ie', validators=[DataRequired()])
    toma_decisiones_adaptado = IntegerField(
        'toma_decisiones_adaptado', validators=[DataRequired()])
    intensidad_perfil_adaptado = IntegerField(
        'intensidad_perfil_adaptado', validators=[DataRequired()])
    energia_adaptado = IntegerField(
        'energia_adaptado', validators=[DataRequired()])
    equilibrio_de_energia = IntegerField(
        'equilibrio_de_energia', validators=[DataRequired()])
    modificacion_perfil = IntegerField(
        'modificacion_perfil', validators=[DataRequired()])
    tiempo_formulario = IntegerField(
        'tiempo_formulario', validators=[DataRequired()])
    unidad_tiempo = IntegerField('unidad_tiempo', validators=[DataRequired()])
    color = IntegerField('color', validators=[DataRequired()])
    nombre_perfil = IntegerField('nombre_perfil', validators=[DataRequired()])
    eje_dominante = IntegerField('eje_dominante', validators=[DataRequired()])
    perfil = IntegerField('perfil', validators=[DataRequired()])


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
    try:
        # Intenta insertar los datos del asesor en la base de datos.
        basedatos.insertar_asesor(
            request.form['numero_documento'],
            request.form['nombre'],
            request.form['edad'],
            request.form['genero'],
            request.form['estado_civil'],
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
            request.form['otra_area_experiencia'],
            request.form['perfil_natural_r'],
            request.form['perfil_natural_e'],
            request.form['perfil_natural_p'],
            request.form['perfil_natural_n'],
            request.form['perfil_natural_a'],
            request.form['perfil_natural_r_ie'],
            request.form['perfil_natural_e_ie'],
            request.form['perfil_natural_p_ie'],
            request.form['perfil_natural_n_ie'],
            request.form['perfil_natural_a_ie'],
            request.form['intensidad_perfil_natural'],
            request.form['energia_natural'],
            request.form['perfil_adaptado_r'],
            request.form['perfil_adaptado_e'],
            request.form['perfil_adaptado_p'],
            request.form['perfil_adaptado_n'],
            request.form['perfil_adaptado_a'],
            request.form['perfil_adaptado_r_ie'],
            request.form['perfil_adaptado_e_ie'],
            request.form['perfil_adaptado_p_ie'],
            request.form['perfil_adaptado_n_ie'],
            request.form['perfil_adaptado_a_ie'],
            request.form['toma_decisiones_adaptado'],
            request.form['intensidad_perfil_adaptado'],
            request.form['energia_adaptado'],
            request.form['equilibrio_de_energia'],
            request.form['modificacion_perfil'],
            request.form['tiempo_formulario'],
            request.form['unidad_tiempo'],
            request.form['color'],
            request.form['nombre_perfil'],
            request.form['eje_dominante'],
            request.form['perfil']
        )
    except Exception as e:
        # Imprime el error si ocurre alguno durante la inserción.
        print(f"Ha ocurrido el error {e}")
    finally:
        # Redirige a la página de asesores después de intentar la inserción.
        return redirect('/asesores')


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
            request.form['numero_documento'],
            request.form['nombre'],
            request.form['edad'],
            request.form['genero'],
            request.form['estado_civil'],
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
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
