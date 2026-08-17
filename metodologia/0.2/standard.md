# Standard oceny rzetelności publikacji o dostępności — zmiany 0.2

**Wersja:** 0.2 — projekt do kalibracji  
**Data:** 18 sierpnia 2026 r.  
**Podstawa:** standard 0.1 zamrożony w identyfikatorze `5f775917f1f8cde33f876ef1875cb617a5f5fd21`  
**Status:** wersja eksperymentalna; nie zastępuje domyślnie wersji 0.1

## 1. Sposób stosowania

Projekt 0.2 jest nakładką na pełny standard 0.1. Przed oceną należy przeczytać oba dokumenty. Jeżeli reguły się różnią, pierwszeństwo ma ten dokument oraz plik `kotwice-0.2.md`.

Nie wolno:

- zmieniać wyników wykonanych według 0.1 tak, jakby powstały według 0.2;
- użyć 0.2 bez jawnego zapisania jej wersji i identyfikatora;
- poprawiać reguł w trakcie pojedynczej analizy lub serii;
- nazywać projektu 0.2 metodologią zwalidowaną przed kolejną niezależną próbą.

## 2. Rozstrzygnięcia wprowadzone w projekcie 0.2

Projekt 0.2:

1. zachowuje dwanaście wymiarów A–L i profil zamiast średniej;
2. nie wprowadza wag ani sumy wyznaczającej werdykt;
3. dopuszcza wartość `nd` wyłącznie przy rzeczywistym braku zastosowania wymiaru;
4. dodaje kotwice 0–4 osobne dla każdego wymiaru;
5. rozdziela znaczenie problemu, jego centralność, ryzyko zastosowania i pewność;
6. wprowadza sekwencję ustalania werdyktu i test korekty kontrfaktycznej;
7. wymaga wersjonowania centralnych materiałów zewnętrznych;
8. wymaga opisania środowiska oceniającego;
9. rozdziela pewność werdyktu od pokrycia źródłowego;
10. wymaga krótkiego wyciągu ustrukturyzowanego przy analizie kalibracyjnej.

## 3. Zamrożenie obiektu i środowiska oceny

### 3.1. Materiały

Każdy materiał należy przypisać do jednej roli:

- `tresc_glowna` — sama oceniana publikacja;
- `material_centralny_zewnetrzny` — załącznik, graf, film, kod, raport lub repozytorium, bez którego nie da się ocenić głównego wywodu;
- `material_dodatkowy` — materiał pomocniczy;
- `material_wylaczony` — element świadomie wyłączony z punktacji.

Dla treści głównej i każdego materiału centralnego trzeba zapisać:

- dokładny URL;
- datę i czas dostępu, jeżeli są dostępne;
- datę publikacji lub aktualizacji;
- commit, wydanie, numer wersji, identyfikator dokumentu albo migawkę, jeżeli istnieje;
- informację, czy identyfikator jest niezmienny;
- zakres wykorzystany w analizie.

Jeżeli dwa przebiegi użyły różnych wersji materiału centralnego, nie wolno przedstawiać ich jako ścisłego powtórzenia tego samego przypadku. Wynik można pokazać oddzielnie jako analizę wrażliwości na wersję.

### 3.2. Środowisko oceniające

Należy zapisać tyle z poniższych danych, ile rzeczywiście jest dostępne:

- rodzaj oceniającego: człowiek, AI albo zespół;
- nazwę osoby, modelu lub zespołu;
- wersję albo migawkę modelu;
- ustawienie poziomu rozumowania;
- dostępne narzędzia;
- datę analizy;
- dostęp do pamięci wcześniejszych rozmów;
- dostęp do projektu lub kontekstu organizacyjnego;
- dostęp do prywatnego laboratorium;
- inne warunki mogące wpływać na odtworzenie próby.

Nie wolno zgadywać niewidocznej nazwy modelu ani parametrów. Należy użyć wartości `not_available` i opisać ograniczenie.

