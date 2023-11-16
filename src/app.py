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


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Error de contraseña...")
        else:
            flash("El usuario no existe...")
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


@app.route('/agregar_asesor')
@login_required
def agregar_asesor():
    form = FormAdd()
    return render_template("agregar_asesor.html", form=form)


@app.route('/guardar_asesor', methods=['POST'])
def guardar_asesor():
    try:
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
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect('/asesores')


@app.route('/asesores')
@login_required
def asesores():
    page = int(request.args.get('page', 1))
    search = request.args.get('search', None)
    estados_civiles = request.args.getlist('estado_civil')
    niveles_estudios = request.args.getlist('nivel_estudios')
    generos = request.args.getlist('genero')
    areas_experiencia = request.args.getlist('area_experiencia')
    export = request.args.get('export', None)
    per_page = 5

    if export:
        return export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    total_asesores = basedatos.count_asesores(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)
    total_pages = math.ceil(total_asesores / per_page)

    if page > total_pages:
        return redirect(url_for('asesores', page=total_pages, search=search, estado_civil=estados_civiles, nivel_estudios=niveles_estudios, genero=generos, area_experiencia=areas_experiencia))

    asesores = basedatos.listar_asesores_pages(
        page, per_page, search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    start_record = ((page - 1) * per_page) + 1
    end_record = min(page * per_page, total_asesores)

    return render_template('asesores.html', asesores=asesores, page=page, total_pages=total_pages, per_page=per_page, start_record=start_record, end_record=end_record, total_records=total_asesores, search=search, estados_civiles=estados_civiles, niveles_estudios=niveles_estudios, generos=generos, areas_experiencia=areas_experiencia)


def export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia):
    # Obtener todos los asesores según los filtros, sin paginación
    asesores = basedatos.listar_asesores_excel(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    # Convertir a DataFrame de Pandas
    df = pd.DataFrame(asesores)

    # Aquí puedes personalizar las columnas o el formato del DataFrame según tus necesidades
    

    # Crear un archivo Excel en memoria
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Asesores')

    output.seek(0)

    return send_file(output, attachment_filename="asesores.xlsx", as_attachment=True)


@app.route('/asesores_info')
@login_required
def asesores_info():
    page = int(request.args.get('page', 1))
    search = request.args.get('search', None)
    estados_civiles = request.args.getlist('estado_civil')
    niveles_estudios = request.args.getlist('nivel_estudios')
    generos = request.args.getlist('genero')
    areas_experiencia = request.args.getlist('area_experiencia')
    export = request.args.get('export', None)
    per_page = 5

    if export:
        return export_asesores(search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    total_asesores = basedatos.count_asesores(
        search, estados_civiles, niveles_estudios, generos, areas_experiencia)
    total_pages = math.ceil(total_asesores / per_page)

    if page > total_pages:
        return redirect(url_for('asesores', page=total_pages, search=search, estado_civil=estados_civiles, nivel_estudios=niveles_estudios, genero=generos, area_experiencia=areas_experiencia))

    asesores = basedatos.listar_asesores_pages(
        page, per_page, search, estados_civiles, niveles_estudios, generos, areas_experiencia)

    start_record = ((page - 1) * per_page) + 1
    end_record = min(page * per_page, total_asesores)

    return render_template('asesores_info.html', asesores=asesores, page=page, total_pages=total_pages, per_page=per_page, start_record=start_record, end_record=end_record, total_records=total_asesores, search=search, estados_civiles=estados_civiles, niveles_estudios=niveles_estudios, generos=generos, areas_experiencia=areas_experiencia)


@app.route("/editar_asesor/<int:id>")
def editar_asesor(id):
    try:
        asesor = basedatos.obtener_asesor(id)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return render_template("editar_asesor.html", asesor=asesor)


@app.route("/actualizar_asesor", methods=['POST'])
def actualizar_asesor():
    id = request.form["id"]
    try:
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
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect("/asesores")


@app.route("/eliminar_asesor", methods=['POST'])
def eliminar_asesor():
    try:
        basedatos.eliminar_asesor(request.form['id'])
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect("/asesores_info")


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
