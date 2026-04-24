---
title: "Transmita sua música do Mac ou PC para o iPhone usando SMB"
description: "Aprenda como transmitir sua coleção de música do Mac ou Windows PC para o seu iPhone ou iPad usando o Evermusic e o protocolo SMB. Um guia simples passo a passo para conectar e curtir áudio sem sincronização."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transmitir música do Mac para iPhone", "SMB áudio streaming iOS", "configuração Evermusic SMB", "conectar música PC iPhone", "compartilhar música Mac iOS", "SMB Windows streaming de arquivos", "acesso Evermusic pastas PC"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Resumo:** Use o aplicativo Evermusic para iPhone ou iPad para transmitir música do seu Mac ou Windows PC pela rede local usando SMB. Sem sincronização, sem cópia -- basta ativar o compartilhamento de arquivos no seu computador, conectar no app e reproduzir. A configuração leva menos de 5 minutos.

Você está se afogando em um mar de música no seu MAC ou PC e quer curtir sem complicações no seu iPhone ou iPad? Não procure mais do que o Evermusic. Com o Evermusic, é incrivelmente simples conectar seu computador usando o protocolo SMB e transmitir suas músicas favoritas sem se preocupar em ocupar espaço extra no dispositivo ou lidar com problemas de sincronização. Aqui está um guia passo a passo para começar:

## Passo 1: Ative o protocolo SMB no seu computador

