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

Życzliwa parafraza nie może usuwać ani osłabiać kwantyfikatorów, absolutów, przeczeń, wyjątków, warunków, zakresu podmiotowego lub przedmiotowego ani statusu prawnego lub normatywnego wypowiedzi. Nie może zmieniać „musi” na „warto”, „zawsze” na „często”, „zapewnia zgodność” na „pomaga w zgodności” ani obowiązku na rekomendację.

Jeżeli wypowiedź zawiera poprawny sens węższy i błędny sens szerszy, mapa zachowuje oba znaczenia albo rozdziela je na osobne twierdzenia. Najmocniejsza rozsądna interpretacja musi nadal być interpretacją tekstu, a nie jego naprawioną wersją.

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

Nie wolno zgadywać danych niewidocznych dla oceniającego. Nieznane dane bibliograficzne zapisuje się jako `null`, niedostępne informacje środowiskowe jako `not_available`, a informacje niedotyczące danego rodzaju oceniającego jako `not_applicable`. Obowiązkowego pola nie wolno pomijać ani zastępować pustym tekstem.

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

### 5.3. Zamrożone wejścia kalibracyjne

Każdy materiał użyty w nowym przebiegu kalibracyjnym musi mieć zapisaną sumę SHA-256 oraz podstawę haszowania:

- `raw_bytes` — dokładne pozyskane bajty;
- `rendered_capture` — utrwalony wynik renderowania;
- `canonical_text` — tekst uzyskany według jawnie ustalonej procedury normalizacji.

Suma bez wskazania podstawy nie wystarcza do stwierdzenia tożsamości wejścia. Brak publicznej kopii materiału, na przykład ze względu na prawa autorskie, nie zwalnia z utrwalenia jego sumy w prywatnym laboratorium. Nieznaną wersję materiału zapisuje się jako `null`; suma kontrolna i data dostępu identyfikują wtedy faktycznie pozyskane wejście, ale nie dowodzą jego wcześniejszej treści.

## 6. Rodzaj, miejsce publikacji, odbiorcy i profil językowy

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

### 6.2. Obowiązkowe rozpoznanie miejsca, celu i odbiorców

Przed krytyczną oceną języka oraz przed nadaniem ocen G, H i L oceniający musi rozpoznać kontekst publikacji. Jeżeli elementy są dostępne, sprawdza co najmniej:

1. stronę główną serwisu;
2. stronę „O nas” lub „Informacje”;
3. opis bloga albo newslettera;
4. stronę zapisu do newslettera;
5. opis kategorii albo cyklu publikacji;
6. politykę redakcyjną;
7. opis autora;
8. sposób promowania publikacji;
9. bezpośrednie zwroty do czytelników w artykule;
10. wiedzę rzeczywiście potrzebną do zrozumienia tekstu.

Dla każdego elementu zapisuje `sprawdzono`, `niedostepne`, `nie_odnaleziono` albo `nie_dotyczy`, wraz z adresem, lokalizacją i datą dostępu, jeżeli są dostępne. Braku informacji nie wolno zastępować domysłem. Informacji o autorze i wydawcy używa się wyłącznie do ustalenia celu, odbiorców, autorstwa i charakteru miejsca, a nie do oceny wiarygodności na podstawie reputacji.

Przebieg krytyczny G, H i L nie może rozpocząć się przed zapisaniem profilu. Jeżeli profil nie może zostać wiarygodnie ustalony, raport wskazuje ten fakt jawnie, nadaje ustaleniu niską pewność i przedstawia co najmniej dwa rozsądne warianty odbiorcy, jeżeli prowadziłyby do innej oceny H lub L.

### 6.3. Hierarchia dowodów dotyczących odbiorców i celu

Dowody stosuje się w następującej kolejności:

1. bezpośrednia deklaracja wydawcy lub autora dotycząca odbiorców konkretnej publikacji;
2. deklarowany cel oraz odbiorcy całego serwisu, bloga, newslettera, kategorii albo cyklu;
3. sposób przedstawiania i promowania publikacji;
4. bezpośrednie wskazówki w artykule, w tym zwroty do czytelników i nazwane zastosowania;
5. zaobserwowany poziom trudności tekstu.

Poziom trudności jest cechą podlegającą ocenie, a nie samodzielnym dowodem specjalistycznego przeznaczenia publikacji.

**Trudny i specjalistyczny język publikacji nie może sam w sobie stanowić dowodu, że publikacja jest przeznaczona dla specjalistów.**

Jeżeli miejsce publikacji deklaruje funkcję popularyzatorską albo kieruje treści również do niespecjalistów, oceniający nie może pominąć tej grupy tylko dlatego, że konkretny artykuł jest trudny. Ogólna deklaracja miejsca tworzy domniemanie objęcia tej grupy. Można je zawęzić tylko za pomocą wyraźnego i dostępnego oznaczenia konkretnego artykułu, kategorii albo cyklu jako materiału dla węższej grupy.

W razie sprzeczności dowodów raport zachowuje oba ustalenia, wskazuje dowód wyższej rangi i wyjaśnia, dlaczego jeden przeważa. Nie wolno ukrywać sprzeczności przez wybór wygodniejszego profilu.

### 6.4. Obowiązkowy profil kontekstu publikacji

Profil zapisuje:

