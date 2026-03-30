        # Skrótowy zapis warunkowego przypisania wartości

# Załóżmy następujący kod, który wytypuje na podstawie (polskiego) imienia klienta potencjalną płeć :

firstname = "Adam"
if firstname[-1] == "a":
    gender = "f"
else:
    gender = "m"

# Mamy tu do czynienia z krótką deklaracją, którą python pozwala zapisać za pomocą skróconej składni:

#   {wartość jeśli warunek} if {warunek} else {wartość jeśli nie warunek}

firstname = "Adam"
gender = "f" if firstname[-1] == "a" else "m"


# Zwróć uwagę na brak dwukropków przy tym zapisie. Nie używamy dwukropków, ponieważ nie otwieramy żadnych dodatkowych bloków kodu.


    # Skrótowy zapis pętli for tworzącej listy, słowniki, zbiory

# Załóżmy przykładowy kod tworzący listę lst_b na podstawie listy lst_a:

lst_a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
lst_b = []
for firstname in lst_a:
    lst_b.append(firstname.capitalize())

# Kod wykonujący dosyć prostą operację zajmuje aż 3 linie. Python udostępnia uproszczoną składnię dla tego typu działań:

    # [ <<nowy_element>> for <<element>> in <<lista>> ]
# <<nowy element>> zazwyczaj jest wyrażeniem które jest otrzymywane ze zmiennej <<element>>

# W naszym przypadku:
# lst_a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
# lst_b = [firstname.capitalize() for firstname in lst_a]

# Powyższy zapis pozwala znacząco skrócić deklaracje takiej zmiennej. Należy go czytać jako:
# Utwórz nową listę lst_b poprzez kapitalizację (zmiany pierwszej litery na wielką) elementów listy lst_a.

# Powyższy zapis pozwala również na filtrowanie elementów starej listy. Rozważmy następujący kod:

lst_a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
lst_b = []
for firstname in lst_a:
    if firstname != firstname.capitalize():
        lst_b.append(firstname.capitalize())

# Powyższy zapis zwróci tylko te imiona, które oryginalnie zaczynały się od małej litery.

# Skrócony zapis będzie wyglądał następująco:
lst_a = ["adam", "Ewa", "wojtek", "Robert", "marcin", "michał"]
lst_b = [firstname.capitalize() for firstname in lst_a if firstname != firstname.capitalize()]

# Skrótowe formy pozwalają również na tworzenie zbiorów i słowników w podobny sposób (zwróć uwagę na ograniczniki):

set_a = {firstname.capitalize() for firstname in lst_a if firstname != firstname.capitalize()}

#   Przy tworzeniu słownika musimy podać zarówno klucz, jak i jego wartość. Utwórzmy słownik, który będzie zawierał jako klucz oryginalną wartość z listy lst_a, 
# jako wartość imię po zastosowaniu metody capitalize:

dict_a = {firstname: firstname.capitalize() for firstname in lst_a}

# Zwróć uwagę na znak dwukropka w deklaracji, jest on identyczny jak w przypadku deklaracji słownika "wprost", czyli poprzez ręczne wpisywanie wartości.

#           Manager pakietów PIP

# Na potrzeby tego ćwiczenia utwórz projekt przez Pycharm wybierając środowisko wirtualne poprzez "venv".
# Python posiada wbudowany manager pakietów o nazwie pip.
# Aby zobaczyć obecnie zainstalowane pakiety wykonaj w konsoli polecenie:

# pip freeze
# #lub 
# python -m pip

# Obecnie zainstalowane pakiety są zapisane w formacie nazwa pakietu== wersja pakietu
# Aby zainstalować pakiet należy wykonać polecenie:

# pip install <<nazwa pakietu>>

# Pakiety możemy wyszukiwać również poprzez polecenie pip search:

# pip search <<słowo kluczowe">>

# Aby usunąć pakiet wykonujemy polecenie:

# pip uninstall <<nazwa pakietu>>

# Możemy również zdefiniować plik, który będzie zawierał listę wszystkich potrzebnych pakietów. Zwyczajowo nazywany jest "requirements.txt"

# plik requirements.txt

# requests
# pytest

# Aby zainstalować potrzebne pakiety za pomocą polecenia pip wykonaj:

# pip install -r requirements.txt

# Co ciekawe, możesz wskazać w pliku dokładną wersję pakietu w pliku requirements.txt poprzez podanie wersji po nazwie pakietu i znaku ==

# requests==2.25.0

# Porównaj tę linię z wydrukiem polecenia pip freeze - format zapisu jest ten sam. Zatem poprzez wykonanie polecenia:

# pip freeze > requirements.txt
# możesz automatycznie stworzyć listę zależności Twojego programu


#   Środowisko wirtualne

# Wykonaj w dwóch oddzielnych projektach w PyCharm polecenie "pip freeze" (powinny być takie same). W pierwszym zainstaluj pakiet "pyquery".
# Teraz wykonaj polecenie pip freeze w pierwszym i w drugim projekcie.
# Wyjścia powinny się różnić o świeżo dodaną bibliotekę

# Środowisko wirtualne to kontener zainstalowanych pakietów i bibliotek dostępnych tylko wewnątrz danego projektu.

# Ręcznie tworzymy nowe środowisko wirtualne poprzez wykonanie polecenia:

# python -m venv <<katalog środowiska>>
# #lub
# python3 -m venv <<katalog środowiska>> # w ten sposób wymuszamy główną wersję python dla własnego środowiska

# Zwyczajowo katalog główny środowiska nazywamy "env"

# python -m venv env

# Środowisko zostało utworzone, ale jeszcze nie jest aktywne. Aby je aktywować, wykonujemy polecenie:

# <<katalog środowiska>>/bin/activate
# w naszym przypadku na Windows

# env/bin/activate
# Linux / Mac os

# source env/bin/activate

# Zauważ, że prompt (wiadomość na początku twojego wiersza poleceń) zawiera teraz nazwę środowiska wirtualnego w nawiasach.
# Aby wyjść ze środowiska wirtualnego wykonaj polecenie:

# deactivate

# Polecenia pip wewnątrz środowiska wirtualnego będą teraz instalować wszystkie pakiety tylko dla tego środowiska wirtualnego.

# Uwaga: katalog wirtualnego środowiska nie powinien być nigdy dodawany do waszego repozytorium - zawiera on zdefiniowane pakiety dla waszej konkretnej wersji systemu operacyjnego.
#  Zamiast tego w repozytorium powinien być plik pozwalający na odtworzenie środowiska np. requirements.txt
