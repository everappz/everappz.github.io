---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Aprenda a usar o Evervideo — o leitor de vídeo em nuvem tudo-em-um para iPhone, iPad e Mac. Transmita e descarregue vídeos do iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA e S3 — além de Plex, Jellyfin, Emby, Subsonic e Navidrome. Imagem-em-imagem, legendas primárias e secundárias, equalizadores de áudio e vídeo, transmissões de câmeras RTSP, Chromecast, AirPlay 2, descodificação H.264 / HEVC por hardware, integração com Fotografias e Apple Music e um leitor compacto sempre no ecrã.'
keywords: [
  "guia Evervideo", "como usar Evervideo", "leitor de vídeo em nuvem iPhone", "leitor de vídeo Mac",
  "leitor MKV iOS", "leitor de vídeo FFmpeg", "leitor HEVC iPhone",
  "imagem-em-imagem iPhone", "leitor PiP iPad",
  "leitor RTSP iPhone", "visualizador de câmeras IP", "leitor DLNA vídeo",
  "cliente Plex iPhone", "cliente Jellyfin iOS", "cliente Emby iPad",
  "leitor de legendas iOS", "legendas SRT VTT ASS", "legendas secundárias iPhone",
  "equalizador de vídeo iOS", "equalizador de áudio para vídeo", "DAC externo vídeo",
  "transmitir vídeo do Google Drive", "transmitir vídeo do Dropbox",
  "transmitir vídeo do OneDrive", "transmitir vídeo do iCloud Drive",
  "transmitir vídeo do MEGA", "transmitir vídeo do NAS",
  "Chromecast vídeo iPhone", "AirPlay 2 vídeo", "leitor de vídeo iCloud",
  "leitor de vídeo biblioteca Fotografias", "leitor de vídeo Apple Music",
  "transferência de vídeo Wi-Fi Drive", "lista de reprodução M3U",
  "Evervideo Premium", "aplicação de vídeo Family Sharing"
]
tags: ["evervideo", "guia", "leitor de vídeo", "PiP", "legendas", "RTSP", "nuvem", "FFmpeg"]
---


### Bem-vindo ao Guia do Evervideo

O Evervideo é um leitor de multimédia em nuvem completo para iPhone, iPad e Mac que transforma qualquer conta de armazenamento em nuvem, NAS ou servidor de multimédia na sua biblioteca de multimédia pessoal, sem necessidade de reenviar nada e mantendo o controlo total dos seus ficheiros.

Construído com um motor de leitor personalizado baseado em FFmpeg com descodificação H.264 e HEVC acelerada por hardware, o Evervideo reproduz praticamente qualquer contêiner e codec modernos — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS e a vasta lista de formatos FFmpeg — com qualidade total, com armazenamento temporário inteligente para transmissão suave por Wi-Fi ou rede móvel. A Imagem-em-imagem mantém o vídeo sobre todas as outras aplicações, o leitor compacto sempre no ecrã permite continuar a ver enquanto navega na biblioteca, e o Chromecast e AirPlay 2 enviam a reprodução para a televisão, HomePod ou sistema de som com um toque.

O Evervideo liga-se a uma lista notavelmente ampla de fontes, todas a partir de uma única aplicação:

- **Armazenamento em nuvem pessoal:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidores de multimédia auto-hospedados:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (e ownCloud através da API partilhada) · Synology Drive · QNAP.
- **Protocolos NAS e partilha de ficheiros:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (palavra-passe ou autenticação por chave pública) · NFS · DLNA · UPnP.
- **Transmissões ao vivo e câmeras IP:** RTSP — aponte o Evervideo para qualquer URL RTSP (`rtsp://ip-da-câmera/fluxo`) e reproduz imediatamente.
- **Armazenamento de objetos compatível com S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualquer outro endpoint da API S3.
- **Fontes no dispositivo:** a biblioteca de Fotografias (Todos os Vídeos, Curtos / Médios / Longos, Gravações de Ecrã e Álbuns de Fotografias), a biblioteca da aplicação Música (Álbuns, Géneros, Listas de reprodução), unidades USB / cartões SD e Ficheiros Locais.

### Um Leitor para Todos os Formatos e Codecs

