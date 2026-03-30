# Podstawowe interfejsy
# Generatory:

# Rozważmy następujący problem - nasz program przetwarza dużą tablicę danych wczytaną z pliku. 
# W pliku występują linie komentarza, zaczynające się od znaku "#" - linie z komentarzem powinny być pominięte. Napiszmy funkcję wczytującą dane:

# def read_data(sciezka):
#     with open(sciezka) as fp:
#         return [line.strip() for line in fp if line and line[0] != "#"]

# for index, line in enumerate(read_data("dane.txt")):
#     print("{}) {}".format(index+1, line))

# Zauważ, że ta funkcja wymagania wczytania całości zawartości pliku do pamięci. Co, jeśli plik ma duży rozmiar > 1GB? 
# W takim wypadku nasz program będzie zużywał bardzo dużo zasobów.
# Napisanie funkcji czytającej tylko jedną linię będzie wymagało użycia zmiennych globalnych lub stworzenia klasy:

fp = open("data/dane.txt")
def read_line(fp):
    while True:
        line = fp.readline()
        if line == "":
            return None
        if line and line[0] == "#":
            continue
        return line

# W pythonie jest możliwe użycie generatorów - funkcji, które zwrócą rezultat więcej niż raz. 
# Do zwracania wartości w generatorze służy słowo kluczowe "yield". Przykładowo:

def generator_1():
    yield 1
# # zwróci jedną wartość: int(1)

def generator_2():
    yield 1
    yield 2
    yield 3
# zwróci trzy wartości: 1, 2, 3

# Wartości z generatora odbieramy za pomocą pętli for:

def generator_2():
    yield 1
    yield 2
    yield 3

for num in generator_2():
    print(num)

# Co ważne, kod wewnątrz generatora jest zatrzymywany przy każdym wystąpieniu słowa kluczowego "yield" i wznawiany, gdy pobieramy następną wartość. 
# Spróbuj wykonać następujący program:

def generator_2():
    print("linia 1")
    yield 1
    print("linia 2")
    yield 2
    print("linia 3")
    yield 3
    print("koniec")

for num in generator_2():
    print(num)

# Wyjście programu:

# linia 1
# 1
# linia 2
# 2
# linia 3
# 3
# koniec

# Zauważ, że "linia 2" została wydrukowana dopiero po pobraniu elementu. Wracając do naszego programu czytającego zawartość pliku:

# 🔹 Co to jest yield
# 👉 yield zamienia funkcję w generator
# Zamiast:
# wykonać się od początku do końca (jak return)
# funkcja:
# zatrzymuje się
# oddaje wartość
# i przy kolejnym wywołaniu wznawia działanie od tego miejsca

# 🔹 Różnica: yield vs return
# yield	                    return
# zatrzymuje funkcję	    kończy funkcję
# zapamiętuje stan	        nie zapamiętuje
# można użyć wiele razy	    tylko raz

# 👉 yield = „oddaj wartość i wróć później”
# 👉 return = „oddaj wartość i zakończ na zawsze”

print('---dane.txt---')

sciezka = "data/dane.txt"
def read_data(sciezka):
    with open(sciezka) as fp:
        for line in fp:
            if line and line[0] == "#":
                continue
            yield line.strip()

for index, line in enumerate(read_data(sciezka)):
    print("{}) {}".format(index+1, line))

# Co ważne, do poszczególnych elementów generatora nie możemy dostać się poprzez indeks w tablicy (w pamięci nie jest przechowywana tablica). Wykonanie:

# read_data(sciezka)[1] 
# zwróci błąd.
# Tak samo nie jest możliwe określenie długości generatora przez użycie:

# len(read_data(sciezka)) 
# zwróci błąd.

# Rzutowanie klas na znane typy prymitywne:

# Rozpatrzmy następującą klasę i jej użycie do wypisywania uczniów:
print('\n---Class---\n')

class Student:
    def __init__(self, firstname, lastname, year=1, group="A"):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.group = group

s1 = Student("Adam", "Abacki")
s2 = Student("Bartosz", "Babacki")
print("{} {}".format(s1.firstname, s1.lastname))
print("{} {}".format(s2.firstname, s2.lastname))

# Zwróć uwagę na dwie ostatnie linie - kod jest identyczny i format, w jakim wypisujemy uczniów, można przenieść do metody wewnątrz klasy Student:
class Student:
    def __init__(self, firstname, lastname, year=1, group="A"):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.group = group

    def name(self):
        return "{} {}".format(self.firstname, self.lastname)

