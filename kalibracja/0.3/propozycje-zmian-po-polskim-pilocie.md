# Propozycje zmian po polskim pilotażu 0.3

**Data:** 14 września 2026 r.  
**Status:** dokument historyczny po polskim pilotażu i B1; T1–T2 oraz S1–S15 wdrożone; B1 zakończone; B2 nie rozpoczęte
**Podstawa:** pięć polskich publikacji, po dwa odizolowane przebiegi A/B

> **Dokument historyczny — aktualny stan 14 września 2026 r.:** S1–S15
> zostały zatwierdzone i wdrożone, a B1 wykonano i zakończono
> proceduralnie. Publiczne wyniki zbiorcze znajdują się w
> [`wyniki-B1.md`](wyniki-B1.md). T1 formalizuje to zamknięcie, a T2 wzmacnia
> techniczny dowód wersji historycznej. S11–S15 są prospektywnymi
> doprecyzowaniami wynikającymi z B1. Wyników pilotażu ani B1 nie przeliczono
> wstecz. B2 nie zostało rozpoczęte.

## 1. Najważniejsza rekomendacja

Zmiany S1–S10 zostały zatwierdzone i wdrożone bez przebudowy celu metodologii. S10 ustanowiło osobny kontrakt techniczny dla nowych serii. B1 zostało wykonane według osobno zatwierdzonego protokołu i zakończone proceduralnie. T1–T2 wdrażają bezpieczne zamknięcie dokumentacji B1 i techniczne uszczelnienie dowodu historycznego. S11–S15 doprecyzowują ujawnione w B1 granice decyzji bez zmiany pięciu werdyktów, obniżenia progu krytyczności ani wprowadzenia sumy A–L. B2 pozostaje niewykonanym badaniem wymagającym osobnego protokołu i decyzji.

| ID | Rodzaj | Rekomendacja | Główny obszar |
| --- | --- | --- | --- |
| S1 | znaczeniowa | przyjąć | atomizacja twierdzeń |
| S2 | znaczeniowa | przyjąć | wyniki dopasowań twierdzeń |
| S3 | znaczeniowa | przyjąć | grupowanie i znaczenie problemów |
| S4 | znaczeniowa | przyjąć | granice H |
| S5 | znaczeniowa i strukturalna | przyjąć | L według grup |
| S6 | znaczeniowa | przyjąć | profil i pewność odbiorców |
| S7 | znaczeniowa i strukturalna | przyjąć | językowa bariera jako problem |
| S8 | znaczeniowa | przyjąć | werdykt i bezpieczne polecenie |
| S9 | znaczeniowa | przyjąć po korekcie — wdrożono | wersja historyczna publikacji |
| S10 | strukturalna | przyjąć po korekcie — wdrożono | jednolita metryka przebiegu |
| B1 | badawcza | wykonano i zakończono | pokrycie nieprzetestowanych progów |
| T1 | techniczna | wdrożono po B1 | bezpieczne zamknięcie dokumentacji B1 |
| T2 | techniczna | wdrożono po B1 | dowód rekonstrukcji wersji historycznej |
| S11 | znaczeniowa i strukturalna | wdrożono po B1 | granice C, J i `nd` |
| S12 | znaczeniowa i strukturalna | wdrożono po B1 | granica problemu średniego i dużego |
| S13 | znaczeniowa i strukturalna | wdrożono po B1 | właściwy przedmiot wymiarów A–L |
| S14 | znaczeniowa i strukturalna | wdrożono po B1 | rozstrzygalność i przesłanki krytyczności |
| S15 | znaczeniowa i strukturalna | wdrożono po B1 | jednolite grupy odbiorców |
| B2 | badawcza | nie rozpoczęto | przenośność między oceniającymi |

## S1. Operacyjne przykłady atomizacji

**Proponowane brzmienie** — po § 8.4 standardu:

> Granicę wpisu ustala się według najmniejszego fragmentu, który zachowuje pełny warunek, zakres i skutek, a zarazem może otrzymać jeden wynik. Nie wolno łączyć poprawnego rdzenia z wadliwym absolutem tylko dlatego, że występują w jednym zdaniu. Nie wolno też rozdzielić kwantyfikatora, wyjątku, przeczenia albo statusu prawnego od części, którą ogranicza.
>
> Przykłady:
>
> 1. „Narzędzie wykrywa część błędów, dlatego gwarantuje zgodność” tworzy co najmniej dwa wpisy: opis wykrywania oraz wniosek o gwarancji.
> 2. „Każdy podmiot musi stosować X, z wyjątkiem Y” tworzy osobne wpisy tylko wtedy, gdy każdy zachowuje informację o właściwym zakresie i wyjątku.
> 3. Wyliczenie kilku wymagań tworzy osobne wpisy, jeżeli mają różne podstawy lub mogą otrzymać różne wyniki; wspólny warunek należy powtórzyć.
> 4. Jedna procedura kodowa pozostaje jednym wpisem, jeżeli jej kroki działają wyłącznie łącznie; niezależny błędny krok tworzy osobny wpis.
>
> W kalibracji `atomization_rationale` musi wskazać zastosowany przykład albo wyjaśnić, dlaczego przypadek jest inny.

