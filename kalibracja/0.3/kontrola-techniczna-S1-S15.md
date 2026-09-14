# Kontrola techniczna wdrożenia T1–T2 i S11–S15

**Data:** 14 września 2026 r.

**Zakres:** pełny publiczny projekt metodologii 0.3 po zakończeniu B1 i wdrożeniu S1–S15

**Wynik:** kontrola zakończona powodzeniem

## Stan projektu

- B1 zostało zakończone proceduralnie po 32 niezależnych ocenach i 16
  porównaniach A/B; R3 nie uruchomiono.
- T1–T2 oraz S1–S15 są wdrożone. Nowe zasady działają wyłącznie
  prospektywnie; wyników polskiego pilotażu ani B1 nie przeliczono.
- Projekt 0.3 pozostaje roboczy i niezamrożony.
- B2 nie zostało rozpoczęte.
- Wersje 0.1 i 0.2 pozostały niezmienione.

## Wyniki kontroli

| Kontrola | Wynik |
| --- | --- |
| Wszystkie testy regresyjne | 85/85 poprawnych |
| Składnia skryptów i testów Python | 7/7 plików poprawnych |
| Schematy JSON | 12/12 plików poprawnie odczytanych |
| Lokalne odwołania `$ref` | 758/758 rozwiązanych |
| Publiczne źródła i bajtowe kopie w pakiecie skill | 9/9 par identycznych |
| Pierwsza i druga budowa pakietu | archiwa identyczne bajtowo |
| Zawartość ZIP | 25 unikalnych plików, wymagane składniki obecne, brak plików tymczasowych |
| Integralność ZIP i plików `.sha256` | poprawna dla obu archiwów |
| `git diff --check` | bez błędów |
| Dokumentacja, szablony, schematy i walidator | wzajemnie spójne |
| Nieaktualne informacje o B1, S11–S15 i B2 | brak w bieżących opisach stanu; dawne informacje zachowane tylko w jawnie oznaczonych zapisach historycznych |
| Zmiany wersji 0.1 i 0.2 | brak |

Obie niezależne budowy utworzyły archiwum
`assess-accessibility-articles-v0.3.0-draft.zip` o SHA-256
`a449806d0e4cf998f03578b377b396c02d14c75f892e11444d6912fb27f51990`.
Test integralności danych skompresowanych, kontrola listy plików i weryfikacja
obu dołączonych plików sum kontrolnych zakończyły się powodzeniem.

## Zakres regresji S11–S15

Testy obejmują między innymi:

- zgodność liczbowego C i J albo `nd` z ustrukturyzowaną podstawą
  stosowalności, w tym szeroką obietnicę publikacji;
- pozytywne i negatywne przypadki granicy problemu `srednie`–`duze` oraz
  grupowania powtarzających się wystąpień;
- kontrolę właściwego przedmiotu A–L i odrębnego skutku obserwacji
  współdzielonej między wymiarami;
- rozróżnienie braku rdzenia, braku zewnętrznego dowodu i braków pomocniczych
  w teście rozstrzygalności;
- komplet czterech przesłanek problemu krytycznego i obowiązek wskazania
  niespełnionej przesłanki dla problemu dużego;
- spójność nowych pól między pełnym wynikiem, wyciągiem i porównaniem pary;
- osobny dowód wersji historycznej wymagany przez T2.

Walidator sprawdza zależności strukturalne i kategoryczne. Zgodnie z S13 nie
próbuje automatycznie oceniać całego naturalnego uzasadnienia ani zastępować
kontroli merytorycznej.

## Granica tej kontroli

Pomyślna kontrola techniczna potwierdza spójność i powtarzalność pakietu, lecz
nie zamraża metodologii, nie rozpoczyna B2 i nie stanowi decyzji o wydaniu
`v0.3.0`.
