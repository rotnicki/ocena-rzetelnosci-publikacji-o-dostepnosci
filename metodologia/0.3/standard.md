# Standard oceny rzetelności publikacji o dostępności

**Wersja:** 0.3 — projekt roboczy  
**Data:** 8 września 2026 r.  
**Status:** wersja w przygotowaniu; nie jest jeszcze zamrożonym wydaniem  
**Przeznaczenie:** ocena artykułów, poradników, komentarzy, analiz, newsletterów i innych publikacji dotyczących dostępności, wykonywana przez człowieka albo system sztucznej inteligencji

## 1. Cel standardu

Celem standardu jest możliwie powtarzalna, porównywalna i sprawdzalna ocena publikacji poświęconych dostępności.

Standard ma ograniczać zależność wyniku od pierwszego wrażenia, stylu odpowiedzi modelu, reputacji autora i swobodnie dobranych kryteriów. Każda analiza powinna:

- obejmować pełną dostępną treść publikacji i jej centralne materiały;
- oddzielać neutralne odtworzenie stanowiska od jego oceny;
- wskazywać konkretne twierdzenia podlegające weryfikacji;
- korzystać przede wszystkim ze źródeł pierwotnych i autorytatywnych;
- odróżniać błąd od uproszczenia, opinii, doświadczenia i sporu interpretacyjnego;
- oceniać poprawność, dowody, rozumowanie, język, zrozumiałość i bezpieczeństwo praktyczne;
- przedstawiać podstawy pozwalające skontrolować wnioski;
- ujawniać ograniczenia, pokrycie źródłowe i poziom pewności.

Wersja 0.3 jest pełnym dokumentem. Do jej zastosowania nie trzeba czytać metodologii 0.1 ani 0.2. Wcześniejsze wersje pozostają odrębnymi, niezmiennymi punktami odniesienia.

## 2. Zakres i przedmiot oceny

Standard można stosować między innymi do:

- artykułów eksperckich i popularyzatorskich;
- poradników technicznych i prawnych;
- komentarzy do prawa, norm i standardów;
- materiałów szkoleniowych;
- wpisów blogowych i newsletterów;
- komunikatów instytucji;
- opisów usług i dobrych praktyk;
- badań i tekstów przedstawiających doświadczenia użytkowników;
- publikacji mieszanych, których centralną częścią jest kod, film, grafika, raport albo interaktywny artefakt.

Przedmiotem oceny jest konkretna publikacja w określonej wersji i kontekście. Standard nie służy do oceniania kompetencji, intencji, uczciwości ani osobowości autora.

## 3. Zasady podstawowe

### 3.1. Pełna treść przed oceną

Nie wolno wystawić oceny na podstawie tytułu, zajawki, fragmentu, wyniku wyszukiwania albo cudzego omówienia.

Jeżeli pełna treść albo centralny materiał są niedostępne, należy oznaczyć zakres jako częściowy. Nie wolno domyślać się brakującej zawartości.

### 3.2. Dwa przebiegi wewnątrz każdej analizy

Każda ocena obejmuje:

1. **przebieg interpretacyjny** — ustalenie celu, odbiorcy, toku wywodu, głównej tezy i najmocniejszej rozsądnej wersji twierdzeń, bez sprawdzania ich prawdziwości;
2. **przebieg krytyczny** — sprawdzenie twierdzeń, źródeł, rozumowania, języka, zrozumiałości i użyteczności.

Wyniki przebiegu krytycznego nie mogą przepisywać neutralnego streszczenia przygotowanego wcześniej.

Nie należy mylić tych dwóch przebiegów wewnętrznych z dwoma niezależnymi ocenami A i B wykonywanymi podczas kalibracji.

### 3.3. Życzliwa i wymagająca interpretacja

Należy przyjmować najmocniejsze rozsądne znaczenie zgodne z tekstem. Nie wolno tworzyć słabszej wersji stanowiska, aby łatwiej je skrytykować. Życzliwa interpretacja nie oznacza pomijania błędów, przemilczeń ani mylących uproszczeń.

### 3.4. Tekst, nie autor

