# Kontrola techniczna wdrożenia S1–S8

> **Dokument historyczny.** Opisuje stan gałęzi po S1–S8, na commicie
> `02d9ca80133351518ec2528d1006c8d7600586f1`, przed wdrożeniem S9 i S10.
> Aktualny stan dokumentuje [kontrola techniczna S1–S15](kontrola-techniczna-S1-S15.md).

**Data:** 14 września 2026 r.

**Gałąź:** `feature/0.3-draft`

**Zakres:** wdrożenie zatwierdzonych zmian S1–S8 po polskim pilotażu
**Wynik:** kontrola zakończona pomyślnie

## Wdrożony zakres

- S1 — operacyjne przykłady atomizacji twierdzeń;
- S2 — zamknięte znaczenia `exact`, `adjacent`, `different` i `not_comparable`, także dla relacji złożonych;
- S3 — cztery warunki grupowania problemów i granica `duze`–`srednie`;
- S4 — operacyjne granice H=4, H=3, H=2 i H=1;
- S5 — osobne L dla istotnych grup oraz ogólne L jako ich minimum;
- S6 — progi statusu i pewności profilu oraz ślad wiedzy koniecznej;
- S7 — jawny problem dla bariery językowej wpływającej na H, L, ograniczenia wyniku albo werdykt;
- S8 — kontrolowana relacja werdyktu z bezpiecznym poleceniem.

Zmiany zostały przeniesione do standardu, kotwic, szablonów, trzech schematów JSON, walidatora i samowystarczalnego pakietu umiejętności.

## Testy regresyjne

Zestaw obejmuje 44 testy. Nowe przypadki sprawdzają między innymi:

- minimum H i L dla istotnych grup objętych obietnicą;
- zgodność listy wiedzy koniecznej z jej szczegółowym śladem;
- zakaz wysokiej pewności profilu przy sprzeczności albo profilu częściowym;
- wymaganie jawnego `language_barrier` po uruchomieniu ograniczenia językowego;
- zakaz polecenia łagodniejszego od domyślnego dla werdyktu;
- obowiązek uzasadnienia polecenia ostrzejszego;
- zamkniętą listę sąsiednich wyników twierdzeń;
- wyprowadzanie wyniku relacji złożonej z liczby jej składowych;
- tożsamość publicznych materiałów 0.3 i ich kopii w skillu;
- brak wdrożenia odłożonych S9 i S10.

Wszystkie 44 testy przeszły.

## Kontrola paczki

Pakiet roboczy został zbudowany dwukrotnie w osobnych katalogach. Oba archiwa miały identyczną sumę SHA-256:

`f1c9e033d721447ae87db403f355ced4d3ad4c8cc3100e210772fbef44514694`

Archiwum zawiera 24 pliki. Test integralności ZIP nie wykazał błędów, wszystkie odsyłacze wewnętrzne istnieją, a kopie standardu, kotwic, szablonów i schematów są bajtowo zgodne ze źródłami publicznymi.

## Kontrole dodatkowe

- wszystkie trzy schematy są poprawnym JSON-em, a lokalne odwołania `$ref` wskazują istniejące definicje;
- walidator i budowniczy paczki przechodzą kompilację składniową Pythona;
- `git diff --check` nie wykrywa błędów formatowania;
- w zmianach nie ma plików wersji 0.1 ani 0.2;
- S9 i S10 nadal są wyłącznie odłożonymi propozycjami;
- PR nr 8 nie został scalony;
- nie utworzono znacznika ani wydania 0.3.

Walidator sprawdza strukturę i wewnętrzną spójność danych. Nie zastępuje merytorycznej kontroli prawdziwości oceny ani ludzkiej oceny dowodów dotyczących odbiorców.
