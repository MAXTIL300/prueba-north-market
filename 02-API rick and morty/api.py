from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura_123'

# Función para validar usuario en la DB SQLite


def validar_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
    usuario = cursor.fetchone()
    conn.close()
    return usuario is not None


@app.route('/')
def index():
    # Redirige al login como página inicial
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validar_usuario(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/home')
def home():
    url = 'https://rickandmortyapi.com/api/character/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extraer solo los campos 'type', 'species' e 'image' para todos los personajes
        characters = [{'name': character['name'], 'type': character['type'],
                       'species': character['species'], 'image': character['image']} for character in data['results']]
    else:
        characters = []

    return render_template('index.html', characters=characters)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
