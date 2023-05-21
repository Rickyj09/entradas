from flask import Flask, render_template, request,send_file, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from flask_mysqldb import MySQL
from aplicacion.forms import LoginForm, alumno,buscapac,buscxc
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
from sqlalchemy import create_engine
from aplicacion.forms import LoginForm, FormUsuario
import os
import qrcode
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


UPLOAD_FOLDER = os.path.abspath("./static/uploads/")
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'entradas'
mysql = MySQL(app)

# setting
app.secret_key = 'millave'


@login_manager.user_loader
def load_user(user_id):
    return (user_id)


@app.route('/')
def inicio():
    return render_template("inicio.html")







@login_manager.user_loader
def load_user(user_id):
    from aplicacion.models import Usuarios
    return Usuarios.query.get(int(user_id))





@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')


def generar_qr(datos):
    # Crea el objeto QRCode con los datos
    qr = qrcode.QRCode()
    qr.add_data(datos)
    qr.make(fit=True)

    # Crea una imagen PIL (Pillow) con el código QR
    img = qr.make_image(fill='black', back_color='white')

    # Crea un buffer de bytes para almacenar la imagen
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    return buffer




@app.route('/bus_articulo', methods = ['POST', 'GET'])
@login_required
def bus_articulo():
    form = alumno()
    if request.method == 'POST':
        iden = request.form['iden']
        nombres = request.form['nombres']
        fec_nac = request.form['fec_nac']
        telefono1 = request.form['telefono1']
        cursor = mysql.connection.cursor()
        cursor.execute('select CURDATE()')
        fec_compra = cursor.fetchone()
        cursor.execute('insert into datos (nombre,iden,fecha_nacimiento,fecha_compra,telefono) VALUES (%s,%s,%s,%s,%s)',(nombres, iden,fec_nac,fec_compra, telefono1))
        mysql.connection.commit()
        # Genera el código QR con los datos ingresados
        datos = f"ID: {iden}\nNombres: {nombres}\nFecha de Nacimiento: {fec_nac}\nTeléfono: {telefono1}"
        qr_buffer = generar_qr(datos)
        # Obtener la ruta absoluta del directorio 'static/uploads'
        uploads_dir = os.path.join(app.root_path, 'static', 'uploads')    
        # Envía el archivo QR como una respuesta
        return send_file(qr_buffer, mimetype='image/png', attachment_filename='qr_code.png', as_attachment=True)
        #return render_template("home.html")
    return render_template("bus_articulo.html", form=form)





@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404


@app.route('/cons_404', methods=['GET', 'POST'])
def cons_404():
    return render_template('404_cons.html')


@app.route('/login', methods=['get', 'post'])
def login():
    from aplicacion.models import Usuarios
    # Control de permisos
    if current_user.is_authenticated:
        # return 'OK'
        return redirect(url_for("home_alumn"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.query.filter_by(username=form.username.data).first()
        print(user)
        pas1 = Usuarios.query.filter_by(password=form.password.data).first()
        print(pas1)
        pas = user.verify_password(form.password.data)
        print(pas)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        form.username.errors.append("Usuario o contraseña incorrectas.")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('inicio'))


@app.route('/perfil/<username>', methods=["get", "post"])
@login_required
def perfil(username):
    from aplicacion.models import Usuarios
    user = Usuarios.query.filter_by(username=username).first()
    if user is None:
        render_template("404.html")
    form = FormUsuario(request.form, obj=user)
    del form.password
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("inicio"))
    return render_template("usuarios_new.html", form=form, perfil=True)


@login_manager.user_loader
def load_user(user_id):
    from aplicacion.models import Usuarios
    return Usuarios.query.get(int(user_id))




