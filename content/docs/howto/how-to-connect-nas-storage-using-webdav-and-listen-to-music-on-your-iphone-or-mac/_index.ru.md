---
title: "Как подключить хранилище NAS через WebDAV и слушать музыку на iPhone или Mac"
date: 2024-07-28
description: "Узнайте, как настроить WebDAV на Synology NAS и транслировать музыку на iPhone или Mac с помощью Evermusic или Flacbox. Следуйте нашему пошаговому руководству."
keywords: ["подключить nas", "webdav synology", "транслировать музыку nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["музыка", "стриминг", "хранилище", "nas", "подключение", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Кратко:** Установите и включите WebDAV на Synology NAS, настройте разрешения общей папки, затем подключитесь из Evermusic или Flacbox, используя IP-адрес NAS и порт WebDAV (по умолчанию 5005/5006). Вы можете транслировать и управлять всей музыкальной библиотекой без копирования файлов на устройство.

Узнайте, как подключить хранилище NAS через WebDAV и легко транслировать музыкальную библиотеку на iPhone или Mac. WebDAV (Web-based Distributed Authoring and Versioning) — это протокол, позволяющий управлять файлами и обмениваться ими через Интернет. Настроив WebDAV на NAS, вы сможете получить доступ к музыкальной коллекции и транслировать её, чтобы любимые треки всегда были под рукой.

В этом руководстве мы покажем, как настроить подключение WebDAV на одном из самых популярных серверов NAS — Synology NAS. Следуйте нашим простым шагам для настройки WebDAV на Synology NAS, и вы сможете просматривать, транслировать и управлять музыкальной библиотекой прямо с iPhone или Mac.

## Шаг 1: Установка WebDAV на Synology NAS

1. Войдите в Synology NAS и откройте **Центр пакетов**.
2. Найдите "webdav" и установите пакет WebDAV, если он ещё не установлен. Откройте сервер WebDAV для настройки.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Установка WebDAV на Synology" width="600" >}}

## Шаг 2: Настройка сервера WebDAV

1. На странице настроек WebDAV установите флажки **Включить HTTP**, **Включить HTTPS**, **Включить анонимный WebDAV** и **Включить DavDepthInfinity**.
2. Нажмите **Применить** для сохранения изменений. Запишите номера портов для подключений HTTP и HTTPS — по умолчанию это 5005 и 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Настройка параметров WebDAV" width="600" >}}

## Шаг 3: Настройка разрешений общей папки

1. Откройте **Панель управления** и перейдите в раздел **Общая папка**.
2. Выберите папку **Музыка** и нажмите **Редактировать**.
3. На вкладке **Разрешения** настройте разрешения. Включите гостевой доступ с правами Только чтение, если вам нужно только слушать музыку, или Чтение/Запись, если нужно изменять файлы. Сохраните изменения.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Разрешения общей папки" width="600" >}}

## Шаг 4: Определение IP-адреса Synology NAS

1. Откройте **Панель управления** и перейдите на вкладку **Сетевой интерфейс** или используйте веб-браузер для перехода на [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Определение IP-адреса NAS" width="600" >}}

2. Запишите IP-адрес вашего Synology NAS (например, 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="IP-адрес Synology NAS" width="600" >}}

## Шаг 5: Подключение к Synology NAS через Evermusic/Flacbox

1. Откройте приложение Evermusic или Flacbox и перейдите на вкладку **Подключения**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Вкладка Подключения в Evermusic" width="600" >}}

2. Для автоматического подключения найдите Synology NAS в разделе **Доступные устройства** и нажмите для подключения.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Список доступных устройств" width="600" >}}

3. Для ручного подключения выберите **Подключить облачный сервис** и выберите **WebDAV**. Введите адрес сервера в формате: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (например, [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Ручная настройка WebDAV" width="600" >}}

4. Оставьте поля логина и пароля пустыми для гостевого доступа или введите учётные данные Synology. Нажмите **Войти**.

## Шаг 6: Навигация и воспроизведение музыки

1. После подключения устройство появится в списке **Подключенные аксессуары**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Подключённые устройства в Evermusic" width="600" >}}

2. Перейдите в папку **Музыка** и нажмите на любой аудиофайл для начала воспроизведения.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Просмотр папки с музыкой" width="600" >}}

## Шаг 7: Добавление подключённой облачной папки в музыкальную библиотеку

1. Откройте раздел **Музыкальная библиотека** в приложении.
2. Выберите **Добавить музыку** и выберите **Подключения**.
3. Выберите подключённый сервер NAS и выберите папку **Музыка**. Нажмите **Готово**.
4. Приложение просканирует папку с музыкой и добавит поддерживаемые аудиофайлы в музыкальную библиотеку. Метаданные будут загружены, и ваши треки будут сгруппированы по альбому, исполнителю и жанру.

## Заключение

Следуя этим шагам, вы можете легко настроить подключение WebDAV на Synology NAS и транслировать музыкальную библиотеку на iPhone или Mac с помощью Evermusic или Flacbox. Наслаждайтесь беспрепятственным доступом к любимым трекам в любое время.

## Часто задаваемые вопросы

{{% details title="Какие устройства NAS поддерживают WebDAV?" closed="true" %}}
Большинство популярных брендов NAS поддерживают WebDAV, включая Synology, QNAP, TrueNAS и Western Digital. Проверьте документацию производителя вашего NAS для получения инструкций по настройке WebDAV.
{{% /details %}}

{{% details title="В чём разница между WebDAV и SMB для потоковой передачи музыки с NAS?" closed="true" %}}
WebDAV работает через HTTP/HTTPS и лучше подходит для удалённого доступа через Интернет. SMB обычно быстрее в локальных сетях. Evermusic и Flacbox поддерживают оба протокола, поэтому выбирайте в зависимости от того, нужен ли вам локальный или удалённый доступ.
{{% /details %}}

{{% details title="Нужны ли имя пользователя и пароль для WebDAV на Synology?" closed="true" %}}
Нет, если вы включите анонимный доступ WebDAV и настроите гостевые разрешения для общей папки. Для лучшей безопасности вы можете использовать учётные данные Synology.
{{% /details %}}

{{% details title="Можно ли транслировать FLAC и другие форматы высокого разрешения с NAS через WebDAV?" closed="true" %}}
Да. И Evermusic, и Flacbox поддерживают FLAC, ALAC, WAV, DSD и другие форматы высокого разрешения при потоковой передаче с хранилища NAS через WebDAV.
{{% /details %}}

{{% details title="Почему приложение не может найти мой NAS в Доступных устройствах?" closed="true" %}}
Убедитесь, что ваш iPhone/Mac и NAS находятся в одной сети Wi-Fi. Если автоматическое обнаружение не работает, используйте опцию ручного подключения и введите IP-адрес NAS и порт WebDAV напрямую.
{{% /details %}}
