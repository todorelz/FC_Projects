# Wbudowane pakiety

# Do tej pory używaliśmy składni import X oraz from X import Y do importowania 
# własnych plików źródłowych. Ta sama składnia służy do importowana wbudowanych pakietów pythona.

# Pełna lista pakietów dostępna jest w oficjalnej dokumentacji:
# https://docs.python.org/3/library/index.html
# Pakiet sys (zbiór przydatnych funkcji systemowych)

# Znasz już jedną z przydatnych funkcjonalności z pakietu sys - 
# listę przekazanch argumentów w zmiennej argv.

import sys
print("Nazwa skryptu: {}".format(sys.argv[0]))

# lub

from sys import argv
print("Nazwa skryptu: {}".format(argv[0]))

# Pakiet ten zawiera również inne przydatne funkcjonalności, przykładowo:

import sys

sys.stdin #deskryptor standardowego wejścia
sys.stdout #deskryptor standardowego wyjścia
sys.stderr #deskryptor standardowego wyjścia błędów

# Deskryptory pozwalają na pracę ze standardowymi strumieniami tak, 
# jakby były to deskryptory plików. Dzięki temu np. na standardowym wejściu możemy użyć 
# np. funkcji readline.

sys.platform # ciąg znaków identyfikujący platformę, przydatny, gdy chcemy np. zaimplementować unikalne funkcjonalności ze względu na system operacyjny
sys.maxsize # wartość 2^64-1 dla systemów 64 bitowych, 2^32-1 dla 32 bitowych

# Pakiet os

# Ten pakiet zawiera implementacje funkcjonalności związanych z obsługą systemu plików 
# oraz uprawnieniami i użytkownikami systemu terminala itp.

import os

# os.unlink(path) # usuwanie pliku
# os.getlogin() # zwraca nazwę zalogowanego użytkownika
# os.getpid() # zwraca id obecnego procesu
# os.terminal_size # zwraca tuple (liczba kolumn, liczba wierszy) w obecnie uruchomionym terminalu
# os.getcwd() # zwraca obecny ROBOCZY katalog
# os.mkdir(path) #tworzy katalog pod wskazaną lokalizacją
# os.remove(path) # usuwa plik w podanej lokalizacji
# os.rename(src, dst) # przenosi plik/katalog z lokalizacji src do dst
# os.system(cmd) # wykonuje polecenie tak, jakby było wpisane w shellu


# Warto zwrócić uwagę na pakiet wewnątrz os - os.path. Jest to pakiet służący do zarządzania 
# ścieżkami plików/katalogów.
# Dlaczego specjalny pakiet jest potrzebny?

# W zależności od systemu operacyjnego ścieżki są konstruowane w inny sposób, 
# Przykładowo głównym katalogiem w systemie windows może być:
# c:\\

# w systemach Unix:
# /

# Zwróć uwagę na różnicę w separatorze w ścieżce, przykładowa ścieżka w systemie linux:
# /usr/bin

# w systemie windows:
# c:\\users\admin


# Dzięki użyciu biblioteki Twój program będzie działać niezależnie od systemu operacyjnego

# os.path.join(base_path, file) # łączy podane ścieżki
# os.path.exists(path) #zwraca True, gdy plik/katalog pod podaną ścieżką istnieje
# os.path.isdir(path) #zwraca informację, czy dana ścieżka jest katalogiem
# os.path.basename(path) # Zwraca katalog nadrzędny
# os.path.abspath(path) # zmienia relatywną ścieżkę na absolutną


# Transformacja obiektu w ciąg znaków i ciągu znaków w obiekt

# Wiodącym formatem zapisu danych w formacie podobnym do słownika/listy jest JSON. 
# Python posiada wbudowany pakiet do obsługi tego formatu

# import json
# json.loads(data_in_str) # zwraca obiekt z ciagu znaków
# json.dumps(dict_data) # zwraca tekstową reprezentacje pliku

# Uwaga: wartość przekazana do zmiany w ciąg znaków może zawierać tylko: słowniki, listy, ciągi znaków, 
# liczby stało i zmiennoprzecinkowe, i boolean.
# Format json nie posiada wsparcia dla wartości None oraz zbiorów.

# Pickle to format zapisu pythona, który posiada wsparcie dla zbiorów i tupli:

# import pickle
# pickle.loads(data_in_str) # zwraca obiekt z ciagu znaków
# pickle.dumps(dict_data) # zwraca tekstową reprezentacje pliku


# Pliki csv:

# Pliki csv nie są czytane w całości, python udostępnia przydatne klasy umożliwiające czytanie i pisanie 
# do tego typu plików.

# Czytanie pliku csv jest możliwe przy pomocy klasy reader:

import csv

with open(csv_file_path, newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        print(" ".join(line))


natomiast pisanie do pliku csv - przy pomocy klasy writer:

with open(csv_file_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([1, 2, 3, 4])


# Praca z liczbami

# Wbudowany moduł math pozwala na użycie zdefiniowanych funkcji do pracy na typach liczbowych:

# import math

# math.floor(liczba) #zaokrągla liczbę w dół
# math.ceil(liczba) #zaokrągla liczbę w górę
# math.fabs(liczba) #zwraca wartość absolutną (z pominięciem +/- na początku)
# math.log(liczba, base=2.71) # zwraca logarytm danej liczby. Jeśli parametr base nie jest podany, zwraca logarytm naturalny
# math.sin(liczba) # zwraca sinus liczby (w radianach)﻿
# math.cos(liczba) # zwraca cosinus liczby (w radianach)
# math.fsum([1, 2 ,3]) # zwraca sumę wszystkich elementów


# Liczby losowe


# Pakiet random umożliwia wprowadzenie losowości do wykonywanego programu:

# import random

# random.random() # zwraca liczbę z zakresu (0-1)

# start, stop = 0, 10
# random.randrange(start, stop, step=1) # zwraca jeden z elementów wygenerowanych przez range(start, stop, step)
# random.choice(["a", "b", "c"]) # zwraca losowy element z przekazanej sekwencji 

# lst = ["a", "b", "c"]
# random.shuffle(lst) # miesza kolejność w sekwencji
# random.sample(lst, k=2) # zwraca próbkę rozmiaru k z podanej sekwencji


# Inne warte sprawdzenia pakiety:


# webbrowser - pozwala na otwieranie kart i okien przeglądarki
# datetime - pozwala na pracę z datą i czasem
# re - pozwala na wyszukiwanie i podmienianie tekstu za pomocą wyrażeń regularnych
