---
title: "Bağlantılar"
date: 2020-02-01
description: "Flacbox'a bulut hizmetleri ve NAS cihazları bağlamayı öğrenin. iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk ve daha fazlasından yüksek çözünürlüklü müzik akışı yapın. SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder Dosya Paylaşımı ve USB flash sürücüler kullanın."
keywords: [
  "Flacbox bulut kurulumu", "Google Drive Flacbox bağlantısı", "SMB müzik akışı",
  "WebDAV iOS çalar", "DLNA müzik uygulaması", "NAS ses akışı", "Wi-Fi Drive iPhone",
  "iPhone'a dosya aktarma", "Flacbox iTunes Dosya Paylaşımı", "NAS iPhone bağlantısı",
  "Synology Drive müzik uygulaması", "QNAP müzik uygulaması", "Bluesound müzik uygulaması",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling müzik uygulaması",
  "iXpand Flash Drive müzik", "USB DAC iPhone"
]
tags: ["kılavuz", "flacbox", "bağlantılar", "bulut", "NAS"]
readingTime: 12
---


Bu ekranda müziğinizin bulunduğu her kaynağı bağlayabilirsiniz. Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive gibi popüler bulut hizmetlerini ve standart protokoller üzerinden Mac, PC veya NAS'ınızı entegre edebilirsiniz. Koleksiyonunuz Dropbox gibi akış dostu bir hizmette mi, yoksa Synology, QNAP, Buffalo, Apple Time Capsule veya WD My Cloud Home gibi kişisel bir NAS'ta mı olursa olsun, Flacbox tek bir ekrandan hepsine bağlanır.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Bağlantılar Ekranı" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Bulut Depolama Alanına Bağlan

- **Bağlantılar** sekmesini açın.
- Menüden **Bulut depolama alanına bağlan** seçeneğini belirleyin.
- Listeden bir bulut depolama hizmeti seçin.
- Bulut sağlayıcısının sunduğu resmi yetkilendirme sayfasına kimlik bilgilerinizi girin, ardından **Tamamlandı** seçeneğine dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Bulut Depolama Hizmeti Ekleme" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Herhangi bir sorunla karşılaşırsanız internet bağlantınızı ve giriş / şifrenizi kontrol edin. Uygulamanın Premium sürümünde sınırsız sayıda hizmet ekleyebilirsiniz; ücretsiz sürüm en fazla üç hizmeti destekler.

## Desteklenen Bulut Depolama Hizmetleri, Medya Sunucuları ve Protokoller

Flacbox, müziğiniz için son derece geniş bir kaynak yelpazesini destekler. Aşağıdakilerin tamamı tek bir **Bulut depolama alanına bağlan** ekranından çalışır.

**Kişisel bulut depolama:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Kendi barındırılan sunucular:** Plex · Jellyfin · Emby · Subsonic (ve her Subsonic uyumlu sunucu — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (ve paylaşılan API aracılığıyla ownCloud) · Synology Drive · QNAP.

**NAS ve dosya paylaşım protokolleri:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH Dosya Aktarım Protokolü, parola veya ortak anahtar kimlik doğrulaması) · NFS · DLNA / UPnP (oynatma ve indirme).

**S3 uyumlu nesne depolama:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ve S3 API uç noktası sunan diğer tüm hizmetler.

**Yerel ağ keşfi:** Mevcut Cihazlar bölümü, Wi-Fi ağınızdaki her Bonjour / mDNS hizmetini otomatik olarak listeler; böylece IP adresi yazmadan dokunarak bağlanabilirsiniz.

