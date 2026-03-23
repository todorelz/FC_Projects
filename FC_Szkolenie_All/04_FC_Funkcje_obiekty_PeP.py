# Funkcje

# Funkcje to nazwane i odizolowane fragmenty kodu, które opcjonalnie mogą zwracać wartość: funkcję definiuje się przez jej nazwę, parametry i ciało (kod właściwy funkcji).
# Składnia:
# def nazwa_funkcji(parametr1, parametr2, parametr3, ... ,parametrn): #dwukropek na końcu
#     kod do wykonania linia 1 #zwróć uwagę na wcięcie
#     kod do wykonania linia 2
#     ﻿kod do wykonania linia 3

# Nazwa funkcji, jak i nazwy parametrów mogą zawierać duże i małe litery, cyfry i podkreślenie "_"
# Kod utworzonej tak funkcji nie jest wykonywany w czasie jej deklaracji, jest wykonywany, gdy 
# funkcja zostanie wywołana:

# nazwa_funkcji(parametr1, parametr2, parametr3) #zauważ brak dwukropka

# Jaki problem rozwiązują funkcje?
# Napiszmy prosty kod wypisujący na standardowe wyjście zawartość słownika:

name = "Saldo miesięczne - Styczeń"
row = {"Saldo": 1200, "Wpłaty": 1800, "Wydatki": 1300}

print("*" * 10)
print(name)
print("*" * 10)
for k,v in row.items():
    print("{}: {}".format(k, v))
print("*" * 10)


# powyższy kod jest jak najbardziej prawidłowy i nie ma powodu, by go zmienić. Co, jeśli będziemy chcieli wypisać wiele miesięcy na raz? Możemy zastosować listę

rows = [ 
  ("Styczeń", {"Saldo": 1200, "Wpłaty": 1800, "Wydatki": 1300}), 
  ("Luty", {"Saldo": 1300, "Wpłaty": 1900, "Wydatki": 1200}), 
]

for name, row in rows:  
    print("*" * 10)
    print("Saldo miesięczne: {}".format(name))
    print("*" * 10)
    for k,v in row.items():
        print("{}: {}".format(k, v))
    print("*" * 10)

# Złożoność programu wzrosła, ale jest dalej czytelnie. Dodajmy teraz na początku wyświetlanie danych właściciela:

owner = {"Imię": "Adam", "Nazwisko": "Kowalski"}
rows = [ 
  ("Styczeń", {"Saldo": 1200, "Wpłaty": 1800, "Wydatki": 1300}), 
  ("Luty", {"Saldo": 1300, "Wpłaty": 1900, "Wydatki": 1200}), 
]


print('*** ćwiczenie z właścicielam i obrotami ***')
print("Właściciel konta")
print("*" * 10)
for k,v in owner.items():
    print("{}: {}".format(k, v))
print("*" * 10)

for name, row in rows:  
    print("*" * 10)
    print("Saldo miesięczne: {}".format(name))
    print("*" * 10)
    for k, v in row.items():
        print("{}: {}".format(k, v))
    print("*" * 10)


# Nasz kod się powtarza - zarówno ten odpowiedzialny za wyświetlanie właściciela konta, 
# jak i poszczególnych miesięcy, jest taki sam. W takich przypadkach dla uproszczenia kodu
# możemy użyć funkcji:
print('*** funkcja print_dict ***')
owner = {"Imię": "Adam", "Nazwisko": "Kowalski"}
rows = [ 
  ("Styczeń", {"Saldo": 1200, "Wpłaty": 1800, "Wydatki": 1300}), 
  ("Luty", {"Saldo": 1300, "Wpłaty": 1900, "Wydatki": 1200}), 
]

def print_dict(name, row):
    print("*" * 10)
    print(name)
    print("*" * 10)
    for k,v in row.items():
        print("{}: {}".format(k, v))
    print("*" * 10)
  
print_dict("Właściciel ", owner)
for name, row in rows:
    print_dict("Miesiąc: {}".format(name), row)  


# Dzięki zastosowaniu funkcji mogliśmy zastąpić powtarzające się fragmenty kodu wywołaniem funkcji. 
# Zastanów się, jakie ma to zastosowanie w przypadku usuwania małych błędów. np. co się stanie, 
# jeśli w kodzie bez funkcji popełniłeś/aś błąd, który następnie był skopiowany w wielu miejscach. 
# Co, jeśli zamiast 10 gwiazdek zdecydujesz się na użycie 15?

