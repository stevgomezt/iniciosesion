from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
import basedatos

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
    try:
        basedatos.insertar_asesor(
            numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect('/asesores')
# End Add Asesor


# Listar Asesor
@ app.route('/')
@ app.route('/asesores')
@login_required
def asesores():
    try:
        asesores = basedatos.listar_asesores()
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return render_template('asesores.html', asesores=asesores)
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
