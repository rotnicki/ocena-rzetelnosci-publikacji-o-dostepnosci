# Protokół doboru publikacji do kalibracji powtarzalności AI

**Wersja protokołu:** 0.1 — projekt do zamrożenia  
**Data:** 21 sierpnia 2026 r.  
**Dotyczy metodologii:** 0.2-draft  
**Identyfikator metodologii:** `c3280da26d2bf0a5a44dfcddc9105180bf3d4267`  
**Status:** protokół należy zamrozić przed rozpoczęciem właściwej serii kalibracyjnej

## 1. Cel

Celem protokołu jest wybranie publikacji do sprawdzenia, czy dwa niezależne przebiegi AI wykonane według tej samej metodologii prowadzą do porównywalnych wyników.

Protokół ma ograniczyć ryzyko, że publikacje będą wybierane:

- przypadkowo;
- dlatego, że zwróciły uwagę osoby prowadzącej projekt;
- dlatego, że spodziewany jest określony werdykt;
- po zapoznaniu się z wynikami wcześniejszych przebiegów;
- w sposób zmieniany podczas trwania serii.

Protokół reguluje dobór publikacji. Nie zmienia kryteriów oceny, kotwic A–L, klasyfikacji problemów ani reguł werdyktu metodologii 0.2-draft.

## 2. Charakter tej kalibracji

Jest to kalibracja powtarzalności AI w jednym środowisku.

Dla każdej publikacji wykonuje się dwa niezależne przebiegi:

- w dwóch nowych i oddzielnych czatach;
- bez udostępniania drugiemu przebiegowi wyniku pierwszego;
- przy użyciu tej samej wersji metodologii i tego samego protokołu;
- przy możliwie podobnym środowisku, ustawieniach i narzędziach;
- z zapisaniem wszystkich znanych różnic środowiska.

Oba przebiegi mogą wykonywać ten sam system AI. Użycie dwóch różnych systemów AI nie jest wymagane w tej serii. Porównanie różnych systemów może zostać przeprowadzone później jako osobny test przenośności.

Ta seria nie jest pełną walidacją całej metodologii. Sprawdza przede wszystkim jej powtarzalność podczas użycia przez AI.

Zamrożony projekt metodologii 0.2 zawiera także oddzielną propozycję szerszej próby z udziałem eksperta będącego człowiekiem. Niniejszy protokół tej propozycji nie wykonuje ani nie usuwa. Decyzję, czy ją zachować, zmienić albo zastąpić inną kontrolą jakości, wolno podjąć dopiero podczas przygotowywania kolejnej wersji metodologii, a nie w trakcie tej serii.

## 3. Status dotychczasowych prób 0.2

Przypadki ocenione przed zamrożeniem tego protokołu są próbami wstępnymi.

Można je wykorzystywać do:

- sprawdzania działania szablonów, schematów i walidatora;
- wykrywania problemów organizacyjnych;
- przygotowania niniejszego protokołu;
- pomocniczego porównania z późniejszą serią.

Nie wolno włączać ich do podstawowych obliczeń zgodności właściwej serii kalibracyjnej, ponieważ ich dobór nie został ustalony z góry według tego protokołu.

## 4. Wielkość właściwego korpusu

Właściwy korpus obejmuje dokładnie osiem nowych publikacji.

Każda publikacja otrzymuje dwa ukończone, niezależne przebiegi. Plan obejmuje więc:

- 8 publikacji;
- 2 przebiegi każdej publikacji;
- łącznie 16 ukończonych ocen.

Liczby tej nie wolno zwiększać ani zmniejszać na podstawie uzyskanej zgodności, punktacji lub werdyktów.

## 5. Kategorie publikacji

Każdą publikację przypisuje się przed oceną krytyczną do jednej kategorii głównej.

Korpus obejmuje:

1. **Dwie publikacje techniczne lub normatywne** — na przykład o WCAG, EN 301 549, kodzie, technologii asystującej albo narzędziach testowych.
2. **Dwie publikacje prawne lub dotyczące obowiązków zgodności** — na przykład o ustawach, dyrektywach, terminach, wyjątkach lub odpowiedzialności.
3. **Dwie publikacje komercyjne lub praktyczne** — na przykład oferta audytu, usługi, szkolenia, certyfikatu albo poradnik wdrożeniowy.
4. **Jedną publikację opartą na badaniach użytkowników, doświadczeniu użytkownika albo opisie potrzeb określonej grupy.**
5. **Jedną publikację popularną, opiniotwórczą, instytucjonalną albo mieszaną**, której nie da się lepiej przypisać do wcześniejszych kategorii.

