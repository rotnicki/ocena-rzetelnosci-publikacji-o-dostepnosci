# Wyniki właściwej serii kalibracyjnej 0.2

**Data zakończenia:** 31 sierpnia 2026 r.  
**Metodologia:** 0.2-draft  
**Identyfikator metodologii:** `c3280da26d2bf0a5a44dfcddc9105180bf3d4267`  
**Identyfikator protokołu i korpusu:** `14241000b8c85d31d91efa67873721bf344c16af`

## Co sprawdzono

Zgodnie z wcześniej zamrożonym protokołem oceniono osiem polskojęzycznych publikacji. Dla każdej wykonano dwa niezależne przebiegi w odizolowanych kontekstach tego samego rodzaju systemu AI.

Seria obejmowała:

- 8 publikacji;
- 16 ukończonych ocen;
- 8 porównań par;
- 96 porównań wpisów A–L.

## Wynik zbiorczy

- zgodność werdyktu: **8/8 przypadków (100%)**;
- identyczne wpisy A–L: **81/96 (84,4%)**;
- różnica najwyżej jednego punktu: **93/94 wspólnie liczbowych ocen (98,9%)**;
- średnia bezwzględna różnica ocen liczbowych: **0,16 punktu**;
- średni kierunek różnicy B minus A: **+0,01 punktu**;
- zgodne werdykty: 6 razy „rzetelny z istotnymi zastrzeżeniami” i 2 razy „nierzetelny”.

## Zgodność według wymiaru

| Wymiar | Identyczna ocena | Różnica najwyżej 1 punkt* | Średnia różnica |
|---|---:|---:|---:|
| A | 7/8 | 7/8 | 0,25 |
| B | 8/8 | 8/8 | 0,00 |
| C | 6/8 | 6/6 | 0,17 |
| D | 7/8 | 8/8 | 0,13 |
| E | 7/8 | 8/8 | 0,13 |
| F | 8/8 | 8/8 | 0,00 |
| G | 5/8 | 8/8 | 0,38 |
| H | 7/8 | 8/8 | 0,13 |
| I | 7/8 | 8/8 | 0,13 |
| J | 7/8 | 8/8 | 0,13 |
| K | 4/8 | 8/8 | 0,50 |
| L | 8/8 | 8/8 | 0,00 |

\* Dla par, w których oba przebiegi podały ocenę liczbową. W wymiarze C wystąpiła jedna rozbieżność liczba–`nd`, a w jednym przypadku oba przebiegi zgodnie zastosowały `nd`.

## Wniosek

W badanym środowisku metodologia 0.2-draft dawała bardzo powtarzalny werdykt i na ogół podobne oceny punktowe. Największego doprecyzowania wymagają wymiary K, G oraz stosowanie `nd` w wymiarze C.

Nie oznacza to jeszcze pełnej walidacji ani gotowości wersji 1.0. Seria:

- obejmowała wyłącznie publikacje polskojęzyczne;
- używała tego samego rodzaju systemu AI w obu przebiegach;
- nie porównywała różnych producentów AI;
- nie korzystała z niezależnego wzorca wyniku;
- badała powtarzalność, a nie pełną trafność metodologii.

## Stan dalszej analizy

Zakończono porównanie ocen A–L i werdyktów. Do wykonania pozostaje jednolite, zbiorcze dopasowanie map twierdzeń i problemów dla wszystkich ośmiu par. Dopiero ono pozwoli podać wspólne miary zgodności klasyfikacji znaczenia, centralności i ryzyka oraz pokrycia mapy twierdzeń.

Brakujące obliczenia nie zmieniają zakończonych ocen. Wyników 0.2 nie należy poprawiać wstecz.

## Następny etap

Należy przygotować osobny projekt kolejnej wersji, oparty na udokumentowanych rozbieżnościach. Nie należy zmieniać zamrożonego standardu, protokołu ani zakończonych wyników 0.2.