**Prosto:** rozdzielamy zdanie tam, gdzie jedna część może być poprawna, a druga błędna, lecz nigdy nie gubimy warunku „kiedy”, „dla kogo”, „zawsze” albo „z wyjątkiem”.

**Problem z pilota:** mapy miały od 23 do 57 twierdzeń; A utworzyło 196 wpisów, B 168. Wystąpiły 23 relacje złożone i 34 wpisy jednostronne.

**Przykład prawidłowy:** osobno ocenić fakt, że test wykrywa błędy, oraz fałszywy wniosek, że zapewnia pełną zgodność.  
**Przykład błędny:** nadać całemu zdaniu `czesciowo_zgodne`, ukrywając fałszywy absolut.

**Wpływ:** bezpośrednio mapa twierdzeń; pośrednio A, B, C, E, F, G, I i K. Nie zmienia definicji wyniku, tylko zmniejsza dowolność granic wpisu.

**Ryzyko skutków ubocznych:** zbyt mechaniczne stosowanie może nadmiernie rozdrobnić tekst i wydłużyć analizę. Ogranicza to zasada zachowania znaczenia zależnego.

**Pliki:** `metodologia/0.3/standard.md`, `skill/references/standard-0.3.md`, `szablony/0.3/karta-oceny.md`, `skill/references/karta-oceny-0.3.md`, `skill/SKILL.md`, testy regresyjne.

## S2. Jednoznaczne znaczenie `exact`, `adjacent`, `different` i `not_comparable`

**Proponowane brzmienie** — po § 8.6 standardu:

> Dla relacji 1:1 wynik dopasowania ustala się następująco:
>
> - `exact` — oba twierdzenia mają tę samą etykietę wyniku;
> - `adjacent` — etykiety tworzą jedną z par: `zgodne`–`zasadniczo_zgodne`, `zasadniczo_zgodne`–`czesciowo_zgodne`, `czesciowo_zgodne`–`mylace` albo `mylace`–`niezgodne`;
> - `different` — oba wyniki są rozstrzygnięciami merytorycznymi, lecz nie są identyczne ani sąsiednie;
> - `not_comparable` — co najmniej jeden wynik to `nieweryfikowalne` lub `nierozstrzygniete`, albo wpisy mimo wspólnego tematu nie oceniają tego samego zakresu.
>
> `nieweryfikowalne` i `nierozstrzygniete` są `exact` wyłącznie wtedy, gdy obie strony mają tę samą z tych etykiet i ten sam przedmiot rozstrzygnięcia.
>
> W relacji złożonej najpierw porównuje się najmniejsze wspólne składowe semantyczne. Cała relacja jest `exact`, gdy wszystkie składowe są dokładnie zgodne; `adjacent`, gdy żadna nie jest `different` ani `not_comparable`, a co najmniej jedna jest sąsiednia; `different`, gdy co najmniej jedna materialna składowa jest różna; w pozostałych przypadkach `not_comparable`. Raport zapisuje liczbę składowych każdego rodzaju.

**Prosto:** etykiety porównania przestają zależeć od intuicji osoby agregującej.

**Problem z pilota:** 38/126 par 1:1 oznaczono jako sąsiednie, 5 jako różne i 5 jako nieporównywalne, ale projekt nie definiował pełnej granicy między tymi wartościami ani relacji złożonych.

**Przykład prawidłowy:** `zasadniczo_zgodne` kontra `czesciowo_zgodne` = `adjacent`.  
**Przykład błędny:** `zgodne` kontra `czesciowo_zgodne` = `adjacent` tylko dlatego, że różnica wydaje się mała.

**Wpływ:** porównywanie wyników twierdzeń i metryki kalibracji; bez wpływu na pojedyncze oceny A–L.

**Ryzyko skutków ubocznych:** porządek etykiet upraszcza niektóre przypadki jakościowe. Dlatego wyniki dowodowe pozostają poza liniową skalą, a relacje złożone wymagają rozpisania składowych.

**Pliki:** `metodologia/0.3/standard.md`, `skill/references/standard-0.3.md`, `szablony/0.3/wzor-porownania.md`, `skill/references/wzor-porownania-0.3.md`, oba pliki `porownanie-pary-0.3.schema.json`, `skill/scripts/validate_0_3.py`, testy regresyjne.

## S3. Grupowanie problemów i granica `duze`–`srednie`

**Proponowane brzmienie** — zastąpienie końca § 13.5 i dodanie kotwicy:

