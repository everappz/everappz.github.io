---
title: "iPhone ve iPad'de Dosya Paylaşımı için SMB Sunucusu Nasıl Kurulur"
description: "Everdisk ile iPhone veya iPad cihazınızı bir SMB dosya sunucusuna dönüştürün ve Wi-Fi üzerinden bir Mac'ten, başka bir iPhone'dan, Linux veya Android'den bir ağ sürücüsü gibi açın. Eksiksiz kurulum, smb adresi ve bağlantı noktası, isteğe bağlı SMB3 şifrelemesi ve her cihaz için adım adım bağlantı."
date: 2026-09-19
tags: ["everdisk", "smb", "dosya paylaşımı", "ağ sürücüsü", "iphone", "ipad", "mac", "finder", "şifreleme", "wifi"]
keywords: ["SMB sunucusu iPhone", "SMB sunucusu iPad", "iPhone'da SMB nasıl kurulur", "iPhone SMB paylaşımı", "iPhone SMB Mac Finder bağlantısı", "smb iphone'dan iphone'a", "iOS Dosyalar uygulaması SMB sunucusuna bağlanma", "iPhone SMB dosya paylaşımı", "iphone ağ sürücüsü Finder", "SMB3 şifrelemesi iOS", "smb paylaşımı iPhone Android", "Linux'tan SMB'ye bağlanma", "iphone ağ sürücüsü olarak", "iphone'lar arası dosya paylaşımı wifi", "iphone'u ağ sürücüsü olarak eşleme"]
readingTime: 10
---

{{< author-byline >}}

SMB, macOS, Windows ve Linux'a ve neredeyse her ağ sürücüsüne (NAS) yerleşik olan dosya paylaşımıdır. Başka bir bilgisayardaki paylaşılan bir klasöre bağlandığınızda ve o klasör Finder veya Dosya Gezgini'nde normal bir disk gibi açıldığında, işi yapan SMB'dir. [Everdisk](/products/everdisk) ile iPhone veya iPad cihazınıza bir SMB paylaşımı koyabilirsiniz; böylece telefonun kendisi, diğer cihazların göz attığı, kopyaladığı ve içine kopyaladığı bir ağ sürücüsü olarak görünür.

iPhone'unuzun bir web sayfası gibi değil, gerçek bir sürücü gibi davranmasını istediğinizde başvuracağınız seçenek budur. Hızlıdır, her iki yönde sürükle ve bırak yapar ve Everdisk'te her aktarımı şifreleyebilen tek bağlantı türüdür. Bu kılavuz, kurulumu ve bir Mac'ten, başka bir iPhone veya iPad'den, Linux'tan, Android'den ve Windows'tan nasıl bağlanılacağını kapsar.

## İhtiyacınız olanlar

- [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) yüklü bir iPhone veya iPad.
- **Aynı Wi-Fi ağında** başka bir cihaz.
- Paylaşmak istediğiniz dosyalar, Everdisk Belgeler klasöründe veya eklediğiniz klasörlerde.

## Everdisk'te SMB sunucusunu kurun

### Adım 1: Ne paylaşacağınızı ve kimin yazabileceğini seçin

Everdisk'i açın, **Paylaşım** sekmesine gidin ve **Ne Paylaşılacak**'a dokunun. Belgeler klasörü varsayılan olarak paylaşılır. **Klasör Ekle** ve **Dosya Ekle** ile daha fazlasını ekleyin ve bunları da kullanılabilir kılmak istiyorsanız Fotoğraflar veya Müzik kitaplığınızı açın.

Diğer cihazların dosyalarınızı yalnızca okuyabileceğine mi yoksa değiştirebileceğine de karar verin. **Ayarlar**'ı, ardından **Paylaşım**'ı, ardından **Erişim**'i açın ve **Dosya Düzenleme**'yi ayarlayın. Açıkken bağlı cihazlar telefonunuza dosya kopyalayabilir ve yeniden adlandırabilir veya silebilir. Kapalıyken paylaşım salt okunurdur.

