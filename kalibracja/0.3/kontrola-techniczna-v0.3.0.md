# Końcowa kontrola techniczna v0.3.0

**Data:** 15 września 2026 r.
**Zakres:** kandydat do oficjalnego wydania v0.3.0
**Wynik:** pozytywny

## Wyniki

| Kontrola | Wynik |
| --- | --- |
| Testy regresyjne | 90/90 zaliczonych |
| Składnia skryptów Python | 6/6 plików poprawnych |
| Schematy JSON | 12/12 plików poprawnych składniowo |
| Lokalne odwołania `$ref` | 758/758 rozwiązanych |
| Publiczne źródła i kopie w skillu | 9/9 par zgodnych bajtowo |
| Dwie niezależne budowy 0.3.0 | archiwa zgodne bajtowo |
| Zawartość ZIP | 25 plików, test integralności pozytywny |
| Manifest i suma SHA-256 | zgodne |
| `git diff --check` | bez błędów |

Pakiet `assess-accessibility-articles-v0.3.0.zip` ma SHA-256:

`72b2604d3a9e4581241570c4ca89726e5a8dd7a8e3fd6addafb3a4596b9a6979`

Budowa jest przypisana do niezmiennego commita treści metodologii i skilla `714a5979e52f889671ba52f376824990549da013`. Pakiet zawiera wymagane pliki licencji, manifest wydania, standard, kotwice, schematy, szablony i walidator.

## Kontrole granic

- ścieżki wersji 0.1 i 0.2 nie zostały zmienione; odtworzone pakiety zachowały wcześniejsze sumy kontrolne;
- wyniki B1 pozostały niezmienione: 32 oceny, 16 porównań i zgodność werdyktu 15/16;
- protokół przenośności zachowano niezależnie na gałęzi `research/0.4-przenosnosc-ai`;
- nie rozpoczęto żadnej oceny B2;
- informacje o statusie roboczym zachowano wyłącznie tam, gdzie opisują prawdziwy stan historyczny albo techniczny identyfikator formatu;
- przenośność pomiędzy rodzinami AI nie jest przedstawiana jako warunek wydania 0.3.

Wykonanie tego samego zestawu kontroli oraz pobranie i sprawdzenie opublikowanych plików jest dodatkowo wymuszane przez proces wydawniczy GitHub Actions.
