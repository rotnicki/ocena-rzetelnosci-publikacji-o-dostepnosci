# Protokół B2 — przenośność metodologii 0.3 pomiędzy rodzinami AI

**Wersja protokołu:** 1.0  
**Data przygotowania:** 14 września 2026 r.  
**Metodologia:** `0.3-draft-S1-S15`  
**Commit metodologii:** `6bc8f21af1fda5f5ba3953970176126641033e12`  
**Status:** przygotowane wejście; oceny B2 nie zostały rozpoczęte

## 1. Cel

B2 sprawdza, czy trzy niezależne rodziny AI — ChatGPT, Gemini i Grok — potrafią
zastosować tę samą zamrożoną metodologię 0.3 do tych samych publikacji w sposób
powtarzalny i porównywalny. Badanie dotyczy przenośności metody pomiędzy
rodzinami modeli, a nie tego, która marka AI jest „najlepsza”.

B2 nie wykorzystuje ludzi jako oceniających. Człowiek zatwierdza projekt i
korpus, lecz nie wykonuje ocen ani nie rozstrzyga rozbieżności zamiast metody.

## 2. Pytania badawcze

1. Czy każda rodzina AI powtarza własny werdykt w przebiegach A/B?
2. Czy rodziny AI podobnie stosują oceny A–L oraz `nd`?
3. Czy podobnie rozpoznają twierdzenia, problemy i ich wielkość?
4. Czy podobnie wykonują test rozstrzygalności i czterech przesłanek
   krytyczności?
5. Czy różnice wynikają z interpretacji metody, możliwości modelu, dostępu do
   źródeł czy usterki technicznej?
6. Czy pakiet `SKILL.md` jest zrozumiały poza środowiskiem OpenAI bez zmiany
   znaczenia metodologii?

## 3. Projekt badania

Każda rodzina wykonuje dwa całkowicie odizolowane przebiegi A i B. Każdy
przebieg ocenia sześć publikacji w tej samej kolejności. Powstaje łącznie 36
ocen:

- ChatGPT A i B — 12 ocen;
- Gemini A i B — 12 ocen;
- Grok A i B — 12 ocen.

Każdy przebieg działa w osobnym prywatnym repozytorium. Repozytorium zawiera
identyczne zamrożone wejście oraz odmienną wyłącznie metrykę rodziny i
oznaczenia A/B.

## 4. Dobór korpusu bez znajomości wyników

Pula wejściowa obejmuje 24 publikacje zakwalifikowane strukturalnie przed B1.
Nie wykorzystuje się wyników B1, późniejszych analiz ani statusu publikacji w
serii B1.

Dla każdego z sześciu wcześniej zdefiniowanych profili P1–P6 oblicza się:

`SHA-256("ocena-0.3-B2-korpus-v1|<profil>|<kanoniczny_url>")`

Wybiera się najmniejszy skrót w profilu. Kandydat musi dać się utrwalić jako
pełny `canonical_text`. Jeżeli kontrolowane pobranie techniczne kończy się
błędem, wybiera się następny skrót z tego samego profilu i zapisuje powód bez
oceny treści. Profile i skróty nie trafiają do repozytoriów oceniających.

W ten sposób wybrano:

| ID | Publikacja | Miejsce | URL |
| --- | --- | --- | --- |
| B2-01 | Dostępność cyfrowa a portale społecznościowe | gov.pl | https://www.gov.pl/web/dostepnosc-cyfrowa/dostepnosc-cyfrowa-a-portale-spolecznosciowe |
| B2-02 | Dostępność cyfrowa w praktyce, czyli technologia dla wszystkich | devstyle.pl | https://devstyle.pl/dostepnosc-cyfrowa-w-praktyce-czyli-technologia-dla-wszystkich |
| B2-03 | WCAG 2.2 – co musisz wiedzieć o standardzie dostępności cyfrowej? | SARE | https://sare.pl/blog/poradniki/wcag-2-2-co-musisz-wiedziec-o-standardzie-dostepnosci-cyfrowej/ |
| B2-04 | Jak polski biznes wdraża dostępność? Wyniki badania BAF rok po wejściu w życie ustawy | Business Accessibility Forum | https://baforum.pl/a,223,jak-polski-biznes-wdraza-dostepnosc-wyniki-badania-baf-rok-po-wejsciu-w-zycie-ustawy |
| B2-05 | Od rampy do smartfona. Bardzo krótka historia dostępności w XXI wieku | Niepelnosprawni.pl | https://niepelnosprawni.pl/dostepnosc/od-rampy-do-smartfona-bardzo-krotka-historia-dostepnosci-w-xxi-wieku |
| B2-06 | Audyt i wdrożenie WCAG 2.2 – kogo obowiązują i kiedy mija termin? | Empressia | https://www.empressia.pl/blog/488-audyt-i-wdrozenie-wcag-2-2-kogo-obowiazuja-i-kiedy-mija-termin |

