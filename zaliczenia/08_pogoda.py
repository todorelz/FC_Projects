# Zadanie - obsługa biblioteki zewnętrznej

# Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:

# Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03. 
# W przypadku nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
# Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
# Istnieją trzy możliwe informacje dla opadów deszczu:
# Będzie padać (dla wyniku większego niż 0.0)
# Nie będzie padać (dla wyniku równego 0.0)
# Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
# Będzie padać
# Nie będzie padać
# Nie wiem
# Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania do API, 
# tylko zwróć wynik z pliku.

# URL do API:
# https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}

# W URL należy uzupełnić parametry: latitude, longitude oraz searched_date


import json
from datetime import datetime, timedelta
import os
import requests

Cache_file = "weather_cache.json"
LATITUDE = 52.23
LONGITUDE = 21.01

def load_cache():
    if os.path.exists(Cache_file):
        with open(Cache_file, "r", encoding = "utf-8") as f:
            return json.load(f)
    return{}
    
def get_date_from_user():
    while True:
        user_input = input("Podaj datę (YYYY-MM-DD) lub Enter dla jutra: ")
        today = datetime.today().date()

        if not user_input:
            return (today + timedelta(days=1)).strftime("%Y-%m-%d")
        
        try:
            date_obj = datetime.strptime(user_input, "%Y-%m-%d").date()
            
            if date_obj < today:
                print("Data nie może być z przeszłości")
                continue
            if date_obj > today + timedelta(days = 14):
                print("Data może być maksymalnie 14 dni do przodu")
                continue
            return user_input
        
        except ValueError:
            print("Niepoprawny format daty")
        
def fetch_weather(date):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        f"&daily=rain_sum"
        f"&timezone=Europe%2FLondon"
        f"&start_date={date}"
        f"&end_date={date}"
    )

    response = requests.get(url)
    data = response.json()

    try:
        rain_value = data["daily"]["rain_sum"][0]
        return rain_value
    except (KeyError, IndexError):
        return None

def interpret_rain(value):
    if value is None or value <0:
        return "Nie wiem"
    elif value == 0.0:
        return "Nie będzie padać"        
    else:
        return "Będzie padać"

def save_cache(cache):
    sorted_cache = dict(sorted(cache.items()))
    
    with open(Cache_file, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)


def main():
    cache = load_cache()
    date = get_date_from_user()

    if date in cache:
        print(f'{date}: {cache[date]}')
        return
    
    rain_value = fetch_weather(date)
    result = interpret_rain(rain_value)

    print(f'{date}: {result}')

    cache[date] = result
    save_cache(cache)

if __name__ == "__main__":
    main()
