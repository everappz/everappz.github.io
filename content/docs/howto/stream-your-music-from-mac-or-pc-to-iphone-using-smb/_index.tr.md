---
title: "SMB Kullanarak Mac veya PC'den iPhone'a Müzik Akışı"
description: "Evermusic ve SMB protokolünü kullanarak Mac veya Windows PC'den iPhone veya iPad'e müzik koleksiyonunuzu nasıl aktaracağınızı öğrenin. Senkronizasyon olmadan bağlanmak ve ses dosyalarının keyfini çıkarmak için basit adım adım kılavuz."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["Mac'ten iPhone'a müzik akışı", "SMB ses akışı iOS", "Evermusic SMB kurulumu", "PC müzik iPhone bağlantısı", "Mac müzik paylaşımı iOS", "SMB Windows dosya akışı", "Evermusic PC klasör erişimi"]
---

{{< author-byline >}}


**Özet:** Mac veya Windows PC'nizden yerel ağınız üzerinden SMB kullanarak müzik akışı yapmak için iPhone veya iPad için Evermusic uygulamasını kullanın. Senkronizasyon yok, kopyalama yok -- bilgisayarınızda dosya paylaşımını etkinleştirin, uygulamada bağlanın ve çalın. Kurulum 5 dakikadan az sürer.

MAC veya PC'nizdeki müzik denizinde boğuluyor ve iPhone veya iPad'inizde sorunsuz bir şekilde keyfini çıkarmak mı istiyorsunuz? Evermusic'ten başka bir yere bakmayın. Evermusic ile bilgisayarınızı SMB protokolünü kullanarak bağlamak ve cihazda ekstra yer kaplamadan veya senkronizasyon sorunlarıyla uğraşmadan sevdiğiniz şarkıları dinlemek inanılmaz derecede basittir. İşte başlamanız için adım adım bir kılavuz:

## Adım 1: Bilgisayarınızda SMB Protokolünü Etkinleştirin

