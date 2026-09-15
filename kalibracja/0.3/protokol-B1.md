# Protokół B1 — test nieobecnych progów metodologii 0.3

**Wersja protokołu:** 1.0
**Data zatwierdzenia założeń:** 14 września 2026 r.
**Metodologia:** `0.3-draft`
**Status:** protokół zamrożony przed wyszukiwaniem i ocenami
**Zakres:** dobór korpusu i wykonanie B1; B2 pozostaje poza zakresem

## 1. Cel

B1 sprawdza, czy metodologia 0.3 pozwala poprawnie i powtarzalnie rozpoznać
sytuacje nieobecne w podstawowym polskim pilotażu. Badanie ma sondować granice,
ale nie może przypisywać publikacjom wyniku przed niezależną oceną.

Badanie ma sprawdzić co najmniej:

- werdykt `rzetelny`;
- werdykt `rzetelny_z_niewielkimi_zastrzezeniami`;
- werdykt `nierzetelny`;
- werdykt `nie_mozna_rozstrzygnac`;
- prawidłowe `nd` w co najmniej dwóch różnych wymiarach A–L;
- możliwy problem krytyczny.

B1 nie mierzy częstości tych wyników w polskich publikacjach, nie jest próbą
reprezentatywną i nie sprawdza przenośności między różnymi systemami lub typami
oceniających. Przenośność pozostaje przedmiotem przyszłego B2.

## 2. Podstawa

Protokół uwzględnia:

- samodzielny standard i kotwice 0.3;
- wyniki wcześniejszego zestawu diagnostycznego i podstawowego pilotażu pięciu
  polskich publikacji;
- protokół, rejestry i wyniki kalibracji 0.2;
- wdrożone zmiany S1–S10;
- kanoniczną metrykę i format porównania pary 0.3.

W polskim pilotażu wszystkie dziesięć przebiegów zakończyło się jednym rodzajem
werdyktu. Nie wystąpiły `nd`, problem krytyczny ani brak możliwości
rozstrzygnięcia. B1 uzupełnia wyłącznie tę lukę i nie przelicza dawnych wyników.

## 3. Pytania badawcze

1. Czy cztery brakujące werdykty mogą zostać uzyskane zgodnie z regułami 0.3,
   bez dostrajania oceny do celu badania?
2. Czy dwa odizolowane przebiegi A i B rozpoznają te same werdykty?
3. Czy oceniający odróżniają prawidłowe `nd` od braku danych, źródeł,
   kompletności albo kompetencji?
4. Czy `nd` jest powtarzalne w co najmniej dwóch różnych wymiarach?
5. Czy problem krytyczny jest odróżniany od problemu dużego przez zastosowanie
   wszystkich czterech przesłanek krytyczności?
6. Czy reguły S1–S10 są stosowane spójnie w zakresie atomizacji, porównania
   twierdzeń, grupowania problemów, H, grupowego L, profilu odbiorców, bariery
   językowej, bezpiecznego polecenia, wersji historycznej i metryki?
7. Jakie granice pozostają niestabilne mimo użycia tej samej metody, materiału
   i środowiska?

Nie zakłada się oczekiwanego rozkładu wyników ani hipotezy, ile publikacji
otrzyma poszczególny werdykt.

## 4. Projekt i liczebność

Korpus główny obejmuje dokładnie dwanaście publikacji: po dwie publikacje dla
każdego z sześciu profili sondy opisanych w rozdziale 5. Każda publikacja
otrzymuje dwa niezależne przebiegi A i B. Seria główna obejmuje więc 24 oceny.

Przed ocenami zamraża się także sześć publikacji rezerwowych: po jednej dla
każdego profilu. Rezerwa nie jest częścią serii głównej. Może wejść do jednej
dodatkowej fali wyłącznie według rozdziału 15.

Wariant minimalny wynosiłby sześć publikacji i dwanaście ocen, lecz nie jest
stosowany w tej serii. Zatwierdzono wariant rekomendowany 12 + 6.