> Twierdzenia wolno połączyć w jeden problem tylko wtedy, gdy łącznie spełniają cztery warunki: mają wspólną przyczynę, wymagają jednej zasadniczej korekty, mają ten sam poziom centralności oraz mają ten sam poziom ryzyka zastosowania. Różnica któregokolwiek z tych elementów wymaga osobnych problemów.
>
> Brak źródła, błąd merytoryczny, niejasny status normatywny i bariera zrozumienia nie są automatycznie jednym problemem, nawet gdy dotyczą tego samego akapitu. Można je połączyć tylko wtedy, gdy jedna korekta rzeczywiście usuwa wszystkie skutki.
>
> Problem jest `duze`, gdy minimalna uczciwa naprawa zmienia ważne zalecenie, zakres ważnego wniosku albo sposób działania istotnej grupy. Jest `srednie`, gdy naprawa pozostawia ten sam ważny wniosek i sposób działania, ale usuwa materialną nieścisłość lub lokalne ryzyko. Duża liczba drobnych wystąpień sama nie tworzy problemu dużego; może go tworzyć wspólny wzorzec, jeżeli łącznie zmienia odbiór lub działanie.

**Prosto:** jeden problem może obejmować wiele miejsc tylko wtedy, gdy ma jedną przyczynę, jedną poprawkę i tę samą wagę.

**Problem z pilota:** liczba problemów wynosiła 5–10, dokładna zgodność ich znaczenia tylko 16/27 (59,3%), a A znalazło 12 problemów dużych wobec 7 w B.

**Przykład prawidłowy:** trzy wystąpienia tego samego błędnego absolutu, naprawiane tym samym zastrzeżeniem, jako jeden problem.  
**Przykład błędny:** połączenie braku źródła i niebezpiecznej instrukcji technicznej tylko dlatego, że występują w tej samej sekcji.

**Wpływ:** severity, centralność, ryzyko, werdykt i pośrednio A–L.

**Ryzyko skutków ubocznych:** może zwiększyć liczbę problemów. Metodologia musi nadal przypominać, że liczba problemów nie jest wynikiem jakości.

**Pliki:** `metodologia/0.3/standard.md`, `skill/references/standard-0.3.md`, `metodologia/0.3/kotwice.md`, `skill/references/kotwice-0.3.md`, oba wzory raportu 0.3, `skill/SKILL.md`, testy regresyjne.

## S4. Granice H dla grup niespecjalistycznych i mieszanych

**Proponowane brzmienie** — uzupełnienie kotwicy H:

> H=4 wymaga, aby grupa samodzielnie odtworzyła główną tezę, przesłanki i bezpieczny sposób użycia bez istotnego dopowiedzenia zewnętrznego.
>
> H=3 stosuje się, gdy grupa rozumie główną tezę i praktyczny rdzeń, a potrzebne dopowiedzenia są lokalne, łatwo wskazywalne i nie zmieniają decyzji ani działania.
>
> H=2 stosuje się, gdy główna teza jest odtwarzalna, lecz bez wiedzy niewskazanej w profilu grupa nie odtworzy co najmniej jednego ważnego warunku, kroku, ograniczenia lub skutku potrzebnego do bezpiecznego zastosowania.
>
> H=1 stosuje się, gdy bez pomocy eksperta grupa nie odtworzy głównego toku, pomyli centralne pojęcia albo nie będzie w stanie odróżnić zalecanego działania od działania ryzykownego.
>
> Pojedynczy krok wymagający CMS, inspektora, kodu albo wiedzy prawnej obniża H do 2 tylko wtedy, gdy jest konieczny dla obiecanego rezultatu tej grupy. Jeżeli jest jawnie opcjonalny albo skierowany do innej, nazwanej grupy, wpływa na opis ograniczeń, nie na H tej grupy.

**Prosto:** H=3 oznacza „rozumiem i umiem bezpiecznie użyć rdzenia”, a H=2 „rozumiem ogólną myśl, lecz brakuje mi ważnego elementu do działania”.

**Problem z pilota:** H było identyczne tylko w 2/5 par. Rozbieżności dotyczyły właśnie tego, czy lokalna wiedza techniczna lub prawna blokuje rdzeń.

**Przykład prawidłowy:** laik rozumie checklistę, lecz obowiązkowy test błysków wymaga niepodanego narzędzia — H=2, jeśli publikacja obiecuje samodzielne sprawdzenie.  
**Przykład błędny:** H=4 dlatego, że ekspert wie, jak wykonać brakujący krok.

**Wpływ:** przede wszystkim H; pośrednio L oraz rejestr problemów językowych.

**Ryzyko skutków ubocznych:** może mieszać zrozumiałość z techniczną poprawnością C lub bezpieczeństwem I. Ogranicza to wymóg, aby H opisywało barierę poznawczą, C działanie mechanizmu, a I skutek zastosowania.

**Pliki:** `metodologia/0.3/kotwice.md`, `skill/references/kotwice-0.3.md`, `metodologia/0.3/standard.md`, `skill/references/standard-0.3.md`, oba wzory raportu 0.3, `skill/SKILL.md`, testy regresyjne.

## S5. Rzeczywista ocena L osobno dla istotnych grup

**Proponowane brzmienie** — uzupełnienie § 6.5 i kotwicy L:

> Dla każdej istotnej grupy objętej obietnicą publikacji zapisuje się także `group_l_score` od 0 do 4. Ocena odpowiada na pytanie, czy publikacja realizuje wobec tej grupy deklarowany cel i obiecany sposób użycia; nie jest kopią ogólnego L.
>
> Ogólne L odpowiada najniższej ocenie L wśród istotnych grup objętych obietnicą publikacji. Grupy nieobjęte obietnicą mogą być opisane, lecz nie obniżają ogólnego L.
>
> Jeżeli ten sam brak dotyczy wyłącznie zrozumiałości, obniża H. Obniża również L tylko wtedy, gdy przez ten brak publikacja nie realizuje zadeklarowanej funkcji wobec danej grupy.