![Evermusic - SMB Desteği - Mac Paylaşım Ekranı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### MAC kullanıyorsanız

- Sistem Tercihleri -> Paylaşım'ı açın.
- Dosya Paylaşımı hizmetini etkinleştirin.
- "Paylaşılan Klasörler" bölümünde müzik klasörünüzü ekleyin, bir kullanıcı seçin ve izin düzeylerini ayarlayın (Okuma ve Yazma veya Yalnızca Okuma).
- Ek kolaylık için müzik klasörü için "Herkes: Yalnızca Okuma" seçebilirsiniz, bu da Evermusic'te kolayca erişilebilir olmasını sağlar.
- Sonraki adımlar için bilgisayarınızın URL'sini (smb://192.168.xx.xx) hatırlamayı unutmayın.

![Evermusic - SMB Desteği - Dosya Paylaşım Ekranı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- "Seçenekler"e dokunun ve "SMB kullanarak dosya ve klasörleri paylaş"ı etkinleştirin.
- Mevcut hesaplar için "Windows Dosya Paylaşımı"nı etkinleştirin.

![Evermusic - SMB Desteği - Dosya ve Klasör Paylaşım Ekranı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Windows PC kullanıyorsanız

![Evermusic - SMB Desteği - Windows'ta Dosya Paylaşımı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Müzik klasörünüze sağ tıklayın.
- "Özellikler"i seçin.
- "Paylaşım" sekmesini açın.
- "Paylaş..."a tıklayın.
- Paylaşacağınız kişileri seçin ve izin düzeylerini ayarlayın.
- MAC'te olduğu gibi, seçili müzik klasörü için "Herkes: Okuma" seçebilirsiniz.
- Ayarlarınızı kaydetmek için "Tamamlandı"ya tıklayın.

![Evermusic - SMB Desteği - Windows'ta Paylaşılan Klasör](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Adım 2: Bilgisayarınızı Otomatik Olarak Ekleyin

- Şimdi Evermusic'i açın ve "Bağlantılar" sekmesine gidin (eski uygulama sürümü kullanıyorsanız "Ağ").
- Bilgisayarınızı "Mevcut cihazlar" (eski uygulama sürümü kullanıyorsanız "Mevcut paylaşımlar") bölümünde görüyorsanız ve önceki adımda "Herkes: Yalnızca Okuma" seçtiyseniz, bilgisayarınıza dokunmanız yeterli, otomatik olarak bağlanacaktır.
- Bu gerçekleşmezse, bilgisayarınızı elle ekleyebilirsiniz.

![Evermusic - SMB Desteği - Hesap Bağlama Ekranı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Adım 3: Bilgisayarınızı Elle Ekleyin

- "Bulut hizmetine bağlan"a dokunun (eski uygulama sürümü kullanıyorsanız "Hesap Ekle")
- Sonraki ekranda mevcut sunucular listesinden "SMB"yi seçin.
- "SMB" ayarlar ekranında:
  - Paylaşılan klasör yoluyla birlikte sunucu URL'sini girin. Sunucu adını veya sunucu IP'sini girebilirsiniz. Örneğin:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Kullanıcı adınızı ve şifrenizi girin veya önceki adımda "Herkes: Yalnızca Okuma" seçtiyseniz bu alanları boş bırakın.
  - "WORKGROUP" alanı isteğe bağlıdır ve Active Directory Etki Alanınız varsa kullanılmalıdır.

![Evermusic - SMB Desteği - Kimlik Bilgileri Giriş Ekranı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

SMB Hesabınızı bağladıktan sonra "Bulut hizmetleri" ("Hesaplar") bölümünde görünecektir. Bağlı hesabı dokunarak açın, müzik klasörüne gidin ve oynatıcıyı başlatmak için herhangi bir ses dosyasına dokunun.

![Evermusic - SMB Desteği - Bağlı Klasör Açma Ekranı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Evermusic ile iPhone veya iPad'inizde müzik koleksiyonunuzun keyfini sorunsuz bir şekilde çıkarın.

![Evermusic - SMB Desteği - Ses Oynatıcı Ekranı](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Adım 4: SMB2 Geçici Çözümü

Klasörlere göz atma veya özel karakterler (ü, ö, é gibi) içeren dosyaları çalma konusunda sorunlarla karşılaşırsanız, bu SMB2 protokolüyle ilgili olabilir. Bu sorunu çözmek için aktif olarak çalışıyoruz.

Geçici bir çözüm olarak, sunucunuzda ve uygulama ayarlarında SMB 1'i etkinleştirmeyi deneyin. Alternatif olarak, sistem dosya açma menüsünü kullanarak SMB sunucunuza bağlanabilirsiniz. İşte nasıl:

1. "Yerel dosyalar"a gidin.
2. "Bu cihazdaki dosyalar" bölümüne kaydırın ve "Dosyaları aç..." veya "Klasörleri aç..."a dokunun.
3. Sunucunuzu bulun ve ihtiyacınız olan dosyaları veya klasörleri seçin.
4. Seçiminizi onaylamak için "Aç"a dokunun.

## Adım 5: WebDAV Geçici Çözümü

Ayrıca, destekleniyorsa WebDAV veya DLNA protokollerini kullanarak NAS'ınıza bağlanmayı deneyebilirsiniz.

Bu adımları izleyerek, dosya adlarındaki özel karakterlerle ilgili sorunları atlayabilir ve medya dosyalarınızın keyfini çıkarmaya devam edebilirsiniz.

Not: iTunes Dosya Paylaşımı'nı kullanarak MAC/PC'nizden iPhone'unuza ses dosyaları aktarabilir ve yerel ses dosyalarını çalabilirsiniz. Bu özellik hakkında daha fazla bilgiyi kılavuzumuzda bulabilirsiniz: [iPhone'da iTunes Dosyalarını Nasıl Çalarsınız](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Sıkça Sorulan Sorular

{{% details title="iTunes olmadan PC'mden iPhone'uma müzik akışı yapabilir miyim?" closed="true" %}}
Evet. Evermusic, yerel Wi-Fi ağınızda SMB üzerinden PC'nize bağlanır. iTunes gerekli değildir. PC'nizde dosya paylaşımını etkinleştirin ve uygulamada bağlanın.
{{% /details %}}

{{% details title="SMB akışı mobil veri kullanır mı?" closed="true" %}}
Hayır. SMB yerel Wi-Fi ağınız üzerinden çalışır. İnternet bağlantısı veya mobil veri gerekmez.
{{% /details %}}

{{% details title="Evermusic SMB üzerinden hangi ses formatlarını destekler?" closed="true" %}}
Evermusic MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC ve diğer yaygın ses formatlarını destekler. Dosyalar doğrudan SMB paylaşımından çalınır.
{{% /details %}}

{{% details title="NAS'tan iPhone'uma müzik akışı yapabilir miyim?" closed="true" %}}
Evet. NAS'ınız SMB'yi destekliyorsa (çoğu destekler, Synology, QNAP ve WD My Cloud dahil), bu kılavuzdaki aynı adımları kullanarak bağlanabilirsiniz.
{{% /details %}}

{{% details title="Akış sırasında bilgisayarımı açık tutmam gerekiyor mu?" closed="true" %}}
Evet. Evermusic dosyaları doğrudan bilgisayarınızdan aktardığından, bilgisayarın açık olması ve iPhone'unuzla aynı ağa bağlı olması gerekir.
{{% /details %}}

{{% details title="SMB akışı için dosya boyutu sınırı var mı?" closed="true" %}}
Hayır. Evermusic SMB üzerinden her boyuttaki dosyayı aktarır. Büyük kayıpsız dosyalar (FLAC, WAV) sorunsuz çalışır.
{{% /details %}}
