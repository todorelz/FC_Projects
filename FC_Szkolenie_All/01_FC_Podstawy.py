# Pycharm Podstawy
#
#
# Pycharm jest dedykowanym edytorem dla pythona. Co ważne, pliki *.py mogą być otwarte przez dowolny edytor plików tekstowych.
# W odróżnieniu od np, Notepad++, Pycharm posiada kontekstowe autouzupełnianie.

# Rozpoczęcie Pracy: Utwórz nowy projekt:
# Ważne: Bazowy interpreter musi być w wersji python3.6 lub wyższej (preferowana wersja to python 3.8). Uwaga: menu może
# znacząco różnić się między systemami operacyjnymi.
# Dla czystości lokalnego środowiska w większości przypadków "Inherit global site-packages" i "Make available to all projects"
# powinny być odznaczone. Opcja "Existing interpreter" może być również użyta, o ile python w wersji 3.6 lub wyższej jest dostępny.

# Jest to widok projektu, w którym masz dostęp do
#
#     Głównego katalogu środowiska wirtualnego :"venv".
#     Plików źródłowych projektu, w naszym przykładzie jest to "main.py"
#     Bibliotek zewnętrznych "External Libraries"
#     Otwartych i zdefiniowanych konsol "Scratches and consoles"
#
#
# Środowiska wirtualne i biblioteki zewnętrzne omówimy na przyszłych zajęciach.
#
# Aby zobaczyć wszystkie pliki i katalogi w projekcie, naciśnij dropdown z domyślną wartością "Project" i wybierz "Project Files".

# Zwróć uwagę na katalog ".idea". Jest to domyślny katalog, w którym przechowywana jest konfiguracja projektu PyCharm,
# co ważne, nie powinien być nigdy dodawany do repozytorium, jest silnie zależny od konfiguracji systemu operacyjnego.
#
# Wbudowana Konsola
#
# Pycharm posiada wbudowany wiersz poleceń / konsolę (może być używana zamiast uruchomionej osobno konsoli /
# wiersza poleceń dostępnego w systemie operacyjnym).
# Można zmienić ustawienia terminala w PyCharm, jest to przydatne jeśli użytkownik Windowsa chce korzystać z komend
# takich samych jak są na Linux, MacOs.
# Aby to zrobić należy wejść w file -> settings -> tools -> terminal -> application settings i zmienić shell path.


# "Python console" pozwala na interaktywne uruchamianie poleceń python. W momencie zatwierdzenia polecenia przez
# naciśnięcie <Enter>, polecenie będzie wykonane natychmiastowo
#
# Aby uruchomić konsolę, taką, jak w systemie operacyjnym, naciśnij przycisk Terminal. Po naciśnięciu przycisku "+"
# Pycharm uruchomi dodatkową konsolę (przydatne, gdy projekt wymaga wielu procesów uruchomionych w tym samym czasie).

# To jest nasze główne pole pracy. Zwróć uwagę na pionową linię w edytorze. Jest to wskazówka, jak maksymalnie długa powinna być linia kodu.
# Ustawienia domyślne PyCharm zakładają 120 znaków,
# Większość firm przyjmuje ograniczenie między 80-100 znaków, oficjalny standard Python zakłada 80 znaków
#
# Na potrzeby kursu zmień go na 80 znaków.
# Przejdź do File -> settings.
# Wybierz Editor -> code style i wpisz wartość 80 w pole "visual guides".


# Program Hello World
# Utwórz nowy plik o nazwie helloworld.py. Wpisz w niego następującą linię:

print("Hello World")
# Uruchom terminal, wpisz w nim następujące polecenie:
#
# python helloworld.py #<Enter>

# Terminal powinien wydrukować następującą linię:
# Hello World


# Właśnie uruchomiłeś/aś Twój pierwszy program. Python jest jednym z niewielu języków, w których "Hello World" wymaga tylko jednej linii.
#
# Co dokładnie zrobiliśmy? Wywołaliśmy funkcję print z jednym stałym parametrem, ciągiem znaków "Hello World".
#
# Wprowadźmy teraz zmienną zamiast naszej stałej, niech nasz plik użyje zmiennej.

