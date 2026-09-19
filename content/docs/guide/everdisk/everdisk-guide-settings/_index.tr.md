---
title: "Ayarlar"
date: 2026-08-20
description: "Everdisk ayarlarının eksiksiz bir turu: cihaz profili (ad ve avatar), beş bağlantı sunucusu, erişim denetimleri, SMB şifrelemesi (SMB3/AES), fotoğraf ve video kalitesi, özel portlar, DLNA küçük resimleri, ağ ve aktarım seçenekleri, dosya yöneticisi seçenekleri ve Premium."
keywords: ["Everdisk ayarları", "cihaz adı avatar", "bağlantı sunucuları", "fotoğraf video kalitesi", "özel portlar HTTP WebDAV FTP", "DLNA küçük resimleri", "paralel aktarımlar", "dosyaları kalıcı olarak sil", "küçük resim önbelleği", "Everdisk Premium"]
tags: ["everdisk", "guide", "settings"]
readingTime: 12
---


**Ayarlar** sekmesi her şeyi üç ana alanda toplar - **Paylaşım**, **Ağ** ve **Dosya Yöneticisi** - ayrıca Premium, geri bildirim ve yasal bağlantılar. Bu sayfa her ayarı ve varsayılanını açıklar.

## Premium

Ayarlar'ın en üstünde Premium durumunuzu ya da bir **Tüm özelliklerin kilidini aç** düğmesini görürsünüz. Everdisk birkaç sınırla ücretsiz kullanılır; tek seferlik bir **Premium Lifetime** satın alımı bunları kaldırır. Bu sayfanın sonundaki [Premium](#premium-lifetime) bölümüne bakın.

## Paylaşım ayarları

### Genel

- **Cihaz paylaşımını otomatik olarak başlat** - uygulamayı açar açmaz paylaşmaya başlayın. *(Premium.)*
- **Belgeler Klasörünü Paylaş** - uygulamanın kendi Belgeler klasörünü paylaşın. Varsayılan olarak açık.
- **Bağlantı kesilmeden önce bildir** - sistem uygulamayı arka planda askıya almadan önce size uygulamayı yeniden açmanızı hatırlatın. Varsayılan olarak kapalı; ilk seferinde bildirim izni ister.

### Cihaz Profili

- **Cihaz Adı** - diğer cihazların ağda sizin için gördüğü ad. Düzenlemek için dokunun. *(Premium.)*
- **Cihaz Avatarı** - cihazınız için simge ve arka plan rengi. Bir simge, bir arka plan geçişi seçebilir ya da **Fotoğraflardan bir avatar seçebilirsiniz**. *(Premium.)*
- **Adı ve Avatarı Yeniden Oluştur** ve **Avatarı Yeniden Oluştur** - yeni bir rastgele ad ve/veya avatar alın. *(Ücretsiz.)*

### Erişim

- **Giriş** ve **Parola** - Tarayıcı, Bilgisayar ve Diğer Uygulamalar bağlantıları için oturum açmayı zorunlu kılın.
- **Dosya Düzenleme** - bağlı cihazların yüklemesine, yeniden adlandırmasına ve silmesine izin verin. Varsayılan olarak açık.
- **Engellenen Cihazlar** - engellediğiniz cihazları yönetin.

Ayrıntılar için bkz. [Erişim ve Gizlilik](/docs/guide/everdisk/everdisk-guide-access).

### Bağlantılar

Her sunucuyu açın ya da kapatın. Beşi de varsayılan olarak açıktır ve her birinin bağlantı talimatlarını içeren bir bilgi (ⓘ) düğmesi vardır:

- **TV ve Medya Merkezi** (DLNA)
- **Tarayıcı** (HTTP)
- **Bilgisayar** (WebDAV)
- **Bilgisayar (Gelişmiş)** (SMB) - Mac, Windows ve Linux için bir ağ sürücüsü; bir Mac'te Finder kenar çubuğunda kendiliğinden görünür. Şifrelenebilen tek bağlantı.
- **Diğer Uygulamalar ve Cihazlar** (FTP)

### Fotoğraflar

- **Biçim** - Orijinal ya da En Uyumlu (JPEG).
- **Kalite** - Orijinal, Yüksek, Orta ya da Düşük.

Orijinal dışındaki herhangi bir şey, fotoğrafları paylaşılırken dönüştürür ve bu daha yavaştır. Dönüştürme bir Premium özelliktir.

### Videolar

- **Biçim** - Orijinal ya da En Uyumlu (H.264 MP4).
- **Kalite** - Orijinal, Yüksek, Orta ya da Düşük.

Fotoğraflarla aynı fikir: en hızlısı Orijinaldir ve dönüştürme Premium'dur. Eski bir TV bir videoyu oynatamıyorsa kaliteyi düşürün.

