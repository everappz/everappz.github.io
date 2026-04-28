---
title: "Evermusic, Flacbox, Evertag'den Bluesound VAULT'un dahili depolama alanına nasıl bağlanılır"
date: 2022-03-10
description: "SMB protokolünü kullanarak Evermusic, Flacbox ve Evertag'den Bluesound VAULT'un dahili sabit diskine nasıl erişileceğini, ses dosyalarını yönetmeyi, düzenlemeyi ve çalmayı öğrenin."
keywords: ["bluesound vault", "smb depolama bağlantısı", "evermusic smb", "flacbox vault", "evertag smb", "nas depolama müzik", "vault dahili sürücü"]
tags: ["evermusic", "bağlantı", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Özet:** Evermusic, Flacbox veya Evertag kullanarak SMB üzerinden Bluesound VAULT'unuzun dahili depolama alanına bağlanın. BluOS uygulamasında VAULT'un IP adresini bulun, misafir erişimiyle SMB bağlantısı olarak girin ve müzik dosyalarınızı çalmaya veya yönetmeye başlayın.

Bluesound VAULT dahili bir sabit diske sahiptir ve Ağa Bağlı Depolama (NAS) olarak çalışır. VAULT'un dahili sabit diskine erişim, Evermusic, Flacbox, Evertag uygulamalarımızdan dosya eklemenize/silmenize, meta veri etiketlerini düzenlemenize olanak tanır.

**VAULT'unuzun dahili sabit diskine erişim adımları aşağıdadır:**

1. BluOS Uygulamasında **Yardım > Tanılama**'yı seçin.

2. **Tanılama** sayfasından VAULT'un **IP Adresini** alın. Bu **IP Adresi** sonraki adımlarda kullanılacaktır.

3. Evermusic, Flacbox veya Evertag'i açın.

   ![Everappz uygulamaları](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. "Bağlantılar" ekranını açın ve "Bulut hizmeti bağla" menü öğesini seçin.

   ![Evermusic Bağlantılar Ekranı](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. "SMB" bulut hizmetini seçin.

   ![Evermusic Bulut Hizmeti Bağla Ekranı](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. "SMB Yapılandırma ekranında" URL'yi aşağıdaki biçimde girin:

   ```
   SMB://<<VAULT-IP>>
   ```

   `<<VAULT-IP>>` kısmını Adım 2'de elde edilen **IP Adresi** ile değiştirin.

   **Not:** VAULT Depolama MISAFIR modunu desteklediği için Kullanıcı Adı ve Şifre alanlarını boş bırakın.

   ![Evermusic SMB Bağlantı Ekranı](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Yapılandırmayı kaydetmek için "Giriş yap" düğmesine dokunun.

8. Bağlı bulut depolama alanını açın, ses dosyalarının bulunduğu klasöre gidin ve ses oynatıcıyı başlatmak için herhangi bir dosyaya dokunun.

   ![Evermusic Açılmış SMB Sunucusu Ekranı](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Yerleşik dosya yöneticisini kullanarak dosyaları da düzenleyebilirsiniz.

   ![Evermusic Dosya Yöneticisi Ekranı](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Bu basit adımlarla Bluesound VAULT'unuzun dahili sabit diskine kolayca erişebilir ve Evermusic, Flacbox veya Evertag kullanarak müzik kütüphanenizin kontrolünü elinize alabilirsiniz.

## SSS

{{% details title="Bluesound VAULT'a bağlanmak için kullanıcı adı ve şifre gerekiyor mu?" closed="true" %}}
Hayır. Bluesound VAULT, SMB üzerinden misafir (anonim) erişimi destekler. Bağlantıyı yapılandırırken Kullanıcı Adı ve Şifre alanlarını boş bırakın.
{{% /details %}}

{{% details title="Bluesound VAULT üzerinde müzik etiketlerini düzenleyebilir miyim?" closed="true" %}}
Evet. Evertag kullanarak, VAULT'un dahili sabit diskinde doğrudan depolanan ses dosyalarının meta veri etiketlerini (başlık, sanatçı, albüm vb.) düzenleyebilirsiniz.
{{% /details %}}

{{% details title="Bluesound VAULT hangi protokolleri destekler?" closed="true" %}}
Bluesound VAULT, dahili depolama alanını SMB (Server Message Block) üzerinden sunar. Evermusic, Flacbox ve Evertag'in tümü SMB bağlantılarını destekler, bu da bağlantıyı kolaylaştırır.
{{% /details %}}

{{% details title="Dosyaları iPhone'uma kopyalamadan VAULT'tan müzik akışı yapabilir miyim?" closed="true" %}}
Evet. SMB üzerinden bağlandıktan sonra, VAULT'un dahili sürücüsünden cihazınıza kopyalamadan doğrudan ses dosyalarını akışla dinleyebilirsiniz.
{{% /details %}}
