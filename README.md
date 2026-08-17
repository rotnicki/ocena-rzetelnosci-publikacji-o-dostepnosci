# Ocena rzetelności publikacji o dostępności

Publiczny projekt metodologii służącej do powtarzalnej, porównywalnej i sprawdzalnej oceny artykułów, poradników oraz innych publikacji dotyczących dostępności.

## Status

Projekt znajduje się na etapie pilotażowym. Obecna metodologia ma numer **0.1** i jest zamrożona na czas pierwszej kalibracji na zróżnicowanym zestawie publikacji. Działająca umiejętność AI korzysta z tej samej wersji zasad.

## Założenia

Ocena powinna:

- obejmować pełną dostępną treść publikacji;
- oddzielać neutralne przedstawienie stanowiska autora od jego krytycznej oceny;
- identyfikować konkretne twierdzenia podlegające weryfikacji;
- korzystać przede wszystkim ze źródeł pierwotnych i autorytatywnych;
- odróżniać błąd od opinii, uproszczenia oraz sporu interpretacyjnego;
- badać poprawność, zrozumiałość i użyteczność tekstu;
- ujawniać ograniczenia analizy oraz poziom pewności;
- zachowywać tę samą strukturę raportu dla kolejnych publikacji.

## Zawartość

- `metodologia/standard.md` — aktualny projekt standardu;
- `szablony/karta-oceny.md` — skrócona karta ocen w poszczególnych wymiarach;
- `szablony/wzor-raportu.md` — obowiązkowa struktura pełnego raportu;
- `skill/SKILL.md` — instrukcja działania umiejętności AI;
- `skill/references/` — zamrożone materiały metodologiczne używane przez umiejętność;
- `skill/agents/openai.yaml` — metadane interfejsu umiejętności.

## Rozdzielenie metodologii i badań

Repozytorium zawiera publiczną metodologię, szablony i — w przyszłości — umiejętność AI. Robocze analizy publikacji, materiały źródłowe oraz wyniki kalibracji mogące zawierać cudze treści nie są tutaj przechowywane.

Do publicznego projektu trafiają jedynie ogólne wnioski służące poprawianiu metodologii, bez ujawniania materiałów wymagających poufności.

## Plan prac

1. Przeprowadzenie pierwszych analiz kalibracyjnych według zamrożonej wersji 0.1.
2. Porównanie wyników i zidentyfikowanie niejednoznacznych kryteriów.
3. Doprecyzowanie kryteriów, kotwic skali ocen i schematu danych.
4. Powtórne sprawdzenie zestawu po zaprojektowaniu zmian.
5. Publikacja metodologii 0.2 i aktualizacja umiejętności `assess-accessibility-articles`.

## Licencja

Licencja projektu nie została jeszcze wybrana. Do czasu jej jednoznacznego wskazania nie należy zakładać prawa do kopiowania, modyfikowania ani rozpowszechniania zawartości poza uprawnieniami wynikającymi z obowiązującego prawa.
