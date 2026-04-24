---
title: "SMB Protokolü Kullanarak Bilgisayardan iPhone'a Dosya Aktarma"
description: "Evermusic ve SMB protokolü kullanarak Mac veya Windows PC'nizden iPhone veya iPad'inize büyük dosyaları nasıl aktaracağınızı ve erişeceğinizi öğrenin. Sorunsuz akış ve dosya yönetimi için adım adım kılavuz."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["iPhone'a dosya aktarma SMB", "PC müziğini iPhone'da yayınlama", "Mac'i iPhone'a bağlama SMB", "Evermusic SMB kurulumu", "bilgisayar dosyalarına iPhone'dan erişim", "Windows müzik paylaşımı iOS", "SMB dosya aktarımı Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Özet:** iPhone veya iPad'inizdeki Evermusic'i kullanarak Mac veya Windows PC'nizde depolanan dosyalara SMB üzerinden yerel ağınız aracılığıyla erişin. Kablo yok, iTunes yok, bulut yüklemesi gerekmiyor. Bilgisayarınızda dosya paylaşımını etkinleştirin, uygulamada bağlanın ve dosyalarınızı kablosuz olarak göz atın veya oynatın.

MAC veya PC'nizde büyük dosyalardan oluşan geniş bir koleksiyonunuz var ve bunlara iPhone veya iPad'inizden zahmetsizce erişmek mi istiyorsunuz? Uygulamalarımız basit bir çözüm sunar.

SMB protokolünü kullanarak bilgisayarınız ve iOS cihazınız arasında sorunsuz erişim sağlamak için bu adımları izleyin:

## Adım 1: Bilgisayarınızda SMB Protokolünü Etkinleştirin

**MAC için:**

1. MAC'inizde "Sistem Tercihleri"ni açın.
2. "Paylaşım"a tıklayın.
3. "Dosya Paylaşımı" hizmetini etkinleştirin.
4. Müzik klasörünüzü "Paylaşılan Klasörler" bölümüne ekleyin. Bir kullanıcı ekleyin ve izin düzeyini seçin (Okuma ve Yazma veya Yalnızca Okuma). Eklenen müzik klasörü için "Herkes: Yalnızca Okuma" seçeneğini tercih edebilirsiniz.

   ![Mac Ayarlar Ekranı](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Bilgisayar URL'sini (smb://192.168.xx.xx) unutmayın, çünkü sonraki adımlarda kullanacaksınız.
6. "Seçenekler"e tıklayın ve "SMB kullanarak dosya ve klasörleri paylaş"ı etkinleştirin.

   ![Mac Dosya Paylaşımı Ekranı](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Mevcut hesaplar için "Windows Dosya Paylaşımı"nı etkinleştirin.

   ![Mac SMB Paylaşım Ekranı](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Windows PC için:**

1. Müzik klasörünüze sağ tıklayın.
2. "Özellikler"i seçin.
3. "Paylaşım" sekmesine gidin.
4. "Paylaş..."a tıklayın.
5. Klasörü paylaşmak istediğiniz kişileri seçin ve izin düzeyini belirtin. Seçilen müzik klasörü için "Herkes: Okuma" seçeneğini tercih edebilirsiniz.

   ![Windows SMB Paylaşım Ekranı](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. "Tamamlandı"ya tıklayın.
7. "Dosya Paylaşımı" penceresinde "Tamamlandı"ya tıklayın ve klasör yolunu unutmayın.

   ![Windows SMB Paylaşılan Klasör](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Adım 2: iOS Cihazınızı Bağlayın

1. iPhone veya iPad'inizde uygulamayı açın.
2. "Bağlantılar" sekmesine gidin.

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic Bağlantılar Ekranı"
  caption="Evermusic Bağlantılar Ekranı"
  width="400"
>}}

*Bilgisayarınız "Mevcut cihazlar" Bölümünde Görünüyorsa:*

Bilgisayarınız "Mevcut cihazlar" bölümünde görünüyorsa ve önceki adımda "Herkes: Yalnızca Okuma" seçtiyseniz, bilgisayarınıza dokunmanız yeterlidir ve otomatik olarak bağlanacaktır.

*Bilgisayarınız Otomatik Olarak Görünmüyorsa:*

1. "Bulut hizmetine bağlan" seçeneğine dokunun.
2. "Bulut hizmetine bağlan" ekranında "SMB"yi seçin.

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic Bulut Hizmetine Bağlan Ekranı"
  caption="Evermusic Bulut Hizmetine Bağlan Ekranı"
  width="400"
>}}

3. "SMB Bağlantısı" ekranında, paylaşılan klasör yoluyla birlikte sunucu URL'sini girin. Sunucu adını veya sunucu IP'sini kullanabilirsiniz:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Kullanıcı adınızı ve şifrenizi girin veya önceki adımda "Herkes: Yalnızca Okuma" seçtiyseniz bu alanları boş bırakın.
5. "WORKGROUP" alanı isteğe bağlıdır ve Active Directory Domain'iniz varsa kullanılmalıdır.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB Bağlayıcı Ekranı"
  caption="Evermusic SMB Bağlayıcı Ekranı"
  width="400"
>}}

