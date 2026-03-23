# [] # pusta lista
# list() # pusta lista﻿
# [1, 2, 3, 6, 8, 12, -1] # lista z wartościami liczbowymi
# ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"] # lista zawierająca ciągi znaków
# ["Adam", 1, False, "Ewa", 2] #lista zawierająca różne typy
# ["Adam", ["Marcin", "Krzysztof", 1], 2, "Anita"] # lista może również zawierać inne listy


#Listy przypisujemy do zmiennych w ten sam sposób, jak inne wartości:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]


# Dostęp do elementów listy jest możliwy przez dodanie [{{index}}] po nazwie zmiennej:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
print(firstnames[0])
#prints "Adam"
print(firstnames[1])
#prints "Ewa"

# Podany indeks może (i zazwyczaj jest) zmienną lub wyrażeniem.

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
startname_index = 2
print(firstnames[startname_index])
print(firstnames[startname_index+1])
print(firstnames[startname_index+2])

print('------>\n')

# Podanie ujemnego indeksu skutkuje odczytaniem od końca listy. Przykład:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
print(firstnames[-1])
#prints Anita
print(firstnames[-2])
#prints Jakub

# Aby sprawdzić, jaka jest długość całej listy, używamy wbudowanej funkcji len():

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
print(len(firstnames))
#prints 6

# Uwaga! Funkcja range z poprzedniej lekcji zwraca wartość zachowującą się podobnie jak lista. Spróbuj wykonać polecenie w interaktywnej konsoli python:

list(range(6))

# Wynik:
# [0, 1, 2, 3, 4, 5]

# Co to oznacza? Pamiętasz konstrukcję w pętli for z poprzedniej lekcji:

for index in range(6):
    print(index)


# Polecenie range możemy zastąpić dowolnym innym wyrażeniem, które daje w wyniku listę bądź wartość, którą można zmienić w listę. Przykładowo poniższa pętla for da taki sam wynik jak powyższa:

for index in [0, 1, 2, 3, 4, 5]:
    print(index)

# Zmienna, na którą rzutujemy wartości, może zawierać dowolne inne wartości, np. łańcuchy znaków:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
for firstname in firstnames:
    print("Imię: {}".format(firstname))

# Raz zdefiniowana lista może być zmieniana w trakcie działania programu. Aby dodać nowy element na końcu listy, użyj metody {{zmienna}}.append()

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
print("Dwa ostatnie elementy: {} {}".format(firstnames[-2], firstnames[-1]))
firstnames.append("Iwona")
print("Dwa ostatnie elementy: {} {}".format(firstnames[-2], firstnames[-1]))

# Aby zmodyfikować wartość, która jest zapisana w liście, używamy podobnej konstrukcji jak przy odczytywaniu i zapisywaniu zmiennej:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
print("Imię pod indeksem 1 to {}".format(firstnames[1]))
firstnames[1] = "Marta"
print("Imię pod indeksem 1 to {}".format(firstnames[1]))

# Aby wstawić nowy element w dowolnym miejscu listy, użyj metody {{zmienna}}.insert({{index}}, {{wartość}}).

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
for firstname in firstnames:
    print(firstname)
firstnames.insert(2, "Marta")
for firstname in firstnames:
    print(firstname)


# Listy można również dodawać. Wynikowa lista będzie zawierać elementy obu list, najpierw elementy pierwszej listy, potem drugiej.

firstnames_female = ["Ewa", "Anita"]
firstnames_male = ["Adam", "Marcin", "Krzysztof", "Jakub"]

firstnames = firstnames_female + firstnames_male
for firstname in firstnames:
    print(firstname)

# Usuwać elementy z list można na dwa sposoby:
# I. Poprzez wbudowaną instrukcję del:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
del firstnames[2]
for firstname in firstnames:
    print(firstname)

# Ta metoda wiąże się z koniecznością znajomości indeksu, który chcemy usunąć.

# II. Możemy również usunąć elementy z listy na podstawie wartości za pomocą metody remove: {{zmienna}}.remove({{wartość}})

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
firstnames.remove("Marcin")
for firstname in firstnames:
    print(firstname)

# Metoda remove usunie PIERWSZE wystąpienie danej wartości.

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita", "Marcin"] # zwróć uwagę na powtórzenie "Marcin"
print(len(firstnames))
firstnames.remove("Marcin")
print(len(firstnames))
print(firstnames)

# Jak znaleźć indeks, pod którym znajduje się dana wartość? Metoda index zwraca index z PIERWSZYM wystąpieniem wartości.

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita", "Marcin"] # zwróć uwagę na powtórzenie "Marcin"
print(firstnames.index("Marcin"))


# Drugim opcjonalnym parametrem jest pierwszy numer indeksu, który chcemy sprawdzić. Dzięki temu parametrowi możemy dotrzeć do pozostałych indeksów z tą samą wartością:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita", "Marcin"] # zwróć uwagę na powtórzenie "Marcin"
print(firstnames.index("Marcin"))
print(firstnames.index("Marcin", 3))


