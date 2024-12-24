from flask import Flask, render_template, request, jsonify
import mysql.connector
import random
from config import db_config

app = Flask(__name__)

# Configuración de la base de datos

def obtener_curiosidad_aleatoria():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT texto FROM curiosidades")
    curiosidades = [row[0] for row in cursor.fetchall()]
    conn.close()
    return random.choice(curiosidades)

def obtener_palabra_aleatoria():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT palabra FROM palabras")
    palabras = [row[0] for row in cursor.fetchall()]
    conn.close()
    return random.choice(palabras)

@app.route('/')
def index():
    curiosidad = obtener_curiosidad_aleatoria()
    palabra_correcta = obtener_palabra_aleatoria()
    return render_template('index.html', curiosidad=curiosidad, palabra_correcta=palabra_correcta)

if __name__ == '__main__':
    app.run(debug=True)
