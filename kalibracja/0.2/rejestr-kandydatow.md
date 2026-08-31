# Rejestr kandydatów do kalibracji 0.2

**Data zamknięcia puli:** 31 sierpnia 2026 r.  
**Czas zamknięcia:** 05:44 UTC  
**Protokół:** `kalibracja/0.2/protokol-doboru-publikacji.md`  
**Język korpusu:** polski  

## Korekty metadanych po zamknięciu puli

Po odczytaniu pełnych publikacji potwierdzono, że autorem P01 jest Wojciech Kutyła, a autorką T04 jest Małgorzata Naumczuk. Bieżąca strona L02 lub jej metadane używają także wariantu tytułu „Dostępność cyfrowa 2025: Jak przygotować się do nowej ustawy?”.

Korekty nie zmieniają kwalifikacji, skrótów, wyboru ani kolejności publikacji. Pierwotny zamrożony stan zachowuje commit `14241000b8c85d31d91efa67873721bf344c16af`.

## Zasada

Pula zawiera dokładnie 24 publikacje spełniające warunki wejścia: po 6 technicznych, prawnych i komercyjnych oraz po 3 oparte na doświadczeniach użytkowników i popularne. Na tym etapie sprawdzono wyłącznie datę, publiczną dostępność pełnej treści, temat, możliwość rozpoznania wersji i obecność co najmniej pięciu materialnych twierdzeń. Nie oceniano prawdziwości twierdzeń ani nie przewidywano werdyktu.

Wartość w kolumnie `SHA-256` obliczono zgodnie z protokołem z ciągu `ocena-0.2-korpus-2026-08-21|` oraz kanonicznego URL.

## Techniczne lub normatywne

