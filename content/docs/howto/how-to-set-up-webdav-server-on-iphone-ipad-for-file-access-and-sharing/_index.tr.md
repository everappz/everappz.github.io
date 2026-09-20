---
title: "iPhone ve iPad'de Dosya Erişimi ve Paylaşımı için WebDAV Sunucusu Nasıl Kurulur"
description: "Everdisk ile iPhone veya iPad cihazınızı bir WebDAV sunucusuna dönüştürün ve Wi-Fi üzerinden Mac Finder'da, Windows Dosya Gezgini'nde, Linux'ta, Android'de veya başka bir iPhone'da ağ sürücüsü olarak bağlayın. Eksiksiz kurulum, WebDAV adresi ve bağlantı noktası ve her cihaz için adım adım bağlantı."
date: 2026-09-19
tags: ["everdisk", "webdav", "ağ sürücüsü", "dosya paylaşımı", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV sunucusu iPhone", "WebDAV sunucusu iPad", "iPhone'da WebDAV nasıl kurulur", "iPhone'u ağ sürücüsü olarak bağlama", "iPhone WebDAV Mac Finder bağlantısı", "WebDAV Windows Dosya Gezgini iPhone", "iphone ağ sürücüsü Windows", "WebDAV Linux iPhone", "iPhone dosyalarına bilgisayardan erişme", "webdav iphone'dan iphone'a", "iPhone WebDAV dosya paylaşımı", "iphone ağ sürücüsü eşleme", "iphone webdav dosya aktarımı", "webdav adresi bağlantı noktası iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV, bir klasörü, bir bilgisayarın normal dosya yöneticisinde açabileceği bir ağ sürücüsüne dönüştürür. Tarayıcınızın kullandığı aynı web protokolü üzerinden çalışır; bu yüzden özel sürücüler olmadan Mac, Windows ve Linux arasında iyi taşınır. [Everdisk](/products/everdisk) ile iPhone veya iPad cihazınızda bir WebDAV sunucusu çalıştırabilirsiniz; böylece telefon, neredeyse her bilgisayardan göz atabileceğiniz, kopyalayabileceğiniz ve içine kopyalayabileceğiniz bir sürücü olarak görünür.

WebDAV, Windows söz konusu olduğunda en iyi tercihtir, çünkü Windows Dosya Gezgini ona sorunsuz bağlanır. Bu kılavuz, kurulumu ve bir Mac'ten, Windows'tan, Linux'tan, Android'den ve ikinci bir iPhone'dan nasıl bağlanılacağını kapsar.

## İhtiyacınız olanlar

- [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) yüklü bir iPhone veya iPad.
- **Aynı Wi-Fi ağında** bir bilgisayar veya başka bir cihaz.
- Paylaşmak istediğiniz dosyalar, Everdisk Belgeler klasöründe veya eklediğiniz klasörlerde.

## Everdisk'te WebDAV sunucusunu kurun

### Adım 1: Ne paylaşacağınızı seçin ve erişimi ayarlayın

Everdisk'i açın, **Paylaşım** sekmesine gidin ve **Ne Paylaşılacak**'a dokunun. Belgeler klasörü varsayılan olarak paylaşılır. **Klasör Ekle** ve **Dosya Ekle** ile daha fazlasını ekleyin.

**Ayarlar**'ı, ardından **Paylaşım**'ı, ardından **Erişim**'i açın. Bağlı bilgisayarların telefonunuza dosya kopyalamasını ve yeniden adlandırmasını veya silmesini istiyorsanız **Dosya Düzenleme**'yi açın ya da salt okunur bir sürücü için kapatın. Bir oturum açma istiyorsanız burada bir **Kullanıcı Adı** ve **Parola** ayarlayın veya konuk erişimi için onları boş bırakın.

### Adım 2: WebDAV sunucusunu açın

**Ayarlar**'a, ardından **Paylaşım**'a, ardından **Bağlantılar**'a gidin ve **Bilgisayar**'ı açın. Bu, WebDAV sunucusudur (WebDAV etiketini taşır).

### Adım 3: Paylaşımı başlatın ve adresi not edin

**Paylaşım** sekmesine dönün ve **Başlat**'a dokunun. **Nasıl Bağlanılır** bölümü WebDAV adresini gösterir. Şuna benzer:

```
http://192.168.1.20:8080
```

İki nokta üst üsteden sonraki sayı **bağlantı noktasıdır** ve varsayılan olarak **8080**'dir. İlk kısım, iPhone'unuzun Wi-Fi'deki adresidir; bu nedenle sizinki farklı olacaktır. Bir cihaz bağlıyken Everdisk'i ekranda açık tutun.

## Bir Mac'ten bağlanın

1. **Finder**'ı açın, **Git**'i, ardından **Sunucuya Bağlan**'ı seçin (veya **Command ve K**'ye basın).
2. Everdisk'te gösterilen WebDAV adresini yazın, örneğin `http://192.168.1.20:8080`.
3. **Bağlan**'a tıklayın, ardından **Konuk**'u seçin veya **Kullanıcı Adı** ve **Parola**'nızı girin.