Rozpoznawalność, stanowisko, organizacja i wcześniejsza reputacja autora nie mogą podnosić ani obniżać oceny. Informacje o autorze i wydawcy można wykorzystać tylko do ustalenia deklarowanego odbiorcy, celu, autorstwa i charakteru miejsca publikacji.

### 3.5. Dowód przed wnioskiem

Każde istotne zastrzeżenie powinno wskazywać:

1. co zawiera publikacja — krótkim cytatem albo wierną parafrazą;
2. jaki jest problem;
3. jakie źródło lub rozumowanie go potwierdza;
4. jaki może mieć skutek dla odbiorcy;
5. jaką poprawkę należałoby wprowadzić.

### 3.6. Brak karania za brak ideału

Publikacja nie musi być wyczerpującą monografią. Wymagany poziom szczegółowości zależy od jej celu, odbiorcy i miejsca. Nie wolno jednak usprawiedliwiać formatem błędu, pominięcia koniecznego warunku ani fałszywej obietnicy.

## 4. Zamrożenie wersji i środowiska

Przed przebiegiem krytycznym trzeba zapisać:

- wersję i identyfikator metodologii;
- identyfikator i wersję publikacji;
- datę analizy;
- rodzaj oceniającego: człowiek, AI albo zespół;
- nazwę osoby, modelu albo zespołu;
- wersję lub migawkę modelu, jeżeli jest dostępna;
- ustawienie poziomu rozumowania, jeżeli jest dostępne;
- dostępne narzędzia;
- dostęp do pamięci rozmów, kontekstu projektu i prywatnych repozytoriów;
- inne warunki wpływające na odtworzenie wyniku.

Nie wolno zgadywać danych niewidocznych dla oceniającego. Należy zapisać `not_available`.

Podczas jednej analizy i zamrożonej serii nie wolno zmieniać kryteriów, kotwic, słowników, reguł werdyktu ani schematu wyniku.

## 5. Publikacja i materiały

### 5.1. Metryka publikacji

Przed analizą należy ustalić:

- tytuł;
- autora, autorów albo redakcję;
- wydawcę i miejsce publikacji;
- dokładny URL;
- datę publikacji i ostatniej aktualizacji;
- datę dostępu;
- język;
- rodzaj publikacji;
- deklarowanego albo rozsądnie przewidywanego odbiorcę;
- deklarowany cel i główną obietnicę;
- kompletność materiału.

Podpis autora, redakcję i daty należy sprawdzić także poza główną treścią, na przykład w nagłówku strony, stopce, danych strukturalnych lub metryce dokumentu. Nie należy przypisywać autorstwa na podstawie samej domeny.

### 5.2. Role materiałów

Każdy analizowany element otrzymuje jedną rolę:

- `tresc_glowna` — oceniana publikacja;
- `material_centralny_zewnetrzny` — załącznik, film, grafika, kod, raport, repozytorium albo aplikacja, bez których nie da się ocenić głównego wywodu;
- `material_dodatkowy` — materiał pomocniczy;
- `material_wylaczony` — element świadomie wyłączony z punktacji.

Dla treści głównej i materiału centralnego należy zapisać URL, datę dostępu, datę publikacji lub aktualizacji, wersję albo niezmienny identyfikator, informację o niezmienności oraz wykorzystany zakres.

Jeżeli dwa przebiegi kalibracyjne użyły różnych wersji materiału centralnego, nie są ścisłym powtórzeniem tego samego przypadku.

## 6. Rodzaj, odbiorca i profil językowy

### 6.1. Rodzaj publikacji

Należy wskazać jeden lub kilka rodzajów:

- informacyjny;
- poradnikowy;
- techniczny;
- prawny;
- analityczny;
- popularyzatorski;
- naukowy;
- szkoleniowy;
- opiniotwórczy;
- felietonowy;
- opis doświadczenia użytkownika;
- promocyjny lub handlowy;
- mieszany.

Rodzaj wpływa na oczekiwania, ale nie zwalnia z odpowiedzialności za sprawdzalne twierdzenia.

### 6.2. Profil odbiorcy

Przed punktacją trzeba zapisać:

- główną grupę odbiorców;
- istotne podgrupy, jeżeli ich rozumienie może się różnić;
- czy odbiorca został zadeklarowany, wywnioskowany, czy ustalony na obu podstawach;
- wiedzę, którą publikacja otwarcie albo milcząco zakłada;
- czy miejsce lub tekst deklarują funkcję popularyzatorską.

### 6.3. Profil językowy

Należy wskazać terminy i skróty konieczne do zrozumienia rdzenia oraz ustalić dla każdego:

- miejsce pierwszego użycia;
- czy został wyjaśniony albo jest jednoznaczny z kontekstu;
- czy jest potrzebny do osiągnięcia celu tekstu;
- jaki skutek ma jego użycie dla zrozumienia.

Nie wolno obniżać oceny za sam fakt używania specjalistycznego słownictwa. Problem występuje, gdy termin jest błędny, niekonsekwentny, zbędny, niewyjaśniony względem odbiorcy albo gdy nagromadzenie terminów blokuje tok wywodu.

Ocena profilu językowego jest oceną ekspercką, a nie wynikiem badania z użytkownikami. Trzeba to jawnie zaznaczyć.

## 7. Przebieg interpretacyjny

Przed sprawdzaniem prawdziwości należy:

- przygotować neutralne streszczenie;
- wskazać główną tezę i podstawowe zastosowanie praktyczne;
- ustalić odbiorcę, cel, obietnicę i zakładaną wiedzę;
- odróżnić informację, instrukcję, komentarz prawny, opinię, doświadczenie i promocję;
- przedstawić najmocniejszą rozsądną wersję głównych twierdzeń;
- ustalić rolę centralnych materiałów zewnętrznych.

Neutralne streszczenie należy zachować bez zmian wynikających z późniejszej krytyki.

## 8. Mapa twierdzeń

### 8.1. Zakres mapy

Mapa musi obejmować:

- wszystkie twierdzenia kluczowe;
- wszystkie zalecenia mogące wpłynąć na działanie odbiorcy;
- twierdzenia prawne, normatywne i techniczne, na których opiera się wniosek;
- twierdzenia pomocnicze, których fałszywość zmieniłaby ocenę przesłanki albo przykładu;
- reprezentatywne dodatkowe twierdzenia potrzebne do oceny powtarzalnego wzorca błędu.

Sama liczba wpisów ani problemów nie jest wynikiem jakości.

### 8.2. Kategorie twierdzeń

Każde twierdzenie otrzymuje jedną kategorię:

- **F — fakt;**
- **P — prawo;**
- **S — standard lub norma;**
- **T — technologia;**
- **B — badania i użytkownicy;**
- **Z — zalecenie;**
- **I — interpretacja;**
- **O — opinia lub ocena wartościująca.**

### 8.3. Znaczenie i weryfikowalność

Znaczenie:

- `kluczowe` — bez twierdzenia główna teza albo podstawowe zastosowanie traci podstawę;
- `wazne` — wpływa na istotną część rozumienia albo działania;
- `pomocnicze` — wspiera wywód, ale nie przesądza o rdzeniu.

Weryfikowalność:

- `weryfikowalne`;
- `czesciowo_weryfikowalne`;
- `nieweryfikowalne`.

### 8.4. Reguła atomizacji

Oddzielny wpis tworzy się, gdy część wypowiedzi może otrzymać inny wynik, kategorię, znaczenie albo zestaw źródeł niż pozostała część.

Należy rozdzielać w szczególności:

- datę od skutku prawnego;
- zakres podmiotów od zakresu produktów lub usług;
- fakt od zalecenia;
- korzyść prawdopodobną od gwarantowanej;
- kilka technik, jeżeli ich poprawność może być różna.

Nie należy rozdzielać wyliczenia, gdy wszystkie elementy mają ten sam status, podstawę i skutek.

Przed zamknięciem każdego wpisu trzeba zastosować test: „Czy część tego wpisu mogłaby być zgodna, a inna niezgodna?”. Jeżeli tak, wpis należy rozdzielić.

### 8.5. Minimalny wpis

Każdy wpis zawiera:

- lokalny identyfikator;
- opcjonalny identyfikator dopasowania kalibracyjnego;
- lokalizację;
- wierną parafrazę albo krótki cytat;
- kategorię;
- znaczenie;
- weryfikowalność;
- wynik;
- uzasadnienie granicy wyniku;
- pewność;
- identyfikatory źródeł;
- możliwy skutek błędu albo niejasności.

### 8.6. Dopasowanie w kalibracji

Jeżeli przed oceną istnieje neutralna wspólna lista twierdzeń, można przypisać `claim_match_id` bez ujawniania ocen innych przebiegów. Oceniający mogą dodawać nowe twierdzenia.

Jeżeli lista nie istnieje, dopasowanie wykonuje się dopiero po zamknięciu obu wyników. Zachowuje się identyfikatory lokalne i osobno zapisuje relacje 1:1, 1:wiele, wiele:1, wiele:wiele oraz wpisy jednostronne.

## 9. Wyniki sprawdzenia twierdzeń

Stosuje się następujące wartości:

- `zgodne` — treść i zakres odpowiadają najlepszym dostępnym źródłom; występują najwyżej pomijalne różnice redakcyjne;
- `zasadniczo_zgodne` — sens i bezpieczne zastosowanie pozostają prawidłowe po drobnym doprecyzowaniu;
- `czesciowo_zgodne` — materialna część jest poprawna, lecz brak, nadmiar albo warunek ogranicza użyteczność i wymaga nazwanej korekty;
- `mylace` — literalny fragment może być możliwy do obrony, lecz typowy odbiorca prawdopodobnie wyciągnie błędny wniosek z zakresu, kontekstu albo kategoryczności;
- `niezgodne` — zasadnicza treść przeczy najlepszym dostępnym źródłom;
- `nieweryfikowalne` — treść jest opinią, deklaracją lub doświadczeniem albo nie istnieje wystarczająca podstawa do jej sprawdzenia;
- `nierozstrzygniete` — istnieją wiarygodne sprzeczne podstawy albo rozstrzygnięcie przekracza dostępne kompetencje lub materiał.

`nierozstrzygniete` i `nieweryfikowalne` nie są punktami pomiędzy zgodnością a niezgodnością.

Każdy wpis musi zawierać krótkie uzasadnienie wyboru wyniku względem najbliższej rozsądnej alternatywy. Brak źródła w publikacji nie jest dowodem fałszu; wpływa przede wszystkim na wymiar D.

## 10. Źródła

### 10.1. Hierarchia

Źródła dobiera się do rodzaju twierdzenia. Preferowana kolejność:

1. obowiązujące akty prawne, dzienniki urzędowe i orzeczenia;
2. normy i standardy oraz dokumenty organizacji je ustanawiających;
3. oficjalne objaśnienia i dokumenty wdrożeniowe właściwych organów;
4. dokumentacja producenta technologii lub usługi;
5. recenzowane badania i rzetelnie opisane badania użytkowników;
6. materiały reprezentatywnych organizacji użytkowników;
7. uznane publikacje eksperckie;
8. materiały popularyzatorskie i branżowe;
9. media społecznościowe i nieudokumentowane relacje indywidualne.

Hierarchii nie wolno stosować mechanicznie. Dokumentacja producenta może potwierdzać deklarowaną funkcję, ale nie zawsze jej dostępność w rzeczywistym użyciu.

### 10.2. Zasady korzystania

- Otworzyć i przeczytać część źródła wspierającą wniosek.
- Nie traktować fragmentu wyniku wyszukiwania jako dowodu.
- Sprawdzić datę, wersję i zakres.
- Nie przypisywać źródłu szerszego wniosku, niż uzasadnia.
- Przy sporze przedstawić główne wiarygodne stanowiska.
- Jawnie wskazać źródło niedostępne lub płatne.
- Podawać bezpośrednie odsyłacze i datę dostępu.
- Dla twierdzeń prawnych, normatywnych, technicznych i innych zmiennych w czasie domyślnie sprawdzać aktualne źródła pierwotne.

## 11. Poprawność historyczna i bieżąca użyteczność

Należy rozdzielić:

1. **poprawność historyczną** — czy publikacja była poprawna według stanu na deklarowaną datę;
2. **bieżącą użyteczność** — czy obecnie dostępna wersja może być dziś bezpiecznie rozumiana i stosowana.

