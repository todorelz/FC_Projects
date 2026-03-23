
# Kilka słów o wcięciach i ich znaczeniu
#
# Python jest językiem, w którym wcięcia mają znaczenie. Nie są tylko ozdobnikiem, wskazują również, w jaki sposób będzie wykonywany program.
#
# Spróbuj wykonać następujący program:

print("Hello", "World")
    # print("Hello", "World")
print("Hello", "World")


# Przy próbie uruchomienia otrzymasz następujący błąd:
# IndentationError: unexpected indent
#
# Powszechnie przyjętym standardem jest wcięcie będące wielokrotnością 4 spacji. Standard python zakłada również, że
# zawsze używamy spacji, nie tabulacji. Dlatego też naciśnięcie <tab> w Pycharm automatycznie zmienia wcięcie na 4 spacje
# Jeśli chcesz wsunąć cały blok w edytorze, zaznacz go i naciśnij <Tab>, jeśli chcesz zmniejszyć poziom wcięcia, naciśnij
# <Shift>+<Tab>.

# Instrukcja warunkowa IF
#
# Instrukcja ta warunkowo wykonuje blok kodu. Podstawowa składnia (zwróć uwagę na wcięcie i dwukropek po warunku):
#
# if {warunek}:
# 	{kod do wykonania linia 1}
# 	{kod do wykonania linia 2}
# 	{kod do wykonania linia 3}
# {kod do wykonania linia 4}
#
#
# Zwróć uwagę na wcięcie. Sygnalizuje ono fragment bloku, który będzie wykonany, jeśli warunek będzie spełniony.
# W przypadku, gdy warunek jest prawdziwy, zostaną wykonane linie 1,2,3,4, jeśli warunek nie jest spełniony, tylko
# linia 4 zostanie wykonana. Warunkiem może być zarówno zmienna, jak i wyrażenie. Przykłady:

a = 3
if a % 2 == 1:
    print("a jest nieparzyste")

# Zauważ, że warunek jest spełniony, tzn. wyrażenie a % 2 == 1 ma wartość True.
# W tym konkretnym wypadku wartość bool( a % 2 == 1) jest tożsama z bool( a % 2) możemy uprościć ten kod do:

a = 3
if a % 2:
    print("a jest nieparzyste")


# Warunek może być również wartością bezpośrednio logiczną:

a = True
b = False
c = a or b
if c:
    print("Warunek prawdziwy")

# Co w przypadku użycia łańcucha znaków?

c = "Przykładowy tekst"
if c:
    print("Ta linia zostanie wykonana")
c = ""
if c:
    print("To polecenie zostanie pominięte")

# Tylko pierwsza komenda print zostanie wykonana. Dlaczego? Ponieważ bool("") jest równoważny False.

# Rozszerzona wersja instrukcji IF
#
# Załóżmy, że chcemy wykonać dwie różne wersje kodu w zależności od wyniku wyrażenia. Możemy to zrealizować za pomocą następującego kodu:
#
# if {wyrażenie}:
# 	{kod jeśli wyrażenie jest prawdziwe}
# if not {wyrażenie}:
# 	{kod jeśli wyrażenie jest fałszywe}
#
#
# Nie jest to najprostsze podejście. Python udostępnia dla takich przypadków uproszczoną formę:
#
# if {wyrażenie}:
# 	{kod jeśli wyrażenie jest prawdziwe}
# else:
# 	{kod jeśli wyrażenie jest fałszywe}
#
# Oba wyrażenia zwrócą ten sam wynik.

# Przykładowy kod:

a = 3
if a % 2:
    print("a jest nieparzyste")
if not a % 2:
    print("a jest parzyste")


# Uproszczony kod:

a = 3
if a % 2:
    print("a jest nieparzyste")
else:
    print("a jest parzyste")

# Zagnieżdżone warunki


