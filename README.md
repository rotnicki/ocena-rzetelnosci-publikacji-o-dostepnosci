# Ocena rzetelności publikacji o dostępności

Ten projekt pomaga sztucznej inteligencji oceniać artykuły, poradniki, oferty i inne publikacje dotyczące dostępności w sposób możliwie powtarzalny, porównywalny i sprawdzalny.

## Najprościej mówiąc

Sama prośba „oceń ten artykuł” jest zbyt ogólna. Dwa systemy AI mogą wtedy zwrócić uwagę na inne rzeczy, inaczej rozumieć skalę ocen i dojść do różnych werdyktów.

Ten projekt dostarcza wspólny sposób pracy. Określa między innymi:

- co trzeba przeczytać;
- jakie twierdzenia należy sprawdzić;
- z jakich źródeł korzystać;
- jak odróżniać fakt, opinię, uproszczenie i błąd;
- jak oceniać poprawność, zrozumiałość i bezpieczeństwo praktycznych zaleceń;
- jak opisywać niepewność i ograniczenia;
- jak zapisać wynik, żeby można go było porównać z innym przebiegiem.

Projekt jest tworzony przede wszystkim dla AI działającej pod kontrolą człowieka. Koordynator AI może wybierać publikacje zgodnie z protokołem, uruchamiać niezależne oceny, zapisywać i porównywać wyniki. Człowiek zatwierdza najważniejsze decyzje dotyczące metodologii i nie musi ręcznie tworzyć nowych czatów ani przeklejać poleceń.

## Jak wygląda pojedyncza ocena

W uproszczeniu AI:

1. czyta pełną dostępną publikację i ważne materiały, do których ona odsyła;
2. przygotowuje neutralne streszczenie stanowiska autora;
3. wyodrębnia konkretne twierdzenia do sprawdzenia;
4. porównuje je przede wszystkim ze źródłami pierwotnymi i autorytatywnymi;
5. ocenia publikację w dwunastu stałych wymiarach;
6. porządkuje wykryte problemy według ich znaczenia;
7. wydaje opisowy werdykt i podaje poziom pewności;
8. zapisuje wynik w stałej strukturze, która pozwala porównywać kolejne oceny.

Metoda może być stosowana również do treści sprzedażowych, na przykład ofert audytów lub usług dostępności. W takim przypadku ocenie podlegają także obietnice, opisy obowiązków prawnych, certyfikatów, terminów, kar i zakresu oferowanej usługi.

## Czego ten projekt nie robi

Projekt:

- nie ocenia charakteru, intencji ani kompetencji autora jako osoby;
- nie zakłada, że każdy spór interpretacyjny jest błędem;
- nie zastępuje porady prawnej, badania naukowego ani profesjonalnego audytu produktu;
- nie gwarantuje poprawności tylko dlatego, że raport ma właściwy format;
- nie zakłada, że jeden wynik AI jest ostateczną prawdą;
- nie pozwala zmieniać zasad w trakcie oceny tylko po to, aby uzyskać oczekiwany werdykt.

## Najważniejsze pojęcia

- **Metoda oceny** — zasady mówiące, jak przeprowadzić analizę i jak uzasadnić wynik.
- **Umiejętność AI** — pakiet instrukcji i plików, który pomaga zgodnemu systemowi AI zastosować metodę.
- **Przebieg** — jedna niezależnie wykonana ocena konkretnej publikacji.
- **Kalibracja** — sprawdzanie, czy kolejne niezależne przebiegi prowadzą do wystarczająco podobnych i porównywalnych wyników.
- **Zamrożenie wersji** — niezmienianie zasad podczas danej serii porównawczej. Nie oznacza, że metoda jest ukończona.
- **Walidator** — program sprawdzający, czy dane wynikowe mają wymaganą strukturę. Walidator nie sprawdza, czy sama analiza jest prawdziwa lub trafna.
- **Werdykt** — opisowe podsumowanie rzetelności publikacji. Nie jest wyliczany jako zwykła średnia ocen.

## Metoda a umiejętność AI

Metoda i umiejętność nie są tym samym.

Formalne zasady znajdują się w katalogu `metodologia/`. Plik `skill/SKILL.md` instruuje zgodny system AI, jak znaleźć te zasady i zastosować je krok po kroku. Szablony określają układ raportów, a walidator kontroluje strukturę danych.

