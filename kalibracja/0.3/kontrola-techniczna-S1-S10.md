# Kontrola techniczna wdrożenia S1–S10

**Data:** 14 września 2026 r.

**Gałąź:** `feature/0.3-draft`

**Zakres:** pełna kontrola projektu 0.3 po wdrożeniu zatwierdzonych zmian S1–S10

**Wynik:** kontrola zakończona pomyślnie

## Stan wdrożenia

S1–S8 doprecyzowują atomizację twierdzeń, wyniki porównań, grupowanie problemów, granice H, ocenę L według grup, profil odbiorców, bariery językowe oraz relację werdyktu z bezpiecznym poleceniem.

S9 określa, kiedy historyczna wersja publikacji może zostać uznana za odtworzoną. Bez stabilnego dowodu zachowującego treść poprawność historyczna pozostaje nierozstrzygnięta, a bieżąca wersja jest oceniana osobno.

S10 wprowadza kanoniczny `metryka.json` dla nowych przebiegów kalibracyjnych, jego schemat oraz kontrole zgodności metryki z pełnym wynikiem. Zakończonych serii i historycznych metryk YAML nie migruje się wstecz.

S9 i S10 są wdrożone w standardzie, szablonach, schematach, walidatorze, testach i pakiecie umiejętności projektu 0.3.

## Testy regresyjne i składnia

- wszystkie 65 testów regresyjnych przechodzi;
- wszystkie 6 plików Pythona w repozytorium przechodzi kompilację składniową;
- testy obejmują walidator, zgodność publicznych źródeł z kopiami skilla, odsyłacze wewnętrzne, wdrożenie S1–S10 oraz rozróżnienie historycznych i aktualnych raportów kontroli.

## Schematy i spójność materiałów

- wszystkie 12 plików `*.schema.json` w repozytorium jest poprawnym JSON-em;
- wszystkie lokalne odwołania `$ref` prowadzą do istniejących definicji;
- publiczne kopie standardu, kotwic, czterech schematów 0.3 i trzech szablonów są bajtowo zgodne z kopiami w pakiecie skilla;
- dokumentacja, szablony, schematy i walidator zgodnie opisują rekonstrukcję wersji historycznej oraz obowiązkową metrykę nowych przebiegów kalibracyjnych.

## Kontrola paczki

Pakiet roboczy został zbudowany dwukrotnie w osobnych katalogach. Oba archiwa były bajtowo identyczne i miały sumę SHA-256:

`baaf499da5b9a0e09381a0e356e3687e52f48b0b0f80d1218e75454d8e206355`

Każde archiwum zawiera 25 plików. Test integralności ZIP nie wykazał błędów, a wszystkie odsyłacze wewnętrzne prowadzą do istniejących plików.

## Korekta dokumentacyjna

Raporty kontroli walidatora po pilocie oraz wdrożenia S1–S8 zachowano jako dokumenty historyczne i wyraźnie oznaczono ich zakres czasowy. Podsumowanie pilota wyjaśnia teraz, że S1–S10 zostały zatwierdzone i wdrożone dopiero po jego zakończeniu. Aktualny raport nie przedstawia S9 ani S10 jako zmian odłożonych.

## Zachowane granice

- `git diff --check` nie wykrywa błędów formatowania;
- wersje 0.1 i 0.2 pozostały niezmienione;
- wyniki zakończonych przebiegów i pilota nie zostały przeliczone wstecz;
- B1 i B2 nie zostały rozpoczęte;
- PR nr 8 pozostaje roboczy i niescalony;
- nie utworzono znacznika ani wydania 0.3.

Walidator sprawdza strukturę i wewnętrzną spójność danych. Nie zastępuje merytorycznej kontroli prawdziwości oceny ani ludzkiej oceny dowodów dotyczących odbiorców.