### Gelişmiş

- **HTTP Portu** (varsayılan 80), **WebDAV Portu** (varsayılan 8080), **SMB Portu** (varsayılan 4455), **FTP Portu** (varsayılan 2121). DLNA portunu otomatik olarak seçer. *(Portları değiştirmek Premium'dur; ücretsiz kullanıcılar değerleri görebilir.)*

### SMB Şifrelemesi

- **SMB şifrelemesi iste** - her SMB aktarımını **SMB3 şifrelemesiyle (AES)** şifreleyin; böylece ağdaki başka hiç kimse dosyalarınızı okuyamaz. Varsayılan olarak kapalı. Yukarıda ayarlanmış bir **giriş ve parola** (şifreli bağlantılar anonim olamaz) ve SMB3'ü destekleyen bir istemci gerektirir; örneğin modern bir Mac'teki Finder ya da Windows 10 ve sonrası. Değişiklikler bir sonraki paylaşım başlatmanızda etkili olur. *(Premium.)*

### DLNA Küçük Resimleri

- **Küçük Resimleri Göster** - TV'ler için önizleme görüntüleri yayınlayın. Varsayılan olarak açık (ücretsiz).
- Hangi boyutların yayınlanacağını seçin: **Küçük (160px)**, **Orta (640px)**, **Büyük (1024px)**, **Çok Büyük (4096px)**.

## Ağ ayarları

- **Dosya Aktarımları** - indirmeler ve yüklemeler için yalnızca **Wi-Fi** ya da **Wi-Fi ve Hücresel Veri** kullanın. Varsayılan Wi-Fi.
- **Paralel Aktarım Sınırı** - aynı anda kaç aktarımın çalışacağı. Varsayılan 5.
- **Arka Plan Aktarımları** - diğer ekranları kullanırken aktarımları sürdürün. Varsayılan olarak açık.
- **Dosyalar için Küçük Resimler** - diğer cihazlardaki dosyalar için küçük resimlerin yalnızca Wi-Fi üzerinden mi yoksa hücresel üzerinden de mi getirileceği. Varsayılan Wi-Fi.

## Dosya Yöneticisi ayarları

- **Dosyaları Kalıcı Olarak Sil** - çöp kutusu olmadan anında silin. Varsayılan olarak kapalı. Bkz. [Erişim ve Gizlilik](/docs/guide/everdisk/everdisk-guide-access).
- **Tüm Bildirim Mesajlarını Sıfırla** - kapattığınız ipucu başlıklarını geri getirin.
- **Küçük Resim Önbelleği** - önbelleğe alınan küçük resimlerin ne kadar yer kapladığını görün ve **Küçük Resim Önbelleğini Temizle**yin.

## Geri bildirim ve yasal

En altta **Bu Uygulamayı Değerlendir**, **Geri Bildirim Gönder**, **Daha Fazla Uygulama Al** işlemlerini yapabilir ve **Şartlar ve Koşullar** ile **Gizlilik Politikası**nı açabilirsiniz.

## Premium Lifetime

Everdisk ücretsiz kullanılır. Tek bir **Premium Lifetime** satın alımı - bir abonelik değil, tek seferlik bir ödeme - şunların kilidini açar:

- **Sınırsız Klasör** - 5'ten fazla klasör paylaşın.
- **Sınırsız Bağlantı** - Cihazlar sekmesinde 10'dan fazla sunucu kaydedin.
- **Fotoğraf ve Video Dönüştürme** - Orijinal dışında herhangi bir kalitede paylaşın.
- **SMB Şifrelemesi** - SMB aktarımlarını SMB3 şifrelemesiyle (AES) koruyun.
- **Özel Portlar** - kendi HTTP, WebDAV, SMB ve FTP portlarınızı belirleyin.
- **Otomatik Paylaşımı Başlatma** - uygulamayı açtığınızda paylaşımı otomatik olarak başlatın.
- **Cihaz Özelleştirme** - özel bir cihaz adı, avatar simgesi, arka plan geçişi ya da fotoğraf avatarı.

Premium, Apple ID'nize bağlıdır. Aynı Apple ID ile oturum açtığınız diğer cihazlarınızda kilidini açmak için **Satın Alımları Geri Yükle**yi kullanın.

## Sonraki adımlar

- [Paylaşım](/docs/guide/everdisk/everdisk-guide-sharing) - Paylaşım ekranı ayrıntılı olarak.
- [Erişim ve Gizlilik](/docs/guide/everdisk/everdisk-guide-access) - parolalar, düzenleme ve engelleme.
- [SSS](/docs/faq/everdisk) - sık sorulan sorulara hızlı yanıtlar.
