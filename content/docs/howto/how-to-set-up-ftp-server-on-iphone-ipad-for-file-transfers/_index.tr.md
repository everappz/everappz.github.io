---
title: "iPhone ve iPad'de Dosya Aktarımları için FTP Sunucusu Nasıl Kurulur"
description: "Everdisk ile iPhone veya iPad cihazınızı bir FTP sunucusuna dönüştürün ve Wi-Fi üzerinden bir Mac'ten, Windows PC'den, Linux'tan, Android'den, FileZilla gibi bir FTP uygulamasından veya başka bir iPhone'dan dosya aktarın. Eksiksiz kurulum, ftp adresi ve bağlantı noktası, konuk erişimi ve her cihaz için adım adım bağlantı."
date: 2026-09-19
tags: ["everdisk", "ftp", "dosya aktarımı", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP sunucusu iPhone", "FTP sunucusu iPad", "iPhone'da FTP nasıl kurulur", "iphone ftp sunucusu uygulaması", "FileZilla'yı iPhone'a bağlama", "Cyberduck iPhone FTP", "iPhone FTP dosya aktarımı", "ftp iphone'dan bilgisayara", "ftp iphone'dan iphone'a", "Windows'tan iPhone FTP'ye bağlanma", "ftp adresi bağlantı noktası iphone", "anonim ftp iphone", "iphone ftp dosya paylaşımı", "kamera nas için iphone ftp"]
readingTime: 9
---

{{< author-byline >}}

FTP, dosya aktarımının eski güvenilir aracıdır. Onlarca yıldır ortalıktadır ve bu kadar kullanışlı olmasının nedeni tam da budur: bir sunucuyla konuşabilen hemen hemen her şey onu anlar. Kameralar, akıllı TV'ler, yönlendiriciler, ağ sürücüleri, otomasyon araçları ve her masaüstü FTP uygulaması FTP konuşur. [Everdisk](/products/everdisk) ile iPhone veya iPad cihazınızda bir FTP sunucusu çalıştırabilirsiniz; böylece telefon, bu cihazların ve uygulamaların bağlanıp dosya taşıyabileceği bir yer olur.

Diğer seçenekler uymadığında FTP'ye başvurun, örneğin daha eski bir cihaz veya yalnızca FTP üzerinden bağlanmayı bilen bir uygulama için. Bu kılavuz, kurulumu ve bir Mac'ten, Windows'tan, bir FTP uygulamasından, Linux'tan, Android'den ve ikinci bir iPhone'dan nasıl bağlanılacağını kapsar.

## İhtiyacınız olanlar

- [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) yüklü bir iPhone veya iPad.
- **Aynı Wi-Fi ağında** bir bilgisayar, uygulama veya cihaz.
- Paylaşmak istediğiniz dosyalar, Everdisk Belgeler klasöründe veya eklediğiniz klasörlerde.

## Everdisk'te FTP sunucusunu kurun

### Adım 1: Ne paylaşacağınızı seçin ve erişimi ayarlayın

Everdisk'i açın, **Paylaşım** sekmesine gidin ve **Ne Paylaşılacak**'a dokunun. Belgeler klasörü varsayılan olarak paylaşılır. **Klasör Ekle** ve **Dosya Ekle** ile daha fazlasını ekleyin.

**Ayarlar**'ı, ardından **Paylaşım**'ı, ardından **Erişim**'i açın. İnsanların yüklemesini, yeniden adlandırmasını ve silmesini istiyorsanız **Dosya Düzenleme**'yi açın ya da yalnızca indirmelere izin vermek için kapatın. Bir oturum açma istiyorsanız bir **Kullanıcı Adı** ve **Parola** ayarlayın veya herkesin konuk olarak bağlanabilmesi için onları boş bırakın.

### Adım 2: FTP sunucusunu açın

**Ayarlar**'a, ardından **Paylaşım**'a, ardından **Bağlantılar**'a gidin ve **Diğer uygulamalar ve cihazlar**'ı açın. Bu, FTP sunucusudur (FTP etiketini taşır).

### Adım 3: Paylaşımı başlatın ve adresi not edin

**Paylaşım** sekmesine dönün ve **Başlat**'a dokunun. **Nasıl Bağlanılır** bölümü FTP adresini gösterir. Şuna benzer:

```
ftp://192.168.1.20:2121
```

İki nokta üst üsteden sonraki sayı **bağlantı noktasıdır** ve varsayılan olarak **2121**'dir. İlk kısım, iPhone'unuzun Wi-Fi'deki adresidir; bu nedenle sizinki farklı olacaktır. Bir cihaz bağlıyken Everdisk'i ekranda açık tutun.

## Bir Mac'ten bağlanın

1. **Finder**'ı açın, **Git**'i, ardından **Sunucuya Bağlan**'ı seçin (veya **Command ve K**'ye basın).
2. Everdisk'te gösterilen FTP adresini yazın, örneğin `ftp://192.168.1.20:2121`.
3. **Bağlan**'a tıklayın, ardından **Konuk**'u seçin veya **Kullanıcı Adı** ve **Parola**'nızı girin.

