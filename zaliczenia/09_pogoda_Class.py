# Zoptymalizuj kod z poprzedniego zadania z pogodą.

# Utwórz klasę WeatherForecast, która będzie służyła do odczytywania i zapisywania pliku, a także odpytywania API.

# Obiekt klasy WeatherForecast dodatkowo musi poprawnie implementować cztery metody:

#  __setitem__
#  __getitem__
#  __iter__
#  items

# Wykorzystaj w kodzie poniższe zapytania:

# weather_forecast[date] da odpowiedź na temat pogody dla podanej daty
# weather_forecast.items() zwróci generator tupli w formacie (data, pogoda) dla już zapisanych rezultatów przy wywołaniu
# weather_forecast to iterator zwracający wszystkie daty, dla których znana jest pogoda

import json
import os
import requests
from datetime import datetime

class WeatherForecast:
    def __init__(self, cache_file="weather_cache.json",latitude=52.23, longitude=21.01):
        self.cache_file = cache_file
        self.latitude = latitude
        self.longitude = longitude
        self.cache = self._load_cache()

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "r", encoding = "utf-8") as f:
                return json.load(f)
        return {}
    
    def _save_cache(self):
        with open(self.cache_file, "w", encoding = "utf-8") as f:
            json.dump(dict(sorted(self.cache.items())), f, indent=2)

    def _fetch_weather(self, date):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            f"&daily=rain_sum"
            f"&timezone=Europe%2FLondon"
            f"&start_date={date}"
            f"&end_date={date}"
        )
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data["daily"]["rain_sum"][0]
        except Exception:
            return None
        
    def _interpreter(self, value):
        if value is None or value<0:
            return "Nie wiem"
        elif value == 0.0:
            return "Nie będzie padać"
        else:
            return "Będzie padać"
        
    def __getitem__(self, date):
        if date in self.cache:
            return self.cache[date]
        
        rain_value = self._fetch_weather(date)
        result = self._interpreter(rain_value)

        self.cache[date] = result
        self._save_cache()

        return result
    
    def __setitem__(self, date, value):
        self.cache[date] = value
        self._save_cache()

    def __iter__(self):
        return iter(self.cache.keys())        

    def items(self):
        for item in self.cache.items():
            yield item

wf = WeatherForecast()

print(wf["2026-03-30"])