**Prosto:** osobno sprawdzamy, czy tekst spełnia obietnicę wobec każdej ważnej grupy, a nie wpisujemy wszystkim grupom tej samej ogólnej liczby.

**Problem z pilota:** porównanie przewidywało grupowe L, lecz wyniki go nie przechowywały. W części par powtórzono ogólne L, a w innych pole pozostawiono puste. Nie dało się uczciwie policzyć zgodności grupowego L.

**Przykład prawidłowy:** poradnik spełnia obietnicę wobec redaktorów (L=4), ale nie wobec jawnie objętych właścicieli małych firm (L=2); ogólne L=2.  
**Przykład błędny:** przepisać ogólne L=3 do każdej grupy bez osobnej oceny.

**Wpływ:** bezpośrednio L oraz profil grup; możliwy pośredni wpływ na werdykt, gdy niespełniona obietnica jest problemem dużym.

**Ryzyko skutków ubocznych:** zasada minimum może nadmiernie podporządkować wynik grupie opisanej bardzo szeroko. Ogranicza to istniejący test istotności i objęcia obietnicą oraz obowiązek uzasadnienia zakresu grupy.

**Pliki:** standard i kotwice 0.3 wraz z kopiami skilla; `wynik.schema.json`, `wyciag-kalibracyjny.schema.json` i ich kopie; oba wzory raportu i wzór porównania wraz z kopiami; `porownanie-pary-0.3.schema.json` i kopia; walidator; `skill/SKILL.md`; testy regresyjne.

## S6. Progi profilu, pewności i wiedzy wymaganej

**Proponowane brzmienie** — zastąpienie akapitu o pewności w § 6.4:

> Profil jest `ustalony`, gdy dowody rangi 1 lub 2 pozwalają określić istotne grupy i nie pozostaje sprzeczność mogąca zmienić H lub L. Jest `czesciowo_ustalony`, gdy główna grupa jest znana, lecz co najmniej jedna istotna grupa, wymagany poziom wiedzy albo zakres obietnicy pozostaje sporny i może zmienić H lub L. Jest `nieustalony_wiarygodnie`, gdy brak podstaw do wyboru między co najmniej dwoma rozsądnymi profilami prowadzącymi do różnych H lub L.
>
> Pewność `wysoka` wymaga bezpośredniego dowodu odpowiedniej rangi dla grup i zakresu konkretnego artykułu oraz braku materialnej sprzeczności. Pewność `srednia` stosuje się przy zgodnych dowodach pośrednich albo gdy deklaracja miejsca wymaga doprecyzowania przez artykuł. Pewność `niska` stosuje się przy samych wskazówkach z tekstu, sprzecznych dowodach albo profilu nieustalonym wiarygodnie.
>
> „Wiedza rzeczywiście potrzebna” obejmuje tylko wiedzę konieczną do odtworzenia głównej tezy, ważnego warunku albo obiecanego działania. Wiedzę pomocną, lecz niekonieczną, zapisuje się osobno jako ułatwiającą. Każdy element wiedzy koniecznej wskazuje fragment publikacji, który bez niej staje się nieodtwarzalny lub ryzykowny.

**Prosto:** wysoka pewność nie oznacza tylko „wiemy, kto czyta”, lecz także „wiemy, co ta grupa powinna już umieć”.

**Problem z pilota:** rodzaj miejsca i główni odbiorcy zgadzali się 5/5, ale wymagana wiedza i pewność profilu tylko 2/5.

**Przykład prawidłowy:** profil `czesciowo_ustalony`, gdy serwis wskazuje przedsiębiorców, ale nie wiadomo, czy artykuł zakłada obsługę kodu, a to zmienia H.  
**Przykład błędny:** pewność wysoka wyłącznie dlatego, że strona „O nas” wymienia szeroką grupę.

**Wpływ:** profil, pewność, H i L; pośrednio G, jeśli znaczenie terminu zależy od zakładanej wiedzy.

**Ryzyko skutków ubocznych:** więcej profili może otrzymać średnią pewność. Jest to zamierzona ostrożność, lecz wymaga krótkich pól dowodowych, aby nie rozbudować nadmiernie raportu.

**Pliki:** `metodologia/0.3/standard.md`, kopia skilla, oba wzory raportu, karta oceny i ich kopie, `wynik.schema.json` i kopia, walidator, testy regresyjne.

## S7. Bariera językowa obniżająca H lub L jako jawny problem

**Proponowane brzmienie** — po § 14.1 standardu:

> Jeżeli bariera językowa, terminologiczna albo strukturalna obniża H lub L, uruchamia ograniczenie H≤2, H≤1 lub L≤2 albo wpływa na werdykt, musi zostać zapisana jako problem z własnym `issue_id`. Problem może mieć pustą listę `claim_ids`, jeżeli nie wynika z jednego twierdzenia; wtedy wskazuje lokalizacje, grupy odbiorców i terminy lub elementy struktury tworzące barierę.
>
> Lokalna trudność, która nie zmienia H, L ani werdyktu, może pozostać wyłącznie w profilu językowym i uzasadnieniu wymiaru.
>
> Tego samego zjawiska nie liczy się podwójnie. Jeżeli niepoprawny termin jest już problemem merytorycznym, opis problemu wskazuje osobno skutek dla G oraz skutek dla H lub L.

**Prosto:** jeśli język realnie obniża ocenę, ślad problemu nie może zniknąć między profilem odbiorcy a werdyktem.

**Problem z pilota:** w jednym przebiegu przypadek językowy pozostawał tylko w profilu i H/L, a w drugim otrzymywał osobny problem. Utrudniało to porównanie list problemów.

**Przykład prawidłowy:** seria niewyjaśnionych skrótów blokująca niespecjalistów ma jeden problem powiązany z grupą i lokalizacjami.  
**Przykład błędny:** tworzyć osobny problem dla każdego trudnego słowa, mimo że żadne nie wpływa na wynik.

**Wpływ:** H, L, czasem G; lista problemów, grupowanie, centralność i werdykt.

**Ryzyko skutków ubocznych:** podwójne liczenie lub mnożenie drobnych problemów. Zapobiega temu próg wpływu na wynik i zakaz dublowania skutku.

**Pliki:** standard i kotwice 0.3 wraz z kopiami; oba wzory raportu i karta oceny wraz z kopiami; `wynik.schema.json`, `wyciag-kalibracyjny.schema.json` i kopie; walidator; `skill/SKILL.md`; testy regresyjne.

## S8. Związek werdyktu z bezpiecznym poleceniem

**Proponowane brzmienie** — po tabeli werdyktów:

> Domyślna relacja jest następująca:
>
> - `rzetelny` → `bez_zastrzezen`;
> - `rzetelny_z_niewielkimi_zastrzezeniami` → `z_niewielkimi_korektami`;
> - `rzetelny_z_istotnymi_zastrzezeniami` → `z_nazwanymi_korektami_lub_zrodlami`;
> - `nierzetelny` → `nie_do_praktycznego_uzycia`;
> - `nie_mozna_rozstrzygnac` → `nie_mozna_ocenic`.
>
> Odchylenie jest dopuszczalne wyłącznie w kierunku większej ostrożności i wymaga osobnego uzasadnienia. Nie wolno wydać polecenia łagodniejszego niż domyślne dla danego werdyktu.

**Prosto:** końcowa etykieta i praktyczne zalecenie nie mogą sobie przeczyć.

**Problem z pilota:** wszystkie przebiegi były zgodne, ale walidator nie może egzekwować tej zgodności, bo standard nie zapisuje wiążącej relacji.

**Przykład prawidłowy:** istotne zastrzeżenia → używać dopiero z nazwanymi korektami.  
**Przykład błędny:** istotne zastrzeżenia → bez zastrzeżeń.

**Wpływ:** werdykt i `safe_recommendation`; bez bezpośredniego wpływu na A–L.

**Ryzyko skutków ubocznych:** wyjątkowy tekst może wymagać ostrożniejszego polecenia niż sugeruje werdykt. Propozycja to dopuszcza, lecz zakazuje kierunku mniej ostrożnego.

**Pliki:** `metodologia/0.3/standard.md`, kopia skilla, oba wzory raportu, `wynik.schema.json` i kopia, walidator, testy regresyjne.

## S9. Rekonstrukcja wersji historycznej bez migawki

**Zatwierdzone brzmienie** — uzupełnienie § 11:

> Bieżącą treścią jest treść rzeczywiście pozyskana w dniu dostępu. Można ją oceniać pod względem bieżącej użyteczności, lecz nie wolno przypisywać jej wcześniejszej dacie bez osobnego dowodu wersji.
>
> Wersję historyczną uznaje się za odtworzoną tylko wtedy, gdy dowód zachowuje rzeczywistą treść, identyfikuje datę lub wersję, obejmuje zakres potrzebny do oceny oraz ma stabilny i sprawdzalny identyfikator. Sama data publikacji lub aktualizacji, bieżąca suma kontrolna, niezmieniony URL, wynik wyszukiwania, pamięć podręczna, opis zmiany albo brak oznaczenia aktualizacji nie dowodzą dawnej treści.
>
> Gdy warunki rekonstrukcji nie są spełnione, `historical_version_reconstructable` ma wartość `false`, oceniana wersja ma wartość `not_reconstructable`, poprawność historyczna pozostaje `nierozstrzygniete`, a jej pewność jest niska. Odtworzona wersja wymaga co najmniej jednego dowodu zachowującego treść i oznaczonego `immutable: tak`.
>
> Przeskalowanie, zmiana kodowania lub techniczna rekompresja nie tworzą innej wersji znaczeniowej tylko wtedy, gdy zachowano całą treść, kolejność, znaczenie i czytelność; transformację i podstawę równoważności trzeba udokumentować.

