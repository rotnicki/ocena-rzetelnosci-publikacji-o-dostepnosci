# Wersjonowanie i wydawanie

Ten dokument określa jeden wspólny sposób nazywania, zamrażania i publikowania kolejnych wersji metodologii oraz umiejętności AI.

## Numery wersji

Projekt używa numerów w postaci `MAJOR.MINOR.PATCH`, na przykład `0.2.0`.

- `MAJOR` — zmiana niezgodna z wcześniejszym sposobem użycia; stabilne wydania rozpoczną się od `1`.
- `MINOR` — nowa zamrożona wersja eksperymentalna metodologii, na przykład `0.2.0` lub `0.3.0`.
- `PATCH` — poprawka techniczna albo redakcyjna, która nie zmienia znaczenia kryteriów ani wyników, na przykład `0.2.1`.

Wszystkie wersje `0.x.y` są rozwojowe. Opublikowane wersje `0.x.y` są jednak zamrożonymi punktami odniesienia: ich metodologii, wyników ani znaczenia ocen nie zmienia się wstecz.

## Statusy

- **W przygotowaniu** — zmiany powstają na osobnej gałęzi i mogą się jeszcze zmieniać. Nie jest to wydanie.
- **Kandydat do wydania** — wersja jest kompletna i podlega końcowej kontroli. W razie potrzeby może otrzymać oznaczenie, np. `v0.3.0-rc.1`.
- **Zamrożona wersja eksperymentalna** — opublikowane wydanie `v0.x.y`, którego można używać w ocenach i testach. Na GitHubie jest oznaczone jako wersja przedpremierowa.
- **Wersja stabilna** — wydanie od `v1.0.0`, przeznaczone do zwykłego stosowania po zakończeniu wymaganej walidacji.

Słowo `draft` nie jest dodawane do numeru zamrożonego wydania. Może występować w historycznych dokumentach opisujących etap przygotowywania danej wersji, ale strona wydania zawsze podaje jej aktualny status prostym językiem.

## Co oznacza wydanie

Każde wydanie musi zawierać:

1. niezmienny znacznik Git `vMAJOR.MINOR.PATCH`;
2. opis statusu, zakresu i ograniczeń wersji;
3. wskazanie źródłowego commita metodologii;
4. listę najważniejszych zmian względem poprzedniej wersji;
5. gotową paczkę umiejętności AI w pliku ZIP;
6. informacje o licencji;
7. sumę kontrolną SHA-256 paczki ZIP.

Opisy opublikowanych wydań są przechowywane także w katalogu `wydania/`, aby historia nie zależała wyłącznie od interfejsu GitHuba.

Historyczne paczki 0.1.0 i 0.2.0 buduje skrypt `scripts/build_skill_release.py`. Pobiera on zawartość skilla z przypisanego źródłowego commita, jednoznacznie ustawia aktywną wersję metodologii, usuwa odsyłacze do nieobecnych historycznie ikon oraz dodaje manifest i licencje. Nie zmienia treści metodologii ani kotwic ocen.

Publikację historycznych wydań wykonuje kontrolowany proces GitHub Actions zapisany w `.github/workflows/publish-historical-releases.yml`. Proces buduje paczki od początku, tworzy brakujące znaczniki na gałęziach wydawniczych, dołącza ZIP-y i sumy kontrolne oraz oznacza wydania jako przedpremierowe. Jeżeli wydanie już istnieje, pozostawia je bez zmian.

Paczka instalacyjna musi zawierać obowiązkowy `SKILL.md` oraz wszystkie pliki, do których się odwołuje. Nie może wymagać pobierania metodologii z tego repozytorium podczas działania. Zewnętrzny dostęp może być nadal potrzebny do pobrania ocenianej publikacji i sprawdzenia jej twierdzeń w źródłach.

## Wydania historyczne

| Wydanie | Status | Źródłowy commit | Znaczenie |
|---|---|---|---|
| `v0.1.0` | zamrożona wersja eksperymentalna | `af83066983e832cd7f61b7c2bd99482a07731afc` | pierwszy kompletny stan metodologii i umiejętności 0.1 przed rozpoczęciem prac nad 0.2 |
| `v0.2.0` | zamrożona wersja eksperymentalna | `c3280da26d2bf0a5a44dfcddc9105180bf3d4267` | dokładna metodologia 0.2 użyta w serii ośmiu publikacji i szesnastu przebiegów |

Historyczne sformułowanie `0.2-draft` oznacza, że wersja była projektem podczas przygotowywania kalibracji. Wydanie `v0.2.0` zamraża dokładnie tę eksperymentalną metodologię i nie przedstawia jej jako wersji stabilnej.

## Kolejne wersje

Prace nad następną metodologią prowadzi się jako projekt 0.3 na osobnej gałęzi. Dopiero po przeglądzie, zatwierdzeniu i zamrożeniu powstaje wydanie `v0.3.0`. Zakończonych wyników 0.1 ani 0.2 nie przelicza się według nowych reguł.
