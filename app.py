from flask import Flask, render_template
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

@app.route('/')
def index():
    curiosidad = obtener_curiosidad_aleatoria()
    return render_template('index.html', curiosidad=curiosidad)

if __name__ == '__main__':
    app.run(debug=True)
