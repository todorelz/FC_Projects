# Relacyjne bazy danych, Podstawowa struktura

# Relacyjne bazy danych w podstawowej wersji składają się z Tabel. Przykładowa Tabela zawierająca dane użytkowników:



# W odróżnieniu od tabel znanych z arkuszy kalkulacyjnych każda kolumna w Tabeli (w przypadku powyżej ID, Imię, Typ, Aktywny) ma przypisany typ i zakres wartości.
# Załóżmy następujące typy dla przykładowej tabeli Użytkownicy:



# Przy obecnym założeniu nie ma możliwości wpisania w kolumnie ID wartości "Student".

# Wpisy w tabeli znajdujemy poprzez zapytania. W każdym zapytaniu definiujemy, jakich wartości szukamy w danych kolumnach oraz jakich kolumn oczekujemy w odpowiedzi.
# Przykładowe pseudo zapytanie:
# Zwróć mi wszystkie wpisy, gdzie Typ = Student i Aktywny=1, potrzebuję kolumn ID i Imię.

# Przykładowe poprawne odpowiedzi na to zapytanie:



# Oraz:



# Jeśli w zapytaniu nie określimy kolumny, według której chcemy posortować dane, wartości, które otrzymamy mogą mieć dowolną kolejność.

# Na czym polega relacyjność bazy danych i do czego będzie przydatna?

# Do tej pory działaliśmy na tylko jednej tabeli w bazie danych. Zauważ, że nasza kolumna Typ otrzymywała tylko dwie wartości: Student lub Mentor. Załóżmy, że dla użytkownika o Id 7 wprowadziliśmy błędną wartość pola Typ (zauważ różnicę w pierwszej literze):



# Dla naszego wcześniejszego zapytania tabela nie zwróci nam rekordu (wiersza) dla użytkownika ID:7, Imię: Arnold. Ten problem możemy rozwiązać poprzez zdefiniowanie wszystkich dostępnych typów jako zamkniętej listy dozwolonych wartości dla kolumny:
# Typ {Mentor, Student}.
# To podejście się sprawdzi, jeśli nasz system nie zakłada dynamicznego definiowania typów użytkowników (co, jeśli z poziomu aplikacji chcemy zdefiniować nowy typ użytkownika Administrator?)

# Do tego celu zdefiniujmy drugą tabelę TypyUżytkowników



# Zmodyfikujmy naszą oryginalną tabelę tak, by korzystała z tabeli Typy Użytkowników:



# Klucz obcy oznacza, że wartość tej kolumny może przyjąć tylko i wyłącznie wartości z pola, do którego nawiązuje.
# Taką zależność między wartościami pól w różnych tabelach nazywamy relacjami.

# Powyższa relacja jest relacją typu jeden do wielu. Jeden TypUżytkownika ma wielu Użytkowników.
# Klucz obcy może nawiązywać tylko do jednego wiersza w tabeli, do której nawiązuje.

# Relacja wiele do wielu:

# Rozszerzmy naszą bazę o przypisanie kursów do użytkowników, Użytkownik może mieć wiele kursów, kurs może być przypisany do wielu użytkowników.

# Zacznijmy od tabeli definiującej dostępne kursy:



# Czy możemy dodać informacje o użytkownikach w kursie w tabeli kursy?
# Wymagałoby to wpisania w jednej kolumnie Użytkownicy wielu kluczy obcych. To samo dotyczy zawarcia informacji o przypisanych kursach w tabeli Użytkownicy.

# Stwórzmy zatem tabelę pomocniczą - Kursy użytkowników:



# Zauważ, że zarówno klucz obcy dla użytkowników jak i kursów może się powtarzać.

# SQLAlchemy relacyjna baza danych SQL i mapowanie Tabela <-> Klasa

# Na potrzeby kursu użyjemy jednoplikowej bazy danych SQLite. Jest to baza danych nie wymagająca serwera, w środowiskach produkcyjnych najczęściej używamy serwerów baz danych PostgreSQL lub MySQL.

# Zainstaluj sqlalchemy dla flask:

# pip install Flask-SQLAlchemy

# Aby użyć sqlalchemy w naszym projekcie flask dodaj następujący kod w twoim głównym pliku aplikacji:

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #test db to nazwa pliku w którym utworzymy bazę danych
# db = SQLAlchemy(app)

# Za pomocą sqlalchemy możemy zdefiniować tabele w bazie danych jako klasy:

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     firstname = db.Column(db.String(120), unique=False, nullable=False)
#     lastname = db.Column(db.String(120), unique=False, nullable=False, server_default="", default="")

