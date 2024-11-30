from flask import Flask, render_template, request, jsonify
import mysql.connector
import random

app = Flask(__name__)

# Configuración de conexión a la base de datos
db_config = {
    'user': 'root',
    'password': 'mymysqlaccount',
    'host': 'localhost',
    'database': 'Wordle_Andaluz'
}

# Función para obtener una palabra aleatoria
def obtener_palabra():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('SELECT palabra FROM palabrasAndaluzas ORDER BY RAND() LIMIT 1')
    palabra = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return palabra

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener una nueva palabra
@app.route('/nueva_palabra', methods=['GET'])
def nueva_palabra():
    palabra = obtener_palabra()
    return jsonify({'palabra': palabra})

# Ruta para comprobar el intento del jugador
@app.route('/comprobar_intento', methods=['POST'])
def comprobar_intento():
    datos = request.get_json()
    palabra_objetivo = datos['palabra_objetivo']
    intento = datos['intento']
    
    resultado = []
    for i, letra in enumerate(intento):
        if letra == palabra_objetivo[i]:
            resultado.append('verde')  # Letra correcta y en la posición correcta
        elif letra in palabra_objetivo:
            resultado.append('amarillo')  # Letra en la palabra pero en la posición incorrecta
        else:
            resultado.append('gris')  # Letra no está en la palabra
    
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