Publikację przypisuje się tylko do jednej kategorii głównej, nawet jeżeli łączy kilka rodzajów treści.

Kategorii nie wolno ustalać na podstawie przewidywanej poprawności tekstu.

## 6. Wymagana różnorodność

Osiem wybranych publikacji musi łącznie spełniać następujące warunki:

- co najmniej sześciu różnych autorów lub zespołów autorskich;
- co najmniej sześć różnych miejsc publikacji lub domen;
- nie więcej niż dwie publikacje tego samego autora;
- nie więcej niż dwie publikacje z tego samego miejsca publikacji;
- co najmniej jedna publikacja instytucji publicznej;
- co najmniej jedna publikacja organizacji społecznej, użytkowników albo środowiska eksperckiego;
- co najmniej dwie publikacje podmiotów komercyjnych;
- co najmniej cztery różne obszary tematyczne dostępności.

Dopuszczalne obszary tematyczne obejmują między innymi:

- dostępność cyfrową;
- dostępność informacyjno-komunikacyjną;
- dostępność architektoniczną;
- dostępność produktów i usług;
- prawo i politykę publiczną;
- prosty język, ETR i dostępność poznawczą;
- badania użytkowników;
- technologie asystujące.

## 7. Warunki włączenia publikacji

Publikacja może wejść do puli kandydatów, jeżeli spełnia wszystkie poniższe warunki:

1. Dostępność jest jej głównym tematem, a nie jedynie wzmianką poboczną.
2. Pełna treść jest publicznie dostępna bez logowania i opłaty.
3. Dostępne są również materiały zewnętrzne konieczne do zrozumienia głównego wywodu.
4. Publikacja jest napisana po polsku.
5. Została opublikowana albo istotnie zaktualizowana od 1 stycznia 2024 r. do dnia zamrożenia puli kandydatów.
6. Zawiera co najmniej pięć materialnych twierdzeń możliwych do wyodrębnienia bez oceniania ich prawdziwości.
7. Jest możliwe zapisanie dokładnego adresu, daty dostępu i informacji pozwalającej rozpoznać analizowaną wersję.
8. Nie była wcześniej oceniana w projekcie według metodologii 0.1 ani 0.2.
9. Żaden z wykonujących przebiegi nie zna jej wcześniejszego wyniku przygotowanego w ramach tego projektu.
10. Autor publikacji nie jest osobą bezpośrednio tworzącą niniejszą metodologię ani wykonującą jej kalibrację.

Podczas sprawdzania warunków włączenia wolno przeczytać tytuł, metadane, wprowadzenie, strukturę i tyle treści, ile jest konieczne do ustalenia zakresu oraz liczby twierdzeń. Nie wolno na tym etapie weryfikować poprawności twierdzeń ani przewidywać werdyktu.

## 8. Warunki wyłączenia

Publikację wyłącza się z puli, jeżeli:

- pełna treść lub materiał centralny jest niedostępny;
- tekst jest krótkim ogłoszeniem, zapowiedzią albo wiadomością bez wystarczającej argumentacji;
- stanowi kopię lub nieznacznie zmienioną wersję innego kandydata;
- nie można ustalić autora, źródła albo analizowanej wersji w stopniu wystarczającym do porównania;
- została już oceniona lub szczegółowo omówiona w ramach projektu;
- osoba wybierająca zna oczekiwany wynik i wybiera tekst właśnie z tego powodu;
- pojawia się konflikt interesów, którego nie da się rozsądnie ograniczyć;
- nie spełnia któregokolwiek warunku włączenia.

Każde wyłączenie musi mieć zapisany krótki, obiektywny powód. Nie wolno wpisywać jako powodu przewidywanej nierzetelności, wysokiej jakości albo interesującego werdyktu.

## 9. Tworzenie puli kandydatów

Przed wyborem korpusu tworzy się rejestr co najmniej 24 kwalifikujących się kandydatów:

- co najmniej 6 kandydatów technicznych lub normatywnych;
- co najmniej 6 kandydatów prawnych lub dotyczących zgodności;
- co najmniej 6 kandydatów komercyjnych lub praktycznych;
- co najmniej 3 kandydatów opartych na badaniach albo doświadczeniu użytkowników;
- co najmniej 3 kandydatów popularnych, opiniotwórczych, instytucjonalnych albo mieszanych.

Kandydatów wyszukuje się za pomocą wcześniej zapisanych zapytań i źródeł, na przykład:

- wyszukiwarki internetowej;
- kanałów RSS i archiwów serwisów poświęconych dostępności;
- serwisów instytucji publicznych;
- serwisów organizacji społecznych i eksperckich;
- stron firm oferujących usługi związane z dostępnością.

Dla każdego wyszukiwania zapisuje się:

- datę i czas;
- dokładne zapytanie albo adres źródła;
- kolejność znalezionych wyników;
- decyzję o włączeniu lub wyłączeniu;
- powód wyłączenia.

Podczas tworzenia puli nie zapisuje się przewidywanego werdyktu ani oceny jakości.

## 10. Wybór ośmiu publikacji

Po zamknięciu puli wybór jest deterministyczny, czyli możliwy do powtórzenia bez uznaniowej decyzji.

Dla każdego kwalifikującego się kandydata oblicza się wartość SHA-256 z połączenia:

`ocena-0.2-korpus-2026-08-21|` oraz kanonicznego adresu publikacji.

W każdej kategorii kandydatów porządkuje się rosnąco według uzyskanej wartości. Wybiera się pierwszych kandydatów aż do wypełnienia limitu kategorii i wszystkich wymagań różnorodności.

Jeżeli kandydat narusza limit autora, miejsca publikacji albo inny warunek różnorodności, pomija się go i wybiera następną pozycję. Powód pominięcia zapisuje się w rejestrze.

Pierwszy niewybrany, kwalifikujący się kandydat w każdej kategorii zostaje kandydatem rezerwowym.

## 11. Zamrożenie korpusu

Przed rozpoczęciem ocen należy opublikować osobny rejestr korpusu zawierający:

- identyfikator przypadku;
- tytuł;
- autora lub zespół;
- miejsce publikacji;
- kanoniczny URL;
- datę publikacji albo aktualizacji;
- kategorię główną;
- znaną wersję lub datę i czas pobrania;
- skrót materiału, jeżeli można go legalnie i technicznie obliczyć;
- kolejność oceny;
- kandydata rezerwowego dla każdej kategorii.

Rejestr nie może zawierać:

- przewidywanego werdyktu;
- przewidywanych ocen;
- listy spodziewanych błędów;
- wcześniejszych analiz publikacji.

Commit zawierający protokół i ostateczny rejestr korpusu stanowi identyfikator zamrożenia serii. Wszystkie przebiegi muszą wskazywać ten identyfikator.

Po zamrożeniu nie wolno wymieniać publikacji dlatego, że pierwszy wynik jest zaskakujący, niewygodny albo trudny do porównania.

## 12. Kolejność ocen

Kolejność ośmiu przypadków ustala się przed rozpoczęciem pierwszego przebiegu.

Do ustalenia kolejności stosuje się rosnący porządek wartości SHA-256 obliczonej z:

`ocena-0.2-kolejnosc-2026-08-21|` oraz kanonicznego adresu publikacji.

Kolejności nie wolno zmieniać na podstawie uzyskiwanych wyników.

## 13. Wersja ocenianego materiału

Oba przebiegi muszą oceniać tę samą wersję publikacji i tych samych materiałów centralnych.

Dla każdego materiału zapisuje się dane wymagane przez metodologię 0.2-draft. Jeżeli nie istnieje niezmienny identyfikator, zapisuje się co najmniej:

- dokładny URL;
- datę i czas pobrania;
- deklarowaną datę publikacji albo aktualizacji;
- skrót pobranej treści, jeżeli jest dostępny;
- informację o braku niezmiennej wersji.

Oba przebiegi należy rozpocząć możliwie blisko siebie, najlepiej w ciągu 72 godzin.

Jeżeli centralna treść zmieni się pomiędzy przebiegami, ocen nie przedstawia się jako ścisłej pary. Należy ponownie wykonać oba przebiegi na tej samej wersji albo oznaczyć przypadek jako nieporównywalny.

## 14. Zasady niezależnych przebiegów

Dla każdego przypadku przygotowuje się dwa polecenia różniące się wyłącznie:

- identyfikatorem przebiegu;
- techniczną informacją konieczną do rozróżnienia plików.

Każdy przebieg:

- rozpoczyna się w nowym czacie;
- nie otrzymuje wyniku, wyciągu ani raportu drugiego przebiegu;
- nie korzysta z wcześniejszych analiz tej publikacji;
- nie korzysta z wyników innych przypadków do zmieniania punktacji;
- używa zamrożonej metodologii, protokołu i wersji materiału;
- zapisuje znane informacje o modelu, ustawieniach, narzędziach, pamięci i dostępie do projektu;
- tworzy oraz waliduje pełny wynik i wyciąg kalibracyjny.