6. Bilgisayarınızı SMB protokolü kullanarak bağladıktan sonra, "Bağlantılar" ekranının "Bulut hizmetleri" bölümünde görünecektir.
7. Bağlı hizmeti açın ve istediğiniz klasöre gidin.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Evermusic'te Açılmış SMB Klasörü"
  caption="Evermusic'te Açılmış SMB Klasörü"
  width="400"
>}}

8. Dosyalarınızı gerektiği gibi düzenlemek için yerleşik dosya yöneticisini kullanabilirsiniz.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic Dosya Yöneticisi"
  caption="Evermusic Dosya Yöneticisi"
  width="400"
>}}

## Adım 3: Özel Karakterli SMB2 Klasörleri için Çözüm

Bazen SMB2 protokolünü kullanırken özel karakterler içeren klasörlerle sorunlar yaşayabilirsiniz. Bu sorunu çözmek için bazı adımlar:

1. **SMB 1'i Etkinleştirin:**  
   • Geçici bir çözüm olarak, sunucunuzda ve uygulama ayarlarında SMB 1'i etkinleştirmeyi deneyin. Bu, klasör adlarındaki özel karakterlerle ilgili sorunları aşmaya yardımcı olabilir.

2. **Sistem Dosya Açma Menüsünü Kullanın:**  
   • "Yerel dosyalar"a gidin.  
   • "Bu cihazdaki dosyalar" bölümüne kadar aşağı kaydırın.  
   • "Dosyaları aç..." veya "Klasörleri aç..."a dokunun.  
   • Sunucunuzu bulun ve ihtiyacınız olan dosyaları veya klasörleri seçin.  
   • Seçiminizi onaylamak için "Aç"a dokunun.

3. **Alternatif Protokoller:**  
   • Sorun devam ederse, NAS'ınız bu seçenekleri destekliyorsa WebDAV veya DLNA protokollerini kullanarak NAS'ınıza bağlanmayı düşünün. Bu protokoller özel karakterleri daha iyi işleyebilir.

Bu adımları izleyerek, SMB2 protokolünü kullanırken klasör adlarındaki özel karakter sorunlarını hafifletebilirsiniz.

## Sonuç

Bu adımlarla, uygulamalarımızı kullanarak MAC veya PC'nizdeki geniş dosya koleksiyonunuza iPhone veya iPad'inizden zahmetsizce erişebilirsiniz.

## Sık Sorulan Sorular

{{% details title="iTunes olmadan iPhone'dan PC'deki dosyalara erişebilir miyim?" closed="true" %}}
Evet. Evermusic, yerel Wi-Fi ağınızda SMB üzerinden bilgisayarınıza bağlanır. iTunes veya Finder senkronizasyonu gerekmez. PC'nizde dosya paylaşımını etkinleştirin ve doğrudan uygulamadan bağlanın.
{{% /details %}}

{{% details title="SMB dosya erişimi internet üzerinden çalışır mı?" closed="true" %}}
Hayır. SMB yerel bir ağ protokolüdür. iPhone'unuz ve bilgisayarınız aynı Wi-Fi ağında olmalıdır. Uzaktan erişim için dosyaları Google Drive veya Dropbox gibi bir bulut hizmetine yükleyin ve Evermusic'te bağlanın.
{{% /details %}}

{{% details title="SMB üzerinden hangi dosya türlerine erişebilirim?" closed="true" %}}
Evermusic MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC ve diğer ses formatlarını destekler. Yerleşik dosya yöneticisini kullanarak ses dışı dosyalara da göz atabilir ve yönetebilirsiniz.
{{% /details %}}

{{% details title="SMB kullanarak NAS'tan iPhone'a dosya aktarabilir miyim?" closed="true" %}}
Evet. Çoğu NAS cihazı (Synology, QNAP, WD My Cloud ve diğerleri) SMB'yi destekler. Bu kılavuzdaki aynı adımları kullanarak NAS'ınıza bağlanın.
{{% /details %}}

{{% details title="Dosyaları çalmak için iPhone'a kopyalamam gerekir mi?" closed="true" %}}
Hayır. Evermusic dosyaları doğrudan bilgisayarınızdan veya NAS'ınızdan ağ üzerinden yayınlar. Çevrimdışı oynatma için indirmeyi seçmediğiniz sürece dosyalar iPhone'unuza kopyalanmaz.
{{% /details %}}

{{% details title="SMB dosya paylaşımı güvenli mi?" closed="true" %}}
SMB dosya paylaşımı yalnızca yerel ağınızda çalışır. Farklı ağlardaki diğer cihazlar paylaşılan klasörlerinize erişemez. Ek güvenlik için anonim (Herkes) erişim yerine kullanıcı adı ve şifre kullanın.
{{% /details %}}
