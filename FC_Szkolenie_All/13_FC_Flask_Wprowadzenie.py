# Framework Flask:

# Jest to podstawowy i lekki framework to tworzenia Stron i aplikacji webowych. Pełna dokumentacja jest dostępna pod adresem:
# https://flask.palletsprojects.com/en/1.1.x/

# Instalacja:
# Utwórz osobne wirtualne środowisko poprzez pakiet venv (aktywuj je), następnie zainstaluj flask poprzez:

# pip install Flask

# Najprostsza aplikacja Flask to jednoplikowy serwer.

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# Aby uruchomić ten serwer wykonaj w terminalu:

# FLASK_APP=nazwapliku.py
# flask run
# Nie zatrzymuj tego programu - dopóki działa, możesz wejść na Twoją stronę:

# Wejdź teraz na stronę:

# http://127.0.0.1:5000

# Jak widzisz, właśnie uruchomiliśmy wersję Hello World w przeglądarce. Jak to właściwie działa?
# Dekorator

# @app.route('/')
# podpina wskazaną funkcję jako funkcję, która będzie uruchomiona, gdy użytkownik wejdzie na stronę główną.

# Co, gdybyśmy chcieli zadeklarować obsługę innego adresu?

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/hello/')
# def hello_world():
#     return 'Hello'

# Wejdź na stronę:

# http://127.0.0.1:5000/hello/
# Zauważ, że do obsługi tego żądania została użyta inna funkcja, niż na stronie głównej.

# Co, jeśli chcemy przekazać parametry poprzez adres? Używamy specjalnej składni w app route:

# @app.route('/hello/<name>/')
# def hello_world(name):
#     return 'Hello {}'.format(name)

# Co ważne, nazwa parametru w funkcji, jak i parametr w ścieżce app route muszą mieć taką samą nazwę.

# Szablony Flask:

# Jak do tej pory zawartość zwracanej odpowiedzi była bezpośrednio przekazana jako ciąg znaków przez instrukcję return. Z uwagi na duży rozmiar treści HTML nie jest to rozwiązanie praktyczne. Flask wykorzystuje system szablonów jinja do renderowania kodu HTML.

# https://jinja.palletsprojects.com/en/2.11.x/templates/

# Utwórz podkatalog templates, a w nim plik "main.html", do którego wstawisz szkielet strony html.
# Aby zwrócić ten plik, zaimportuj z pakietu flask:

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/hello/<name>')
# def hello(name):
#     return render_template("main.html")

# To wykonanie nie różni się niczym od wczytania zawartości pliku i zwrócenia go w nie zmienionej wersji. Funkcja render_template przyjmuje również nazwane parametry, które będą przekazane do pliku szablonu:

# Wewnątrz tagu body wstaw:

# Hello {{name}}

# Zmień funkcję hello na:

# @app.route('/hello/<name>/')
# def hello(name):
#     return render_template("main.html", name=name)

# Każde wystąpienie {{name}} będzie zmienione na zawartość parametru name metody render_template

# Jinja pozwala również na warunkowe wykonanie kodu. Zmieńmy zawartość bloku body na:

# {% if name %}Hello {{ name }} {% else %}Hello Stranger{% endif %} 

# oraz plik python:

# @app.route('/')
# def hello_world():
#     return render_template("main.html")

# Zauważ, że składnia jinja nie rozpoznaje wcięć jako identyfikatorów bloku, blok IF kończy się, gdy jinja napotka instrukcję {% endif %}.

# Jinja pozwala również na operacje na listach, pętlach:

# {% for item in seq %}
#     <li>{{ item }}</li>
# {% endfor %}


# Przekierowania:

# Aby uzyskać adres utworzony przez app.route, użyj funkcji url_for, parametrem jest nazwa funkcji dowiązanej do ścieżki:

# from flask import url_for
# url_for("hello_world")

# Możesz użyć tej funkcji, by utworzyć przekierowanie zamiast drukowania treści:

# from flask import url_for, redirect

# def hello_world():
#   return redirect(url_for("hello", name="stranger"))


# Dostęp do danych wysłanych z formularza:

# Dane wysłane z formularza są dostępne poprzez obiekt request z pakietu flask. Jeśli metodą wysłania był POST a nazwą pola "firstname", wartość pola będzie zapisana w:

# from flask import request
# requets.form["firstname"]

# jeśli parametry zostały wysłane metodą get:

# from flask import request
# requets.args["firstname"]
