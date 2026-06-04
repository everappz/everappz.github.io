---
title: "Dosyalar"
date: 2020-02-01
lastmod: 2026-06-01
description: "Evervideo'da iPhone, iPad ve Mac'te Dosyalar sekmesini nasıl kullanacağınızı öğrenin. Bulut hizmetlerini, NAS cihazlarını, medya sunucularını ve RTSP akışlarını tek bir yerde bağlayın. Çevrimdışı videoları, aktarım kuyruğunu, indirmeleri, Wi-Fi Drive'ı, iTunes / Finder Dosya Paylaşımını ve USB sürücüleri yönetin. iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA ve S3 uyumlu depolamayı kapsar."
keywords: [
  "Evervideo dosyalar", "Evervideo bağlantılar", "Evervideo yerel dosyalar",
  "iPhone bulut video kurulumu", "Google Drive video bağlantısı", "SMB video akışı",
  "WebDAV video oynatıcı iOS", "DLNA video iPhone", "NAS video akışı",
  "Wi-Fi Drive video aktarımı", "Evervideo iTunes Dosya Paylaşımı", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo çevrimdışı mod video", "Evervideo aktarım kuyruğu",
  "Evervideo dosya yöneticisi", "Evervideo Documents klasörü",
  "video oynatıcı Synology", "video oynatıcı QNAP",
  "video oynatıcı Apple Time Capsule", "USB DAC video",
  "iXpand video oynatıcı", "S3 video oynatıcı"
]
tags: ["rehber", "evervideo", "dosyalar", "bağlantılar", "bulut", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Dosyalar sekmesi, Evervideo'nun hepsi bir arada dosya yöneticisidir. Bulut depolamayı yerel dosyalardan farklı sekmelere ayıran çoğu video uygulamasının aksine, Evervideo her ikisini de tek, kaydırılabilir bir ekranda birleştirir; böylece sekmeler arasında geçiş yapmadan Plex sunucusundan bulut klasörüne ve iPhone'unuzun Documents klasörüne geçebilirsiniz.

Dosyalar sekmesi, ekranınızda bu sırayla görünen net bölümlere ayrılmıştır:

- **Hızlı Erişim** — en son açtığınız dosya ve klasörler için son kullanılanlar ve favoriler.
- **Bu Uygulamadaki Dosyalar** — Evervideo'nun korumalı Documents klasöründe bulunanlar.
- **Bu iPhone / iPad / Mac'teki Dosyalar** — sistem dosya seçici aracılığıyla cihazınızın diğer yerlerindeki videolar.
- **Bulut Depolama** — bağladığınız her bulut hesabı, NAS ve medya sunucusu.
- **Mevcut Cihazlar** — yerel ağınızda Bonjour / mDNS ile otomatik olarak keşfedilen sunucular ve sürücüler.

Dosyalar ekranının sağ üst köşesinde bir Aktarımlar düğmesi (dönen oklar simgesi) bulunur. Tüm kaynaklarınızdaki her indirmeyi ve yüklemeyi izlediğiniz Aktarım Kuyruğunu açmak için dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bağlı depolardaki Evervideo dosyaları" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Bulut Depolamaya Bağlan

Dosyalar sekmesinin Bulut Depolama bölümü, bağlı her hesabın, NAS'ın, medya sunucusunun ve akışın bulunduğu yerdir — yan yana, tek bir kaydırılabilir listede.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dosyalar Sekmesindeki Evervideo Bulut Depolama Bölümü" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- **Dosyalar** sekmesini açın.
- **Bulut Depolama** bölümüne kaydırın.
- Menüden **Bulut depolamaya bağlan** seçeneğine dokunun.
- Listeden bir bulut depolama hizmetini seçin.
- Bulut sağlayıcısı tarafından sağlanan resmi yetkilendirme sayfasında kimlik bilgilerinizi girin, ardından **Tamamlandı** seçeneğine dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Bulut Depolama Hizmeti Bağlama" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Sorunlarla karşılaşırsanız internet bağlantınızı ve giriş / şifrenizi kontrol edin. Uygulamanın Premium sürümünde sınırsız sayıda hizmet ekleyebilirsiniz; ücretsiz sürüm en fazla üçü destekler.

## Desteklenen Bulut Depolama Hizmetleri, Medya Sunucuları ve Protokoller

Evervideo, videolarınız için istisnai derecede geniş bir kaynak yelpazesini destekler. Aşağıdakilerin tümü tek bir Bulut depolamaya bağlan akışından çalışır.

**Kişisel bulut depolama:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘)

