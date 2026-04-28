---
title: "Как подключить внутреннее хранилище Bluesound VAULT из Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Узнайте, как получить доступ к внутреннему жёсткому диску Bluesound VAULT из Evermusic, Flacbox и Evertag с помощью протокола SMB для управления, редактирования и воспроизведения аудиофайлов."
keywords: ["bluesound vault", "подключение smb хранилища", "evermusic smb", "flacbox vault", "evertag smb", "nas хранилище музыка", "внутренний диск vault"]
tags: ["evermusic", "подключение", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Кратко:** Подключитесь к внутреннему хранилищу Bluesound VAULT через SMB с помощью Evermusic, Flacbox или Evertag. Найдите IP-адрес VAULT в приложении BluOS, введите его как SMB-подключение с гостевым доступом и начните воспроизводить или управлять своими музыкальными файлами.

Bluesound VAULT имеет внутренний жёсткий диск и работает как сетевое хранилище (NAS). Доступ к внутреннему жёсткому диску VAULT позволяет добавлять/удалять файлы, редактировать теги метаданных из наших приложений Evermusic, Flacbox, Evertag.

**Ниже приведены шаги для доступа к внутреннему жёсткому диску VAULT:**

1. В приложении BluOS выберите **Справка > Диагностика**.

2. На странице **Диагностика** получите **IP-адрес** VAULT. Этот **IP-адрес** будет использоваться в следующих шагах.

3. Откройте Evermusic, Flacbox или Evertag.

   ![Приложения Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Откройте экран «Подключения» и выберите пункт меню «Подключить облачный сервис».

   ![Экран Подключения Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Выберите облачный сервис «SMB».

   ![Экран Подключить облачный сервис Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. На «Экране настройки SMB» введите URL в следующем формате:

   ```
   SMB://<<VAULT-IP>>
   ```

   Замените `<<VAULT-IP>>` на **IP-адрес**, полученный на Шаге 2.

   **Примечание:** Оставьте поля Логин и Пароль пустыми, так как хранилище VAULT поддерживает гостевой режим (GUEST).

   ![Экран SMB-подключения Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Нажмите кнопку «Войти», чтобы сохранить настройки.

8. Откройте подключённое облачное хранилище, перейдите в папку с аудиофайлами и нажмите на любой файл, чтобы запустить аудиоплеер.

   ![Экран открытого SMB-сервера Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Вы также можете редактировать файлы с помощью встроенного файлового менеджера.

   ![Экран Файлового менеджера Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

С помощью этих простых шагов вы можете легко получить доступ к внутреннему жёсткому диску Bluesound VAULT и управлять своей музыкальной библиотекой с помощью Evermusic, Flacbox или Evertag.

## Часто задаваемые вопросы

{{% details title="Нужны ли мне имя пользователя и пароль для подключения к Bluesound VAULT?" closed="true" %}}
Нет. Bluesound VAULT поддерживает гостевой (анонимный) доступ через SMB. Оставьте поля Логин и Пароль пустыми при настройке подключения.
{{% /details %}}

{{% details title="Могу ли я редактировать музыкальные теги на Bluesound VAULT?" closed="true" %}}
Да. С помощью Evertag вы можете редактировать теги метаданных (название, исполнитель, альбом и т.д.) аудиофайлов, хранящихся непосредственно на внутреннем жёстком диске VAULT.
{{% /details %}}

{{% details title="Какие протоколы поддерживает Bluesound VAULT?" closed="true" %}}
Bluesound VAULT предоставляет доступ к своему внутреннему хранилищу через SMB (Server Message Block). Evermusic, Flacbox и Evertag поддерживают SMB-подключения, что делает подключение простым.
{{% /details %}}

{{% details title="Могу ли я транслировать музыку с VAULT без копирования файлов на iPhone?" closed="true" %}}
Да. После подключения через SMB вы можете транслировать аудиофайлы напрямую с внутреннего диска VAULT без копирования их на ваше устройство.
{{% /details %}}
