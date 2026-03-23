# % Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.

# % Na koniec działania program powinien wyświetlić w podsumowaniu:
# %     Liczbę paczek wysłanych
# %     Liczbę kilogramów wysłanych
# %     Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
# %     Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik


# % Restrykcje:
# %     Waga elementów musi być z przedziału od 1 do 10 kg.
# %     Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
# %     W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
# %     W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

no_packages = int(input('podaj liczbę planowanych paczek '))
weight_total = 0
no_boxes = 1
weight_box = 0
weight_list = []

for i in range(no_packages):
    product_weight = int(input(f'podaj wagę {i+1} paczki: '))

    if product_weight < 1 or product_weight > 10:
        break
    weight_total += product_weight     
    if weight_box+product_weight <= 20:
        weight_box += product_weight
    else:
        weight_list.append(weight_box)
        weight_box = product_weight
        no_boxes +=1
if weight_box > 0:
    weight_list.append(weight_box) 

najlzejszy_box = min(weight_list)
numer_najlżejszego_boxa = weight_list.index(najlzejszy_box) + 1

print(f"""
liczba wysłanych paczek: {no_boxes},
Liczbę kilogramów wysłanych: {weight_total},
Suma "pustych"- kilogramów {no_boxes * 20 - weight_total}kg.
{numer_najlżejszego_boxa} paczka miała najwięcej "pustych" kilogramów, ważyła {najlzejszy_box}kg
        """)