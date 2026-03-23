# Import lokalnych plików


# Do tej pory pracowaliśmy na jednym pliku. Takie podejście sprawdzi się 
# tylko w przypadku małych programów, do tego utrudnia znacznie równoległą 
# pracę programistów. Aby skorzystać z klas, funkcji i zmiennych 
# zdefiniowanych w innym pliku, korzystamy z następującej składni:

# import {nazwa liku lokalnego}
# from {nazwa pliku lokalnego} import {nazwa klasy, funkcji lub zmiennej}


# Przykładowo stwórzmy plik helper.py w tym samym katalogu:

# TPL_FORMAT = "Witaj {}"

# def print_hello(firstname):
#     print(TPL_FORMAT.format(firstname))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def length(self):
#         return (self.x*self.x + self.y*self.y) ** 0.5

# Aby zaimportować odpowiedni zmienną, funkcje, klasę z tego pliku 
# w pliku main.py:

from data.helper import TPL_FORMAT
from data.helper import print_hello
from data.helper import Point

# Zaimportowane metody wykonujemy potem tak, jakby były napisane 
# w tym samym pliku:

print(TPL_FORMAT.format("Adam"))
print_hello("Ewa")

p1 = Point(3, 4)
p2 = Point(5, 12)

print(p1.length() + p2.length())


# Import za pomocą składni from ... import możemy również zapisać 
# w jednej linii:

from data.helper import TPL_FORMAT, print_hello, Point

# Istnieje również forma skrótowa pozwalająca na zaimportowanie wszystkich elementów z pliku.

from data.helper import *

# Z uwagi na brak prostej metody sprawdzenia skąd element został zaimportowany, ta metoda jest często 
# niedozwolona w środowiskach produkcyjnych.
# Stwórzmy teraz plik helper2.py z alternatywną formą powitania

# TPL_FORMAT = "Dzień Dobry {}"

# def print_hello(firstname):
#     print(TPL_FORMAT.format(firstname))

# Jest możliwe nadpisanie zaimportowanego elementu innym o tej samej nazwie. 
# Zaktualizujmy nasz plik main.py

from data.helper import TPL_FORMAT
from data.helper import print_hello
from data.helper2 import print_hello
from data.helper import Point

print(TPL_FORMAT.format("Adam"))
print_hello("Ewa")

p1 = Point(3, 4)
p2 = Point(5, 12)

print(p1.length() + p2.length())


# Wynik działania programu:

# Witaj Adam
# Dzień Dobry Ewa
# 18.0

print(f'Zauważ, że funkcja print_hello z pliku helper nie jest teraz dostępna (konflikt nazw). Możemy temu zaradzić przypisując inną nazwę importowanego elementu.') 

from data.helper import print_hello
from data.helper2 import print_hello as print_formal_hello

print_hello("Ewa")
print_formal_hello("Ewa")

print('-'*20)
# Importować możemy również całościowo pliki. Odwołujemy się wówczas w kodzie do importowanych 
# elementów poprzez składnię:
# {{nazwa pliku}}.{{nazwa elementu}}

import data.helper as helper
import data.helper2 as helper2

print(helper.TPL_FORMAT.format("Adam"))
helper.print_hello("Ewa")
helper2.print_hello("Ewa")

p1 = helper.Point(3, 4)
p2 = helper.Point(5, 12)

print(p1.length() + p2.length())

# Również w tym przypadku możemy przypisywać tymczasowe nazwy:

import data.helper2 as helper_formal

# Pliki możemy również importować z podfolderów. Separator katalogu ("/" lub "\") zastępujemy znakiem "."

import data.helper
print('-'*20)
print('PACZKI (zawiera plik __init__.py)')
# Paczki

# Paczka jest odpowiednikiem katalogu w pythonie. 
# Katalog będący paczką powinien zawierać plik __init__.py (może być pusty)
# Gdy zaimportujemy całą paczkę:

# import {{nazwa paczki}}

# w tle zostanie zaimportowany {{nazwa_paczki}}.__init__
# Dodatkowym plikiem specjalnym w paczce jest __main__.py
# W przypadku wykonania kodu jako paczka:

# python -m {{nazwa paczki}}

# zostanie wykonany plik

# {{nazwa paczki}}.__main__.py

# W naszym kodzie możemy odwoływać się do plików wyżej w katalogu, ale tylko gdy katalog nadrzędny jest paczką (zawiera plik __init__.py)
# Do katalogu nadrzędnego przechodzimy poprzez dwie kropki:

# import ..utils

print('-----\n')
print("1\n2\n3")
print('Czytanie z pliku')
# Czytanie z pliku

# Python pozwala na bezpośrednie edytowanie plików tekstowych za pomocą wbudowanej funkcji open():
# Aby zacząć czytać plik najpierw tworzymy deskryptor pliku:

# fd = open(filepath)

# Podana ścieżka może być stałą, jak również zmienną lub wyrażeniem.
# Z otwartego w ten sposób pliku możemy czytać za pomocą (między innymi) następujących metod:

    # fd.read() # czyta całość pliku, zwraca go jako str
    # fd.read(max_bytes)  # czyta całość pliku, zwraca go jako str maksymalnie max_bytes znaków
    # fd.readline()  # czyta jedną linię z pliku
    # fd.readline(max_bytes)  # czyta jedną linię z pliku ale nie więcej niż max_bytes
    # fd.readlines() #czyta całość pliku, zwraca zawartość pliku w postaci listy ciągów znaków (każda linia jako osobny element)
    # fd.readlines(max_bytes) #czyta całość pliku, zwraca zawartość pliku w postaci listy ciągów znaków (każda linia jako osobny element ale nie więcej niż max_bytes znaków)

# Wszystkie powyższe metody zwrócą pusty ciąg znaków, jeśli dotarły do końca pliku.
# Gdy zakończymy pracę z plikiem, należy go zamknąć poprzez wykonanie:

    # fd.close()

# Możliwe jest również czytanie linii pliku w pętli for:
    # fd = open(filepath)
    # for line in fd:
    #     print(line)


# Istnieje również możliwość automatycznego zamknięcia pliku dzięki instrukcji with:

# with open(filepath) as fd:
#     for line in fd:
#         print(line)
# print("Plik jest już zamknięty")


# W momencie opuszczenia bloku with (niezależnie czy z powodu dotarcia do końca bloku, wyjątku, 
# instrukcji break, continue, return - plik zostanie automatycznie zamknięty.


# Pisanie do pliku tekstowego

# Plik tekstowy do pisania otwieramy również poprzez funkcję open(), z drugim parametrem "w" lub "a".

# fd = open(filepath, "w") #w przypadku gdy nadpisujemy całą zawartość pliku
# fd = open(filepath, "a") #w przypadku gdy chcemy dopisać nową zawartość do końca pliku


# do pliku dopisujemy zawartość poprzez metody:

# fd.write(content) # zapisuje łańcuch znaków do pliku
# fd.writelines(lines) #zapisuje listę łańcuchów znaków do pliku


# Content to ciąg znaków.
# Lines to lista ciągów znaków.

# Podobnie jak w przypadku czytania z plików, plik należy zamknąć po zakończeniu operacji na pliku. 
# Instrukcja with jest również dostępna.