- rodzaj miejsca publikacji;
- deklarowany cel miejsca publikacji;
- deklarowanych odbiorców;
- rozsądnie przewidywanych odbiorców;
- dodatkowe istotne grupy odbiorców;
- odbiorców konkretnego artykułu;
- wiedzę zadeklarowaną jako wymagana;
- wiedzę rzeczywiście potrzebną do zrozumienia tekstu;
- dowody wykorzystane do każdego ustalenia;
- sprzeczności między opisem miejsca a treścią artykułu;
- pewność profilu: `wysoka`, `srednia` albo `niska`;
- stan ustalenia: `ustalony`, `czesciowo_ustalony` albo `nieustalony_wiarygodnie`.

Każde ustalenie wskazuje identyfikatory wspierających dowodów. Dowód zapisuje rodzaj, rangę 1–5, URL, lokalizację, datę dostępu oraz krótki cytat lub wierną parafrazę.

Profil jest `ustalony`, gdy dowody rangi 1 lub 2 pozwalają określić istotne grupy i nie pozostaje sprzeczność mogąca zmienić H lub L. Jest `czesciowo_ustalony`, gdy główna grupa jest znana, lecz co najmniej jedna istotna grupa, wymagany poziom wiedzy albo zakres obietnicy pozostaje sporny i może zmienić H lub L. Jest `nieustalony_wiarygodnie`, gdy brak podstaw do wyboru między co najmniej dwoma rozsądnymi profilami prowadzącymi do różnych H lub L.

Pewność `wysoka` wymaga bezpośredniego dowodu odpowiedniej rangi dla grup i zakresu konkretnego artykułu oraz braku materialnej sprzeczności. Pewność `srednia` stosuje się przy zgodnych dowodach pośrednich albo gdy deklaracja miejsca wymaga doprecyzowania przez artykuł. Pewność `niska` stosuje się przy samych wskazówkach z tekstu, sprzecznych dowodach albo profilu nieustalonym wiarygodnie.

„Wiedza rzeczywiście potrzebna” obejmuje tylko wiedzę konieczną do odtworzenia głównej tezy, ważnego warunku albo obiecanego działania. Wiedzę pomocną, lecz niekonieczną, zapisuje się osobno jako ułatwiającą. Każdy element wiedzy koniecznej wskazuje fragment publikacji, który bez niej staje się nieodtwarzalny lub ryzykowny.

Każdy element wiedzy koniecznej musi wskazywać dokładny fragment, warunek albo działanie, którego odbiorca bez tej wiedzy nie odtworzy. Wiedza jedynie pomocna trafia do osobnego pola `facilitating_knowledge` i nie obniża H.

Jeżeli odbiorcy nie mogą zostać wiarygodnie ustaleni, nie wolno bez odpowiednich dowodów uznać ich za specjalistów. Należy zapisać warianty profilu i wrażliwość H oraz L na te warianty. Wynik H pozostaje liczbowy, ale przy równorzędnych wariantach przyjmuje ostrożniejszy wynik i niską pewność.

### 6.5. Publikacje dla grup mieszanych

Role zawodowe łączy się w jedną grupę, jeżeli publikacja składa wobec nich tę samą obietnicę, wymaga tej samej wiedzy i prowadzi do tego samego zadania. Grupę dzieli się tylko wtedy, gdy różni się obietnica, potrzebna wiedza, bariera zrozumienia albo możliwy wynik H lub L.

Przykładowo programistów front-end i back-end można połączyć, jeżeli tekst kieruje do obu tę samą procedurę, wymaga tych samych wiadomości i prowadzi do tego samego rezultatu. Koordynatora i wykonawcę należy rozdzielić, gdy pierwszy ma podjąć decyzję organizacyjną, a drugi wykonać kroki techniczne, lub gdy bez dodatkowej wiedzy ich H albo L może być inne. Samo występowanie dwóch nazw stanowisk nie uzasadnia ani połączenia, ani podziału.

Dla każdej istotnej grupy odbiorców należy osobno ocenić możliwość zrozumienia rdzenia i zapisać `group_h_score` od 0 do 4, wymagane założenia oraz bariery. Dla każdej istotnej grupy objętej obietnicą publikacji zapisuje się także `group_l_score` od 0 do 4. Ocena odpowiada na pytanie, czy publikacja realizuje wobec tej grupy deklarowany cel i obiecany sposób użycia; nie jest kopią ogólnego L.

Grupa jest istotna, jeżeli jest bezpośrednio zadeklarowana dla publikacji lub miejsca albo jeżeli cel, promocja i przewidywane użycie wskazują, że publikacja składa wobec niej materialną obietnicę. Sama możliwość przypadkowego trafienia na stronę nie czyni grupy istotną.

Ogólna ocena H odpowiada najniższej ocenie wśród istotnych grup objętych obietnicą konkretnej publikacji. Grupa zadeklarowana dla całego miejsca pozostaje objęta domniemaniem, chyba że artykuł, kategoria albo cykl został wyraźnie i dostępnie oznaczony jako przeznaczony dla węższej grupy.

Ogólne L odpowiada najniższej ocenie L wśród istotnych grup objętych obietnicą publikacji. Grupy nieobjęte obietnicą mogą być opisane, lecz nie obniżają ogólnego L. Jeżeli ten sam brak dotyczy wyłącznie zrozumiałości, obniża H. Obniża również L tylko wtedy, gdy przez ten brak publikacja nie realizuje zadeklarowanej funkcji wobec danej grupy.