**Prosto:** bez zachowanej starej kopii nie zgadujemy, co dokładnie było na stronie w dniu publikacji.

**Problem z pilota:** w kilku parach różnie rozstrzygnięto możliwość odtworzenia wersji pierwotnej mimo pracy na tym samym bieżącym materiale.

**Przykład prawidłowy:** brak archiwum → historia nierozstrzygnięta, bieżąca wersja oceniona osobno.  
**Przykład błędny:** uznać dzisiejszą treść za identyczną z pierwotną tylko dlatego, że URL się nie zmienił.

**Wpływ:** ocena temporalna, pewność, A–F i K zależnie od rodzaju twierdzenia; nie musi zmieniać oceny bieżącej.

**Ryzyko skutków ubocznych:** więcej ocen historycznych będzie nierozstrzygniętych. To uczciwy skutek braku dowodów, ale może zmniejszyć użyteczność analiz dawnych stron.

**Pliki:** standard 0.3 i kopia, oba wzory raportu, karta oceny i kopie, `wynik.schema.json` i kopia, walidator, testy regresyjne.

## S10. Kanoniczna metryka przebiegu

**Zatwierdzone brzmienie technicznego kontraktu:**

> Każdy nowy przebieg kalibracyjny zawiera kanoniczny `metryka.json` zgodny z `metryka-0.3.schema.json`. Metryka zapisuje identyfikatory analizy, serii, przypadku i przebiegu; metodologię wraz z SHA-256 użytej paczki; czas i język przebiegu; publikację; zamrożone materiały wraz z ich SHA-256 i podstawą haszowania; identyfikację oceniającego; środowisko, dostęp, izolację i ograniczenia.
>
> JSON jest jedynym źródłem kanonicznym. YAML może być wyłącznie automatycznie wygenerowaną kopią dla człowieka. Nieznane dane bibliograficzne zapisuje się jako `null`, niedostępne dane środowiskowe jako `not_available`, a niedotyczące jako `not_applicable`. Obowiązkowych pól nie wolno pomijać ani zastępować pustym tekstem.
>
> Walidator sprawdza metrykę oraz zgodność jej wspólnych pól z `wynik.json`. Starych przebiegów i historycznych plików YAML nie migruje się ani nie waliduje wstecz. Kontrakt obowiązuje przyszłe serie i musi być stosowany przed rozpoczęciem B1 lub B2.

**Prosto:** jedna maszynowa metryka zastępuje kilka różnych układów YAML.

**Problem z pilota:** 6/10 plików YAML nie miało `schema_version`, układy pól były różne, a brak wydawcy zapisano początkowo na dwa sposoby.

**Przykład prawidłowy:** `publisher: null` zgodne ze schematem.  
**Przykład błędny:** raz `not_available`, raz pusty tekst, raz brak pola.

**Wpływ:** wyłącznie struktura i odtwarzalność przebiegu; bez wpływu na znaczenie A–L.

**Ryzyko skutków ubocznych:** migracja narzędzi i dodatkowy plik. Nie należy zmieniać starych przebiegów; nowy kontrakt obowiązywałby dopiero przyszłe serie.

**Pliki:** nowy `metodologia/0.3/metryka-0.3.schema.json` i kopia skilla; standard i dokumentacja 0.3; schematy wyniku i wyciągu wraz z kopiami; `skill/SKILL.md`; karta oceny i wzór raportu wraz z kopiami; walidator i testy regresyjne. Skrypt budowy pakietu nie wymaga zmiany, ponieważ automatycznie kopiuje cały katalog `skill`.

## S11–S15. Doprecyzowania zatwierdzone po B1

Poniższe decyzje obowiązują prospektywnie. Nie przeliczają wyników polskiego
pilotażu ani B1.

- **S11 — granice C, J i `nd`:** C jest liczbowe tylko dla własnego twierdzenia
  autora o działaniu technologii, mechanizmu, narzędzia, testu lub rozwiązania.
  J jest liczbowe, gdy tekst przedstawia, wykorzystuje lub uogólnia perspektywę
  użytkowników albo składa obietnicę, która jej wymaga. Sama podstawa prawna,
  beneficjenci regulacji lub cudza lista oczekiwań nie wystarczają. Szeroka
  obietnica kompletnego poradnika może jednak uczynić perspektywę użytkowników
  wymaganą.
- **S12 — granica `srednie`–`duze`:** zapisuje się istotną grupę odbiorców,
  minimalną uczciwą poprawkę oraz działanie lub wniosek przed i po poprawce.
  Problem jest `duze` tylko wtedy, gdy poprawka zmienia ważną decyzję, zakres
  lub sposób działania co najmniej jednej istotnej grupy. Grupowanie powtórzeń
  wymaga jednej wspólnej poprawki i tego samego skutku.
- **S13 — właściwy przedmiot wymiaru:** przed zamknięciem A–L sprawdza się, czy
  główne uzasadnienie dotyczy właściwego przedmiotu. Wspólna obserwacja może
  wpływać na kilka wymiarów tylko po opisaniu odrębnego skutku dla każdego.
  Walidator kontroluje strukturę tego zapisu, lecz nie udaje wiarygodnej
  interpretacji całego uzasadnienia naturalnego.
