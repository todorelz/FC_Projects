import sys
import csv
import os

def read_csv(file_name):
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
            print(f'błędny format zmiany: {change}')

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
    main(
        "data/in.csv",
        "data/out.csv",
        ["2,0,gitara","9,1,kubek","1,2,17", "3,3,0"]
    )