Trudności grupy wpływają tylko na opis ograniczeń, a nie na ogólną ocenę H, jeżeli grupa nie jest zadeklarowana, nie jest rozsądnie przewidywaną grupą celu i nie otrzymuje od publikacji materialnej obietnicy.

Tekstu nie wolno uznać za zrozumiały dla grupy mieszanej tylko dlatego, że rozumie go specjalista.

Jeżeli niewyjaśnione terminy blokują ważną część tekstu dla istotnej grupy niespecjalistycznej, H nie może być wyższe niż 2. Jeżeli bez pomocy eksperta nie można odtworzyć głównej myśli, H nie może być wyższe niż 1.

Jeżeli miejsce deklaruje funkcję popularyzatorską, ale zrozumienie rdzenia wymaga nieujawnionej wiedzy specjalistycznej, L nie może być wyższe niż 2.

Niezbędny termin specjalistyczny nie obniża wyniku tylko dlatego, że jest specjalistyczny, jeżeli został poprawnie użyty i wystarczająco wyjaśniony w tekście, kontekście lub łatwo dostępnym materiale, do którego publikacja prowadzi przed użyciem terminu do ważnego wniosku.

### 6.6. Profil językowy

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
- zapisać profil miejsca i odbiorców wraz z hierarchią dowodów, sprzecznościami i pewnością;
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

Oddzielny wpis tworzy się, gdy część wypowiedzi może mieć inny wynik, kategorię, znaczenie, zestaw źródeł, punkt odniesienia w czasie albo skutek praktyczny.

Należy rozdzielać w szczególności:

- fakt, przyczynę i skutek, jeżeli każde wymaga osobnej podstawy;
- obowiązek, zakres, warunek i wyjątek, jeżeli mogą być ocenione odmiennie;
- każdą liczbę albo kategorię z wyliczenia, jeżeli może pochodzić z innej wartości źródłowej;
- przykłady kodu lub techniki, jeżeli ich poprawność może być różna;
- opis stanu historycznego i twierdzenie o stanie obecnym;
- twierdzenie opisowe i wynikające z niego zalecenie.

Nie rozdziela się składników, które tracą sens bez wspólnego warunku lub kwantyfikatora. Przy rozdzieleniu warunek, wyjątek, przeczenie i zakres powtarza się w każdym wpisie, którego dotyczy.

Przed zamknięciem wpisu oceniający odpowiada na trzy pytania:

1. czy dowolna część może otrzymać inny wynik;
2. czy wymaga innego źródła;
3. czy jej błąd miałby inny skutek.

Jedna odpowiedź „tak” wymaga rozdzielenia, chyba że spowodowałoby to utratę znaczenia zależnego; wyjątek trzeba uzasadnić w polu `atomization_rationale`.

Granicę wpisu ustala się według najmniejszego fragmentu, który zachowuje pełny warunek, zakres i skutek, a zarazem może otrzymać jeden wynik. Nie wolno łączyć poprawnego rdzenia z wadliwym absolutem tylko dlatego, że występują w jednym zdaniu. Nie wolno też rozdzielić kwantyfikatora, wyjątku, przeczenia albo statusu prawnego od części, którą ogranicza.

Przykłady:

1. „Narzędzie wykrywa część błędów, dlatego gwarantuje zgodność” tworzy co najmniej dwa wpisy: opis wykrywania oraz wniosek o gwarancji.
2. „Każdy podmiot musi stosować X, z wyjątkiem Y” tworzy osobne wpisy tylko wtedy, gdy każdy zachowuje informację o właściwym zakresie i wyjątku.
3. Wyliczenie kilku wymagań tworzy osobne wpisy, jeżeli mają różne podstawy lub mogą otrzymać różne wyniki; wspólny warunek należy powtórzyć.
4. Jedna procedura kodowa pozostaje jednym wpisem, jeżeli jej kroki działają wyłącznie łącznie; niezależny błędny krok tworzy osobny wpis.

W kalibracji `atomization_rationale` musi wskazać zastosowany przykład albo wyjaśnić, dlaczego przypadek jest inny.

### 8.5. Minimalny wpis

Każdy wpis zawiera:

- lokalny identyfikator;
- opcjonalny identyfikator dopasowania kalibracyjnego;
- lokalizację;
- wierną parafrazę albo krótki cytat;
- kategorię;
- znaczenie;
- weryfikowalność;
- uzasadnienie atomizacji;
- odtwarzalny ślad ekstrakcji;
- wynik;
- uzasadnienie granicy wyniku;
- pewność;
- identyfikatory źródeł;
- możliwy skutek błędu albo niejasności.

Każde twierdzenie w kalibracji zawiera odtwarzalny ślad:

`fragment albo lokalizacja publikacji → dokładna liczba, kod lub treść źródłowa → wierna parafraza → wynik`.

Jeżeli krótki cytat nie jest potrzebny albo jego zapis byłby nieproporcjonalny, wystarcza dokładna lokalizacja. Dla liczby zapisuje się licznik, mianownik, jednostkę i warunek. Dla kodu zapisuje się minimalny fragment potrzebny do oceny. Dla wykresu zapisuje się serię, kategorię i odczytaną wartość. Ślad wskazuje identyfikatory źródeł weryfikacyjnych. Parafraza i wynik w śladzie muszą być zgodne z głównymi polami twierdzenia.

