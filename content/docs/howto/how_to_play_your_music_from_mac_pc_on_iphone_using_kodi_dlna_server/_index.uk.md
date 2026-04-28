---
title: "Як відтворювати музику з Mac / PC / Linux / NAS на iPhone за допомогою сервера Kodi DLNA"
date: 2025-07-25
description: "Стрімте музику з комп'ютера або NAS на iPhone через Wi-Fi за допомогою Kodi DLNA та додатку Evermusic."
keywords: ["kodi dlna сервер", "стрімінг музики на iphone", "відтворення музики з nas", "evermusic dlna", "музика з mac на iphone", "музика з windows на iphone", "kodi dlna iphone", "dlna аудіо стрімінг"]
tags: ["dlna", "kodi", "evermusic", "iphone", "стрімінг музики", "mac", "nas", "linux", "локальна мережа"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Встановіть Kodi на Mac, PC, Linux або NAS, увімкніть DLNA/UPnP сервер та транслюйте всю музичну бібліотеку на iPhone або iPad за допомогою безкоштовного додатку Evermusic або Flacbox через Wi-Fi. Без підписок.

## Вступ

Якщо у вас є **Mac, ПК з Windows, комп'ютер з Linux або пристрій NAS**, ви можете легко перетворити його на **персональний музичний сервер** вдома за допомогою [Kodi](https://kodi.tv/), безкоштовної та відкритої медіаплатформи. За допомогою вбудованого **DLNA/UPnP сервера** Kodi ви можете транслювати всю музичну бібліотеку на будь-який DLNA-сумісний клієнт — включаючи ваш iPhone або iPad.

У цьому посібнику ми покажемо вам покроково, як:

- Встановити Kodi на Mac або PC
- Налаштувати музичні папки для спільного доступу
- Увімкнути музичний DLNA сервер
- Отримати доступ до музики за допомогою додатку **Evermusic** або **Flacbox** для iOS

Це налаштування на 100% безкоштовне — без підписок, лише ваша власна музика, яка транслюється по мережі Wi-Fi.

## Завантажте та встановіть Kodi на Mac / PC / Linux / NAS

Спочатку відвідайте офіційний сайт Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Головна сторінка Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Натисніть **Завантаження** та прокрутіть, щоб знайти версію для вашого комп'ютера.
Виберіть операційну систему. У цьому прикладі ми використовуємо **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Сторінка завантажень Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Натисніть **Intel (x86/64)**, якщо у вас Intel Mac, або **Apple Silicon** для M1, M2, M3 Mac, щоб почати завантаження.

{{< cards cols="1">}}
{{< card subtitle="Виберіть інсталятор macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Зачекайте, поки інсталятор завантажується.

{{< cards cols="1">}}
{{< card subtitle="Kodi завантажено" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Після завантаження знайдіть файл `.dmg` у папці **Завантаження**.

{{< cards cols="1">}}
{{< card subtitle="Встановлення Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Двічі клацніть завантажений файл для запуску інсталятора.
Перетягніть Kodi в папку **Програми** для встановлення.

{{< cards cols="1">}}
{{< card title="" subtitle="Встановіть Kodi перетягнувши в Програми" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Запустіть Kodi. Можливо, потрібно дозволити його в **Системні налаштування → Безпека та конфіденційність → Все одно відкрити**.

{{< cards cols="1">}}
{{< card subtitle="Головний екран Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Додайте музику до бібліотеки Kodi

Натисніть **іконку шестерні** (Налаштування) на головному екрані.

{{< cards cols="1">}}
{{< card subtitle="Налаштування Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Перейдіть до **Налаштування медіа → Бібліотека**. Увімкніть **Оновлювати бібліотеку при запуску** для відео- та музичної бібліотеки для автоматичної індексації.

{{< cards cols="1">}}
{{< card subtitle="Налаштування бібліотеки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Потім перейдіть до розділу **Музика** та натисніть **Додати музику**.

{{< cards cols="1">}}
{{< card subtitle="Додати музичну папку" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Перегляньте та виберіть папку, де зберігається ваша музика.

{{< cards cols="1">}}
{{< card subtitle="Виберіть джерело музики" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Додайте джерело музики до Kodi.

{{< cards cols="1">}}
{{< card subtitle="Додати джерело музики" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Підтвердіть і дозвольте Kodi просканувати вашу музичну бібліотеку.

{{< cards cols="1">}}
{{< card subtitle="Підтвердіть джерела музики" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Зачекайте, поки бібліотека сканується та повністю створюється.

{{< cards cols="1">}}
{{< card subtitle="Сканування музичної бібліотеки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Увімкніть DLNA сервер Kodi

Перейдіть до **Налаштування → Сервіси → UPnP/DLNA**.

Увімкніть опцію: **Надати спільний доступ до бібліотек**.

Kodi тепер працює як DLNA сервер у вашій локальній мережі Wi-Fi.

{{< cards cols="1">}}
{{< card subtitle="Увімкнення DLNA в Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Відкрийте бібліотеку Kodi

Клацніть правою кнопкою миші, щоб закрити вікно налаштувань та відкрити головну бібліотеку Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Правий клік для доступу до бібліотеки Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Завантажте додаток для стрімінгу музики на iOS

Отримайте безкоштовний iOS DLNA-додаток, який дозволяє транслювати музику з різних хмарних сховищ та DLNA серверів.

- Використовуйте **Evermusic**, якщо ваша колекція — переважно MP3 та інші стандартні аудіоформати.
- Виберіть **Flacbox**, якщо у вас є бібліотека музики високої роздільності у форматах FLAC, ALAC або DSD.

Обидва додатки доступні для **iOS** та **macOS** і безкоштовні.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Завантажити Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Завантажити Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Додайте DLNA-джерело

Після завантаження iOS-додатку відкрийте розділ **Усі З'єднання**.

{{< cards cols="1">}}
{{< card title="" subtitle="Головна бічна панель додатку Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Прокрутіть вниз і натисніть **Локальна мережа - Доступні пристрої** для виявлення DLNA серверів.
У цьому розділі ви побачите всі доступні пристрої у вашій локальній мережі. Ваш **Kodi DLNA сервер** повинен з'явитися тут. Натисніть на сервер Kodi для підключення.

{{< cards cols="1">}}
{{< card title="" subtitle="Доступні DLNA пристрої в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic відобразить папки бібліотеки, спільні через Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Музична бібліотека Kodi в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Перейдіть до папки **Пісні** для перегляду всіх доступних аудіофайлів на DLNA сервері.

{{< cards cols="1">}}
{{< card title="" subtitle="Пісні з віддаленої папки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Натисніть на будь-який аудіофайл, щоб миттєво розпочати стрімінг.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3 файл відтворюється в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Поверніться до розділу **З'єднання**. Доданий DLNA сервер тепер з'явиться тут. Натисніть на його іконку для повторного підключення у будь-який час.

Ви також можете увімкнути **скробблінг Last.fm** тут. Статистика відтворення буде збережена у вашому обліковому записі Last.fm.

{{< cards cols="1">}}
{{< card title="" subtitle="З'єднання в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Створіть музичну бібліотеку

**Evermusic** та **Flacbox** дозволяють додавати музику до бібліотеки та організовувати її за **тегами метаданих**: виконавці, альбоми, жанри та композитори.

Для початку відкрийте розділ **Музична бібліотека**. Прокрутіть вниз до **Інструменти та налаштування** і натисніть **Додати музику**.

{{< cards cols="1">}}
{{< card title="" subtitle="Музична бібліотека Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Виберіть джерело музики — у цьому випадку виберіть **З'єднання**.

{{< cards cols="1">}}
{{< card title="" subtitle="Додати нову музику в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Знайдіть **Kodi DLNA сервер** у З'єднаннях і натисніть для перегляду папок і файлів.

{{< cards cols="1">}}
{{< card title="" subtitle="Виберіть DLNA сервер для імпорту музики" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Виберіть папки або файли, які хочете додати, і натисніть **Готово**.

{{< cards cols="1">}}
{{< card title="" subtitle="Виберіть папку з музикою для додавання" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Додаток просканує вибрані файли та організує їх за допомогою метаданих у розділи: Виконавці, Альбоми, Жанри та Композитори.

{{< cards cols="1">}}
{{< card title="" subtitle="Музична бібліотека з категоріями" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Створіть плейлисти

Ви також можете створювати власні плейлисти.

Спочатку відкрийте вкладку **Плейлисти**.

{{< cards cols="1">}}
{{< card title="" subtitle="Вкладка Плейлисти в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Натисніть кнопку **плюс (+)** і виберіть **Новий плейлист**.

{{< cards cols="1">}}
{{< card title="" subtitle="Створити новий плейлист" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Введіть назву плейлиста і натисніть **Зберегти**.

{{< cards cols="1">}}
{{< card title="" subtitle="Введіть назву плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Далі виберіть джерело для додавання пісень — тут ми вибираємо **Бібліотеку**.

{{< cards cols="1">}}
{{< card title="" subtitle="Додати пісні до нового плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Виберіть потрібні пісні і натисніть **Готово** для додавання.

{{< cards cols="1">}}
{{< card title="" subtitle="Додати музику з бібліотеки до плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Вибрані треки тепер з'являться у створеному плейлисті.

{{< cards cols="1">}}
{{< card title="" subtitle="Створений плейлист у списку" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

За замовчуванням пісні доступні для стрімінгу. Для прослуховування офлайн увімкніть **Офлайн режим** — додаток завантажить усі треки плейлиста.

{{< cards cols="1">}}
{{< card title="" subtitle="Офлайн режим увімкнено для плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Натисніть кнопку **Більше дій** для вивчення додаткових опцій. Ви можете:

- Архівувати плейлист
- Змінити обкладинку альбому
- Змінити порядок треків
- І інші корисні функції

{{< cards cols="1">}}
{{< card title="" subtitle="Додаткові дії плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Висновок

З **Evermusic** та **Flacbox** перетворити iPhone, iPad або Mac на потужний DLNA-плеєр легко.

- Стрімте MP3 або hi-res FLAC прямо з вашого **Kodi DLNA сервера**
- Створіть персональну музичну бібліотеку, згруповану за метаданими (альбоми, жанри, композитори)
- Створюйте та керуйте **користувацькими плейлистами**
- Увімкніть **офлайн режим** для прослуховування в дорозі
- Підключайтесь до **кількох хмарних сервісів** та **пристроїв локальної мережі**
- Відстежуйте звички прослуховування з **інтеграцією Last.fm**

Будь ви аудіофілом або звичайним слухачем, Evermusic та Flacbox пропонують усе необхідне для безперебійного стрімінгу та організації музики.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Завантажити Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Завантажити Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Почніть створювати свій персональний музичний досвід вже сьогодні.

## Часті запитання

{{% details title="Kodi безкоштовний як DLNA сервер?" closed="true" %}}
Так. Kodi повністю безкоштовний та має відкритий вихідний код. Працює на macOS, Windows, Linux та багатьох пристроях NAS.
{{% /details %}}

{{% details title="Чи підтримують Evermusic та Flacbox стрімінг FLAC через DLNA?" closed="true" %}}
Так. Flacbox оптимізований для форматів високої роздільності, таких як FLAC, ALAC та DSD. Evermusic також підтримує відтворення FLAC.
{{% /details %}}

{{% details title="Чи можу я слухати офлайн після стрімінгу з Kodi?" closed="true" %}}
Так. Увімкніть Офлайн режим на будь-якому плейлисті, і додаток завантажить усі треки на пристрій.
{{% /details %}}

{{% details title="Чи потрібна мені преміум-підписка для використання DLNA?" closed="true" %}}
Безкоштовна версія підтримує до 3 хмарних або мережевих підключень. Преміум знімає це обмеження.
{{% /details %}}

{{% details title="Чи повинен мій iPhone бути в тій самій мережі Wi-Fi, що й Kodi?" closed="true" %}}
Так. DLNA стрімінг працює через локальну мережу. Сервер Kodi та пристрій iOS повинні бути підключені до однієї мережі Wi-Fi.
{{% /details %}}

{{% details title="Чи можу я використовувати це налаштування з NAS замість Mac або PC?" closed="true" %}}
Так. Багато пристроїв NAS (Synology, QNAP тощо) підтримують Kodi або мають власний вбудований DLNA сервер. Evermusic та Flacbox можуть підключатися до будь-якого стандартного DLNA/UPnP сервера.
{{% /details %}}