## 4. Zakres analizy i mapa twierdzeń

### 4.1. Liczba twierdzeń

Pełna analiza nie wymaga osobnego wpisu dla każdego zdania. Mapa musi jednak obejmować:

- wszystkie twierdzenia kluczowe;
- wszystkie zalecenia mogące wpływać na działanie odbiorcy;
- twierdzenia prawne, normatywne i techniczne, na których opiera się wniosek;
- twierdzenia pomocnicze, których fałszywość zmieniałaby ocenę przesłanki albo przykładu;
- reprezentatywne twierdzenia dodatkowe potrzebne do oceny powtarzalnego wzorca błędu.

Należy podać liczbę wpisów w mapie. Sama liczba wykrytych problemów nie jest wynikiem jakości i nie może zastępować oceny ich znaczenia.

### 4.2. Dopasowanie twierdzeń w kalibracji

W zamkniętym pakiecie kalibracyjnym należy przed rozpoczęciem ocen przypisać wspólne identyfikatory `claim_match_id` do uzgodnionej listy twierdzeń. Oceniający mogą dodać nowe twierdzenia, ale nie mogą widzieć cudzych wyników.

Jeżeli nie przygotowano listy wspólnej, dopasowanie twierdzeń wykonuje się dopiero po zamknięciu ocen. Trzeba wtedy zachować lokalny identyfikator twierdzenia i osobno zapisać identyfikator dopasowania.

## 5. Stosowalność wymiaru i wartość `nd`

Domyślnie każdy wymiar A–L należy ocenić liczbowo. Wartość `nd` oznacza „nie dotyczy”, a nie „brak danych”, „niska jakość” ani „oceniający nie potrafi rozstrzygnąć”.

`nd` wolno zastosować tylko wtedy, gdy:

1. publikacja nie zawiera twierdzeń, zaleceń ani implikacji należących do danego wymiaru;
2. brak tego zakresu jest zgodny z rodzajem i celem publikacji;
3. ocena liczbowa wymagałaby karania albo nagradzania tekstu za treści, których zasadnie nie podejmuje;
4. raport zawiera jednozdaniowe uzasadnienie.

`nd` nie wolno zastosować, gdy:

- materiał składa twierdzenie, ale nie da się go zweryfikować;
- potrzebne źródło jest niedostępne;
- tekst pomija konieczny wyjątek lub grupę użytkowników;
- zalecenie jest niepełne albo niebezpieczne;
- oceniającemu brakuje kompetencji;
- popularny charakter publikacji służy jako wymówka dla błędu.

W porównaniu ocen należy podać liczbę wymiarów ocenionych liczbowo. Parę z `nd` wyłącza się z obliczenia różnicy punktowej, ale raportuje jako rozbieżność stosowalności.

## 6. Cztery niezależne cechy problemu

Każdy problem otrzymuje znaczenie i pewność. Każdy problem duży lub krytyczny otrzymuje dodatkowo centralność oraz ryzyko zastosowania.

### 6.1. Znaczenie

- `krytyczne` — istnieje wiarygodne i bezpośrednie ryzyko poważnego naruszenia prawa lub praw osoby, poważnej bariery, znacznego wykluczenia albo decyzji o dotkliwych skutkach; ewentualnie główne rozwiązanie jest całkowicie nieskuteczne, a typowy odbiorca prawdopodobnie je zastosuje;
- `duze` — problem istotnie zmienia rozumienie albo praktyczne zastosowanie rdzenia lub ważnego wsparcia, lecz nie osiąga progu bezpośredniej poważnej szkody;
- `srednie` — wymaga korekty i może zmienić część interpretacji lub działania, ale nie podważa zasadniczej wartości materiału;
- `male` — lokalna nieścisłość, brak albo problem redakcyjny o ograniczonych konsekwencjach.

