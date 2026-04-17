from flask import Flask, render_template, request, redirect
from models import db, Saldo, Produkt, Historia
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///accountant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)



def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def is_valid_positive(value):
    return value is not None and value > 0



@app.route("/", methods=["GET", "POST"])
def index():
    saldo = Saldo.query.first()
    if not saldo:
        saldo = Saldo(value=0)
        db.session.add(saldo)
        db.session.commit()

    if request.method == "POST":
        action = request.form.get("action")

        try:

   
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

                if saldo.value < koszt:
                    db.session.add(Historia(action="Błąd: brak środków"))
                    db.session.commit()
                    return redirect("/")

                saldo.value -= koszt

                produkt = Produkt.query.filter_by(name=name).first()

                if not produkt:
                    produkt = Produkt(name=name, qty=0, price=price)
                    db.session.add(produkt)
                else:
                    # średnia ważona ceny
                    if produkt.qty > 0:
                        produkt.price = (
                            produkt.price * produkt.qty + price * qty
                        ) / (produkt.qty + qty)
                    else:
                        produkt.price = price

                produkt.qty += qty

                saldo.value = round(saldo.value, 2)

                db.session.add(Historia(
                    action=f"Zakup: {name}, {qty} szt., koszt {koszt:.2f}"
                ))

                db.session.commit()



            elif action == "sprzedaz":
                name = request.form.get("name")

                qty = safe_float(request.form.get("qty"))

                if not name or not is_valid_positive(qty):
                    db.session.add(Historia(action="Błąd: niepoprawne dane sprzedaży"))
                    db.session.commit()
                    return redirect("/")

                qty = int(qty)

                produkt = Produkt.query.filter_by(name=name).first()

                if not produkt:
                    db.session.add(Historia(
                        action=f"Błąd: brak produktu {name}"
                    ))
                    db.session.commit()
                    return redirect("/")

                if produkt.qty < qty:
                    db.session.add(Historia(
                        action="Błąd: za mało towaru"
                    ))
                    db.session.commit()
                    return redirect("/")

                przychod = qty * produkt.price

                produkt.qty -= qty

                if produkt.qty == 0:
                    db.session.delete(produkt)

                saldo.value += przychod
                saldo.value = round(saldo.value, 2)

                db.session.add(Historia(
                    action=f"Sprzedaż: {name}, {qty} szt., cena {produkt.price:.2f}, przychód {przychod:.2f}"
                ))

                db.session.commit()



            elif action == "saldo":
                value = safe_float(request.form.get("value"))

                if value is None:
                    db.session.add(Historia(action="Błąd: niepoprawna wartość"))
                    db.session.commit()
                    return redirect("/")

                saldo.value += value
                saldo.value = round(saldo.value, 2)

                db.session.add(Historia(
                    action=f"Zmiana salda: {value:.2f}"
                ))

                db.session.commit()

        except Exception as e:
            db.session.rollback()
            print("Błąd systemu:", e)

        return redirect("/")

    produkty = Produkt.query.order_by(Produkt.name).all()
    return render_template("index.html", saldo=saldo, produkty=produkty)



@app.route("/historia/")
@app.route("/historia/<int:start>/<int:end>")
def historia(start=None, end=None):
    query = Historia.query.order_by(Historia.id).all()

    if start is None or end is None:
        return render_template("historia.html", historia=query)

    if start < 0 or end >= len(query) or start > end:
        error = f"Nieprawidłowy zakres. Dostępny: 0 - {len(query)-1}"
        return render_template("historia.html", historia=query, error=error)

    return render_template("historia.html", historia=query[start:end + 1])

with app.app_context():
    db.create_all()
    if not Saldo.query.first():
        db.session.add(Saldo(value=0))
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        if not Saldo.query.first():
            db.session.add(Saldo(value=0))
            db.session.commit()

    app.run(debug=True)