**Kendi barındırılan medya sunucuları:** Plex · Jellyfin · Emby · Subsonic (ve her Subsonic uyumlu sunucu — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (ve paylaşılan API aracılığıyla ownCloud) · Synology Drive · QNAP

**NAS ve dosya paylaşım protokolleri:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, parola veya genel anahtar doğrulaması) · NFS · DLNA / UPnP (oynatma ve indirme)

**Canlı ve IP kamera akışları:** RTSP — Evervideo'yu herhangi bir `rtsp://` URL'sine yöneltin ve doğrudan oynar. Güvenlik kameraları, IPTV akışları, zil kameralar, bebek monitörleri ve benzer canlı kaynaklar için mükemmel.

**S3 uyumlu nesne depolama:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ve diğer S3-API uç noktaları.

**Cihazdaki kütüphaneler:** Photos kütüphanesi (tüm videolar, ekran kayıtları, fotoğraf albümleri) ve Music uygulaması kütüphanesi (Albümler, Türler, Oynatma Listeleri) — her ikisi de Medya Kütüphanesi'nde görünür; bu yüzden hiçbir şey kopyalamanız gerekmez.

**Yerel ağ keşfi:** Mevcut Cihazlar bölümü Wi-Fi ağınızdaki her Bonjour / mDNS hizmetini otomatik olarak listeler — Plex, Jellyfin, Emby sunucuları, Synology, QNAP, bağlı sürücülerle AirPort router'lar, Apple Time Capsule — böylece IP adresi girmeden bağlanmak için dokunabilirsiniz.

Her bağlantı, OAuth tabanlı yetkilendirme ile hizmetin resmi SDK'sını veya açık protokolünü kullanır. Aynı hizmetin birden fazla hesabını bağlayabilirsiniz (örneğin, iki Google Drive hesabı veya hem Plex hem de Jellyfin sunucusu) ve bunları Bulut Depolama bölümünde yan yana görebilirsiniz.

## Güvenlik ve Gizlilik

Evervideo, bağlı bulut hizmetleriyle etkileşim için yalnızca resmi SDK'ları ve güvenli bağlantıları kullanır. Giriş bilgileriniz ve parolanız uygulamaya erişilemez — tüm aktarımlar TLS şifrelidir.

Giriş bilgilerinizi ve parolanızı girdiğinizde, uygulama size bulut hizmet sağlayıcısı tarafından sağlanan resmi yetkilendirme sayfasını gösterir ve yetkilendirme işleminin tamamı uygulamanın dışında gerçekleşir. Bulut hizmet sağlayıcısı, başarılı yetkilendirmenin ardından uygulamaya bir auth-token gönderir ve bu token API çağrıları yapmak için kullanılır.

Auth-token, üçüncü taraf uygulamaların adınıza bulut depolamayla etkileşime girmesine olanak tanıyan dijital bir anahtardır. Token, cihazınızda Apple'ın güvenli sistem depolamasında (Keychain) saklanır; bu depolama beklemede şifrelenir ve cihaz parola veya biyometrik kilitle korunur. Bağlı bulut hizmetlerinden cihazınıza dosya indirebilirsiniz; bu dosyalar uygulamanın Documents dizinine yerleştirilir ve yerleşik dosya yöneticisi kullanılarak herhangi bir zamanda kaldırılabilir.