Późniejsza zmiana prawa, standardu albo technologii nie może automatycznie obniżać historycznej poprawności. Może obniżać kompletność, przejrzystość, bezpieczeństwo zastosowania lub dopasowanie, jeżeli strona jest nadal przedstawiana jako aktualna i nie sygnalizuje ograniczeń.

Oba ustalenia trzeba opisać osobno wraz z uzasadnieniem.

## 12. Wartość `nd`

Domyślnie każdy wymiar A–L otrzymuje ocenę liczbową. `nd` oznacza „nie dotyczy”, a nie brak danych, niską jakość ani trudność oceniającego.

`nd` wolno zastosować wyłącznie wtedy, gdy:

1. publikacja nie zawiera twierdzeń, zaleceń ani implikacji danego wymiaru;
2. brak zakresu jest zgodny z rodzajem i celem publikacji;
3. ocena liczbowa karałaby albo nagradzała tekst za treść, której zasadnie nie podejmuje;
4. raport zawiera jednozdaniowe uzasadnienie.

`nd` nie wolno zastosować, gdy materiał składa twierdzenie, lecz brakuje dowodów, źródło jest niedostępne, pominięto warunek, zalecenie jest niepełne albo oceniającemu brakuje kompetencji.

Wymiar C zawsze jest liczbowy, jeżeli publikacja opisuje działanie technologii, podaje technikę wdrożeniową, zaleca narzędzie, test lub audyt albo twierdzi, że rozwiązanie zapewnia zgodność lub usuwa barierę. Krótka lub handlowa forma nie uzasadnia `nd`.

## 13. Problemy

### 13.1. Znaczenie

- `krytyczne` — realne i prawdopodobne zastosowanie potwierdzonego błędu może bezpośrednio spowodować poważną barierę, naruszenie praw albo dotkliwą decyzję, a publikacja nie zawiera prostego zabezpieczenia;
- `duze` — problem istotnie zmienia rozumienie lub praktyczne zastosowanie rdzenia albo ważnego wsparcia, ale nie spełnia pełnego progu krytycznego;
- `srednie` — wymaga korekty i może zmienić część interpretacji albo działania, lecz nie podważa zasadniczej wartości;
- `male` — lokalna nieścisłość, brak albo problem redakcyjny o ograniczonych konsekwencjach.

Problem krytyczny wymaga łącznie: potwierdzonego błędu lub bardzo wysokiej pewności, prawdopodobnego zastosowania, możliwej poważnej szkody oraz braku prostego zabezpieczenia. W przeciwnym razie domyślnym maksimum jest problem duży.

### 13.2. Centralność

- `rdzen`;
- `istotne_wsparcie`;
- `element_poboczny`.

Centralność ocenia się względem konkretnej publikacji, nie ogólnej ważności tematu. Dla problemu dużego i krytycznego trzeba odpowiedzieć:

1. czy jego usunięcie zmienia główną tezę, podstawowe zalecenie lub obiecany rezultat;
2. czy po usunięciu publikacja nadal realizuje deklarowany cel.

### 13.3. Ryzyko zastosowania

- `wysokie` — typowy odbiorca może rozsądnie zastosować treść, a błąd prawdopodobnie spowoduje poważną barierę, naruszenie albo istotnie błędną decyzję;
- `srednie` — możliwy skutek jest zauważalny, ale ograniczony, odwracalny albo zależny od dodatkowych warunków;
- `niskie` — problem ma głównie skutek informacyjny lub redakcyjny.

Dla problemu dużego i krytycznego trzeba zapisać:

1. prawdopodobieństwo działania odbiorcy;
2. możliwą dotkliwość skutku;
3. odwracalność skutku;
4. krótkie uzasadnienie wyniku.

Centralność nie wyznacza automatycznie ryzyka, a ryzyko nie wyznacza centralności.

### 13.4. Pewność

Pewność `wysoka`, `srednia` albo `niska` opisuje siłę podstaw klasyfikacji, nie dotkliwość problemu. Problem o niskiej pewności nie może samodzielnie przesądzić o werdykcie `nierzetelny`.

### 13.5. Grupowanie

