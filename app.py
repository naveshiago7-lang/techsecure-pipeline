"""Aplicação simples da TechSecure Solutions (prova de conceito de CI/CD seguro)."""
from flask import Flask, jsonify

APP_VERSION = "1.0.0"  # altere este valor na demonstração para disparar a pipeline

app = Flask(__name__)


@app.route("/")
def home():
    return f"<h1>TechSecure Solutions</h1><p>Esteira CI/CD segura - versão {APP_VERSION}</p>"


@app.route("/health")
def health():
    return jsonify(status="ok", version=APP_VERSION)


if __name__ == "__main__":
    # Uso local apenas. No container a app roda com gunicorn (ver Dockerfile).
    app.run(host="0.0.0.0", port=5000)
