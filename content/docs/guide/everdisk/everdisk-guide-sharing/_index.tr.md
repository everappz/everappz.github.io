---
title: "Paylaşım"
date: 2026-08-20
description: "Everdisk'te paylaşımın nasıl çalıştığını öğrenin: iPhone veya iPad'inizi kablosuz sürücüye dönüştürmek için Başlat'a dokunun, ne paylaşacağınızı seçin (dosyalar, klasörler, fotoğraflar ve müzik), beş sunucuyu (DLNA, HTTP, WebDAV, SMB, FTP) çalıştırın, SMB bağlantısını SMB3 (AES) ile şifreleyin, bağlantı adreslerini okuyun, kimin bağlı olduğunu görün ve paylaşımı Wi-Fi veya bir USB kablosu üzerinden çalışır durumda tutun."
keywords: ["Everdisk paylaşım", "iPhone kablosuz sürücü", "paylaşımı başlat", "iPhone dosya paylaşma", "ağ üzerinden fotoğraf paylaşma", "DLNA HTTP WebDAV FTP", "ne paylaşılır", "nasıl bağlanılır", "uygulamayı açık tut", "Wi-Fi veya USB kablosuyla paylaşım"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


**Paylaşım** sekmesi Everdisk'in kalbidir. iPhone veya iPad'inizi kablosuz bir sürücüye dönüştürdüğünüz, tam olarak neyi paylaşmak istediğinizi seçtiğiniz ve diğer cihazların bağlanmak için kullandığı adresleri aldığınız yerdir. Uygulamayı açtığınızda ilk gördüğünüz sekme budur.

## Paylaşımı başlatma ve durdurma

Paylaşım ekranının ortasında büyük, yuvarlak bir düğme bulunur.

- Etkin sunucularınızın tümünü aynı anda çevrimiçi getirmek için **Başlat**'a dokunun. Düğme önce **Başlatılıyor...**, paylaşım etkin olduğunda ise **Durdur** gösterir.
- Her şeyi yeniden çevrimdışına almak için **Durdur**'a dokunun. Bağlı cihazların bağlantısı kesilir.

Paylaşım çalışırken seçtiğiniz dosyalar, fotoğraflar ve müzik, aşağıdaki beş yöntemden birini kullanarak bağlanan, aynı ağdaki herhangi bir cihaz için erişilebilir olur.

> Paylaşım yalnızca uygulama açıkken çalışır. Nedenini ve büyük aktarımları nasıl sürdüreceğinizi öğrenmek için bu sayfanın sonuna yakın **Uygulamayı açık tutun** bölümüne bakın.

## Ne paylaşacağınızı seçme

Başlamadan önce, üç grubu açmak için **Ne Paylaşılır** başlığına dokunun. Bunların herhangi bir karışımını paylaşabilirsiniz; paylaşım başlamadan önce en az bir şey seçmeniz gerekir.

**Dosyalar ve Klasörler**

- Uygulamanızın kendi **Belgeler** klasörü varsayılan olarak paylaşılır. İsterseniz paylaşımını durdurabilirsiniz.
- Cihazınızın herhangi bir yerinden bir klasörü paylaşmak için **Klasör Ekle**'ye, tek tek dosyaları paylaşmak için **Dosya Ekle**'ye dokunun.
- Paylaşılan her öğenin bir **Bilgi** düğmesi ve bir **Paylaşımı Durdur** düğmesi vardır.

**Fotoğraflar ve Videolar**

- Tüm fotoğraf ve video kitaplığınızı paylaşmak için **Tüm Fotoğraf Kitaplığına erişime izin ver**i açın, ya da
- Yalnızca paylaşmak istediğiniz fotoğraf ve videoları elle seçmek için **Fotoğraf Ekle**'ye dokunun.

**Müzik**

- Tüm müzik kitaplığınızı paylaşmak için **Tüm Müzik Kitaplığına erişime izin ver**i açın, ya da
- Yalnızca seçili şarkıları paylaşmak için **Parça Ekle**'ye dokunun.
- Korumalı (DRM) ya da yalnızca bulutta saklanan parçalar paylaşılamaz.

Hiçbir şey seçmeden başlatmayı denerseniz, Everdisk bir **Paylaşılacak Bir Şey Yok** notu gösterir. Paylaşım çalışırken paylaşılanları değiştirirseniz, değişikliği uygulamak için **Durdurup yeniden Başlatın**.

## Beş sunucu

Everdisk aynı içeriği aynı anda beş farklı yolla paylaşır. Her biri farklı türde bir cihaz için tasarlanmıştır ve her biri **Ayarlar → Paylaşım → Bağlantılar** üzerinden açılıp kapatılabilir. Varsayılan olarak beşi de açıktır.

- **TV ve Medya Merkezi (DLNA)** - akıllı TV'ler ve medya oynatıcıları için. Cihazınızı kendileri keşfeder ve fotoğraflarınızı, videolarınızı ve müziklerinizi önizleme küçük resimleriyle gösterir.
- **Tarayıcı (HTTP)** - herhangi bir telefon, tablet veya bilgisayar için. Karşı taraf, dosyalarınıza göz atmak ve indirmek için bir web tarayıcısında bir bağlantı açar. Kurulacak bir şey yok.
- **Bilgisayar (WebDAV)** - bir Mac, Windows PC veya Linux makine için. Cihazınız sıradan bir ağ sürücüsü gibi görünür; böylece dosyaları her iki yönde de sürükleyebilirsiniz.
- **Bilgisayar (Gelişmiş) (SMB)** - Mac, Windows ve Linux için bir ağ sürücüsü. Bir Mac'te Finder kenar çubuğunda kendiliğinden görünür; Windows'ta bir `smb://` adresiyle Dosya Gezgini'nde açın. **Şifreleyebileceğiniz** tek bağlantıdır, SMB3 şifrelemesiyle (AES).
- **Diğer Uygulamalar ve Cihazlar (FTP)** - FTP konuşan dosya uygulamaları ve ileri düzey kullanıcılar için.

Her tür için adım adım bağlantı talimatları için bkz. [Cihazlarınızı Bağlayın](/docs/guide/everdisk/everdisk-guide-connect).

## Nasıl Bağlanılır ve bağlantı adresleri

Başlat'a dokunduktan sonra **Nasıl Bağlanılır** bölümü, her etkin sunucu için diğer cihaza yazacağınız tam **adres**i içeren bir kart gösterir. Her adresi kopyalamak kolaydır - kopyalamak için üzerine dokunun, göndermek için **Paylaş** düğmesini kullanın ya da protokole özel ayrıntılı talimatlar için **bilgi (ⓘ)** düğmesine dokunun.

- DLNA kartı, isteyen oynatıcılar için `/device-desc.xml` ile biten bir cihaz açıklaması adresi gösterir.
- Cihazınız bir Mac'e kabloyla takılıyken, cihazınızın `.local` adını kullanan ve **Kablo Bağlantısı** rozetli ekstra bir adres görünür.

Adresi ayrıca bir **QR kodu** olarak açabilirsiniz; böylece başka bir cihazın kamerası doğrudan adrese atlayabilir.

## Kim bağlı

**Kim Bağlı** bölümü, o anda size bağlı olan cihazları gerçek zamanlı olarak listeler. Tanımadığınız bir cihazı **Bu cihazı engelle** ile engellemek için yanındaki daha fazla eylem düğmesine dokunun. Engellenen cihazlar [Erişim ve Gizlilik](/docs/guide/everdisk/everdisk-guide-access) bölümünde yönetilir.

## Cihaz adınız ve avatarınız

Her cihazın kolay bir adı ("Speedy-Hare" gibi) ve renkli bir avatarı vardır. Bu, bir TV'nin, bilgisayarın ya da başka bir uygulamanın ağda cihazınız için gösterdiği addır; böylece kolayca ayırt edilir. Adı ve avatarı ücretsiz olarak yeniden oluşturabilir ya da Premium ile özel bir ad, simge veya fotoğraf avatarı belirleyebilirsiniz. Bkz. [Ayarlar](/docs/guide/everdisk/everdisk-guide-settings).

## Wi-Fi veya bir USB kablosu üzerinden paylaşım

Paylaşım iki durumda çalışabilir:

- **Wi-Fi üzerinden** - cihazınız ve diğer cihazlar aynı Wi-Fi ağındadır.
- **Bir USB kablosu üzerinden** - hiç Wi-Fi olmasa bile cihazınız bir **Mac**'e kabloyla takılıdır. Bu Wi-Fi'dan daha hızlıdır ve bir uçakta, otelde ya da kilitli bir ağda çalışmayı sürdürür.

Ne Wi-Fi ne de bir kablo varsa **Başlat** düğmesi devre dışı kalır ve bir **Wi-Fi Bağlantısı Yok** notu görünür. Paylaşım sırasında bağlantı koparsa, Everdisk paylaşımı otomatik olarak durdurur ve sizi bilgilendirir. Tam bir açıklama için bu notların herhangi birinde bilgi düğmesine dokunun.

## Uygulamayı açık tutun

iPhone veya iPad'iniz sunucu görevi gördüğü için **paylaşım yalnızca Everdisk ekranda açıkken çalışır**. Uygulamayı kapatır ya da cihazı uzun süre kilitli tutarsanız, sistem uygulamayı duraklatabilir ve paylaşım durur.

Büyük aktarımlar için:

- Everdisk'i açık ve ön planda tutun.
- Cihazınızı güce takın.
- Aktarım sırasında iOS Ayarlar uygulamasında **Otomatik Kilit**i **Asla** olarak ayarlayın.

**Bağlantı kesilmeden önce bildir**i (Ayarlar → Paylaşım'da) açabilirsiniz; böylece Everdisk, sistem uygulamayı askıya almadan önce size uygulamayı yeniden açmanızı hatırlatır. Daha fazla ayrıntı için **Uygulamayı açık tutun** başlığındaki bilgi düğmesine dokunun.

## Sonraki adımlar

- [Cihazlarınızı Bağlayın](/docs/guide/everdisk/everdisk-guide-connect) - bir TV, bilgisayar, tarayıcı, telefon ya da USB kablosu bağlayın.
- [Erişim ve Gizlilik](/docs/guide/everdisk/everdisk-guide-access) - bir parola ekleyin ve düzenlemeyi denetleyin.
- [Ayarlar](/docs/guide/everdisk/everdisk-guide-settings) - sunucuları açıp kapatın ve kaliteyi ayarlayın.
