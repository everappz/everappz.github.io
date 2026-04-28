---
title: "Как воспроизводить музыку с Mac / PC / Linux / NAS на iPhone с помощью сервера Kodi DLNA"
date: 2025-07-25
description: "Стримьте музыку с компьютера или NAS на iPhone через Wi-Fi с помощью Kodi DLNA и приложения Evermusic."
keywords: ["kodi dlna сервер", "стриминг музыки на iphone", "воспроизведение музыки с nas", "evermusic dlna", "музыка с mac на iphone", "музыка с windows на iphone", "kodi dlna iphone", "dlna аудио стриминг"]
tags: ["dlna", "kodi", "evermusic", "iphone", "стриминг музыки", "mac", "nas", "linux", "локальная сеть"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Установите Kodi на Mac, PC, Linux или NAS, включите DLNA/UPnP сервер и транслируйте всю музыкальную библиотеку на iPhone или iPad с помощью бесплатного приложения Evermusic или Flacbox по Wi-Fi. Без подписок.

## Введение

Если у вас есть **Mac, ПК с Windows, компьютер с Linux или устройство NAS**, вы можете легко превратить его в **персональный музыкальный сервер** дома с помощью [Kodi](https://kodi.tv/), бесплатной и открытой медиаплатформы. С помощью встроенного **DLNA/UPnP сервера** Kodi вы можете транслировать всю музыкальную библиотеку на любой DLNA-совместимый клиент — включая ваш iPhone или iPad.

В этом руководстве мы покажем вам пошагово, как:

- Установить Kodi на Mac или PC
- Настроить музыкальные папки для общего доступа
- Включить музыкальный DLNA сервер
- Получить доступ к музыке с помощью приложения **Evermusic** или **Flacbox** для iOS

Эта настройка на 100% бесплатна — без подписок, только ваша собственная музыка, транслируемая по сети Wi-Fi. Хотите ли вы организовать большую коллекцию MP3, слушать FLAC по Wi-Fi или просто наслаждаться локальной музыкой без синхронизации через iTunes — эта настройка идеально подходит для вас.

## Скачайте и установите Kodi на Mac / PC / Linux / NAS

Сначала посетите официальный сайт Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Главная страница Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Нажмите **Загрузки** и прокрутите, чтобы найти версию для вашего компьютера.
Выберите операционную систему. В этом примере мы используем **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Страница загрузок Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Нажмите **Intel (x86/64)**, если у вас Intel Mac, или **Apple Silicon** для M1, M2, M3 Mac, чтобы начать загрузку.

{{< cards cols="1">}}
{{< card subtitle="Выберите установщик macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Подождите, пока установщик загружается.

{{< cards cols="1">}}
{{< card subtitle="Kodi загружен" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

После загрузки найдите файл `.dmg` в папке **Загрузки**.

{{< cards cols="1">}}
{{< card subtitle="Установка Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Дважды щёлкните загруженный файл для запуска установщика.
Перетащите Kodi в папку **Программы** для установки.

{{< cards cols="1">}}
{{< card title="" subtitle="Установите Kodi перетащив в Программы" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Запустите Kodi. Возможно, потребуется разрешить его в **Системные настройки → Безопасность и конфиденциальность → Всё равно открыть**.

{{< cards cols="1">}}
{{< card subtitle="Главный экран Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Добавьте музыку в библиотеку Kodi

Нажмите **значок шестерёнки** (Настройки) на главном экране.

{{< cards cols="1">}}
{{< card subtitle="Настройки Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Перейдите в **Настройки медиа → Библиотека**. Включите **Обновлять библиотеку при запуске** для видео- и музыкальной библиотеки для автоматической индексации.

{{< cards cols="1">}}
{{< card subtitle="Настройки библиотеки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Затем перейдите в раздел **Музыка** и нажмите **Добавить музыку**.

{{< cards cols="1">}}
{{< card subtitle="Добавить музыкальную папку" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Просмотрите и выберите папку, в которой хранится ваша музыка.

{{< cards cols="1">}}
{{< card subtitle="Выберите источник музыки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Добавьте источник музыки в Kodi.

{{< cards cols="1">}}
{{< card subtitle="Добавить источник музыки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Подтвердите и позвольте Kodi просканировать вашу музыкальную библиотеку.

{{< cards cols="1">}}
{{< card subtitle="Подтвердите источники музыки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Подождите, пока библиотека сканируется и полностью создаётся.

{{< cards cols="1">}}
{{< card subtitle="Сканирование музыкальной библиотеки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Включите DLNA сервер Kodi

Перейдите в **Настройки → Сервисы → UPnP/DLNA**.

Включите опцию: **Предоставить общий доступ к библиотекам**.

Kodi теперь работает как DLNA сервер в вашей локальной сети Wi-Fi.

{{< cards cols="1">}}
{{< card subtitle="Включение DLNA в Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Откройте библиотеку Kodi

Щёлкните правой кнопкой мыши, чтобы закрыть окно настроек и открыть главную библиотеку Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Правый клик для доступа к библиотеке Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Скачайте приложение для стриминга музыки на iOS

Получите бесплатное iOS DLNA-приложение, которое позволяет транслировать музыку из различных облачных хранилищ и DLNA серверов.

- Используйте **Evermusic**, если ваша коллекция — в основном MP3 и другие стандартные аудиоформаты.
- Выберите **Flacbox**, если у вас есть библиотека музыки высокого разрешения в форматах FLAC, ALAC или DSD.

Оба приложения доступны для **iOS** и **macOS** и бесплатны.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Скачать Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Скачать Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Добавьте DLNA-источник

После загрузки iOS-приложения откройте раздел **Все Подключения**.

{{< cards cols="1">}}
{{< card title="" subtitle="Главная боковая панель приложения Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Прокрутите вниз и нажмите **Локальная сеть - Доступные устройства** для обнаружения DLNA серверов.
В этом разделе вы увидите все доступные устройства в вашей локальной сети. Ваш **Kodi DLNA сервер** должен появиться здесь. Нажмите на сервер Kodi для подключения.

{{< cards cols="1">}}
{{< card title="" subtitle="Доступные DLNA устройства в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic отобразит папки библиотеки, общие через Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Музыкальная библиотека Kodi в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Перейдите в папку **Песни** для просмотра всех доступных аудиофайлов на DLNA сервере.

{{< cards cols="1">}}
{{< card title="" subtitle="Песни из удалённой папки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Нажмите на любой аудиофайл, чтобы мгновенно начать стриминг.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3 файл воспроизводится в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Вернитесь в раздел **Подключения**. Добавленный DLNA сервер теперь появится здесь. Нажмите на его значок для повторного подключения в любое время. Вы также можете подключить другие облачные сервисы с этого экрана, используя те же шаги.

Вы также можете включить **скробблинг Last.fm** здесь. Статистика воспроизведения будет сохранена в вашем аккаунте Last.fm, предоставляя персонализированные музыкальные рекомендации позже.

{{< cards cols="1">}}
{{< card title="" subtitle="Подключения в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Создайте музыкальную библиотеку

**Evermusic** и **Flacbox** позволяют добавлять музыку в библиотеку и организовывать её по **тегам метаданных**: исполнители, альбомы, жанры и композиторы.

Для начала откройте раздел **Музыкальная библиотека**. Прокрутите вниз до **Инструменты и настройки** и нажмите **Добавить музыку**.

{{< cards cols="1">}}
{{< card title="" subtitle="Музыкальная библиотека Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Выберите источник музыки — в данном случае выберите **Подключения**.

{{< cards cols="1">}}
{{< card title="" subtitle="Добавить новую музыку в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Найдите **Kodi DLNA сервер** в Подключениях и нажмите для просмотра папок и файлов.

{{< cards cols="1">}}
{{< card title="" subtitle="Выберите DLNA сервер для импорта музыки" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Выберите папки или файлы, которые хотите добавить, и нажмите **Готово**.

{{< cards cols="1">}}
{{< card title="" subtitle="Выберите папку с музыкой для добавления" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Приложение просканирует выбранные файлы и организует их с помощью метаданных в разделы: Исполнители, Альбомы, Жанры и Композиторы.

{{< cards cols="1">}}
{{< card title="" subtitle="Музыкальная библиотека с категориями" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Создайте плейлисты

Вы также можете создавать собственные плейлисты.

Сначала откройте вкладку **Плейлисты**.

{{< cards cols="1">}}
{{< card title="" subtitle="Вкладка Плейлисты в Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Нажмите кнопку **плюс (+)** и выберите **Новый плейлист**.

{{< cards cols="1">}}
{{< card title="" subtitle="Создать новый плейлист" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Введите название плейлиста и нажмите **Сохранить**.

{{< cards cols="1">}}
{{< card title="" subtitle="Введите название плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Далее выберите источник для добавления песен — здесь мы выбираем **Библиотеку**.

{{< cards cols="1">}}
{{< card title="" subtitle="Добавить песни в новый плейлист" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Выберите нужные песни и нажмите **Готово** для добавления.

{{< cards cols="1">}}
{{< card title="" subtitle="Добавить музыку из библиотеки в плейлист" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Выбранные треки теперь появятся в созданном плейлисте.

{{< cards cols="1">}}
{{< card title="" subtitle="Созданный плейлист в списке" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

По умолчанию песни доступны для стриминга. Для прослушивания офлайн включите **Офлайн режим** — приложение загрузит все треки плейлиста.

{{< cards cols="1">}}
{{< card title="" subtitle="Офлайн режим включён для плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Нажмите кнопку **Другие действия** для изучения дополнительных опций. Вы можете:

- Архивировать плейлист
- Изменить обложку альбома
- Изменить порядок треков
- И другие полезные функции

{{< cards cols="1">}}
{{< card title="" subtitle="Дополнительные действия плейлиста" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Заключение

С **Evermusic** и **Flacbox** превратить iPhone, iPad или Mac в мощный DLNA-плеер легко. Храните ли вы музыку в облаке, на NAS или на домашнем медиасервере, таком как **Kodi**, эти приложения позволяют транслировать, организовывать и наслаждаться коллекцией без ограничений.

- Стримьте MP3 или hi-res FLAC прямо с вашего **Kodi DLNA сервера**
- Создайте персональную музыкальную библиотеку, сгруппированную по метаданным (альбомы, жанры, композиторы)
- Создавайте и управляйте **пользовательскими плейлистами**
- Включите **офлайн режим** для прослушивания в дороге
- Подключайтесь к **нескольким облачным сервисам** и **устройствам локальной сети**
- Отслеживайте привычки прослушивания с **интеграцией Last.fm**

Будь вы аудиофилом или обычным слушателем, Evermusic и Flacbox предлагают всё необходимое для бесперебойного стриминга и организации музыки.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Скачать Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Скачать Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Начните создавать свой персональный музыкальный опыт уже сегодня.

## Часто задаваемые вопросы

{{% details title="Kodi бесплатен в качестве DLNA сервера?" closed="true" %}}
Да. Kodi полностью бесплатен и имеет открытый исходный код. Работает на macOS, Windows, Linux и многих устройствах NAS.
{{% /details %}}

{{% details title="Поддерживают ли Evermusic и Flacbox стриминг FLAC через DLNA?" closed="true" %}}
Да. Flacbox оптимизирован для форматов высокого разрешения, таких как FLAC, ALAC и DSD. Evermusic также поддерживает воспроизведение FLAC наряду с MP3 и другими стандартными форматами.
{{% /details %}}

{{% details title="Могу ли я слушать офлайн после стриминга с Kodi?" closed="true" %}}
Да. Включите Офлайн режим на любом плейлисте, и приложение загрузит все треки на устройство для прослушивания без сетевого подключения.
{{% /details %}}

{{% details title="Нужна ли мне премиум-подписка для использования DLNA?" closed="true" %}}
Бесплатная версия поддерживает до 3 облачных или сетевых подключений. Премиум убирает это ограничение и позволяет подключать неограниченное количество сервисов и DLNA серверов.
{{% /details %}}

{{% details title="Должен ли мой iPhone быть в той же сети Wi-Fi, что и Kodi?" closed="true" %}}
Да. DLNA стриминг работает через локальную сеть. Сервер Kodi и устройство iOS должны быть подключены к одной сети Wi-Fi.
{{% /details %}}

{{% details title="Могу ли я использовать эту настройку с NAS вместо Mac или PC?" closed="true" %}}
Да. Многие устройства NAS (Synology, QNAP и др.) поддерживают Kodi или имеют собственный встроенный DLNA сервер. Evermusic и Flacbox могут подключаться к любому стандартному DLNA/UPnP серверу.
{{% /details %}}
