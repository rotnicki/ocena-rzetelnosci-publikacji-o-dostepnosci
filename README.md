# Ocena rzetelności publikacji o dostępności

## W skrócie

Projekt pomaga sztucznej inteligencji sprawdzać rzetelność artykułów, poradników, ofert i innych publikacji o dostępności. Zamiast ogólnego polecenia „oceń ten tekst” daje AI wspólne zasady, źródła oceny i format wyniku.

Aktualną wersją jest [oficjalne wydanie v0.3.0](https://github.com/rotnicki/ocena-rzetelnosci-publikacji-o-dostepnosci/releases/tag/v0.3.0). Jest to oficjalna, zamrożona wersja eksperymentalna. Można jej używać jako stałego punktu odniesienia, ale projekt pozostaje na etapie przed wersją stabilną 1.0.

Metodologia 0.3 jest domyślną wersją źródłowej umiejętności dostępnej w tym repozytorium.

## Do czego służy

Metoda pomaga AI:

- przeczytać pełną publikację i ważne materiały, do których ona odsyła;
- oddzielić stanowisko autora od jego oceny;
- wskazać twierdzenia wymagające sprawdzenia;
- porównać je przede wszystkim ze źródłami pierwotnymi i autorytatywnymi;
- ocenić poprawność, jakość dowodów, zrozumiałość i bezpieczeństwo zaleceń;
- opisać wykryte problemy i ich znaczenie;
- wydać jeden z pięciu opisowych werdyktów;
- zapisać wynik tak, aby można go było sprawdzić i porównać z drugą oceną.

Publikacja otrzymuje osobne oceny w dwunastu obszarach oznaczonych od A do L. Nie tworzy się z nich jednej średniej ani sumy, która automatycznie wyznacza werdykt. Liczy się znaczenie konkretnych problemów, ich wpływ na odbiorców oraz jakość uzasadnienia.

Metoda ocenia konkretną publikację, a nie charakter, intencje ani kompetencje jej autora.

## Dla kogo

Projekt jest przeznaczony przede wszystkim dla systemów AI działających pod kontrolą człowieka. Może być przydatny osobom zajmującym się dostępnością, redakcjom, badaczom oraz wszystkim, którzy chcą otrzymać udokumentowaną i porównywalną ocenę publikacji.

Pakiet korzysta z formatu Agent Skills. Nie oznacza to, że każdy czat AI automatycznie odczyta repozytorium, zainstaluje pakiet lub uruchomi walidator. Środowisko musi obsługiwać taki pakiet albo umożliwiać przekazanie jego plików z zachowaniem ich struktury.

## Jak użyć

1. Pobierz pakiet ZIP z [wydania v0.3.0](https://github.com/rotnicki/ocena-rzetelnosci-publikacji-o-dostepnosci/releases/tag/v0.3.0).
2. Dodaj pakiet do narzędzia obsługującego Agent Skills. Jeżeli narzędzie nie instaluje takich pakietów, przekaż mu plik `SKILL.md` razem z katalogami `references` i `scripts`.
3. Podaj pełną treść publikacji albo jej adres internetowy. AI musi mieć możliwość odczytania całego materiału i otwierania źródeł potrzebnych do sprawdzenia twierdzeń.
4. Wydaj polecenie:

```text
Oceń tę publikację zgodnie z metodologią 0.3. Zastosuj dołączony skill, sprawdź twierdzenia w źródłach i przygotuj pełny raport oraz wynik strukturalny.
```

5. Jeżeli środowisko potrafi uruchamiać skrypty, sprawdź plik wyniku dołączonym walidatorem. Walidator kontroluje kompletność i zgodność struktury danych, ale nie potwierdza, że sama analiza jest prawdziwa.
6. Gdy potrzebujesz sprawdzić powtarzalność, uruchom drugą ocenę w osobnym kontekście, bez udostępniania pierwszego wyniku. Dopiero potem porównaj oba przebiegi.

Dokładna instrukcja operacyjna dla AI znajduje się w pliku [`skill/SKILL.md`](skill/SKILL.md). Pełny raport nie gwarantuje sam w sobie poprawności oceny — uzasadnienia i źródła nadal wymagają krytycznej kontroli.

## Co sprawdzono

Rozwój metody obejmował wcześniejsze próby, serię dla wersji 0.2, polski pilotaż projektu 0.3 oraz zakończone badanie B1.

W B1 wykonano 32 niezależne oceny, czyli 16 porównań A/B. Werdykt był zgodny w 15/16 par. Szczegóły, pozostałe miary i ograniczenia zawiera [publiczne podsumowanie B1](kalibracja/0.3/wyniki-B1.md). Wyniki wcześniejszej serii znajdują się w [podsumowaniu kalibracji 0.2](kalibracja/0.2/wyniki-serii.md).

Wyników zakończonych badań ani wcześniejszych wersji nie przelicza się później według nowych zasad. Pełne analizy, prywatny manifest i kopie ocenianych publikacji nie są publikowane w tym repozytorium.

## Ograniczenia

- Metoda nie zastępuje porady prawnej, badania naukowego ani profesjonalnego audytu produktu.
- Jeden wynik AI nie jest automatycznie ostateczną prawdą.
- Poprawny format raportu nie dowodzi poprawności jego treści.
- Zamrożenie oznacza, że reguły wydania v0.3.0 nie są zmieniane wstecz. Nie oznacza pełnego potwierdzenia trafności metody.
- Przenośność metodologii pomiędzy różnymi rodzinami AI nie była objęta zakresem walidacji 0.3. Może zostać zbadana osobno na podstawie zamrożonej wersji 0.3, a wyniki mogą posłużyć do prac nad przyszłą wersją 0.4.

## Dokumentacja

- [Opis metodologii 0.3](metodologia/0.3/README.md) — zawartość i status aktualnej wersji.
- [Pełny standard 0.3](metodologia/0.3/standard.md) — wszystkie obowiązujące reguły oceny.
- [Instrukcja operacyjna skilla](skill/SKILL.md) — kolejność pracy systemu AI.
- [Wyniki badania B1](kalibracja/0.3/wyniki-B1.md) — bezpieczne podsumowanie 32 ocen.
- [Wyniki serii 0.2](kalibracja/0.2/wyniki-serii.md) — wcześniejsze badanie powtarzalności.
- [Informacje o wydaniu v0.3.0](wydania/v0.3.0.md) — zakres zmian i suma kontrolna pakietu.
- [Zasady wersjonowania](WERSJONOWANIE.md) — statusy oraz historia wersji 0.1, 0.2 i 0.3.
- [Licencje i zasady wykorzystania](LICENSE.md) — zakres licencji oraz sposób wskazywania autorstwa.

Metodologia 0.3 jest samodzielna. Wersje 0.1 i 0.2 pozostają niezmiennymi, historycznymi punktami odniesienia i trzeba wybierać je jawnie.

## Licencja

Metodologia i pozostałe materiały tekstowe są udostępniane na licencji CC BY 4.0. Kod, skrypty, schematy i pliki techniczne są udostępniane na licencji MIT. Szczegóły zawiera dokument [Licencje i autorstwo](LICENSE.md).