## 5. Profile sondy

Profil opisuje widoczną przed oceną budowę, zakres albo sposób udokumentowania
tekstu. Nie jest przewidywanym werdyktem, oceną jakości ani listą spodziewanych
błędów.

| Kod | Obiektywna charakterystyka przed oceną |
| --- | --- |
| P1 | Wąski materiał z jawnymi odwołaniami do identyfikowalnych źródeł, ograniczonym zakresem i twierdzeniami możliwymi do zewnętrznego sprawdzenia. |
| P2 | Materiał łączący główny wywód z co najmniej dwoma rodzajami twierdzeń pomocniczych, na przykład faktograficznymi, terminologicznymi, prawnymi albo technicznymi. |
| P3 | Szeroki tekst instruktażowy zawierający kategoryczne, powszechne albo bezwarunkowe zalecenia przeznaczone do praktycznego użycia. |
| P4 | Materiał, którego co najmniej jedno centralne twierdzenie zależy od danych, metody, badania albo wersji niewłączonej do publikacji i nieudostępnionej przez autora. Braku nie wolno tworzyć przez pominięcie dostępnego materiału. |
| P5 | Materiał, którego zadeklarowany zakres może uczciwie nie obejmować wybranego wymiaru. W korpusie głównym jedna publikacja ma sondować C, a druga J; nie przesądza to zastosowania `nd`. |
| P6 | Bezpośrednio wykonalna instrukcja dotycząca działania o możliwych poważnych skutkach dla dostępności, praw lub decyzji odbiorcy, bez widocznego w tekście zabezpieczenia, testu kontrolnego albo warunku konsultacji. Nie sprawdza się na tym etapie poprawności instrukcji. |

Kandydat może pasować do kilku profili. Przypisuje się go do pierwszego profilu,
dla którego został zarejestrowany podczas wykonania zamrożonej kolejności
zapytań. Ten sam URL nie może wystąpić w więcej niż jednym profilu.

## 6. Warunki włączenia

Publikacja kwalifikuje się, jeżeli:

1. jest napisana po polsku;
2. dostępność jest jej głównym tematem;
3. pełna treść główna jest publicznie dostępna bez logowania i opłaty;
4. zawiera co najmniej pięć materialnych twierdzeń możliwych do rozpoznania bez
   sprawdzania ich prawdziwości;
5. można ustalić kanoniczny URL, tytuł, miejsce publikacji, datę dostępu oraz
   autora, zespół lub podpis redakcyjny;
6. można pozyskać i zahaszować analizowaną treść jako `raw_bytes`,
   `rendered_capture` albo `canonical_text`;
7. nie została wcześniej oceniona według metodologii 0.1, 0.2 ani 0.3 w tym
   projekcie;
8. nie jest kopią albo nieznacznie zmienioną wersją innego kandydata;
9. autor nie jest osobą tworzącą metodologię lub wykonującą B1;
10. spełnia obiektywne cechy jednego profilu sondy.

Dla P4 pełna publikacja musi być dostępna, ale może ona sama nie udostępniać
danych, metody albo wersji, na których opiera centralne twierdzenie. Nie wolno
ukrywać przed oceną materiału, który został odnaleziony i jest dostępny.

Nie stosuje się dolnej granicy daty publikacji. Starsza publikacja może wejść do
puli, jeżeli da się rozdzielić wersję historyczną od bieżącej użyteczności
zgodnie z S9.

## 7. Warunki wyłączenia

Kandydata wyłącza się, jeżeli:

- dostępność jest jedynie wzmianką poboczną;
- pełna treść główna wymaga logowania, opłaty albo jest niedostępna;
- tekst jest krótką zapowiedzią, reklamą lub komunikatem bez pięciu
  materialnych twierdzeń;
- nie można wiarygodnie zidentyfikować publikacji lub analizowanej wersji;
- został wcześniej oceniony albo szczegółowo omówiony w projekcie;
- kandydatura została zgłoszona z powodu znanego wyniku lub wcześniejszej
  analizy jakości;