# Każdy blok kodu może zawierać w sobie inne podbloki, wyróżnione poziomem wcięcia. Przykładowy kod dla znanego zadania
# FizzBuzz (jeśli podana liczba dzieli się przez 5, wydrukuj Fizz, jeśli dzieli się przez 3 "Buzz", jeśli dzieli się
# przez 3 i 5 wydrukuj "Fizzbuzz", w przeciwnym wypadku wydrukuj podaną liczbę:

liczba = int(input("Podaj liczbę "))
if liczba % 5 and liczba % 3: # prostszy warunek liczba % 15
    print(liczba)
else:
    response = ""
    if liczba %5 == 0:
        response = response + "Fizz"
    if liczba %3 == 0:
        response = response + "Buzz"
    print(response)


# W powyższym kodzie blok wewnątrz zewnętrznej części else zawiera dodatkowe podbloki. Taka sama sytuacja może wystąpić w
# bloku IF. Poniższy kod zwróci ten sam wynik:
liczba = int(input("Podaj liczbę "))
if liczba % 5 == 0 or liczba % 3 == 0:
    response = ""
    if liczba %5 == 0:
        response = response + "Fizz"
    if liczba %3 == 0:
        response = response + "Buzz"
    print(response)
else:
    print(liczba)

# Ciąg warunków


# Powyższy kod FizzBuzz wymaga zagnieżdżonych bloków if / else. Jest skuteczny, ale niekoniecznie najbardziej czytelny.
# I tutaj Python posiada składnię, która uprości kod. Gdy pierwszy test nie zostanie spełniony, pozostałe przypadki
# możemy również rozdrobnić następnym warunkiem, na tym samym poziomie zagnieżdżenia. Uwaga - ciąg warunków jest
# sprawdzany do momentu, aż któryś warunek zostanie spełniony. Przykładowo jeśli spełniony będzie warunek1 to kolejne
# warunki nie będą rozpatrywane. Składnia:
# if {warunek1}:
# 	{kod wykonywany gdy warunek1 jest prawdziwy
# elif {warunek2}:
# 	{kod wykonywany gdy warunek1 jes fałszywy i warunek2 prawdziwy}
# ....
# elif {warunekN}:
# 	{kod wykonywany gdy warunek 1 do warunek n-1 jest fałszywy i warunek n prawdziwy}
# else:
# 	{kod wykonywany gdy warunki 1-n były fałszywe}

# Ostatnie dwie linie są opcjonalne, blok else, jeśli występuje, to musi być dodany jako ostatni.
#
# Nasz program do FizzBuzz w uproszczonej formie:

liczba = int(input("Podaj liczbę "))
if not liczba % 15:
    print("FizzBuzz")
elif not liczba % 5:
    print("Fizz")
elif not liczba % 3:
    print("Buzz")
else:
    print(liczba)


# Pętla While
#
# Kod w bloku if zostanie wykonany najwyżej raz. Jeśli chcemy, by był wykonany więcej razy, użyjemy do tego instrukcji "while". Składnia:
#
# while {warunek}:
# 	{kod wykonywany póki warunek jest prawdziwy}
#
#
# Uwaga: upewnij się, że kod wewnątrz while może zmienić warunek. Tak, by program nie wykonywał się w nieskończoność!
#
# Przykład. Kod, który sprawdza czy podana liczba jest liczbą pierwszą. Zacznijmy od napisania fragmentu kodu, który
#     wydrukuje nam czynniki danej liczby.

number = int(input("Podaj liczbę "))
x = number // 2
while x > 1:
    if number % x == 0:
        print(f"{number} ma czynnik {x}")
    x -= 1

# Przykładowy wynik:
#
# Podaj liczbę 24
# 24 ma czynnik 12
# 24 ma czynnik 8
# 24 ma czynnik 6
# 24 ma czynnik 4
# 24 ma czynnik 3
# 24 ma czynnik 2

