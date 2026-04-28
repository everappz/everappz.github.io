---
title: "Як підключити сховище NAS через WebDAV і слухати музику на iPhone або Mac"
date: 2024-07-28
description: "Дізнайтеся, як налаштувати WebDAV на Synology NAS і транслювати музику на iPhone або Mac за допомогою Evermusic або Flacbox. Дотримуйтесь нашого покрокового посібника."
keywords: ["підключити nas", "webdav synology", "транслювати музику nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["музика", "стримінг", "сховище", "nas", "підключення", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Коротко:** Встановіть і увімкніть WebDAV на Synology NAS, налаштуйте дозволи спільної папки, потім підключіться з Evermusic або Flacbox, використовуючи IP-адресу NAS і порт WebDAV (за замовчуванням 5005/5006). Ви можете транслювати та керувати всією музичною бібліотекою без копіювання файлів на пристрій.

Дізнайтеся, як підключити сховище NAS через WebDAV і легко транслювати музичну бібліотеку на iPhone або Mac. WebDAV (Web-based Distributed Authoring and Versioning) — це протокол, який дозволяє керувати файлами та обмінюватися ними через Інтернет. Налаштувавши WebDAV на NAS, ви зможете отримати доступ до музичної колекції та транслювати її, щоб улюблені треки завжди були під рукою.

У цьому посібнику ми покажемо, як налаштувати підключення WebDAV на одному з найпопулярніших серверів NAS — Synology NAS. Дотримуйтесь наших простих кроків для налаштування WebDAV на Synology NAS, і ви зможете переглядати, транслювати та керувати музичною бібліотекою прямо з iPhone або Mac.

## Крок 1: Встановлення WebDAV на Synology NAS

1. Увійдіть до Synology NAS і відкрийте **Центр пакетів**.
2. Знайдіть "webdav" і встановіть пакет WebDAV, якщо він ще не встановлений. Відкрийте сервер WebDAV для налаштування.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Встановлення WebDAV на Synology" width="600" >}}

## Крок 2: Налаштування сервера WebDAV

1. На сторінці налаштувань WebDAV встановіть прапорці **Увімкнути HTTP**, **Увімкнути HTTPS**, **Увімкнути анонімний WebDAV** та **Увімкнути DavDepthInfinity**.
2. Натисніть **Застосувати** для збереження змін. Запишіть номери портів для підключень HTTP та HTTPS — за замовчуванням це 5005 і 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Налаштування параметрів WebDAV" width="600" >}}

## Крок 3: Налаштування дозволів спільної папки

1. Відкрийте **Панель керування** і перейдіть до розділу **Спільна папка**.
2. Виберіть папку **Музика** і натисніть **Редагувати**.
3. На вкладці **Дозволи** налаштуйте дозволи. Увімкніть гостьовий доступ з правами Лише читання, якщо потрібно тільки слухати музику, або Читання/Запис, якщо потрібно змінювати файли. Збережіть зміни.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Дозволи спільної папки" width="600" >}}

## Крок 4: Визначення IP-адреси Synology NAS

1. Відкрийте **Панель керування** і перейдіть на вкладку **Мережевий інтерфейс** або використайте веб-браузер для переходу на [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Визначення IP-адреси NAS" width="600" >}}

2. Запишіть IP-адресу вашого Synology NAS (наприклад, 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="IP-адреса Synology NAS" width="600" >}}

## Крок 5: Підключення до Synology NAS через Evermusic/Flacbox

1. Відкрийте додаток Evermusic або Flacbox і перейдіть на вкладку **З'єднання**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Вкладка З'єднання в Evermusic" width="600" >}}

2. Для автоматичного підключення знайдіть Synology NAS у розділі **Доступні пристрої** і натисніть для підключення.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Список доступних пристроїв" width="600" >}}

3. Для ручного підключення виберіть **Підключити хмарний сервіс** і виберіть **WebDAV**. Введіть адресу сервера у форматі: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (наприклад, [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Ручне налаштування WebDAV" width="600" >}}

4. Залиште поля логіна та пароля порожніми для гостьового доступу або введіть облікові дані Synology. Натисніть **Увійти**.

## Крок 6: Навігація та відтворення музики

1. Після підключення пристрій з'явиться у списку **Підключені аксесуари**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Підключені пристрої в Evermusic" width="600" >}}

2. Перейдіть до папки **Музика** і натисніть на будь-який аудіофайл для початку відтворення.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Перегляд папки з музикою" width="600" >}}

## Крок 7: Додавання підключеної хмарної папки до музичної бібліотеки

1. Відкрийте розділ **Музична бібліотека** в додатку.
2. Виберіть **Додати музику** і виберіть **З'єднання**.
3. Виберіть підключений сервер NAS і виберіть папку **Музика**. Натисніть **Готово**.
4. Додаток просканує папку з музикою і додасть підтримувані аудіофайли до музичної бібліотеки. Метадані будуть завантажені, і ваші треки будуть згруповані за альбомом, виконавцем та жанром.

## Висновок

Дотримуючись цих кроків, ви можете легко налаштувати підключення WebDAV на Synology NAS і транслювати музичну бібліотеку на iPhone або Mac за допомогою Evermusic або Flacbox. Насолоджуйтесь безперешкодним доступом до улюблених треків у будь-який час.

## Поширені запитання

{{% details title="Які пристрої NAS підтримують WebDAV?" closed="true" %}}
Більшість популярних брендів NAS підтримують WebDAV, включаючи Synology, QNAP, TrueNAS та Western Digital. Перевірте документацію виробника вашого NAS для отримання інструкцій з налаштування WebDAV.
{{% /details %}}

{{% details title="У чому різниця між WebDAV і SMB для потокової передачі музики з NAS?" closed="true" %}}
WebDAV працює через HTTP/HTTPS і краще підходить для віддаленого доступу через Інтернет. SMB зазвичай швидший у локальних мережах. Evermusic і Flacbox підтримують обидва протоколи, тому обирайте залежно від того, чи потрібен вам локальний або віддалений доступ.
{{% /details %}}

{{% details title="Чи потрібні ім'я користувача та пароль для WebDAV на Synology?" closed="true" %}}
Ні, якщо ви увімкнете анонімний доступ WebDAV і налаштуєте гостьові дозволи для спільної папки. Для кращої безпеки ви можете використовувати облікові дані Synology.
{{% /details %}}

{{% details title="Чи можу я транслювати FLAC та інші формати високої роздільної здатності з NAS через WebDAV?" closed="true" %}}
Так. І Evermusic, і Flacbox підтримують FLAC, ALAC, WAV, DSD та інші формати високої роздільної здатності при потоковій передачі зі сховища NAS через WebDAV.
{{% /details %}}

{{% details title="Чому додаток не може знайти мій NAS у Доступних пристроях?" closed="true" %}}
Переконайтеся, що ваш iPhone/Mac і NAS знаходяться в одній мережі Wi-Fi. Якщо автоматичне виявлення не працює, використовуйте опцію ручного підключення та введіть IP-адресу NAS і порт WebDAV безпосередньо.
{{% /details %}}
