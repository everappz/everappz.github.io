---
title: "Dostęp i prywatność"
date: 2026-08-20
description: "Zadbaj o bezpieczeństwo udostępniania w Everdisk: zabezpiecz dostęp loginem i hasłem, zaszyfruj połączenie SMB szyfrowaniem SMB3 (AES), kontroluj za pomocą Edycji plików, czy podłączone urządzenia mogą przesyłać, zmieniać nazwy i usuwać, blokuj nieznane urządzenia, wybieraj kosz kontra trwałe usuwanie i zrozum, dlaczego wszystko pozostaje w Twojej sieci lokalnej."
keywords: ["ochrona hasłem Everdisk", "szyfrowanie SMB", "szyfrowanie SMB3 AES", "przełącznik edycji plików", "blokowanie urządzenia", "zablokowane urządzenia", "trwałe usuwanie plików", "tylko sieć lokalna", "prywatne udostępnianie plików", "DLNA bez hasła", "bezpieczeństwo sieci"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk trzyma Twoje pliki w Twojej własnej sieci i daje Ci proste narzędzia kontroli nad tym, kto może po nie sięgnąć i co może z nimi zrobić. Te narzędzia znajdziesz w **Ustawienia → Udostępnianie → Dostęp**, a także kilka powiązanych ustawień w Menedżerze plików.

## Zabezpieczanie dostępu loginem i hasłem

Domyślnie każdy w tej samej sieci, kto ma Twój adres, może otworzyć udostępnione pliki. Aby wymagać logowania:

1. Przejdź do **Ustawienia → Udostępnianie → Dostęp**.
2. Wprowadź **Login** i **Hasło**.
3. Od teraz połączenia **Przeglądarka (HTTP)**, **Komputer (WebDAV)**, **Komputer (zaawansowane) (SMB)** oraz **Inne aplikacje i urządzenia (FTP)** będą prosić o te dane, zanim pokażą Twoje pliki.

Pozostaw oba pola puste dla otwartego dostępu. Twoje hasło jest bezpiecznie przechowywane w Pęku kluczy urządzenia.

> **DLNA jest zawsze otwarte.** Połączenia TV i centrum multimedialne (DLNA) nie da się zabezpieczyć hasłem, więc gdy jest włączone, każde urządzenie w tej samej sieci Wi-Fi może przeglądać Twoje udostępnione multimedia. Wyłącz je, jeśli chcesz mieć tylko zabezpieczone połączenia, i udostępniaj wyłącznie w sieciach, którym ufasz.

## Szyfrowanie połączenia SMB (SMB3 / AES)

Login i hasło kontrolują to, **kto** może się połączyć, ale same dane w większości połączeń nadal przesyłane są w postaci jawnej. **SMB to jedyne połączenie, które Everdisk potrafi zaszyfrować**, co szyfruje każdy transfer, dzięki czemu nikt inny w tej samej sieci nie może go odczytać.

Aby je włączyć:

1. Ustaw **Login** i **Hasło** jak powyżej - szyfrowane połączenia nie mogą być anonimowe.
2. Przejdź do **Ustawienia → Udostępnianie** i włącz **Wymagaj szyfrowania SMB**.
3. **Zatrzymaj i ponownie rozpocznij** udostępnianie, aby zmiana zaczęła obowiązywać.

Każdy transfer SMB jest wtedy chroniony **szyfrowaniem SMB3 (AES)**. Łączące się urządzenie musi obsługiwać SMB3 - Finder na nowoczesnym Macu albo **Windows 10 i nowszy**. To świetny wybór w sieci Wi-Fi, której nie w pełni ufasz. Szyfrowanie SMB to funkcja Premium.

## Zezwalanie na edycję lub jej blokowanie (Edycja plików)

Przełącznik **Edycja plików** kontroluje, czy podłączone urządzenia mogą tylko przeglądać Twoje pliki, czy również je zmieniać.

- **Włączony** (domyślnie): podłączone urządzenia mogą **przesyłać, zmieniać nazwy i usuwać** udostępnione pliki - dzięki czemu Twoje urządzenie działa jak prawdziwy dwukierunkowy dysk sieciowy.
- **Wyłączony**: Twoje udostępnione pliki są **tylko do odczytu**. Inni mogą je oglądać i pobierać, ale nie mogą niczego dodawać ani zmieniać.

Włączenie tej opcji wyświetla krótkie ostrzeżenie, ponieważ pozwala innym modyfikować Twoje pliki. Gdy jest włączona, ma plakietkę **Ważne**.

## Blokowanie urządzenia

Jeśli widzisz urządzenie, którego nie rozpoznajesz:

1. Na ekranie Udostępniania znajdź je w sekcji **Kto jest podłączony**.
2. Dotknij jego przycisku Więcej akcji i wybierz **Zablokuj to urządzenie**.

Zablokowane urządzenia są wymienione w **Ustawienia → Udostępnianie → Dostęp → Zablokowane urządzenia**, gdzie możesz **odblokować** jedno lub wybrać **Odblokuj wszystkie**. Blokada podąża za urządzeniem, nawet jeśli zmieni się jego adres sieciowy (dla połączeń Przeglądarka, Komputer i TV).

## Kosz kontra trwałe usuwanie

Gdy plik zostaje usunięty - przez Ciebie w menedżerze plików lub przez podłączone urządzenie - zwykle trafia do odzyskiwalnego **kosza**, dzięki czemu możesz go odzyskać.

Jeśli wolisz, aby pliki były usuwane od razu bez możliwości odzyskania, włącz **Trwale usuwaj pliki** w **Ustawienia → Menedżer plików → Usuwanie plików**. Domyślnie jest to wyłączone. **Dotyczy to menedżera plików na urządzeniu** oraz **usunięć dokonanych przez sieć**; nie zmienia to sposobu, w jaki systemowa biblioteka Zdjęć lub biblioteka Muzyki obsługują usuwanie.

## Wszystko pozostaje lokalnie

Everdisk udostępnia wyłącznie w Twojej **sieci lokalnej** - nic nie jest przesyłane do internetu i pośrodku nie ma żadnego konta w chmurze. Kilka rzeczy warto wiedzieć:

- Everdisk potrzebuje uprawnienia iOS **Sieć lokalna**, aby pobliskie urządzenia mogły go znaleźć. Jeśli to uprawnienie jest wyłączone, komunikat wyjaśni, jak włączyć je ponownie w aplikacji Ustawienia iOS.
- Aby zapewnić maksymalną prywatność, udostępniaj tylko wtedy, gdy jesteś w **domowej lub prywatnej sieci Wi-Fi**, której ufasz, i zachowaj ostrożność w publicznych sieciach Wi-Fi. Login i hasło pomagają, ale nie zastępują zaufanej sieci.
- **Najbardziej prywatną opcją ze wszystkich jest kabel USB do Maca** - dane idą prosto przez kabel i nigdy nie przechodzą przez router ani internet. Zobacz [Podłącz swoje urządzenia](/docs/guide/everdisk/everdisk-guide-connect).

## Następne kroki

- [Udostępnianie](/docs/guide/everdisk/everdisk-guide-sharing) - wybierz, co udostępnić, i rozpocznij udostępnianie.
- [Ustawienia](/docs/guide/everdisk/everdisk-guide-settings) - wszystkie ustawienia Dostępu i Menedżera plików w jednym miejscu.