Kilka błędnych twierdzeń tworzy jeden problem, jeżeli mają wspólną przyczynę i można je naprawić jedną korektą zasadniczą.

Należy je rozdzielić, jeżeli wymagają różnych poprawek albo mają różną centralność lub ryzyko. Każdy problem zawiera opis wzorca, powiązane twierdzenia, główną poprawkę i uzasadnienie sposobu grupowania.

## 14. Oceny A–L

Każdy wymiar ocenia się oddzielnie od 0 do 4 według pliku `kotwice.md`. Nie wolno ustalać punktów na podstawie ogólnego wrażenia ani liczby problemów.

Dla każdego wymiaru należy:

1. wskazać dowody z publikacji;
2. porównać poziom z kotwicą niższą i wyższą;
3. zapisać uzasadnienie i pewność;
4. uzasadnić każde `nd`;
5. przy ocenie 0, 1 albo 4 wskazać cechę przekraczającą granicę.

Nie wolno:

- mechanicznie obniżać kilku wymiarów za ten sam błąd bez opisania odmiennego skutku;
- podwyższać poprawności za atrakcyjny styl;
- dostrajać wyniku do poprzedniego artykułu;
- korygować przesunięcia surowości w trakcie zamrożonej serii;
- zastępować profilu A–L jedną średnią.

### 14.1. Rozdział G, H i L

- **G** ocenia poprawność, jednoznaczność i konsekwencję terminów.
- **H** ocenia rzeczywistą możliwość zrozumienia tekstu przez zakładanego odbiorcę.
- **L** ocenia zgodność języka, szczegółowości i treści z celem oraz miejscem publikacji.

Nie należy obniżać G wyłącznie za trudny, ale poprawny termin. Niewyjaśniony termin obniża H, a przy niespełnionej obietnicy popularyzacji także L.

Jeżeli seria niewyjaśnionych terminów koniecznych do zrozumienia głównej tezy blokuje znaczącą część niespecjalistycznych odbiorców, H nie może przekroczyć 2. Jeżeli bez pomocy eksperta nie da się odtworzyć głównego toku, H nie może przekroczyć 1.

Jeżeli publikacja ma funkcję popularyzatorską, a jej rdzeń wymaga niewskazanej wiedzy specjalistycznej, L nie może przekroczyć 2.

## 15. Sekwencja werdyktu

### Krok 1. Możliwość rozstrzygnięcia

`nie_mozna_rozstrzygnac` stosuje się, gdy brak pełnej treści, centralnego materiału albo wystarczających dowodów uniemożliwia ocenę rdzenia. Nie stosuje się go tylko dlatego, że część twierdzeń jest nierozstrzygnięta.

### Krok 2. Wskazanie rdzenia

Przed werdyktem trzeba zapisać:

- główną tezę;
- podstawowe zastosowanie;
- problemy rdzenia;
- problemy wysokiego ryzyka.

W materiale mieszanym należy ustalić rolę centralnego artefaktu. Ostrzeżenie o eksperymentalności poprawia przejrzystość, ale nie usuwa błędów. Jeżeli publikacja zachęca do użycia wadliwego artefaktu, może on podważyć rdzeń.

### Krok 3. Test korekty kontrfaktycznej

Pytanie: „Co pozostaje po uczciwym poprawieniu potwierdzonych problemów?”

- `ograniczona` — główna teza, metoda i zasadnicza użyteczność pozostają;
- `strukturalna` — trzeba odwrócić główną tezę, zastąpić metodę, usunąć centralne zalecenie albo zmienić deklarowane zastosowanie;
- `nie_dotyczy` — tylko przy braku możliwości rozstrzygnięcia.

### Krok 4. Definicje

- `rzetelny` — rdzeń jest zgodny lub zasadniczo zgodny, nie ma problemów dużych ani krytycznych, źródła wystarczają, a materiał można bezpiecznie wykorzystać;
- `rzetelny_z_niewielkimi_zastrzezeniami` — nie ma problemów dużych ani krytycznych, a ograniczone problemy średnie nie zmieniają wniosku ani bezpiecznego działania;
- `rzetelny_z_istotnymi_zastrzezeniami` — istnieje problem duży albo kilka powiązanych średnich, ale po ograniczonej korekcie pozostaje wartościowy rdzeń;
- `nierzetelny` — problem rdzenia unieważnia główną tezę lub zastosowanie, potrzebna jest korekta strukturalna, podstawowe zalecenie zachowuje wysokie ryzyko albo kilka dużych problemów łącznie podważa rdzeń;
- `nie_mozna_rozstrzygnac` — ocena rdzenia nie jest odpowiedzialnie możliwa.