Uygulama, bağlı bulut hesaplarınızdan herhangi bir bilgiyi Everappz, reklamverenler veya herhangi bir üçüncü tarafla paylaşmaz. Web tarayıcınızda hesap ayarları sayfasını açarak bulut hesabınıza erişimi istediğiniz zaman iptal edebilirsiniz.

## Auth-Token'ı Reddet

Bir auth-token'ı iptal etmek için web tarayıcınızda bulut hesabınıza giriş yapın ve güvenlik veya bağlı uygulamalar sayfasına gidin. Orada bulut hesabınıza bağlı her üçüncü taraf uygulamayı bulabilir ve artık kullanmak istemediğiniz herhangi birini kaldırabilirsiniz. Google hesapları için ayrıntılı talimatlar [burada](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) mevcuttur.

Bulut hesabını uygulamanın içinden de bağlantısını kesebilirsiniz — bunu yaptığınızda, auth-token cihazınızdan hemen silinir. Uygulamayı cihazınızdan kaldırırsanız, tüm indirilen veriler ve erişim token'ları otomatik olarak onunla birlikte kaldırılır.

## Bulut Depolama Bağlantısını Kes veya Yapılandırmayı Değiştir

- **Bulut depolama seçeneklerine erişin** — Dosyalar sekmesinin **Bulut Depolama** bölümünde bağlı hizmeti bulun.
- **Hizmet başlığının yanındaki "..." düğmesine dokunun** ek seçenekleri açmak için:
  - **Yeniden Adlandır** — bulut hizmetinin listenizdeki görünen adını değiştirin.
  - **Ayarlar** — yapılandırmayı veya kimlik doğrulama verilerini değiştirin. Bazen yetkilendirme token'ı süresi dolmuşsa bağlı bulut hizmetini yeniden yetkilendirmeniz gerekebilir.
  - **Bağlantıyı Kes** — uygulama ile bulut hizmeti arasındaki bağlantıyı tamamen kesin. Bu, medya kütüphanenizden söz konusu hizmetle ilişkili tüm videoları kaldırır, ancak sunucuda dokunulmadan bırakır.

## Bilgisayara veya NAS'a Bağlanın

SMB, WebDAV, FTP / FTPS, SFTP, NFS veya DLNA protokolünü kullanarak bilgisayarınıza, kişisel NAS'ınıza veya diğer ağ cihazına bağlanabilirsiniz. Bu, Mac, Windows PC, Synology, QNAP, Apple Time Capsule veya WD My Cloud Home'da bulunan mevcut bir ev medya kütüphanesini hiçbir şeyi kopyalamadan Evervideo'ya getirmenin en kolay yoludur.

### SMB Kullanarak Bilgisayara Bağlanın

- **Bulut depolamaya bağlan → SMB** seçeneğine dokunun.
- Bilgisayarın IP adresini ve paylaşılan klasör adını `smb://computer-ip-address/shared-folder-name` biçiminde girin.
- Protokol sürümünü seçin: **Auto**, **SMB1** veya **SMB2**.
- Giriş bilgilerinizi ve parolanızı girin (gerekirse).
- **Tamamlandı** seçeneğine dokunun.

Bağlantı başarılıysa, paylaşım Bulut Depolama bölümünde görünür. SMB kullanarak Mac veya PC'nizi nasıl bağlayacağınıza dair tam bir öğretici [burada](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) mevcuttur.

### WebDAV Kullanarak NAS'a Bağlanın

Tüm adımlar URL alanı dışında SMB ile aynıdır. Sunucu SSL destekliyorsa `http://server-name` veya `https://server-name` kullanın. WebDAV; Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home ve WebDAV uç noktasına sahip diğer sunucularla çalışır.

WebDAV hakkında tam bir öğretici [burada](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) mevcuttur.