### 8.6. Dopasowanie w kalibracji

Jeżeli przed oceną istnieje neutralna wspólna lista twierdzeń, można przypisać `claim_match_id` bez ujawniania ocen innych przebiegów. Oceniający mogą dodawać nowe twierdzenia.

Jeżeli lista nie istnieje, dopasowanie wykonuje się dopiero po zamknięciu obu wyników. Zachowuje się identyfikatory lokalne i osobno zapisuje relacje 1:1, 1:wiele, wiele:1, wiele:wiele oraz wpisy jednostronne.

Dla relacji 1:1 wynik dopasowania ustala się następująco:

- `exact` — oba twierdzenia mają tę samą etykietę wyniku;
- `adjacent` — etykiety tworzą jedną z par: `zgodne`–`zasadniczo_zgodne`, `zasadniczo_zgodne`–`czesciowo_zgodne`, `czesciowo_zgodne`–`mylace` albo `mylace`–`niezgodne`;
- `different` — oba wyniki są rozstrzygnięciami merytorycznymi, lecz nie są identyczne ani sąsiednie;
- `not_comparable` — co najmniej jeden wynik to `nieweryfikowalne` lub `nierozstrzygniete`, albo wpisy mimo wspólnego tematu nie oceniają tego samego zakresu.

`nieweryfikowalne` i `nierozstrzygniete` są `exact` wyłącznie wtedy, gdy obie strony mają tę samą z tych etykiet i ten sam przedmiot rozstrzygnięcia.

W relacji złożonej najpierw porównuje się najmniejsze wspólne składowe semantyczne. Cała relacja jest `exact`, gdy wszystkie składowe są dokładnie zgodne; `adjacent`, gdy żadna nie jest `different` ani `not_comparable`, a co najmniej jedna jest sąsiednia; `different`, gdy co najmniej jedna materialna składowa jest różna; w pozostałych przypadkach `not_comparable`. Raport zapisuje liczbę składowych każdego rodzaju.

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

Przy granicznych przypadkach stosuje się następującą kolejność:

1. `niezgodne`, gdy zasadnicza treść twierdzenia w zwykłym, kontekstowym odczytaniu przeczy najlepszym dostępnym źródłom; węższa prawdziwa teza nie ratuje wypowiedzianej tezy szerszej;
2. `mylace`, gdy literalny fragment da się obronić, lecz zakres, kategoryczność, zestawienie lub pominięty kontekst z dużym prawdopodobieństwem prowadzi istotnego odbiorcę do błędnego wniosku;
3. `czesciowo_zgodne`, gdy dająca się wskazać materialna część twierdzenia jest poprawna, a inna część lub warunek wymaga korekty, lecz po nazwanym ograniczeniu pozostaje bezpieczny i użyteczny sens;
4. `nierozstrzygniete`, gdy po adekwatnym wyszukaniu istnieją wiarygodne sprzeczne podstawy albo brakuje materiału potrzebnego do odpowiedzialnego wyboru; nie stosuje się tej wartości tylko dlatego, że oceniający nie znalazł szybkiego potwierdzenia;
5. `mylace` zamiast `nierozstrzygniete`, gdy problemem nie jest stan dowodów, lecz znany sposób, w jaki tekst prowadzi odbiorcę do błędnego wniosku.

Każdy wpis musi zawierać krótkie uzasadnienie wyboru wyniku względem najbliższej rozsądnej alternatywy oraz jedno zdanie wyjaśniające, dlaczego ją odrzucono. Brak źródła w publikacji nie jest dowodem fałszu; wpływa przede wszystkim na wymiar D.

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

Bieżącą treścią jest treść rzeczywiście pozyskana w dniu dostępu. Można ją oceniać pod względem bieżącej użyteczności, lecz nie wolno przypisywać jej wcześniejszej dacie bez osobnego dowodu wersji.

Wersję historyczną uznaje się za odtworzoną tylko wtedy, gdy co najmniej jeden wskazany dowód:

1. zachowuje rzeczywistą treść ocenianej wersji, a nie wyłącznie jej metadane lub opis zmian;
2. identyfikuje datę, wydanie albo wersję;
3. obejmuje zakres treści potrzebny do ustalenia wyniku;
4. ma stabilny i sprawdzalny identyfikator, na przykład adres migawki archiwalnej, commit, wersjonowane wydanie albo sumę SHA-256 zachowanej kopii.

Sama data publikacji lub aktualizacji, bieżąca suma kontrolna, niezmieniony URL, wynik wyszukiwania, pamięć podręczna, opis zmiany albo brak widocznego oznaczenia aktualizacji nie dowodzą treści wcześniejszej wersji.

Jeżeli warunki rekonstrukcji nie są spełnione, `historical_version_reconstructable` ma wartość `false`, `assessed_historical_version` ma wartość `not_reconstructable`, `historical_accuracy` ma wartość `nierozstrzygniete`, a `historical_confidence` ma wartość `niska`. Pewność historyczna oznacza pewność ustalenia poprawności zachowanej wersji, a nie pewność, że dawnego materiału nie odnaleziono.

