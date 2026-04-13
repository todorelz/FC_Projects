from flask import Flask, render_template, request, redirect

app = Flask(__name__)

saldo = 0.0
magazyn = {}
historia = []

@app.route("/", methods=["GET", "POST"])
def index():
    global saldo, magazyn, historia

    if request.method == "POST":
        action = request.form.get("action")

        if action == "zakup":
            name = request.form["name"]
            price = float(request.form["price"])
            qty = int(request.form["qty"])

            koszt = price * qty
            saldo -= koszt
            magazyn[name] = magazyn.get(name, 0) + qty

            historia.append(f"Zakup: {name}, {qty} szt., koszt {koszt}")

        elif action == "sprzedaz":
            name = request.form["name"]
            price = float(request.form["price"])
            qty = int(request.form["qty"])

            if magazyn.get(name, 0) >= qty:
                przychod = price * qty
                saldo += przychod
                magazyn[name] -= qty

                historia.append(f"Sprzedaż: {name}, {qty} szt., przychód {przychod}")

        elif action == "saldo":
            comment = request.form["comment"]
            value = float(request.form["value"])

            saldo += value
            historia.append(f"Zmiana salda: {comment}, {value}")

        return redirect("/")

    return render_template("index.html", saldo=saldo, magazyn=magazyn)


@app.route("/historia/")
@app.route("/historia/<int:line_from>/<int:line_to>/")
def historia_view(line_from=None, line_to=None):
    if line_from is not None and line_to is not None:
        data = historia[line_from:line_to]
    else:
        data = historia

    return render_template("historia.html", historia=data)


if __name__ == "__main__":
    app.run(debug=True)