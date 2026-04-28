---
title: "Як підключити внутрішнє сховище Bluesound VAULT з Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Дізнайтеся, як отримати доступ до внутрішнього жорсткого диска Bluesound VAULT з Evermusic, Flacbox та Evertag за допомогою протоколу SMB для керування, редагування та відтворення аудіофайлів."
keywords: ["bluesound vault", "підключення сховища smb", "evermusic smb", "flacbox vault", "evertag smb", "сховище nas музика", "внутрішній диск vault"]
tags: ["evermusic", "підключення", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Коротко:** Підключіться до внутрішнього сховища Bluesound VAULT через SMB за допомогою Evermusic, Flacbox або Evertag. Знайдіть IP-адресу VAULT у додатку BluOS, введіть її як SMB-з'єднання з гостьовим доступом і почніть відтворювати або керувати своїми музичними файлами.

Bluesound VAULT має внутрішній жорсткий диск і працює як мережеве сховище (NAS). Доступ до внутрішнього жорсткого диска VAULT дозволяє додавати/видаляти файли, редагувати теги метаданих з наших додатків Evermusic, Flacbox, Evertag.

**Нижче наведені кроки для доступу до внутрішнього жорсткого диска VAULT:**

1. У додатку BluOS виберіть **Довідка > Діагностика**.

2. На сторінці **Діагностика** отримайте **IP-адресу** VAULT. Ця **IP-адреса** буде використовуватися в наступних кроках.

3. Відкрийте Evermusic, Flacbox або Evertag.

   ![Додатки Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Відкрийте екран «З'єднання» та виберіть пункт меню «Підключити хмарний сервіс».

   ![Екран З'єднання Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Виберіть хмарний сервіс «SMB».

   ![Екран Підключити хмарний сервіс Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. На «Екрані налаштування SMB» введіть URL у наступному форматі:

   ```
   SMB://<<VAULT-IP>>
   ```

   Замініть `<<VAULT-IP>>` на **IP-адресу**, отриману на Кроці 2.

   **Примітка:** Залиште поля Логін та Пароль порожніми, оскільки сховище VAULT підтримує гостьовий режим (GUEST).

   ![Екран SMB-з'єднання Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Натисніть кнопку «Увійти», щоб зберегти налаштування.

8. Відкрийте підключене хмарне сховище, перейдіть до папки з аудіофайлами та натисніть на будь-який файл, щоб запустити аудіоплеєр.

   ![Екран відкритого SMB-сервера Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Ви також можете редагувати файли за допомогою вбудованого файлового менеджера.

   ![Екран Файлового менеджера Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

За допомогою цих простих кроків ви можете легко отримати доступ до внутрішнього жорсткого диска Bluesound VAULT та керувати своєю музичною бібліотекою за допомогою Evermusic, Flacbox або Evertag.

## Поширені запитання

{{% details title="Чи потрібні мені ім'я користувача та пароль для підключення до Bluesound VAULT?" closed="true" %}}
Ні. Bluesound VAULT підтримує гостьовий (анонімний) доступ через SMB. Залиште поля Логін та Пароль порожніми при налаштуванні з'єднання.
{{% /details %}}

{{% details title="Чи можу я редагувати музичні теги на Bluesound VAULT?" closed="true" %}}
Так. За допомогою Evertag ви можете редагувати теги метаданих (назва, виконавець, альбом тощо) аудіофайлів, збережених безпосередньо на внутрішньому жорсткому диску VAULT.
{{% /details %}}

{{% details title="Які протоколи підтримує Bluesound VAULT?" closed="true" %}}
Bluesound VAULT надає доступ до свого внутрішнього сховища через SMB (Server Message Block). Evermusic, Flacbox та Evertag підтримують SMB-з'єднання, що робить підключення простим.
{{% /details %}}

{{% details title="Чи можу я транслювати музику з VAULT без копіювання файлів на iPhone?" closed="true" %}}
Так. Після підключення через SMB ви можете транслювати аудіофайли безпосередньо з внутрішнього диска VAULT без копіювання їх на ваш пристрій.
{{% /details %}}
