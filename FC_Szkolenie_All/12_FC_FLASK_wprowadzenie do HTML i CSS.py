# <!-- Wprowadzenie do HTML/XML:

# Język HTML to wariant języka XML dostosowany do potrzeb prezentacji treści w sieci WWW. Jest to język opisowy tworzący strukturę drzewa. Węzły drzewa (tagi) zawierają się w innych tagach.

# Podstawowym budulcem w HTML jest Tag:

# <nazwatagu>

# Powyższy blok rozpoczyna tag "nazwatagu" treść podana po <nazwatagu> będzie się znajdować wewnątrz podanego tagu. Aby zamknąć tag, stosujemy podobną składnię:

# </tagname>
# Zwróć uwagę na ukośnik.

# Nazwa tagu może zawierać znaki alfanumeryczne oraz "-" "_"

# Jak tagi są osadzane?

# <tagname>
# 	<subtagname></subtagname>
# 	<subtagname></subtagname>
# </tagname>

# W powyższym przykładzie dokument xml składa się z jednego elementu tagname zawierającego dwa elementy subtagname. Tagi mogą się powtarzać, a ich kolejność ma znaczenie.

# Tagi muszą być zamykane w odwrotnej kolejności, niż były otwierane. Poniższy kod nie jest prawidłowym kodem XML:

# <tagname>
# 	<subtagname1><subtagname2>
# 	<subtagname1></subtagname2>
# </tagname>

# Tag, który nie ma wewnątrz dodatkowej zawartości, może być zamknięty według powyższej składni:

# <nazwatagu />

# Zwróć uwagę na końcowy ukośnik. Dwie poniższe linie są sobie równoważne:

# <nazwatagu></nazwatagu>
# <nazwatagu />

# Każdy tag może dodatkowo zawierać atrybuty:

# <nazwatagu atrybut1=wartosc1 atrybut2=wartosc2></nazwatagu>

# Nazwy atrybutów powinny być unikalne wewnątrz danego elementu. Jeśli wartość zawiera znaki spoza zakresu A-Z a-z 0-9, wartość należy ująć w cudzysłowy lub apostrofy.

# <nazwatagu atrybut1=wartosc1 atrybut2="wartość która zawiera spację"></nazwatagu>

# Element może zawierać jednocześnie pod-elementy i atrybuty.

# <tagname atrybut1=wartosc1 atrybut2="wartość która zawiera spację">
# 	<subtagname1><subtagname2>
# 	<subtagname1></subtagname2>
# </tagname>


# Podstawowy szkielet kodu HTML


# <!DOCTYPE html>
# <html>
#  <head>  
#    <meta charset="utf-8" />  
#    <title></title>  
#    <meta name="author" content="" />  
#    <meta name="description" content="" />  
#    <meta name="viewport" content="width=device-width, initial-scale=1" />
#    <link href="css/style.css" rel="stylesheet">
#  </head>
#  <body>
#    ...
# ﻿ </body>
# </html>

# Elementy widoczne na stronie powinny być dodanie wewnątrz tagu <body>, każdy dokument html powinien zawierać tylko jeden tag <html> na najwyższym poziomie, zawierający tylko jeden element z tagiem head i jeden element o tagu body.
# W tagu head zapisujemy informacje o zaimportowanych stylach (tag link), tytule strony (tag title) i kodowaniu <meta charset>.

# Podstawowymi tagami do opisu treści są:

# 1. img src

# <img src="sciezka-do-plliku.jpg" />
# Za pomocą tego tagu dodasz obraz do dokumentu. Opcjonalne parametry tego tagu to width i height opisujące wielkość obrazka.

# 2. h1, h2, h3...
# Nagłówki o różnym poziomie:

# <h1>Treść nagłówka</h1>
# <h2>Treść nagłówka</h2>
# <h3>Treść nagłówka</h3>
# <h4>Treść nagłówka</h4>
# <h5>Treść nagłówka</h5>
# <h6>Treść nagłówka</h6>﻿

# 3. p
# Znacznik dla pojedynczego paragrafu tekstu:

# <p>Paragraf teksu</p>

# 4. div
# Podstawowy tag służący do podziału treści dokumentu na pod-elementy.