# Funkcje nie muszą pobierać żadnych parametrów, nic nie stoi też na przeszkodzie by użyć funkcji 
# wewnątrz innej funkcji. W naszym kodzie możemy na przykład dodatkowo stworzyć funkcję drukującą 
# podzielnik treści (10 gwiazdek)
print('---Funkcja z ilością gwardek dodatkowo---')
owner = {"Imię": "Adam", "Nazwisko": "Kowalski"}
rows = [ 
  ("Styczeń", {"Saldo": 1200, "Wpłaty": 1800, "Wydatki": 1300}), 
  ("Luty", {"Saldo": 1300, "Wpłaty": 1900, "Wydatki": 1200}), 
]

def divider():
    print("*" * 10)

def print_dict(name, row):
    divider()
    print(name)
    divider()
    for k,v in row.items():
        print("{}: {}".format(k, v))
    divider()
  
print_dict("Właściciel ", owner)
for name, row in rows:
    print_dict("Miesiąc: {}".format(name), row)  

# Dzięki temu podejściu, jeśli zdecydujemy się, że nasz podzielnik będzie teraz na początku 
# miał znak ">" na końcu "<", a w środku 15 znaków "-", wystarczy zmodyfikować funkcję divider:

def divider():
    print(">" + 15 * "-" + "<")
  
# Do tej pory używaliśmy funkcji jako powtarzalnego bloku kodu, funkcja może również zwracać wartość 
# (lub wartości, jeśli funkcja zwraca na przykład tuple). 
# Do zwrócenia wartości używamy słowa kluczowego "return"
# Napiszmy dla przykładu funkcję, która zwróci prawdopodobny dopełniacz podanego imienia 
# (definicja prosta, tylko dla języka polskiego):

print('---funkcja dla Dopełniacza---')
def name_genitive(name):
    if name[-1] == "a":
        return "{}y".format(name[:-1])
    if name[-1] != "a":
        return "{}a".format(name)

names = ["Adam", "Ewa", "Łukasz", "Iwona"]
for firstname in names:
    print("Wysyłam zaproszenie do {}".format(name_genitive(firstname)))

# Co ważne, funkcja kończy działanie, gdy napotka instrukcję "return". 
# Dzięki temu możemy znacząco uprościć naszą funkcję:

def name_genitive(name):
    if name[-1] == "a":
        return "{}y".format(name[:-1])
    return "{}a".format(name)

# Czasami funkcja może wymagać znaczącej liczby parametrów, gdzie w większości zastosowań 
# parametry mogą się powtarzać. Python umożliwia zadeklarowanie domyślnych wartości, 
# które będą przyjęte, gdy programista nie poda wartości parametru dosłownie. 
# Parametry posiadające wartości domyślne (argumenty opcjonalne), muszą być zawsze za normalnymi parametrami.

# Spróbujmy napisać naszą funkcję divider, tak byśmy mogli podać, jaki będzie środkowy znak 
# i jak często go powtórzymy:

def divider(mul=10, char="*"):
    print(char * mul)

divider()
divider(15)
divider(20, "-")

# Co, jeśli chcemy podać znak, ale z domyślną liczbą powtórzeń? Możemy użyć tej samej deklaracji 
# używając nazwy przekazanego parametru:

divider(char="-")


# Czy parametry mogą być zmodyfikowane wewnątrz funkcji?
print('---Czy parametry mogą być zmodyfikowane wewnątrz funkcji?---')
# Rozważmy następujący kod:

def double_value(a):
    a = a * 2

a = 10
double_value(a)
print(a)

b = "Sample String"
double_value(b)
print(b)

# Powyższy kod wydrukuje na standardowym wyjściu:
# 10
# Sample String

# Wygląda na to, że dla podstawowych typów, takich jak int, czy string, 
# wartość nie będzie zmieniana. Spróbujmy teraz następującego kodu:
print('--double_value2--')
def double_values(row):
    for k,v in row.items():
        row[k] = v*2

sample_dict = {"a": 10, "b": "Sample String"}
double_values(sample_dict)
print(sample_dict["a"])
print(sample_dict["b"])

# Tym razem na standardowym wyjściu otrzymamy następujący wynik:
# 20
# Sample StringSample String

# Przekazanie jako parametru słownika pozwoliło na modyfikacje wartości wewnątrz funkcji.
# Gdzie jest więc różnica? Spójrz na wynik działania funkcji id() na zmiennej:

a = 10
print(id(a))
a = a+ 10
print(id(a))

sample_dict= {"a": 10}
print(id(sample_dict))
sample_dict["a"] += 10
print(id(sample_dict))

