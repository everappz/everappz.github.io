---
title: "Połącz z serwerami"
date: 2026-08-20
description: "Skorzystaj z karty Urządzenia w Everdisk, aby połączyć się z innymi serwerami w sieci. Dodawaj i przeglądaj serwery DLNA, WebDAV, FTP, SFTP i SMB oraz dyski NAS, odtwarzaj strumieniowo dźwięk i wideo, pobieraj pliki oraz twórz, przesyłaj, zmieniaj nazwy, przenoś lub usuwaj na serwerach, które na to pozwalają."
keywords: ["karta Urządzenia Everdisk", "połączenie z NAS", "klient DLNA iPhone", "klient WebDAV iPhone", "klient FTP iPhone", "klient SFTP iPhone", "klient SMB iPhone", "łączenie z udziałem SMB", "przeglądanie serwera sieciowego", "streaming z NAS", "pobieranie z serwera", "połączenie chmury WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk to nie tylko bezprzewodowy dysk - to także klient dla pozostałych urządzeń w Twojej sieci. Karta **Urządzenia** pozwala łączyć się z serwerami **DLNA**, **WebDAV**, **FTP**, **SFTP** i **SMB**, w tym z Makami, komputerami z Windows, maszynami z Linux, dyskami NAS i serwerami multimediów, a następnie przeglądać, odtwarzać strumieniowo i pobierać ich pliki.

## Ekran Urządzenia

Karta Urządzenia ma dwie części:

- **Połączenia** - serwery, które już zapisałeś.
- **Dostępne urządzenia** - serwery, które Everdisk automatycznie znajduje w Twojej sieci lokalnej.

Aby połączyć się z czymś, co Everdisk już znalazł, po prostu dotknij tego w **Dostępnych urządzeniach**. Aby dodać serwer ręcznie, dotknij przycisku **plus (+)** lub **Nowe połączenie**.

## Dodawanie nowego połączenia

Dotknij **Nowe połączenie** i wybierz typ serwera, do którego chcesz dotrzeć:

- **DLNA / UPnP** - najlepszy dla serwerów multimediów. Odtwarzaj strumieniowo wideo, muzykę i zdjęcia z bibliotek multimediów, sieciowych dysków pamięci oraz telewizorów i komputerów obsługujących DLNA. DLNA jest tylko do odczytu: możesz przeglądać, odtwarzać strumieniowo i pobierać, ale nie możesz przesyłać ani zmieniać plików.
- **WebDAV** - łącz się z serwerami plików, sieciowymi dyskami pamięci oraz dyskami w chmurze obsługującymi WebDAV. Odczyt i zapis, gdy serwer na to pozwala.
- **FTP** - powszechny w routerach, sieciowych dyskach pamięci i hostingu internetowym. Domyślny port to 21 (990 dla bezpiecznego FTPS); własny port możesz ustawić w adresie, na przykład `ftp://host:2121`. Pozostaw login i hasło puste dla dostępu anonimowego.
- **SFTP** - łącz się bezpiecznie przez SSH. Domyślny port to 22; w razie potrzeby użyj własnego portu w adresie, na przykład `sftp://host:2222`.
- **SMB** - łącz się z Makami, komputerami z Windows, serwerami Linux i pamięciami sieciowymi (NAS), które udostępniają foldery przez **SMB / CIFS**. Wpisz adres taki jak `smb://server-address/share-name/` (przykłady: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB dodaje dwa opcjonalne pola: nazwę **Grupy roboczej** oraz **Wersję protokołu**, którą możesz pozostawić na **Wersja automatyczna** albo wymusić **SMB1** lub **SMB2**. Jeśli pliki lub foldery ze znakami specjalnymi nie chcą się otwierać, spróbuj przełączyć wersję na **SMB1**.

> Everdisk łączy się wyłącznie z tymi protokołami sieci lokalnej i adresowanymi bezpośrednio. Nie loguje się do kont w chmurze, takich jak Google Drive czy Dropbox. Dysk w chmurze jest dostępny tylko wtedy, gdy dana usługa oferuje adres **WebDAV**, który możesz wpisać.

## Wprowadzanie adresu i logowanie

W edytorze połączenia uzupełnij:

- **Tytuł** - przyjazna nazwa połączenia.
- **URL / adres** - adres serwera (dla każdego typu pokazane są przykłady).
- **Login** i **Hasło** - pozostaw oba puste, jeśli serwer zezwala na dostęp anonimowy.

W przypadku WebDAV możesz zezwolić na nieprawidłowe certyfikaty, jeśli Twój serwer używa certyfikatu podpisanego samodzielnie. Jeśli tożsamości bezpiecznego serwera nie da się zweryfikować, Everdisk poprosi Cię o potwierdzenie przed zaufaniem mu.

Darmowi użytkownicy mogą zapisać do **10** połączeń. Premium znosi ten limit.

## Przeglądanie, streaming i pobieranie

Po połączeniu dotknij serwera, aby go otworzyć:

- **Przeglądaj** foldery w widoku listy lub siatki, sortuj je i oglądaj miniatury. Serwery DLNA pokazują też szczegóły muzyki i okładki.
- **Odtwarzaj strumieniowo** dźwięk i wideo. Dźwięk trafia do kolejki miniodtwarzacza; wideo odtwarza się na pełnym ekranie. Przewijanie działa podczas strumieniowania pliku.
- **Pobieraj** pliki na urządzenie. Wybierz kilka naraz, aby pobrać je grupowo. Pobrania pojawiają się w **Transferach plików** i lądują w folderze **Dokumenty**.
- **Informacje** o dowolnym elemencie pokazują jego rodzaj, rozmiar, datę, ścieżkę i szczegóły multimediów.

## Zmienianie plików na serwerze

Na serwerach, które pozwalają na zapis - **WebDAV, FTP, SFTP i SMB** - możesz również zarządzać plikami:

- **Nowy folder**
- **Prześlij pliki** z urządzenia
- **Zmień nazwę**, **Przenieś** i **Usuń** (jeden element lub kilka naraz)

Serwery **DLNA** są tylko do odczytu, więc te akcje nie są tam dostępne.

## Śledzenie transferów

Pobrania i wysyłki działają w tle i pojawiają się w **Transferach plików**, które otwierasz w lewym górnym rogu karty **Dokumenty**. Tam możesz obserwować postęp oraz wstrzymywać, wznawiać, ponawiać, anulować lub czyścić zadania. Transfery możesz też dostroić w [Ustawienia → Sieć](/docs/guide/everdisk/everdisk-guide-settings) (tylko Wi-Fi kontra Wi-Fi i sieć komórkowa, ile działa jednocześnie oraz czy kontynuują w tle).

## Następne kroki

- [Pliki i dokumenty](/docs/guide/everdisk/everdisk-guide-files) - zarządzaj wszystkim, co pobierzesz.
- [Zdjęcia, muzyka i wideo](/docs/guide/everdisk/everdisk-guide-media) - odtwarzaj to, co strumieniujesz.
- [Ustawienia](/docs/guide/everdisk/everdisk-guide-settings) - limity połączeń i opcje transferu.
