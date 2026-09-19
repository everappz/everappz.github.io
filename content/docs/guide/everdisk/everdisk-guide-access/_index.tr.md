---
title: "Erişim ve Gizlilik"
date: 2026-08-20
description: "Everdisk paylaşımınızı güvende tutun: erişimi bir giriş ve parolayla koruyun, SMB bağlantısını SMB3 (AES) ile şifreleyin, Dosya Düzenleme ile bağlı cihazların yükleyip yeniden adlandırıp silebilmesini denetleyin, bilinmeyen cihazları engelleyin, çöp kutusu ile kalıcı silme arasında seçim yapın ve her şeyin neden yerel ağınızda kaldığını anlayın."
keywords: ["Everdisk parola koruması", "SMB şifrelemesi", "SMB3 AES şifrelemesi", "dosya düzenleme anahtarı", "cihazı engelle", "engellenen cihazlar", "dosyaları kalıcı olarak sil", "yalnızca yerel ağ", "özel dosya paylaşımı", "DLNA parolasız", "ağ güvenliği"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk, dosyalarınızı kendi ağınızda tutar ve bunlara kimin erişebileceği ile neler yapabileceği üzerinde size basit denetimler sunar. Bu denetimleri **Ayarlar → Paylaşım → Erişim**'de ve Dosya Yöneticisi'ndeki birkaç ilgili ayarda bulursunuz.

## Erişimi bir giriş ve parolayla koruyun

Varsayılan olarak, aynı ağda olup adresinize sahip olan herkes paylaşılan dosyalarınızı açabilir. Oturum açmayı zorunlu kılmak için:

1. **Ayarlar → Paylaşım → Erişim**'e gidin.
2. Bir **Giriş** ve bir **Parola** girin.
3. Artık **Tarayıcı (HTTP)**, **Bilgisayar (WebDAV)**, **Bilgisayar (Gelişmiş) (SMB)** ve **Diğer Uygulamalar ve Cihazlar (FTP)** bağlantılarının tümü, dosyalarınızı göstermeden önce bu bilgileri sorar.

Açık erişim için her iki alanı da boş bırakın. Parolanız cihazın Keychain'inde güvenle saklanır.

> **DLNA her zaman açıktır.** TV ve Medya Merkezi (DLNA) bağlantısı parola ile korunamaz; bu nedenle açık olduğunda, aynı Wi-Fi'daki her cihaz paylaşılan medyanıza göz atabilir. Yalnızca korumalı bağlantılar istiyorsanız onu kapatın ve yalnızca güvendiğiniz ağlarda paylaşın.

## SMB bağlantısını şifreleyin (SMB3 / AES)

Bir giriş ve parola **kimin** bağlanabileceğini denetler, ancak çoğu bağlantıda verinin kendisi hâlâ açık olarak aktarılır. **SMB, Everdisk'in şifreleyebileceği tek bağlantıdır** ve her aktarımı karıştırır; böylece aynı ağdaki başka hiç kimse onu okuyamaz.

Açmak için:

1. Yukarıdaki gibi bir **Giriş** ve **Parola** ayarlayın - şifreli bağlantılar anonim olamaz.
2. **Ayarlar → Paylaşım**'a gidin ve **SMB şifrelemesi iste**'yi açın.
3. Değişikliğin etkili olması için paylaşımı **Durdurup yeniden Başlatın**.

Her SMB aktarımı ardından **SMB3 şifrelemesiyle (AES)** korunur. Bağlanan cihaz SMB3'ü desteklemelidir - modern bir Mac'teki Finder ya da **Windows 10 ve sonrası**. Bu, tam olarak güvenmediğiniz bir Wi-Fi'de harika bir seçimdir. SMB şifrelemesi bir Premium özelliğidir.

## Düzenlemeye izin verin ya da engelleyin (Dosya Düzenleme)

**Dosya Düzenleme** anahtarı, bağlı cihazların dosyalarınıza yalnızca bakabileceğini mi yoksa onları değiştirebileceğini mi denetler.

- **Açık** (varsayılan): bağlı cihazlar paylaşılan dosyalarınızı **yükleyebilir, yeniden adlandırabilir ve silebilir** - böylece cihazınız gerçek, çift yönlü bir ağ sürücüsü gibi çalışır.
- **Kapalı**: paylaşılan dosyalarınız **salt okunur**dur. Başkaları görüntüleyip indirebilir, ancak hiçbir şey ekleyemez ya da değiştiremez.

Onu açmak, başkalarının dosyalarınızı değiştirmesine izin verdiği için kısa bir uyarı gösterir. Açıkken bir **Önemli** rozeti taşır.

## Bir cihazı engelleyin

Tanımadığınız bir cihaz görürseniz:

1. Paylaşım ekranında onu **Kim Bağlı** altında bulun.
2. Daha fazla eylem düğmesine dokunun ve **Bu cihazı engelle**yi seçin.

Engellenen cihazlar **Ayarlar → Paylaşım → Erişim → Engellenen Cihazlar**'da listelenir; burada birinin **engelini kaldırabilir** ya da **Tümünün Engelini Kaldır**abilirsiniz. Engelleme, ağ adresi değişse bile cihazı izler (Tarayıcı, Bilgisayar ve TV bağlantıları için).

## Çöp kutusu ile kalıcı silme

Bir dosya silindiğinde - dosya yöneticisinde sizin tarafınızdan ya da bağlı bir cihaz tarafından - normalde geri alabilmeniz için kurtarılabilir bir **çöp kutusu**na gider.

Dosyaların kurtarma olmadan anında kaldırılmasını tercih ederseniz, **Ayarlar → Dosya Yöneticisi → Dosyaları Silme**'de **Dosyaları Kalıcı Olarak Sil**i açın. Bu varsayılan olarak kapalıdır. **Cihaz üzerindeki dosya yöneticisini** ve **ağ üzerinden yapılan silmeleri** etkiler; sistem Fotoğraflar kitaplığının ya da Müzik kitaplığının silmeyi nasıl ele aldığını değiştirmez.

## Her şey yerel kalır

Everdisk yalnızca **yerel ağınız** üzerinden paylaşım yapar - hiçbir şey internete yüklenmez ve arada bir bulut hesabı yoktur. Bilmeye değer birkaç şey:

- Everdisk'in, yakındaki cihazların onu bulabilmesi için iOS **Yerel Ağ** iznine ihtiyacı vardır. Bu izin kapalıysa, bir not iOS Ayarlar uygulamasında onu yeniden nasıl açacağınızı açıklar.
- En yüksek gizlilik için, yalnızca güvendiğiniz bir **ev ya da özel Wi-Fi** ağındayken paylaşın ve halka açık Wi-Fi'da dikkatli olun. Bir giriş ve parola yardımcı olur, ancak güvenilir bir ağın yerini tutmaz.
- **En özel seçenek, bir Mac'e bağlı bir USB kablosudur** - veri doğrudan kablo üzerinden gider ve asla yönlendiriciye ya da internete dokunmaz. Bkz. [Cihazlarınızı Bağlayın](/docs/guide/everdisk/everdisk-guide-connect).

## Sonraki adımlar

- [Paylaşım](/docs/guide/everdisk/everdisk-guide-sharing) - ne paylaşacağınızı seçin ve paylaşmaya başlayın.
- [Ayarlar](/docs/guide/everdisk/everdisk-guide-settings) - tüm Erişim ve Dosya Yöneticisi ayarları tek bir yerde.