Wykonanie dwóch przebiegów przez różne systemy AI jest dopuszczalne wyłącznie jako osobno oznaczony test między systemami. Nie zastępuje podstawowej pary w tej serii.

## 15. Przerwanie i ponowienie przebiegu

Przebieg przerwany z powodu limitu, błędu narzędzia, braku walidatora albo innej awarii nie jest ukończonym wynikiem.

Należy:

1. zachować informację o nieudanej próbie;
2. nie poprawiać jej częściowych ocen;
3. rozpocząć nowy przebieg w nowym czacie;
4. nadać mu nowy identyfikator wskazujący ponowienie;
5. zachować to samo polecenie, metodologię, protokół i materiał.

Ponowienia technicznego nie traktuje się jako dodatkowej niezależnej oceny.

## 16. Zastępowanie publikacji

Publikację wolno zastąpić kandydatem rezerwowym wyłącznie wtedy, gdy przed ukończeniem pierwszego przebiegu:

- treść została usunięta;
- przestała być publicznie dostępna;
- centralny materiał stał się niedostępny;
- wykryto niespełnienie obiektywnego warunku włączenia;
- nie da się zamrozić wersji w stopniu wystarczającym do porównania.

Nie wolno zastępować publikacji z powodu:

- przewidywanego albo otrzymanego werdyktu;
- trudności merytorycznej;
- dużej liczby twierdzeń;
- niezgodności obu przebiegów;
- niezadowalającego wyniku całej serii.

Każde zastąpienie wymaga zapisania daty, przyczyny i użytego kandydata rezerwowego.

## 17. Reguła zatrzymania

Seria kończy się po uzyskaniu dwóch ukończonych, porównywalnych przebiegów dla wszystkich ośmiu wybranych przypadków.

Nie wolno:

- zakończyć serii wcześniej dlatego, że wyniki wyglądają dobrze albo źle;
- dodawać publikacji w celu poprawienia zgodności;
- usuwać przypadku po poznaniu jego wyniku;
- zmieniać metodologii, kotwic, protokołu lub słownika wartości podczas serii.

Podejrzenia dotyczące wad metodologii zapisuje się oddzielnie i rozpatruje dopiero po zakończeniu wszystkich przypadków.

## 18. Porównanie wyników

Po zakończeniu całej serii porównuje się wyniki zgodnie z metodologią 0.2-draft, w tym:

- dokładną zgodność ocen A–L;
- zgodność w granicy jednego punktu;
- średnią bezwzględną różnicę;
- kierunek różnicy drugiego przebiegu względem pierwszego;
- zgodność werdyktów;
- zgodność klasyfikacji problemów po ich dopasowaniu;
- pokrycie wspólnej mapy twierdzeń;
- rozbieżności dotyczące wartości `nd`.

Wyników nie uśrednia się do jednego wyniku publikacji i nie poprawia się ich wstecz.

## 19. Jawność i przechowywanie

W publicznym repozytorium można przechowywać:

- protokół;
- rejestr kandydatów i obiektywne powody wyłączeń;
- zamrożony rejestr wybranego korpusu;
- ogólne wyniki kalibracji;
- wnioski dotyczące rozwoju metodologii.

W publicznym repozytorium nie należy przechowywać:

- pełnych kopii chronionych publikacji;
- nieukończonych raportów roboczych;
- materiałów wymagających poufności;
- danych dostępowych;
- informacji o miejscu przechowywania materiałów niepublicznych.

## 20. Zmiany protokołu

Po zamrożeniu korpusu protokołu nie wolno zmieniać podczas serii.

Jeżeli zmiana okaże się konieczna:

1. należy zakończyć albo formalnie unieważnić bieżącą serię;
2. zachować dotychczasowe dane bez przerabiania;
3. opisać przyczynę zmiany;
4. utworzyć nową wersję protokołu;
5. zamrozić nowy korpus albo jawnie wskazać zasady jego migracji;
6. rozpocząć nową serię.

Błędu protokołu nie naprawia się po cichu ani wstecz.

## 21. Co następuje po serii

Dopiero po zamknięciu wszystkich szesnastu przebiegów wolno:

- analizować systematyczne rozbieżności;
- proponować zmiany kotwic i reguł werdyktu;
- oceniać, które elementy metodologii są niejednoznaczne;
- przygotować kolejną wersję projektu;
- zaplanować oddzielny test przenośności między systemami AI;
- zdecydować, jakiego dodatkowego sprawdzenia wymaga metodologia przed uznaniem jej za stabilną.

Wyniki tej serii nie mogą same w sobie dowieść pełnej poprawności ani bezstronności metodologii.
