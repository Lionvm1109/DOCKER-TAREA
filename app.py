import logging
import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, render_template

# Carga las variables definidas en el archivo .env al entorno.
load_dotenv()

app = Flask(__name__)
logger = logging.getLogger(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", 3307)),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "125053792"),
        database=os.getenv("DB_NAME", "escuela"),
    )


@app.route("/")
def index():
    students = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumnos ORDER BY id")
        students = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        logger.warning(
            f"No se pudo conectar a la base de datos, mostrando lista vacía. Error: {e}"
        )

    return render_template("index.html", students=students)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)