# Korpus B1 do zatwierdzenia

**Data ustalenia:** 14 września 2026 r.
**Korpus główny:** 12 publikacji, po dwa niezależne przebiegi A/B
**Rezerwa:** 6 publikacji, po jednej na profil
**Stan zapisany w tym dokumencie:** 0 z 24 przebiegów głównych; oceny nie były jeszcze rozpoczęte
**Status zapisany przed ocenami:** korpus zamrożony algorytmicznie, oczekujący na zatwierdzenie właściciela i prywatną kontrolę kolizji P01–P05
**Stan późniejszy:** B1 zakończone proceduralnie po 32 ocenach; zob. [`wyniki-B1.md`](wyniki-B1.md)

> Rejestr zachowuje pierwotny korpus i bramki sprzed ocen. Nie przypisuje
> publikacjom wyników i nie jest bieżącym raportem postępu B1.

## 1. Zasada wyboru

Korpus ustalono przez rosnące wartości SHA-256 zapisane w rejestrze
kandydatów. Identyfikatory B1-01–B1-12 nadano według profilu i kolejności
skrótu tylko na potrzeby dalszego haszowania. Tabela korpusu nie ujawnia profilu
sondy, dzięki czemu może służyć jako neutralny manifest koordynatora.

Planowaną podstawą zamrożenia treści jest `canonical_text`. Jeżeli dla danej
strony nie da się zachować równoważnej treści tą metodą, przed pierwszym
przebiegiem zostanie użyte `rendered_capture` albo `raw_bytes`, a wybór i
SHA-256 materiału zostaną zapisane w prywatnej metryce. A i B otrzymają tę samą
kopię.

## 2. Publikacje główne i kolejność wykonania

Kolejność ustalono rosnąco według SHA-256 ciągu:

`ocena-0.3-B1-kolejnosc-v1|<case_id>|<kanoniczny_url>`