Próg `krytyczne` ma być stosowany oszczędnie. Błędna składnia kopiowalnego przykładu kodu nie jest automatycznie krytyczna. Zwykle jest problemem dużym albo średnim. Staje się krytyczna dopiero wtedy, gdy prawdopodobne użycie przykładu bezpośrednio tworzy poważną barierę, naruszenie lub szkodę i brak prostego zabezpieczenia ograniczającego to ryzyko.

### 6.2. Centralność

- `rdzen` — problem dotyczy głównej tezy, podstawowego zalecenia, deklarowanego celu albo rezultatu, po który odbiorca sięga do publikacji;
- `istotne_wsparcie` — problem dotyczy ważnej przesłanki, metody, przykładu lub części argumentacji, lecz główna teza może przetrwać jego korektę;
- `element_poboczny` — problem dotyczy dygresji, lokalnego przykładu albo informacji, której usunięcie nie zmienia głównego przekazu.

Centralność ocenia się względem konkretnej publikacji, a nie ogólnej ważności tematu.

### 6.3. Ryzyko zastosowania

- `wysokie` — typowy odbiorca może rozsądnie zastosować informację lub zalecenie, a błąd prawdopodobnie spowoduje poważną barierę, naruszenie albo istotnie błędną decyzję;
- `srednie` — zastosowanie może spowodować zauważalny błąd lub nieskuteczne działanie, ale skutek jest ograniczony, odwracalny albo zależny od dodatkowych warunków;
- `niskie` — problem ma głównie znaczenie informacyjne lub redakcyjne i mało prawdopodobne jest, aby sam doprowadził do istotnie błędnego działania.

### 6.4. Pewność

Pewność opisuje siłę podstaw zaklasyfikowania problemu, a nie jego dotkliwość. Problem o niskiej pewności nie może samodzielnie przesądzić o werdykcie `nierzetelny`.

## 7. Punktacja A–L

Przed nadaniem ocen należy przeczytać `kotwice-0.2.md`. Wspólna skala 0–4 ze standardu 0.1 pozostaje tylko ogólnym opisem; o granicy między poziomami rozstrzygają kotwice właściwego wymiaru.

Dla każdego wymiaru trzeba:

1. wskazać dowody z publikacji;
2. porównać je z kotwicą proponowanego poziomu i poziomów sąsiednich;
3. zapisać krótkie uzasadnienie;
4. podać pewność;
5. przy ocenie 0, 1 albo 4 wskazać cechę przekraczającą granicę skali.

Nie wolno:

- ustalać oceny z liczby problemów;
- mechanicznie obniżać kilku wymiarów za ten sam błąd bez opisania odmiennego skutku w każdym z nich;
- podwyższać punktów za atrakcyjny styl w wymiarach poprawności;
- wyrównywać ocen do poprzedniego artykułu w serii;
- korygować systematycznej surowości w trakcie zamrożonej serii.

Po serii wolno obliczyć kierunek różnic i wykryć przesunięcie surowości, ale nie wolno retroaktywnie normalizować wyników bez jawnej procedury migracji.

## 8. Sekwencja ustalania werdyktu

### Krok 1. Możliwość rozstrzygnięcia

Zastosować `nie_mozna_rozstrzygnac`, gdy brak pełnej treści, wersji centralnego materiału albo wystarczających dowodów uniemożliwia ocenę rdzenia publikacji. Nie stosować tego werdyktu tylko dlatego, że część twierdzeń pozostaje nierozstrzygnięta.

### Krok 2. Wskazanie rdzenia

Przed wyborem pozostałych werdyktów zapisać:

- główną tezę;
- podstawowe zastosowanie praktyczne;
- problemy oznaczone `rdzen`;
- problemy o `wysokim` ryzyku zastosowania.

W publikacji mieszanej trzeba osobno ustalić rolę tekstu i centralnego materiału zewnętrznego. Uczciwe ostrzeżenie, że mapa, kod, prototyp albo raport jest eksperymentalny, poprawia przejrzystość epistemiczną, ale nie usuwa jego błędów. Jeżeli publikacja zachęca do używania, kopiowania albo podejmowania decyzji na podstawie tego materiału, jego zasadnicza wadliwość może podważyć rdzeń całej publikacji. Jeżeli materiał jest pokazany wyłącznie jako demonstracja procesu, ma wyraźny zakaz praktycznego użycia i nie stanowi podstawy zaleceń, jego wpływ na werdykt może być mniejszy.