Finder, FTP paylaşımını bağlar; böylece göz atabilir ve dosyaları Mac'inize kopyalayabilirsiniz. Finder'ın FTP'yi salt okunur olarak açtığını unutmayın. Bir Mac'ten yüklemek istediğinizde aşağıda açıklandığı gibi bir FTP uygulaması kullanın.

## Windows'tan bağlanın

1. **Dosya Gezgini**'ni açın ve üstteki adres çubuğuna tıklayın.
2. Everdisk'teki FTP adresini yazın, örneğin `ftp://192.168.1.20:2121`, ve **Enter**'a basın.
3. Ayarladıysanız **Kullanıcı Adı** ve **Parola**'nızı girin veya konuk olarak devam edin.

Paylaşılan dosyalar pencerede görünür ve onları PC'nize kopyalayabilirsiniz.

## Bir FTP uygulamasıyla bağlanın (FileZilla, Cyberduck)

Yüklemeler ve tam kontrol için bir FTP uygulaması en iyi araçtır. **FileZilla** ve **Cyberduck** ücretsizdir ve Windows, Mac ve Linux'ta çalışır.

1. Uygulamayı açın ve yeni bir bağlantı oluşturun.
2. **Host**'u iPhone'unuzun Wi-Fi adresine ve **Port**'u **2121**'e ayarlayın.
3. Oturum açma için **Kullanıcı Adı** ve **Parola**'nızı girin ya da birini ayarlamadıysanız **Anonymous**'u seçin.
4. Bağlanın ve dosyaları her iki yönde sürükleyin (yüklemeler için Dosya Düzenleme açık olmalıdır).

## Linux'tan bağlanın

1. Dosya yöneticinizi açın ve **Connect to Server** veya **Other Locations**'ı seçin.
2. Adresi girin, örneğin `ftp://192.168.1.20:2121`.
3. Konuk olarak veya oturum açma bilgilerinizle bağlanın.

Ayrıca terminalden herhangi bir Linux FTP istemcisini, aynı ana bilgisayara ve 2121 bağlantı noktasına yönlendirerek kullanabilirsiniz.

## Android'den bağlanın

Android'in sistem düzeyinde bir FTP tarayıcısı yoktur; bu nedenle bir uygulama kullanın:

1. **AndFTP**, **FTPCafe** gibi bir FTP istemcisi ya da **Solid Explorer** gibi FTP desteği olan bir dosya yöneticisi yükleyin.
2. Ana bilgisayar, **2121 bağlantı noktası** ve oturum açma bilgileriniz veya Anonymous ile bir bağlantı ekleyin.
3. Göz atın ve aktarın.

## Başka bir iPhone veya iPad'den bağlanın

iOS Dosyalar uygulaması bir FTP istemcisi içermez; bu nedenle ikinci cihazda bunlardan birini kullanın:

- **Everdisk'in kendi Cihazlar sekmesi.** Everdisk'i açın, **Cihazlar**'a gidin, **Yeni Bağlantı**'ya dokunun, **FTP**'yi seçin ve adresi girin, örneğin `ftp://192.168.1.20:2121`. Bu en basit yoldur.
- **Özel bir FTP uygulaması** iOS için, aynı ana bilgisayar, 2121 bağlantı noktası ve oturum açma bilgilerini kullanarak.

## Diğer donanımları bağlayın: kameralar, TV'ler, yönlendiriciler ve NAS

FTP'nin parladığı yer burasıdır. Birçok cihazın, dosya gönderebilen veya alabilen yerleşik bir FTP istemcisi vardır:

- Fotoğrafları FTP üzerinden yükleyen **kameralar** onları doğrudan iPhone'unuza gönderebilir.
- FTP'yi destekleyen **akıllı TV'ler, yönlendiriciler, NAS kutuları ve otomasyon araçları** aynı şekilde bağlanabilir.

Onları, Everdisk'te gösterilen adresi kullanarak iPhone'unuzun Wi-Fi adresine, **2121** bağlantı noktasına ve oturum açma bilgilerinize (veya Anonymous) yönlendirin.

## Salt okunur veya okuma ve yazma

Ayarlar, Paylaşım, Erişim'deki **Dosya Düzenleme** anahtarı bunu kontrol eder. Açık, insanların yükleyebileceği, yeniden adlandırabileceği ve silebileceği anlamına gelir. Kapalı, yalnızca indirebilecekleri anlamına gelir. Dosyaları verirken ve telefonunuzda hiçbir şeyin değiştirilmesini istemediğinizde salt okunuru seçin.

## İnsanların bunu gerçek hayatta kullanma yolları

- **FileZilla'yı iPhone'unuza bağlayın** ve bir grup dosyayı tek seferde telefona gönderin.
- **Yalnızca FTP konuşan eski bir uygulamanın veya cihazın** başka hiçbir şey bağlanamadığında dosyalarınıza ulaşmasına izin verin.
- **FTP üzerinden yükleme yapan bir kameradan fotoğraf alın.**
- **Bir iPhone ile bir iPad arasında dosya taşıyın**, alıcı cihazda Everdisk'in Cihazlar sekmesini kullanarak.

## Birkaç ipucu

- Bir cihaz bağlıyken Everdisk'i açık tutun, çünkü iOS bir süre sonra arka plan uygulamalarını duraklatır.
- Bir Mac'ten yüklemek için Finder yerine FileZilla veya Cyberduck kullanın, çünkü Finder FTP'yi salt okunur olarak açar.
- En geniş uyumluluk için oturum açmayı boş bırakın, ardından çoğu FTP istemcisinin sunduğu Anonymous olarak bağlanın.
- FTP trafiğini şifrelemez. Güvenmediğiniz bir ağda bunun yerine [şifrelemeli SMB sunucusunu](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) kullanın.

## Sıkça Sorulan Sorular

{{% details title="iPhone'um için FTP adresi ve bağlantı noktası nedir?" closed="true" %}}
Paylaşımı başlattıktan sonra Everdisk adresi Paylaşım ekranında gösterir. ftp://192.168.1.20:2121 gibi görünür. 2121, Everdisk'in FTP için kullandığı bağlantı noktasıdır ve ilk kısım iPhone'unuzun Wi-Fi'deki adresidir; bu nedenle sizinki farklı olacaktır.
{{% /details %}}

{{% details title="FileZilla veya Cyberduck'ı iPhone'uma nasıl bağlarım?" closed="true" %}}
Uygulamayı açın ve yeni bir bağlantı oluşturun. Host'u iPhone'unuzun Wi-Fi adresine ve Port'u 2121'e ayarlayın. Kullanıcı Adı ve Parola'nızı girin ya da Everdisk'te birini ayarlamadıysanız Anonymous'u seçin. Bağlanın; Dosya Düzenleme açıkken dosyaları her iki yönde sürükleyebilirsiniz.
{{% /details %}}

