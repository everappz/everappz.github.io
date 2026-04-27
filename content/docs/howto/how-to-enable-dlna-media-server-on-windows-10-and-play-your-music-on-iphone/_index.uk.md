---
title: "Як увімкнути DLNA медіасервер у Windows 10 та слухати музику на iPhone"
date: 2019-11-26
description: "Увімкніть DLNA-сервер у Windows 10 та транслюйте музику на iPhone за допомогою додатку Evermusic. Покрокова інструкція з налаштування."
keywords: ["evermusic", "dlna", "windows 10", "потокова музика на iphone", "медіасервер", "локальна мережа", "upnp"]
tags: ["evermusic", "музика", "хмара", "iphone", "сховище", "локальний", "nas", "windows", "wifi", "слухати", "мережа", "віддалений", "дім", "онлайн", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Коротко:** Windows 10 має вбудований DLNA-сервер. Увімкніть його в налаштуваннях мережі та спільного доступу, потім використовуйте безкоштовний додаток **Evermusic** на iPhone для трансляції всієї музичної бібліотеки через Wi-Fi. Стороннє серверне ПЗ не потрібне.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Обкладинка" caption="Потокова передача музики через DLNA на iPhone за допомогою Windows 10 та Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) — це потужний інструмент, який дозволяє легко транслювати різноманітний медіаконтент, включаючи музику, між пристроями з підтримкою DLNA у вашій мережі. Гарна новина полягає в тому, що Windows 10 та попередні версії мають вбудовану функцію DLNA, що усуває потребу у сторонніх медіасерверах. Ось як увімкнути DLNA медіасервер у Windows 10 та насолоджуватися потоковою музикою на iPhone.

## Як увімкнути DLNA медіасервер у Windows 10

1. Натисніть кнопку «Пуск».  
2. Виберіть значок «Параметри».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Налаштування сервера" caption="Відкрийте Параметри Windows" width="500" >}}

3. На екрані «Параметри Windows» виберіть «Мережа та Інтернет».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Параметри Windows" caption="Виберіть Мережа та Інтернет" width="500" >}}

4. У розділі «Мережа» виберіть «Центр мережевих підключень та спільного доступу».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Центр спільного доступу" caption="Відкрийте Центр мережевих підключень та спільного доступу" width="500" >}}

5. На екрані «Центр мережевих підключень та спільного доступу» натисніть «Змінити додаткові параметри спільного доступу» у лівому меню.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Додаткові параметри спільного доступу" caption="Змінити додаткові параметри спільного доступу" width="500" >}}

6. На екрані «Додаткові параметри спільного доступу» прокрутіть вниз до розділу «Усі мережі» та розгорніть його, натиснувши на стрілку.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Увімкнути виявлення" caption="Розгорніть параметри всіх мереж" width="500" >}}

7. Натисніть «Увімкнути потокову передачу мультимедіа» для активації DLNA-сервера.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Увімкнути сервер" caption="Увімкніть сервер потокової передачі мультимедіа" width="500" >}}

8. Дайте назву медіабібліотеці та виберіть пристрої, яким дозволено доступ.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Назва медіабібліотеки" caption="Назвіть вашу DLNA медіабібліотеку" width="500" >}}

9. Натисніть «ОК» для підтвердження. Тепер ваші особисті папки — Музика, Зображення та Відео — будуть видимі для всіх пристроїв з підтримкою UPnP.

## Як вимкнути DLNA медіасервер у Windows 10

1. Натисніть «Пуск» та введіть «services» у поле пошуку.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Служби Windows" caption="Відкрийте Служби Windows" width="500" >}}

2. На екрані «Служби» прокрутіть вниз, щоб знайти «Служба спільного доступу до мережі програвача Windows Media».  
3. Двічі клацніть на ній та встановіть «Тип запуску» на «Вручну».  
4. Зупиніть службу, натиснувши кнопку «Зупинити».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Зупинити службу DLNA" caption="Вимкніть службу мережевого спільного доступу DLNA" width="500" >}}

## Як відтворювати музику з DLNA-сервера на iPhone

1. Встановіть безкоштовний додаток **Evermusic** з App Store:  
   [Додаток Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Відкрийте вкладку «Підключення» та натисніть «Доступні пристрої» в розділі «Локальна мережа».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Підключення Evermusic" caption="Evermusic: екран Підключення" width="500" >}}

3. Зачекайте кілька секунд, поки завантажиться список пристроїв, та натисніть на DLNA-сервер Windows Media Player (наприклад, «MSEDGEWIN10: My Windows Library»).

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Доступні пристрої" caption="Доступні DLNA-сервери в Evermusic" width="500" >}}

4. Ви побачите список папок, доступних на медіасервері.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Папки Evermusic" caption="Перегляд спільних папок з DLNA-сервера" width="500" >}}

5. Відкрийте будь-яку папку з аудіофайлами.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Вміст папки" caption="Перегляд вмісту спільних DLNA-папок" width="500" >}}

6. Натисніть на будь-який файл, щоб запустити аудіоплеєр.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Аудіоплеєр" caption="Відтворення аудіофайлу з DLNA в Evermusic" width="500" >}}

7. Для покращення звучання натисніть значок «Еквалайзер» біля індикатора гучності внизу екрана, щоб увімкнути еквалайзер у стилі iPod з передпідсилювачем.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Еквалайзер" caption="Використовуйте вбудований еквалайзер для покращеного відтворення" width="500" >}}

## Висновок

З DLNA медіасервером у Windows 10 та Evermusic на iPhone ви можете насолоджуватися безперервною потоковою передачею музики з комп'ютера на мобільний пристрій. Попрощайтеся з обмеженнями сховища та привітайте музику на вимогу!

## Часті запитання

{{% details title="Чи потрібно встановлювати серверне ПЗ на Windows 10?" closed="true" %}}
Ні. Windows 10 містить вбудований DLNA медіасервер. Вам потрібно лише увімкнути потокову передачу мультимедіа в налаштуваннях Центру мережевих підключень та спільного доступу. Стороннє ПЗ не потрібне.
{{% /details %}}

{{% details title="Чи повинен мій iPhone бути в тій самій мережі Wi-Fi?" closed="true" %}}
Так. Потокова передача DLNA працює через вашу локальну мережу. І комп'ютер з Windows 10, і iPhone повинні бути підключені до однієї мережі Wi-Fi, щоб Evermusic міг виявити DLNA-сервер.
{{% /details %}}

{{% details title="Які аудіоформати можна транслювати через DLNA?" closed="true" %}}
DLNA-сервер Windows надає спільний доступ до файлів із папки Музика незалежно від формату. Evermusic підтримує MP3, FLAC, AAC, WAV, OGG, AIFF та багато інших форматів, тому ви можете відтворити практично будь-який аудіофайл із сервера.
{{% /details %}}

{{% details title="Чи можна використовувати Flacbox замість Evermusic?" closed="true" %}}
Так. Flacbox також підтримує перегляд та відтворення через DLNA/UPnP. Ви можете використовувати будь-який із двох додатків для виявлення та відтворення музики з вашого DLNA-сервера Windows.
{{% /details %}}

{{% details title="Чи використовує потокова передача DLNA мобільні дані?" closed="true" %}}
Ні. DLNA працює виключно через вашу локальну мережу Wi-Fi. Мобільні дані не використовуються. Однак обидва пристрої повинні залишатися підключеними до однієї мережі під час відтворення.
{{% /details %}}
