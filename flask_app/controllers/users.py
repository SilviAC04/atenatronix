from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/registrar')
def show_register_page():
    return render_template("registrar_usuario.html")

@app.route('/register_user', methods = ['POST'])
def register():
    # registro del usuario
    if not User.validate_register(request.form):
        return redirect('/registrar')
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password":bcrypt.generate_password_hash(request.form['password']),
        "birthday":request.form['birthday'],
        "cedula_ruc":request.form['cedula_ruc'],
        "user_type_id":request.form['user_type_id'],
        "empresa_id" : request.form['empresa_id'],
        "direccion_id":1
    }
    print(data)
    session["user_id"] = User.save(data)
    print(session)
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Email o contraseña inválido","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Email o contraseña inválido","login")
        return redirect('/')
    print(user.id)
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/dashboard')
def show_dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session["user_id"]
    }
    this_user = User.get_by_id(data)
    return render_template("dashboard.html", this_user=this_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/Atenatronix')
def show_atenatronix():
    return render_template("Atenatronix.html")