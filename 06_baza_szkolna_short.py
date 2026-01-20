class Uczen:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa


class Nauczyciel:
    def __init__(self, imie, przedmiot, klasy):
        self.imie = imie
        self.przedmiot = przedmiot
        self.klasy = klasy


class Wychowawca:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa


class Szkola:
    def __init__(self):
        self.uczniowie = []
        self.nauczyciele = []
        self.wychowawcy = []

    # -------- MENU GŁÓWNE --------
    def uruchom(self):
        while True:
            cmd = input("\nutwórz / zarządzaj / koniec: ").lower()
            if cmd == "utwórz":
                self.utworz()
            elif cmd == "zarządzaj":
                self.zarzadzaj()
            elif cmd == "koniec":
                print("Koniec programu")
                break
            else:
                print("Nieznana komenda")

    # -------- TWORZENIE --------
    def utworz(self):
        while True:
            cmd = input("\nuczeń / nauczyciel / wychowawca / koniec: ").lower()

            if cmd == "uczeń":
                imie = input("Imię i nazwisko: ")
                klasa = input("Klasa: ")
                self.uczniowie.append(Uczen(imie, klasa))

            elif cmd == "nauczyciel":
                imie = input("Imię i nazwisko: ")
                przedmiot = input("Przedmiot: ")
                klasy = []
                print("Podaj klasy (pusta linia kończy):")
                while True:
                    k = input()
                    if k == "":
                        break
                    klasy.append(k)
                self.nauczyciele.append(Nauczyciel(imie, przedmiot, klasy))

            elif cmd == "wychowawca":
                imie = input("Imię i nazwisko: ")
                klasa = input("Klasa: ")
                self.wychowawcy.append(Wychowawca(imie, klasa))

            elif cmd == "koniec":
                break
            else:
                print("Błędna opcja")

    def zarzadzaj(self):
        while True:
            cmd = input("\nklasa / uczeń / nauczyciel / wychowawca / koniec: ").lower()

            if cmd == "klasa":
                klasa = input("Podaj klasę: ")
                print("Uczniowie:")
                for u in self.uczniowie:
                    if u.klasa == klasa:
                        print("-", u.imie)

                print("Wychowawca:")
                for w in self.wychowawcy:
                    if w.klasa == klasa:
                        print("-", w.imie)

            elif cmd == "uczeń":
                imie = input("Imię i nazwisko ucznia: ")
                klasa = None

                for u in self.uczniowie:
                    if u.imie == imie:
                        klasa = u.klasa

                if klasa is None:
                    print("Nie znaleziono ucznia")
                    continue

                print("Lekcje:")
                for n in self.nauczyciele:
                    if klasa in n.klasy:
                        print(f"- {n.przedmiot} ({n.imie})")

            elif cmd == "nauczyciel":
                imie = input("Imię i nazwisko nauczyciela: ")
                for n in self.nauczyciele:
                    if n.imie == imie:
                        print("Prowadzi klasy:", ", ".join(n.klasy))

            elif cmd == "wychowawca":
                imie = input("Imię i nazwisko wychowawcy: ")
                for w in self.wychowawcy:
                    if w.imie == imie:
                        print("Uczniowie:")
                        for u in self.uczniowie:
                            if u.klasa == w.klasa:
                                print("-", u.imie)

            elif cmd == "koniec":
                break
            else:
                print("Błędna opcja")

szkola = Szkola()
szkola.uruchom()