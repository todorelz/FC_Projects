from flask import Flask, render_template, request, redirect
from models import db, Saldo, Produkt, Historia
from flask_migrate import Migrate

app = Flask(__name__)

# =========================
# KONFIGURACJA
# =========================
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///accountant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


# =========================
# WALIDACJA
# =========================
def safe_float(value):
    try:
        return float(value)
    except:
        return None


def is_valid_positive(value):
    return value is not None and value > 0


# =========================
# INIT SALDO
# =========================
@app.before_request
def create_saldo():
    if not Saldo.query.first():
        db.session.add(Saldo(value=0))
        db.session.commit()


# =========================
# STRONA GŁÓWNA
# =========================
@app.route("/", methods=["GET", "POST"])
def index():
    saldo = Saldo.query.first()

    if request.method == "POST":
        action = request.form.get("action")

        try:

            # =========================
            # ZAKUP
            # =========================
            if action == "zakup":
                name = request.form.get("name")

                price = safe_float(request.form.get("price"))
                qty = safe_float(request.form.get("qty"))

                if not name or not is_valid_positive(price) or not is_valid_positive(qty):
                    db.session.add(Historia(action="Błąd: niepoprawne dane zakupu"))
                    db.session.commit()
                    return redirect("/")

                qty = int(qty)

                koszt = price * qty
                saldo.value -= koszt

                produkt = Produkt.query.filter_by(name=name).first()
                if not produkt:
                    produkt = Produkt(name=name, qty=0)
                    db.session.add(produkt)

                produkt.qty += qty

                db.session.add(Historia(
                    action=f"Zakup: {name}, {qty} szt., koszt {koszt}"
                ))

                db.session.commit()


            # =========================
            # SPRZEDAŻ
            # =========================
            elif action == "sprzedaz":
                name = request.form.get("name")

                qty = safe_float(request.form.get("qty"))

                if not name or not is_valid_positive(qty):
                    db.session.add(Historia(action="Błąd: niepoprawne dane sprzedaży"))
                    db.session.commit()
                    return redirect("/")

                qty = int(qty)

                produkt = Produkt.query.filter_by(name=name).first()

                if not produkt or produkt.qty < qty:
                    db.session.add(Historia(
                        action=f"Błąd sprzedaży: brak produktu {name}"
                    ))
                    db.session.commit()
                    return redirect("/")

                produkt.qty -= qty

                przychod = qty * 10
                saldo.value += przychod

                db.session.add(Historia(
                    action=f"Sprzedaż: {name}, {qty} szt., przychód {przychod}"
                ))

                db.session.commit()


            # =========================
            # ZMIANA SALDA
            # =========================
            elif action == "saldo":
                value = safe_float(request.form.get("value"))

                if not is_valid_positive(value):
                    db.session.add(Historia(action="Błąd: niepoprawna zmiana salda"))
                    db.session.commit()
                    return redirect("/")

                saldo.value += value

                db.session.add(Historia(
                    action=f"Zmiana salda: {value}"
                ))

                db.session.commit()

        except Exception as e:
            db.session.rollback()
            print("Błąd systemu:", e)

        return redirect("/")

    produkty = Produkt.query.all()
    return render_template("index.html", saldo=saldo, produkty=produkty)


# =========================
# HISTORIA + ZAKRES
# =========================
@app.route("/historia/")
@app.route("/historia/<int:start>/<int:end>")
def historia(start=None, end=None):
    query = Historia.query.order_by(Historia.id).all()

    if start is None or end is None:
        return render_template("historia.html", historia=query)

    if start < 0 or end > len(query) or start >= end:
        error = f"Nieprawidłowy zakres. Dostępny: 0 - {len(query)-1}"
        return render_template("historia.html", historia=query, error=error)

    return render_template("historia.html", historia=query[start:end])


# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(debug=True)