Pierwszy skrót P6 wskazał publikację Shopera. Serwer zwrócił HTTP 403 podczas
kontrolowanego pobrania, dlatego przed oceną i bez badania rzetelności użyto
drugiego skrótu P6 — publikacji Empressii.

## 5. Zamrożenie wejścia

Każdy przebieg otrzymuje bajtowo identyczne:

- samodzielną metodologię 0.3 po S1–S15;
- pakiet skill z `SKILL.md`;
- schematy, kotwice, szablony i walidator;
- sześć publikacji utrwalonych jako `canonical_text`;
- wspólny wykaz źródeł startowych;
- instrukcję wykonania, kolejność i strukturę wyników;
- manifest i `SHA256SUMS`.

Wspólna suma pakietu jest SHA-256 pliku `SHA256SUMS`. Metryka konkretnego
przebiegu nie należy do wspólnego pakietu i może różnić się wyłącznie nazwą
repozytorium, rodziną AI oraz oznaczeniem A/B. Zamrożenie obowiązuje tylko w B2
i nie oznacza wydania `v0.3.0` ani ogólnego zamrożenia projektu 0.3.

SHA-256 wspólnego pakietu wejściowego:
`63857cf3311cc2c8a66f592d5fc35a471d7e118efc2f4a8233fd77dfb8aab60c`.

## 6. Izolacja

Każda z sześciu kombinacji rodzina–przebieg działa w osobnym prywatnym
repozytorium. Oceniający ma dostęp wyłącznie do własnego repozytorium i
publicznych źródeł potrzebnych do weryfikacji. Nie otrzymuje:

- wyników polskiego pilotażu ani B1;
- pełnych raportów wcześniejszych ocen;
- profilu, skrótu lub powodu wyboru publikacji;
- wyników innej rodziny;
- wyniku drugiego przebiegu A/B;
- historii rozmowy koordynatora.

Gemini A, Gemini B, Grok A i Grok B są uruchamiane w nowych rozmowach. Dostęp
GitHub każdego środowiska ogranicza się do właściwego repozytorium. ChatGPT A i
B zostaną uruchomione przez koordynatora jako świeże zadania bez historii i bez
kontekstu tego wątku. Jeżeli techniczne ograniczenie dostępu nie zapewni tych
warunków, dany przebieg nie może się rozpocząć.

## 7. Wspólne warunki narzędziowe

Każdy przebieg:

- może korzystać z internetu do sprawdzania twierdzeń i profilu miejsca;
- musi preferować źródła pierwotne i otwierać właściwe fragmenty;
- nie może wyszukiwać ocen B1 lub B2;
- zapisuje dokładny model, wersję lub snapshot, dostawcę, ustawienie
  rozumowania, narzędzia, dostęp do internetu, pamięci i repozytoriów;
- używa najwyższego dostępnego stabilnego ustawienia rozumowania;
- wpisuje `not_available`, jeżeli środowisko nie ujawnia dokładnej wartości.

Różnice funkcji produktów są ujawnianym ograniczeniem, a nie uzupełniane
domysłem. Przebieg bez możliwości czytania pełnych plików, zapisywania wyników,
otwierania źródeł lub uruchomienia walidatora nie jest porównywalny i zatrzymuje
się przed oceną.

## 8. Przebieg i dokumentowanie

Kolejność przypadków ustalono rosnąco według:

`SHA-256("ocena-0.3-B2-kolejnosc-v1|<case_id>|<kanoniczny_url>")`

Kolejność wynosi: B2-04, B2-02, B2-03, B2-05, B2-06, B2-01.

Każdy przypadek powstaje osobno i zawiera `metryka.json`, `analiza.md`,
`wynik.json` oraz `wyciag-kalibracyjny.json`. Po każdym przypadku powstaje
osobny commit. Nie wolno wracać do zamkniętego wyniku po zobaczeniu kolejnych
przypadków. Podejrzenia wady metodologii zapisuje się osobno i nie stosuje
podczas serii.

## 9. Walidacja i ponowienia

Każda metryka, pełny wynik i wyciąg muszą przejść walidator 0.3. Po sześciu
przypadkach wykonuje się ponowną walidację całości, kontrolę sum wejścia,
składni danych i `git diff --check`.

Ponowienie jest dozwolone tylko wtedy, gdy przed wynikiem merytorycznym
wystąpił udokumentowany błąd techniczny albo rezultat jest niekompletny,
uszkodzony lub niewalidowalny z przyczyny technicznej. Zaskakujący werdykt lub
rozbieżność nie są podstawą ponowienia.