iPhone'unuz bir Finder penceresinde açılır ve normal bir klasör gibi davranır. Dosya Düzenleme açıksa dosyaları her iki yönde kopyalayın.

## Windows'tan bağlanın

Windows'ta yerleşik bir WebDAV istemcisi vardır; bu nedenle bu, Dosya Gezgini'nden çalışır.

1. **Dosya Gezgini**'ni açın, kenar çubuğunda **Bu Bilgisayar**'a sağ tıklayın ve **Ağ konumu ekle**'yi seçin (**Ağ sürücüsü eşle**'yi de kullanabilirsiniz).
2. Adres sorulduğunda, Everdisk'teki aynı WebDAV adresini yazın, örneğin `http://192.168.1.20:8080`, ardından **İleri**'ye tıklayın.
3. Ayarladıysanız **Kullanıcı Adı** ve **Parola**'nızı girin.

Cihaz daha sonra Bu Bilgisayar altında, açabileceğiniz ve dosya kopyalayabileceğiniz bir ağ konumu olarak görünür. Windows ilk seferinde bağlanmayı reddederse, **WebClient** hizmetinin çalıştığından emin olun (Başlat menüsünde Hizmetler'i arayın, WebClient'i bulun ve başlaması için ayarlayın), ardından yeniden deneyin.

## Linux'tan bağlanın

1. Dosya yöneticinizi açın ve **Connect to Server** veya **Other Locations**'ı seçin.
2. Adresi bir WebDAV önekiyle girin, örneğin `dav://192.168.1.20:8080` (`davs://` yalnızca TLS kurduysanız kullanın).
3. Konuk olarak bağlanın veya oturum açma bilgilerinizi girin.

## Android'den bağlanın

Android'in sistem düzeyinde bir WebDAV tarayıcısı yoktur; bu nedenle onu destekleyen bir dosya yöneticisi kullanın:

1. **Solid Explorer** veya **CX File Explorer** gibi bir uygulama yükleyin.
2. Yeni bir **WebDAV** bağlantısı ekleyin.
3. Ana bilgisayarı ve **8080 bağlantı noktasını** girin, `http` şemasını seçin ve ayarladıysanız oturum açma bilgilerinizi ekleyin.

## Başka bir iPhone veya iPad'den bağlanın

iOS Dosyalar uygulaması bir WebDAV istemcisi içermez; bu nedenle bunlardan birini kullanın:

- **Everdisk'in kendi Cihazlar sekmesi.** İkinci cihazda Everdisk'i açın, **Cihazlar**'a gidin, **Yeni Bağlantı**'ya dokunun, **WebDAV**'ı seçin ve adresi girin, örneğin `http://192.168.1.20:8080`. Bu en basit yoldur ve ekstra bir şey gerektirmez.
- **Bir WebDAV uygulaması** olan Documents by Readdle gibi; aynı adres ve oturum açma bilgileriyle bir WebDAV bağlantısı ekleyebilir.

## Bir sürücü yerine hızlı bir bağlantı mı tercih edersiniz?

Yalnızca bir dosyayı hızlıca almak istiyorsanız ve hiç sürücü bağlamak istemiyorsanız, Ayarlar, Paylaşım, Bağlantılar'da **Tarayıcı** bağlantısını açın. Everdisk daha sonra size, dosyalarınıza göz atmak ve indirmek için herhangi bir cihazdaki herhangi bir tarayıcıda açabileceğiniz bir web adresi verir. Bir dosyayı bir Windows PC'ye, bir Chromebook'a veya bir arkadaşınızın telefonuna vermenin en hızlı yoludur.

## Salt okunur veya okuma ve yazma

Ayarlar, Paylaşım, Erişim'deki **Dosya Düzenleme** anahtarı buna karar verir. Açık, bağlı bilgisayarların yükleyebileceği, yeniden adlandırabileceği ve silebileceği anlamına gelir. Kapalı, sürücünün salt okunur olduğu anlamına gelir; böylece diğerleri dosyalarınızı görüntüleyebilir ve kopyalayabilir ancak değiştiremez.

## İnsanların bunu gerçek hayatta kullanma yolları

- **Bir Windows PC'den iPhone'unuza dosya kopyalayın**, onu bir ağ konumu olarak eşleyip dosyaları karşıya sürükleyerek.
- **Fotoğrafları ve belgeleri bir dizüstü bilgisayara aktarın**, kablo ve iTunes olmadan, zaten bildiğiniz dosya yöneticisini kullanarak.
- **Bir belgeyi yerinde düzenleyin**, Mac'inizden onu doğrudan telefondan açıp geri kaydederek.
- **Bir iPhone ile bir iPad arasında bir klasör taşıyın**, alıcı cihazda Everdisk'in Cihazlar sekmesini kullanarak.

## Birkaç ipucu

- Bir cihaz bağlıyken Everdisk'i açık tutun. Telefonu uzun süre kilitlemek uygulamayı duraklatabilir.
- Windows'ta bağlantı başarısız olursa, WebClient hizmetini başlatın ve adresi yeniden deneyin.
- WebDAV ve SMB'nin ikisi de ağ sürücüsü olarak bağlanır. Windows söz konusu olduğunda WebDAV'ı, Finder hızı ve şifreleme istediğinizde [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)'yi kullanın.
- En hızlı aktarımlar için Ayarlar'da fotoğraf ve video kalitesini Orijinal'de tutun.

## Sıkça Sorulan Sorular

{{% details title="iPhone'um için WebDAV adresi ve bağlantı noktası nedir?" closed="true" %}}
Paylaşımı başlattıktan sonra Everdisk adresi Paylaşım ekranında gösterir. http://192.168.1.20:8080 gibi görünür. 8080, Everdisk'in WebDAV için kullandığı bağlantı noktasıdır ve ilk kısım iPhone'unuzun Wi-Fi'deki adresidir; bu nedenle sizinki farklı olacaktır.
{{% /details %}}

{{% details title="iPhone WebDAV'ıma Windows'tan nasıl bağlanırım?" closed="true" %}}
Dosya Gezgini'ni açın, Bu Bilgisayar'a sağ tıklayın ve Ağ konumu ekle veya Ağ sürücüsü eşle'yi seçin. Everdisk'teki WebDAV adresini girin, örneğin http://192.168.1.20:8080, ardından ayarladıysanız oturum açma bilgilerinizi girin. Windows bağlanmazsa, WebClient hizmetinin çalıştığından emin olun (Hizmetler'i arayın, WebClient'i bulun, başlatın) ve yeniden deneyin.
{{% /details %}}

