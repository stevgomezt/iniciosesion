from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
import basedatos
from basedatos import count_asesores, listar_asesores
import math
from math import ceil

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Error de contraseña...")
                return render_template('auth/login.html')
        else:
            flash("El usuario no existe...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

# Add Asesor


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

    # Datos adicionales

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


@app.route('/agregar_asesor')
@login_required
def agregar_asesor():
    form = FormAdd()  # Crea una instancia de tu formulario
    return render_template("agregar_asesor.html", form=form)


@app.route('/guardar_asesor', methods=['POST'])
def guardar_asesor():
    numero_documento = request.form['numero_documento']
    nombre = request.form['nombre']
    edad = request.form['edad']
    genero = request.form['genero']
    estado_civil = request.form['estado_civil']

    correo = request.form['correo']
    telefono = request.form['telefono']
    nivel_estudios = request.form['nivel_estudios']
    estrato = request.form['estrato']
    num_hijos = request.form['num_hijos']
    personas_cargo = request.form['personas_cargo']

    experiencia = request.form['experiencia']
    area_experiencia = request.form['area_experiencia']
    tiempo_ventas = request.form['tiempo_ventas']
    experiencia_general = request.form['experiencia_general']
    otra_area_experiencia = request.form['otra_area_experiencia']

    perfil_natural_r = request.form['perfil_natural_r']
    perfil_natural_e = request.form['perfil_natural_e']
    perfil_natural_p = request.form['perfil_natural_p']
    perfil_natural_n = request.form['perfil_natural_n']
    perfil_natural_a = request.form['perfil_natural_a']
    perfil_natural_r_ie = request.form['perfil_natural_r_ie']
    perfil_natural_e_ie = request.form['perfil_natural_e_ie']
    perfil_natural_p_ie = request.form['perfil_natural_p_ie']
    perfil_natural_n_ie = request.form['perfil_natural_n_ie']
    perfil_natural_a_ie = request.form['perfil_natural_a_ie']
    intensidad_perfil_natural = request.form['intensidad_perfil_natural']
    energia_natural = request.form['energia_natural']
    perfil_adaptado_r = request.form['perfil_adaptado_r']
    perfil_adaptado_e = request.form['perfil_adaptado_e']
    perfil_adaptado_p = request.form['perfil_adaptado_p']
    perfil_adaptado_n = request.form['perfil_adaptado_n']
    perfil_adaptado_a = request.form['perfil_adaptado_a']
    perfil_adaptado_r_ie = request.form['perfil_adaptado_r_ie']
    perfil_adaptado_e_ie = request.form['perfil_adaptado_e_ie']
    perfil_adaptado_p_ie = request.form['perfil_adaptado_p_ie']
    perfil_adaptado_n_ie = request.form['perfil_adaptado_n_ie']
    perfil_adaptado_a_ie = request.form['perfil_adaptado_a_ie']
    toma_decisiones_adaptado = request.form['toma_decisiones_adaptado']
    intensidad_perfil_adaptado = request.form['intensidad_perfil_adaptado']
    energia_adaptado = request.form['energia_adaptado']
    equilibrio_de_energia = request.form['equilibrio_de_energia']
    modificacion_perfil = request.form['modificacion_perfil']
    tiempo_formulario = request.form['tiempo_formulario']
    unidad_tiempo = request.form['unidad_tiempo']
    color = request.form['color']
    nombre_perfil = request.form['nombre_perfil']
    eje_dominante = request.form['eje_dominante']
    perfil = request.form['perfil']

    try:
        basedatos.insertar_asesor(
            numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, perfil_natural_r, perfil_natural_e, perfil_natural_p, perfil_natural_n, perfil_natural_a, perfil_natural_r_ie, perfil_natural_e_ie, perfil_natural_p_ie, perfil_natural_n_ie, perfil_natural_a_ie, intensidad_perfil_natural, energia_natural, perfil_adaptado_r, perfil_adaptado_e, perfil_adaptado_p, perfil_adaptado_n, perfil_adaptado_a, perfil_adaptado_r_ie, perfil_adaptado_e_ie, perfil_adaptado_p_ie, perfil_adaptado_n_ie, perfil_adaptado_a_ie, toma_decisiones_adaptado, intensidad_perfil_adaptado, energia_adaptado, equilibrio_de_energia, modificacion_perfil, tiempo_formulario, unidad_tiempo, color, nombre_perfil, eje_dominante, perfil)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect('/asesores')
# End Add Asesor


# Listar Asesor
# @ app.route('/')
# @ app.route('/asesores')
# @login_required
# def asesores():
#     try:
#         asesores = basedatos.listar_asesores()
#     except Exception as e:
#         print(f"Ha ocurrido el error {e}")
#     finally:
#         return render_template('asesores.html', asesores=asesores)
# Define la cantidad de registros por página

# ROWS_PER_PAGE = 10

@app.route('/asesores')
@login_required
def asesores():
    page = int(request.args.get('page', 1))
    per_page = 7

    total_asesores = basedatos.count_asesores()
    total_pages = math.ceil(total_asesores / per_page)

    if page > total_pages:
        return redirect(url_for('asesores', page=total_pages))

    asesores = basedatos.listar_asesores(page, per_page)

    # Realiza los cálculos antes de renderizar la plantilla
    start_record = ((page - 1) * per_page) + 1
    end_record = min(page * per_page, total_asesores)
    total_records = count_asesores()

    return render_template('asesores.html', asesores=asesores, page=page, total_pages=total_pages, per_page=per_page, start_record=start_record, end_record=end_record, total_records=total_records)

# End Listar Asesor

# Editar Asesor


@ app.route("/editar_asesor/<int:id>")
def editar_asesor(id):
    try:
        asesor = basedatos.obtener_asesor(id)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return render_template("editar_asesor.html", asesor=asesor)


@ app.route("/actualizar_asesor", methods=['POST'])
def actualizar_asesor():
    id = request.form["id"]
    numero_documento = request.form['numero_documento']
    nombre = request.form['nombre']
    edad = request.form['edad']
    genero = request.form['genero']
    estado_civil = request.form['estado_civil']

    correo = request.form['correo']
    telefono = request.form['telefono']
    nivel_estudios = request.form['nivel_estudios']
    estrato = request.form['estrato']
    num_hijos = request.form['num_hijos']
    personas_cargo = request.form['personas_cargo']

    experiencia = request.form['experiencia']
    area_experiencia = request.form['area_experiencia']
    tiempo_ventas = request.form['tiempo_ventas']
    experiencia_general = request.form['experiencia_general']
    otra_area_experiencia = request.form['otra_area_experiencia']
    try:
        basedatos.actualizar_asesor(id, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato,
                                    num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect("/asesores")

# End Editar Asesor


# Eliminar Asesor

@ app.route("/eliminar_articulo", methods=['POST'])
def eliminar_articulo():
    try:
        basedatos.eliminar_articulo(request.form['id'])
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:

        return redirect("/asesores")
# End Eliminar Asesor


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
