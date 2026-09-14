# Kontrola techniczna walidatora po polskim pilotażu 0.3

> **Dokument historyczny.** Opisuje stan walidatora na commicie
> `af5f556fa49c5a383e487a591a896a3292ccfe84`, przed decyzjami i wdrożeniem
> S1–S10. Aktualny stan dokumentuje
> [kontrola techniczna S1–S10](kontrola-techniczna-S1-S10.md).

**Data:** 14 września 2026 r.  
**Status:** poprawki techniczne projektu; bez zmiany znaczenia metodologii  
**Zakres danych kontrolnych:** 10 wyników, 10 wyciągów i 5 porównań par z polskiego pilotażu P01–P05

## Wynik

Walidator został wzmocniony w granicach reguł już zapisanych w projekcie 0.3. Nie zmieniono żadnego wyniku pilota, oceny A–L, klasyfikacji twierdzenia, problemu ani werdyktu.

Po poprawkach:

- odrzuca powtórzone nazwy pól w JSON;
- może porównać wyciąg kalibracyjny z odpowiadającym mu pełnym wynikiem;
- porównuje z wynikami A/B identyfikatory przebiegów i publikacji, metodologię, oceny, werdykty i korekty kontrfaktyczne;
- sprawdza obiektywnie rozstrzygalne flagi dopasowań 1:1 i wpisów jednostronnych;
- przelicza miary zgodności zamiast sprawdzać jedynie, czy mieszczą się w zakresie 0–1;
- egzekwuje istniejące warunki użycia `nd` dla B, C i I;
- egzekwuje istniejący związek między werdyktem `nie_mozna_rozstrzygnac` a korektą `nie_dotyczy`.

Pola opisowe wyciągu mogą być krótszą, wierną parafrazą pełnego raportu. Dlatego porównanie między plikami wymaga identyczności danych strukturalnych i kategorycznych, ale nie identycznego brzmienia skróconych uzasadnień.

## Kontrole wykonane po zmianie

- 35 testów jednostkowych walidatora i pakietu: wynik poprawny;
- kompilacja walidatora: wynik poprawny;
- kontrola struktury pakietu umiejętności: wynik poprawny;
- 10/10 pełnych wyników pilota: wynik poprawny;
- 10/10 wyciągów sprawdzonych razem z pełnymi wynikami: wynik poprawny;
- 5/5 porównań sprawdzonych razem z wynikami A/B: wynik poprawny;
- dwie niezależne budowy ZIP: identyczna suma SHA-256;
- kontrola archiwum ZIP: brak błędów.

## Granice poprawki technicznej

Walidator nie rozstrzyga jeszcze kwestii, których projekt 0.3 nie definiuje jednoznacznie. Dotyczy to zwłaszcza:

- różnicy między `adjacent`, `different` i `not_comparable` dla wyników twierdzeń;
- sposobu liczenia zgodności w relacjach wiele:1, 1:wiele i wiele:wiele;
- związku werdyktu z `safe_recommendation`;
- odrębnej oceny L dla grup odbiorców;
- jednolitego, maszynowego formatu `metryka.yaml`.

Wprowadzenie tych kontroli wymaga najpierw decyzji znaczeniowej albo strukturalnej. Propozycje są opisane w osobnym dokumencie i nie zostały wdrożone.

## Zachowane granice

- wersje 0.1 i 0.2 pozostały niezmienione;
- PR nr 8 nie został scalony;
- nie utworzono znacznika ani wydania 0.3;
- nie zmieniono wstecz danych pilota.