{{% details title="İki iPhone arasında WebDAV kullanabilir miyim?" closed="true" %}}
Evet, ama iOS Dosyalar uygulamasında WebDAV istemcisi yoktur; bu nedenle ikinci cihazda Everdisk'i kullanın. Cihazlar sekmesini açın, Yeni Bağlantı'ya dokunun, WebDAV'ı seçin ve ilk telefonda gösterilen adresi girin. Documents by Readdle gibi bir WebDAV uygulaması da çalışır.
{{% /details %}}

{{% details title="WebDAV bir parola gerektirir mi?" closed="true" %}}
Hayır, oturum açma isteğe bağlıdır. Konuk erişimi için Ayarlar, Paylaşım, Erişim'de Kullanıcı Adı ve Parola'yı boş bırakın veya bağlantıların oturum açmasını istiyorsanız onları ayarlayın.
{{% /details %}}

{{% details title="Başkaları WebDAV üzerinden dosyalarımı değiştirebilir mi?" closed="true" %}}
Yalnızca izin verirseniz. Ayarlar, Paylaşım, Erişim'deki Dosya Düzenleme anahtarı bunu kontrol eder. Açık, bağlı cihazların yüklemesine, yeniden adlandırmasına ve silmesine izin verir. Kapalı, sürücüyü salt okunur yapar; böylece diğerleri görüntüleyip kopyalayabilir ancak hiçbir şeyi değiştiremez.
{{% /details %}}

{{% details title="WebDAV veya SMB, fark nedir?" closed="true" %}}
Her ikisi de iPhone'unuzu bir ağ sürücüsü olarak bağlar. WebDAV, web protokolü üzerinden çalışır ve Windows Dosya Gezgini'nden sorunsuz bağlanır; bu onun ana gücüdür. SMB, Mac, Linux ve NAS cihazlarındaki yerel dosya paylaşımıdır, bir Mac'te genellikle daha hızlıdır ve aktarımları şifreleyebilen tek Everdisk bağlantısıdır. Everdisk her ikisini de aynı anda çalıştırabilir.
{{% /details %}}

{{% details title="WebDAV sürücüm neden bağlantısı kesiliyor?" closed="true" %}}
iPhone'unuz sunucudur ve iOS çok uzun süre arka planda kalan uygulamaları duraklatır. Bir cihaz bağlıyken Everdisk'i ekranda açık tutun ve uzun aktarımlar için güce takın. Ayrıca her iki cihazın da hâlâ aynı Wi-Fi'de olduğunu doğrulayın.
{{% /details %}}

{{% details title="Wi-Fi olmadan WebDAV üzerinden bağlanabilir miyim?" closed="true" %}}
Evet, iPhone'unuzu bir Mac'e kabloyla takarsanız. Everdisk daha sonra, bağlı Mac'in Finder'da açabileceği ekstra bir kablo bağlantı adresi gösterir; bu, hiç Wi-Fi olmasa bile çalışır. Kabloda cihaza yalnızca o Mac ulaşabilir.
{{% /details %}}

{{% details title="Everdisk ücretsiz mi?" closed="true" %}}
Evet, Everdisk ücretsiz indirilir ve WebDAV sunucusu dahildir. İsteğe bağlı, tek seferlik Premium satın alma, özel bağlantı noktaları ve fotoğraf ve video dönüştürme gibi ekstralar ekler. WebDAV'ı ödeme yapmadan kurabilir ve dosya paylaşabilirsiniz.
{{% /details %}}

Denemeye hazır mısınız? [Everdisk'i App Store'dan indirin](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) ve birkaç dakika içinde iPhone'unuzu bir sürücü olarak bağlayın. Sorularınız veya geri bildiriminiz mi var? Bize **support@everappz.com** adresinden e-posta gönderin.