| ID | Publikacja | Autor / zespół | Data | SHA-256 | Status |
|---|---|---|---|---|---|
| T01 | [Jak zacząć testować strony WWW pod kątem dostępności cyfrowej?](https://sii.pl/blog/jak-zaczac-testowac-strony-www-pod-katem-dostepnosci-cyfrowej/) | Kinga Witko, Sii Polska | 2026-02-11 | `6613f00fb503db49ad4df245e5060e83782fd13218baaa827b0d2ed8830d0249` | kwalifikuje się |
| T02 | [Standard WCAG 2.2 – od kiedy obowiązują nowe wytyczne?](https://www.ifirma.pl/blog/standard-wcag-2-2-od-kiedy-obowiazuje-i-jakie-sa-jego-wytyczne/) | Adrianna Glapiak, iFirma | 2025-05-21 | `594ea50ccb00ed790e010644416204d7050a25e28be4def5101a435c81d151a4` | kwalifikuje się; rezerwa |
| T03 | [WCAG 2.2 – co musisz wiedzieć o standardzie dostępności cyfrowej?](https://sare.pl/blog/poradniki/wcag-2-2-co-musisz-wiedziec-o-standardzie-dostepnosci-cyfrowej/) | Magdalena Niedobecka, SARE | 2025-01-30 | `f9c2766dcc8fff802e248a509033d261bcae89d218955ea99673ba81bce41b57` | kwalifikuje się |
| T04 | [Dostępność cyfrowa 2.2 i EAA](https://adequate.digital/dostepnosc-cyfrowa-2-2-i-eu-accessibility-act/) | Małgorzata Naumczuk, Adequate Digital | 2024-02-26 | `116b1d8b0c0970e800e2bb1f098685cf313e1ce14153cc3418eb50f784523f5e` | wybrana |
| T05 | [Dostępność cyfrowa w praktyce, czyli technologia dla wszystkich](https://devstyle.pl/dostepnosc-cyfrowa-w-praktyce-czyli-technologia-dla-wszystkich) | Julia Dündar, devstyle.pl | 2025-11-20 | `628d4a7a0534d821fdb39ddbaa9e65617010d2e5fd97939cc9b8c606adefa21e` | kwalifikuje się |
| T06 | [Dostępność cyfrowa w ustawach i dyrektywach](https://testerzy.pl/baza-wiedzy/artykuly/dostepnosc-cyfrowa-w-ustawach-i-dyrektywach) | Redakcja Testerzy.pl | 2024-10-23 | `44933fa3d1688823e697af6d16e88c0212b373a11ca56f632e8d44b9bad4180b` | wybrana |

## Prawne lub dotyczące zgodności

| ID | Publikacja | Autor / zespół | Data | SHA-256 | Status |
|---|---|---|---|---|---|
| L01 | [Polski Akt o Dostępności — usługi handlu elektronicznego](https://www.gov.pl/web/dostepnosc-cyfrowa/polski-akt-o-dostepnosci--uslugi-handlu-elektronicznego) | Małgorzata Wenek; aktualizacja Anna Dębska | 2025-06-27; aktualizacja 2025-08-14 | `d47ab182bb8a86f8ce90433a7c06c1c81877d978336501263d925d53c1a03e0e` | kwalifikuje się |
| L02 | [Nowe obowiązki w zakresie dostępności cyfrowej w 2025 roku](https://staniekandpartners.pl/blog/dostepnosc-cyfrowa-2025-ustawa-obowiazki/) | Paweł Żychowski, Staniek & Partners | 2025-04-15 | `7bee84fb9f6f24335817433e1146fe630a5045bb95586e0466f5810f039876e0` | wybrana |
| L03 | [Polski Akt o Dostępności – jakie obowiązki czekają przedsiębiorców? – cz. I](https://ziemskibiznes.pl/kompleksowa-obsluga/polski-akt-o-dostepnosci-jakie-obowiazki-czekaja-przedsiebiorcow-cz-i/) | Anna Przygocka, Weronika Miara | 2025-06-24 | `7e7f408901a4b8796ec7f472311651011b3831600b9150ea654388f1c395aa34` | kwalifikuje się |
| L04 | [Rewolucja w dostępności: jak nowe regulacje zmienią oblicze branż od 2025 roku](https://www.parp.gov.pl/component/content/article/85761%3Arewolucja-w-dostepnosci-jak-nowe-regulacje-zmienia-oblicze-branz-od-2025-roku) | PARP | 2024-02-12 | `7e6ff87307de42a5eb6f78a74b47103e151b7c091e44c0421ad0e6daaf9ddf32` | kwalifikuje się; rezerwa |
| L05 | [Polski Akt o Dostępności: czym jest i jak się do niego przygotować](https://akademiacyfryzacji.gs1.pl/baza_wiedzy/polski-akt-o-dostepnosci-czym-jest-i-jak-sie-do-niego-przygotowac/) | Paulina Chełstowska, GS1 Polska | 2025-03-25; aktualizacja 2026-06-22 | `f89aa1f641991ec4e927e5ce31f5b99d82ca63f926f47fb9a6e35c2eaf11a564` | kwalifikuje się |
| L06 | [Europejski Akt o Dostępności (EAA) – czym jest i co warto o nim wiedzieć?](https://wygodnezwroty.pl/dla-sklepow/blog/europejski-akt-o-dostepnosci) | Wygodne Zwroty | 2025-06-27; aktualizacja 2025-07-17 | `7c1bc21addbcb8f7ef88ec176946c159707657c9429c4f048150cc93ece27f20` | wybrana |

## Komercyjne lub praktyczne

| ID | Publikacja | Autor / zespół | Data | SHA-256 | Status |
|---|---|---|---|---|---|
| C01 | [Audyt i wdrożenie WCAG 2.2 – kogo obowiązują i kiedy mija termin?](https://www.empressia.pl/blog/488-audyt-i-wdrozenie-wcag-2-2-kogo-obowiazuja-i-kiedy-mija-termin) | Beata Cygan, Empressia | 2025-04-15 | `6fbe632629624160feb7724cf2d376cfb68b067ccb5aedcdcd6de2cdfc5502ec` | kwalifikuje się |
| C02 | [Europejski Akt o Dostępności w praktyce](https://www.shoper.pl/learn/artykul/europejski-akt-o-dostepnosci-co-musisz-wiedziec-jako-przedsiebiorca-dzialajacy-w-sieci) | zespół Shoper | 2025-02-11 | `a999b3e6c07228a7c82cbb6d443d0cb5933e7a71ee5d883e063864f4a675b018` | kwalifikuje się |
| C03 | [WCAG i Europejski Akt o Dostępności – kompletny przewodnik dla przedsiębiorców](https://blog.sky-shop.pl/wcag-i-europejski-akt-o-dostepnosci-kompletny-przewodnik-dla-przedsiebiorcow/) | Katarzyna Kwartnik, Sky-Shop | 2025-05-29; aktualizacja 2026-08-22 | `d413774d5b2722bda2e63c618ba853da9f298a171bc0c76c7c9c02560428533b` | kwalifikuje się |
| C04 | [Europejski Akt o Dostępności – jak dostosować sklep internetowy do jego wymogów?](https://www.ibif.pl/blog/sklepy-internetowe/europejski-akt-o-dostepnosci-jak-dostosowac-sklep-internetowy-do-jego-wymogow) | Magdalena Krawczyńska, IBIF | 2025-06-05 | `612249288446d294a44bc83fc41245b752a462fb40e20e81a34f1f94cdcf621f` | wybrana |
| C05 | [Nowe przepisy WCAG 2025](https://emeraldmedia.pl/nowe-przepisy-wcag-2025-co-musisz-wiedziec-o-obowiazkowej-dostepnosci-stron-i-sklepow-internetowych/) | zespół Emerald Media | 2025-05-27 | `66816f1c51d2336ed86151f4574d5c9df2a5bc18f4bfc652259083443e4650c7` | kwalifikuje się; rezerwa |
| C06 | [Deklaracja dostępności](https://webster-studio.pl/oferta/wdrozenia-wcag/deklaracja-dostepnosci) | Webster Studio | aktualizacja 2025-02-14 | `4f782ff6ac69950d14cf96ae4dd94fad1c6d8f7d6a1d5fb7b18e050403225cf9` | wybrana |

## Badania lub doświadczenia użytkowników

| ID | Publikacja | Autor / zespół | Data | SHA-256 | Status |
|---|---|---|---|---|---|
| U01 | [Internet bez barier? Osoby niewidome i słabowidzące o swoich doświadczeniach w sieci](https://journals.umcs.pl/lrp/article/view/16069) | Mikołaj Olszewski | 2024-05-10 | `24483c8e6323917331ff3595387fd70aedee840ac20cf1b8dc90bdf75fc8de55` | wybrana |
| U02 | [Czy strony urzędów są dostępne?](https://pzn.org.pl/czy-strony-urzedow-sa-dostepne/) | Centrum Komunikacji PZN | 2025-10-17 | `ef32fae290ed05c84e4192723b8f33f84ad3686c5c897a30579dd47c511c6bd4` | kwalifikuje się |
| U03 | [Dostępność cyfrowa dla osób niewidomych](https://imset.it/strefa-wiedzy/dostepnosc-cyfrowa-dla-osob-niewidomych-na-czym-polega-i-jak-udostepnic-strone-internetowa) | zespół Imset | 2025-09-08 | `995601e404b882ae0da02d460a97bb2d283053e4c863000a3c4f3eda6a866cbd` | kwalifikuje się; rezerwa |

## Popularne, opiniotwórcze, instytucjonalne lub mieszane

| ID | Publikacja | Autor / zespół | Data | SHA-256 | Status |
|---|---|---|---|---|---|
| P01 | [Co to jest dostępność cyfrowa i dlaczego warto o nią dbać?](https://helion.pl/blog/co-to-jest-dostepnosc-cyfrowa-i-dlaczego-warto-o-nia-dbac-152) | Wojciech Kutyła, Helion.pl | 2025-02-12 | `6ea27965b29eb2eb7eb7f0ffea739ecd5e619504e9ecc3902375aa22dbe4d307` | wybrana |
| P02 | [Dostępność cyfrowa to nie dodatek. To element dobrej usługi publicznej](https://lukasiewicz.gov.pl/dostepnosc-cyfrowa-to-nie-dodatek-to-element-dobrej-uslugi-publicznej/) | Sieć Badawcza Łukasiewicz | 2026-05-28 | `ea569c26615cc20aceb54d262f030e1cce7a85d35be8e04e97c868895f77cd3f` | kwalifikuje się |
| P03 | [Cyfrowy mur wart miliardy](https://nowymarketing.pl/cyfrowy-mur-wart-miliardy-dlaczego-dostepnosc-to-nowy-standard-konkurencyjnosci/) | Anna Krawczyk, NowyMarketing | 2026-08-04 | `a85e5272a06d7d65d996dbb8c3dc76c1975cb6a91d2dab83c8b5123c1211bfe0` | kwalifikuje się; rezerwa |

## Kontrola liczebności

| Kategoria | Wymagane minimum | W rejestrze |
|---|---:|---:|
| techniczne lub normatywne | 6 | 6 |
| prawne lub zgodnościowe | 6 | 6 |
| komercyjne lub praktyczne | 6 | 6 |
| badania lub doświadczenia użytkowników | 3 | 3 |
| popularne, opiniotwórcze, instytucjonalne lub mieszane | 3 | 3 |
| **Razem** | **24** | **24** |

Teksty zagraniczne i obcojęzyczne nie weszły do tej puli, ponieważ punkt 7 protokołu wymaga publikacji napisanej po polsku. Mogą zostać wykorzystane dopiero w osobnej serii z osobnym protokołem.
