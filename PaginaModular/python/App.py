from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, current_user, login_user, logout_user,login_required
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

# Models
from models.ModelUser import ModelUser
# Entities
from models.entities.User import User

app = Flask(__name__);
csrf = CSRFProtect()
mysql = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id)

# MySQL connection
class DevelopmentConfig():
    DEBUG = True
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'registro'

config ={
    'development': DevelopmentConfig
}

# Setting
class config: 
    app.secret_key = 'mysecretkey'

@app.route('/registro')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM datos')
    
    return render_template('registro.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        usuario = request.form['usuario']
        correo = request.form['correo']
        password = request.form['password']
        semestre = request.form['semestre']
        carrera = request.form['carrera']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO datos (nombre, apellido, nom_usuario, correo, password, semestre, carrera) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                    (nombre, apellido, usuario, correo, generate_password_hash(password), semestre, carrera))
        mysql.connection.commit()
        flash('Usuario Registrado')
        return redirect(url_for('Index'))


@app.route('/vistalogin')
def Vistalogin():
    return redirect(url_for('login'))

@app.route('/')
def Foro():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        # print (request.form['usuario'])
        # print (request.form['password'])
        user = User(0, request.form['usuario'], request.form['password'])
        logged_user=ModelUser.login(mysql, user)
        if logged_user != None:
            if logged_user.password == True:
                login_user(logged_user)
                return redirect(url_for('perfilusuario'))
            else:
                flash('Contraseña incorrecta')
                return render_template('iniciarsesion.html')
        else:
            flash('Usuario no encontrado')
            return render_template('iniciarsesion.html')
    else:    
        return render_template('iniciarsesion.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/perfilusuario')
@login_required
def perfilusuario():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM datos')
    data = cur.fetchall()
    return render_template('PerfilUsuario.html', usuario = data[0])

def status401(error):
    return redirect(url_for('login'))

def status404(error):
    return "<h1> Pagina no encontrada </h1>", 404

@app.route('/post')
def nuevo_post():
    return render_template('NuevoPost.html')

@app.route('/crearpost', methods=['POST'])
def crear_post():
    if request.method == 'POST':
        titulo = request.form['titulo']
        publicacion = request.form['publicacion']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO publicaciones (titulo, contenido) VALUES (%s, %s)", (titulo, publicacion))
        mysql.connection.commit()
        return redirect(url_for('Foro'))

@app.route('/update', methods = ['POST'])
def update_contact():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        password = request.form['password']
        correo = request.form['email']
        carrera = request.form['carrera']
        semestre = request.form['semestre']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE datos SET nom_usuario=%s,
                    nombre = %s,
                    apellido = %s,
                    password = %s,
                    correo = %s,
                    carrera = %s,
                    semestre = %s 
                    WHERE id = %s""", (usuario, nombre, apellido, generate_password_hash(password), correo, carrera, semestre, current_user.id))
        mysql.connection.commit()
        flash('Contacto actualizado')
        return redirect(url_for('perfilusuario'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto removido')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    csrf.init_app(app)
    app.register_error_handler(401, status401)
    app.register_error_handler(404, status404)
    app.run(port = 3000, debug= True)