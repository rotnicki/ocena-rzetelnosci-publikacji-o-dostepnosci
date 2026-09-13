# Pilotaż projektu 0.3 — ogólne wnioski

**Data:** 13 września 2026 r.  
**Status:** wynik pilota projektu; nie jest zatwierdzeniem ani wydaniem 0.3  
**Zakres wykonanych prac:** 1 polski przypadek diagnostyczny i 2 pomocnicze testy międzyjęzykowe w języku angielskim; 6 odizolowanych przebiegów A/B

Pełne analizy przypadków są przechowywane poza repozytorium publicznym. Ten dokument zawiera wyłącznie zagregowane informacje potrzebne do oceny działania metodologii.

## Korekta opisu zakresu

Pierwotne podsumowanie zbyt szeroko przedstawiało trzy publikacje jako jeden równorzędny pilotaż. Polski artykuł pozostał przypadkiem diagnostycznym ujawniającym problem ustalania odbiorców. Digidop i WebAIM należy traktować jako pomocnicze testy angielskie, a nie jako dwa główne przypadki polskiego pilota.

Dobór dwóch tekstów angielskich był zmianą zakresu dokonaną bez wcześniejszego zatwierdzenia właściciela projektu. Ogranicza to możliwość oceny polskiego języka, żargonu i wymiarów G, H oraz L. Nie usunięto, nie przeliczono ani nie poprawiono wstecz żadnego zakończonego wyniku A/B.

## Kontrola techniczna

Standard, kotwice, szablony, schematy, walidator i pakiet umiejętności odpowiadają zatwierdzonej propozycji 0.3. Kontrola wykryła jedną niespójność egzekwowania istniejącej reguły: H i L mogły przyjąć `nd` mimo oznaczenia terminologii jako blokującej. Schematy, walidator i test regresyjny poprawiono bez zmiany znaczenia metodologii.

Po poprawce testy walidatora, zgodność kopii referencyjnych, kontrola struktury pakietu i odtwarzalna budowa ZIP przechodzą. Historyczne wersje 0.1 i 0.2 nie zostały zmienione.

## Wyniki zagregowane całego wykonanego zestawu

Poniższe liczby opisują jeden przypadek polski i dwa testy angielskie łącznie. Nie są wynikiem trzytekstowego polskiego pilota i nie potwierdzają jeszcze stabilności G, H oraz L w polskich warunkach komunikacyjnych.

| Miara | Wynik |
|---|---:|
| Zgodność werdyktu | 3/3 par (100%) |
| Zgodność korekty kontrfaktycznej i bezpiecznego polecenia | 3/3 (100%) |
| Dokładna zgodność A–L, wraz ze wspólnym `nd` | 29/36 (80,6%) |
| Zgodność A–L w granicy jednego punktu | 36/36 (100%) |
| Średnia bezwzględna różnica ocen liczbowych | 0,20 |
| Rozbieżności `nd` | 0 |
| Pokrycie map wspólnym znaczeniem | A: 87,1%; B: 86,5% |
| Dokładna zgodność wyniku w porównywalnych parach twierdzeń 1:1 | 44/60 (73,3%) |
| Wspólne problemy duże: zgodność severity / centralności / ryzyka | 100% / 80% / 80% |

## Co działa

- decyzja końcowa, test korekty i ostrożność polecenia są stabilne;
- wszystkie różnice A–L mieszczą się w jednym punkcie;
- stosowanie `nd` i wymiar K są w tej małej próbie powtarzalne;
- testy problemów dużych oraz uzasadnienia grupowania ułatwiają porównanie;
- rozdzielenie poprawności historycznej od bieżącej użyteczności zapobiega automatycznemu karaniu starszych danych;
- samowystarczalny pakiet umożliwia wykonanie i walidację oceny bez pobierania zasad z repozytorium.

## Co wymaga dalszej pracy

- atomizacja i wierne zachowanie zakresu parafrazy nadal są niestabilne;
- zgodność profilu może ukryć sprzeczne rozstrzygnięcie pojedynczego przykładu;
- ekstrakcja liczb, progów i przykładów kodu wymaga audytowalnego śladu;
- grupowanie zmienia surową liczbę i widoczną wagę problemów;
- granice D i G oraz podział odpowiedzialności C/D/H wymagają dodatkowych kotwic;
- test centralności potrzebuje jednoznacznego obiektu kontrfaktycznego;
- brak wspólnego schematu raportu porównawczego utrudnia automatyczne agregowanie;
- ograniczenie H/L dla blokującego żargonu nie zostało uruchomione w tym korpusie i wymaga osobnego testu regresyjnego.
- ustalanie odbiorców wymaga dowodowego profilu miejsca publikacji i zakazu wnioskowania o specjalistycznym odbiorcy wyłącznie z trudności tekstu.

Powyższe punkty są wnioskami z pilota. Zmiany wpływające na znaczenie metodologii nie zostały wprowadzone i wymagają osobnego zatwierdzenia.

## Ograniczenia

To mały zestaw techniczno-diagnostyczny wykonany przez jeden typ systemu AI. Zawiera tylko jeden polski przypadek, dlatego właściwy polski pilotaż pozostaje do wykonania. Wszystkie trzy przypadki zakończyły się tym samym rodzajem werdyktu, więc zestaw nie sprawdził granic między czterema kategoriami werdyktu. Nie dowodzi jeszcze trafności metody, przenośności między systemami ani stabilności na szerszym korpusie. Dynamiczne strony nie miały wspólnej zapisanej migawki, a w jednym przypadku nie były dostępne dane surowe i pełna dokumentacja metody.
