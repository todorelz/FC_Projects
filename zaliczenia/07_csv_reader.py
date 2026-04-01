# Program do zarządzania plikami csv.
# Oczekuje na weryfikację
# Flag Outlined
# 6
# Arrow down
# Napisz program, który odczyta wejściowy plik CSV, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

# Uruchomienie programu przez terminal:
# python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

#  <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv
#  <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv
# <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na podane miejsce.

# Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.csv".

# Przykład działania:
# python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# Z pliku in.csv:
# drzwi,3,7,0
# kanapka,12,5,1
# pedzel,22,34,5
# plakat,czerwony,8,kij
# Ma wyjść plik out.csv:
# gitara,3,7,0
# kanapka,12,5,kubek
# pedzel,17,34,5
# plakat,czerwony,8,0

import sys
import csv
import os

def read_csv(file_name):
    if not os.path.exists(file_name):
        print(f"Plik nie istnieje: {file_name}")
        sys.exit(1)    
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f)
        return  [row for row in reader]

    
def apply_changes(data, changes):
    for change in changes:
        try:
            x, y, value = change.split(",",2)
            x = int(x)
            y = int(y)

            if 0 <= y < len(data) and 0 <= x < len(data[y]):
                data[y][x] = value
            else:
                print(f'Zmiana poza zakresem: {change}')
        except ValueError:
            print(f"Błędny format zmiany (oczekiwano x,y,wartosc): {change}")
            
    return data

def print_data(data):
    for row in data:
        print(",".join(row))

def save_csv(file_name, data):
    with open(file_name, mode = "w", newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def main(input_file, output_file, changes):

    data = read_csv(input_file)
    data = apply_changes(data, changes)

    print("\n Zmodyfikowano dane")
    print_data(data)

    save_csv(output_file, data)
    print(f"\n Zapisano do pliku: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Użycie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiany...>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    main(input_file, output_file, changes)