Jeżeli wersja historyczna została odtworzona, `assessed_historical_version` wskazuje `original` albo `archived_update`, a `version_evidence_ids` zawiera co najmniej jeden materiał zachowujący ocenianą treść.

`historical_version_reconstructable: true` wymaga osobnego zapisu `historical_version_evidence` dla każdego wskazanego materiału. Zapis zawiera identyfikator materiału, datę albo oznaczenie zachowanej treści, stabilny identyfikator, rodzaj dowodu oraz objęty zakres. Materiał musi być oznaczony `immutable: tak`, a zestaw identyfikatorów materiałów w zapisach dowodowych musi być zgodny z `version_evidence_ids`.

Kopia pobrana w dniu analizy potwierdza wyłącznie treść bieżącą, chyba że osobny dowód wskazuje, jaką wcześniejszą wersję zachowuje. Bieżąca suma SHA-256 i oznaczenie `immutable: tak` nie są samodzielnym dowodem treści historycznej. Walidator sprawdza kompletność i spójność zapisu dowodowego, ale nie zastępuje merytorycznej oceny, czy wskazana migawka albo wersja rzeczywiście zachowuje deklarowaną treść.

Przeskalowanie, zmiana kodowania lub techniczna rekompresja materiału nie tworzą odrębnej wersji znaczeniowej tylko wtedy, gdy zachowano całą treść, kolejność, znaczenie i czytelność. Transformację i podstawę uznania równoważności trzeba opisać w `material_changes`.

Późniejszej poprawki nie wolno użyć do podniesienia historycznej oceny wersji pierwotnej, a dawnego błędu nie wolno przypisać wersji obecnej bez dowodu, że pozostał.

## 12. Wartość `nd`

Domyślnie każdy wymiar A–L otrzymuje ocenę liczbową. `nd` oznacza „nie dotyczy”, a nie brak danych, niską jakość ani trudność oceniającego.

`nd` wolno zastosować wyłącznie wtedy, gdy:

1. publikacja nie zawiera twierdzeń, zaleceń ani implikacji danego wymiaru;
2. brak zakresu jest zgodny z rodzajem i celem publikacji;
3. ocena liczbowa karałaby albo nagradzała tekst za treść, której zasadnie nie podejmuje;
4. raport zawiera jednozdaniowe uzasadnienie.

`nd` nie wolno zastosować, gdy materiał składa twierdzenie, lecz brakuje dowodów, źródło jest niedostępne, pominięto warunek, zalecenie jest niepełne albo oceniającemu brakuje kompetencji.

Wymiar C otrzymuje ocenę liczbową tylko wtedy, gdy publikacja sama przedstawia twierdzenie o działaniu technologii, mechanizmu, narzędzia, testu albo rozwiązania. Samo wymienienie WCAG lub normy jako podstawy prawnej nie jest jeszcze twierdzeniem technicznym. Przytoczenie funkcji oczekiwanych przez uczestników badania nie staje się twierdzeniem technicznym autora bez jego własnej oceny działania tych funkcji. Krótka lub handlowa forma nie uzasadnia `nd`, jeżeli takie twierdzenie występuje.

Wymiar J otrzymuje ocenę liczbową, gdy publikacja przedstawia, wykorzystuje albo uogólnia doświadczenia, potrzeby lub wyniki badań użytkowników albo składa obietnicę, której realizacja wymaga takiej perspektywy. Samo wymienienie osób z niepełnosprawnościami jako beneficjentów regulacji nie wystarcza. Brak badań użytkowników w wąskim tekście prawnym lub technicznym nie obniża J i prowadzi do `nd`. Szeroki cel albo obietnica kompletnego poradnika może jednak powodować, że perspektywa użytkowników staje się wymagana; wtedy J pozostaje liczbowe także wtedy, gdy publikacja tej perspektywy nie dostarczyła.

W `dimension_applicability` zapisuje się osobno podstawę stosowalności C i J. Walidator sprawdza zgodność tej decyzji z wartością liczbową albo `nd`; nie rozstrzyga automatycznie znaczenia naturalnego języka publikacji.

## 13. Problemy

### 13.1. Znaczenie

- `krytyczne` — realne i prawdopodobne zastosowanie potwierdzonego błędu może bezpośrednio spowodować poważną barierę, naruszenie praw albo dotkliwą decyzję, a publikacja nie zawiera prostego zabezpieczenia;
- `duze` — problem istotnie zmienia rozumienie lub praktyczne zastosowanie rdzenia albo ważnego wsparcia, ale nie spełnia pełnego progu krytycznego;
- `srednie` — wymaga korekty i może zmienić część interpretacji albo działania, lecz nie podważa zasadniczej wartości;
- `male` — lokalna nieścisłość, brak albo problem redakcyjny o ograniczonych konsekwencjach.

Problem krytyczny wymaga łącznie: potwierdzonego błędu lub bardzo wysokiej pewności, prawdopodobnego zastosowania, możliwej poważnej szkody oraz braku prostego zabezpieczenia. W przeciwnym razie domyślnym maksimum jest problem duży.