### DLNA / UPnP Üzerinden Bağlanın

Windows PC veya NAS'ınızdaki bir medya kütüphanesini DLNA / UPnP protokolünü kullanarak paylaşın ve [burada](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) açıklandığı gibi Evervideo'da erişin. DLNA geniş çapta desteklenir, ancak yalnızca video oynamanıza veya indirmenize izin verir — DLNA sunucusuna dosya yükleyemez veya yeni klasörler oluşturamazsınız.

### FTP, FTPS veya SFTP Kullanarak Bağlanın

Evervideo klasik dosya aktarım protokollerini de destekler. FTP veya FTPS üzerinden bir sunucuya bağlanmak için Bulut depolamaya bağlan → FTP seçeneğine dokunun, `ftp://server-name` (veya şifreli bağlantı için `ftps://server-name`) biçiminde ana bilgisayar URL'sini girin, giriş bilgilerinizi ve parolanızı sağlayın, ardından Tamamlandı seçeneğine dokunun. SFTP (SSH File Transfer Protocol) için bunun yerine SFTP'yi seçin ve parola ya da SSH anahtar çifti sağlayın.

### NFS Paylaşımına Bağlanın

Evervideo, NFS (Network File System) desteği içerir — SMB yerine NFS üzerinden video kütüphanelerini açığa çıkarmayı tercih eden Linux ana bilgisayarlar, BSD sunucuları ve NAS cihazları için kullanışlıdır. Bulut depolamaya bağlan menüsünde NFS'yi seçin, sunucu adresini ve dışa aktarılan yolu girin ve Tamamlandı seçeneğine dokunun.

## Plex Media Server'a Bağlanın

Evervideo, doğrudan bir Plex Media Server'a bağlanabilir ve Film, TV Dizisi ve Ev Videoları kütüphanelerinize göz atabilir. Bulut depolamaya bağlan → Plex seçeneğine dokunun, Plex hesabınızla oturum açın, bir sunucu seçin ve kütüphane bulut hizmetlerinizin yanında görünür. Aynı yerel ağdaki Plex sunucuları da Mevcut Cihazlar bölümünde otomatik olarak keşfedilir.

## Jellyfin veya Emby Sunucusuna Bağlanın

Hem Jellyfin (açık kaynak) hem de Emby (ticari) medya sunucuları Evervideo'da yerel olarak çalışır. Bulut depolamaya bağlan → Jellyfin veya Emby seçeneğine dokunun, sunucu URL'nizi (genellikle `http://server-ip:8096` gibi bir şey) ve kimlik bilgilerini girin ve kütüphaneniz akışa hazır.

## Subsonic veya Navidrome Sunucusuna Bağlanın

Evervideo, Subsonic API'sini konuşur, yani Subsonic, Navidrome ve diğer tüm Subsonic uyumlu sunucularla — Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) ve Ampache dahil — çalışır. Bulut depolamaya bağlan → Subsonic seçeneğine dokunun, sunucu URL'sini ve kimlik bilgilerini girin ve kütüphane Bulut Depolama bölümünde görünür.

## RTSP Akışı Bağlayın (IP Kameraları, Canlı TV, IPTV)

Evervideo'nun yerel RTSP desteği vardır, bu nedenle herhangi bir RTSP kaynağına yönlendirebilirsiniz — güvenlik kameraları, zil kameraları, IPTV sağlayıcıları, bebek monitörleri, yayın beslemeleri — ve Evervideo akışı canlı olarak çeker ve çözer. Çevrimiçi Bağlantılar → Bağlantı ekle seçeneğine dokunun, tam URL'yi (`rtsp://camera-ip:port/stream-path`) yapıştırın, gerekirse giriş bilgilerini ve parolayı sağlayın ve Tamamlandı seçeneğine dokunun.

## S3 Uyumlu Nesne Depolamaya Bağlanın

