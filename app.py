import logging
import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template

# Carga las variables definidas en el archivo .env (si existe) al entorno.
load_dotenv()

app = Flask(__name__)
logger = logging.getLogger(__name__)


def get_db_connection():
    # Las credenciales viven únicamente en variables de entorno (ver .env.example).
    # No se les pone un valor por defecto aquí: si faltan, no hay ninguna
    # credencial "de respaldo" escondida en el código fuente.
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
    )

# ---------------------------------------------------------------------------
# Mal ejemplo (NO HACER ESTO): credenciales hardcodeadas en el código fuente.
# Cualquiera que vea este archivo, o el historial de git, vería la contraseña
# real de la base de datos. Y para cambiarla habría que tocar el código en
# vez de solo la variable de entorno.
#
# def get_db_connection():
#     return psycopg2.connect(
#         host="localhost",
#         port="5432",
#         user="postgres",
#         password="root1234",
#         dbname="db",
#     )
# ---------------------------------------------------------------------------


@app.route("/")
def index():
    students = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY student_id")
        students = cursor.fetchall()
        cursor.close()
        conn.close()
    except psycopg2.OperationalError:
        logger.warning("No se pudo conectar a la base de datos, mostrando lista vacía.")
    return render_template("index.html", students=students)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