# Funkcja id() zwraca abstrakcyjny identyfikator zmiennej w pamięci. 
# Dzięki niej jesteśmy w stanie określić, które typy wartości zmienią lokalizacje przy modyfikacji.
# Wartości, które można zmodyfikować bez usunięcia i ponownego dodania do pamięci nazywamy 
# wartościami Mutable.
# Wartości, których nie można zmieniać bez realokacji, to wartości immutable

# Wartości mutable to: słowniki, zbiory, listy, obiekty.
# Wartości immutable to: liczby całkowite, liczby zmiennoprzecinkowe, ciągi znaków, tuple.

# Wewnątrz funkcji możliwa jest modyfikacja zmiennych z wartościami mutable, zmienne immutable nie będą zmienione.

# *args, **kwargs

# Parametry możemy przekazywać jako lista bądź słownik.
# Aby móc je odczytać, należy użyć specjalnego znaczenia zmiennych.

# Zmienna oznaczona * będzie zawierała listę z podanymi parametrami.
# Zmienna oznaczona ** będzie zawierała słownik z nazwanymi parametrami.

# zwyczajowo zmienne te nazywa się odpowiednio:
# *args, **kwargs

# Koncepcja Obiektu

# Obiekt można postrzegać jako rozszerzoną wersję słownika. 
# Tzn. każdy obiekt zawiera dane w formacie "klucz": "wartość", 
# gdzie klucz musi być ciągiem znaków w określonym formacie. 
# To, co daje obiektom przewagę nad słownikami, to możliwość przypisywania domyślnych wartości, 
# jasno zdefiniowanej struktury oraz interfejsu (funkcji, które działają na wartościach obiektu).

# Klasami nazywamy szablony, na podstawie których tworzone są obiekty.
# Właściwości to zmienne dostępne wewnątrz obiektu.
# Metody to funkcje działające na podanych parametrach i zmiennych wewnątrz obiektu.
# Do metod i właściwości wewnątrz obiektu mamy dostęp poprzez następującą składnię:

# object.property_name
# object.method_name

# Przykładowo, aby odczytać (i wydrukować) właściwość "property_name" z obiektu "object", 
# a następnie zwiększyć wartość "property_name" wewnątrz obiektu, wykonamy następujący kod:

# print(object.property_name)
# object.property_name += 1

# Aby przypisać wynik działania metody "method_name" (z parametrami 1, 2) do zmiennej result:

# result = object.method_name(1, 2)

# Jak widzisz, sposób działania z właściwościami i metodami jest bardzo podobny do działania 
# na zmiennych i funkcjach. Jedyna różnica to prefix w postaci nazwy obiektu i kropki.

# Pewnie kojarzysz wcześniej używaną konstrukcje:

# "ciąg znaków".format(..parametry..)
# Zbieżność składni nie jest przypadkowa. Jest to w istocie użycie metody format klasy str.

# Zgodnie z tym przykładem:
# Klasą (szablonem obiektu) jest "str". Niezależnie od zawartości obiektu klasy 
# zawsze udostępnia te same metody (w tym metodę format).
# Obiektami klasy str są na przykład:

# a = "Ciąg znaków"
# b = str(12344)

# Klasy definiujemy poprzez nazwę:
# class {nazwa klasy}:
#     {deklaracja dostępnych metod }

# A tworzymy poprzez podanie nazwy klasy i parametrów tak, jak w przypadku funkcji:

# obj = ClassName(parametr1, parametr2...)

# Pierwszy kod klasy

# Każda metoda wewnątrz klasy to funkcja (deklarowana we wciętym bloku), 
# która jako pierwszy parametr przyjmuje obiekt na którym pracuje, zwyczajowo używamy nazwy "self".
# Specjalną metodą, którą deklarujemy wewnątrz obiektu, jest metoda __init__. 
# Metoda ta jest wykonywana, gdy obiekt jest tworzony.

# Utwórzmy pierwszą klasę i jej pierwszy obiekt:

class User: # tworzymy klasę o nazwie "User"
    def __init__(self, firstname, lastname): # przy tworzeniu obiektu będą wymagane dwa parametry: firstname, lastname
        self.firstname = firstname # parametr firstname zapiszemy wewnątrz obiektu jako właściwość firstname
        self.lastname = lastname # parametr lastname zapiszemy wewnątrz obiektu jako właściwość lastname		

    def print_hello(self): #ta metoda nie używa parametrów, tylko obiektu, w którym jest zadeklarowana
        print("Hello {} {}".format(self.firstname, self.lastname))

    def print_bye(self): #ta metoda nie używa parametrów, tylko obiektu, w którym jest zadeklarowana
        print("Bye {} {}".format(self.firstname, self.lastname))

