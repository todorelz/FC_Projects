# ; Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.
# ; Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.
# ;     Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
# ;     Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
# ;     Polecenie "koniec" - Kończy działanie aplikacji.
# ; Proces tworzenia użytkowników:
# ;     Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# ;     Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
# ;     Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
# ;     Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
# ;     Polecenie "koniec" - Wraca do pierwszego menu.

# ; Proces zarządzania użytkownikami:
# ;     Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# ;     Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
# ;     Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
# ;     Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
# ;     Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
# ;     Polecenie "koniec" - Wraca do pierwszego menu.

class Uczen:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa

class Nauczyciel:
    def __init__(self,imie, przedmiot, klasy):
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


def tworzenie(self):
    while True:
        print(('\nOpcje: uczeń, nauczyciel, wychowawca, koniec'))
        cmd = input('>>> ').lower()

        if cmd == 'uczeń':
            imie = input("Imię i nazwisko ucznia: ")
            klasa = input("Klasa (np 2A): ")
            self.uczniowie.append(Uczen(imie, klasa))

        elif cmd == "nauczyciel":
            imie = input('Imię i Nazwisko nauczyciela: ')
            przedmiot = input("Przedmiot: ")
            klasy = []
            print("Podaj klasy (pusta linia kończy): ")
            while True:
                k = input()
                if k =="":
                    break
                klasy.append(k)
            self.nauczyciele.append(Nauczyciel(imie, przedmiot, klasy))

        elif cmd == "wychowawca":
            imie = input("Imię i nazwisko wychowawcy: ")
            klasa = input("Prowadzona klasa (np 2A): ")
            self.wychowawcy.append(Wychowawca(imie, klasa))

        elif cmd == "koniec":
            break
        else:
            print("nieznana komenda")

def zarzadzanie(self):
    while True:
        print("\nOpcje: klasa, uczeń, nauczyciel, wychowawca, koniec")
        cmd = input('>>> ').lower()

        if cmd =="klasa":
            klasa = input("Podaj klasę: ")

            print("\nUczniowie: ")
            for u in self.uczniowie:
                print("-", u.imie)
        elif cmd == "uczeń":
            imie = input("Imie i nazwisko ucznia: ")
            klasa = None

            for u in self.uczniowie:
                if u.imie == imie:
                    klasa = u.klasa
            if not klasa:
                print("Uczeń nie isnieje")
                continue

            print("Lekcje:")
            for n in self.nauczyciele:
                if klasa in n.klasy:
                    print(f' - {n.przedmiot} ({n.imie})')
        elif cmd == "wychowca":
            imie = input("Imię i nazwisko wychowawcy: ")
            klasa = None

            for w in self.wychowcy:
                if w.imie == imie:
                    klasa = w.klasa
            
            if not klasa:
                print("Brak wychowawcy")
                continue

            print("Uczniowie:")
            for u in self.uczniowie:
                if u.klasa == klasa:
                    print("-", u.imie)
        
        elif cmd == "koniec":
            break
        else:
            print("Nieznana komenda")

szkola = Szkola()
while True:
    print("\nKomendy główne: utwórz, zarządzaj, koniec")
    cmd = input(">>>").lower()

    if cmd == "utwórz":
        szkola.tworzenie()
    elif cmd == "zarządzaj":
        szkola.zarzadzanie()
    elif cmd == "koniec":
        print("Koniec programu")
        break
    else:
        print("Nieznana komenda")