message = "Hello"
print(message)

# UUruchom program, rezultatem powinna być jedna linia:
# Hello

# Właśnie utworzyłeś/aś pierwszą zmienną. Nazwa zmiennej znajduje się zawsze po lewej stronie znaku równości, po prawej
# stronie znajduje się jej wartość. Nazwa zmiennej może składać się z dużych i małych liter alfabetu łacińskiego, cyfr,
# oraz znaku "_". Nie może zawierać znaku spacji!
# Spróbujmy teraz zmodyfikować naszą zmienną zaraz po jej deklaracji:

message = "Hello"
print(message)
message = message + "World"
print(message)

# Oczekiwany wynik to ( zauważ brak spacji między "Hello" a "World":
#
# Hello
# HelloWorld

# Typy zmiennych:
#
# Zmienne mogą przyjmować wiele wartości. Jednymi z podstawowych są:

# Wartość całkowita "int", przykład:
counter = 2

# Wartość zmienno-przecinkowa:
weight_sum = 10.5

# Wartość logiczna (duża litera na początku):
always_true = True
never_true = False

# Ciąg znaków:
message = 'Hello World'
message = "Hello World"


# Możliwe jest również przełamanie pliku na wiele linii:
message = '''
Hello 
World'''
message = """
Hello 
World
"""

# Jest też dostępny specjalny typ zmiennej oznaczający brak jakiejkolwiek wartości:
nothing_here = None


# Co możemy robić ze zmiennymi:
# Typy liczbowe, takie jak int, float mają następujące dostępne operatory : + - * / ** %

a = 1.5
b = 0.5
print(a + b)
print(a * b)
print(a / b)
a = 2
b = 3
print(a ** b)
print(b % a)

# PPowyższy kod po wykonaniu powinien zwrócić następujący wynik:

2.0
0.75
3.0
8.0
1.0

# Operatorami zwracającymi Wartości Logiczne (True/False) są:

# {zmienna1} == {zmienna2}  # zwraca True gdy wartość zmienna1 jest równa zmienna2 w przeciwnym wypadku zwraca False
# {zmienna1} != {zmienna2}  # zwraca True gdy wartość zmienna1 jest różna od zmienna2 w przeciwnym wypadku zwraca False
# {zmienna1} < {zmienna2}}  # zwraca True gdy wartość zmienna1 jest mniejsza od zmienna2 w przeciwnym wypadku zwraca False
# {zmienna1} <= {zmienna2}}  # zwraca True gdy wartość zmienna1 jest mniejsza lub równa zmienna2 w przeciwnym wypadku zwraca False
# {zmienna1} > {zmienna2}}  # zwraca True gdy wartość zmienna1 jest większa od zmienna2 w przeciwnym wypadku zwraca False
# {zmienna2} >= {zmienna2}}  # zwraca True gdy wartość zmienna1 jest większa lub równa zmienna2 w przeciwnym wypadku zwraca False


# przykładowo wykonaj:

print(1 == 2)
a = 1
b = 2
print(a == 1)
print(a != b)

# Operatory działające tylko na zmiennych logicznych:

# {zmienna1} or {zmienna2}  # zwraca True jeśli jedna z wartości jest prawdziwa (== True) w przeciwnym wypadku zwraca False
# {zmienna1} and {zmienna2}  # zwraca True jeśli obie z wartości są prawdziwe (== True) w przeciwnym wypadku zwraca False
# not {zmienna}  # zwraca False jeśli zmienna ma wartość True, w przeciwnym wypadku zwraca True


# Jeśli stosujemy operatory logiczne na zmiennej o innej wartości, jest ona rzutowana na wartość logiczną.
# Wykonaj poniższy kod, by zobaczyć, jaki będzie wynik poniższej operacji:

