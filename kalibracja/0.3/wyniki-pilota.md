# Pilotaż projektu 0.3 — ogólne wnioski

**Data:** 13 września 2026 r.  
**Status:** wynik pilota projektu; nie jest zatwierdzeniem ani wydaniem 0.3  
**Zakres wykonanych prac:** wcześniejszy przypadek diagnostyczny i 2 pomocnicze testy angielskie oraz nowy podstawowy pilotaż 5 polskich publikacji; łącznie 16 odizolowanych przebiegów, przy czym oba zestawy są raportowane osobno

Pełne analizy przypadków są przechowywane poza repozytorium publicznym. Ten dokument zawiera wyłącznie zagregowane informacje potrzebne do oceny działania metodologii.

## Korekta opisu zakresu

Pierwotne podsumowanie zbyt szeroko przedstawiało trzy publikacje jako jeden równorzędny pilotaż. Polski artykuł pozostał przypadkiem diagnostycznym ujawniającym problem ustalania odbiorców. Digidop i WebAIM należy traktować jako pomocnicze testy angielskie, a nie jako dwa główne przypadki polskiego pilota.

Dobór dwóch tekstów angielskich był zmianą zakresu dokonaną bez wcześniejszego zatwierdzenia właściciela projektu. Ogranicza to możliwość oceny polskiego języka, żargonu i wymiarów G, H oraz L. Nie usunięto, nie przeliczono ani nie poprawiono wstecz żadnego zakończonego wyniku A/B.

## Kontrola techniczna

Standard, kotwice, szablony, schematy, walidator i pakiet umiejętności odpowiadają zatwierdzonej propozycji 0.3. Kontrola wykryła jedną niespójność egzekwowania istniejącej reguły: H i L mogły przyjąć `nd` mimo oznaczenia terminologii jako blokującej. Schematy, walidator i test regresyjny poprawiono bez zmiany znaczenia metodologii.

Po poprawce testy walidatora, zgodność kopii referencyjnych, kontrola struktury pakietu i odtwarzalna budowa ZIP przechodzą. Historyczne wersje 0.1 i 0.2 nie zostały zmienione.

## Wyniki zagregowane wcześniejszego zestawu diagnostycznego

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

To mały zestaw techniczno-diagnostyczny wykonany przez jeden typ systemu AI. Zawierał tylko jeden polski przypadek, dlatego sam nie mógł zastąpić właściwego polskiego pilotażu opisanego niżej. Wszystkie trzy przypadki zakończyły się tym samym rodzajem werdyktu, więc zestaw nie sprawdził granic między czterema kategoriami werdyktu. Nie dowodzi jeszcze trafności metody, przenośności między systemami ani stabilności na szerszym korpusie. Dynamiczne strony nie miały wspólnej zapisanej migawki, a w jednym przypadku nie były dostępne dane surowe i pełna dokumentacja metody.

## Nowy podstawowy pilotaż polski po zmianach M1–M14

Nowy pilotaż objął pięć polskojęzycznych publikacji z pięciu różnych miejsc publikacji: tekst ekspercki, popularyzatorski, techniczny, urzędowy oraz komercyjny. Dla każdej publikacji wykonano dwa odizolowane przebiegi A i B. Poniżej podano wyłącznie dane zbiorcze; pełne oceny pozostają w prywatnym laboratorium.

| Miara | Wynik |
|---|---:|
| Dokładna zgodność A–L | 48/60 (80,0%) |
| Zgodność A–L w granicy jednego punktu | 60/60 (100%) |
| Średnia bezwzględna różnica | 0,20 punktu |
| Zgodność werdyktu | 5/5 par (100%) |
| Twierdzenia z odpowiednikiem semantycznym po obu stronach | 330/364 (90,7%) |
| Dokładna zgodność wyniku twierdzeń w relacjach 1:1 | 78/126 (61,9%) |
| Problemy z odpowiednikiem semantycznym po obu stronach | 61/72 (84,7%) |
| Zgodność centralności / ryzyka wspólnych problemów | 77,8% / 77,8% |
| Rozbieżności `nd` | 0 |

### Co działa w projekcie 0.3

- profil miejsca, celu i głównych odbiorców był zgodny w każdej parze;
- wszystkie różnice A–L mieściły się w jednym punkcie;
- oceny E, I i L były identyczne we wszystkich pięciu parach;
- werdykt, zakres wymaganej korekty i ostrożność polecenia były zgodne w każdej parze;
- wspólny format porównania zapewnił jednokrotne pokrycie wszystkich twierdzeń i problemów;
- reguła ustalania H na podstawie istotnych grup odbiorców została zastosowana we wszystkich przebiegach.

### Co zawiodło albo pozostało słabe

- wymiar H był dokładnie zgodny tylko w 2 z 5 par; największą trudność stanowiły publikacje dla grup mieszanych;
- wiedza rzeczywiście potrzebna odbiorcy i pewność profilu były zgodne tylko w 2 z 5 par;
- liczba twierdzeń w jednym przebiegu wahała się od 23 do 57, co wskazuje na nadal niestabilną atomizację;
- liczba problemów wahała się od 5 do 10, a dokładna zgodność ich znaczenia była niższa niż zgodność ocen A–L;
- wszystkie 10 przebiegów zakończyło się jednym rodzajem werdyktu, dlatego pilotaż nie sprawdził rozróżniania wszystkich progów;
- nie wystąpiły `nd`, problem krytyczny ani werdykt o braku możliwości rozstrzygnięcia;
- grupowe L nie było zapisywane w dostatecznie jednolity sposób;
- walidator nie sprawdza jeszcze wszystkich zależności między wynikiem, wyciągiem i porównaniem, choć bieżącą serię zweryfikowano dodatkowymi kontrolami.

### Zmiany do rozważenia przed kandydatem wydawniczym

- dodać dokładniejsze przykłady atomizacji i grupowania problemów;
- doprecyzować granice H=2/3 i H=3/4 dla grup niespecjalistycznych i mieszanych;
- ujednolicić znaczenie oraz zapis oceny L według grup;
- doprecyzować poziomy pewności profilu odbiorców i wiedzy wymaganej od czytelnika;
- rozbudować walidator o kontrole zależności między wszystkimi plikami;
- przygotować osobny korpus sprawdzający pozostałe werdykty, `nd`, problem krytyczny i brak rozstrzygnięcia;
- sprawdzić przenośność metodologii na innych oceniających i systemach.

Powyższe punkty są wnioskami z pilota, a nie wdrożonymi zmianami zasad. Wersje 0.1 i 0.2 pozostały nietknięte. PR nr 8 nie został scalony i nie utworzono znacznika ani wydania 0.3.
