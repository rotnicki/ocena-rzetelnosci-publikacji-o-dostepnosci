# Rejestr odchyleń B1

**Utworzono:** 14 września 2026 r.
**Stan serii:** zakończona proceduralnie
**Liczba ocen:** 32 w 16 parach A/B

## Zasada

Rejestr zachowuje odchylenia techniczne i proceduralne bez zmieniania metody w
trakcie B1. Podejrzenie wady metodologii zapisuje się, ale rozpatruje dopiero po
zamknięciu serii.

| ID | Data i czas UTC | Etap | Rodzaj | Opis | Wpływ na porównywalność | Działanie | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | Nie zarejestrowano odchylenia zmieniającego zamrożoną metodologię albo naruszającego izolację A/B. | — | — | zamknięte |

Techniczne zastąpienia materiałów wykonano i zatwierdzono przed rozpoczęciem ocen, zgodnie z protokołem i bez doboru według wyniku. Po 24 ocenach korpusu głównego uruchomiono osobno zatwierdzoną falę rezerwową obejmującą R1, R2, R4 i R5. R3 nie uruchomiono. Zdarzenia te nie zmieniły zamrożonej metodologii.

## Zamknięcie bramek

Bramek nie liczy się jako odchyleń, dopóki oceny nie zostały rozpoczęte.

| Bramka | Stan | Warunek zamknięcia |
| --- | --- | --- |
| zatwierdzenie korpusu | zamknięta przed ocenami | jawna akceptacja właściciela projektu |
| kontrola kolizji z prywatnym pilotem P01–P05 | zamknięta przed ocenami | porównanie kanonicznych URL z prywatnym manifestem bez ujawnienia manifestu |
| zamrożenie kopii i metryk | zamknięta przed ocenami | SHA-256 wszystkich materiałów i poprawna walidacja metryk |
| izolacja A/B | zamknięta przed ocenami i zachowana | dwa puste, odizolowane konteksty dla każdej pary |

Zamknięcie bramek pozwoliło wykonać B1. Nie stanowi decyzji o rozpoczęciu B2;
B2 nie zostało rozpoczęte.
