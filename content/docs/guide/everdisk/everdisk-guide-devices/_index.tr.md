---
title: "Sunuculara Bağlanın"
date: 2026-08-20
description: "Ağınızdaki diğer sunuculara bağlanmak için Everdisk'teki Cihazlar sekmesini kullanın. DLNA, WebDAV, FTP, SFTP ve SMB sunucuları ile NAS sürücüleri ekleyin ve bunlara göz atın, ses ve video akışı yapın, dosya indirin ve buna izin veren sunucularda oluşturun, yükleyin, yeniden adlandırın, taşıyın veya silin."
keywords: ["Everdisk Cihazlar sekmesi", "NAS bağlantısı", "iPhone DLNA istemci", "iPhone WebDAV istemci", "iPhone FTP istemci", "iPhone SFTP istemci", "iPhone SMB istemci", "SMB paylaşımına bağlan", "ağ sunucusuna göz at", "NAS'tan akış", "sunucudan indir", "bulut WebDAV bağlantısı"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk yalnızca bir kablosuz sürücü değildir - aynı zamanda ağınızdaki diğer cihazlar için bir istemcidir. **Cihazlar** sekmesi, Mac'ler, Windows PC'ler, Linux makineleri, NAS sürücüleri ve medya sunucuları dahil olmak üzere **DLNA**, **WebDAV**, **FTP**, **SFTP** ve **SMB** sunucularına bağlanmanıza ve ardından onların dosyalarına göz atmanıza, akış yapmanıza ve bunları indirmenize olanak tanır.

## Cihazlar ekranı

Cihazlar sekmesinin iki bölümü vardır:

- **Bağlantılar** - halihazırda kaydettiğiniz sunucular.
- **Mevcut cihazlar** - Everdisk'in yerel ağınızda otomatik olarak bulduğu sunucular.

Everdisk'in halihazırda bulduğu bir şeye bağlanmak için, **Mevcut cihazlar**da ona dokunmanız yeterli. Bir sunucuyu elle eklemek için **artı (+)** düğmesine ya da **Yeni Bağlantı**ya dokunun.

## Yeni bir bağlantı ekleyin

**Yeni Bağlantı**ya dokunun ve ulaşmak istediğiniz sunucu türünü seçin:

- **DLNA / UPnP** - medya sunucuları için idealdir. Medya kitaplıklarından, ağ depolama sürücülerinden ve DLNA destekli TV'ler ile bilgisayarlardan video, müzik ve fotoğraf akışı yapın. DLNA salt okunurdur: göz atabilir, akış yapabilir ve indirebilirsiniz, ancak dosya yükleyemez ya da değiştiremezsiniz.
- **WebDAV** - WebDAV'ı destekleyen dosya sunucularına, ağ depolama sürücülerine ve bulut sürücülerine bağlanın. Sunucu izin verdiğinde okuyun ve yazın.
- **FTP** - yönlendiricilerde, ağ depolama sürücülerinde ve web barındırmada yaygındır. Varsayılan port 21'dir (güvenli FTPS için 990); adreste özel bir port belirleyebilirsiniz, örneğin `ftp://host:2121`. Anonim erişim için giriş ve parolayı boş bırakın.
- **SFTP** - SSH üzerinden güvenli şekilde bağlanın. Varsayılan port 22'dir; gerekirse adreste özel bir port kullanın, örneğin `sftp://host:2222`.
- **SMB** - klasörleri **SMB / CIFS** üzerinden paylaşan Mac'lere, Windows PC'lere, Linux sunucularına ve ağ depolamaya (NAS) bağlanın. `smb://server-address/share-name/` gibi bir adres girin (örnekler: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB iki isteğe bağlı alan ekler: bir **Çalışma grubu** adı ve **Otomatik** olarak bırakabileceğiniz ya da **SMB1** veya **SMB2** olarak zorlayabileceğiniz bir **Protokol sürümü**. Özel karakterler içeren dosya veya klasörler açılmıyorsa, sürümü **SMB1** olarak değiştirmeyi deneyin.

> Everdisk yalnızca bu yerel ağ ve doğrudan adreslenen protokollere bağlanır. Google Drive ya da Dropbox gibi bulut hesaplarında oturum açmaz. Bir bulut sürücüsüne yalnızca o hizmet, yazabileceğiniz bir **WebDAV** adresi sunuyorsa erişilebilir.

## Adresi girin ve oturum açın

Bağlantı düzenleyicisinde şunları doldurun:

- **Başlık** - bağlantı için kolay bir ad.
- **URL / adres** - sunucu adresi (her tür için örnekler gösterilir).
- **Giriş** ve **Parola** - sunucu anonim erişime izin veriyorsa ikisini de boş bırakın.

WebDAV için, sunucunuz kendinden imzalı bir sertifika kullanıyorsa geçersiz sertifikalara izin verebilirsiniz. Güvenli bir sunucunun kimliği doğrulanamıyorsa, Everdisk ona güvenmeden önce onaylamanızı ister.

Ücretsiz kullanıcılar en fazla **10** bağlantı kaydedebilir. Premium bu sınırı kaldırır.

## Göz atın, akış yapın ve indirin

Bağlandıktan sonra, açmak için sunucuya dokunun:

- Klasörlere liste ya da ızgara görünümünde **göz atın**, onları sıralayın ve küçük resimleri görün. DLNA sunucuları ayrıca müzik ayrıntılarını ve kapak resmini gösterir.
- Ses ve video **akışı yapın**. Ses, mini oynatıcı kuyruğuna gider; video tam ekran oynatılır. Bir dosya akış halindeyken ileri geri sarma çalışır.
- Dosyaları cihazınıza **indirin**. Toplu indirme için aynı anda birkaç dosya seçin. İndirmeler **Dosya Aktarımları**nda görünür ve **Belgeler** klasörünüze iner.
- Herhangi bir öğedeki **Bilgi**, öğenin türünü, boyutunu, tarihini, yolunu ve medya ayrıntılarını gösterir.

## Bir sunucudaki dosyaları değiştirin

Yazmaya izin veren sunucularda - **WebDAV, FTP, SFTP ve SMB** - dosyaları da yönetebilirsiniz:

- **Yeni Klasör**
- Cihazınızdan **Dosya Yükle**
- **Yeniden Adlandır**, **Taşı** ve **Sil** (bir öğe ya da aynı anda birkaç öğe)

**DLNA** sunucuları salt okunurdur; bu nedenle bu eylemler orada kullanılamaz.

## Aktarımlarınızı izleyin

İndirmeler ve yüklemeler arka planda çalışır ve **Belgeler** sekmesinin sol üstünden açtığınız **Dosya Aktarımları**nda görünür. Orada ilerlemeyi izleyebilir; görevleri duraklatabilir, sürdürebilir, yeniden deneyebilir, iptal edebilir ya da temizleyebilirsiniz. Aktarımları [Ayarlar → Ağ](/docs/guide/everdisk/everdisk-guide-settings) bölümünde de ayarlayabilirsiniz (yalnızca Wi-Fi ya da Wi-Fi ve hücresel, aynı anda kaç tanesinin çalışacağı ve arka planda sürüp sürmeyecekleri).

## Sonraki adımlar

- [Dosyalar ve Belgeler](/docs/guide/everdisk/everdisk-guide-files) - indirdiğiniz her şeyi yönetin.
- [Fotoğraflar, Müzik ve Video](/docs/guide/everdisk/everdisk-guide-media) - akış yaptığınız şeyleri oynatın.
- [Ayarlar](/docs/guide/everdisk/everdisk-guide-settings) - bağlantı sınırları ve aktarım seçenekleri.