# Listy w wyrażeniach logicznych
#
# Aby sprawdzić, czy dany element znajduje się w liście, stosujemy operatory "in" / "not in"

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
if "Jakub" in firstnames:
    print("Imię Jakub jest dostępne")
else:
    print("Ten blok nie będzie wykonany")

if "Weronika" not in firstnames:
    print("Imię Weronika nie jest dostępne")
else:
    print("Ten blok nie będzie wykonany")

# Lista jako warunek zwraca True, gdy posiada jakiekolwiek parametry:

sample_list = []
print(bool(sample_list)) # returns False
sample_list = ["a", "b"]
print(bool(sample_list)) # returns True
sample_list = [""]
print(bool(sample_list)) # returns True


# W przypadku użycia instrukcji IF:

sample_list = []
if sample_list:
    print("Lista ma elementy")
else:
    print("Lista jest pusta")

# Krotki

# Krotki (tuple) są podobne do list, z zastrzeżeniem, że raz zadeklarowane nie mogą być modyfikowane.
# Tuple deklaruje się poprzez oddzielanie wartości przecinkami. Gdy sama deklaracja z przecinkami nie pozwala na
# jednoznaczną deklarację, używamy okrągłych nawiasów.

empty_tuple = tuple()
integer_tuple = 1, 2, 3, 4
mixed_tuple = "a", 1, "b", 2, True
single_element_tuple = tuple(["single element"])
single_element_tuple = "single element", # przecinek na końcu!
tuple_inside_of_list = [(1, 2), (3,), 4, 5]


# Elementy tupli są dostępne tak samo, jak w liście, z tą różnicą, że nie mogą być modyfikowane.

mixed_tuple = "a", 1, "b", 2, True
print(mixed_tuple[2])

# Metoda .index, jak i operatory "in", "not in" również są dostępne.

mixed_tuple = "a", 1, "b", 2, True
print(mixed_tuple.index("b"))
print("a" in mixed_tuple)


# Tuple mogą być przekształcane w listy, a listy w tuple.

mixed_tuple = "a", 1, "b", 2, True
mixed_list = list(mixed_tuple)

mixed_list2 = ["a", 1, "b", 2, True]
mixed_tuple2 = tuple(mixed_list2)

# Główne różnice w wydajności między listami a tuplami:
#
#     Operatory "in", "not in" są znacząco szybsze w tuplach
#     Tworzenie tupli jest znacząco szybsze niż tworzenie listy
#     Porównywanie dwóch tupli jest znacząco szybsze niż porównywanie dwóch list.


# Przypisanie wielu zmiennych w jednej linii za pomocą tupli
#
# Następująca deklaracja jest jak najbardziej prawidłowa:

a, b = 1, 2
print(a)
print(b)

# a funkcjonalność jest szczególnie przydatna w pętlach for:

fullnames = [
	("Adam", "Abacki"),
	("Bartosz", "Babacki"),
	("Czesław", "Cabacki")
]
for firstname, lastname in fullnames:
    print("{} {}".format(firstname, lastname))

# Ta właściwość tupli pozwala również na łatwe użycie wbudowanej funkcji "enumerate"
# Funkcja enumerate pobiera za parametr listę, a zwraca generator (obiekt obsługujący protokół iteracji, będzie omówiony
# dokładniej na kolejnych lekcjach). Zamieniając wynik funkcji enumerate na listę otrzymamy listę składają się z tupli,
# gdzie pierwszy element tupli jest indeksem, a drugi wartością z oryginalnej listy). Przykładowo lista:

mixed_list = list(enumerate(["a", 1, "b", 2, True]))

# będzie miała wartość:

mixed_list = [
  (0, "a"),
  (1, 1),
  (2, "b"),
  (3, 2),
  (4, True)
]
# Przykładowe użycie w pętli for:

firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita"]
for index, firstname in enumerate(firstnames):
    print("Imię {}: {}".format(index+1, firstname))


# Hashable, id
#
# Typty zmiennych hashable to typy, które są tylko do odczytu i takie, które mogą być rzutowane na ciąg znaków, to znaczy
# przy każdej operacji zmieniającej ich wartość są na nowo tworzone.
# Aby sprawdzić, które typy są na nowo tworzone, możesz wykorzystać funkcję id.
# Funkcja id zwraca unikalny wskaźnik pozycji w pamięci danej wartości. Jeśli po operacji zmiany wartości wynik funkcji
# id się zmienia, to znaczy, że jest to wartość immutable.
# Przykładowo:

a = 1
print(id(a))
a = a+1
print(id(a))


# Domyślnie wszystkie podstawowe typy: int, float, string są hashable.
# Hashable są również tuple zawierające tylko elementy hashable (typy podstawowe + tuple) .

# Zbiory (Set)
#
# Zbiory to kontenery wartości, w których każda wartość jest unikalna. Deklaruje się je za pomocą nawiasów klamrowych.
# Przykładowe deklaracje:

empty_set = set()
# sample_set = {"a", "b", "c", 1, True, ("a1", "a2", "a3")}

# Tylko wartości hashable mogą być zawarte w zbiorze.