Bir oturum açma istiyorsanız aynı Erişim ekranında bir **Kullanıcı Adı** ve **Parola** ayarlayın. Konuk erişimine izin vermek için ikisini de boş bırakın.

### Adım 2: SMB sunucusunu açın

**Ayarlar**'a, ardından **Paylaşım**'a, ardından **Bağlantılar**'a gidin ve **Bilgisayar (Gelişmiş)**'i açın. Bu, SMB sunucusudur (SMB etiketini taşır).

### Adım 3: Paylaşımı başlatın ve adresi not edin

**Paylaşım** sekmesine geri dönün ve **Başlat**'a dokunun. **Nasıl Bağlanılır** bölümü artık SMB adresini gösterir. Şuna benzer:

```
smb://192.168.1.20:4455/Share
```

Bu adres hakkında bilinmesi gereken üç şey:

- İki nokta üst üsteden sonraki sayı **bağlantı noktasıdır**. Everdisk varsayılan olarak **4455** kullanır.
- Paylaşımın adı **Share**'dir.
- İlk kısım, iPhone'unuzun Wi-Fi'deki adresidir; bu nedenle ağınızda farklı olacaktır.

Cihazlar bağlıyken Everdisk'i açık tutun, çünkü iOS çok uzun süre arka planda kalan uygulamaları duraklatır.

## Bir Mac'ten bağlanın

macOS SMB'yi yerel olarak konuştuğu için bu en sorunsuz durumdur.

En hızlı yol: **Finder**'ı açın ve kenar çubuğunda **Konumlar** veya **Ağ** altına bakın. Everdisk kendini Wi-Fi'de duyurur; bu nedenle iPhone'unuz genellikle orada kendiliğinden görünür. Ona tıklayın, ardından **Farklı Bağlan**'a tıklayın ve **Konuk**'u seçin ya da oturum açma bilgilerinizi girin.

Elle bağlanmak için:

1. Finder'da **Git**'i, ardından **Sunucuya Bağlan**'ı seçin (veya **Command ve K**'ye basın).
2. Everdisk'te gösterilen SMB adresini yazın, örneğin `smb://192.168.1.20:4455/Share`.
3. **Bağlan**'a tıklayın, ardından **Konuk**'u seçin veya **Kullanıcı Adı** ve **Parola**'nızı girin.

iPhone'unuz bir Finder penceresinde açılır. Dosyaları sürükleyerek tam olarak diğer sürücülerdeki gibi içeri veya dışarı kopyalayın (Dosya Düzenleme açıksa).

## Başka bir iPhone veya iPad'den bağlanın

iOS ve iPadOS, SMB paylaşımlarını yerleşik **Dosyalar** uygulamasında açabilir; bu da telefondan telefona aktarımları temiz ve hızlı kılar.

İkinci cihazda:

1. **Dosyalar** uygulamasını açın.
2. **daha fazla** düğmesine (iPhone'da sağ üstteki üç nokta) dokunun ve **Sunucuya Bağlan**'ı seçin.
3. Everdisk'teki SMB adresini girin, örneğin `smb://192.168.1.20:4455/Share`.
4. **Konuk**'u ya da **Kayıtlı Kullanıcı**'yı seçin ve oturum açma bilgilerinizi girin.
5. Paylaşım, Dosyalar'da Konumlar altında görünür. Göz atın ve her iki yönde kopyalayın.

İkinci cihazda Everdisk'in kendi **Cihazlar** sekmesini de kullanabilirsiniz; bu sekme bir SMB istemcisi içerir. Everdisk'i açın, **Cihazlar**'a gidin, **Yeni Bağlantı**'ya dokunun, **SMB**'yi seçin ve adresi girin.

## Linux'tan bağlanın

1. Dosya yöneticinizi açın (GNOME'da Files/Nautilus, KDE'de Dolphin).
2. **Other Locations** veya **Connect to Server**'ı seçin.
3. Adresi girin, örneğin `smb://192.168.1.20:4455/Share`.
4. Konuk olarak bağlanın veya oturum açma bilgilerinizi girin.

Bir terminalden ayrıca `smbclient //192.168.1.20/Share -p 4455` komutunu çalıştırabilir ve sorulduğunda oturum açma bilgilerinizi girebilirsiniz.

## Android'den bağlanın

Android'in sistem düzeyinde bir SMB tarayıcısı yoktur; bu nedenle SMB'yi destekleyen bir dosya yöneticisi kullanın:

1. **CX File Explorer**, **Solid Explorer** veya **X-plore File Manager** gibi bir uygulama yükleyin.
2. Yeni bir **SMB** veya **LAN** bağlantısı ekleyin.
3. Ana bilgisayarı (iPhone'unuzun Wi-Fi adresi) girin, **bağlantı noktasını 4455** olarak ayarlayın ve paylaşım adı **Share**'i girin.
4. Konuk olarak veya oturum açma bilgilerinizle bağlanın, ardından göz atın ve kopyalayın.

## Windows'tan bağlanın

Windows SMB paylaşımlarını okuyabilir, ancak baştan bilinmesi gereken bir püf noktası vardır. Yerleşik Dosya Gezgini yalnızca standart bağlantı noktasındaki SMB ile konuşur ve yola özel bir bağlantı noktası yazmanıza izin vermez; Everdisk ise 4455 bağlantı noktasını kullanır. Bu nedenle düz **Ağ sürücüsü eşle** yolu ona genellikle ulaşamaz.

Windows'ta iki iyi seçeneğiniz var:

- Özel bir bağlantı noktası ayarlamanıza izin veren bir dosya yöneticisi veya SMB istemcisi kullanın ve onu iPhone'unuzun adresine, **4455** bağlantı noktasıyla ve paylaşım adı **Share** ile yönlendirin.
- Ya da bunun yerine Everdisk'in diğer sunucularından birini kullanarak Windows'tan bağlanın. [WebDAV kurulumu](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) ve [FTP kurulumu](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/), her ikisi de Windows Dosya Gezgini'nden iyi çalışır ve tarayıcı bağlantısı herhangi bir tarayıcıda çalışır.

Yine de Ağ sürücüsü eşle'yi denemek isterseniz: **Dosya Gezgini**'ni açın, **Bu Bilgisayar**'a sağ tıklayın, **Ağ sürücüsü eşle**'yi seçin ve Everdisk'te gösterilen ana bilgisayar ve paylaşım adını girin. Bağlanamıyorsa, bu yukarıdaki bağlantı noktası sınırlamasıdır; bu nedenle WebDAV veya FTP'ye geçin.

## Güvenilmeyen Wi-Fi için şifrelemeyi açın

SMB, her aktarımı şifreleyebilen tek Everdisk bağlantısıdır; bu, bir kafe veya ofis ağı gibi tam olarak kontrol etmediğiniz Wi-Fi'de önemlidir.

1. **Ayarlar**, **Paylaşım**, **Erişim**'de bir **Kullanıcı Adı** ve **Parola** ayarlayın. Şifreli bağlantılar anonim olamaz; bu nedenle bu adım gereklidir.
2. **Ayarlar**, **Paylaşım**'da **SMB şifrelemesi iste**'yi açın.
3. Değişikliğin etkili olması için paylaşımı durdurup yeniden başlatın.

Her SMB aktarımı bundan sonra **SMB3 şifrelemesiyle (AES)** korunur. Bağlanan cihazın SMB3'ü desteklemesi gerekir; modern bir Mac'teki Finder ve Windows 10 veya sonrası bunu destekler. SMB Şifrelemesi, tek seferlik Premium satın almanın bir parçasıdır.

## Salt okunur veya okuma ve yazma

Ayarlar, Paylaşım, Erişim'deki **Dosya Düzenleme** anahtarı, SMB dahil her sunucu için bunu kontrol eder. Açın ve bağlı cihazlar yükleyebilir, yeniden adlandırabilir ve silebilir. Kapatın ve yalnızca göz atıp telefonunuzdan dosya kopyalayabilirler. Hiçbir şeyi değiştirmesini istemediğiniz birine dosya verirken salt okunuru seçin.

## İnsanların bunu gerçek hayatta kullanma yolları

- **Bir Mac'ten iPhone'unuza büyük bir klasör taşıyın**, onu Finder penceresine sürükleyerek; bu bir web yüklemesinden daha hızlıdır.
- **Bir günlük fotoğraf ve videoyu telefonunuzdan çekin**, iTunes veya kablo olmadan bir dizüstü bilgisayara.
- **İki iPhone arasında dosya gönderin**, Dosyalar uygulaması üzerinden, her iki tarafta da üçüncü bir uygulama olmadan.
- **Bir dosyayla yerinde çalışın**, telefondan bir belgeyi doğrudan Mac'inizdeki bir uygulamada açıp geri kaydederek.

## Birkaç ipucu

- Bir cihaz bağlıyken Everdisk'i açık tutun. Telefonu uzun süre kilitlemek uygulamayı duraklatabilir ve bağlantıyı düşürebilir.
- Bir Mac telefonu Finder kenar çubuğunda göremiyorsa, Sunucuya Bağlan ve tam smb adresiyle elle bağlanın.
- Büyük aktarımlarda en iyi hız için Ayarlar'da fotoğraf ve video kalitesini Orijinal'de tutun.
- Güvenilmeyen bir ağda, SMB şifrelemesi iste'yi açın ve çalışırken diğer sunucuları kapatın.

## Sıkça Sorulan Sorular

{{% details title="iPhone'um için SMB adresi ve bağlantı noktası nedir?" closed="true" %}}
Paylaşımı başlattıktan sonra Everdisk adresi Paylaşım ekranında gösterir. smb://192.168.1.20:4455/Share gibi görünür. 4455, Everdisk'in SMB için kullandığı bağlantı noktasıdır ve Share, paylaşılan klasörün adıdır. İlk kısım iPhone'unuzun Wi-Fi'deki adresidir; bu nedenle sizinki farklı olacaktır.
{{% /details %}}

{{% details title="iPhone SMB paylaşımıma Windows'tan bağlanabilir miyim?" closed="true" %}}
Windows Dosya Gezgini yalnızca standart bağlantı noktasındaki SMB'ye bağlanır ve yolda özel bir bağlantı noktasını kabul etmez; Everdisk ise 4455 bağlantı noktasını kullanır. Bu nedenle düz Ağ sürücüsü eşle yolu ona genellikle ulaşamaz. Özel bir bağlantı noktası ayarlamanıza izin veren bir dosya yöneticisi kullanın ya da bunun yerine Windows'tan WebDAV, FTP veya tarayıcı bağlantısıyla bağlanın. Bunların hepsi Windows'tan bağlantı noktası sorunu olmadan çalışır.
{{% /details %}}

{{% details title="İki iPhone arasında SMB ile dosyaları nasıl paylaşırım?" closed="true" %}}
İlk iPhone'da Everdisk'te SMB sunucusunu başlatın. İkinci iPhone'da Dosyalar uygulamasını açın, daha fazla düğmesine dokunun, Sunucuya Bağlan'ı seçin ve Everdisk'te gösterilen smb adresini girin (örneğin smb://192.168.1.20:4455/Share). Konuk olarak veya oturum açma bilgilerinizle bağlanın; paylaşım Dosyalar'da görünür. İkinci telefonda Everdisk'in kendi Cihazlar sekmesini de kullanabilirsiniz.
{{% /details %}}

{{% details title="iPhone'um Mac Finder kenar çubuğunda otomatik olarak görünür mü?" closed="true" %}}
Genellikle evet. Everdisk SMB paylaşımını Wi-Fi'nizde duyurur; bu nedenle iPhone'unuz çoğunlukla Finder kenar çubuğunda Konumlar veya Ağ altında görünür. Ona tıklayın ve Farklı Bağlan'ı, ardından Konuk'u veya oturum açma bilgilerinizi seçin. Görünmüyorsa, Git, Sunucuya Bağlan ve tam smb adresiyle elle bağlanın.
{{% /details %}}

{{% details title="SMB kullanmak için bir parolaya ihtiyacım var mı?" closed="true" %}}
Hayır, oturum açma isteğe bağlıdır. Konuk erişimine izin vermek için Ayarlar, Paylaşım, Erişim'de Kullanıcı Adı ve Parola'yı boş bırakın. Bağlantıların oturum açmasını istiyorsanız onları ayarlayın. Kullanıcı adı ve parola yalnızca SMB şifrelemesi iste'yi açarsanız gereklidir, çünkü şifreli bağlantılar anonim olamaz.
{{% /details %}}

{{% details title="SMB bağlantısı şifreli mi?" closed="true" %}}
Öyle olabilir. SMB, şifrelemeyi destekleyen tek Everdisk bağlantısıdır. Bir kullanıcı adı ve parola ayarlayın, ardından Ayarlar, Paylaşım'da SMB şifrelemesi iste'yi açın. Her aktarım bundan sonra SMB3 (AES) ile korunur. Diğer cihazın SMB3'ü desteklemesi gerekir; modern Mac'ler ve Windows 10 veya sonrası bunu destekler. Şifreleme bir Premium özelliğidir.
{{% /details %}}

{{% details title="İnsanlar SMB üzerinden dosyalarımı değiştirebilir veya silebilir mi?" closed="true" %}}
Yalnızca izin verirseniz. Ayarlar, Paylaşım, Erişim'deki Dosya Düzenleme anahtarı bunu kontrol eder. Açıkken bağlı cihazlar yükleyebilir, yeniden adlandırabilir ve silebilir. Kapalıyken paylaşım salt okunurdur ve diğerleri telefonunuzdan dosyalara göz atabilir ve kopyalayabilir, ancak hiçbir şeyi değiştiremez.
{{% /details %}}

{{% details title="SMB bağlantım neden düştü?" closed="true" %}}
iPhone'unuz sunucudur ve iOS çok uzun süre arka planda kalan uygulamaları duraklatır. Bir cihaz bağlıyken Everdisk'i ekranda açık tutun ve uzun aktarımlar sırasında telefonu güce takın. Ayrıca her iki cihazın da aynı Wi-Fi'de kaldığından emin olun.
{{% /details %}}

{{% details title="SMB, WebDAV veya FTP, hangisini kullanmalıyım?" closed="true" %}}
Telefonun bir Mac'te, başka bir iPhone'da, Linux'ta veya bir NAS'ta gerçek bir ağ sürücüsü gibi davranmasını istediğinizde ve şifreleme istediğinizde SMB kullanın. Windows'tan da iyi çalışan bir ağ sürücüsü istediğinizde WebDAV kullanın. Eski cihazlar ve uygulamalarla en geniş uyumluluk için FTP kullanın. Everdisk hepsini aynı anda çalıştırabilir; bu nedenle tek birine bağlı kalmazsınız.
{{% /details %}}

{{% details title="Everdisk ücretsiz mi?" closed="true" %}}
Evet, Everdisk ücretsiz indirilir ve SMB sunucusu dahildir. İsteğe bağlı, tek seferlik Premium satın alma, SMB şifrelemesi, özel bağlantı noktaları ve birkaç ekstra ekler. SMB'yi ödeme yapmadan kurabilir ve dosya paylaşabilirsiniz.
{{% /details %}}

Denemeye hazır mısınız? [Everdisk'i App Store'dan indirin](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) ve yaklaşık bir dakika içinde iPhone'unuzu Finder'da açın. Sorularınız veya geri bildiriminiz mi var? Bize **support@everappz.com** adresinden e-posta gönderin.
