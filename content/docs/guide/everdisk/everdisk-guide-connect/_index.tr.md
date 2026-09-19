---
title: "Cihazlarınızı Bağlayın"
date: 2026-08-20
description: "Everdisk kablosuz sürücünüze bağlanmak için adım adım talimatlar: akıllı bir TV'de DLNA üzerinden izleyin, dosyalarınızı herhangi bir web tarayıcısında açın, cihazınızı Finder, Windows veya Linux'ta WebDAV ya da SMB üzerinden (isteğe bağlı SMB3/AES şifrelemesiyle) bir ağ sürücüsü olarak bağlayın, dosya uygulamalarını FTP üzerinden bağlayın ve Wi-Fi olmadan bir Mac'e USB kablosu üzerinden aktarım yapın."
keywords: ["Everdisk'e bağlan", "DLNA ile TV'ye aktarma", "dosyaları tarayıcıda aç", "Finder ağ sürücüsü bağla", "WebDAV Windows Linux", "FTP dosya uygulaması", "USB kabloyla Mac aktarımı", "iPhone'u bilgisayara bağla", "iPhone ağ sürücüsü"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


[Paylaşım](/docs/guide/everdisk/everdisk-guide-sharing) ekranında **Başlat**'a dokunduğunuzda, diğer cihazlar dosyalarınıza beş farklı yolla bağlanabilir. Kullanmak istediğiniz cihaza uyan yöntemi seçin. Her durumda ihtiyacınız olan tam **adres**, Paylaşım ekranının **Nasıl Bağlanılır** bölümünde gösterilir.

> Her iki cihaz da **aynı Wi-Fi ağında** olmalıdır - ya da bir Mac için bir **USB kablosuyla** bağlı olmalıdır (son bölüme bakın).

## Bir TV'de izleyin (DLNA)

Bunu, akıllı bir TV veya medya oynatıcıda fotoğrafları, videoları ve müzikleri göstermek için kullanın.

1. **Ayarlar → Paylaşım → Bağlantılar**'da **TV ve Medya Merkezi**nin açık olduğundan emin olun (varsayılan olarak açıktır).
2. Paylaşım ekranında **Başlat**'a dokunun.
3. TV'nizde yerleşik medya oynatıcısını veya medya sunucusu uygulamasını açın (Media Player, SmartShare, AllShare veya benzeri bir ad taşıyabilir).
4. Cihazınız, medya sunucuları listesinde adıyla görünür (örneğin "Speedy-Hare"). Onu seçin.
5. Paylaşılan fotoğraflarınıza, videolarınıza ve müziklerinize göz atın ve oynatmaya başlayın. Önizleme küçük resimleri otomatik olarak görünür.

Notlar:

- DLNA parola ile korunamaz; bu nedenle bu bağlantı, açık olduğu sürece aynı Wi-Fi'daki herkese açıktır.
- Eski bir TV'de bir video oynatılamıyorsa, **Ayarlar → Paylaşım → Videolar**'da video kalitesini düşürün; böylece Everdisk onu daha uyumlu bir biçime dönüştürür.

## Bir web tarayıcısında açın (HTTP)

Bunu, web tarayıcısı olan herkese dosya vermek için kullanın - kurulacak uygulama yok.

1. **Ayarlar → Paylaşım → Bağlantılar**'da **Tarayıcı**nın açık olduğundan emin olun.
2. **Başlat**'a dokunun.
3. Paylaşım ekranında **Tarayıcı** adresini kopyalayın (ya da QR kodunu gösterin).
4. Diğer telefonda, tablette veya bilgisayarda herhangi bir web tarayıcısı (Safari, Chrome, Edge, Firefox) açın ve o adresi yazın.
5. Sayfa, paylaşılan dosyalarınızla açılır.

Tarayıcıda karşı taraf şunları yapabilir:

- **Liste** ve **ızgara** görünümleri arasında geçiş yapabilir ve ada, tarihe veya boyuta göre sıralayabilir.
- Fotoğraflar, videolar, PDF'ler ve müzik kapak resimleri için gerçek **küçük resimler** görebilir.
- Bir fotoğrafı, kaydırma, sıkıştırarak yakınlaştırma ve slayt gösterisi içeren tam ekran bir **galeri**de açabilir.
- Müziği; kuyruk, karıştırma ve tekrar özellikleri olan yerleşik bir **oynatıcı**da çalabilir.
- Herhangi bir dosyayı **indirebilir** ya da tüm bir klasörü (veya seçili birkaç öğeyi) tek bir **Archive.zip** olarak indirebilir.
- Dosyaları cihazınıza geri **yükleyebilir** - yalnızca **Dosya Düzenleme**yi açtıysanız (bkz. [Erişim ve Gizlilik](/docs/guide/everdisk/everdisk-guide-access)).

## Ağ sürücüsü olarak kullanın (WebDAV)

Bunu, cihazınızı bir Mac, Windows PC veya Linux makinede sıradan bir disk gibi göstermek için kullanın; böylece dosyaları her iki yönde de sürükleyebilirsiniz.

**Bir Mac'te (Finder)**

1. **Ayarlar → Paylaşım → Bağlantılar**'da **Bilgisayar**ın açık olduğundan emin olun.
2. **Başlat**'a dokunun ve **Bilgisayar (WebDAV)** adresini not edin.
3. Finder'da **Git → Sunucuya Bağlan**'ı seçin (ya da **⌘K**'ye basın).
4. WebDAV adresini gösterildiği gibi tam olarak yazın ve **Bağlan**'a tıklayın.
5. Bir tane belirlediyseniz giriş ve parolayı girin, aksi halde konuk olarak bağlanın.
6. Cihazınız başka herhangi bir ağ sürücüsü gibi açılır. Dosyaları içeri ya da dışarı sürükleyin.

**Windows'ta**

1. **Dosya Gezgini**'ni açın, **Bu Bilgisayar**'a sağ tıklayın ve **Ağ konumu ekle**'yi seçin (ya da bir ağ sürücüsü eşleyin).
2. Everdisk'te gösterilen WebDAV adresini girin.
3. Bir tane belirlediyseniz giriş ve parolayı girin.

**Linux'ta**

1. Dosya yöneticinizi açın ve **Sunucuya Bağlan**'ı seçin (ya da `davs://` / `dav://` kullanın).
2. Everdisk'te gösterilen WebDAV adresini girin.

Bağlantının salt okunur mu yoksa çift yönlü mü olacağı **Dosya Düzenleme** ayarına bağlıdır. Açıkken cihazınıza dosya kopyalayabilir, yeniden adlandırabilir ya da silebilirsiniz; kapalıyken sürücü salt okunurdur.

## SMB üzerinden bağlanın (şifreli ağ sürücüsü)

SMB, Mac, Windows ve Linux için, bu sistemlerde zaten bulunan dosya paylaşımı üzerine kurulu bir ağ sürücüsüdür; böylece cihazınız normal bir ağ sürücüsü olarak görünür - ve şifreleyebileceğiniz tek bağlantıdır.

1. **Ayarlar → Paylaşım → Bağlantılar**'da **Bilgisayar (Gelişmiş)** (SMB bağlantısı)'nın açık olduğundan emin olun.
2. **Başlat**'a dokunun ve `smb://192.168.1.20:4455/Share` gibi görünen **SMB** adresini not edin.
3. Bilgisayarınızdan bağlanın:
   - **Mac:** cihazınız **Konumlar** (Ağ) altında **Finder kenar çubuğunda** kendiliğinden görünür - sadece tıklayın ve oturum açın. Bunun yerine elle bağlanmak için **Git → Sunucuya Bağlan** (**⌘K**)'yi seçin ve adresi girin.
   - **Windows:** **Dosya Gezgini**'ni açın, **Bu Bilgisayar**'a sağ tıklayın ve **Ağ sürücüsü eşle**'yi seçin, ardından Paylaşım ekranındaki ana bilgisayar ve paylaşım adını kullanarak `\\<address>\Share` girin (veya `smb://` adresini adres çubuğuna yazın).
   - **Linux:** dosya yöneticinizde **Sunucuya Bağlan**'ı seçin ve adresi girin.
4. Bir tane belirlediyseniz giriş ve parolayı girin, aksi halde konuk olarak bağlanın.
5. Paylaşım **Share** olarak adlandırılır. **Dosya Düzenleme** açıkken dosyaları iki yönde kopyalayabilirsiniz; kapalıyken salt okunurdur.

**Şifrelemeyi açın (güvenilmeyen Wi-Fi'de önerilir)**

SMB, şifrelenebilen tek Everdisk bağlantısıdır. Her aktarımı **SMB3 şifrelemesiyle (AES)** korumak için:

1. **Ayarlar → Paylaşım → Erişim**'de bir **Giriş** ve **Parola** ayarlayın - şifreli bağlantılar anonim olamaz.
2. **Ayarlar → Paylaşım**'da **SMB şifrelemesi iste**'yi açın.
3. Değişikliğin etkili olması için paylaşımı **Durdurup yeniden Başlatın**.

İstemciniz SMB3'ü desteklemelidir - modern bir Mac'teki Finder ya da **Windows 10 ve sonrası**. SMB şifrelemesi bir Premium özelliğidir.

## Bir dosya uygulaması bağlayın (FTP)

Bunu, FTP konuşan dosya yöneticisi ve aktarım uygulamaları için (örneğin bilgisayarda FileZilla veya Cyberduck) kullanın.

1. **Ayarlar → Paylaşım → Bağlantılar**'da **Diğer Uygulamalar ve Cihazlar**ın açık olduğundan emin olun.
2. **Başlat**'a dokunun ve **FTP** adresini not edin.
3. FTP uygulamanızda, o adresi kullanarak yeni bir bağlantı ekleyin.
4. Bir tane belirlediyseniz giriş ve parolayı girin, ya da anonim erişim için boş bırakın.

## Bir USB kablosu üzerinden aktarım (Mac, Wi-Fi gerekmez)

Bunu, Wi-Fi olmadığında ya da en hızlı ve en özel aktarımı istediğinizde kullanın. Yalnızca bir **Mac** ile çalışır.

1. iPhone veya iPad'inizi normal şarj kablosuyla Mac'e takın.
2. Cihazda sorulursa **Bu Bilgisayara Güven**'e dokunun.
3. Everdisk'te **Başlat**'a dokunun. Bir **Hızlı Bağlantı Kullanılabilir** notu görünür ve Paylaşım ekranı, `.local` ile biten, **Kablo Bağlantısı** rozetli ekstra bir adres gösterir.
4. Mac'te Finder → **Git → Sunucuya Bağlan** (**⌘K**)'yi açın ve o `.local` adresini girin (hem Tarayıcı hem de Bilgisayar bağlantıları için çalışır).
5. Cihazınız kablo üzerinden açılır - Wi-Fi'dan daha hızlı ve veri asla yönlendiriciye ya da internete dokunmaz.

Notlar:

- Bir IP adresi değil, **`.local` adı**nı kullanın (IP adresleri yalnızca Wi-Fi üzerinden çalışır) ve asla `localhost` kullanmayın.
- Kablo yolu **yalnızca Mac** içindir. Windows PC'ler ve Android cihazlar Wi-Fi kullanmalıdır.
- Ayrıca Mac'te Finder'ı ya da Windows'ta Apple Devices uygulamasını (veya iTunes'u) kullanarak, standart iOS dosya paylaşımı üzerinden dosyaları Everdisk klasörüne sürükleyebilirsiniz.

## Sonraki adımlar

- [Erişim ve Gizlilik](/docs/guide/everdisk/everdisk-guide-access) - bir parola ekleyin, yüklemelere izin verin, bir cihazı engelleyin.
- [Fotoğraflar, Müzik ve Video](/docs/guide/everdisk/everdisk-guide-media) - tüm kitaplığınızı paylaşın ve kaliteyi ayarlayın.
- [Sunuculara Bağlanın](/docs/guide/everdisk/everdisk-guide-devices) - Everdisk'ten diğer cihazlara ulaşın.