{{% details title="iPhone FTP'me Windows'tan bağlanabilir miyim?" closed="true" %}}
Evet. Dosya Gezgini'ni açın, adres çubuğuna tıklayın, Everdisk'teki FTP adresini yazın (örneğin ftp://192.168.1.20:2121) ve Enter'a basın. Ayarladıysanız oturum açma bilgilerinizi girin veya konuk olarak devam edin. Yüklemeler ve daha fazla kontrol için bunun yerine FileZilla gibi bir FTP uygulaması kullanın.
{{% /details %}}

{{% details title="FTP için bir oturum açmaya ihtiyacım var mı?" closed="true" %}}
Hayır, oturum açma isteğe bağlıdır. Ayarlar, Paylaşım, Erişim'de Kullanıcı Adı ve Parola'yı boş bırakın ve çoğu FTP istemcisinin sunduğu Anonymous olarak bağlanın. Bağlantıların önce oturum açmasını istiyorsanız bir oturum açma ayarlayın.
{{% /details %}}

{{% details title="FTP üzerinden neden yalnızca indirebiliyorum ama yükleyemiyorum?" closed="true" %}}
İki neden yaygındır. İlk olarak, yüklemelere, yeniden adlandırmalara ve silmelere izin vermek için Ayarlar, Paylaşım, Erişim'deki Dosya Düzenleme anahtarı açık olmalıdır. İkinci olarak, Mac Finder FTP'yi salt okunur olarak açar; bu nedenle yüklemek istediğinizde FileZilla veya Cyberduck gibi bir FTP uygulaması kullanın.
{{% /details %}}

{{% details title="İki iPhone arasında FTP kullanabilir miyim?" closed="true" %}}
Evet. İlk iPhone'da FTP sunucusunu başlatın. İkincide Everdisk'i açın, Cihazlar sekmesine gidin, Yeni Bağlantı'ya dokunun, FTP'yi seçin ve ilk telefonda gösterilen adresi girin. iOS için özel bir FTP uygulaması da çalışır, çünkü iOS Dosyalar uygulaması bir FTP istemcisi içermez.
{{% /details %}}

{{% details title="FTP güvenli mi?" closed="true" %}}
Düz FTP trafiğini şifrelemez; bu nedenle onu ev Wi-Fi'niz gibi güvendiğiniz ağlar için bir araç olarak görün. Kontrol etmediğiniz bir ağda, her aktarımı koruyan SMB şifrelemesi iste'nin açık olduğu SMB sunucusunu kullanın.
{{% /details %}}

{{% details title="FTP üzerinden hangi cihazlar bağlanabilir?" closed="true" %}}
FTP istemcisi olan hemen hemen her şey. Buna Mac, Windows ve Linux bilgisayarları, FileZilla ve Cyberduck gibi FTP uygulamaları, Android dosya yöneticileri ve kameralar, akıllı TV'ler, yönlendiriciler, NAS kutuları ve otomasyon araçları gibi donanımlar dahildir. Bu geniş erişim, FTP'yi seçmenin ana nedenidir.
{{% /details %}}

{{% details title="FTP bağlantım neden düştü?" closed="true" %}}
iPhone'unuz sunucudur ve iOS çok uzun süre arka planda kalan uygulamaları duraklatır. Bir cihaz bağlıyken Everdisk'i ekranda açık tutun ve uzun aktarımlar için güce takın. Ayrıca her iki cihazın da hâlâ aynı Wi-Fi'de olduğundan emin olun.
{{% /details %}}

{{% details title="Everdisk ücretsiz mi?" closed="true" %}}
Evet, Everdisk ücretsiz indirilir ve FTP sunucusu dahildir. İsteğe bağlı, tek seferlik Premium satın alma, özel bağlantı noktaları ve fotoğraf ve video dönüştürme gibi ekstralar ekler. FTP'yi ödeme yapmadan kurabilir ve dosya aktarabilirsiniz.
{{% /details %}}

Denemeye hazır mısınız? [Everdisk'i App Store'dan indirin](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) ve birkaç dakika içinde ilk FTP istemcinizi bağlayın. Sorularınız veya geri bildiriminiz mi var? Bize **support@everappz.com** adresinden e-posta gönderin.