# Utwórzmy teraz kilka obiektów naszej klasy, i zobaczmy, jak działają:

user1 = User("Ewa", "Nowak")
user2 = User("Jan", "Kowalski")

user1.print_hello()
user2.print_hello()
user1.print_bye()
user2.print_bye()

# Zauważ, że metody hello i bye pobrały dane z wewnątrz obiektu. 
# Dlaczego podajemy pierwszy parametr self? Metodę można również wykonać poprzez Nazwę klasy:

User.print_hello(user1)

# W ten sposób jawnie widać, skąd bierze się pierwszy parametr.

# Nic nie stoi na przeszkodzie, by zmodyfikować właściwości obiektu poza kodem klasy:

user1 = User("Ewa", "Nowak")
user1.print_hello()
user1.lastname = "Nowacka"
user1.print_hello()

# Właściwości możemy modyfikować wewnątrz metody:

# class Logger:
#     def __init__(self):
#         self.log = []

#     def add(self, msg):
# ﻿        self.log.append(msg)

#     def print(self):
#         print("\n".join(self.log))

# logger = Logger()
# logger.add("first message")
# logger.add("second message")
# logger.print()

print('---przykład sklep internetowy---')
# Przykład zastosowania:

# Zacznijmy od następującego problemu. W sklepie internetowym mamy dostępne produkty, 
# które w zależności od rodzaju są wyceniane na podstawie:
#     Liczby sztuk (cena sztuki x liczba zamówionych sztuk)
#     Liczby paczek (cena paczki * (liczba zamówionych sztuk / liczba sztuk w paczce zaokrąglona w górę) )
#     Wycena na podstawie ilości + ustalony dodatkowy % straty na ścinki, ucięte rogi itp.)
# Rozpocznijmy od znanego nam słownika, czyli zmiennej, która zawiera dane w formacie 
# "klucz": "wartość", która przechowuje parametry produktu:

# #produkt z ceną liczoną według paczek
product_floor_tiles_white = {"price": 120, "size": 15}
product_floor_tiles_black = {"price": 140, "size": 20}
# #produkt z ceną według sztuki
paint_can = {"price": 60}
paint_brush = {"price": 60}
# #produkt z ceną za ilość
planks = {"price": 80, "loss": 0.1, "unit": "metry"}
concrete = {"price": 60, "loss": 0.05, "unit": "kilogramy"} 

# Napiszmy przykładową implementację przez funkcję:

from math import floor  # import funkcji zaokrąglającej w dół

products = {
    "product_floor_tiles_white": {"price": 120, "size": 15},
    "product_floor_tiles_black": {"price": 140, "size": 20},
    "paint_can": {"price": 60},
    "paint_brush": {"price": 60},
    "planks": {"price": 80, "loss": 0.1, "unit": "metry"},
    "concrete": {"price": 60, "loss": 0.05, "unit": "kilogramy"},
}
products_piece = {"paint_can", "paint_brush"}
products_pack = {"product_floor_tiles_white", "product_floor_tiles_black"}
products_amount = {"planks", "concrete"}

# # pierwsze pytanie o ilość/liczbę produktów
def piece_or_pack_ask():
    print("Podaj liczbę sztuk")
    return int(input())

def amount_ask(unit_name):
    print("Podaj ilość ({})".format(unit_name))
    return floor(int(input()))

# oblicz cenę:
def price_piece(price, quantity):
    return quantity * price

def price_pack(price, pack_size, pieces):
    packs = int((pieces + pack_size - 1) / pack_size)
    return packs * price

def price_amount(price, loss, quantity):
    return price * quantity * (1 + loss)

# wydrukuj potiwerdzenie
def piece_print(quantity):
    print("Zamówiono {} liczbę sztuk".format(quantity))

def pack_print(quantity, pack_size):
    packs = int((quantity + pack_size - 1) / pack_size)
    print("Zamówiono {} liczbę paczek".format(packs))

def amount_print(quantity, unit):
    print("Zamówiono {} ({})".format(quantity, unit))