### Krok 3. Test korekty kontrfaktycznej

Zadać pytanie: „Co pozostałoby z publikacji po uczciwym poprawieniu potwierdzonych problemów?”

- **Korekta ograniczona:** główna teza, podstawowa metoda lub zasadnicza użyteczność pozostaje; wystarczą wskazane poprawki, doprecyzowania albo źródła.
- **Korekta strukturalna:** trzeba wycofać lub odwrócić główną tezę, zastąpić podstawową metodę, usunąć główne zalecenie albo zasadniczo zmienić deklarowane zastosowanie tekstu.

Korekta ograniczona wskazuje zwykle na `rzetelny_z_istotnymi_zastrzezeniami`. Korekta strukturalna jest mocną podstawą `nierzetelny`.

### Krok 4. Zastosowanie definicji

#### `rzetelny`

Zastosować, gdy główne twierdzenia i zalecenia są zgodne lub zasadniczo zgodne, nie ma problemów dużych ani krytycznych, pokrycie źródłowe jest wystarczające, a materiał można bezpiecznie wykorzystać zgodnie z celem.

#### `rzetelny_z_niewielkimi_zastrzezeniami`

Zastosować, gdy nie ma problemów dużych ani krytycznych, a problemy średnie są ograniczone i nie zmieniają głównego wniosku ani bezpiecznego działania. Poprawki mają charakter lokalny.

#### `rzetelny_z_istotnymi_zastrzezeniami`

Zastosować, gdy występuje co najmniej jeden problem duży albo kilka powiązanych problemów średnich, ale po korekcie ograniczonej pozostaje wartościowy rdzeń. Materiał wolno polecić tylko z nazwanymi korektami albo źródłami uzupełniającymi.

#### `nierzetelny`

Zastosować, gdy spełniony jest co najmniej jeden z warunków:

1. potwierdzony z wysoką lub średnią pewnością problem w rdzeniu unieważnia główną tezę albo podstawowe zastosowanie;
2. korekta wymaga zmiany strukturalnej;
3. podstawowe zalecenie ma wysokie ryzyko zastosowania i nie staje się bezpieczne po prostym doprecyzowaniu;
4. kilka problemów dużych łącznie podważa rdzeń, mimo że żaden pojedynczo nie wystarcza;
5. centralna obietnica publikacji pozostaje niespełniona w sposób, który typowego odbiorcę prowadzi do istotnie błędnej decyzji.

Nie wolno zastosować `nierzetelny` wyłącznie dlatego, że suma ocen jest niska, lista problemów jest długa albo występuje jeden łatwo naprawialny błąd poboczny.

### Krok 5. Kontrola spójności

- `rzetelny` oraz `rzetelny_z_niewielkimi_zastrzezeniami` nie mogą współistnieć z problemem dużym lub krytycznym;
- `nierzetelny` musi wskazywać identyfikatory problemów przesądzających, ich centralność, ryzyko oraz wynik testu korekty;
- oceny A–L nie wyznaczają werdyktu, ale rażąca sprzeczność profilu z werdyktem wymaga jawnego wyjaśnienia;
- brak problemu krytycznego nie wyklucza werdyktu `nierzetelny`, jeżeli kilka dużych problemów podważa rdzeń;
- problem krytyczny o charakterze pobocznym wymaga osobnego uzasadnienia wpływu na możliwość polecenia całej publikacji.

## 9. Pokrycie źródłowe i pewność werdyktu

Pokrycie źródłowe należy oznaczyć osobno:

- `pelne` — wszystkie twierdzenia kluczowe i ważne sprawdzono w odpowiednich źródłach;
- `wystarczajace` — sprawdzono cały rdzeń i zalecenia, a luki dotyczą elementów pomocniczych;
- `czesciowe` — pozostają luki mogące wpłynąć na część ocen, ale nie uniemożliwiają ostrożnego werdyktu;
- `niewystarczajace` — luki dotyczą rdzenia i zwykle prowadzą do `nie_mozna_rozstrzygnac`.

Pewność werdyktu pozostaje `wysoka`, `srednia` albo `niska`. Należy ją uzasadnić dostępnością materiału, jakością źródeł, stopniem interpretacji i zakresem nierozstrzygniętych twierdzeń.

## 10. Dane ustrukturyzowane

Pełny `wynik.json` musi być zgodny z `wynik-0.2.schema.json`. Wartości maszynowe stosują małe litery, zapis bez polskich znaków i `snake_case`. Raport dla człowieka używa naturalnych polskich etykiet.

W analizie kalibracyjnej należy dodatkowo utworzyć `wyciag-kalibracyjny.json` zgodny z osobnym schematem. Wyciąg nie zastępuje pełnego raportu ani pełnego wyniku.

Jeżeli rezultat jest przekazywany w czacie, wyciąg należy przedstawić w jednym kompletnym bloku kodu JSON. Nie należy wymagać ręcznego kopiowania wielostronicowego raportu do porównania punktacji.

## 11. Porównanie przebiegów

Dla dwóch ocen tego samego, zamrożonego korpusu należy raportować co najmniej:

- zgodność dokładną ocen A–L;
- zgodność w granicy jednego punktu;
- średnią bezwzględną różnicę;
- średni kierunek różnicy drugiego przebiegu względem pierwszego;
- wyniki osobno dla każdego wymiaru;
- zgodność werdyktów;
- zgodność klasyfikacji znaczenia, centralności i ryzyka po dopasowaniu problemów;
- pokrycie wspólnej mapy twierdzeń;
- rozbieżności stosowalności `nd`.

Ważoną kappę Cohena można podać pomocniczo dla dwóch oceniających, jeżeli liczba przypadków i rozkład ocen pozwalają na sensowną interpretację. Trzeba ujawnić rodzaj wag, liczbę obserwacji i sposób traktowania `nd`. Przy większej liczbie oceniających można rozważyć alfę Krippendorffa. Żadna pojedyncza miara nie zastępuje analizy rozbieżności.

Systematyczne przesunięcie surowości należy opisać, ale nie wolno automatycznie odejmować ani dodawać punktów do zamkniętej serii.

## 12. Kontrola jakości przed zamknięciem analizy

Należy potwierdzić:

1. pełna treść i wszystkie materiały centralne mają zapisane wersje;
2. neutralne streszczenie powstało przed oceną;
3. mapa obejmuje rdzeń i wszystkie zalecenia wpływające na działanie;
4. każde źródło faktycznie odczytano w zakresie wspierającym wniosek;
5. każde `nd` ma uzasadnienie i nie ukrywa braku danych;
6. każda ocena A–L została porównana z kotwicami sąsiednimi;
7. każdy problem duży i krytyczny ma centralność oraz ryzyko zastosowania;
8. werdykt przeszedł test korekty kontrfaktycznej;
9. pewność werdyktu i pokrycie źródłowe zapisano osobno;
10. JSON i wyciąg kalibracyjny przeszły walidację;
11. raport nie zawiera pełnej kopii chronionej publikacji bez podstawy;
12. wyniki nie zostały dostrojone do wcześniejszych przypadków.

## 13. Status projektu i następna próba

Projekt 0.2 należy sprawdzić na nowym, zróżnicowanym korpusie obejmującym więcej niż jednego autora. Co najmniej dwóch oceniających powinno pracować niezależnie, a jeden z nich powinien być człowiekiem posiadającym odpowiednią wiedzę o dostępności. Dopiero po tej próbie można zdecydować, czy usunąć oznaczenie „projekt” i uczynić 0.2 wersją domyślną.
