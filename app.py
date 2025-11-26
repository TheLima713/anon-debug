from flask import Flask, render_template, request,session
from anonimizador import anonimizar_texto

import requests
import os
import json
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "qualquercoisa"
app.permanent_session_lifetime = timedelta(days=365)

contador_total = 0

@app.route("/", methods=["GET", "POST"])
def index():

    global contador_total
    if not session.get("contou"):
        contador_total += 1
        session["contou"] = True


    if request.method == "POST":
        lei = request.form.get("lei")
        texto = request.form.get("prompt", "")
        if not lei:
            return render_template("index.html", original=None, erro="Selecione uma legislação antes de continuar.", contador=contador_total)
        texto_anon = anonimizar_texto(texto, lei)
        return render_template("index.html", original=texto, anonimizado=texto_anon, contador=contador_total)
    return render_template("index.html", original=None, contador=contador_total)

if __name__ == "__main__":
    app.run(debug=True)