# Program działa prawidłowo zwracając czynniki podanej liczby. Dodajmy warunek, który wydrukuje informację czy podana
# liczba jest liczbą pierwszą. Możemy to zrobić np. wprowadzając zmienną factor, która ma na początku wartość zero
# i będzie mieć wartość czynnika x, jeśli taki istnieje. Jeśli zmienna number ma kilka czynników to i tak bool(factor)
# będzie True, bo factor będzie mieć wartość różną od 0.

number = int(input("Podaj liczbę "))
x = number // 2
factor = 0
while x > 1:
    if number % x == 0:
        print(f"{number} ma czynnik {x}")
        factor = x
    x -= 1
if not factor:
    print(f"{number} jest liczbą pierwszą")
else:
    print(f"{number} nie jest liczbą pierwszą")


# Użycie break, else wewnątrz pętli

# Czasami może zaistnieć potrzeba wyjścia z wewnątrz pętli zanim całość bloku zostanie wykonane. Służy do tego instrukcja break:
#
# Przykładowy program drukujący silnię:

counter = 0
product = 1
while counter < 10:
    counter += 1
    product *= counter
    print("{}: {}".format(counter, product))

# powinien zwrócić:

# 1: 1
# 2: 2
# 3: 6
# 4: 24
# 5: 120
# 6: 720
# 7: 5040
# 8: 40320
# 9: 362880
# 10: 3628800

# Wstawmy teraz instrukcję break, która zakończy przedwcześnie program, gdy silnia (product) osiągnie wartość większą niż 1000:

counter = 0
product = 1
while counter < 10:
    counter += 1
    print("obliczam {}".format(counter))
    product *= counter
    if product > 1000:
        break
    print("{}: {}".format(counter, product))

# Przykładowe wyjście:
#
# obliczam 1
# 1: 1
# obliczam 2
# 2: 2
# obliczam 3
# 3: 6
# obliczam 4
# 4: 24
# obliczam 5
# 5: 120
# obliczam 6
# 6: 720
# obliczam 7

# Zauważ, że 7 przejście pętli zostało rozpoczęte (stąd linia "obliczam 7"), ale nie dotarło do końca bloku.
# Instrukcja break jest często używana jako zabezpieczenie przed nieskończonym wykonywaniem programu.
#
# Używając pętli można skorzystać z bloku else, który zostanie wykonany wtedy (i tylko wtedy), gdy pętli nie zakończyła
# instrukcja break. Poprawmy nasz program do sprawdzania czy podana liczba jest liczbą pierwszą, tak aby kończył się
# w momencie, gdy znajdzie się chociaż jeden czynnik dla podanej liczby (bo już wtedy będzie wiadomo, że liczba nie jest
# pierwsza) oraz żeby wykorzystywał klauzulę else pętli.

number = int(input("Podaj liczbę "))
x = number // 2
while x > 1:
    if number % x == 0:
        print(f"{number} nie jest liczbą pierwszą")
        break
    x -= 1
else:
    print(f"{number} jest liczbą pierwszą")


# Zwróć uwagę, że klauzula else zostanie wykonana również wtedy, gdy ciało pętli nie zostanie nigdy wykonane. Na przykład dla liczb ujemnych.
# Poprawmy nasz program, aby działał prawidłowo, również dla liczb ujemnych.

number = int(input("Podaj liczbę "))
if number < 2:
    print(f"{number} nie jest liczbą pierwszą")
else:
    x = number // 2
    while x > 1:
        if number % x == 0:
            print(f"{number} nie jest liczbą pierwszą")
            break
        x -= 1
    else:
        print(f"{number} jest liczbą pierwszą")



