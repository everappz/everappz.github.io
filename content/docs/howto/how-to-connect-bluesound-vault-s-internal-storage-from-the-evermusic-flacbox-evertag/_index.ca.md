---
title: "Com connectar l'emmagatzematge intern del Bluesound VAULT des d'Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Apreneu com accedir al disc dur intern del Bluesound VAULT des d'Evermusic, Flacbox i Evertag utilitzant el protocol SMB per gestionar, editar i reproduir fitxers d'àudio."
keywords: ["bluesound vault", "connectar emmagatzematge smb", "evermusic smb", "flacbox vault", "evertag smb", "emmagatzematge nas música", "unitat interna vault"]
tags: ["evermusic", "connectar", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Resum:** Connecteu-vos a l'emmagatzematge intern del Bluesound VAULT via SMB utilitzant Evermusic, Flacbox o Evertag. Trobeu l'adreça IP del VAULT a l'aplicació BluOS, introduïu-la com a connexió SMB amb accés de convidat i comenceu a reproduir o gestionar els vostres fitxers de música.

El Bluesound VAULT té un disc dur intern i funciona com un emmagatzematge connectat a la xarxa (NAS). Accedir al disc dur intern del VAULT us permet afegir/eliminar fitxers, editar etiquetes de metadades des de les nostres aplicacions Evermusic, Flacbox, Evertag.

**A continuació es mostren els passos per accedir al disc dur intern del VAULT:**

1. A l'aplicació BluOS, seleccioneu **Ajuda > Diagnòstics**.

2. Des de la pàgina de **Diagnòstics**, obtingueu l'**Adreça IP** del VAULT. Aquesta **Adreça IP** s'utilitzarà en els passos següents.

3. Obriu Evermusic, Flacbox o Evertag.

   ![Aplicacions Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Obriu la pantalla "Connexions" i seleccioneu l'element de menú "Connectar un servei al núvol".

   ![Pantalla de Connexions d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Seleccioneu el servei al núvol "SMB".

   ![Pantalla de Connectar un Servei al Núvol d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. A la "Pantalla de configuració SMB" introduïu l'URL en el format següent:

   ```
   SMB://<<VAULT-IP>>
   ```

   Substituïu `<<VAULT-IP>>` per l'**Adreça IP** obtinguda al Pas 2.

   **Nota:** Deixeu els camps d'Inici de sessió i Contrasenya en blanc perquè l'emmagatzematge VAULT admet el mode CONVIDAT.

   ![Pantalla de connexió SMB d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Toqueu el botó "Iniciar sessió" per desar la configuració.

8. Obriu l'emmagatzematge al núvol connectat i navegueu dins la carpeta amb fitxers d'àudio i toqueu qualsevol fitxer per iniciar el reproductor d'àudio.

   ![Pantalla de servidor SMB obert d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. També podeu editar fitxers utilitzant el gestor de fitxers integrat.

   ![Pantalla del gestor de fitxers d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Amb aquests senzills passos, podeu accedir fàcilment al disc dur intern del Bluesound VAULT i controlar la vostra biblioteca de música utilitzant Evermusic, Flacbox o Evertag.

## PMF

{{% details title="Necessito un nom d'usuari i una contrasenya per connectar-me al Bluesound VAULT?" closed="true" %}}
No. El Bluesound VAULT admet l'accés de convidat (anònim) via SMB. Deixeu els camps d'Inici de sessió i Contrasenya en blanc quan configureu la connexió.
{{% /details %}}

{{% details title="Puc editar les etiquetes de música al Bluesound VAULT?" closed="true" %}}
Sí. Utilitzant Evertag, podeu editar les etiquetes de metadades (títol, artista, àlbum, etc.) dels fitxers d'àudio emmagatzemats directament al disc dur intern del VAULT.
{{% /details %}}

{{% details title="Quins protocols admet el Bluesound VAULT?" closed="true" %}}
El Bluesound VAULT exposa el seu emmagatzematge intern via SMB (Server Message Block). Evermusic, Flacbox i Evertag admeten connexions SMB, cosa que fa que connectar-s'hi sigui senzill.
{{% /details %}}

{{% details title="Puc reproduir música en streaming des del VAULT sense copiar fitxers al meu iPhone?" closed="true" %}}
Sí. Un cop connectat via SMB, podeu reproduir fitxers d'àudio en streaming directament des de la unitat interna del VAULT sense copiar-los al vostre dispositiu.
{{% /details %}}