Bulut nesne depolaması kullanan kendi barındıranlar ve güçlü kullanıcılar için Evervideo, S3 uyumlu bir bağlayıcı içerir. Bulut depolamaya bağlan → S3 depolama seçeneğine dokunun, ardından uç nokta URL'sini, bölgeyi, erişim anahtarını, gizli anahtarı ve kova adını girin. Bu; AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ve diğer S3-API uç noktalarıyla çalışır.

## Mevcut Cihazlar

Bu bölüm, yerel ağınızda Bonjour / mDNS keşfi aracılığıyla Evervideo'dan bağlanabileceğiniz her cihazı gösterir — Plex, Jellyfin, Emby sunucuları, Synology, QNAP, bağlı sürücülerle AirPort router'lar, Apple Time Capsule vb. Bağlantı kurmak için:

- Dosyalar sekmesinde Mevcut Cihazlar bölümüne kaydırın.
- Bağlanmak istediğiniz cihaza dokunun.
- Gerekirse bağlantıyı tamamlamak için giriş bilgilerinizi girin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo yerel ağdaki mevcut cihazlar" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive, herhangi bir masaüstü tarayıcı, Finder veya File Explorer aracılığıyla bilgisayarınızdan iOS cihazınıza kablosuz olarak dosya aktarmanızı sağlar. Cihazınızın ve bilgisayarınızın aynı Wi-Fi ağında olması gerekir.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive'ı Etkinleştirin

- Dosyalar sekmesinde, Wi-Fi Drive ana ekranını açmak için Bulut Depolama → Wi-Fi Üzerinden Bağlan seçeneğine kaydırın.
- (İsteğe bağlı) Gömülü web sunucusu için kullanıcı adı ve parola belirleyin.
- Wi-Fi Drive'ı Başlat seçeneğine dokunun.

### Bilgisayarınızdan Wi-Fi Drive'a Erişin

- Bilgisayarınızda bir web tarayıcısı açın (Chrome, Firefox, Safari vb.).
- Uygulama tarafından gösterilen URL'yi girin.
- Bilgisayarınızdan web sayfasına dosyaları sürükleyip bırakın — iOS cihazınıza aktarılmaya başlayacaklar.

Wi-Fi Drive'ı macOS'ta **Finder**'a (Git → Sunucuya Bağlan…) veya Windows'ta File Explorer'a (Ağ Sürücüsü Eşle…) doğrudan bağlayarak iPhone veya iPad'inizi normal bir ağ sürücüsü olarak kullanabilirsiniz.

Ayrıntılı talimatlar [burada](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) mevcuttur.

## iTunes / Finder Dosya Paylaşımı

iTunes Dosya Paylaşımı (macOS Catalina ve sonrasında artık Finder Dosya Paylaşımı) Lightning veya USB-C kablo kullanarak dosya aktarmanızı sağlar. Cihazı bağlayın, Mac'te Finder'ı (veya Windows'ta iTunes'u) açın, uygulama listesinde Evervideo'yu bulun ve paylaşılan klasörüne dosya kopyalayın.

## USB Flash Sürücü veya SD Kart Bağlayın

Lightning-to-USB / USB-C adaptörü veya kart okuyucu aracılığıyla iPhone, iPad veya Mac'inize USB sürücüsü veya SD kart takın. Dosyalar → Bu iPhone'daki Dosyalar → Klasör Aç seçeneğini açın, sürücüye gidin ve bir video dosyası veya klasör seçin. Evervideo, dosyaları dahili depolamaya kopyalamadan doğrudan sürücüden oynatır — çok büyük 4K kütüphaneler için kullanışlıdır.

## Bağlı Depolarda Klasör Gezintisi

Dosya gezginini açmak için herhangi bir bağlı bulut hizmetine dokunun. Klasörler mevcut olduğunda video küçük resimleri gösterir ve bir videoya dokunmak, dosyanın geri kalanı arka planda akışa devam ederken oynatmayı hemen başlatır.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo bağlı depolarda klasörlere göz atma" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Hızlı Erişim

