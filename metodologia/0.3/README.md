# Metodologia 0.3 — publiczny projekt roboczy

Ten katalog zawiera pełną propozycję metodologii 0.3. Nie jest to jeszcze zamrożone wydanie ani wersja przeznaczona do cytowania jako stabilna.

Projekt 0.3:

- jest samodzielny — nie wymaga składania zasad z wersji 0.1 i 0.2;
- powstał na podstawie wniosków z 16 przebiegów kalibracyjnych 0.2;
- doprecyzowuje mapowanie twierdzeń, grupowanie problemów, granice wyników i stosowanie `nd`;
- rozdziela historyczną poprawność publikacji od jej dzisiejszej przydatności;
- dokładniej ocenia język względem odbiorcy i celu miejsca publikacji;
- dodaje jawne testy centralności problemu i ryzyka zastosowania;
- wymaga udokumentowanego profilu miejsca, celu i grup odbiorców przed oceną G, H i L;
- wprowadza wspólny format semantycznego porównania par A/B;
- wymaga kanonicznego `metryka.json` z sumami zamrożonych wejść dla nowych przebiegów kalibracyjnych.

Pliki:

- `standard.md` — pełna metodologia;
- `kotwice.md` — znaczenie ocen 0–4 w wymiarach A–L;
- `wynik.schema.json` — schemat pełnego wyniku;
- `metryka-0.3.schema.json` — schemat kanonicznej metryki nowego przebiegu kalibracyjnego;
- `wyciag-kalibracyjny.schema.json` — schemat skrótu do porównywania przebiegów;
- `porownanie-pary-0.3.schema.json` — schemat kompletnego porównania dwóch przebiegów A/B.

Historyczne wersje 0.1 i 0.2 pozostają niezmienione. Zmiany w tym katalogu obowiązują wyłącznie wtedy, gdy oceniający świadomie wybierze projekt 0.3.

Historycznych metryk YAML ani wyników zakończonych serii nie migruje się do nowego kontraktu. `metryka.yaml` może być w przyszłych seriach jedynie automatycznie wygenerowaną kopią dla człowieka; źródłem kanonicznym pozostaje JSON.