Werdyktu nie wolno wyprowadzać z sumy punktów ani liczby problemów.

### Krok 5. Kontrola spójności

- `rzetelny` i `rzetelny_z_niewielkimi_zastrzezeniami` nie mogą współistnieć z problemem dużym lub krytycznym;
- `nierzetelny` wskazuje problemy przesądzające, centralność, ryzyko i test korekty;
- rażącą rozbieżność profilu A–L z werdyktem trzeba wyjaśnić;
- brak problemu krytycznego nie wyklucza `nierzetelny`;
- problem krytyczny poza rdzeniem wymaga osobnego uzasadnienia wpływu na możliwość polecenia całej publikacji.

## 16. Pokrycie, pewność i możliwość polecenia

### 16.1. Pokrycie źródłowe

- `pelne` — sprawdzono wszystkie twierdzenia kluczowe i ważne;
- `wystarczajace` — sprawdzono rdzeń i zalecenia, a luki dotyczą elementów pomocniczych;
- `czesciowe` — luki mogą wpłynąć na część ocen, ale pozwalają na ostrożny werdykt;
- `niewystarczajace` — luki dotyczą rdzenia i zwykle prowadzą do braku rozstrzygnięcia.

### 16.2. Pewność mapy twierdzeń

- `wysoka` — rdzeń i wszystkie działania odbiorcy są objęte, a pominięcie materialnej tezy jest mało prawdopodobne;
- `srednia` — rdzeń jest objęty, ale część wspierająca może być inaczej podzielona albo niepełna;
- `niska` — braki materiału lub niejasna struktura utrudniają wiarygodne ustalenie mapy.

Pewność mapy należy uzasadnić oddzielnie od pewności werdyktu.

### 16.3. Pewność werdyktu

Pewność werdyktu jest `wysoka`, `srednia` albo `niska` i zależy od kompletności materiału, jakości źródeł, stopnia interpretacji oraz nierozstrzygniętych twierdzeń.

### 16.4. Bezpieczne polecenie

Należy wybrać jedną wartość:

- `bez_zastrzezen`;
- `z_niewielkimi_korektami`;
- `z_nazwanymi_korektami_lub_zrodlami`;
- `nie_do_praktycznego_uzycia`;
- `nie_mozna_ocenic`.

## 17. Raport i dane ustrukturyzowane

Raport musi zawierać w kolejności:

1. metrykę publikacji i przebiegu;
2. zakres, materiały i ograniczenia;
3. neutralne streszczenie;
4. odbiorcę, cel, miejsce i profil językowy;
5. najważniejsze tezy;
6. mapę i weryfikację twierdzeń;
7. poprawność historyczną i bieżącą użyteczność;
8. oceny A–L;
9. mocne strony;
10. problemy według znaczenia;
11. zrozumiałość dla grup odbiorców;
12. zalecane poprawki;
13. profil ocen i werdykt;
14. pewność mapy, werdyktu i pokrycie źródłowe;
15. wykaz źródeł.

Pełny `wynik.json` musi być zgodny z `wynik.schema.json`. W kalibracji tworzy się także `wyciag-kalibracyjny.json`. Wartości maszynowe stosują `snake_case` bez polskich znaków, a raport używa naturalnego języka.

## 18. Kalibracja i porównanie niezależnych ocen

### 18.1. Zamrożona seria

Przed ocenami należy ustalić i zamrozić korpus, kolejność, metodologię, schemat i środowisko. Każda publikacja jest osobnym przypadkiem. Wynik jednej nie może wpływać na punktację następnej. Problemy metodologii zapisuje się oddzielnie i rozpatruje dopiero po zakończeniu serii.

### 18.2. Niezależność przebiegów A i B