![Evermusic - Suporte SMB - Tela de compartilhamento do Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Se você usa MAC

- Abra Preferências do Sistema -> Compartilhamento.
- Ative o serviço de Compartilhamento de Arquivos.
- Na seção "Pastas Compartilhadas", adicione sua pasta de música, selecione um usuário e defina os níveis de permissão (Leitura e Gravação ou Somente Leitura).
- Para maior conveniência, você pode selecionar "Todos: Somente Leitura" para a pasta de música, tornando-a facilmente acessível no Evermusic.
- Não se esqueça de lembrar o URL do seu computador (smb://192.168.xx.xx) para os próximos passos.

![Evermusic - Suporte SMB - Tela de compartilhamento de arquivos](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Toque em "Opções" e ative "Compartilhar arquivos e pastas usando SMB."
- Ative "Compartilhamento de Arquivos Windows" para as contas disponíveis.

![Evermusic - Suporte SMB - Tela de compartilhamento de arquivos e pastas](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Se você usa um Windows PC

![Evermusic - Suporte SMB - Compartilhar arquivos no Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Clique com o botão direito na sua pasta de música.
- Selecione "Propriedades."
- Abra a aba "Compartilhamento."
- Clique em "Compartilhar..."
- Escolha as pessoas com quem compartilhar e defina seus níveis de permissão.
- Assim como no MAC, você pode optar por "Todos: Leitura" para a pasta de música selecionada.
- Clique em "Concluído" para salvar suas configurações.

![Evermusic - Suporte SMB - Pasta compartilhada no Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Passo 2: Adicione seu computador automaticamente

- Agora, abra o Evermusic e vá para a aba "Conexões" ("Rede" se estiver usando uma versão antiga do app).
- Se você vir seu computador na seção "Dispositivos disponíveis" ("Compartilhamentos disponíveis" se estiver usando uma versão antiga do app) e selecionou "Todos: Somente Leitura" no passo anterior, simplesmente toque no seu computador e ele se conectará automaticamente.
- Se isso não acontecer, você pode adicionar seu computador manualmente.

![Evermusic - Suporte SMB - Tela de conexão de conta](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Passo 3: Adicione seu computador manualmente

- Toque em "Conectar um serviço de nuvem" ("Adicionar Conta" se estiver usando uma versão antiga do app)
- Selecione "SMB" na lista de servidores disponíveis na próxima tela.
- Na tela de configurações "SMB":
  - Digite o URL do servidor com o caminho da pasta compartilhada. Você pode digitar o nome do servidor ou o IP do servidor. Por exemplo:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Digite seu Login e Senha ou deixe esses campos em branco se selecionou "Todos: Somente Leitura" no passo anterior.
  - O campo "WORKGROUP" é opcional e deve ser usado se você tiver um Domínio Active Directory.

![Evermusic - Suporte SMB - Tela de inserção de credenciais](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Depois de conectar sua conta SMB, ela aparecerá na seção "Serviços de nuvem" ("Contas"). Abra a conta conectada tocando nela, navegue até a pasta de música e toque em qualquer arquivo de áudio para iniciar o reprodutor.

![Evermusic - Suporte SMB - Tela de abrir pasta conectada](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Curta sua coleção de música sem problemas no seu iPhone ou iPad com o Evermusic.

![Evermusic - Suporte SMB - Tela do reprodutor de áudio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Passo 4: Solução alternativa para SMB2

Se você encontrar problemas ao navegar pelas pastas ou reproduzir arquivos que contêm símbolos especiais (como ü, ö, é), isso pode estar relacionado ao protocolo SMB2. Estamos trabalhando ativamente para resolver esse problema.

Como solução temporária, tente ativar o SMB 1 no seu servidor e nas configurações do app. Alternativamente, você pode se conectar ao seu servidor SMB usando o menu de abertura de arquivos do sistema. Veja como:

1. Navegue até "Arquivos locais."
2. Role para baixo até a seção "Arquivos neste dispositivo" e toque em "Abrir arquivos..." ou "Abrir pastas..."
3. Localize seu servidor e selecione os arquivos ou pastas que você precisa.
4. Toque em "Abrir" para confirmar sua seleção.

## Passo 5: Solução alternativa WebDAV

Além disso, você pode tentar se conectar ao seu NAS usando os protocolos WebDAV ou DLNA, se suportados.

Seguindo esses passos, você pode contornar os problemas relacionados a símbolos especiais nos nomes dos arquivos e continuar curtindo seus arquivos de mídia.

P.S. Você também pode transferir arquivos de áudio do seu MAC/PC para o iPhone usando o Compartilhamento de Arquivos do iTunes e reproduzir arquivos de áudio locais. Saiba mais sobre esse recurso em nosso guia: [Como reproduzir arquivos do iTunes no iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Perguntas frequentes

{{% details title="Posso transmitir música do meu PC para o meu iPhone sem o iTunes?" closed="true" %}}
Sim. O Evermusic se conecta ao seu PC via SMB na sua rede Wi-Fi local. O iTunes não é necessário. Basta ativar o compartilhamento de arquivos no seu PC e conectar no app.
{{% /details %}}

{{% details title="O streaming SMB usa dados móveis?" closed="true" %}}
Não. O SMB funciona pela sua rede Wi-Fi local. Não é necessária conexão com a internet ou dados móveis.
{{% /details %}}

{{% details title="Quais formatos de áudio o Evermusic suporta via SMB?" closed="true" %}}
O Evermusic suporta MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC e outros formatos de áudio comuns. Os arquivos são reproduzidos diretamente do compartilhamento SMB.
{{% /details %}}

{{% details title="Posso transmitir música de um NAS para o meu iPhone?" closed="true" %}}
Sim. Se o seu NAS suporta SMB (a maioria suporta, incluindo Synology, QNAP e WD My Cloud), você pode se conectar a ele usando os mesmos passos deste guia.
{{% /details %}}

{{% details title="Preciso manter meu computador ligado durante o streaming?" closed="true" %}}
Sim. Como o Evermusic transmite arquivos diretamente do seu computador, ele precisa estar ligado e conectado à mesma rede que seu iPhone.
{{% /details %}}

{{% details title="Existe um limite de tamanho de arquivo para streaming SMB?" closed="true" %}}
Não. O Evermusic transmite arquivos de qualquer tamanho via SMB. Arquivos lossless grandes (FLAC, WAV) funcionam sem problemas.
{{% /details %}}
