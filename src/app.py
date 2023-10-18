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


@app.route('/asesores')
@login_required
def asesores():
    return render_template('asesores.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


# CRUD
# Add Asesor
class FormAdd(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    precio = IntegerField('Precio', validators=[DataRequired()])


@app.route('/agregar_asesor')
@login_required
def agregar_asesor():
    form = FormAdd()  # Crea una instancia de tu formulario
    return render_template("agregar_asesor.html", form=form)


@app.route('/guardar_asesor', methods=['POST'])
def guardar_asesor():
    nombre = request.form['nombre']
    precio = request.form['precio']
    try:
        basedatos.insertar_asesor(nombre, precio)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect('/agregar_asesor')
# End Add Asesor


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
