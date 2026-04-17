from flask import Flask, render_template, request, redirect

app = Flask(__name__)

data = {
    "saldo": 0.0,
    "magazyn": {},
    "historia": []
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "zakup":
            try:
                name = request.form["name"].lower()
                price = float(request.form["price"])
                qty = int(request.form["qty"])
            except:
                data["historia"].append("Błąd: niepoprawne dane zakupu")
                return redirect("/")

            if price <= 0 or qty <= 0:
                data["historia"].append("Błąd: cena i ilość muszą być > 0")
                return redirect("/")

            koszt = price * qty

            if data["saldo"] < koszt:
                data["historia"].append("Błąd: brak środków")
                return redirect("/")

            data["saldo"] -= koszt
            data["magazyn"][name] = data["magazyn"].get(name, 0) + qty

            data["historia"].append(
                f"Zakup: {name}, {qty} szt., koszt {koszt:.2f}"
            )


        elif action == "sprzedaz":
            try:
                name = request.form["name"].lower()
                price = float(request.form["price"])
                qty = int(request.form["qty"])
            except:
                data["historia"].append("Błąd: niepoprawne dane sprzedaży")
                return redirect("/")

            if price <= 0 or qty <= 0:
                data["historia"].append("Błąd: cena i ilość muszą być > 0")
                return redirect("/")

            if name not in data["magazyn"]:
                data["historia"].append(f"Błąd: brak produktu {name}")
                return redirect("/")

            if data["magazyn"][name] < qty:
                data["historia"].append("Błąd: za mało towaru")
                return redirect("/")

            przychod = price * qty
            data["saldo"] += przychod
            data["magazyn"][name] -= qty

            if data["magazyn"][name] == 0:
                del data["magazyn"][name]

            data["historia"].append(
                f"Sprzedaż: {name}, {qty} szt. x {price:.2f}, przychód {przychod:.2f}"
            )


        elif action == "saldo":
            try:
                value = float(request.form["value"])
            except:
                data["historia"].append("Błąd: saldo")
                return redirect("/")

            data["saldo"] += value
            data["historia"].append(f"Zmiana salda: {value:.2f}")

        return redirect("/")

    return render_template("index.html", data=data)


@app.route("/historia/")
@app.route("/historia/<int:start>/<int:end>/")
def historia_view(start=None, end=None):

    historia = data["historia"]

    if len(historia) == 0:
        return render_template("historia.html", historia=[], error="Brak historii")

    if start is None or end is None:
        return render_template("historia.html", historia=historia)

    if start < 0 or end >= len(historia) or start > end:
        return render_template(
            "historia.html",
            historia=historia,
            error="Błędny zakres"
        )

    return render_template(
        "historia.html",
        historia=historia[start:end + 1]
    )


if __name__ == "__main__":
    app.run(debug=True)