- istnieje konflikt interesów, którego nie da się ograniczyć;
- nie spełnia dowolnego warunku włączenia.

Powód wyłączenia musi być obiektywny. Nie wolno używać określeń takich jak
„dobry”, „błędny”, „nierzetelny”, „prawdopodobnie krytyczny” albo wpisywać
przewidywanego werdyktu.

## 8. Wyszukiwanie

Przed rozpoczęciem wyszukiwania zamraża się:

- sześć grup zapytań odpowiadających profilom P1–P6;
- kolejność zapytań;
- źródła i rodzaje serwisów;
- limit pierwszych 20 unikalnych wyników sprawdzanych dla jednego zapytania;
- warunki włączenia i wyłączenia;
- zasady kanonizacji URL;
- pola dziennika wyszukiwania.

Stosuje się publiczne wyszukiwarki oraz bezpośrednie wyszukiwanie w serwisach
instytucji publicznych, organizacji społecznych i eksperckich, uczelni,
wydawców, firm i autorów. Nie używa się rekomendacji opartych na wcześniejszym
werdykcie publikacji.

Dla każdej sesji zapisuje się datę i czas, dokładne zapytanie albo adres źródła,
kolejność sprawdzanych wyników, decyzję oraz obiektywny powód wyłączenia.

Podczas kwalifikacji wolno odczytać tytuł, metadane, strukturę, wprowadzenie,
nagłówki i tyle treści, ile jest potrzebne do potwierdzenia liczby twierdzeń,
zakresu oraz cechy profilu. Nie wolno sprawdzać prawdziwości twierdzeń,
porównywać ich ze źródłami ani przewidywać oceny.

## 9. Pula kandydatów

Zamknięta pula zawiera co najmniej 24 kwalifikujące się publikacje: co najmniej
cztery dla każdego profilu P1–P6.

Rejestr kandydatów zawiera:

- identyfikator;
- profil sondy;
- tytuł, autora lub zespół, miejsce i URL;
- datę publikacji albo aktualizacji, jeżeli jest podana;
- datę i czas kontroli;
- podstawę kwalifikacji ograniczoną do cech strukturalnych;
- skrót wyboru;
- status: główna, rezerwowa albo niewybrana.

Rejestr nie zawiera przewidywanego werdyktu, wyniku A–L, spodziewanych błędów
ani oceny prawdziwości. Oceniający A i B nie otrzymują rejestru kandydatów ani
informacji o profilu przypadku.

## 10. Deterministyczny wybór

Po zamknięciu puli dla każdego kandydata oblicza się SHA-256 z połączenia:

`ocena-0.3-B1-korpus-v1|<kod_profilu>|<kanoniczny_url>`

W każdym profilu kandydatów porządkuje się rosnąco według skrótu. Dwie pierwsze
publikacje wybiera się do korpusu głównego, a trzecią jako rezerwę.

Wybór musi łącznie zapewnić:

- co najmniej osiem różnych domen;
- co najmniej ośmiu różnych autorów lub zespołów;
- nie więcej niż dwie publikacje jednego autora albo zespołu;
- nie więcej niż dwie publikacje z jednej domeny;
- co najmniej cztery rodzaje miejsc publikacji;
- co najmniej cztery obszary tematyczne dostępności;
- w P5 jedną sondę możliwego `nd` dla C i jedną dla J.

Jeżeli kandydat narusza warunek różnorodności, pomija się go i wybiera kolejną
pozycję z tego samego profilu. Każde pominięcie zapisuje się bez oceny jakości.

Rezerwa pozostaje przypisana do profilu. Nie wolno zamieniać rezerw między
profilami po poznaniu wyników.

## 11. Zamrożenie korpusu i kolejności

Przed pierwszym przebiegiem publikuje się rejestr korpusu zawierający:

- identyfikator przypadku;
- tytuł, autora lub zespół, miejsce, URL i datę;
- znaną wersję oraz datę i czas pobrania;
- planowaną podstawę haszowania;
- identyfikator rezerwy;
- kolejność wykonania.

Rejestr korpusu nie zawiera profilu sondy. Powiązanie profilu z publikacją jest
widoczne w rejestrze kandydatów, do którego przebiegi A i B nie mają dostępu.

Kolejność ustala się rosnąco według SHA-256 z połączenia:

`ocena-0.3-B1-kolejnosc-v1|<case_id>|<kanoniczny_url>`

Commit zawierający protokół, dziennik, zamkniętą pulę i rejestr korpusu jest
identyfikatorem zamrożenia B1. Ocen nie wolno rozpocząć przed zatwierdzeniem
korpusu przez właściciela projektu.

## 12. Zamrożenie materiału i metryka

Przed przebiegiem krytycznym każdego A i B tworzy się `metryka.json` zgodny z
`metryka-0.3.schema.json`. Metryka zapisuje co najmniej:

- identyfikatory serii, przypadku, analizy i przebiegu;
- wersję i commit metodologii oraz SHA-256 użytego pakietu;
- czas, język i identyfikację oceniającego;
- publikację i wszystkie materiały;
- SHA-256 każdego materiału i podstawę haszowania;
- narzędzia, dostęp do pamięci, projektu i repozytoriów prywatnych;
- warunki izolacji i ograniczenia.

A i B otrzymują tę samą zamrożoną wersję publikacji i tych samych materiałów
centralnych. Po rozpoczęciu części krytycznej wolno uzupełnić w metryce tylko
czas zakończenia i ograniczenia ujawnione podczas wykonania.

Kolejność walidacji wynosi:

1. `metryka.json`;
2. `wynik.json` z metryką;
3. `wyciag-kalibracyjny.json` z wynikiem;
4. po zamknięciu A i B — `porownanie-pary.json` z oboma wynikami.

## 13. Niezależne przebiegi

Każda publikacja otrzymuje dwa przebiegi A i B wykonane przez ten sam typ
systemu lub oceniającego. Użycie innego typu systemu należałoby do B2.

Przebiegi A i B:

- rozpoczynają się w dwóch pustych, odizolowanych kontekstach;
- otrzymują identyczne polecenie poza identyfikatorem przebiegu;
- używają tej samej metody i zamrożonego materiału;
- nie widzą wyniku, raportu ani wyciągu drugiego przebiegu;
- nie widzą wyników wcześniejszych przypadków;
- nie otrzymują kodu profilu ani oczekiwanego wyniku;
- nie korzystają z wcześniejszych analiz publikacji;
- zapisują wszystkie znane cechy środowiska i izolacji.

Każda publikacja jest osobnym przypadkiem. Koordynator uruchamia przebiegi,
zbiera i waliduje pliki, lecz porównuje je dopiero po zamknięciu A i B.
Użytkownik nie musi ręcznie tworzyć kontekstów ani przeklejać poleceń.

Jeżeli rzeczywistej izolacji nie da się zapewnić, B1 nie rozpoczyna się, a
ograniczenie zostaje zgłoszone właścicielowi projektu.

## 14. Dokumentowanie przebiegów

Każdy przebieg tworzy w prywatnym laboratorium:

- użyte polecenie;
- `metryka.json`;
- pełny raport `analiza.md`;
- `wynik.json`;
- `wyciag-kalibracyjny.json`;
- krótki dziennik techniczny.

Każda para tworzy `porownanie-pary.md` i `porownanie-pary.json`. Nieudane próby
techniczne zachowuje się w dzienniku. Ponowienie otrzymuje nowy identyfikator,
ale nie jest dodatkową niezależną oceną.

Podejrzenia wad metodologii zapisuje się w rejestrze odchyleń i rozpatruje
dopiero po zamknięciu serii. Nie wolno zmieniać metody, kotwic, schematów,
polecenia ani słownika wartości podczas B1.

## 15. Brak sondowanego wyniku i rezerwa

