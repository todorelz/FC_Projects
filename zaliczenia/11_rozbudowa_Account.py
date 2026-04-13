
# Rozbudowa programu accountant
# Arrow down
# Rozbuduj program do zarządzania firmą. Wszystkie funkcjonalności (komendy, zapisywanie i czytanie przy użyciu pliku itp.) pozostają bez zmian.

# Stwórz clasę Manager, która będzie implementowała dwie kluczowe metody - execute i assign. Przy ich użyciu wywołuj poszczególne fragmenty aplikacji. Metody execute i assign powinny zostać zaimplementowane zgodnie z przykładami z materiałów do zajęć.



import os

class Manager:
    def __init__(self, plik="dane.txt"):
        self.saldo = 0.0
        self.magazyn = {}    
        self.historia = []   
        self.plik = plik
        self.komendy = {
            "saldo": self.cmd_saldo,
            "zakup": self.cmd_zakup,
            "sprzedaz": self.cmd_sprzedaz,
            "konto": self.cmd_konto,
            "lista": self.cmd_lista,
            "magazyn": self.cmd_magazyn,
            "przeglad": self.cmd_przeglad
        }
        self.wczytaj_z_pliku()

        
    def zapisz_do_pliku(self):
        with open(self.plik, "w", encoding="utf-8") as f:
            f.write("SALDO\n")
            f.write(f"{self.saldo}\n")
            f.write("MAGAZYN\n")
            for nazwa, dane in self.magazyn.items():
                f.write(f"{nazwa};{dane['cena']};{dane['ilosc']}\n")
            f.write("HISTORIA\n")
            for wpis in self.historia:
                f.write(wpis + "\n")

    def wczytaj_z_pliku(self):
        self.saldo = 0.0
        self.magazyn = {}
        self.historia = []

        if not os.path.exists(self.plik):
            return

        with open(self.plik, "r", encoding="utf-8") as f:
            linie = [linia.strip() for linia in f.readlines()]

        sekcja = None
        for linia in linie:
            if linia in ("SALDO", "MAGAZYN", "HISTORIA"):
                sekcja = linia
                continue

            if sekcja == "SALDO":
                self.saldo = float(linia)
            elif sekcja == "MAGAZYN":
                nazwa, cena, ilosc = linia.split(";")
                self.magazyn[nazwa] = {"cena": float(cena), "ilosc": int(ilosc)}
            elif sekcja == "HISTORIA":
                self.historia.append(linia)


    def pokaz_komendy(self):
        print("""
Dostępne komendy:
saldo
zakup
sprzedaz
konto
lista
magazyn
przeglad
koniec
""")


    def assign(self, operacja, *args):
        if operacja == "saldo":
            self.saldo += args[0]
            self.historia.append(f"saldo {args[0]}")

        elif operacja == "zakup":
            nazwa, cena, ilosc = args

            if cena <= 0 or ilosc <= 0:
                print("Błąd - cena i ilość muszą być dodatnie")
                return False
            koszt = cena * ilosc
            if self.saldo - koszt < 0:
                print("Brak środków na koncie")
                return False
            self.saldo -= koszt
            if nazwa in self.magazyn:
                old_qty = self.magazyn[nazwa]["ilosc"]
                old_price = self.magazyn[nazwa]["cena"]
                self.magazyn[nazwa]["ilosc"] += ilosc
                self.magazyn[nazwa]["cena"] = (old_price * old_qty + cena * ilosc) / self.magazyn[nazwa]["ilosc"]
            else:
                self.magazyn[nazwa] = {"cena": cena, "ilosc": ilosc}
            self.historia.append(f"zakup {nazwa} {cena} {ilosc}")
        elif operacja == "sprzedaz":
            nazwa, cena, ilosc = args
            if cena <= 0 or ilosc <= 0:
                print("Błąd - cena i ilość muszą być dodatnie")
                return False
            if nazwa not in self.magazyn:
                print("Brak produktu w magazynie")
                return False
            if self.magazyn[nazwa]["ilosc"] < ilosc:
                print("Za mało towaru w magazynie")
                return False
            self.magazyn[nazwa]["ilosc"] -= ilosc
            if self.magazyn[nazwa]["ilosc"] == 0:
                del self.magazyn[nazwa]

            self.saldo += cena * ilosc
            self.historia.append(f"sprzedaz {nazwa} {cena} {ilosc}")
        else:
            print("Nieznana operacja")
            return False
        return True

    def execute(self, cmd):
        funkcja = self.komendy.get(cmd)
        if funkcja:
            funkcja()
        else:
            print("Nieznana komenda")


    def cmd_saldo(self):
        try:
            kwota = float(input("Podaj kwotę (+/-): "))
            self.assign("saldo", kwota)
        except ValueError:
            print("Błędne dane")

    def cmd_zakup(self):
        try:
            nazwa = input("Nazwa produktu: ").lower()
            cena = float(input("Cena: "))
            ilosc = int(input("Ilość: "))
            if cena <= 0 or ilosc <= 0:
                print("Błąd - cena i ilość muszą być dodatnie")
                return
            self.assign("zakup", nazwa, cena, ilosc)
        except ValueError:
            print("Błędne dane")

    def cmd_sprzedaz(self):
        try:
            nazwa = input("Nazwa produktu: ").lower()

            if nazwa not in self.magazyn:
                print("Brak produktu w magazynie")
                return

            cena = float(input("Cena: "))
            ilosc = int(input("Ilość: "))

            if cena <= 0 or ilosc <= 0:
                print("Błąd - cena i ilość muszą być dodatnie")
                return

            if self.magazyn[nazwa]["ilosc"] < ilosc:
                print("Za mało towaru w magazynie")
                return

            self.assign("sprzedaz", nazwa, cena, ilosc)
        except ValueError:
            print("Błędne dane")


    def cmd_konto(self):
        print(f"Stan konta: {self.saldo:.2f} zł")


    def cmd_lista(self):
        if not self.magazyn:
            print("Magazyn pusty")
            return
        for nazwa, dane in self.magazyn.items():
            print(f"{nazwa}: {dane['ilosc']} szt., cena {dane['cena']:.2f} zł")


    def cmd_magazyn(self):
        nazwa = input("Podaj nazwę produktu: ").lower()

        if nazwa in self.magazyn:
            dane = self.magazyn[nazwa]
            print(f"{nazwa}: {dane['ilosc']} szt., cena {dane['cena']:.2f} zł")
        else:
            print("Brak produktu w magazynie")


    def cmd_przeglad(self):
        if not self.historia:
            print("Brak zapisanych operacji")
            return
        print(f"Dostępny zakres indeksów: [0:{len(self.historia)-1}]")
        od = input("Od (domyślnie 0): ")
        do = input("Do (domyślnie koniec): ")
        try:
            start = int(od) if od else 0
            end = int(do) if do else len(self.historia)-1
            if start < 0 or end >= len(self.historia) or start > end:
                print("Błędny zakres!")
                return
            for i in range(start, end+1):
                print(f"{i}: {self.historia[i]}")
        except ValueError:
            print("Błędne dane")



if __name__ == "__main__":
    manager = Manager()
    while True:
        manager.pokaz_komendy()
        cmd = input("Wybierz komendę: ").strip().lower()
        if cmd == "koniec":
            manager.zapisz_do_pliku()
            break
        manager.execute(cmd)