| Kolejność | ID | Publikacja | Autor / miejsce | Data lub znana wersja | Kontrola publicznej wersji | SHA-256 kolejności | Rezerwa |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | B1-06 | [WCAG 2025 — nowe przepisy WCAG 2.2](https://emeraldmedia.pl/nowe-przepisy-wcag-2025-co-musisz-wiedziec-o-obowiazkowej-dostepnosci-stron-i-sklepow-internetowych/) | zespół Emerald Media | 2025-05-27 | 2026-09-14 11:59 UTC | `0a1cca36003f4f9f87327adfc4e71ef4a09f709bd66f87078d59ad9372756388` | R3 |
| 2 | B1-07 | [Jak polski biznes wdraża dostępność? Wyniki badania BAF rok po wejściu w życie ustawy](https://baforum.pl/a,223,jak-polski-biznes-wdraza-dostepnosc-wyniki-badania-baf-rok-po-wejsciu-w-zycie-ustawy) | Business Accessibility Forum | 2026-08-03 | 2026-09-14 11:59 UTC | `0a5ef2d32b71dab4bfda61a9f9623062d64d27348d43b3c0361dcc58c472e95a` | R4 |
| 3 | B1-12 | [Europejski Akt o Dostępności w praktyce](https://www.shoper.pl/learn/artykul/europejski-akt-o-dostepnosci-co-musisz-wiedziec-jako-przedsiebiorca-dzialajacy-w-sieci) | zespół Shoper | 2025-02-11 | 2026-09-14 11:59 UTC | `19f9520bd1c13b0c9232bbb337d7c52bf3ff2236f391ad823457fc3dbd0ec31e` | R6 |
| 4 | B1-10 | [Dostępność zaczyna się w toalecie, łazience i łóżku](https://niepelnosprawni.pl/dostepnosc/dostepnosc-zaczyna-sie-w-toalecie-lazience-i-lozku) | Mateusz Różański / Niepelnosprawni.pl | 2025-11-20 | 2026-09-14 11:59 UTC | `1ef613f7e916e1d70a66419f64ca7fcb7cbc368510cc56aee4c5277444826da6` | R5 |
| 5 | B1-08 | [Czy strony urzędów są dostępne?](https://pzn.org.pl/czy-strony-urzedow-sa-dostepne/) | Centrum Komunikacji PZN | 2025-10-17 | 2026-09-14 11:59 UTC | `51b5e11393e828f0d5ca8d5f6cba1ca3f08ee2f7fbb5e5d6ddc2f8ae0c345f50` | R4 |
| 6 | B1-09 | [Jak prowadzić testy dostępności?](https://testerzy.pl/baza-wiedzy/artykuly/jak-prowadzic-testy-dostepnosci) | redakcja testerzy.pl | 2026-06-23 | 2026-09-14 11:59 UTC | `7d1d2217af4f87b98e98487270a7ec5ac6ebd4f146f31a6f362ffab91b2e2b1c` | R5 |
| 7 | B1-02 | [Dostępność cyfrowa a portale społecznościowe](https://www.gov.pl/web/dostepnosc-cyfrowa/dostepnosc-cyfrowa-a-portale-spolecznosciowe) | Adam Pietrasiewicz, aktualizacja Jakub Dębski / gov.pl | aktualizacja 2021-01-22 | 2026-09-14 11:59 UTC | `854c1cd0949cad14b85b860aeb292327fc7f7c30c68096fcd5f91f2e0890ab92` | R1 |
| 8 | B1-04 | [Jak zacząć testować strony WWW pod kątem dostępności cyfrowej?](https://sii.pl/blog/jak-zaczac-testowac-strony-www-pod-katem-dostepnosci-cyfrowej/) | Kinga Witko / Sii Polska | 2026-02-11 | 2026-09-14 11:59 UTC | `8d3b55f29dbfc70657b10013ae11ef15e5782e3a3302bf343c322b901ec935ec` | R2 |
| 9 | B1-01 | [Jakie akty prawne dotyczą dostępności cyfrowej](https://www.gov.pl/web/dostepnosc-cyfrowa/jakie-akty-prawne-dotycza-dostepnosci-cyfrowej) | zespół Dostępności Cyfrowej / gov.pl | brak daty w widoku strony | 2026-09-14 11:59 UTC | `ab52cc8481aa06ee6352c14bce0d092f027dde881e531f9b3ee12edfaf6a963f` | R1 |
| 10 | B1-05 | [WCAG i Europejski Akt o Dostępności – kompletny przewodnik dla przedsiębiorców](https://blog.sky-shop.pl/wcag-i-europejski-akt-o-dostepnosci-kompletny-przewodnik-dla-przedsiebiorcow/) | Katarzyna Kwartnik / Sky-Shop | aktualizacja 2026-08-22 | 2026-09-14 11:59 UTC | `ac61ac2b3fe17fb3a0bf9e717dc74a8a5473f7876f4da352eb19c05245a0e43a` | R3 |
| 11 | B1-11 | [Polski Akt o Dostępności: czym jest i jak się do niego przygotować](https://akademiacyfryzacji.gs1.pl/baza_wiedzy/polski-akt-o-dostepnosci-czym-jest-i-jak-sie-do-niego-przygotowac/) | Paulina Chełstowska / GS1 Polska | aktualizacja 2026-06-22 | 2026-09-14 11:59 UTC | `d37cd9f6f13cae2304640d699cd0a4f64d7106f8343004740091313dbed00103` | R6 |
| 12 | B1-03 | [XYZ pierwszym ogólnopolskim medium bez barier](https://niepelnosprawni.pl/dostepnosc/xyz-pierwszym-ogolnopolskim-medium-bez-barier) | redakcja Niepelnosprawni.pl | aktualizacja 2026-06-25 | 2026-09-14 11:59 UTC | `f8a9decc0e1fb624337fd3b8532c82f384a6311849bbf0b813751aaa12dead03` | R2 |

## 3. Wcześniej zamrożone rezerwy

Rezerwy są przypisane do odpowiednich profili, ale kod profilu pozostaje w
rejestrze kandydatów, a nie w neutralnym manifeście dla oceniających.

| ID | Publikacja | Autor / miejsce | Data lub znana wersja | Kontrola publicznej wersji |
| --- | --- | --- | --- | --- |
| R1 | [Kto, za co odpowiada w zakresie dostępności cyfrowej](https://www.gov.pl/web/dostepnosc-cyfrowa/kto-za-co-odpowiada-w-zakresie-dostepnosci-cyfrowej) | zespół Dostępności Cyfrowej / gov.pl | brak daty w widoku strony | 2026-09-14 11:59 UTC |
| R2 | [Dostępność cyfrowa w praktyce, czyli technologia dla wszystkich](https://devstyle.pl/dostepnosc-cyfrowa-w-praktyce-czyli-technologia-dla-wszystkich) | Julia Dündar / devstyle.pl | 2025-11-20 | 2026-09-14 11:59 UTC |
| R3 | [Standard WCAG 2.2 – nowy standard dostępności cyfrowej od czerwca 2025 roku](https://www.ifirma.pl/blog/standard-wcag-2-2-od-kiedy-obowiazuje-i-jakie-sa-jego-wytyczne/) | Adrianna Glapiak / iFirma | 2025-05-21 | 2026-09-14 11:59 UTC |
| R4 | [Raport dostępności cyfrowej e-commerce'u w Polsce](https://kinaole.co/dostepnosc-ecommerce/) | Piotr Źrołka i zespół / Kinaole | brak daty w metadanych strony | 2026-09-14 11:59 UTC |
| R5 | [Od rampy do smartfona. Bardzo krótka historia dostępności w XXI wieku](https://niepelnosprawni.pl/dostepnosc/od-rampy-do-smartfona-bardzo-krotka-historia-dostepnosci-w-xxi-wieku) | Maciej Piwowarczuk / Niepelnosprawni.pl | 2025-10-20 | 2026-09-14 11:59 UTC |
| R6 | [Audyt i wdrożenie WCAG 2.2 – kogo obowiązują i kiedy mija termin?](https://www.empressia.pl/blog/488-audyt-i-wdrozenie-wcag-2-2-kogo-obowiazuja-i-kiedy-mija-termin) | Beata Cygan / Empressia | 2025-04-15 | 2026-09-14 11:59 UTC |

## 4. Bramki przed startem ocen

Oceny B1 pozostają zablokowane do czasu łącznego spełnienia warunków:

1. właściciel projektu zatwierdzi niniejszy korpus;
2. prywatny manifest P01–P05 potwierdzi brak kolizji URL;
3. wszystkie materiały główne i centralne zostaną zamrożone, zahaszowane i
   wpisane do metryk;
4. pakiet metodologii i środowisko ocen zostaną zamrożone;
5. zostanie potwierdzona rzeczywista izolacja A/B.

Żaden wynik, ocena A–L, przewidywany problem ani oczekiwany werdykt nie został
przypisany do publikacji.

## 5. Kontrola techniczna przed publikacją

Kontrolę wykonano 14 września 2026 r. przed utworzeniem commita:

- 71 z 71 testów przeszło, w tym 6 nowych testów rejestrów B1;
- wszystkie pliki Pythona przeszły kontrolę składni;
- 12 schematów jest poprawnymi dokumentami JSON, a lokalne `$ref` są
  rozwiązywalne;
- publiczne źródła 0.3 i ich kopie w pakiecie skill są bajtowo zgodne;
- dwa niezależne zbudowania pakietu dały identyczne archiwa ZIP o SHA-256
  `baaf499da5b9a0e09381a0e356e3687e52f48b0b0f80d1218e75454d8e206355`;
- archiwum zawiera 25 plików i przechodzi test integralności;
- `git diff --check` nie zgłasza błędów;
- wersje 0.1 i 0.2 pozostały niezmienione;
- dokumenty stanu rozróżniają wcześniejszy brak B1 od obecnych prac
  przygotowawczych i potwierdzają, że ocen B1 ani B2 nie rozpoczęto.