Jeżeli publikacja nie daje wyniku, którego granicę miała sondować:

1. zachowuje się rzeczywisty wynik bez korekty;
2. nie usuwa się publikacji z korpusu;
3. nie wykonuje się poprawionej oceny;
4. wynik zalicza się do rzeczywiście zaobserwowanej kategorii;
5. decyzję o rezerwie podejmuje się dopiero po ukończeniu wszystkich 24
   przebiegów głównych i dwunastu porównań.

Dla każdego celu niezaobserwowanego stabilnie wolno uruchomić wyłącznie jedną,
wcześniej zamrożoną rezerwę przypisaną do właściwego profilu. Wszystkie użyte
rezerwy tworzą jedną dodatkową falę i są raportowane oddzielnie.

Jeżeli rezerwa także nie uruchomi celu, oznacza się go jako niezaobserwowany i
kończy badanie. Nie wolno wyszukiwać dalszych publikacji aż do uzyskania
pożądanego wyniku.

Publikację wolno zastąpić przed ukończeniem pierwszego przebiegu wyłącznie z
powodu usunięcia treści, utraty dostępu, wykrycia obiektywnego niespełnienia
warunku wejścia albo niemożności zamrożenia materiału. Awaria techniczna
powoduje ponowienie na tym samym materiale, nie wymianę publikacji.

## 16. Porównanie wyników

Dla każdej pary A/B raportuje się co najmniej:

- dokładną zgodność A–L;
- zgodność w granicy jednego punktu;
- średnią bezwzględną różnicę i jej kierunek;
- wyniki według wymiaru;
- zgodność werdyktu i bezpiecznego polecenia;
- profile odbiorców oraz grupowe H i L;
- wszystkie zastosowania i rozbieżności `nd`;
- pokrycie map twierdzeń i wyniki relacji 1:1;
- różnice atomizacji;
- zgodność znaczenia i grupowania problemów;
- zgodność dotkliwości, centralności i ryzyka;
- problemy duże i krytyczne osobno;
- rozstrzygnięcia dotyczące wersji historycznej;
- kompletność i spójność metryki.

Każdy wymagany wynik otrzymuje po zamknięciu serii status:

- `zaobserwowany_stabilnie` — A i B niezależnie uzyskały ten sam wynik;
- `granica_uruchomiona_niestabilnie` — wynik wystąpił tylko w A albo B;
- `niezaobserwowany` — wynik nie wystąpił w żadnym przebiegu.

`nd` liczy się jako stabilne tylko wtedy, gdy A i B zastosują je w tym samym
wymiarze i oba uzasadnienia spełnią wszystkie reguły rozdziału 12 standardu.

Problem krytyczny liczy się jako stabilny, gdy A i B dopasują ten sam problem
znaczeniowy i niezależnie potwierdzą: błąd lub bardzo wysoką pewność, prawdopodobne
zastosowanie, możliwą poważną szkodę oraz brak prostego zabezpieczenia.

Wyniki B1 porównuje się opisowo z polskim pilotażem. Nie łączy się prób, nie
uśrednia A i B i nie wyprowadza werdyktu z sumy ocen. Miary statystyczne są
pomocnicze ze względu na celowy i mały korpus.

## 17. Kryteria zakończenia

B1 jest zakończone proceduralnie, gdy:

1. protokół, korpus, kolejność, metoda, schematy, środowisko i materiały zostały
   zamrożone przed ocenami;
2. wszystkie 24 przebiegi główne są ukończone i porównywalne;
3. wszystkie wymagane pliki i pary przeszły walidację;
4. wykonano kompletne dopasowanie semantyczne twierdzeń i problemów;
5. zakończono jedną falę rezerwową, jeżeli była wymagana;
6. zapisano wszystkie odchylenia i nie zmieniono metody w trakcie serii.

Cel badawczy jest w pełni osiągnięty, gdy stabilnie zaobserwowano cztery
wymagane werdykty, prawidłowe `nd` w dwóch różnych wymiarach oraz co najmniej
jeden problem krytyczny.