# Instrukcja "continue"
#
# Co, gdy chcemy pominąć część kodu i w bloku, ale tylko w obecnym przebiegu? Możemy użyć zagnieżdżonego warunku if.
#
# Przykład:
# Mały program, który pobiera wiek wszystkich pasażerów lotu. Koszt biletu dziecka to 200 zł, koszt biletu pełnoletniej
# osoby to 400 zł. Jeśli pasażer jest pełnoletni może również zamówić alkohol (maksymalnie 3 lampki wina, każda w
# cenie 10 zł). Pasażerów może być maksymalnie 20. Program oblicza całkowity przychód z biletów. Jeśli wiek podanego
# pasażera to 0 lub została osiągnięta maksymalna liczba pasażerów, program kończy działanie wyświetlając podsumowanie:
# Pełen przychód, liczbę pasażerów dorosłych, liczbę dzieci, liczbę lampek wina.

wine_count = 0
children_count = 0
adult_count = 0
passenger_count = 0

while passenger_count < 20:
    print("podaj wiek pasażera")
    age = int(input())
    if age == 0:
        break
    elif age < 18:
        children_count += 1
    else:
        adult_count += 1
    passenger_count += 1
    print("podaj liczbę lampek wina")
    wine_current = int(input())
    if wine_current > 3:
        print("nieprawidłowa liczba lampek wina")
    elif wine_current < 0:
        print("nieprawidłowa liczba lampek wina")
    else:
        wine_count += wine_current
    print("Dorosłych: {}, Dzieci: {}, lampek wina: {}, Przychód: {}".format(
        adult_count,
        children_count,
        wine_count,
        adult_count * 400 + children_count * 200 + wine_count * 10
    ))


# Kod jest dosyć rozbudowany, do tego pyta o liczbę lampek wina dla dzieci! W przypadku błędu podaje też złą liczbę
# pasażerów. Uprośćmy kod używając instrukcji continue:

wine_count = 0
children_count = 0
adult_count = 0
passenger_count = 0
while passenger_count < 20:
    print("podaj wiek pasażera")
    age = int(input())
    if age == 0:
        break
    elif age < 18:
        children_count += 1
        passenger_count += 1
        continue
    print("podaj liczbę lampek wina")
    wine_current = int(input())
    if wine_current < 0 or wine_current > 3:
        print("nieprawidłowa liczba lampek wina")
        continue
        wine_count += wine_current
        adult_count += 1
        passenger_count += 1
    print("Dorosłych: {}, Dzieci: {}, lampek wina: {}, Przychód: {}".format(
        adult_count,
        children_count,
        wine_count,
        adult_count * 400 + children_count * 200 + wine_count * 10
    ))

# Dzięki użyciu "continue" program nie zapyta o liczbę lampek wina dla dziecka, łatwiej też obsłuży błąd związany z
# niewłaściwą liczbą lampek wina

# Ogólny format pętli while

# while {warunek1}:
#     {kod wykonywany dopóki warunek jest prawdziwy}
#     if {warunek2}: break #wyjście z pętli, pominięcie reszty
#     if {warunek3}: continue #przejście do góry pętli, do warunku1
# else:
#     {kod wykonywany, jeśli pętli nie zakończyło break}
#
# Pętla FOR
#
# Pętla ta służy do wykonania konkretnego bloku, gdy z góry znamy liczbę powtórzeń. Składnia:
#
# for {zmienna} in range({wartość końcowa}):
#     {kod wykonywany zadaną liczbę razy}
#
# Zmienna w każdym przebiegu przyjmuje po kolei wartości z zakresu 0 do maksymalna wartość - 1

# Druga opcja:
#
# for {zmienna} in range({wartość początkowa}, {wartość końcowa}):
#     {kod wykonywany zadaną liczbę razy}
#
# Zmienna w każdym przebiegu przyjmuje po kolei wartości z zakresu minimalna wartość do maksymalna wartość - 1


# Trzecia opcja:
#
# for {zmienna} in range({wartość początkowa}, {wartość końcowa}, {krok}):
#     {kod wykonywany zadaną liczbę razy}
#
# W pierwszym przebiegu zmienna przyjmuje wartość "wartość początkowa", w każdym następnym przyjmuje poprzednią wartość
#     + krok, aż osiągnie wartość końcową (wartość końcowa nie jest uwzględniana)
#
# przykładowy kod:

for i in range(0,6):
    print("Pętla 1 {}".format(i))
for i in range(2,6):
    print("Pętla 2 {}".format(i))
for i in range(14, 6, -2):
    print("Pętla 3 {}".format(i))

# wynik działania:
#
# Pętla 1 0
# Pętla 1 1
# Pętla 1 2
# Pętla 1 3
# Pętla 1 4
# Pętla 1 5
# Pętla 2 2
# Pętla 2 3
# Pętla 2 4
# Pętla 2 5
# Pętla 3 14
# Pętla 3 12
# Pętla 3 10
# Pętla 3 8


# Uwaga: instrukcje "continue" i "break" również działają w pętlach for! W pętli for również działa klauzula "else" pętli.

# Przykładowy program dla zakładu mechanicznego:
# w zakładzie pracuje 3 mechaników, każdy ma 8 godzin pracy dziennie. Użytkownik podaje liczbę samochodów do obsłużenia, następnie dla każdego samochodu podaje liczbę godzin potrzebną do zakończenia pracy mechanika. Przypisujemy poszczególne usługi do mechaników wybierając mechanika z obecnie najmniejszą liczbą godzin roboczych. Jeśli liczba jest ta sama, wybieramy mechanika z niższym numerem. Godziny pracy nie mogą być dzielone na mechaników.
# Program powinien zwrócić liczbę dni, których potrzeba do zwolnienia któregokolwiek z mechaników, oraz liczbę dni potrzebnych wszystkim mechanikom do zakończenia zleceń:

print("Podaj liczbę zleceń")
job_count = int(input())
workload1 = 0
workload2 = 0
workload3 = 0
for job in range(job_count):
    print("Podaj liczbę godzin pracy dla zlecenia")
    job_hours = int(input())
    if job_hours <= 0:
        print("Błąd: Nieprawidłowa liczba godzin!")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours
print("Najbliży mechanik będzie wolny w ciągu {} dni".format(
    int((min(workload1, workload2, workload3)+7)  / 8)
))
print("Wszyscy mechanicy będą wolni w ciągu {} dni".format(
    int((max(workload1, workload2, workload3)+7)  / 8)
))



# Parametry podawane w linii poleceń


# Do tej pory pobieraliśmy parametry wpisując je podczas wykonywania programu. Parametry możemy przekazać również jako argument w linii komend.
#
# Przykładowo program main.py wykonujemy poprzez komendę:
#
# python main.py<Enter>
#
# Parametry, które przekazujemy, podajemy oddzielane spacją po nazwie pliku:
#
# python main.py parametr1 parametr2 ....<Enter>
#
# Jeśli podawany argument zawiera spację, ujmij go w cudzysłów:

# python main.py "parametr ze spacją" parametr2 ...<Enter>
#
#
# Aby skorzystać z wbudowanej obsługi parametrów, musimy zaimportować wbudowany moduł "sys" na początku pliku:

import sys


# Wartość pierwszego argumentu jest dostępna jako

sys.argv[1]

# drugiego

sys.argv[2]

# itd
#
# Oto, jak możemy podać liczbę zleceń jako pierwszy argument do programu:

import sys

job_count = int(sys.argv[1])
workload1 = 0
workload2 = 0
workload3 = 0
for job in range(job_count):
    print("Podaj liczbę godzin pracy dla zlecenia")
    job_hours = int(input())
    if job_hours <= 0:
        print("Błąd: Nieprawidłowa liczba godzin!")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours
print("Najbliży mechanik będzie wolny w ciągu {} dni".format(
    int((min(workload1, workload2, workload3)+7)  / 8)
))
print("Wszyscy mechanicy będą wolni w ciągu {} dni".format(
    int((max(workload1, workload2, workload3)+7)  / 8)
))