Hızlı Erişim bölümü, Dosyalar sekmesinin en üstünde bulunur. Hem bulut hizmetlerinden hem de cihazdaki depolamadan favori ve son açılan dosya ve klasörlerinize hızlı erişim sağlar. Buluttan bir dosya veya klasör her açtığınızda, Son Açılanlara listenize eklenir. Dizin yapısını gezmeden hızlıca erişmek için derine gömülü klasörleri Favoriler olarak işaretleyebilirsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo çevrimiçi bağlantılar ve hızlı erişim" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Bu Uygulamadaki Dosyalar

Bu bölüm, Evervideo'nun korumalı Documents dizininde depolanan dosya ve klasörleri gösterir — buluttan indirdiğiniz, Wi-Fi Drive aracılığıyla aktardığınız, Finder Dosya Paylaşımı ile kopyaladığınız veya başka bir uygulamadan içe aktardığınız her şey.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo bu uygulamadaki dosyalar" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Documents Klasörü

Documents klasörü, Bu Uygulamadaki Dosyalar içindeki her şeyin köküdür. Alt klasörler oluşturabilir, dosyaları yeniden adlandırabilir, taşıyabilir ve istediğiniz gibi gruplandırabilirsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo yerel dosyalar — Documents klasörü" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Bu iPhone / iPad / Mac'teki Dosyalar

Bu bölüm, farklı uygulamalarda cihazınızda bulunan videoları gösterir. Bunları sistem dosya seçici kullanarak Evervideo'ya aktarabilirsiniz:

- Belirli dosyaları seçmek için Dosyaları Aç… seçeneğine dokunun.
- Tüm bir klasörü seçmek için Klasör Aç… seçeneğine dokunun.

Hiçbir şeyi kopyalamadan iCloud Drive veya bağlı USB sürücüsündeki bir klasörle çalışmak için — okuma / yazma erişimiyle cihazınızdaki bir klasöre bağlantı oluşturmak için Klasör Bağla seçeneğini de kullanabilirsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo bu cihazdaki dosyalar" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Özel Klasörler

Dosyalar sekmesinde Evervideo'nun otomatik olarak oluşturduğu ve kullandığı birkaç özel klasör göreceksiniz:

- **İndirilenler** — buluttan indirilen her dosya varsayılan olarak burada görünür. Ayarlar → Dosya Yöneticisi → İndirilen Dosyaları Şuraya Kaydet seçeneğinden özelleştirin.
- **Oynatıcı Önbelleği** — medya oynatıcısı önbelleği. Varsayılan olarak oynatıcı, sorunsuz oynatma için yaklaşan videoları indirir. Uygulama ayarlarından önbelleği devre dışı bırakabilir veya bu klasörü silebilirsiniz.
- **iCloud** — bu klasördeki dosyalar, aynı iCloud hesabına bağlı tüm cihazlarınızda senkronize edilir.
- **Çevrimdışı klasörler** — bir klasörü, oynatma listesini, albümü veya türü çevrimdışı olarak kullanılabilir şekilde işaretlediğinizde, dosyalar bu klasöre indirilir.

## Üst Araç Çubuğu

Gezinme çubuğunun altında bulunan üst araç çubuğu, aşağıya kaydırma hareketiyle gösterebileceğiniz veya gizleyebileceğiniz çeşitli eylemler sunar:

- **Ara** — geçerli klasörde veya bölümde arama yapın.
- **Oynatmaya Devam Et** — ayarlarda etkinleştirilmişse, geçerli klasör için oynatıcı kuyruğunu ve son video konumunu geri yükler.
- **Tümünü Oynat** — geçerli klasörü ve alt klasörlerini tara ve dosyaları oynatıcı kuyruğuna ekle.
- **Tümünü Karıştır** — Tümünü Oynat gibi, ancak eklemeden önce karıştırır.

