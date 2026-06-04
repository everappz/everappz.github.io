---
date: 2020-01-01
title: 'Flacbox'
description: "Flacbox'u nasıl kullanacağınızı öğrenin — iPhone, iPad ve Mac için hi-res FLAC, DSD, ALAC ve FFmpeg destekli bulut müzik çalar. iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB ve DLNA'ya bağlanın. Yüksek çözünürlüklü ses akışı yapın ve indirin, meta verileri düzenleyin, sesli kitap dinleyin, Last.fm'e scrobble yapın, Apple CarPlay ve Ana Ekran widget'larını kullanın ve 10 bantlı ekolayzerı özelleştirin."
keywords: [
  "Flacbox kullanıcı kılavuzu", "Flacbox nasıl kullanılır", "hi-res müzik çalar iPhone", "FLAC çalar iPhone",
  "DSD çalar iOS", "ALAC çalar Mac", "kayıpsız müzik uygulaması", "bulut müzik çalar iPhone",
  "çevrimdışı FLAC çalar Mac", "müzik kütüphanesi yöneticisi", "ses etiketi düzenleyici",
  "CarPlay FLAC çalar", "Chromecast ses uygulaması", "AirPlay 2 müzik",
  "Flacbox widget'ları", "Flacbox CarPlay", "FFmpeg müzik çalar iOS",
  "sesli kitap çalar iPhone", "ses yer imleri iOS", "ses tonu düzeltme uygulaması",
  "ses çıkışı örnekleme hızı", "harici DAC iPhone", "USB DAC Mac",
  "Synology müzik uygulaması", "QNAP müzik uygulaması", "NAS müzik çalar iPhone",
  "WebDAV müzik çalar", "SMB müzik akışı", "DLNA müzik çalar",
  "iCloud Drive müzik", "Google Drive FLAC", "Dropbox FLAC çalar",
  "Wi-Fi Drive müzik transferi", "M3U çalma listesi içe aktarma", "Last.fm scrobbling"
]
tags: ["flacbox", "kılavuz", "hi-res", "FLAC", "FFmpeg", "bulut", "CarPlay", "widget'lar"]
---


### Flacbox Kılavuzuna Hoş Geldiniz

Flacbox, iPhone, iPad ve Mac için yüksek çözünürlüklü bir müzik çalardır. Favori bulut depolama alanınızı, NAS'ınızı ve medya sunucularınızı kendi kişisel akış hizmetinize dönüştürmenizi sağlar.

Flacbox, tek bir uygulamada oldukça geniş bir kaynak listesine bağlanır:

