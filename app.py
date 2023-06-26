from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Entrega Final - 10ASO - Grupo 06 : Adriano, Diogo, Fabio e Rafael"

if __name__ == '__main__':
    app.run()