Pakiet umiejętności korzysta z formatu `SKILL.md` zgodnego z otwartym standardem [Agent Skills](https://agentskills.io/). Ma więc założenie przenośności między zgodnymi narzędziami, a nie działania wyłącznie w jednym produkcie.

Nie oznacza to jednak, że każdy czat AI automatycznie przeczyta repozytorium lub uruchomi umiejętność. Dane środowisko musi obsługiwać ten format albo otrzymać odpowiednie pliki i instrukcje. Obecna wersja była praktycznie sprawdzana głównie w ChatGPT/Codex. Zgodność z innymi narzędziami wymaga osobnych testów. Plik `skill/agents/openai.yaml` zawiera jedynie dodatkowe metadane dla środowiska OpenAI i nie stanowi rdzenia metody.

## Status wersji

Projekt pozostaje na wczesnym etapie rozwoju, przed wersją 1.0.

### Wersja 0.1

To pierwsza zamrożona wersja robocza. Została użyta w początkowej serii ocen i w ich zaślepionym powtórzeniu. Pozostaje domyślną wersją działającej umiejętności.

„Zamrożona” oznacza tutaj, że podczas porównywania wyników nie zmieniano jej reguł. Nie oznacza to, że wersja 0.1 jest ostateczna albo w pełni zwalidowana.

### Wersja 0.2-draft

To projekt zmian przeznaczony do dalszej kalibracji. Dodaje między innymi:

- dokładniejsze reguły ustalania, czy problem dotyczy rdzenia publikacji;
- test sprawdzający, czy poprawienie problemów wymagałoby drobnej czy strukturalnej zmiany tekstu;
- osobne kotwice ocen od 0 do 4 dla wszystkich dwunastu wymiarów;
- dokładniejsze rozróżnienie problemów dużych i krytycznych;
- zapisywanie wersji ocenianych materiałów;
- walidowane dane ustrukturyzowane do porównywania przebiegów.

Wersja 0.2-draft nie jest jeszcze stabilnym standardem. Umiejętność używa jej tylko wtedy, gdy polecenie wyraźnie wybiera tę wersję. Jej reguły mogą się zmienić po analizie dalszych prób.

## Główne zasady

Ocena powinna:

- obejmować pełną dostępną treść publikacji i dokładne wersje materiałów ważnych dla jej argumentacji;
- oddzielać neutralne przedstawienie stanowiska autora od krytycznej oceny;
- identyfikować konkretne twierdzenia podlegające weryfikacji;
- korzystać przede wszystkim ze źródeł pierwotnych i autorytatywnych;
- odróżniać błąd od opinii, uproszczenia oraz sporu interpretacyjnego;
- badać poprawność, zrozumiałość i praktyczne bezpieczeństwo tekstu;
- oddzielać znaczenie problemu od jego centralności, ryzyka zastosowania i pewności oceny;
- ujawniać ograniczenia analizy oraz informacje o środowisku oceniającym;
- zachowywać tę samą strukturę raportu dla kolejnych publikacji;
- zapisywać wyniki w formie umożliwiającej automatyczne porównanie.

## Co znajduje się w repozytorium

### Kalibracja

- `kalibracja/0.2/protokol-doboru-publikacji.md` — formalne zasady tworzenia, wyboru i zamrożenia korpusu do kalibracji powtarzalności AI.

### Metodologia

- `metodologia/standard.md` — zamrożony standard 0.1 zachowany dla zgodności dotychczasowych odsyłaczy;
- `metodologia/0.1/standard.md` — wersjonowana kopia standardu 0.1;
- `metodologia/0.2/standard.md` — projekt zmian 0.2, czytany łącznie ze standardem 0.1;
- `metodologia/0.2/kotwice.md` — szczegółowe kotwice ocen 0–4 dla wymiarów A–L;
- `metodologia/0.2/wynik.schema.json` — schemat pełnego wyniku;
- `metodologia/0.2/wyciag-kalibracyjny.schema.json` — schemat krótkiego wyniku do porównywania przebiegów.

### Szablony, umiejętność i narzędzia

- `szablony/0.1/` i `szablony/0.2/` — wersjonowane karty oraz wzory raportów;
- `skill/SKILL.md` — główna instrukcja działania umiejętności AI i wyboru wersji;
- `skill/references/` — kopie materiałów metodologicznych używane przez umiejętność;
- `skill/scripts/validate_0_2.py` — walidator pełnego wyniku i wyciągu kalibracyjnego;
- `skill/agents/openai.yaml` — opcjonalne metadane interfejsu dla środowiska OpenAI.

Formalne pliki metodologii są źródłem obowiązujących reguł. Ten README służy ich prostemu objaśnieniu i nie zastępuje standardu.

## Gdzie są wyniki prób i pełne analizy

Wyniki prób, materiały robocze i pełne analizy publikacji nie są przechowywane w tym publicznym repozytorium.

Publicznie udostępniane mogą być ogólne wyniki kalibracji i wnioski potrzebne do rozwijania metody. Takie rozdzielenie ogranicza ryzyko naruszenia praw autorskich, ujawnienia materiałów roboczych oraz pomylenia wstępnych wyników ze stabilną częścią standardu.

## Dlaczego powstał projekt 0.2

W zaślepionym powtórzeniu pięciu analiz oba przebiegi wskazywały zasadniczo te same problemy merytoryczne, ale:

- identyczne oceny A–L wystąpiły w 53,3% przypadków;
- wszystkie różnice mieściły się w jednym punkcie;
- werdykt był identyczny w 60% przypadków;
- drugi przebieg był średnio o 0,40 punktu surowszy.

Największa niejednoznaczność dotyczyła przejścia od wykrytych problemów do werdyktu, szczególnie rozstrzygnięcia, czy błąd podważa rdzeń publikacji. Projekt 0.2 próbuje zmniejszyć tę niejednoznaczność, lecz wymaga dalszych niezależnych prób.

## Następny etap

Plan dalszych prac obejmuje:

1. utworzenie rejestru kandydatów i zamrożenie korpusu ośmiu publikacji zgodnie z protokołem doboru;
2. wykonanie dla każdej publikacji dwóch odizolowanych przebiegów uruchamianych przez koordynatora AI, bez ręcznego przeklejania poleceń przez użytkownika;
3. automatyczne sprawdzanie struktury wyników i półautomatyczne porównywanie rozbieżności;
4. dokumentowanie problemów metody bez zmieniania wstecz wyników już zakończonych przebiegów;
5. podjęcie decyzji po kalibracji, jakie zmiany powinny znaleźć się w kolejnej wersji projektu;
6. przeprowadzenie testów z innymi systemami AI dopiero jako osobnego etapu sprawdzania przenośności.

Szczegółowe zasady zawiera `kalibracja/0.2/protokol-doboru-publikacji.md`.

## Licencja

Licencja projektu nie została jeszcze wybrana. Do czasu jej jednoznacznego wskazania nie należy zakładać prawa do kopiowania, modyfikowania ani rozpowszechniania zawartości poza uprawnieniami wynikającymi z obowiązującego prawa.