- **S14 — rozstrzygalność i krytyczność:** oddziela się brak rdzenia publikacji,
  brak zewnętrznego dowodu widocznego twierdzenia i brak danych pomocniczych.
  `nie_mozna_rozstrzygnac` wymaga braku uniemożliwiającego ocenę rdzenia jako
  całości. Problem duży o wysokim ryzyku lub bezpośrednio wykonalna instrukcja
  o możliwych poważnych skutkach uruchamia jawny test czterech przesłanek;
  krytyczność nadal wymaga spełnienia wszystkich czterech.
- **S15 — grupy odbiorców:** role łączy się, gdy tekst składa tę samą obietnicę,
  wymaga tej samej wiedzy i prowadzi do tego samego zadania. Rozdzielenie wymaga
  różnicy mogącej zmienić H lub L. Każdy element wiedzy koniecznej wskazuje
  konkretny fragment, warunek lub działanie, którego bez niej nie da się
  odtworzyć; wiedza jedynie pomocna nie obniża H.

Zmiany objęły standard, kotwice, schematy wyniku, wyciągu i porównania pary,
wszystkie szablony 0.3, instrukcję i kopie pakietu skill, walidator oraz testy
regresyjne.

## B1. Osobny pilotaż progów nieobecnych w pierwszej serii

> **Stan po wykonaniu:** B1 zakończono proceduralnie 14 września 2026 r.
> Wykonano 32 niezależne oceny i 16 porównań A/B. R3 nie uruchomiono.
> Poniższy tekst zachowuje historyczne uzasadnienie decyzji o rozpoczęciu
> badania; aktualne wyniki zawiera [`wyniki-B1.md`](wyniki-B1.md).

**Proponowane brzmienie protokołu badawczego:**

> Przed zamrożeniem 0.3 należy przeprowadzić kontrolowany test przypadków sondujących co najmniej: `rzetelny`, `rzetelny_z_niewielkimi_zastrzezeniami`, `nierzetelny`, `nie_mozna_rozstrzygnac`, prawidłowe `nd` w co najmniej dwóch wymiarach oraz problem potencjalnie krytyczny. Dobór ma testować granice, ale nie może nakazywać oceniającym oczekiwanego wyniku. Nieudane trafienie w planowaną kategorię jest wynikiem badania, nie podstawą do poprawiania oceny.

**Prosto:** obecny pilot pokazał powtarzalność jednej kategorii, więc potrzebny jest osobny test pozostałych progów.

**Problem z pilota:** wszystkie 10 przebiegów zakończyło się tym samym werdyktem; nie wystąpiły `nd`, problem krytyczny ani brak rozstrzygnięcia.

**Ryzyko skutków ubocznych:** dobór pod progi może sztucznie wzbogacić korpus. Dlatego kandydatury mają sondować granice, a nie mieć z góry przypisany wynik.

**Pliki:** nowy protokół w `kalibracja/0.3/`; bez zmiany standardu, kotwic i schematów przed wynikami testu.

## B2. Test przenośności

**Proponowane brzmienie protokołu badawczego:**

> Co najmniej jedna przyszła seria powinna zostać wykonana przez inny system albo niezależnego oceniającego, bez dostępu do bieżących wyników. Porównanie podaje osobno powtarzalność wewnątrz jednego typu systemu i przenośność między typami oceniających.

**Prosto:** dwa odizolowane przebiegi tego samego rodzaju AI nie wystarczą, aby stwierdzić, że metoda działa tak samo dla innych oceniających.

**Problem z pilota:** wszystkie przebiegi pochodziły z jednej rodziny systemu; często nie dało się zapisać dokładnej migawki modelu i ustawienia rozumowania.

**Ryzyko skutków ubocznych:** wyniki mogą być mniej zgodne, lecz właśnie tę zależność test ma ujawnić.

**Pliki:** nowy protokół w `kalibracja/0.3/`; ewentualne zmiany standardu dopiero po analizie testu.

## 2. Granica decyzji

Po decyzjach z 14 września 2026 r.:

- S1–S15 są zatwierdzone i zostały wdrożone w odpowiednich materiałach projektu 0.3;
- B1 zostało zakończone proceduralnie, a R3 nie uruchomiono;
- T1–T2 zostały zatwierdzone i wdrożone po analizie B1;
- S11–S15 obowiązują prospektywnie i nie zmieniają historycznych wyników B1;
- B2 nie zostało rozpoczęte;
- nie wolno przeliczać wstecz wyników polskiego pilota;
- PR nr 8 pozostaje niescalonym projektem, bez znacznika i wydania 0.3.

## 3. Dokładna macierz plików do przyszłej zmiany

Poniższa lista rozwija skróty „kopia skilla” i „wzory” użyte powyżej. Pliki zostaną zmienione tylko dla zatwierdzonych propozycji.

