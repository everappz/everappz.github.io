---
title: "Udostępnianie"
date: 2026-08-20
description: "Dowiedz się, jak działa udostępnianie w Everdisk: dotknij Start, aby zamienić iPhone'a lub iPada w bezprzewodowy dysk, wybierz, co udostępnić (pliki, foldery, zdjęcia i muzykę), uruchom cztery serwery (DLNA, HTTP, WebDAV, FTP), odczytaj adresy połączeń, zobacz, kto jest podłączony, i utrzymaj udostępnianie przez Wi-Fi lub kabel USB."
keywords: ["udostępnianie Everdisk", "bezprzewodowy dysk iPhone", "rozpocznij udostępnianie", "udostępnianie plików iPhone", "udostępnianie zdjęć w sieci", "DLNA HTTP WebDAV FTP", "co udostępnić", "jak się połączyć", "utrzymaj aplikację otwartą", "udostępnianie przez Wi-Fi lub kabel USB"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


Karta **Udostępnianie** to serce Everdisk. To tutaj zamieniasz iPhone'a lub iPada w bezprzewodowy dysk, wybierasz dokładnie to, co chcesz udostępnić, i otrzymujesz adresy, których inne urządzenia używają do połączenia. To pierwsza karta, jaką widzisz po otwarciu aplikacji.

## Rozpoczynanie i zatrzymywanie udostępniania

Na środku ekranu Udostępniania znajduje się duży okrągły przycisk.

- Dotknij **Start**, aby jednocześnie uruchomić wszystkie włączone serwery. Przycisk pokaże **Uruchamianie...**, a następnie **Stop**, gdy udostępnianie ruszy.
- Dotknij **Stop**, aby ponownie wyłączyć wszystko. Podłączone urządzenia zostaną odłączone.

Gdy udostępnianie działa, wybrane pliki, zdjęcia i muzyka są dostępne dla każdego urządzenia w tej samej sieci, które połączy się jedną z czterech metod opisanych poniżej.

> Udostępnianie działa tylko wtedy, gdy aplikacja jest otwarta. Zobacz **Utrzymaj aplikację otwartą** pod koniec tej strony, aby dowiedzieć się dlaczego oraz jak utrzymać duże transfery.

## Wybór tego, co udostępnić

Zanim zaczniesz, dotknij nagłówka **Co udostępnić**, aby otworzyć trzy grupy. Możesz udostępnić dowolne ich połączenie, ale zanim udostępnianie ruszy, musisz wybrać przynajmniej jedną rzecz.

**Pliki i foldery**

- Folder **Dokumenty** aplikacji jest udostępniany domyślnie. Jeśli wolisz, możesz przestać go udostępniać.
- Dotknij **Dodaj folder**, aby udostępnić folder z dowolnego miejsca na urządzeniu, lub **Dodaj plik**, aby udostępnić pojedyncze pliki.
- Każdy udostępniony element ma przycisk **Informacje** oraz przycisk **Zatrzymaj udostępnianie**.

**Zdjęcia i filmy**

- Włącz **Zezwalaj na dostęp do całej biblioteki zdjęć**, aby udostępnić całą bibliotekę zdjęć i filmów, lub
- Dotknij **Dodaj zdjęcia**, aby ręcznie wybrać tylko te zdjęcia i filmy, które chcesz udostępnić.

**Muzyka**

- Włącz **Zezwalaj na dostęp do całej biblioteki muzycznej**, aby udostępnić całą bibliotekę muzyczną, lub
- Dotknij **Dodaj utwory**, aby udostępnić tylko wybrane piosenki.
- Utworów chronionych (DRM) lub przechowywanych wyłącznie w chmurze nie można udostępnić.

Jeśli spróbujesz uruchomić udostępnianie bez żadnego wyboru, Everdisk pokaże komunikat **Nie ma czego udostępnić**. Jeśli zmienisz to, co jest udostępniane, gdy udostępnianie działa, **zatrzymaj je i uruchom ponownie**, aby zastosować zmianę.

## Cztery serwery

Everdisk udostępnia tę samą zawartość na cztery sposoby naraz. Każdy z nich jest przeznaczony dla innego rodzaju urządzeń i każdy można włączyć lub wyłączyć w **Ustawieniach → Udostępnianie → Połączenia**. Domyślnie wszystkie cztery są włączone.

- **TV i centrum multimedialne (DLNA)** - dla smart TV i odtwarzaczy multimedialnych. Same wykrywają Twoje urządzenie i wyświetlają zdjęcia, filmy oraz muzykę wraz z miniaturami podglądu.
- **Przeglądarka (HTTP)** - dla dowolnego telefonu, tabletu lub komputera. Druga osoba otwiera link w przeglądarce, aby przeglądać i pobierać Twoje pliki. Nic nie trzeba instalować.
- **Komputer (WebDAV)** - dla Maca, komputera z systemem Windows lub Linux. Twoje urządzenie pojawia się jako zwykły dysk sieciowy, więc możesz przeciągać pliki w obie strony.
- **Inne aplikacje i urządzenia (FTP)** - dla aplikacji do plików i zaawansowanych użytkowników, którzy posługują się FTP.

Instrukcje połączenia krok po kroku dla każdego typu znajdziesz w [Podłącz swoje urządzenia](/docs/guide/everdisk/everdisk-guide-connect).

## Jak się połączyć i adresy połączeń

Po dotknięciu Start sekcja **Jak się połączyć** pokazuje kartę dla każdego aktywnego serwera z dokładnym **adresem** do wpisania na drugim urządzeniu. Każdy adres łatwo skopiować - dotknij go, aby skopiować, użyj przycisku **Udostępnij**, aby go wysłać, lub dotknij przycisku **informacji (ⓘ)**, aby uzyskać szczegółowe instrukcje dla danego protokołu.

- Karta DLNA pokazuje adres opisu urządzenia zakończony `/device-desc.xml` dla odtwarzaczy, które go wymagają.
- Gdy urządzenie jest podłączone do Maca kablem, pojawia się dodatkowy adres z plakietką **Połączenie kablowe**, który używa nazwy `.local` Twojego urządzenia.

Adres możesz również otworzyć jako **kod QR**, aby aparat innego urządzenia mógł od razu do niego przejść.

## Kto jest podłączony

Sekcja **Kto jest podłączony** wyświetla na bieżąco urządzenia obecnie do Ciebie podłączone. Dotknij przycisku Więcej akcji obok dowolnego urządzenia, aby **Zablokować to urządzenie**, jeśli go nie rozpoznajesz. Zablokowanymi urządzeniami zarządzasz w [Dostęp i prywatność](/docs/guide/everdisk/everdisk-guide-access).

## Nazwa i awatar Twojego urządzenia

Każde urządzenie ma przyjazną nazwę (np. "Speedy-Hare") i kolorowy awatar. To nazwa, którą telewizor, komputer lub inna aplikacja pokazuje dla Twojego urządzenia w sieci, dzięki czemu łatwo je rozpoznać. Możesz wygenerować nazwę i awatar ponownie za darmo albo ustawić własną nazwę, ikonę lub awatar ze zdjęcia z Premium. Zobacz [Ustawienia](/docs/guide/everdisk/everdisk-guide-settings).

## Udostępnianie przez Wi-Fi lub kabel USB

Udostępnianie może działać w dwóch sytuacjach:

- **Przez Wi-Fi** - Twoje urządzenie i pozostałe urządzenia są w tej samej sieci Wi-Fi.
- **Przez kabel USB** - Twoje urządzenie jest podłączone kablem do **Maca**, nawet gdy w ogóle nie ma Wi-Fi. Jest to szybsze niż Wi-Fi i działa w samolocie, w hotelu czy w zablokowanej sieci.

Jeśli nie ma ani Wi-Fi, ani kabla, przycisk **Start** jest nieaktywny i pojawia się komunikat **Brak połączenia Wi-Fi**. Jeśli połączenie zerwie się podczas udostępniania, Everdisk automatycznie zatrzymuje udostępnianie i informuje Cię o tym. Dotknij przycisku informacji przy dowolnym z tych komunikatów, aby uzyskać pełne wyjaśnienie.

## Utrzymaj aplikację otwartą

Ponieważ Twój iPhone lub iPad pełni rolę serwera, **udostępnianie działa tylko wtedy, gdy Everdisk jest otwarty na ekranie**. Jeśli zamkniesz aplikację lub zablokujesz urządzenie na dłużej, system może wstrzymać aplikację i udostępnianie się zatrzyma.

W przypadku dużych transferów:

- Trzymaj Everdisk otwarty i na pierwszym planie.
- Podłącz urządzenie do zasilania.
- Ustaw **Autoblokadę** na **Nigdy** w aplikacji Ustawienia iOS na czas transferu.

Możesz włączyć **Powiadamiaj przed rozłączeniem** (w Ustawienia → Udostępnianie), aby Everdisk przypominał Ci o ponownym otwarciu aplikacji, zanim system ją zawiesi. Dotknij przycisku informacji na banerze **Utrzymaj aplikację otwartą**, aby poznać szczegóły.

## Następne kroki

- [Podłącz swoje urządzenia](/docs/guide/everdisk/everdisk-guide-connect) - podłącz telewizor, komputer, przeglądarkę, telefon lub kabel USB.
- [Dostęp i prywatność](/docs/guide/everdisk/everdisk-guide-access) - dodaj hasło i kontroluj edycję.
- [Ustawienia](/docs/guide/everdisk/everdisk-guide-settings) - włączaj lub wyłączaj serwery i dostrajaj jakość.