total_price = 0
while True:
    print("Podaj nazwę produktu lub pustą linię jeśli chcesz zakończyć")
    product = input()
    if not product:
        break
    if product not in products:
        print("Błędna nazwa produktu")
        continue
    # zapytajmy o wielkość zamówienia
    if product in products_piece or product in products_pack:
        quantity = piece_or_pack_ask()
    if product in products_amount:
        quantity = amount_ask(products[product]["unit"])
    # wydrukujmy potwierdzenie
    if product in products_piece:
        piece_print(quantity)
    if product in products_pack:
        pack_print(quantity, products[product]["size"])
    if product in products_amount:
        amount_print(quantity, products[product]["unit"])
    # dodajmy cenę
    if product in products_piece:
        total_price += price_piece(products[product]["price"], quantity)
    if product in products_pack:
        total_price += price_pack(products[product]["price"], products[product]["size"], quantity)
    if product in products_amount:
        total_price += price_amount(products[product]["price"], products[product]["loss"], quantity)

print("Całkowity koszt zamówienia {}".format(total_price))

# Kod jest dosyć długi i do tego często pojawia się pytanie jakiego typu jest produkt. 
# Możemy wyróżnić trzy główne akcje każdego produktu:

#     Pytanie o ilość/liczbę produktu
#     Wydruk potwierdzenia
#     Obliczenie ceny

# Zaprojektujmy w takim razie trzy metody, które powinny nam zwracać produkty:

# def ask():
# def print():
# def price():

# Utwórzmy klasy dla każdego z trzech typów produktów:
print('---klasy---')
from math import floor

class ProductPiece:
    def __init__(self, price):
        self.price = price

    def ask(self):
        print("Podaj liczbę sztuk")
        return int(input())

    def print(self, quantity):
        print("Zamówiono {} liczbę sztuk".format(quantity))

    def get_price(self, quantity):
        return quantity * self.price

class ProductPack:
    def __init__(self, price, size):
        self.price = price
        self.size = size

    def ask(self):
        print("Podaj liczbę sztuk")
        return int(input())

    def print(self, quantity):
        packs = int((quantity + self.size - 1) / self.size)
        print("Zamówiono {} liczbę paczek".format(packs))

    def get_price(self, quantity):
        packs = int((quantity + self.size - 1) / self.size)
        return packs * self.price

class ProductAmount:
    def __init__(self, price, loss, unit):
        self.price = price
        self.loss = loss
        self.unit = unit

    def ask(self):
        print("Podaj ilość ({})".format(self.unit))
        return floor(int(input()))

    def print(self, quantity):
        print("Zamówiono {} ({})".format(quantity, self.unit))

    def get_price(self, quantity):
        return self.price * quantity * (1 + self.loss)

# Zauważ, że jest to w większości kod skopiowany z metod print_*, price_*, ask_*

# Przeróbmy resztę kodu tak, by skorzystać z naszych klas. Najpierw deklaracja danych produktów:

products = {
  "product_floor_tiles_white": ProductPack(120, 15),
  "product_floor_tiles_black": ProductPack(140,20),
  "paint_can": ProductPiece(60),
  "paint_brush": ProductPiece(60),
  "planks": ProductAmount(80, 0.1, "metry"),
  "concrete": ProductAmount(60, 0.05, "kilogramy") 
}

# I nasza główna pętla:

total_price = 0
while True:
    print("Podaj nazwę produktu lub pustą linię jeśli chcesz zakończyć")
    product = input()
    if not product:
        break
    if product not in products:
        print("Błędna nazwa produktu")
        continue
    product = products[product]
    # zapytajmy o wielkość zamówienia
    quantity = product.ask()
    # wydrukujmy potwierdzenie
    product.print(quantity)
    # dodajmy cenę
    total_price += product.get_price(quantity)
    
print("Całkowity koszt zamówienia {}".format(total_price))

# Ta część naprawdę robi różnicę. Ten sam kod jest dwukrotnie krótszy i zdecydowanie łatwiejszy do rozszerzania.
# Standardy PEP. Oficjalny standard pisania kodu w pythonie:

# https://www.python.org/dev/peps/pep-0008/

#     wcinamy kod o 4 spacje, nie używamy tabulacji
#     linia powinna mieć maksymalnie 79 znaków
#     2 puste linie przed deklaracją klasy, 1 przed funkcją metodą; unikaj spacji wewnątrz metody funkcji
#     Kodowanie pliku w utf-8
#     linie nie powinny się kończyć pustymi znakami
#     zawsze zapisuj tuple z nawiasami
#     snake_case dla zmiennych i właściwości, CamelCase dla nazw klas
#     STAŁE pisane wielkimi literami ze znakiem"_"
#     uważaj na małe "L" i duże "O" w nazwach zmiennych, szczególnie, gdy jest to zmienna jednoliterowa