| Propozycja | Dokładne pliki |
| --- | --- |
| S1 | `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; `szablony/0.3/karta-oceny.md`; `skill/references/karta-oceny-0.3.md`; `skill/SKILL.md`; `tests/test_0_3_package.py`; `tests/test_validate_0_3.py` |
| S2 | `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; `szablony/0.3/wzor-porownania.md`; `skill/references/wzor-porownania-0.3.md`; `metodologia/0.3/porownanie-pary-0.3.schema.json`; `skill/references/porownanie-pary-0.3.schema.json`; `skill/scripts/validate_0_3.py`; `tests/test_validate_0_3.py`; `tests/test_0_3_package.py` |
| S3 | `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; `metodologia/0.3/kotwice.md`; `skill/references/kotwice-0.3.md`; `szablony/0.3/wzor-raportu.md`; `skill/references/wzor-raportu-0.3.md`; `szablony/0.3/karta-oceny.md`; `skill/references/karta-oceny-0.3.md`; `skill/SKILL.md`; oba pliki testów 0.3 |
| S4 | `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; `metodologia/0.3/kotwice.md`; `skill/references/kotwice-0.3.md`; `szablony/0.3/wzor-raportu.md`; `skill/references/wzor-raportu-0.3.md`; `szablony/0.3/karta-oceny.md`; `skill/references/karta-oceny-0.3.md`; `skill/SKILL.md`; oba pliki testów 0.3 |
| S5 | standard i kotwice 0.3 oraz ich kopie skilla; wszystkie trzy szablony 0.3 i ich kopie skilla; wszystkie trzy schematy JSON 0.3 i ich kopie skilla; `skill/scripts/validate_0_3.py`; `skill/SKILL.md`; oba pliki testów 0.3 |
| S6 | `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; `szablony/0.3/wzor-raportu.md`; `skill/references/wzor-raportu-0.3.md`; `szablony/0.3/karta-oceny.md`; `skill/references/karta-oceny-0.3.md`; `metodologia/0.3/wynik.schema.json`; `skill/references/wynik-0.3.schema.json`; `skill/scripts/validate_0_3.py`; oba pliki testów 0.3 |
| S7 | standard i kotwice 0.3 oraz ich kopie skilla; `szablony/0.3/wzor-raportu.md`; `skill/references/wzor-raportu-0.3.md`; `szablony/0.3/karta-oceny.md`; `skill/references/karta-oceny-0.3.md`; `metodologia/0.3/wynik.schema.json`; `skill/references/wynik-0.3.schema.json`; `metodologia/0.3/wyciag-kalibracyjny.schema.json`; `skill/references/wyciag-kalibracyjny-0.3.schema.json`; `skill/scripts/validate_0_3.py`; `skill/SKILL.md`; oba pliki testów 0.3 |
| S8 | `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; `szablony/0.3/wzor-raportu.md`; `skill/references/wzor-raportu-0.3.md`; `metodologia/0.3/wynik.schema.json`; `skill/references/wynik-0.3.schema.json`; `skill/scripts/validate_0_3.py`; oba pliki testów 0.3 |
| S9 | `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; `szablony/0.3/wzor-raportu.md`; `skill/references/wzor-raportu-0.3.md`; `szablony/0.3/karta-oceny.md`; `skill/references/karta-oceny-0.3.md`; `metodologia/0.3/wynik.schema.json`; `skill/references/wynik-0.3.schema.json`; `skill/SKILL.md`; `skill/scripts/validate_0_3.py`; oba pliki testów 0.3 |
| S10 | `README.md`; `metodologia/0.3/README.md`; `metodologia/0.3/standard.md`; `skill/references/standard-0.3.md`; nowy `metodologia/0.3/metryka-0.3.schema.json`; nowy `skill/references/metryka-0.3.schema.json`; `metodologia/0.3/wynik.schema.json`; `skill/references/wynik-0.3.schema.json`; `metodologia/0.3/wyciag-kalibracyjny.schema.json`; `skill/references/wyciag-kalibracyjny-0.3.schema.json`; `szablony/0.3/karta-oceny.md`; `skill/references/karta-oceny-0.3.md`; `szablony/0.3/wzor-raportu.md`; `skill/references/wzor-raportu-0.3.md`; `skill/SKILL.md`; `skill/scripts/validate_0_3.py`; oba pliki testów 0.3 |
| S11–S15 | standard i kotwice 0.3 wraz z kopiami; wszystkie trzy szablony 0.3 i ich kopie; schematy wyniku, wyciągu i porównania pary wraz z kopiami; `skill/SKILL.md`; `skill/scripts/validate_0_3.py`; oba pliki testów 0.3 |
| B1 | wykonany protokół i rejestry w `kalibracja/0.3/`; po zakończeniu bezpieczne podsumowanie `kalibracja/0.3/wyniki-B1.md` |
| B2 | nowy protokół w `kalibracja/0.3/`; bez zmian standardu, kotwic, schematów i skilla przed analizą wyników |

„Oba pliki testów 0.3” oznacza `tests/test_validate_0_3.py` i `tests/test_0_3_package.py`. „Wszystkie trzy schematy” oznacza wynik, wyciąg i porównanie pary. „Wszystkie trzy szablony” oznacza kartę oceny, wzór raportu i wzór porównania.
