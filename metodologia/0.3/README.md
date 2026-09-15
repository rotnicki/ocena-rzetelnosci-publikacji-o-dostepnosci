# Metodologia 0.3 — zamrożona wersja eksperymentalna

Ten katalog zawiera pełną metodologię wydania `v0.3.0`. Jest to zamrożona wersja eksperymentalna przeznaczona do ocen i dalszych badań, a nie wersja stabilna 1.0.

Wersja 0.3:

- jest samodzielny — nie wymaga składania zasad z wersji 0.1 i 0.2;
- powstał na podstawie wniosków z 16 przebiegów kalibracyjnych 0.2;
- doprecyzowuje mapowanie twierdzeń, grupowanie problemów, granice wyników i stosowanie `nd`;
- rozdziela historyczną poprawność publikacji od jej dzisiejszej przydatności;
- dokładniej ocenia język względem odbiorcy i celu miejsca publikacji;
- dodaje jawne testy centralności problemu i ryzyka zastosowania;
- wymaga udokumentowanego profilu miejsca, celu i grup odbiorców przed oceną G, H i L;
- wprowadza wspólny format semantycznego porównania par A/B;
- wymaga kanonicznego `metryka.json` z sumami zamrożonych wejść dla nowych przebiegów kalibracyjnych;
- wymaga osobnego dowodu każdej rekonstruowanej wersji historycznej;
- wyznacza dokładne granice stosowania `nd` w C i J;
- wprowadza ustrukturyzowane testy granicy problemu średniego i dużego, rozstrzygalności oraz przesłanek krytyczności;
- kontroluje właściwy przedmiot uzasadnienia A–L i jednolite tworzenie grup odbiorców.

Pliki:

- `standard.md` — pełna metodologia;
- `kotwice.md` — znaczenie ocen 0–4 w wymiarach A–L;
- `wynik.schema.json` — schemat pełnego wyniku;
- `metryka-0.3.schema.json` — schemat kanonicznej metryki nowego przebiegu kalibracyjnego;
- `wyciag-kalibracyjny.schema.json` — schemat skrótu do porównywania przebiegów;
- `porownanie-pary-0.3.schema.json` — schemat kompletnego porównania dwóch przebiegów A/B.

Historyczne wersje 0.1 i 0.2 pozostają niezmienione. W nowych ocenach pakietu 0.3 ta wersja jest aktywna; wcześniejsze wersje należy wybierać jawnie.

Wersja obejmuje zatwierdzone doprecyzowania S1–S15. Badanie B1 zostało zakończone proceduralnie. Przenośność pomiędzy rodzinami AI pozostaje poza zakresem walidacji 0.3 i może zostać zbadana osobno podczas prac nad 0.4.

Wartość `0.3-draft` zachowana w schematach i walidatorze jest zamrożonym identyfikatorem formatu danych użytego podczas kalibracji. Nie oznacza roboczego statusu wydania i nie została zmieniona, aby nie unieważniać zgodnych wyników B1.

Historycznych metryk YAML ani wyników zakończonych serii nie migruje się do nowego kontraktu. `metryka.yaml` może być w przyszłych seriach jedynie automatycznie wygenerowaną kopią dla człowieka; źródłem kanonicznym pozostaje JSON.