Jeżeli problem duży ma wysokie ryzyko albo dotyczy bezpośrednio wykonalnej instrukcji o możliwych poważnych skutkach, należy wskazać osobno cztery przesłanki krytyczności i zapisać, której nie spełniono. Problem jest krytyczny tylko wtedy, gdy spełnia wszystkie cztery. Ustrukturyzowany `criticality_test` zapisuje także, czy problem dotyczy takiej bezpośrednio wykonalnej instrukcji. Dla problemu krytycznego wszystkie cztery przesłanki mają wartość `true`, a `failed_prerequisite` ma wartość `null`; dla problemu dużego co najmniej jedna przesłanka ma wartość `false` i zostaje wskazana w `failed_prerequisite`.

### 13.2. Centralność

- `rdzen`;
- `istotne_wsparcie`;
- `element_poboczny`.

Centralność ocenia się względem konkretnej publikacji, nie ogólnej ważności tematu.

W teście centralności „usunięcie problemu” oznacza najpierw **minimalną uczciwą naprawę wady przy zachowaniu zamierzonego tematu i funkcji publikacji**: poprawienie błędu, dodanie koniecznego warunku, zapewnienie brakującego odpowiednika albo zawężenie wniosku do zakresu wspieranego przez dowody.

Nie oznacza automatycznego skasowania całej sekcji zawierającej problem. Usunięcie całej części stosuje się dopiero wtedy, gdy nie istnieje prawdziwa, udokumentowana wersja zachowująca jej funkcję. Wtedy raport zapisuje oba kroki: próbę minimalnej naprawy i skutek koniecznego usunięcia lub zastąpienia części.

Centralność odpowiada na pytanie, czy po uczciwej naprawie trzeba zmienić główną tezę, podstawowe zalecenie, obiecany rezultat albo deklarowane zastosowanie. Nie mierzy samej długości poprawki.

Dla problemu dużego i krytycznego trzeba odpowiedzieć:

1. jaka jest minimalna uczciwa naprawa;
2. czy naprawa zmienia główną tezę, podstawowe zalecenie, obiecany rezultat lub deklarowane zastosowanie;
3. czy po naprawie publikacja nadal realizuje deklarowany cel;
4. czy konieczne jest usunięcie albo zastąpienie części.

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

W zwykłej pojedynczej ocenie pełny test składowy centralności i ryzyka pozostaje obowiązkowy dla problemów dużych i krytycznych. W każdej ocenie należącej do kalibracji poziom centralności, poziom ryzyka zastosowania i krótkie uzasadnienie są obowiązkowe dla wszystkich problemów, także średnich i małych.

Dla problemów średnich i małych nie trzeba wypełniać pełnej listy składowych testu, chyba że mogą wpłynąć na werdykt, grupowanie albo różnią się między przebiegami. Porównanie zgodności centralności i ryzyka podaje osobno dla wszystkich dopasowanych problemów oraz dla podzbioru problemów dużych i krytycznych.

### 13.4. Pewność

Pewność `wysoka`, `srednia` albo `niska` opisuje siłę podstaw klasyfikacji, nie dotkliwość problemu. Problem o niskiej pewności nie może samodzielnie przesądzić o werdykcie `nierzetelny`.

### 13.5. Grupowanie

Kilka błędnych twierdzeń tworzy jeden problem, jeżeli mają wspólną przyczynę i można je naprawić jedną korektą zasadniczą.

Twierdzenia wolno połączyć w jeden problem tylko wtedy, gdy łącznie spełniają cztery warunki: mają wspólną przyczynę, wymagają jednej zasadniczej korekty, mają ten sam poziom centralności oraz mają ten sam poziom ryzyka zastosowania. Różnica któregokolwiek z tych elementów wymaga osobnych problemów.

Brak źródła, błąd merytoryczny, niejasny status normatywny i bariera zrozumienia nie są automatycznie jednym problemem, nawet gdy dotyczą tego samego akapitu. Można je połączyć tylko wtedy, gdy jedna korekta rzeczywiście usuwa wszystkie skutki.

Każdy problem `srednie` albo `duze` przechodzi ustrukturyzowany test granicy. Należy zapisać: istotną grupę odbiorców, minimalną uczciwą poprawkę, działanie lub wniosek przed poprawką, działanie lub wniosek po poprawce oraz informację, czy zmiana dotyczy ważnego zakresu albo sposobu działania.

Problem jest `duze`, gdy po poprawce co najmniej jedna istotna grupa powinna zmienić ważną decyzję, zakres działania albo sposób wykonania. Jeżeli poprawka usuwa materialną nieścisłość, ale nie zmienia ważnej decyzji ani działania, problem pozostaje `srednie`.

Powtarzające się wystąpienia można grupować tylko wtedy, gdy jedna wspólna poprawka rzeczywiście naprawia wszystkie i prowadzi do tego samego skutku dla odbiorców. Test zapisuje, czy problem grupuje powtarzające się wystąpienia; jeżeli tak, obie przesłanki grupowania muszą być potwierdzone.

Każdy problem zawiera opis wzorca, powiązane twierdzenia, główną poprawkę i uzasadnienie sposobu grupowania.

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
- **H** ocenia rzeczywistą możliwość zrozumienia tekstu osobno przez każdą istotną grupę odbiorców, a wynik ogólny ustala według reguły z rozdziału 6.5.
- **L** ocenia zgodność języka, szczegółowości i treści z celem oraz miejscem publikacji.

