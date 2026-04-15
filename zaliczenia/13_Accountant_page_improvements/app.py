from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "saldo": 0.0,
            "magazyn": {},
            "historia": []
        }

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_history(data, text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["historia"].append(f"{timestamp} | {text}")



@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()

    if request.method == "POST":
        action = request.form.get("action")


        if action == "zakup":
            name = request.form.get("name")

            try:
                price = float(request.form.get("price"))
                qty = int(request.form.get("qty"))
            except (ValueError, TypeError):
                add_history(data, "Błąd: nieprawidłowe dane zakupu")
                save_data(data)
                return redirect("/")

            if not name:
                add_history(data, "Błąd: brak nazwy produktu")
                save_data(data)
                return redirect("/")

            koszt = price * qty
            data["saldo"] -= koszt
            data["magazyn"][name] = data["magazyn"].get(name, 0) + qty

            add_history(data, f"Zakup: {name}, {qty} szt., koszt {koszt}")


        elif action == "sprzedaz":
            name = request.form.get("name")

            try:
                qty = int(request.form.get("qty"))
            except (ValueError, TypeError):
                add_history(data, "Błąd: ilość musi być liczbą")
                save_data(data)
                return redirect("/")

            if not name:
                add_history(data, "Błąd: brak nazwy produktu")
                save_data(data)
                return redirect("/")

            if data["magazyn"].get(name, 0) >= qty:
                data["magazyn"][name] -= qty

                # możesz zmienić logikę ceny sprzedaży
                price = 10
                przychod = price * qty
                data["saldo"] += przychod

                add_history(data, f"Sprzedaż: {name}, {qty} szt., przychód {przychod}")
            else:
                add_history(data, f"Błąd: brak produktu '{name}' w magazynie")


        elif action == "saldo":
            try:
                value = float(request.form.get("value"))
            except (ValueError, TypeError):
                add_history(data, "Błąd: nieprawidłowa wartość salda")
                save_data(data)
                return redirect("/")

            data["saldo"] += value
            add_history(data, f"Zmiana salda: {value}")


        save_data(data)
        return redirect("/")

    return render_template("index.html", data=data)



@app.route("/historia/")
@app.route("/historia/<int:start>/<int:end>")
def historia(start=None, end=None):
    data = load_data()
    historia = data["historia"]


    if start is None or end is None:
        return render_template("historia.html", historia=historia)


    if start < 0 or end > len(historia) or start >= end:
        error = f"Nieprawidłowy zakres. Dostępny zakres: 0 - {len(historia)-1}"
        return render_template(
            "historia.html",
            historia=historia,
            error=error
        )

    zakres = historia[start:end]

    return render_template("historia.html", historia=zakres)


if __name__ == "__main__":
    app.run(debug=True)