Her bağlantı, desteklendiği durumlarda OAuth tabanlı yetkilendirmeyle birlikte hizmetin **resmi SDK veya açık protokolünü** kullanır. Aynı hizmetin birden fazla hesabını bağlayabilir (örneğin iki Google Drive hesabı, kişisel ve iş Dropbox'ı ya da hem Plex hem Jellyfin sunucusu) ve Bağlantılar ekranında bunlara yan yana göz atabilirsiniz.

## Güvenlik ve Gizlilik

Bağlı bulut hizmetleriyle etkileşim için yalnızca resmi SDK'ları ve güvenli bağlantıları kullanıyoruz. Giriş bilgileriniz ve şifreniz uygulamaya erişilemez — tüm aktarımlar TLS ile şifrelenir.

Giriş bilgilerinizi girdiğinizde uygulama, bulut hizmet sağlayıcısının sunduğu resmi yetkilendirme sayfasını gösterir ve yetkilendirme işleminin tamamı uygulamanın dışında gerçekleşir. Başarılı yetkilendirmenin ardından bulut hizmet sağlayıcısı, uygulamaya bir kimlik doğrulama token'ı gönderir ve bu token API çağrıları için kullanılır.

Kimlik doğrulama token'ı, üçüncü taraf uygulamaların bulut depolama alanınızla sizin adınıza etkileşim kurmasını sağlayan dijital bir anahtardır. Token, cihazınızda Apple'ın güvenli sistem deposunda (Keychain) saklanır; bu depo depolamada şifrelenir ve cihaz parolanız ya da biyometrik kilitleme ile korunur. Bağlı bulut hizmetlerinden cihazınıza dosya indirebilirsiniz; bu dosyalar uygulamanın Documents dizinine yerleştirilir ve yerleşik dosya yöneticisi kullanılarak her zaman silinebilir.

Uygulama, bağlı bulut hesaplarınızdaki hiçbir bilgiyi Everappz, reklamverenler veya herhangi bir üçüncü tarafla paylaşmaz. Web tarayıcınızda hesap ayarları sayfasını açarak bulut hesabınıza erişimi istediğiniz zaman iptal edebilirsiniz.

## Kimlik Doğrulama Token'ını İptal Etme

Bir token'ı iptal etmek için web tarayıcısında bulut hesabınıza giriş yapın ve güvenlik veya bağlı uygulamalar sayfasına gidin. Burada bulut hesabınıza bağlı tüm üçüncü taraf uygulamaları görebilir ve artık kullanmak istemediklerinizi kaldırabilirsiniz. Google hesapları için ayrıntılı talimatlar [burada](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) mevcuttur.

Uygulamanın içinden de bulut hesabının bağlantısını kesebilirsiniz — bu işlemi yaptığınızda token cihazınızdan hemen silinir. Uygulamayı cihazınızdan kaldırırsanız, indirilen tüm veriler ve erişim token'ları otomatik olarak onunla birlikte silinir.

## Bulut Depolama Bağlantısını Kesme veya Yapılandırmayı Değiştirme

- **Bulut depolama seçeneklerine erişin** — **Bağlantılar** ekranında bağlı hizmeti bulun.
- Ek seçenekleri açmak için hizmet başlığının yanındaki **"..." düğmesine** dokunun:
  - **Yeniden Adlandır** — bulut hizmetinin listenizdeki görünen adını değiştirin.
  - **Ayarlar** — yapılandırmayı veya kimlik doğrulama verilerini düzenleyin. Yetkilendirme token'ının süresi dolduysa bağlı bulut hizmetini yeniden yetkilendirmeniz gerekebilir.
  - **Bağlantıyı Kes** — uygulama ile bulut hizmet arasındaki bağlantıyı tamamen kesin. Bu işlem, söz konusu hizmetle ilişkili tüm şarkıları uygulamanın müzik kitaplığından kaldırır; ancak sunucudaki dosyalara dokunmaz.

## Bilgisayara veya NAS'a Bağlanma

SMB, DLNA veya WebDAV protokollerini kullanarak bilgisayarınıza, kişisel NAS'ınıza veya diğer ağ cihazlarına da bağlanabilirsiniz. Mac, Windows PC, Synology kutusu veya NAS'ta bulunan mevcut bir ev müzik kitaplığını hiçbir şeyi kopyalamadan Flacbox'a taşımanın en kolay yolu budur.

## SMB Kullanarak Bilgisayara Bağlanma

- **Bulut depolama alanına bağlan → SMB** seçeneğine dokunun.
- URL alanına bilgisayarın IP adresini ve paylaşılan klasör adını `smb://bilgisayar-ip-adresi/paylaşılan-klasör-adı` biçiminde girin.
- Protokol sürümünü seçin: **Auto**, **SMB1** veya **SMB2**.
- Giriş adınızı ve şifrenizi girin (gerekiyorsa).
- **Tamamlandı** seçeneğine dokunun.

Bağlantı başarılıysa **Bulut Depolama** bölümünde bağlı depolama alanını göreceksiniz. SMB kullanarak Mac veya PC'nizi nasıl bağlayacağınıza ilişkin tam bir eğitim [burada](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) mevcuttur.

## WebDAV Kullanarak NAS'a Bağlanma

Tüm adımlar SMB ile aynıdır, yalnızca URL alanı farklıdır. URL, `http://sunucu-adı` biçiminde ya da sunucu SSL destekliyorsa `https://sunucu-adı` biçiminde olmalıdır. WebDAV; **Synology, QNAP, Nextcloud, ownCloud** ve WebDAV uç noktasının bulunduğu diğer birçok sunucuyla çalışır.

WebDAV kullanarak NAS bağlama hakkındaki tam eğitime [buradan](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) ulaşabilirsiniz.

## DLNA Kullanarak Bilgisayara veya NAS'a Bağlanma

Windows PC'nizde veya kişisel NAS'ınızda bulunan bir müzik kitaplığını DLNA / UPnP protokolü aracılığıyla paylaşabilir ve [burada](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) açıklandığı gibi bu kitaplığa uygulamadan erişebilirsiniz. DLNA popüler ve yaygın desteklenen bir protokoldür; ancak yalnızca müzik oynatmanıza veya indirmenize izin verir — DLNA sunucusuna dosya yükleyemez veya yeni klasör oluşturamazsınız.

## FTP, FTPS veya SFTP Kullanarak NAS'a veya Sunucuya Bağlanma

Flacbox, klasik dosya aktarım protokollerini de destekler. FTP veya FTPS üzerinden sunucu bağlamak için **Bulut depolama alanına bağlan → FTP** seçeneğine dokunun, host URL'sini `ftp://sunucu-adı` biçiminde (şifreli bağlantı için `ftps://sunucu-adı`) girin, giriş adınızı ve şifrenizi sağlayın, ardından **Tamamlandı** seçeneğine dokunun. **SFTP** (SSH Dosya Aktarım Protokolü) için **SFTP** seçeneğini belirleyin ve parola ya da SSH anahtar çifti sağlayın. Her ikisi de NAS cihazları, Linux sunucuları ve FTP / FTPS / SSH arka plan programı çalıştıran her sunucuyla çalışır.

## NFS Paylaşımına Bağlanma

Flacbox, **NFS** (Ağ Dosya Sistemi) desteği içerir — müzik kitaplıklarını SMB yerine NFS üzerinden sunan Linux sunucuları, BSD sunucuları ve NAS cihazları için oldukça kullanışlıdır. **Bulut depolama alanına bağlan** menüsünden **NFS** seçeneğini belirleyin, sunucu adresini ve dışa aktarılan yolu girin, ardından **Tamamlandı** seçeneğine dokunun.

## Plex Medya Sunucusu Bağlama

Flacbox, bir Plex Medya Sunucusuna doğrudan bağlanabilir ve müzik kitaplığınıza Sanatçılar, Albümler, Türler ve Çalma Listeleri üzerinden göz atabilirsiniz. **Bulut depolama alanına bağlan → Plex** seçeneğine dokunun, Plex hesabınızla giriş yapın, bir sunucu seçin; kitaplık bulut hizmetlerinizin yanında görünür. Aynı yerel ağdaki Plex sunucuları da **Mevcut Cihazlar** bölümünde otomatik olarak keşfedilir.

## Jellyfin veya Emby Sunucusu Bağlama

Hem **Jellyfin** (açık kaynak) hem de **Emby** (ticari) medya sunucuları Flacbox'ta yerel olarak çalışır. **Bulut depolama alanına bağlan → Jellyfin** veya **Emby** seçeneğine dokunun, sunucu URL'nizi (örneğin `http://sunucu-ip:8096`) ve kimlik bilgilerinizi girin; müzik kitaplığınız akışa hazır hale gelir. Plex'te olduğu gibi, yerel ağdaki kitaplıklar **Mevcut Cihazlar** bölümünde otomatik olarak listelenir.

## Subsonic veya Navidrome Sunucusu Bağlama

Flacbox, Subsonic API konuşur; bu da **Subsonic**'in kendisi, **Navidrome** ve diğer tüm Subsonic uyumlu sunucularla — Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache dahil — çalıştığı anlamına gelir. **Bulut depolama alanına bağlan → Subsonic** seçeneğine dokunun, sunucu URL'sini ve kimlik bilgilerini girin; kitaplık Bağlantılar ekranında görünür. Bu, temel dosya paylaşımını açıklamadan Flacbox'a kendi barındırdığınız müzik koleksiyonuna erişim vermenin en kolay yoludur.

## S3 Uyumlu Nesne Depolama Alanına Bağlanma

Bulut nesne depolama kullanan kendi barındırmacılar ve audiofiller için Flacbox, S3 uyumlu bir bağlayıcı içerir. **Bulut depolama alanına bağlan → S3 depolama** seçeneğine dokunun, ardından uç nokta URL'sini, bölgeyi, erişim anahtarını, gizli anahtarı ve kova adını girin. Bu; AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ve S3 API uç noktası sunan diğer tüm hizmetlerle çalışır.

## Mevcut Cihazlar

Bu bölüm, Bonjour keşfi aracılığıyla Flacbox'tan bağlanabileceğiniz yerel ağdaki tüm cihazları gösterir. Bağlantı kurmak için şu adımları izleyin:

- Uygulamayı açın ve Bağlantılar altındaki **Mevcut Cihazlar** bölümüne gidin.
- Bağlanmak istediğiniz cihaza dokunun.
- Gerekirse bağlantıyı tamamlamak için giriş bilgilerinizi girin.

Bu, IP adreslerini manuel olarak yazmadan ev ağınızdaki bir SMB, WebDAV veya DLNA paylaşımını keşfetmenin en hızlı yoludur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Yerel Ağdaki Mevcut Cihazlar" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive, bilgisayarınızdan iOS cihazınıza herhangi bir masaüstü tarayıcı aracılığıyla kablosuz dosya aktarımı sağlayan pratik bir teknolojidir. Bu özelliği etkin biçimde kullanmak için cihazınızın ve bilgisayarınızın aynı Wi-Fi ağına bağlı olduğundan emin olun. Wi-Fi Drive kullanma hakkında adım adım kılavuz aşağıda verilmiştir.

### Wi-Fi Drive'ı Etkinleştirme

- Uygulamayı açın ve **Bağlantılar** sekmesine gidin.
- Wi-Fi Drive ana ekranına erişmek için **Wi-Fi üzerinden bağlan** seçeneğini belirleyin.
- (İsteğe bağlı) Erişimi korumak amacıyla yerleşik web sunucusu için kullanıcı adı ve şifre belirleyin.
- Wi-Fi Drive'ı etkinleştirmek için **Wi-Fi Drive'ı Başlat** seçeneğine dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Bilgisayarınızdan Wi-Fi Drive'a Erişme

- Bilgisayarınızda (masaüstü veya dizüstü) Chrome, Firefox veya Safari gibi bir web tarayıcısı açın.
- Tarayıcının adres çubuğuna uygulama tarafından sağlanan URL'yi girin.

### Dosyaları Kablosuz Olarak Aktarma

iOS cihazınıza karşılık gelen web sayfası tarayıcıda açıldığında, bilgisayarınızdaki dosyaları web sayfasına sürükleyip bırakabilirsiniz. Bıraktığınız dosyalar iOS cihazınıza aktarılmaya başlar ve Flacbox içinden erişilebilir hale gelir.

Wi-Fi Drive'ı macOS'ta doğrudan Finder'a da bağlayabilirsiniz (Git → Sunucuya Bağlan…) veya Windows'ta Dosya Gezgini'ne (Ağ Sürücüsü Eşle…); iPhone veya iPad'inizi normal bir ağ sürücüsü gibi kullanın.

Wi-Fi Drive kullanarak dosyaları kablosuz aktarmaya ilişkin ayrıntılı talimatlar [burada](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) mevcuttur.

## iTunes / Finder Dosya Paylaşımı

iTunes Dosya Paylaşımı (macOS Catalina ve sonrasında Finder Dosya Paylaşımı), Lightning veya USB-C kablo kullanarak bilgisayardan cihaza dosya aktarmanın bir başka yoludur.

- Cihazı bir kablo ile bilgisayara bağlayın ve Mac'te **Finder**'ı (veya Windows'ta **iTunes**'u) çalıştırın.
- **Konumlar → Bağlı Cihazınız → Dosyalar** bölümünü açın ve Flacbox uygulamasını bulun.
- Tüm paylaşılan klasörleri görmek için uygulama simgesine dokunun.
- Sürükle ve bırak yöntemiyle bilgisayardaki dosyaları cihazdaki paylaşılan klasöre kopyalayın.

Finder Dosya Paylaşımı kullanma hakkında ayrıntılı talimatlar [burada](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) mevcuttur.

## USB Flash Sürücü Bağlama

SD kart veya USB sürücünüz varsa Lightning - USB / SD Kart Okuyucu veya USB-C sürücü (iPad ve iPhone 15 / 16 / 17 / Pro'da) kullanarak bağlayabilirsiniz. Uygulama, Apple Sertifikalı kart okuyucuları ve iXpand Flash Drive'ları destekler. iXpand Flash Drive ile Lightning bağlantı noktasına takın ve uygulamayı açın — Harici Cihaz Bağlandı mesajını ve cihaz bilgilerini göreceksiniz. Müzik klasörüne erişmek için flash sürücü simgesine dokunun ve oynatmayı başlatmak için herhangi bir ses dosyasına dokunun.

iPhone'a USB flash sürücü bağlama ve üzerinde müzik dinleme veya dosya yönetme hakkında ayrıntılı talimatlar [burada](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) mevcuttur.

## Dosya Yöneticisi

Bir bulut depolama hizmetini bağladıktan sonra, mevcut tüm dosya ve klasörleri görmek için simgesine dokunun. Bu dosyalarla çalışmak için yerleşik dosya yöneticisini kullanabilirsiniz — indirme, yeniden adlandırma, taşıma, yükleme, silme ve daha fazlası. Bir indirme başlattığınızda dosya aktarım kuyruğunda görünür. Aktarım kuyruğunu açmak için Yerel Dosyalar sekmesine gidin ve sol üst köşedeki dönen oklar simgesine dokunun. İndirilen tüm dosya ve klasörler Yerel Dosyalar bölümünde mevcuttur.

## Üst Araç Çubuğu

Gezinme çubuğunun hemen altında bulunan üst araç çubuğu, kolay erişim için birkaç yararlı eylem sunar. Basit bir aşağı kaydırma hareketiyle gösterip gizleyebilirsiniz.

- **Arama** — belirli dosya veya klasörleri bulmayı kolaylaştıran, geçerli dizin içinde hızlı arama yapmanızı sağlar.
- **Oynatmaya Devam Et** — uygulama ayarlarında etkinleştirilmişse, geçerli klasör için ses çalar kuyruğunu ve son medya konumunu geri yükler. Kaldığınız yerden devam etmek için pratik bir yoldur.
- **Tümünü Oynat** — geçerli klasörü ve alt klasörlerini tarar, ardından bulunan tüm ses dosyalarını yeni bir çalar kuyruğuna ekler. Bir dizindeki her parçayı oynatmak istediğinizde kullanışlıdır.
- **Tümünü Karıştır** — Tümünü Oynat gibi, ancak dosyaları ses çalar kuyruğuna eklemeden önce karıştırır. Eski bir müzik klasörünü yeniden keşfetmek için harikadır.

## Klasör Seçenekleri

Bir klasörü açtığınızda, sağ üst köşedeki **"..."** düğmesine dokunarak kullanışlı bir eylemler dizisine ulaşabilirsiniz.

- **Seç** — dosya seçim modunu etkinleştirir. Bu mod, klasör içinde bir veya daha fazla dosya seçmenizi ve seçimin tamamı üzerinde işlem yapmanızı sağlar.
- **Yeni Klasör** — geçerli klasör içinde yeni bir klasör oluşturur. Kitaplığınızı iyi yapılandırılmış tutmak için harikadır.
- **Çevrimdışı Modu Etkinleştir** — geçerli klasör için çevrimdışı modunu açar. Çevrimdışı mod, basit bir indirmenin ötesine geçer: klasördeki değişiklikleri aktif olarak izler. Çevrimiçi olarak yeni dosyalar eklerseniz, bunlar cihazınızda otomatik olarak görünür.
- **Dosya Yükle** — cihazınızdaki dosyaları çevrimiçi klasöre yükler. Bu sayede aynı bulut hizmeti aracılığıyla her yerden erişilebilir hale gelirler.
- **Arama** — geçerli klasör içinde belirli dosyaları arar.
- **Sırala** — dosyaları ada, boyuta, değiştirilme tarihine veya meta veriye göre sıralar. Varsayılan sıralama modu, sunucudaki sıralama düzenini yansıtır; ancak tercihlerinize göre değiştirebilirsiniz.
- **Izgara / Liste Görünümü** — tablo görünümü ile küçük resim görünümü arasında geçiş yapar. Tablo görünümü kompakt bir liste gösterir; küçük resim görünümü hızlı görsel tanımlama için büyük kapak önizlemeleri sunar.

## Çevrimiçi Dosyaları Düzenleme

Bulut depolama alanınızdaki birden fazla dosyayı yönetmeniz gerektiğinde, işlemlerinizi kolaylaştırmak için **Seçim Modu**'nu kullanın:

- **Seçim Modunu Etkinleştir** — sağ üst köşedeki **"..."** düğmesine dokunun ve **Seç** seçeneğini belirleyin.
- **Dosya Seçin** — her dosya ve klasörün yanında onay kutuları görünür. Bir veya birden fazla öğe seçmek için dokunun.
- **İşlem Yapın** — dosyaları veya klasörleri seçtikten sonra Sonra Oynat, Daha Sonra Oynat, Müzik Kitaplığına Ekle, Çalma Listesine Ekle, Kopyala, Yükle, Taşı, Yeniden Adlandır ve Sil seçeneklerine erişebilirsiniz.

Bağlı bulut depolama alanını salt okunur olarak kullanmayı tercih ederseniz (yanlışlıkla silmeleri önlemek için), arayüzden tüm yıkıcı işlemleri gizlemek için Ayarlar → Dosya Yöneticisi → Çevrimiçi Dosyaları Düzenle → Kapalı seçeneğini etkinleştirin.

## Dosya Eylemleri

Bir dosyanın eylemler menüsünü açmak için dosya başlığının yanındaki **"..."** simgesine dokunun:

- **Sonra Oynat** — dosyayı çalar kuyruğunun başına ekler; böylece geçerli parçanın hemen ardından oynatılır.
- **Daha Sonra Oynat** — dosyayı çalar kuyruğunun sonuna ekler.
- **Müzik Kitaplığına Ekle** — dosyayı sanatçı, albüm, tür veya besteciye göre düzenlenmiş müzik kitaplığınıza dahil eder.
- **Çalma Listesine Ekle** — dosyayı mevcut bir çalma listesine ekler veya yeni bir tane oluşturur.
- **Ses Etiketlerini Düzenle** — meta verileri değiştirmek için yerleşik etiket düzenleyicisini açar. Çevrimiçi dosyalar için parça geçici olarak indirilir, düzenlenir ve ardından onayladıktan sonra yeniden yüklenir.
- **Favorilere Ekle** — dosyayı hızlı erişim için favoriler listenize ekler.
- **İndir** — dosyayı veya klasörü çevrimdışı kullanım için cihazınıza indirir.
- **Yeniden Adlandır** — dosyayı doğrudan uzak depolama alanında yeniden adlandırır.
- **Taşı** — dosyayı bulut depolama alanınızdaki farklı bir klasöre taşır.
- **Şurada Aç** — dosyayı başka bir uyumlu uygulamaya aktarır. Dosya cihazınıza indirilir, ardından sistem Paylaşma sayfası görünür.
- **Sil** — dosyayı bulut depolama alanınızdan kalıcı olarak kaldırır. **Bu işlem geri alınamaz.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Bağlı Bulut Depolamadaki Dosya İçin Daha Fazla Eylem" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Eylemler listesi mevcut ekran alanını aşarsa, ek seçeneklere ulaşmak için eylemler menüsünde aşağı kaydırın.

## Klasör Eylemleri

Bulut depolama alanınızdaki her klasör için, klasör başlığının yanındaki **"..."** simgesine dokunarak geniş bir eylemler dizisine erişebilirsiniz. Tüm eylemleri göremiyorsanız, daha fazlasını ortaya çıkarmak için aşağı kaydırın.

- **Tümünü Oynat** — geçerli çalar kuyruğunu seçilen klasördeki her öğeyle değiştirir.
- **Sonra Oynat** — klasörün tamamını çalar kuyruğunun başına ekler.
- **Daha Sonra Oynat** — klasör içeriğini çalar kuyruğunun sonuna ekler.
- **Müzik Kitaplığına Ekle** — klasörün içeriğini müzik kitaplığına dahil eder.
- **Çalma Listesine Ekle** — klasörün tamamını bir çalma listesine ekler. Ayrıca yeni bir çalma listesi oluşturma seçeneğiniz de vardır; adı klasör adından otomatik olarak doldurulur.
- **Favorilere Ekle** — hızlı erişim için klasörü favorilerinize ekler.
- **Çevrimdışı Modu Etkinleştir** — basit bir indirmenin ötesinde, yeni dosyalar için klasörü sürekli izler ve çevrimiçi göründükçe otomatik olarak indirir.
- **İndir** — klasörün tüm içeriğini çevrimdışı erişim için cihazınıza indirir.
- **Yeniden Adlandır** — klasörü doğrudan uzak depolama alanında yeniden adlandırır.
- **Taşı** — klasörü bulut depolama alanınızdaki farklı bir konuma taşır.
- **Arşivle (ZIP)** — klasör içeriğini tek bir ZIP dosyasında paketler (Premium özelliği).
- **Sil** — klasörü ve içeriğini bulut depolama alanınızdan kalıcı olarak kaldırır. **Bu işlem geri alınamaz.**

## Hızlı Erişim

Hızlı Erişim bölümü ekranın üst kısmında yer alır. Bağlı bulut hizmetlerindeki en sevdiğiniz ve son açtığınız dosyalara hızlı erişim sağlar. Buluttan bir dosya veya klasör her açtığınızda Son Açılanlar listesine eklenir. Bu listeyi temizlemek için Son Açılanlar'ı açın, Daha Fazla Eylem düğmesine dokunun ve Listeyi Sil seçeneğini belirleyin. Dizin yapısında derinlere gömülü klasörleri Favorilere de ekleyerek onlara hızla erişebilirsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Çevrimiçi Bağlantılar ve Hızlı Erişim" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Diğer Hizmetler

Bu bölüm, deneyiminizi zenginleştiren ek özellikleri gösterir. Şu anda uygulama **Last.fm** scrobbling'i destekler — bağlandığında oynatma istatistikleriniz otomatik olarak Last.fm hesabınıza gönderilir. Daha sonra Last.fm profilinizi ziyaret ederek dinleme analizlerini görüntüleyebilir ve kişiselleştirilmiş müzik önerileri alabilirsiniz. Ayrıntılı kurulum talimatları [burada](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm) mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm Bağlantısı" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
