# Ocena rzetelności publikacji o dostępności

Publiczny projekt metodologii służącej do powtarzalnej, porównywalnej i sprawdzalnej oceny artykułów, poradników oraz innych publikacji dotyczących dostępności.

## Status

- **0.1** — wersja zamrożona użyta w pierwszej serii i jej zaślepionym powtórzeniu; pozostaje domyślną wersją działającej umiejętności.
- **0.2 — projekt do kalibracji** — zawiera regułę centralności problemu, test korekty kontrfaktycznej, osobne kotwice A–L, dokładniejszą granicę problemu dużego i krytycznego, wersjonowanie materiałów oraz walidowane dane ustrukturyzowane.

Projektu 0.2 nie należy jeszcze przedstawiać jako wersji zwalidowanej. Umiejętność użyje go tylko wtedy, gdy polecenie jawnie wskaże wersję 0.2.

## Dlaczego powstał projekt 0.2

W zaślepionym powtórzeniu pięciu analiz oba przebiegi wskazywały zasadniczo te same problemy merytoryczne, ale:

- identyczne oceny A–L wystąpiły w 53,3% przypadków;
- wszystkie różnice mieściły się w jednym punkcie;
- werdykt był identyczny w 60% przypadków;
- drugi przebieg był średnio o 0,40 punktu surowszy.

Największa niejednoznaczność dotyczyła przejścia od wykrytych problemów do werdyktu, szczególnie rozstrzygnięcia, czy błąd podważa rdzeń publikacji. Projekt 0.2 odpowiada na te problemy, ale wymaga nowej niezależnej próby.

## Założenia

Ocena powinna:

- obejmować pełną dostępną treść publikacji i dokładne wersje materiałów centralnych;
- oddzielać neutralne przedstawienie stanowiska autora od jego krytycznej oceny;
- identyfikować konkretne twierdzenia podlegające weryfikacji;
- korzystać przede wszystkim ze źródeł pierwotnych i autorytatywnych;
- odróżniać błąd od opinii, uproszczenia oraz sporu interpretacyjnego;
- badać poprawność, zrozumiałość i użyteczność tekstu;
- oddzielać znaczenie problemu od jego centralności, ryzyka i pewności;
- ujawniać ograniczenia analizy oraz środowisko oceniające;
- zachowywać tę samą strukturę raportu dla kolejnych publikacji;
- zapisywać wyniki w formie możliwej do automatycznego porównania.

## Zawartość

### Metodologia

- `metodologia/standard.md` — zamrożony standard 0.1 zachowany dla zgodności dotychczasowych odsyłaczy;
- `metodologia/0.1/standard.md` — wersjonowana kopia standardu 0.1;
- `metodologia/0.2/standard.md` — projekt zmian 0.2, czytany łącznie ze standardem 0.1;
- `metodologia/0.2/kotwice.md` — szczegółowe kotwice ocen 0–4 dla wymiarów A–L;
- `metodologia/0.2/wynik.schema.json` — schemat pełnego wyniku;
- `metodologia/0.2/wyciag-kalibracyjny.schema.json` — schemat krótkiego wyniku do porównywania przebiegów.

### Szablony i umiejętność

- `szablony/0.1/` i `szablony/0.2/` — wersjonowane karty oraz wzory raportów;
- `skill/SKILL.md` — instrukcja działania umiejętności AI z wyborem wersji;
- `skill/references/` — materiały metodologiczne używane przez umiejętność;
- `skill/scripts/validate_0_2.py` — walidator pełnego wyniku i wyciągu kalibracyjnego;
- `skill/agents/openai.yaml` — metadane interfejsu umiejętności.

## Rozdzielenie metodologii i badań

Repozytorium zawiera publiczną metodologię, szablony i umiejętność AI. Robocze analizy publikacji, materiały źródłowe i pełne wyniki kalibracji nie są tutaj przechowywane.

Do publicznego projektu trafiają wyłącznie ogólne wnioski służące poprawianiu metodologii, bez pełnych kopii ocenianych publikacji i bez materiałów wymagających poufności.

## Następny etap

1. Zamrozić dokładny identyfikator projektu 0.2 i korpus obejmujący różnych autorów oraz typy publikacji.
2. Przeprowadzić oceny niezależnie, bez dostępu do cudzych wyników.
3. Włączyć co najmniej jednego ludzkiego eksperta dostępności.
4. Porównać oceny A–L, werdykty, mapy twierdzeń, znaczenie, centralność i ryzyko problemów.
5. Po analizie rozbieżności zdecydować, czy projekt może stać się stabilną metodologią 0.2.

## Licencja

Licencja projektu nie została jeszcze wybrana. Do czasu jej jednoznacznego wskazania nie należy zakładać prawa do kopiowania, modyfikowania ani rozpowszechniania zawartości poza uprawnieniami wynikającymi z obowiązującego prawa.

