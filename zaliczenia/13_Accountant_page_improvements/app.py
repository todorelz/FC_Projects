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

            if not name or price <= 0 or qty <= 0:
                add_history(data, "Błąd: nieprawidłowe dane")
                save_data(data)
                return redirect("/")

            koszt = price * qty

            if data["saldo"] < koszt:
                add_history(data, "Błąd: brak środków")
                save_data(data)
                return redirect("/")

            data["saldo"] -= koszt

            if name in data["magazyn"]:
                old = data["magazyn"][name]
                new_qty = old["ilosc"] + qty
                new_price = (old["cena"] * old["ilosc"] + price * qty) / new_qty

                data["magazyn"][name] = {
                    "ilosc": new_qty,
                    "cena": new_price
                }
            else:
                data["magazyn"][name] = {
                    "ilosc": qty,
                    "cena": price
                }

            add_history(data, f"Zakup: {name}, {qty} szt., koszt {koszt:.2f}")

        elif action == "sprzedaz":
            name = request.form.get("name")

            try:
                qty = int(request.form.get("qty"))
            except (ValueError, TypeError):
                add_history(data, "Błąd: ilość musi być liczbą")
                save_data(data)
                return redirect("/")

            if not name or qty <= 0:
                add_history(data, "Błąd: nieprawidłowe dane")
                save_data(data)
                return redirect("/")

            if name not in data["magazyn"]:
                add_history(data, f"Błąd: brak produktu '{name}'")
                save_data(data)
                return redirect("/")

            if data["magazyn"][name]["ilosc"] < qty:
                add_history(data, "Za mało towaru")
                save_data(data)
                return redirect("/")

            price = data["magazyn"][name]["cena"]
            przychod = price * qty

            data["magazyn"][name]["ilosc"] -= qty

            if data["magazyn"][name]["ilosc"] == 0:
                del data["magazyn"][name]

            data["saldo"] += przychod

            add_history(
                data,
                f"Sprzedaż: {name}, {qty} szt., cena {price:.2f}, przychód {przychod:.2f}"
            )


        elif action == "saldo":
            try:
                value = float(request.form.get("value"))
            except (ValueError, TypeError):
                add_history(data, "Błąd: nieprawidłowa wartość")
                save_data(data)
                return redirect("/")

            data["saldo"] += value
            add_history(data, f"Zmiana salda: {value:.2f}")

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

    if start < 0 or end >= len(historia) or start > end:
        error = f"Nieprawidłowy zakres. Dostępny zakres: 0 - {len(historia)-1}"
        return render_template("historia.html", historia=historia, error=error)

    zakres = historia[start:end + 1]

    return render_template("historia.html", historia=zakres)


if __name__ == "__main__":
    app.run(debug=True)