# Aby utworzyć naszą bazę danych wykonaj:

# db.create_all()

# primary_key - to kolumna, która jest uzupełniana automatycznie i ma unikalną wartość w tabeli.
# default i server_default to domyślne wartości dla kolumny: default - w kodzie python, server_default - według silnika bazy danych.

# Aby dodać wiersz (rekord) w bazie danych, utwórz obiekt klasy:

# me = User(
#   username="robergo", 
#   email="robert.gorzynski@not-real.com", 
#   firstname="Robert"
# )

# Taki obiekt jest zadeklarowany w pamięci, ale jeszcze nie jest zapisany w bazie danych.

# Dodaj go do bieżącej sesji, następnie wyślij zmiany:

# db.session.add(me)
# db.session.commit()

# Aby wydobyć już istniejący wpis z bazy danych, znajdziemy go poprzez metodę query w db.session:

# db.session.query(User).all() #zwróci listę obiektów reprezentujących wszystkie wiersze w tabeli User
# db.session.query(User).filter(User.username=="robergo").all() #zwróci listę obiektów reprezentujących wszystkie wiersze w tabeli User, gdzie username == "robergo"
# db.session.query(User).filter(User.username=="robergo").first() #zwróci obiekt reprezentujący pierwszy wiersz User, gdzie username == "robergo"

# Aby pobrać i zmodyfikować już istniejący wpis w tabeli należy go podobnie dodać do sesji i wykonać commit:

# me = db.session.query(User).filter(User.username=="robergo").first()
# me.lastname = "Coś"

# db.session.add(me)
# db.session.commit()

# Aby usunąć wybrane wiersze, musimy je znaleźć poprzez metodę query, następnie na rezultacie wykonać metodę delete():

# db.session.query(User).filter(User.username=="robergo").delete()

# Zmiana nie zostanie wysłana do bazy danych, dopóki nie wykonamy polecenia:

# db.session.commit()


# Problem z aktualizacją bazy danych i propagowaniem zmian w bazie danych:

# Dodajmy dodatkową kolumnę w klasie User - user_type:

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     firstname = db.Column(db.String(120), unique=False, nullable=False)
#     lastname = db.Column(db.String(120), unique=False, nullable=False, server_default="", default="")
#     user_type = db.Column(db.String(120), unique=False, nullable=False, server_default="", default="student")

# Wykonaj ponownie db.create_all(), a następnie wykonaj polecenie:

# db.session.query(User).first()

# Zauważ, ze wystąpił błąd - nieznana kolumna user_type.- to dlatego, że sqlalchemy jedynie sprawdza istnienie tabel, nie aktualizuje jej pól automatycznie. Aby dodać takie pole, należałoby usunąć tabelę (!) lub całą bazę danych (!) i wygenerować ją na nowo. Zastanów się, z jakimi konsekwencjami wiązałoby się to na środowisku produkcyjnym.

# Istnieje narzędzie do automatycznego zarządzania zmianami struktury bazy danych. Zakomentuj linię deklarującą pole user_type w klasie User, a następnie w terminalu wykonaj:

# pip install Flask-Alembic

# na początku głównego pliku flask dodaj:

# from flask_alembic import Alembic

# Dodaj na końcu głównego pliku flask:

# alembic = Alembic()
# alembic.init_app(app)

# Od teraz flask udostępnia dodatkowe polecenia terminala do tworzenia rewizji /migracji.

# Wykonaj polecenie:

# flask db revision initial

# W katalogu głównym aplikacji flask pojawił się katalog migrations. Znajdź plik kończący się na _initial.py. Część nazwy przed _initial to identyfikator migracji. Sprawdź zawartość tego pliku - zauważ, że jest to kod python z dwoma metodami - upgrade i downgrade.

# Migracje stosujemy do bazy danych poprzez polecenie:

# flask db upgrade

# Odkomentuj teraz linię z kolumną user_type i wykonaj:

# flask db revision add_user_type
# flask db upgrade

# Zauważ zmianę w katalogu migrations.
# Jeśli z jakiegoś powodu potrzebujesz wycofać zmianę w bazie danych, wykonaj:

# flask db downgrade {{identyfikator migracji}}

# Zauważ, jak łatwo dzięki temu możesz dodać informacje o zmianach w bazie danych do swojego repozytorium.

# Dla własnych migracji wystarczy wykonać:

# flask db revision empty {{nazwa migracji}}