from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Aplicación Web en Python</h1>
    <p>Práctica: GitHub Actions y Azure App Service</p>
    <p>Endpoint disponible: /api/status</p>
    """

@app.route("/api/status")
def status():
    return jsonify({
        "estado": "OK",
        "mensaje": "Aplicación funcionando correctamente",
        "tecnologia": "Python Flask",
        "despliegue": "Azure App Service con GitHub Actions",
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)