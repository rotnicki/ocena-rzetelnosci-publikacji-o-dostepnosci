# Ocena rzetelności publikacji o dostępności

## W skrócie

Projekt pomaga wykorzystywać AI do oceny rzetelności artykułów, poradników, ofert, materiałów szkoleniowych i innych publikacji dotyczących dostępności.

Zawiera metodologię określającą zasady oceny, skill prowadzący AI przez analizę oraz walidator sprawdzający strukturę wyniku. Skill, czyli przygotowana umiejętność AI, wykorzystuje otwarty standard [Agent Skills](https://agentskills.io/). Dzięki temu może być używany przez różne zgodne narzędzia, a nie tylko przez jeden model AI.

Aktualną wersją jest [oficjalne wydanie v0.3.0](https://github.com/rotnicki/ocena-rzetelnosci-publikacji-o-dostepnosci/releases/tag/v0.3.0). Jest to oficjalna, zamrożona wersja eksperymentalna i stały punkt odniesienia przed stabilną wersją 1.0. Metodologia 0.3 jest domyślną wersją skilla.

## Jaki problem rozwiązuje projekt

Wyobraź sobie, że chcesz nauczyć się czegoś o dostępności albo musisz ocenić artykuł, szkolenie czy ofertę audytu. Materiał wygląda profesjonalnie, ale nie masz pewności, czy przekazuje aktualną wiedzę, właściwie opisuje przepisy i standardy oraz proponuje bezpieczne rozwiązania.

Publikacja może zawierać błędy, uczyć nieprawidłowych praktyk, powielać utrwalone mity albo przedstawiać dobrą praktykę jako bezwzględny wymóg. Materiał marketingowy może wyolbrzymiać korzyści, pomijać ograniczenia lub sugerować skuteczność i kompetencje, których odpowiednio nie udokumentowano.

Specjalistyczny język i pewny ton mogą sprawić, że nierzetelna treść brzmi wiarygodnie. Osobie bez odpowiedniej wiedzy lub czasu może być trudno odróżnić rzeczywiste wymaganie od uproszczenia, branżowego przyzwyczajenia albo chwytu marketingowego.

Naturalnym odruchem jest poproszenie AI o pomoc. W zwykłej rozmowie na czacie AI może jednak pominąć ważne źródło, przedstawić niepełną ocenę albo przy kolejnej próbie wydać inny werdykt. Użytkownik, który nie zna ograniczeń AI, może zbyt łatwo zaufać jednej odpowiedzi.

Projekt wyrósł z wieloletnich doświadczeń i obserwacji Mikołaja Rotnickiego — eksperta i popularyzatora dostępności cyfrowej. Potrzeby te pojawiały się podczas szkoleń, audytów, przygotowywania ofert, rozmów na forach internetowych oraz analizowania problemów zgłaszanych przez urzędników, zamawiających i osoby uczące się dostępności.

## Dla kogo

Projekt może pomagać:

- osobom uczącym się dostępności i sprawdzającym jakość wybranej publikacji;
- osobom bez wiedzy lub czasu potrzebnego do samodzielnej kontroli wszystkich twierdzeń i źródeł;
- urzędnikom odbierającym publikacje lub szkolenia przygotowane za pieniądze publiczne;
- zamawiającym porównującym oferty audytu, badania, szkolenia albo przebudowy strony czy aplikacji;
- redakcjom, trenerom i autorom sprawdzającym materiał przed publikacją;
- ekspertom porządkującym analizę i porównującym niezależne wyniki.

Metoda może skrócić pierwszą analizę i wskazać elementy wymagające dokładniejszego sprawdzenia. Nie wybiera jednak automatycznie najlepszej oferty ani nie potwierdza rzeczywistych kompetencji wykonawcy.

## Jak pomagają metodologia i skill

Metodologia określa, co należy ocenić: jakie twierdzenia sprawdzić, jak dobierać źródła, jak rozpoznawać problemy oraz jak ustalać ich znaczenie dla odbiorców.

Skill jest przygotowaną umiejętnością AI. Zawiera instrukcję postępowania, materiały metodologiczne, schematy, szablony i skrypty kontrolne. Zgodne narzędzie AI może wczytać ten pakiet i przeprowadzić ocenę według opisanej procedury.

Stały format wyniku pozwala wykonać drugą, niezależną ocenę i porównać oba przebiegi. Pokazuje nie tylko końcowy werdykt, ale także miejsca zgodności i rozbieżności.

Metodologia i skill powstały na podstawie kolejnych prób, pilotaży i badań powtarzalności. Nie usuwają ryzyka błędu AI, ale wymagają korzystania ze źródeł i pokazania podstaw oceny.

## Co jest oceniane

Publikacja otrzymuje osobne oceny w dwunastu obszarach:

- A–D: poprawność faktów, prawa i norm, zagadnień technicznych oraz jakość źródeł;
- E–H: kompletność i kontekst, jakość rozumowania, precyzja pojęć i zrozumiałość;
- I–L: użyteczność i bezpieczeństwo zaleceń, doświadczenia użytkowników, odróżnianie wiedzy od niepewności oraz dopasowanie treści do celu.

Nie tworzy się z nich średniej automatycznie wyznaczającej werdykt. Pełne definicje zawierają [kotwice ocen A–L](metodologia/0.3/kotwice.md).

Metoda ocenia publikację i przedstawione w niej dowody, a nie charakter ani intencje autora.

## Jak użyć

1. Pobierz pakiet ZIP z [wydania v0.3.0](https://github.com/rotnicki/ocena-rzetelnosci-publikacji-o-dostepnosci/releases/tag/v0.3.0).
2. Dodaj go do narzędzia obsługującego Agent Skills. Jeżeli nie jest to możliwe, przekaż AI plik `SKILL.md` razem z katalogami `references` i `scripts`.
3. Podaj pełną treść materiału albo jego adres internetowy.
4. Wydaj polecenie:

```text
Oceń ten materiał zgodnie z metodologią 0.3. Zastosuj dołączony skill, sprawdź twierdzenia w wiarygodnych źródłach i przygotuj pełny raport oraz wynik strukturalny.
```

5. Jeżeli środowisko pozwala uruchamiać skrypty, sprawdź wynik dołączonym walidatorem.
6. Aby zbadać powtarzalność, wykonaj drugi przebieg bez udostępniania pierwszego wyniku.

Dokładna instrukcja znajduje się w pliku [`skill/SKILL.md`](skill/SKILL.md).

## Co sprawdzono

Rozwój metody obejmował wcześniejsze próby, serię wersji 0.2, polski pilotaż 0.3 oraz badanie B1.

W B1 każdą z 16 publikacji oceniono dwa razy w odizolowanych przebiegach. Łącznie wykonano 32 niezależne oceny. Werdykt był taki sam w 15 z 16 porównań. Szczegóły zawiera [publiczne podsumowanie B1](kalibracja/0.3/wyniki-B1.md).

## Ograniczenia

- AI może popełnić błąd, pominąć źródło albo niewłaściwie zinterpretować materiał.
- Walidator sprawdza strukturę wyniku, a nie prawdziwość analizy.
- Metoda nie zastępuje porady prawnej, audytu ani procedury udzielania zamówienia.
- Wynik powinien wspierać odpowiedzialną decyzję, a nie automatycznie ją zastępować.
- Przenośność pomiędzy różnymi rodzinami AI nie była objęta zakresem walidacji 0.3. Może zostać zbadana podczas prac nad przyszłą wersją 0.4.

## Dokumentacja

- [Opis metodologii 0.3](metodologia/0.3/README.md).
- [Pełny standard 0.3](metodologia/0.3/standard.md).
- [Kotwice ocen A–L](metodologia/0.3/kotwice.md).
- [Instrukcja skilla](skill/SKILL.md).
- [Wyniki badania B1](kalibracja/0.3/wyniki-B1.md).
- [Informacje o wydaniu v0.3.0](wydania/v0.3.0.md).
- [Historia wersji](WERSJONOWANIE.md).
- [Licencje i autorstwo](LICENSE.md).

## Licencja

Metodologia i materiały tekstowe są udostępniane na licencji CC BY 4.0. Kod, skrypty, schematy i pliki techniczne są udostępniane na licencji MIT.