Przebiegi A i B:

- pracują w oddzielnych pustych kontekstach;
- nie widzą swoich wyników;
- używają tej samej zamrożonej wersji materiału i metody;
- mogą być wykonane przez ten sam system AI;
- zapisują środowisko oceniające.

Różne systemy AI są osobnym testem przenośności i nie są obowiązkowe dla zwykłej serii powtarzalności.

Jeżeli środowisko pozwala uruchamiać odizolowanych agentów lub konteksty, koordynator AI powinien sam uruchomić oba przebiegi, zebrać wyniki, przeprowadzić walidację i porównanie. Użytkownik nie powinien ręcznie przeklejać wielostronicowych poleceń. Jeżeli rzeczywista izolacja nie jest możliwa, trzeba to jawnie zgłosić.

### 18.3. Miary porównawcze

Raportować co najmniej:

- dokładną zgodność ocen A–L;
- zgodność w granicy jednego punktu;
- średnią bezwzględną różnicę i kierunek różnicy;
- wyniki według wymiaru;
- zgodność werdyktów;
- pokrycie map twierdzeń;
- zgodność wyników bezpośrednich par 1:1;
- zgodność znaczenia, centralności i ryzyka problemów po ich dopasowaniu;
- rozbieżności `nd`;
- różnice wynikające z atomizacji i grupowania.

Miary statystyczne, takie jak ważona kappa Cohena, są pomocnicze i nie zastępują analizy rozbieżności.

## 19. Kontrola jakości

Przed zamknięciem analizy należy potwierdzić:

1. pełna treść i centralne materiały zostały pozyskane i oznaczone wersją;
2. autorstwo, wydawca i daty zostały sprawdzone;
3. metodologia została zamrożona przed krytyką;
4. neutralne streszczenie powstało przed weryfikacją;
5. profil odbiorcy, wiedzy zakładanej i języka został zapisany;
6. mapa obejmuje rdzeń i działania odbiorcy;
7. zastosowano test atomizacji;
8. każde źródło faktycznie odczytano;
9. wynik każdego twierdzenia ma uzasadnienie granicy;
10. poprawność historyczną oddzielono od bieżącej użyteczności;
11. każde `nd` ma prawidłowe uzasadnienie;
12. każdą ocenę porównano z kotwicami sąsiednimi;
13. każdy problem duży i krytyczny ma test centralności i ryzyka;
14. sposób grupowania problemów został uzasadniony;
15. werdykt przeszedł test korekty;
16. pewność mapy, werdyktu i pokrycie źródłowe zapisano osobno;
17. dane strukturalne przeszły walidację;
18. raport nie przechowuje pełnej kopii chronionej publikacji bez podstawy;
19. wynik nie został dostrojony do wcześniejszych przypadków.

## 20. Role AI i człowieka

AI może samodzielnie pozyskiwać materiał, tworzyć mapę, sprawdzać źródła, wystawiać oceny, walidować pliki i porównywać przebiegi w granicach dostępnych narzędzi i uprawnień.

Człowiek zarządza rozwojem metody: zatwierdza zmianę metodologii, korpus kalibracyjny i publikację wydania oraz rozstrzyga sporne decyzje o dużym znaczeniu. Nie musi ręcznie powtarzać każdej oceny AI.

W sprawach o wysokim ryzyku prawnym, finansowym, zdrowotnym, bezpieczeństwa lub praw osób wynik AI powinien wspierać, a nie zastępować odpowiedzialną decyzję osoby posiadającej właściwe kompetencje.

## 21. Ograniczenia

Standard zwiększa porównywalność, lecz jej nie gwarantuje. Na wynik wpływają między innymi:

- dostępność pełnej treści i źródeł;
- zmiany prawa, norm, technologii i praktyk;
- dobór korpusu;
- różnice interpretacyjne i językowe;
- właściwości modelu lub oceniającego;
- brak niezależnego wzorca prawidłowej oceny;
- brak reprezentatywnych badań użytkowników;
- ręczny charakter późniejszego dopasowania semantycznego.

Wersja 0.3 pozostaje projektem do czasu zakończenia kontroli, zamrożenia i opublikowania wydania.
