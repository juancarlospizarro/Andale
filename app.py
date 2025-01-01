from flask import Flask, render_template, request, jsonify
import mysql.connector
import random
from config import db_config
import os

app = Flask(__name__)

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

def obtener_significado_palabra(palabra_expresion):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT significado FROM palabras WHERE palabra = %s", (palabra_expresion,))
    significado = cursor.fetchone()
    conn.close()

    if significado:
        return significado[0]
    else:
        return "Significado no encontrado."

@app.route('/')
def index():
    curiosidad = obtener_curiosidad_aleatoria()
    palabra_expresion = obtener_palabra_aleatoria()
    significado = obtener_significado_palabra(palabra_expresion)
    return render_template('index.html', curiosidad=curiosidad, palabra_expresion=palabra_expresion, significado=significado)

if __name__ == '__main__':
    # Usar el puerto asignado por Render, que generalmente se configura en la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto 5000 por defecto si no se encuentra la variable de entorno PORT
    app.run(host='0.0.0.0', port=port, debug=True)