print(bool(-1))
print(bool(1))
print(bool(2))
print(bool(0))
print(bool(0.0))
print(bool(0.1))
print(bool(""))
print(bool("coś"))
print(bool(" "))
print(bool(None))

# PPraca z typami zmiennych
# Aby sprawdzić typ danej zmiennej, użyj funkcji type({zmienna}), przykładowo:

a = "Ciąg znaków"
print(type(a))

# W przypadku sprawdzenia, czy dana zmienna jest danego typu stosujemy polecenie "is" bądź "is not"

a = "Ciąg znaków"
print(type(a) is str)
print(type(a) is not int)


# Możemy swobodnie zmieniać typ zmiennej poprzez funkcje bool, int, str, float:

print("1" + "2")
print(int("1") + int("2"))

print(bool(1))
print(str(12))


# Zmienna nie musi trzymać cały czas tego samego typu. Przykładowy kod jest poprawny (w niektórych przypadkach może p
# rowadzić do zmniejszenia czytelności):

message = "nowa wiadomość"
message = 2


# Operacje na tekście:

# Łańcuchy znaków możemy łączyć za pomocą operatora +, przykładowo:

print("Hello" + " " + "World")

# Możemy też powtórzyć wybrany tekst kilkukrotnie za pomocą operatora *

print("Hello " * 5)


# Czasami przyda nam się szablon wypowiedzi, do którego będziemy wstawiać nasze wartości. Możemy to osiągnąć przez użycie operatora %

print("Tekst do %s formatowania %i" % ("a", 2))


# %s oznacza ciąg znaków, %i liczbę całkowitą
#
# Jest to obecnie niezalecana metoda, rozwiązaniem proponowanym w python 3 jest obecnie metoda format:

print("Jest to {} linia programu".format(1))
print("Jest to {} linia programu w której występuje słowo '{}'".format(2, "słowo"))


# Jeśli potrzebujemy wykorzystać ten sam argument kilkukrotnie, możemy nazwać nasze parametry:

print("Jest to {line} linia programu w której drukujemy słowo '{word}'. Koniec linii {line}".format(line=1, word="Hello"))


# Plusem tej metody jest brak konieczności podawania typu zmiennej.
#
# Możemy użyć też skrótowego zapisu metody format

a = "world"
print(f"Hello {a}!")


# Pobieranie wejścia z linii komend:

# Jak do tej pory działaliśmy na danych zapisanych wewnątrz kodu. 
# Istnieje również możliwość pobrania danych od użytkownika programu, służy do tego instrukcja input.
#  Przykładowy kod:

print("Jak masz na imię?")
user_name = input()
print("Twoje Imię to {}".format(user_name))


# Przykładowy wynik:

# Jak masz na imię?
# Robert<Enter>
# Twoje Imię to Robert


# Wynik działania instrukcji input() zawsze będzie typu str. 
# Jeśli chcesz pobrać wartość liczbową, zmień typ na np int.

print("Ile masz lat?")
age = int(input())
print("Twój wiek to {}".format(age))
print("Za rok będziesz mieć {} lat".format(age+1))


# Dodatkowe formatowanie tekstu
# Niektórych znaków nie będziesz w stanie wpisać bezpośrednio z klawiatury. 
# Tego typu znaki musisz zastąpić odpowiadającemu im znakowi ucieczki:
# znak nowej linii zastąp przez \n

print("1\n2\n3\n4\n5")

# wynik działania:
# 1
# 2
# 3
# 4
# 5

# Co, jeśli chcemy wrócić do początku linii, ale nie przechodzić linię wyżej? Spróbuj wykonać:

print("1\r 2\r 3\r 4\r 50\r 6")

# Otrzymamy wynik:
# 60

# Jeśli chcesz użyć znaku takiego, jak:
# \ ' "
# Musisz poprzedzić go znakiem ucieczki "\"
# przykładowo:
print(" Używam \"cudzysłowu\" wewnątrz ciagu znaków")