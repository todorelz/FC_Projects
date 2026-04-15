from app import app
from models import db, Saldo, Produkt

with app.app_context():
    saldo = Saldo.query.first()
    produkty = Produkt.query.all()

    suma_magazynu = sum(p.qty for p in produkty)

    print("Saldo:", saldo.value)
    print("Suma produktów:", suma_magazynu)

    if saldo.value < 0:
        print("Uwaga: saldo ujemne!")

    print("Sprawdzenie zakończone")