# sample_set = {"a", "b", "c", 1, True, ["a1", "a2", "a3"]}

# Powyższa linia zwróci błąd TypeError (lista nie jest hashable).

# Zbiory obsługują operację dodawania elementów poprzez metodę add:

sample_set = {"a", "b", "c", 1, True}
sample_set.add("d")

# ...usuwania poprzez metodę remove():

sample_set = {"a", "b", "c", 1, True}
sample_set.remove("c")


# Pozwalają na testowanie, czy element zawiera się w zbiorze (in / not in):

sample_set = {"a", "b", "c", 1, True}
print("a" in sample_set)
print("d" not in sample_set)

# Elementy w zbiorze nie są uporządkowane, dlatego nie ma możliwości dostania się do nich według indeksu:

sample_set = {"a", "b", "c", 1, True}
# sample_set[0]

# Druga linia zwróci błąd:

# TypeError: 'set' object is not subscriptable
sample_set = {"a", "b", "c"}
sample_list = ["a", "b", "c"]
print("set:{} list: {}".format(len(sample_set), len(sample_list)))
sample_set.add("c")
sample_list.append("c")
print("set:{} list: {}".format(len(sample_set), len(sample_list)))

# Możliwe jest iterowanie po zbiorze w taki sam sposób, jak po liście, z tym, że nie możemy zakładać, że kolejność
# elementów będzie zachowana:

sample_set = {"a", "b", "c"}
for elem in sample_set:
    print(elem)

# Ten kod może zwrócić wynik:
# a
# b
# c
#
# # ale możemy się również spodziewać:
# b
# a
# c
# Zbiór może być przekształcany w tuple i listę poprzez użycie funkcji tuple, list

sample_set = {"a", "b", "c"}
sample_list = list(sample_set)
sample_tuple = tuple(sample_set)


# Należy pamiętać, że przy takim rzutowaniu kolejność elementów może nie być przewidywalna.

# Istnieje również możliwość rzutowania list i tupli na zbiór, przy czym wszystkie wartości muszą być hashable.

sample_set = set([1,2,3,4])
sample_set = set( (1,2,3,4) )

# Słowniki:
#
#
# Słowniki są kontenerami wartości, które przechowujemy jako pary klucz -> wartość. Klucz musi być wartością hashable,
# natomiast wartość może być dowolna.
# Słowniki deklarujemy jako pary: klucz, wartość oddzielone dwukropkiem, poszczególne pary rozdzielamy przecinkami.
# Całość deklaracji znajduje się wewnątrz nawiasów klamrowych. konstruktorem dla słowników jest "dict"
# Przykładowe deklaracje:

empty_dict = dict()
empty_dict = {}
sample_dict = {"a": 1, "b": 2, "c": None, ("d", "e"): "f"}

# Dostęp do wartości w słowniku, jak i zapis konkretnych wartości jest podobny do list, z tym, że zamiast indeksu używamy klucza.

sample_dict = {"a": 1, "b": 2, "c": None, ("d", "e"): "f"}
print(sample_dict["a"])


# tak samo robimy w przypadku zapisu wartości:

sample_dict = {"a": 1, "b": 2, "c": None, ("d", "e"): "f"}
sample_dict["a"] += 1

# Klucze w słowniku są UNIKALNE. Nie ma możliwości zdefiniowania dwóch wartości dla tego samego klucza, natomiast
# wartością może być lista lub inny słownik.
# Jeśli w słowniku nie występuje podany klucz, interpreter zwróci błąd. Możemy tego uniknąć wykrywając wcześniej, czy
# klucz należy do słownika (in / not in) bądź stosując metodę get.

sample_dict = {"a": 1, "b": 2, "c": None, ("d", "e"): "f"}
print(sample_dict.get("a")) #prints  1
print(sample_dict.get("d")) #prints None
print(sample_dict.get("d", False)) #prints False.

# Operatory in / not in działają na kluczach:

sample_dict = {"a": 1, "b": 2, "c": None, ("d", "e"): "f"}
print("a" in sample_dict) #prints True
print(1 in sample_dict) #prints False


# Jeśli chcemy użyć operatora in / not in na wartościach słownika, możemy użyć metody values

sample_dict = {"a": 1, "b": 2, "c": None, ("d", "e"): "f"}
print("a" in sample_dict.values()) #prints False
print(1 in sample_dict.values()) #prints True

# Usuwamy wartości ze słownika za pomocą instrukcji del:

sample_dict = {"a": 1, "b": 2, "c": None, ("d", "e"): "f"}
del sample_dict["c"]


# Domyślnie iterowanie po słowniku to iterowanie po liście kluczy:

# sample_dict = {"a": 1, "b": 2, "c": 3}
# for k in sample_dict:
#     print("{}: {}".format(k, sample_dict[k])
#
#
# # Przydatna metoda do iterowania po słowniku to .items(). Zwraca ona listę tupli (klucz, wartość). Dzięki niej możemy uprościć powyższy kod kod do:
#
# sample_dict = {"a": 1, "b": 2, "c": 3}
# for k, v in sample_dict.items():
#     print("{}: {}".format(k, v)