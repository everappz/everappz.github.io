---
title: "Jak podłączyć wewnętrzną pamięć Bluesound VAULT z aplikacji Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Dowiedz się, jak uzyskać dostęp do wewnętrznego dysku twardego Bluesound VAULT z aplikacji Evermusic, Flacbox i Evertag za pomocą protokołu SMB do zarządzania, edytowania i odtwarzania plików audio."
keywords: ["bluesound vault", "podłączyć pamięć smb", "evermusic smb", "flacbox vault", "evertag smb", "pamięć nas muzyka", "wewnętrzny dysk vault"]
tags: ["evermusic", "połączyć", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Podsumowanie:** Połącz się z wewnętrzną pamięcią Bluesound VAULT przez SMB za pomocą Evermusic, Flacbox lub Evertag. Znajdź adres IP VAULT w aplikacji BluOS, wprowadź go jako połączenie SMB z dostępem gościa i zacznij odtwarzać lub zarządzać plikami muzycznymi.

Bluesound VAULT posiada wewnętrzny dysk twardy i działa jako sieciowa pamięć masowa (NAS). Dostęp do wewnętrznego dysku twardego VAULT umożliwia dodawanie/usuwanie plików, edytowanie tagów metadanych z naszych aplikacji Evermusic, Flacbox, Evertag.

**Poniżej znajdują się kroki dostępu do wewnętrznego dysku twardego VAULT:**

1. W aplikacji BluOS wybierz **Pomoc > Diagnostyka**.

2. Na stronie **Diagnostyka** uzyskaj **Adres IP** VAULT. Ten **Adres IP** będzie używany w kolejnych krokach.

3. Otwórz Evermusic, Flacbox lub Evertag.

   ![Aplikacje Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Otwórz ekran "Połączenia" i wybierz pozycję menu "Podłącz usługę chmurową".

   ![Ekran Połączenia Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Wybierz usługę chmurową "SMB".

   ![Ekran Podłącz usługę chmurową Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Na "Ekranie konfiguracji SMB" wprowadź URL w następującym formacie:

   ```
   SMB://<<VAULT-IP>>
   ```

   Zastąp `<<VAULT-IP>>` **Adresem IP** uzyskanym w Kroku 2.

   **Uwaga:** Pozostaw pola Login i Hasło puste, ponieważ pamięć VAULT obsługuje tryb GOŚCIA.

   ![Ekran połączenia SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Dotknij przycisku "Zaloguj się", aby zapisać konfigurację.

8. Otwórz podłączoną pamięć chmurową, przejdź do folderu z plikami audio i dotknij dowolnego pliku, aby uruchomić odtwarzacz audio.

   ![Ekran otwartego serwera SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Możesz również edytować pliki za pomocą wbudowanego menedżera plików.

   ![Ekran Menedżera Plików Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Dzięki tym prostym krokom możesz łatwo uzyskać dostęp do wewnętrznego dysku twardego Bluesound VAULT i przejąć kontrolę nad swoją biblioteką muzyczną za pomocą Evermusic, Flacbox lub Evertag.

## Często zadawane pytania

{{% details title="Czy potrzebuję nazwy użytkownika i hasła, aby połączyć się z Bluesound VAULT?" closed="true" %}}
Nie. Bluesound VAULT obsługuje dostęp gościa (anonimowy) przez SMB. Pozostaw pola Login i Hasło puste podczas konfigurowania połączenia.
{{% /details %}}

{{% details title="Czy mogę edytować tagi muzyczne na Bluesound VAULT?" closed="true" %}}
Tak. Za pomocą Evertag możesz edytować tagi metadanych (tytuł, artysta, album itp.) plików audio przechowywanych bezpośrednio na wewnętrznym dysku twardym VAULT.
{{% /details %}}

{{% details title="Jakie protokoły obsługuje Bluesound VAULT?" closed="true" %}}
Bluesound VAULT udostępnia swoją wewnętrzną pamięć przez SMB (Server Message Block). Evermusic, Flacbox i Evertag obsługują połączenia SMB, co ułatwia połączenie.
{{% /details %}}

{{% details title="Czy mogę strumieniować muzykę z VAULT bez kopiowania plików na iPhone?" closed="true" %}}
Tak. Po połączeniu przez SMB możesz strumieniować pliki audio bezpośrednio z wewnętrznego dysku VAULT bez kopiowania ich na urządzenie.
{{% /details %}}