# <div></div>


# W języku HTML mamy dwa specjalne atrybuty służące między innymi do stylowania elementów: id oraz class. Id musi mieć unikalną wartość w skali całego dokumentu. Parametr class może się powtarzać. Wewnątrz atrybutu class nazwy poszczególnych klas oddzielamy spacjami.

# <div id="pierwszy-element" class="klasa-1 klasa-2 klasa-3"></div>

# Nazwy identyfikatorów i klas mogą składać się tylko ze znaków alfanumerycznych i "-" "_".

# Pliki html zapisujemy z rozszerzeniem "html" lub "htm".

# Formularze:

# Formularze służą do przesyłania treści na serwer www. Formularze tworzymy poprzez tag:

# <form method="METODA" action="ADRES"> ... Zawartość formularza ...</form>
# METODA to sposób przesłania danych na serwer:

#  GET: wszystkie pola formularza są dodawane na koniec adresu URL podanego w polu action, za znakiem "?". Jest to domyślny sposób, w jaki formularze są wysłane na serwer
# POST: Pola są wysyłane w sposób ukryty - nie pojawią się nigdzie w adresie URL.
# ADRES jest do docelowy adres, pod który wysyłamy dane.

# Każde pole w formularzu powinno zawierać atrybut "name", jest to nazwa pola, które wpisujemy. Atrybut ten służy do odwoływania się do pola wewnątrz kodu HTML, jego wartość nie jest widoczna na stronie.
# Natomiast tekst, który jest wyświetlany na stronie - etykietę danego pola, określa element label:

# <label>Etykieta pola</label>

# Zawartością formularza mogą być:

# Pole tekstowe - jedna linia:

# <input type="text" name="nazwa pola" value="wartosc domyslna" />
# Pole tekstowe - tylko numery:

# <input type="number" name="nazwa pola" value="wartosc domyslna" />
# Pole typu checkbox:

# <input type="checkbox" name="nazwa pola" />
# Jeśli chcecie, żeby pole było domyślnie zaznaczone:

# <input type="checkbox" checked="checked" name="nazwa pola" />
# Jeśli chcecie przekazać wartość niewidoczną dla użytkownika:

# <input type="hidden" name="nazwa pola" value="wartosc pola" />

# Przycisk do wysłania formularza:

# <input type="submit" value="Etykieta przycisku" />
# lub
# <button type="submit">Etykieta Pola</button>


# Spectre CSS

# Spectre jest to prosty framework, który pozwoli Ci stworzyć przyzwoicie wyglądające strony bez osobnego deklarowania styli i tworzenia kodu CSS i JS.

# Oficjalna strona frameworku:
# https://picturepan2.github.io/spectre/getting-started.html

# Aby dołączyć Spectre.Css do swojej strony wstaw poniższy kod do sekcji <head>:

# <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre.min.css">
# <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-exp.min.css">
# <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-icons.min.css">

# Spectre.CSS korzysta z układu 12 kolumn. To znaczy, że szerokość kontenera jest dzielona na 12 równych części. Gdy deklarujemy szerokość kolumny, używamy wielokrotności 1/12 dostępnej szerokości.

# Klika przykładów wykorzystania:

# Zgodnie z dokumentacją: https://picturepan2.github.io/spectre/layout/grid.html , utworzenie 3 kolumn o równej szerokości (12 / 3 == 4):

#   <div class="columns">
#     <div class="column col-4">col-6</div>
#     <div class="column col-4">col-3</div>
#     <div class="column col-4">col-2</div>
#   </div>

# Jeśli kolumny nie mają mieć odstępu między elementami:

#   <div class="columns col-gapless">
#     <div class="column col-4">col-6</div>
#     <div class="column col-4">col-3</div>
#     <div class="column col-4">col-2</div>
#   </div>

# Formularze wymagają użycia dodatkowych klas:

# <div class="form-group">
#   <label class="form-label" for="input-example-1">Name</label>
#   <input class="form-input" type="text" id="input-example-1" placeholder="Name">
# </div>

# Sprawdź dokumentację w dziale Utilities i Components.
# Na ten moment odradzam elementy z działu Experimentals. -->