## 10. Porównanie

Porównanie rozpoczyna się dopiero po zamknięciu i walidacji wszystkich
dostępnych przebiegów. Obejmuje:

- powtarzalność A/B wewnątrz każdej rodziny;
- zgodność trzech rodzin dla każdego przypadku;
- werdykty i `safe_recommendation`;
- wszystkie A–L, w tym zgodność `nd`;
- atomizację i wyniki twierdzeń dopasowanych znaczeniowo;
- grupowanie, wielkość, centralność i ryzyko problemów;
- test rozstrzygalności i cztery przesłanki krytyczności;
- profile odbiorców oraz grupowe G, H i L.

Twierdzenia i problemy dopasowuje się znaczeniowo, a nie według lokalnych
numerów. Różnica techniczna to niespójne wejście, brak narzędzia, błąd pobrania,
uszkodzony plik lub niewalidowalna struktura. Różnica pomiędzy poprawnymi,
zwalidowanymi wynikami przy równych wejściach jest różnicą oceny modelu.

## 11. Kryteria przenośności ustalone przed wynikami

Metodologię uznaje się za wystarczająco przenośną w tym ograniczonym badaniu,
jeżeli łącznie:

1. wszystkie 36 ocen są kompletne i poprawne technicznie albo każda luka ma
   jednoznacznie udokumentowaną przyczynę techniczną;
2. każda rodzina ma zgodny werdykt A/B w co najmniej 5 z 6 przypadków;
3. w co najmniej 5 z 6 przypadków minimum dwie z trzech rodzin uzyskują ten sam
   werdykt i nie występuje przypadek trzech różnych werdyktów;
4. wewnątrz rodzin co najmniej 70% porównywalnych A–L jest identycznych, a 90%
   mieści się w granicy jednego punktu;
5. pomiędzy rodzinami co najmniej 60% porównywalnych A–L jest identycznych, a
   85% mieści się w granicy jednego punktu;
6. nie występuje systematyczne odwracanie zasad `nd`, rozstrzygalności lub
   krytyczności przez jedną rodzinę;
7. różnice dają się jawnie wyjaśnić na poziomie twierdzeń, problemów, źródeł
   albo interpretacji kotwic.

Niespełnienie progu nie oznacza automatycznie odrzucenia całej metodologii.
Wymaga rozdzielenia problemu instrukcji, formatu skilla, możliwości modelu i
doboru korpusu. Progów nie zmienia się po poznaniu wyników.

## 12. Prywatność

Pełne publikacje, metryki, analizy, wyniki i identyfikatory wykonania pozostają
w sześciu prywatnych repozytoriach. Publicznie można później opublikować tylko
wyniki zbiorcze i bezpieczne wnioski. Nie wolno publicznie łączyć nazwanej
publikacji z negatywnym werdyktem ani ujawniać prywatnego manifestu, pełnych
analiz lub kopii publikacji.

## 13. Zakończenie, czas i ryzyka

B2 kończy się po uzyskaniu i walidacji 36 ocen, wykonaniu 18 porównań A/B,
porównań międzyrodzinnych, kontroli izolacji oraz bezpiecznego raportu
zbiorczego. Jeżeli rodzina nie spełnia minimalnych możliwości technicznych,
badanie dokumentuje nieporównywalność zamiast zastępować ją człowiekiem.

Przewidywany nakład to cztery zewnętrzne sesje oceniające, dwa odizolowane
zadania ChatGPT, 36 pełnych ocen, walidacja oraz porównania. Czas zależy od
limitów usług i długości weryfikacji źródeł; koszt zależy od planów lub API i
przed uruchomieniem musi zostać zapisany jako znany albo `not_available`.

Główne ryzyka to niedostateczne odizolowanie pamięci lub repozytoriów, różne
możliwości internetowe, nieujawniona zmiana modelu, zmiana treści źródła,
niepełne wykonanie długiej serii oraz potraktowanie różnicy platformy jako
różnicy metodologii.

## 14. Bramki przed ocenami

Oceny pozostają zablokowane do czasu łącznego spełnienia warunków:

1. właściciel zatwierdzi protokół i sześć publikacji;
2. wszystkie sześć prywatnych repozytoriów ma poprawne, zgodne bajtowo wejście;
3. sumy kontrolne i walidator przechodzą kontrolę;
4. dostęp Gemini i Groka jest ograniczony do właściwego repozytorium;
5. potwierdzono nowe rozmowy i brak dostępu do drugiego przebiegu;
6. określono dokładne modele i ustawienia;
7. właściciel wyda osobne polecenie rozpoczęcia ocen.

Do czasu spełnienia wszystkich bramek B2 jest przygotowane, ale nie rozpoczęte.
