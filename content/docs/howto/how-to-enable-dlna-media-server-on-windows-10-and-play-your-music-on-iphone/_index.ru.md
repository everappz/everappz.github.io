---
title: "Как включить DLNA медиасервер в Windows 10 и слушать музыку на iPhone"
date: 2019-11-26
description: "Включите DLNA-сервер в Windows 10 и транслируйте музыку на iPhone с помощью приложения Evermusic. Пошаговое руководство по настройке."
keywords: ["evermusic", "dlna", "windows 10", "потоковая музыка на iphone", "медиасервер", "локальная сеть", "upnp"]
tags: ["evermusic", "музыка", "облако", "iphone", "хранилище", "локальный", "nas", "windows", "wifi", "слушать", "сеть", "удалённый", "дом", "онлайн", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Кратко:** В Windows 10 есть встроенный DLNA-сервер. Включите его в настройках сети и общего доступа, затем используйте бесплатное приложение **Evermusic** на iPhone для потоковой передачи всей музыкальной библиотеки через Wi-Fi. Стороннее серверное ПО не требуется.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Обложка" caption="Потоковая передача музыки через DLNA на iPhone с помощью Windows 10 и Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) — это мощный инструмент, позволяющий легко транслировать различный медиаконтент, включая музыку, между устройствами с поддержкой DLNA в вашей сети. Хорошая новость в том, что Windows 10 и предыдущие версии имеют встроенную функцию DLNA, что устраняет необходимость в сторонних медиасерверах. Вот как включить DLNA медиасервер в Windows 10 и наслаждаться потоковой музыкой на iPhone.

## Как включить DLNA медиасервер в Windows 10

1. Нажмите кнопку «Пуск».  
2. Выберите значок «Параметры».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Настройка сервера" caption="Откройте параметры Windows" width="500" >}}

3. На экране «Параметры Windows» выберите «Сеть и Интернет».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Параметры Windows" caption="Выберите Сеть и Интернет" width="500" >}}

4. В разделе «Сеть» выберите «Центр управления сетями и общим доступом».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Центр управления сетями" caption="Откройте Центр управления сетями и общим доступом" width="500" >}}

5. На экране «Центр управления сетями и общим доступом» нажмите «Изменить дополнительные параметры общего доступа» в левом меню.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Дополнительные параметры общего доступа" caption="Изменить дополнительные параметры общего доступа" width="500" >}}

6. На экране «Дополнительные параметры общего доступа» прокрутите вниз до раздела «Все сети» и разверните его, нажав на стрелку.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Включить обнаружение" caption="Разверните параметры всех сетей" width="500" >}}

7. Нажмите «Включить потоковую передачу мультимедиа» для активации DLNA-сервера.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Включить сервер" caption="Включите сервер потоковой передачи мультимедиа" width="500" >}}

8. Дайте имя медиабиблиотеке и выберите устройства, которым разрешён доступ.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Имя медиабиблиотеки" caption="Назовите вашу DLNA медиабиблиотеку" width="500" >}}

9. Нажмите «ОК» для подтверждения. Теперь ваши личные папки — Музыка, Изображения и Видео — будут видны всем устройствам с поддержкой UPnP.

## Как отключить DLNA медиасервер в Windows 10

1. Нажмите «Пуск» и введите «services» в поле поиска.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Службы Windows" caption="Откройте Службы Windows" width="500" >}}

2. На экране «Службы» прокрутите вниз, чтобы найти «Служба общих сетевых ресурсов проигрывателя Windows Media».  
3. Дважды щёлкните по ней и установите «Тип запуска» на «Вручную».  
4. Остановите службу, нажав кнопку «Остановить».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Остановить службу DLNA" caption="Отключите службу сетевого общего доступа DLNA" width="500" >}}

## Как воспроизводить музыку с DLNA-сервера на iPhone

1. Установите бесплатное приложение **Evermusic** из App Store:  
   [Приложение Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Откройте вкладку «Подключения» и нажмите на «Доступные устройства» в разделе «Локальная сеть».

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Подключения Evermusic" caption="Evermusic: экран Подключения" width="500" >}}

3. Подождите несколько секунд, пока загрузится список устройств, и нажмите на DLNA-сервер Windows Media Player (например, «MSEDGEWIN10: My Windows Library»).

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Доступные устройства" caption="Доступные DLNA-серверы в Evermusic" width="500" >}}

4. Вы увидите список папок, доступных на медиасервере.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Папки Evermusic" caption="Просмотр общих папок с DLNA-сервера" width="500" >}}

5. Откройте любую папку с аудиофайлами.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Содержимое папки" caption="Просмотр содержимого общих DLNA-папок" width="500" >}}

6. Нажмите на любой файл, чтобы запустить аудиоплеер.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Аудиоплеер" caption="Воспроизведение аудиофайла с DLNA в Evermusic" width="500" >}}

7. Для улучшения звучания нажмите значок «Эквалайзер» рядом с индикатором громкости внизу экрана, чтобы включить эквалайзер в стиле iPod с предусилителем.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Эквалайзер" caption="Используйте встроенный эквалайзер для улучшенного воспроизведения" width="500" >}}

## Заключение

С DLNA медиасервером в Windows 10 и Evermusic на iPhone вы можете наслаждаться бесперебойной потоковой передачей музыки с компьютера на мобильное устройство. Попрощайтесь с ограничениями хранилища и наслаждайтесь музыкой по запросу!

## Часто задаваемые вопросы

{{% details title="Нужно ли устанавливать серверное ПО на Windows 10?" closed="true" %}}
Нет. Windows 10 включает встроенный DLNA медиасервер. Вам нужно лишь включить потоковую передачу мультимедиа в настройках Центра управления сетями и общим доступом. Стороннее ПО не требуется.
{{% /details %}}

{{% details title="Должен ли мой iPhone быть в той же сети Wi-Fi?" closed="true" %}}
Да. Потоковая передача DLNA работает через локальную сеть. И компьютер с Windows 10, и iPhone должны быть подключены к одной сети Wi-Fi, чтобы Evermusic мог обнаружить DLNA-сервер.
{{% /details %}}

{{% details title="Какие аудиоформаты можно транслировать через DLNA?" closed="true" %}}
DLNA-сервер Windows предоставляет общий доступ к файлам из папки Музыка независимо от формата. Evermusic поддерживает MP3, FLAC, AAC, WAV, OGG, AIFF и многие другие форматы, поэтому вы можете воспроизвести практически любой аудиофайл с сервера.
{{% /details %}}

{{% details title="Можно ли использовать Flacbox вместо Evermusic?" closed="true" %}}
Да. Flacbox также поддерживает просмотр и воспроизведение через DLNA/UPnP. Вы можете использовать любое из двух приложений для обнаружения и воспроизведения музыки с вашего DLNA-сервера Windows.
{{% /details %}}

{{% details title="Использует ли потоковая передача DLNA мобильные данные?" closed="true" %}}
Нет. DLNA работает исключительно через локальную сеть Wi-Fi. Мобильные данные не используются. Однако оба устройства должны оставаться подключёнными к одной сети во время воспроизведения.
{{% /details %}}