## Klasör Seçenekleri

Bir klasör açtığınızda, bu eylemler için sağ üst köşedeki **"..." düğmesine** dokunun:

- **Seçmek** — dosya seçim modunu etkinleştirin.
- **Yeni Klasör** — geçerli klasörde yeni bir klasör oluşturun.
- **Çevrimdışı Modu Etkinleştir** — geçerli klasör için çevrimdışı senkronizasyonu açın. Çevrimiçi olarak eklenen yeni dosyalar otomatik olarak indirilir.
- **Dosyaları Yükle** — cihazınızdaki dosyaları çevrimiçi klasöre yükleyin.
- **Ara** — klasör içinde arama yapın.
- **Sırala** — dosyaları ada, boyuta, değiştirilme tarihine veya meta veriye göre sıralayın.
- **Izgaralı / Liste Görünümü** — tablo görünümü ile küçük resim görünümü arasında geçiş yapın. Küçük resim görünümü büyük video posteri önizlemelerini gösterir.

## Seçim Modu

Sağ üst köşedeki **"..."** seçeneğine dokunun ve seçim moduna girmek için **Seçmek** seçeneğini seçin. Her dosya ve klasörün yanında onay kutuları görünür. Bir veya birkaç öğe seçmek için dokunun, ardından toplu eylemler gerçekleştirin: Sonra Oynat, Daha Sonra Oynat, Medya Kütüphanesine Ekle, Oynatma Listesine Ekle, Kopyala, Yükle, Taşı, Yeniden Adlandır veya Sil.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo dosya yöneticisinde seçim modu" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Bağlı bulut depolamayı salt okunur olarak değerlendirmeyi tercih ederseniz (kazara silmeleri önlemek için), tüm yıkıcı işlemleri UI'dan gizlemek için Ayarlar → Dosya Yöneticisi → Çevrimiçi Dosyaları Düzenle → Kapalı seçeneğini etkinleştirin.

## Dosya Eylemleri

Eylemler menüsünü açmak için bir dosyanın başlığının yanındaki **"..."** simgesine dokunun:

- **Sonra Oynat** — dosyayı oynatıcı kuyruğunun en üstüne ekleyin.
- **Daha Sonra Oynat** — dosyayı oynatıcı kuyruğunun en altına ekleyin.
- **Medya Kütüphanesine Ekle** — dosyayı Album ve Türe göre düzenlenmiş medya kütüphanenize dahil edin.
- **Oynatma Listesine Ekle** — dosyayı mevcut bir oynatma listesine ekleyin veya yeni bir tane oluşturun.
- **Etiketleri Düzenle** — meta verileri değiştirmek için yerleşik etiket düzenleyicisini açın. Çevrimiçi dosyalar için dosya geçici olarak indirilir, düzenlenir ve onayladıktan sonra yeniden yüklenir.
- **Favorilere Ekle** — hızlı erişim için dosyayı favoriler listesine ekleyin.
- **İndir** — çevrimdışı kullanım için dosyayı veya klasörü cihazınıza indirin.
- **Yeniden Adlandır** — dosyayı doğrudan uzak depolama üzerinde yeniden adlandırın.
- **Taşı** — dosyayı bulut depolama alanınızdaki farklı bir klasöre taşıyın.
- **Arşive Ekle** — dosyayı tek bir ZIP dosyasına paketleyin (Premium özellik).
- **Şurada Aç** — sistem Paylaş sayfası aracılığıyla dosyayı başka uyumlu bir uygulamaya aktarın.
- **Sil** — dosyayı kalıcı olarak kaldırın. **Bu eylem geri alınamaz.**

## Klasör Eylemleri

Bulut depolamanızdaki her klasör için, klasör başlığının yanındaki **"..."** simgesine dokunarak birçok eylem kullanılabilir.