Enquanto a maioria das aplicações iOS se limita a H.264 / H.265 em MP4 / MOV, o Evervideo inclui FFmpeg juntamente com os codecs de sistema da Apple para que possa reproduzir formatos que o sistema não reconhece — contêineres MKV, VP9, AV1, MPEG-2, OGG, Vorbis e muitos mais — e alterna automaticamente entre descodificação H.264 / HEVC por hardware e descodificação por software com base no ficheiro e no dispositivo.

Pode selecionar a faixa de vídeo (rips de Blu-ray com múltiplos fluxos), a faixa de áudio (faixas de comentários, dobragens alternativas) e a faixa de legendas. Ficheiros de legendas externos SRT, VTT e ASS / SSA carregam com um toque; a estilização avançada ASS / SSA é renderizada corretamente graças à biblioteca libass incluída.

### Legendas Inteligentes

- **Seleção de faixa de legendas** — perfeita para aprender idiomas.
- **Ficheiros de legendas externos** (`.srt`, `.vtt`, `.ass`, `.ssa`) carregados de qualquer lugar no dispositivo ou da nuvem.
- **libass** — renderização de ASS / SSA totalmente estilizada.
- **Seleção de tipo de letra por faixa e global** para legendas.
- **Seleção de faixa de áudio** — escolha a dobragem, comentário ou faixa do realizador.
- **Seleção de faixa de vídeo** — para ficheiros com múltiplos ângulos ou versões.

### Ajuste a Imagem e o Som

Dois equalizadores lado a lado: um equalizador de áudio para ajustar graves e agudos (com importação / exportação de predefinições personalizadas) e um equalizador de vídeo para ajustar brilho, contraste, saturação e matiz (também com importação / exportação). Ambos os motores também expõem controlos audiófilo: taxa de amostragem de saída de áudio, número de canais, duração do buffer IO e **Modo misto** — para utilizadores com DACs externos e recetores de home theater.

### Cast, AirPlay e Imagem-em-imagem

- **Imagem-em-imagem (PiP):** continue a ver enquanto usa outras aplicações.
- **AirPlay 2:** envie vídeo para Apple TV, HomePod ou qualquer altifalante / TV AirPlay 2.
- **Google Chromecast:** transmita diretamente para um Chromecast ou TV compatível com Cast.
- **Leitor compacto:** um mini-leitor persistente no topo de cada ecrã para que possa navegar na biblioteca sem perder o vídeo.

### Privacidade e Segurança

O Evervideo utiliza SDKs oficiais e inícios de sessão baseados em OAuth de cada fornecedor de nuvem para que a sua palavra-passe nunca chegue à aplicação. Os tokens de acesso vivem encriptados no iOS/MacOS Keychain, cada transferência é protegida por TLS e revogar o acesso a partir da sua conta na nuvem (ou remover o Evervideo do dispositivo) elimina tudo instantaneamente. Proteja a sua biblioteca com um código de acesso opcional de 4 dígitos para uma camada extra de privacidade.

### Primeiros Passos com o Evervideo

Este guia percorre cada parte do Evervideo no iPhone, iPad e Mac — desde a ligação de serviços em nuvem, navegação na biblioteca, descarregamento e transferência de ficheiros, gestão de listas de reprodução, até ao ajuste fino do leitor de multimédia, equalizadores, legendas e Imagem-em-imagem. Use os cartões abaixo para ir diretamente à secção de que necessita.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navegação" subtitle="Barra de separadores no iPhone, menu esquerdo no iPad e Mac, leitor de multimédia compacto sempre no ecrã." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Ficheiros" subtitle="Um separador unificado para nuvem, NAS, transmissões RTSP, ficheiros locais, unidades USB e a fila de transferências." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Biblioteca de Multimédia" subtitle="Navegue por Álbuns, Géneros, Recentes, Favoritos — além da biblioteca de Fotografias iOS e Apple Music." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Listas de reprodução" subtitle="Crie listas de reprodução a partir da nuvem, ficheiros locais, Fotografias ou biblioteca de Música, importe M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Leitor de Multimédia" subtitle="Imagem-em-imagem, faixas de áudio e vídeo, legendas, equalizadores de áudio e vídeo, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Configurações" subtitle="Motor de áudio, descodificador de vídeo, legendas, biblioteca, gestor de ficheiros, widgets, personalização, idioma, cópia de segurança." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Encontre respostas para as perguntas mais comuns sobre o Evervideo." >}}

{{< /cards >}}