s1 = Student("Adam", "Abacki")
s2 = Student("Bartosz", "Babacki")
print(s1.name())
print(s2.name())

# Możemy śmiało powiedzieć, że

# "{} {}".format(self.firstname, self.lastname)

# jest wynikiem, który w naszym przypadku definiuje rzutowanie klasy Student na typ str.
# W pythonie jest możliwe zdefiniowanie metody, która będzie domyślnie używana, gdy chcemy rzutować naszą klasę na ciąg znaków:

class Student:
    def __init__(self, firstname, lastname, year=1, group="A"):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.group = group

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

s1 = Student("Adam", "Abacki")
s2 = Student("Bartosz", "Babacki")
print(s1)
print(s2)

# Zauważ, że wywołanie metody __str__() wprost nie było wymagane. Wykonanie w pythonie:

# str(obj)
# jest równoznaczne z wykonaniem:

# obj.__str__()

# Ta sama składnia jest również dostępna dla innych typów podstawowych.
#  Użyj składni __{{nazwa typu}}__() do zadeklarowania odpowiedniej metody rzutującej:

class Student:
    def __init__(self, firstname, lastname, year=1, group="A"):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.group = group

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __int__(self):
        return self.year

    def __float__(self):
        return float(self.year)

    def __bool__(self):
        return self.year > 1


s1 = Student("Adam", "Abacki")
s2 = Student("Bartosz", "Babacki", 2)
print(int(s1))
if s2:
    print("{} nie jest już w pierwszej klasie".format(s2))


print('Dostęp do elementów za pomocą operatora []')
# Dostęp do elementów za pomocą operatora []

# Problem:
# Napiszmy klasę, która będzie pełnić rolę cache'a dla tablicy zapisanej w pliku tekstowym. 
# Gdy linia jest odczytywana z pliku, powinna być zapisana w pamięci. 
# W momencie, gdy drugi raz będziesz chciał odczytać daną linię, obiekt klasy powinien zwrócić linię zapisaną w pamięci, zamiast czytać ponownie zawartość pliku.

class FileCache:
    def __init__(self, filepath):
        self.fp = open(filepath)
        self.cache = {}

    def readchar(self, position):
        if position not in self.cache:
            self.fp.seek(position)
        self.cache[position] = self.fp.read(1)

# Zauważ, że funkcjonalnie metoda readchar działa podobnie jak odczytywanie elementów z listy. Przydatne w takim przypadku byłoby zaimplementowanie identycznego interfejsu.
# Jest to możliwe dzięki implementacji metod __getitem__(self, index) oraz __setitem__(self, index, value)

# Metoda:
# __getitem__(self, index)
# jest wywoływana, gdy wartość jest odczytywana za pomocą operatora []:

# value = obj[index]

# Metoda:
# __setitem__(self, index, value)
# jest wywoływana, gdy wartość jest zapisywana za pomocą operatora []:

# obj[index] = value


# Interfejs Iterable:

# Python pozwala również używać obiektu, służy do tego metoda

# def __iter__(self):
# Wartością zwracaną przez tą metodę musi być iterator bądź generator.

# Przykład z użyciem generatora:

def __iter__(self):
    for x in range(6):
        yield x

# W przypadku, gdy odpowiedzią mogłaby być lista, możemy stworzyć iterator z listy za pomocą funkcji iter:

def __iter__(self):
    return iter([0, 1, 2, 3, 4 ,5])

# W obu przypadkach wykonanie kodu:

# for elem in obj:
#     print(elem)
# da ten sam rezultat.

# Iterator to obiekt implementujący metodę __next__(self). Metoda ta zwraca rezultat dla bieżącego kroku pętli 
# lub podnosi wyjątek StopIteration, gdy skończyły się elementy w tablicy.

# Przykładowa implementacja, gdy obiekt jest własnym iteratorem (klasa, która przechowuje raz otwarty plik w pamięci):

class FileReader:
    def __init__(self, filepath):
        self.fp = open(filepath)
        self.lines = []
        self.done = False

    def __iter__(self):
        if self.done:
            return iter(self.lines)
        return self

    def __next__(self):
        line = self.fp.readline()
        if not line:
            self.done = True
            self.fp.close()
            raise StopIteration
        self.lines.append(line[:-1])
        return line[:-1]
      
for line in FileReader("dane.txt"):
    print(line)