- **Tümünü Oynat** — geçerli oynatıcı kuyruğunu klasördeki her videoyla değiştirin.
- **Sonra Oynat / Daha Sonra Oynat** — klasörün tamamını kuyruğa ekleyin.
- **Medya Kütüphanesine Ekle** — klasörün içeriğini medya kütüphanenize dahil edin.
- **Oynatma Listesine Ekle** — klasörün tamamını bir oynatma listesine ekleyin.
- **Favorilere Ekle** — klasörü favorilerinize ekleyin.
- **Çevrimdışı Modu Etkinleştir** — basit bir indirmenin ötesinde, bu klasörü yeni dosyalar için sürekli izler ve çevrimiçi göründüklerinde otomatik olarak indirir.
- **İndir** — çevrimdışı erişim için klasörün tüm içeriğini cihazınıza indirin.
- **Yeniden Adlandır / Taşı** — klasörü uzak depolama üzerinde yeniden adlandırın veya taşıyın.
- **Arşive Ekle** — klasör içeriğini bir ZIP dosyasına paketleyin (Premium özellik).
- **Sil** — klasörü ve içeriğini kalıcı olarak kaldırın. **Bu eylem geri alınamaz.**

## Aktarım Kuyruğu

Dosyalar sekmesinin sağ üst köşesinde bir **Aktarımlar** düğmesi (dönen oklar simgesi) bulunur. Tüm kaynaklarınızdaki her aktif indirme ve yüklemenin gerçek zamanlı ilerleme, hız ve dosya başına ETA ile bulunduğu Aktarım Kuyruğunu açmak için dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo dosya aktarım kuyruğu" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Başarısız aktarımları duraklatabilir, devam ettirebilir, yeniden deneyebilir, belirli indirmelere öncelik vermek için öğeleri yeniden düzenleyebilir veya tek tek iptal edebilirsiniz. Ayrıca Ayarlar → Dosya Yöneticisi'nden aktarım kuyruğu hızını (maksimum paralel görevler), ağ türünü (yalnızca Wi-Fi veya Wi-Fi + Hücresel) ve arka plan aktarımlarını ayarlayabilirsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo dosya aktarım kuyruğundaki eylemler" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Çevrimdışı Mod ve Senkronize Çevrimdışı Klasörler

Çevrimdışı mod, internete bağlı olmadığınızda bile favori videolarınızı izlemenizi sağlayan kullanışlı bir özelliktir. Herhangi bir klasör, oynatma listesi, albüm veya tür için çevrimdışı modu etkinleştirdiğinizde, söz konusu koleksiyondaki tüm dosyalar çevrimdışı oynatma için cihazınıza otomatik olarak indirilir. Çevrimdışı Klasörler bölümünde görünürler.

Uzak sunucuya yeni dosyalar eklediğinizde, bunlar da otomatik olarak indirilir — bu nedenle çevrimdışı koleksiyonunuz hiçbir şey yapmadan güncel kalır. Manuel olarak yeniden senkronize etmek için çevrimdışı bir klasörün sağ üst köşesindeki üç noktaya dokunun ve Senkranize Et seçeneğini seçin.

Senkronizasyon zaman aşımını Ayarlar → Dosya Yöneticisi → Senkrone edilmiş çevrimdışı klasörler → Zaman Aralığı seçeneğinden ayarlayabilirsiniz.

Ayrıntılı talimatlar [burada](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/) mevcuttur.

## Kişiselleştirme

Ayarlar → Kişiselleştirme'de Dosyalar sekmesinin nasıl sunulacağını yapılandırabilirsiniz:

- **Dosyalar Ekranı Stili** — Düz Menü (klasör listesini doğrudan gösterir) veya Gruplandırılmış Menü (içeriği kategoriye göre gruplar — Hızlı Erişim, Özel Klasörler, Bulut Depolama vb.).
