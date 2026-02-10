saldo = 0.0
magazyn = {}        # {nazwa: {"cena": float, "ilosc": int}}
historia = []       # lista wykonanych operacji


def zapisz_do_pliku(nazwa_pliku="dane.txt"):
    with open(nazwa_pliku, "w", encoding="utf-8") as f:
        f.write("SALDO\n")
        f.write(f"{saldo}\n")

        f.write("MAGAZYN\n")
        for nazwa, dane in magazyn.items():
            f.write(f"{nazwa};{dane['cena']};{dane['ilosc']}\n")

        f.write("HISTORIA\n")
        for wpis in historia:
            f.write(wpis+ "\n")

def wczytaj_z_pliku(nazwa_pliku="dane.txt"):
    global saldo, magazyn, historia

    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as f:
            linie=[linia.strip() for linia in f.readlines()]

        sekcja = None
        for linia in linie:
            if linia in ("SALDO", "MAGAZYN", "HISTORIA"):
                sekcja = linia
                continue

            if sekcja == "SALDO":
                saldo = float(linia)

            elif sekcja == "MAGAZYN":
                nazwa, cena, ilosc = linia.split(";")
                magazyn[nazwa] = {
                    "cena": float(cena),
                    "ilosc": int(ilosc)
                }
            elif sekcja == "HISTORIA":
                historia.append(linia)

    except FileNotFoundError:
        pass


def pokaz_komendy():
    print("""
Dostępne komendy:
saldo
sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec
""")


def cmd_saldo():
    global saldo
    try:
        kwota = float(input("Podaj kwotę (+/-): "))
        saldo += kwota
        historia.append(f"saldo {kwota}")
    except ValueError:
        print("Błędne dane")

def cmd_zakup():
    global saldo
    try:
        nazwa = input("Nazwa produktu: ").lower()
        cena = float(input("Cena: "))
        ilosc = int(input("Ilość: "))

        if cena <= 0 or ilosc <= 0:
            print("Błąd - cena i ilość muszą być dodatnie")
            return

        koszt = cena * ilosc
        if saldo - koszt < 0:
            print("Brak środków na koncie")
            return

        saldo -= koszt

        if nazwa in magazyn:
            magazyn[nazwa]["ilosc"] += ilosc
            magazyn[nazwa]["cena"] = cena
        else:
            magazyn[nazwa] = {"cena": cena, "ilosc": ilosc}

        historia.append(f"zakup {nazwa} {cena} {ilosc}")

    except ValueError:
        print("Błąd danych")

def cmd_sprzedaz():
    global saldo
    try:
        nazwa = input("Nazwa produktu: ").lower()
        if nazwa not in magazyn:
            print("Brak produktu w magazynie")
            return

        cena = float(input("Cena: "))
        ilosc = int(input("Ilość: "))

        if cena <= 0 or ilosc <= 0:
            print("Błąd - cena i ilość muszą być dodatnie")
            return

        if magazyn[nazwa]["ilosc"] < ilosc:
            print("Za mało towaru w magazynie")
            return

        magazyn[nazwa]["ilosc"] -= ilosc
        saldo += cena * ilosc

        historia.append(f"sprzedaż {nazwa} {cena} {ilosc}")

    except ValueError:
        print("Błąd danych")

def cmd_konto():
    print(f"Stan konta: {saldo:.2f} zł")

def cmd_lista():
    if not magazyn:
        print("Magazyn pusty")
        return
    for nazwa, dane in magazyn.items():
        print(f"{nazwa}: {dane['ilosc']} szt., cena {dane['cena']} zł")


def cmd_magazyn():
    nazwa = input("Podaj nazwę produktu: ").lower()
    if nazwa in magazyn:
        dane = magazyn[nazwa]
        print(f"{nazwa}: {dane['ilosc']} szt., cena {dane['cena']:.2f} zł")
    else:
        print("Brak produktu w magazynie")


def cmd_przeglad():
    if not historia:
        print("Brak zapisanych operacji")
        return
    print(f"Dostępny zakres indeksów: [0:{len(historia)-1}]")
    od = input(f"Od (podaj index operacji od której ma zaczynać się przegląd - domyślnie 0: ")
    do = input("Do (podaj index operacji na której ma kończyć się przegląd: ")
    
    try:
        start = int(od) if od else 0
        end = int(do) if do else len(historia)

        if start < 0 or end > len(historia) or end < 0 or start > len(historia) or start > end :
            print(f"Błędny zakres!")
            return

        for i in range(start, end):
            print(f"{i}: {historia[i]}")

    except ValueError:
        print("Błędne dane")
komendy = {
    "saldo": cmd_saldo,
    "zakup": cmd_zakup,
    "sprzedaż": cmd_sprzedaz,
    "konto": cmd_konto,
    "lista": cmd_lista,
    "magazyn": cmd_magazyn,
    "przegląd": cmd_przeglad,
}
if __name__ =="__main__":
    wczytaj_z_pliku()

    while True:
        pokaz_komendy()
        cmd = input("Wybierz komendę: ").strip().lower()

        if cmd == "koniec":
            zapisz_do_pliku()
            break 
        # komendy.get(cmd, "nieznana komenda")()

        elif cmd in komendy:
            komendy[cmd]()
        else:
            print("Nieznana komenda")
    