- **Kişisel bulut depolama:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘)
- **Kendi barındırılan sunucular:** Plex · Jellyfin · Emby · Subsonic (ve her Subsonic uyumlu sunucu — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (ve paylaşılan API aracılığıyla ownCloud) · Synology Drive · QNAP
- **NAS ve dosya paylaşım protokolleri:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (parola veya ortak anahtar kimlik doğrulaması) · NFS · DLNA / UPnP (oynatma ve indirme). Apple Time Capsule, Synology, QNAP, WD My Cloud, herhangi bir Linux Samba / NFS / SSH ana bilgisayarı veya Mac ya da Windows PC'nizdeki paylaşılan bir klasörle çalışır.
- **S3 uyumlu nesne depolama:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ve diğer S3-API uç noktaları
- **Yerel ağ keşfi:** Mevcut cihazlar bölümü, Wi-Fi ağınızdaki her Bonjour / mDNS hizmetini otomatik olarak listeler — Plex, Jellyfin, Emby sunucuları, Synology, QNAP, sürücü bağlı AirPort yönlendiricileri, Time Capsule — böylece IP adresi yazmadan bağlanabilirsiniz.

Çoğu müzik uygulaması Apple'ın yerleşik ses motoruna bağlı kalırken, Flacbox iOS'un desteklemediği formatları — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV ile normal MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC ailesini — çalabilmek için sistem kodekleriyle birlikte **FFmpeg** sunar. Yapılandırılabilir ses çıkışı örnekleme hızıyla (44,1 / 48 / 64 / 88,2 / 96 kHz), çok kanallı çıkışla (Mono → 5.1 → SDDS → ITU BS.775-1), IO tampon ayarı ve ses tonu düzeltmeyle Flacbox, çoğu tüketici müzik uygulamasının sunmadığı kontrolü audofillere verir.

### Akıcı Akış ve Çevrimdışı Oynatmanın Keyfini Çıkarın

Flacbox, akıcı akış için akıllı arabelleğe alma ve çevrimdışı kullanım için tüm Çalma Listelerini, Sanatçıları, Albümleri, Klasörleri veya tek tek parçaları cihazınıza çekebileceğiniz yerleşik bir indirme yöneticisine sahiptir. Depolama alanı azaldığında önbelleğe alınmış dosyaları tek dokunuşla temizleyip buluttan akışa devam edebilirsiniz. Klasörler, çalma listeleri, albümler ve sanatçılar için Çevrimdışı Mod, bulutta görünür görünmez yeni parçaları otomatik olarak senkronize eder, böylece çevrimdışı koleksiyonunuz her zaman güncel kalır.

### Otomatik Olarak Düzenlenmiş Müzik Kütüphanesi

Ses parçalarını içe aktardığınızda Flacbox, meta verilerini tarar ve bunları temiz bir Müzik Kütüphanesi'nde düzenler — Şarkılar, Oynatılmamış Şarkılar, Albümler, Albüm Sanatçıları, Sanatçılar, Türler ve Besteciler olarak gruplandırılmış. Saniyeler içinde herhangi bir şeyi bulmak için yerleşik aramayı kullanın, kaynağa göre filtreleyin (çevrimiçi bulut / çevrimdışı / cihaz) ve Plain / Grouped / Tabbed kütüphane düzenleri arasında seçim yapın. Karışık "çeşitli sanatçılar" derlemeleriyle kütüphaneler için Flacbox, gürültü olmadan doğru sonuçları ortaya çıkarmak için özel Tüm Albümler / Özel Albümler / Solo Albümler görünümleri sunar.

### Meta Verileri Düzeltin ve Müziğinizi Etiketleyin

Bozuk etiketler veya dağınık kodlamalarla karşılaşırsanız (riplanmış veya eski dosyalar için yaygın bir sorun), yerleşik ID3 Etiketleri Düzenleyici bunları temizleyebilir — manuel olarak veya otomatik MusicBrainz aramaları ile. Ayrıca bozuk karakter kodlamalarını normalleştirebilir (Windows PC'lerden gelen Kiril, Japonca veya Çince etiketler için harika), eksik albüm kapaklarını arayabilir ve değişiklikleri buluttaki orijinal dosyaya otomatik olarak geri yazabilirsiniz. Daha derin toplu düzenleme için yardımcı uygulamamız Evertag'ı yükleyin.

### Mac, PC veya NAS'tan Kolay Aktarım

Müziği bilgisayarınız ile iPhone veya iPad'iniz arasında şu araçlardan herhangi biriyle taşıyın: SMB, WebDAV, DLNA, Wi-Fi Drive (herhangi bir masaüstü tarayıcısında sürükle ve bırak), Lightning veya USB-C kablosu üzerinden iTunes / Finder Dosya Paylaşımı, USB flash sürücüler veya iXpand Flash Drives. SMB / WebDAV / DLNA / FTP / SFTP sunan Apple Time Capsule, WD My Cloud, Synology, QNAP veya başka bir NAS'a sahip misiniz? Bir kez bağlayın ve herhangi bir cihaz depolama alanı kullanmadan tüm kütüphanenizi akışa alın.

### Ekolayzer ile Sesinizi Özelleştirin

Flacbox, iPod tarzı ön ayarlarla (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz ve daha fazlası) 10 bantlı bir ekolayzer, bir ön yükselteç ve kendi ön ayarlarınızı kaydetme özelliği içerir. İster audiofil IEM çifti, ister HomePod mini, ister araç stereosu için ayarlıyor olun, sesi tam istediğiniz gibi şekillendirebilirsiniz.

### Sesli Kitap Dostu

Flacbox mükemmel bir sesli kitap çalardır — parça başına birden fazla yer imi, hassas oynatma hızı (0,02× - 3,00×), durduğunuz yere tam olarak geri dönmek için oynatmaya devam etme, özelleştirilebilir atlama süresi düğmeleri ve yatmadan önce yumuşakça kısılan bir uyku zamanlayıcısı. M4B bölüm işaretleri ve uzun dosyalar tam olarak desteklenmektedir.

### Her Yerde Akış Yapın — Arabanızda ve Ana Ekranınızda Dahil

AirPlay 2 aracılığıyla Apple TV / HomePod'a müzik akışı yapın, Google Chromecast hoparlörlerine ve Cast özellikli TV'lere gönderin ve Apple CarPlay ile her şeyi yola çıkın. Şu anda çalan parçayı bir bakışta görmek için iPhone ve iPad'de Ana Ekran widget'larını kullanın ve Last.fm scrobbling ile dinleme geçmişinizi uygulamalar arası taşıyın.

### Gizlilik ve Güvenlik

Flacbox yalnızca resmi SDK'ları ve her bulut sağlayıcısından OAuth tabanlı girişleri kullanır — şifreniz asla uygulamaya ulaşmaz. Erişim token'ları iOS Keychain'de şifreli olarak saklanır, tüm aktarımlar TLS korumalıdır ve bulut hesabınızdaki erişimi iptal etmek veya Flacbox'ı cihazdan kaldırmak her şeyi anında siler. Ekstra bir gizlilik katmanı için isteğe bağlı bir parola ile kütüphanenizi koruyun.

### Flacbox ile Başlarken

Bu kılavuz, iPhone, iPad ve Mac'te Flacbox'ın her bölümünü anlatır — bulut hizmetlerine bağlanmaktan, kütüphanenizi düzenlemekten, dosya aktarmaktan ve çalma listelerini yönetmekten, ekolayzerı ince ayarlamaya ve ses motorunu yapılandırmaya kadar. İhtiyaç duyduğunuz bölüme doğrudan geçmek için aşağıdaki kartları kullanın.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Gezinme" subtitle="iPhone'da Sekme Çubuğu, iPad ve Mac'te Sol Menü, mini oynatıcı, widget'lar, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Bağlantılar" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Müzik Kütüphanesi" subtitle="Şarkılar, albümler, sanatçılar, türler, besteciler — senkronizasyon, arama, meta veri düzenleme." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Çalma Listeleri" subtitle="Oluştur, M3U / M3U8 / CUE içe aktar, yeniden sırala ve M3U / CSV / TXT olarak dışa aktar." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Yerel Dosyalar" subtitle="Çevrimdışı müzik, USB sürücüler, Wi-Fi Drive, dosya yöneticisi, çevrimdışı klasörler." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Ses Çalar" subtitle="Hi-res çıkış, ekolayzer, ses tonu, yer imleri, AirPlay, Chromecast, hız, uyku zamanlayıcısı." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Ayarlar" subtitle="Ses motoru, kütüphane, dosya yöneticisi, CarPlay, widget'lar, kişiselleştirme, dil, yedekleme." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="SSS" subtitle="Flacbox hakkındaki en sık sorulan 50 soruya yanıt bulun." >}}

{{< /cards >}}