Nie należy obniżać G wyłącznie za trudny, ale poprawny termin. Niewyjaśniony termin obniża H, a przy niespełnionej obietnicy popularyzacji także L.

Jeżeli seria niewyjaśnionych terminów koniecznych do zrozumienia głównej tezy blokuje znaczącą część niespecjalistycznych odbiorców, H nie może przekroczyć 2. Jeżeli bez pomocy eksperta nie da się odtworzyć głównego toku, H nie może przekroczyć 1.

Jeżeli publikacja ma funkcję popularyzatorską, a jej rdzeń wymaga niewskazanej wiedzy specjalistycznej, L nie może przekroczyć 2.

Ten sam brak może wpływać na więcej niż jeden wymiar wyłącznie wtedy, gdy raport opisze odmienny skutek w każdym z nich:

- C odpowiada za poprawność działania technologii, kodu, mechanizmu, narzędzia, danych technicznych albo dostępności centralnego artefaktu, gdy publikacja składa o nim twierdzenie techniczne;
- D odpowiada za jakość, adekwatność i śledzalność podstaw, z których czytelnik ma zweryfikować twierdzenie;
- H odpowiada za możliwość zrozumienia przekazu przez istotne grupy odbiorców, w tym za dostępność sposobu przedstawienia danych, kodu i wykresów.

Brak tekstowego odpowiednika wykresu wpływa na H, jeżeli blokuje zrozumienie danych. Wpływa na D, jeżeli uniemożliwia prześledzenie wartości lub metody. Wpływa na C tylko wtedy, gdy publikacja twierdzi, że artefakt jest technicznie dostępny albo działanie artefaktu jest częścią ocenianej porady. Nie wolno obniżyć wszystkich trzech wymiarów jednym zdaniem „wykres jest niedostępny”.

Jeżeli bariera językowa, terminologiczna albo strukturalna obniża H lub L, uruchamia ograniczenie H≤2, H≤1 lub L≤2 albo wpływa na werdykt, musi zostać zapisana jako problem z własnym `issue_id`. Problem może mieć pustą listę `claim_ids`, jeżeli nie wynika z jednego twierdzenia; wtedy wskazuje lokalizacje, grupy odbiorców i terminy lub elementy struktury tworzące barierę.

Lokalna trudność, która nie zmienia H, L ani werdyktu, może pozostać wyłącznie w profilu językowym i uzasadnieniu wymiaru.

Tego samego zjawiska nie liczy się podwójnie. Jeżeli niepoprawny termin jest już problemem merytorycznym, opis problemu wskazuje osobno skutek dla G oraz skutek dla H lub L.

### 14.2. Kontrola właściwego przedmiotu wymiaru

Przed zamknięciem A–L należy sprawdzić, czy główne uzasadnienie każdego wyniku dotyczy właściwego przedmiotu. Struktura i możliwość prześledzenia tekstu należą do H; poprawność terminów do G; bezpieczeństwo działania do I; doświadczenia i potrzeby użytkowników do J; jawność statusu wiedzy do K; realizacja obietnicy publikacji do L.

Uzasadnienie nie jest wystarczające, jeżeli opiera wynik głównie na cesze należącej do innego wymiaru. Jedna obserwacja może wpływać na kilka wymiarów tylko wtedy, gdy dla każdego zostanie opisany odmienny skutek. Karta oceny i raport wymagają jawnego potwierdzenia tej kontroli dla wszystkich A–L. Walidator sprawdza obecność ustrukturyzowanej kontroli i odmienny skutek przy współdzielonej obserwacji, lecz nie próbuje automatycznie interpretować naturalnego uzasadnienia.

## 15. Sekwencja werdyktu

### Krok 1. Możliwość rozstrzygnięcia

Przed werdyktem należy rozdzielić: brak treści publikacji lub centralnego artefaktu potrzebnego do poznania głównej tezy; brak zewnętrznych dowodów wspierających widoczne twierdzenie; oraz brak części danych pomocniczych. Ustalenie zapisuje się w `decidability_test`.

Brak źródła albo danych wspierających widoczne twierdzenie nie prowadzi automatycznie do `nie_mozna_rozstrzygnac`. Twierdzenie może pozostać nierozstrzygnięte, a D i pokrycie źródłowe mogą zostać obniżone. Werdykt `nie_mozna_rozstrzygnac` stosuje się dopiero wtedy, gdy brak treści publikacji albo centralnego artefaktu uniemożliwia odpowiedzialną ocenę rdzenia jako całości. Brak części danych pomocniczych zapisuje się jako ograniczenie, ale sam nie blokuje werdyktu.

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

Domyślna relacja werdyktu z bezpiecznym poleceniem jest następująca:

- `rzetelny` → `bez_zastrzezen`;
- `rzetelny_z_niewielkimi_zastrzezeniami` → `z_niewielkimi_korektami`;
- `rzetelny_z_istotnymi_zastrzezeniami` → `z_nazwanymi_korektami_lub_zrodlami`;
- `nierzetelny` → `nie_do_praktycznego_uzycia`;
- `nie_mozna_rozstrzygnac` → `nie_mozna_ocenic`.

Odchylenie jest dopuszczalne wyłącznie w kierunku większej ostrożności i wymaga osobnego uzasadnienia. Nie wolno wydać polecenia łagodniejszego niż domyślne dla danego werdyktu.

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
4. profil miejsca, celu i odbiorców wraz z dowodami, sprzecznościami i pewnością;
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

