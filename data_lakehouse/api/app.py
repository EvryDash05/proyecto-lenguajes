from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from flask_cors import CORS
from sqlalchemy import text
from pathlib import Path
import os

from routes import blueprints

APP_ROOT = Path(str(Path(__file__).parent)).absolute()

app = Flask(__name__)

print(f"APP ROOT => {APP_ROOT}")

# Configuración de CORS perimiento cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})
load_dotenv(os.path.join(APP_ROOT, "..", ".env"))

# Configuración de credenciales para la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(os.getenv("DB_URI"))

for bp in blueprints:
    app.register_blueprint(bp)

# Verificación de conexión a la base de datos
with engine.connect() as connect:
    try:
        result = connect.execute(text("SELECT 1"))
        print(result.fetchone())
    except Exception as e:
        print(f"Error connecting to database: {e}")

@app.route("/")
def index() -> str:
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)
