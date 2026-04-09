# Napisz program oparty na klasach i dziedziczeniu, który odczyta wejściowy plik, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

# Uruchomienie programu przez terminal:
# python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

#  <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv, in.json lub in.txt
#  <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv, out.json, out.txt lub out.pickle
#  <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na podane miejsce.

# Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.json”.

# Przykład działania:
# python reader.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# Z pliku in.json ma wyjść plik out.csv:
# gitara,3,7,0
# kanapka,12,5,kubek
# pedzel,17,34,5
# plakat,czerwony,8,0
# Wymagane formaty:

# .csv
# .json
# .txt
# .pickle

import sys
import os
import csv
import json
import pickle

class FileHandler:
    def read(self, file_name):
        raise NotImplementedError
    
    def save(self, file_name, data):
        raise NotImplementedError
        
class CSVHandler(FileHandler):
    def read(self, file_name):
        with open(file_name, encoding="utf-8") as f:
            return [row for row in csv.reader(f)]
        
    def save(self, file_name, data):
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)

class JSONHandler(FileHandler):
    def read(self, file_name):
        with open(file_name, encoding="utf-8") as f:
            return json.load(f)
        
    def save(self, file_name, data):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indend=2)

class TXTHandler(FileHandler):
    def read(self, file_name):
        with open(file_name, encoding="utf-8") as f:
            return [line.strip().split(",") for line in f]
        
    def save(self, file_name, data):
        with open(file_name, "w", encoding="utf-8") as f:
            for row in data:
                f.write(",".join(map(str,row)) + "\n")

class PickleHandler(FileHandler):
    def read(self, file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
        
    def save(self, file_name, data):
        with open(file_name,"wb") as f:
            pickle.dump(data, f)

def get_handler(file_name):
    ext = file_name.split(".")[-1].lower()

    if ext == "csv":
        return CSVHandler()
    elif ext == "json":
        return JSONHandler()
    elif ext == "txt":
        return TXTHandler()
    elif ext == "pickle":
        return PickleHandler()
    else:
        print(f'Nieobsługiwany format: {ext}')
        sys.exit(1)

def apply_changes(data,changes):
    for change in changes:
        try:
            x, y, value = change.split(",",2)
            x, y = int(x), int(y)
            if 0 <= y <len(data) and 0 <= x < len(data[y]):
                data[y][x] = value
            else:
                print(f'Zmiana poza zakresem: {change}')
        except ValueError:
            print(f"Błędny format (oczekiwano x,y,wartosc): {change}")

    return data

def print_data(data):
    for row in data:
        print(",".join(map(str, row)))

def main(input_file, output_file, changes):

    if not os.path.exists(input_file):
        print(f'Plik {input_file} nie istnieje')
        sys.exit(1)

    reader, writer = get_handler(input_file), get_handler(output_file)

    data = reader.read(input_file)
    data = apply_changes(data, changes)

    print("\nZmodyfikowano dane:")
    print_data(data)

    writer.save(output_file, data)
    print(f'Zapisano dane do pliku: {output_file}')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Użycie: python reader.py <in> <out> <zmiany...>")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]
    changes = sys.argv[3:]

    main(input_file,output_file,changes)

