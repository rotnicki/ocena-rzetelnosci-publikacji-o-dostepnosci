# Pilotaż projektu 0.3 — ogólne wnioski

**Data:** 13 września 2026 r.  
**Status:** wynik pilota projektu; nie jest zatwierdzeniem ani wydaniem 0.3  
**Zakres:** 3 publikacje różnego rodzaju, 6 odizolowanych przebiegów A/B

Pełne analizy przypadków są przechowywane poza repozytorium publicznym. Ten dokument zawiera wyłącznie zagregowane informacje potrzebne do oceny działania metodologii.

## Kontrola techniczna

Standard, kotwice, szablony, schematy, walidator i pakiet umiejętności odpowiadają zatwierdzonej propozycji 0.3. Kontrola wykryła jedną niespójność egzekwowania istniejącej reguły: H i L mogły przyjąć `nd` mimo oznaczenia terminologii jako blokującej. Schematy, walidator i test regresyjny poprawiono bez zmiany znaczenia metodologii.

Po poprawce testy walidatora, zgodność kopii referencyjnych, kontrola struktury pakietu i odtwarzalna budowa ZIP przechodzą. Historyczne wersje 0.1 i 0.2 nie zostały zmienione.

## Wyniki zagregowane

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

Powyższe punkty są wnioskami z pilota. Zmiany wpływające na znaczenie metodologii nie zostały wprowadzone i wymagają osobnego zatwierdzenia.

## Ograniczenia

To mały test wykonany przez jeden typ systemu AI. Nie dowodzi jeszcze trafności metody, przenośności między systemami ani stabilności na szerszym korpusie. Dynamiczne strony nie miały wspólnej zapisanej migawki, a w jednym przypadku nie były dostępne dane surowe i pełna dokumentacja metody.