Pełny `wynik.json` musi być zgodny z `wynik.schema.json`. Każdy nowy przebieg kalibracyjny tworzy także kanoniczny `metryka.json` zgodny z `metryka-0.3.schema.json`, a następnie `wyciag-kalibracyjny.json`. Po zamknięciu pary tworzy się `porownanie-pary.json` i raport według wspólnego wzoru. Wartości maszynowe stosują `snake_case` bez polskich znaków, a raport używa naturalnego języka.

`metryka.json` jest jedynym kanonicznym źródłem metadanych przebiegu. Zawiera identyfikatory serii, przypadku i przebiegu; dokładny identyfikator i SHA-256 użytego artefaktu metodologii; czas i język przebiegu; pełną metrykę publikacji; zamrożone materiały wejściowe wraz z sumami i podstawą haszowania; identyfikację oceniającego; środowisko, dostęp, izolację i ograniczenia. Pola wspólne z `wynik.json` muszą być identyczne i są kontrolowane przez walidator.

Metrykę tworzy się i zamraża przed przebiegiem krytycznym. Po jego zakończeniu wolno uzupełnić wyłącznie czas zakończenia oraz ograniczenia ujawnione podczas wykonania; pozostałych danych wejściowych i warunków przebiegu nie wolno przepisywać pod wpływem wyniku.

Opcjonalny `metryka.yaml` może być wyłącznie automatycznie wygenerowaną kopią dla człowieka. Nie jest źródłem kanonicznym i nie wolno utrzymywać go ręcznie niezależnie od JSON. Kontrakt ten obowiązuje nowe serie rozpoczęte po jego wdrożeniu; istniejących przebiegów i ich historycznych plików YAML nie migruje się ani nie waliduje wstecz.

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

### 18.4. Wspólny format porównania pary

Każda para A/B w kalibracji kończy się jednym raportem porównawczym Markdown i jednym plikiem JSON zgodnym ze schematem `porownanie-pary-0.3.schema.json`. Porównanie powstaje dopiero po zamknięciu i walidacji obu przebiegów.

Dopasowanie odbywa się według znaczenia, nie numerów lokalnych. Dopuszczalne relacje to `one_to_one`, `one_to_many`, `many_to_one`, `many_to_many`, `a_only` i `b_only`. Każdy identyfikator twierdzenia i problemu z A oraz B występuje w mapowaniu dokładnie raz.

Porównanie obejmuje: tożsamość wersji materiału i metodologii; profile miejsca i odbiorców; G, H i L dla każdej grupy; wszystkie A–L i `nd`; werdykt i korektę kontrfaktyczną; atomizację twierdzeń; wyniki twierdzeń; grupowanie problemów; znaczenie, centralność i ryzyko; wpisy jednostronne; źródła rozbieżności oraz zbiorcze miary wymagane w rozdziale 18.3.

## 19. Kontrola jakości

Przed zamknięciem analizy należy potwierdzić:

1. pełna treść i centralne materiały zostały pozyskane i oznaczone wersją;
2. autorstwo, wydawca i daty zostały sprawdzone;
3. metodologia została zamrożona przed krytyką;
4. neutralne streszczenie powstało przed weryfikacją;
5. przed oceną G, H i L sprawdzono dostępne elementy miejsca publikacji i zapisano dowody, sprzeczności oraz pewność profilu;
6. zrozumiałość oceniono osobno dla każdej istotnej grupy objętej obietnicą publikacji;
7. mapa obejmuje rdzeń i działania odbiorcy;
8. zastosowano test atomizacji i zapisano uzasadnienia wyjątków;
9. każde twierdzenie ma kompletny ślad od fragmentu publikacji do wyniku;
10. każde źródło faktycznie odczytano;
11. wynik każdego twierdzenia ma uzasadnienie granicy;
12. poprawność historyczną oddzielono od bieżącej użyteczności i ustalono osobny dowód wersji;
13. każda grupa odbiorców przeszła test połączenia albo podziału, a wiedzę konieczną oddzielono od pomocnej;
14. każde `nd` ma prawidłowe uzasadnienie, a stosowalność C i J odpowiada danym ustrukturyzowanym;
15. każdą ocenę porównano z kotwicami sąsiednimi;
16. kontrola przedmiotu potwierdza, że uzasadnienia A–L dotyczą właściwych wymiarów;
17. każdy problem duży i krytyczny ma pełny test centralności i ryzyka;
18. każdy problem średni i duży ma test granicy znaczenia;
19. wymagane problemy mają kontrolę czterech przesłanek krytyczności;
20. w kalibracji każdy problem ma centralność, ryzyko i krótkie uzasadnienie;
21. sposób grupowania problemów został uzasadniony;
22. test rozstrzygalności poprzedził werdykt, a werdykt przeszedł test korekty;
23. pewność mapy, werdyktu i pokrycie źródłowe zapisano osobno;
24. dane strukturalne przeszły walidację;
25. w kalibracji para ma kompletne mapowanie semantyczne twierdzeń i problemów;
26. raport nie przechowuje pełnej kopii chronionej publikacji bez podstawy;
27. wynik nie został dostrojony do wcześniejszych przypadków.

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