Proceduralnie poprawne B1 kończy się również wtedy, gdy któregoś wyniku nie
zaobserwowano po dopuszczonej rezerwie. Brak trafienia jest wynikiem badania,
nie podstawą do dalszego dobierania tekstów.

## 18. Materiały prywatne i bezpieczne podsumowanie

W prywatnym laboratorium przechowuje się pełne kopie publikacji i materiałów,
polecenia, surowe dzienniki, kompletne analizy, wyniki, wyciągi, porównania oraz
informacje techniczne środowiska. Dostęp otrzymują wyłącznie osoby i procesy
wykonujące B1. Nie zapisuje się danych logowania.

W publicznym repozytorium przechowuje się protokół, dziennik wyszukiwania,
rejestr kandydatów, zamrożony korpus, obiektywne przyczyny wyłączeń, rejestr
odchyleń i późniejsze bezpieczne wyniki zagregowane.

Publicznie nie umieszcza się pełnych kopii chronionych publikacji, długich
cytatów, surowych raportów ani powiązania nazwanej publikacji z negatywnym
werdyktem bez osobnej decyzji właściciela projektu.

Materiały prywatne zachowuje się co najmniej do decyzji o wersji 0.3. Dwanaście
miesięcy po zamknięciu B1 przeprowadza się przegląd retencji. Manifesty, skróty
i bezpieczne wyniki mogą pozostać, a zbędne kopie chronionych treści usuwa się
po udokumentowanym przeglądzie.

## 19. Nakład i ryzyka

Orientacyjny nakład dla serii głównej:

| Etap | Nakład wykonawczy |
| --- | ---: |
| Wyszukanie i kwalifikacja puli | 8–14 godzin |
| Zamrożenie materiałów i metryk | 6–10 godzin |
| 24 niezależne oceny | 36–60 godzin |
| 12 porównań A/B | 12–20 godzin |
| Kontrola i raport | 4–8 godzin |

Łącznie oznacza to około 66–112 godzin pracy wykonawczej i orientacyjnie 5–10
dni kalendarzowych przy bezpiecznej równoległości. Pełna fala rezerwowa może
zwiększyć nakład najwyżej o około 50%.

Główne ryzyka i zabezpieczenia:

- nietrafienie w cel — dwie publikacje na profil i jedna zamrożona rezerwa;
- dobór pod wynik — zamknięta pula, brak weryfikacji i wybór według SHA-256;
- przeciek A/B — puste konteksty bez pamięci i wyników innych przebiegów;
- zmiana strony — zamrożone kopie, skróty i identyczny materiał A/B;
- mylenie braku danych z `nd` — obowiązkowy czteroelementowy test `nd`;
- mylenie ryzyka z krytycznością — obowiązkowe cztery przesłanki problemu
  krytycznego;
- mała próba — wnioski dotyczą granic metody, nie częstości zjawisk;
- wada metody odkryta w serii — zapis bez zmiany zasad do końca B1.

## 20. Pliki serii

Przed ocenami w publicznym repozytorium powstają:

- `kalibracja/0.3/protokol-B1.md`;
- `kalibracja/0.3/dziennik-wyszukiwan-B1.md`;
- `kalibracja/0.3/rejestr-kandydatow-B1.md`;
- `kalibracja/0.3/rejestr-korpusu-B1.md`;
- `kalibracja/0.3/rejestr-odchylen-B1.md`.

Po zakończeniu ocen powstanie `kalibracja/0.3/wyniki-B1.md`.

W prywatnym laboratorium powstaną pliki serii i zestawy przypadku opisane w
zatwierdzonym projekcie B1. Lokalizacji prywatnego laboratorium nie publikuje
się w repozytorium.

Protokół nie zmienia standardu, kotwic, schematów, walidatora ani pakietu skill.
Nie rozpoczyna B2, nie zamraża wydania 0.3 i nie zezwala na scalenie PR.
