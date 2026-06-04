---
date: 2020-01-01
title: 'Flacbox'
description: 'Aprenda a usar o Flacbox — o leitor de música hi-res com FLAC, DSD, ALAC e FFmpeg para iPhone, iPad e Mac. Ligue o iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB e DLNA. Transmita e descarregue áudio de alta resolução, edite metadados, ouça audiolivros, faça scrobbling no Last.fm, use o Apple CarPlay e widgets do ecrã inicial, e personalize o equalizador de 10 bandas.'
keywords: [
  "guia Flacbox", "como usar Flacbox", "leitor de música hi-res iPhone", "leitor FLAC iPhone",
  "leitor DSD iOS", "leitor ALAC Mac", "aplicação de música sem perdas", "leitor de música na nuvem iPhone",
  "leitor FLAC offline Mac", "gestor de biblioteca musical", "editor de tags de áudio",
  "leitor FLAC CarPlay", "aplicação áudio Chromecast", "música AirPlay 2",
  "widgets Flacbox", "Flacbox CarPlay", "leitor de música FFmpeg iOS",
  "leitor de audiolivros iPhone", "marcadores de áudio iOS", "aplicação de correção de tom",
  "taxa de amostragem de saída de áudio", "DAC externo iPhone", "USB DAC Mac",
  "aplicação de música Synology", "aplicação de música QNAP", "leitor de música NAS iPhone",
  "leitor WebDAV", "streaming SMB", "leitor DLNA",
  "música iCloud Drive", "Google Drive FLAC", "leitor FLAC Dropbox",
  "transferência de música Wi-Fi Drive", "importação de lista M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "guia", "hi-res", "FLAC", "FFmpeg", "nuvem", "CarPlay", "widgets"]
---


### Bem-vindo ao Guia do Flacbox

O Flacbox é um leitor de música de alta resolução para iPhone, iPad e Mac que lhe permite transformar o seu serviço de armazenamento na nuvem favorito, NAS e servidores de media no seu serviço de streaming pessoal.

O Flacbox liga-se a uma lista notavelmente ampla de fontes, tudo numa só aplicação:

- **Armazenamento pessoal na nuvem:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidores auto-hospedados:** Plex · Jellyfin · Emby · Subsonic (e todos os servidores compatíveis com Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (e ownCloud via API partilhada) · Synology Drive · QNAP.
- **Protocolos NAS e partilha de ficheiros:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (palavra-passe ou autenticação por chave pública) · NFS · DLNA / UPnP (reprodução e transferência). Funciona com Apple Time Capsule, Synology, QNAP, WD My Cloud, qualquer host Linux Samba / NFS / SSH, ou uma pasta partilhada no seu Mac ou PC Windows.
- **Armazenamento de objetos compatível com S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, e qualquer outro endpoint S3-API.
- **Descoberta na rede local:** A secção Dispositivos disponíveis lista automaticamente todos os serviços Bonjour / mDNS na sua rede Wi-Fi — servidores Plex, Jellyfin, Emby, Synology, QNAP, routers AirPort com discos ligados, Time Capsule — para que possa ligar sem digitar um endereço IP.

Enquanto a maioria das aplicações de música usa o motor de áudio integrado da Apple, o Flacbox inclui o **FFmpeg** ao lado dos codecs do sistema para que possa reproduzir formatos que o iOS não suporta nativamente — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, além da família MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. Combinado com uma taxa de amostragem de saída de áudio configurável (44,1 / 48 / 64 / 88,2 / 96 kHz), saída multicanal (Mono → 5.1 → SDDS → ITU BS.775-1), ajuste do buffer IO e correção de tom, o Flacbox dá aos audiófilos um controlo que a maioria das aplicações de música para consumidores simplesmente não oferece.

### Desfrute de Streaming Suave e Reprodução Offline

O Flacbox inclui buffering inteligente para streaming suave e um gestor de transferências integrado para que possa descarregar listas de reprodução, artistas, álbuns, pastas ou faixas individuais para o seu dispositivo para uso offline. Quando o armazenamento estiver a ficar cheio, limpe os ficheiros em cache com um toque e continue a transmitir da nuvem. O Modo offline para pastas, listas de reprodução, álbuns e artistas também sincroniza automaticamente novas faixas assim que aparecem na nuvem, para que a sua coleção offline esteja sempre atualizada.

### Biblioteca Musical Organizada Automaticamente

Quando importa faixas de áudio, o Flacbox analisa os seus metadados e organiza-as numa Biblioteca Musical limpa — agrupadas por Músicas, Músicas não reproduzidas, Álbuns, Artistas de álbum, Artistas, Géneros e Compositores. Use a pesquisa integrada para encontrar qualquer coisa em segundos, filtre por fonte (nuvem online / offline / dispositivo), e escolha entre os layouts de biblioteca Simples / Agrupado / Com separadores. Para bibliotecas com compilações de 'vários artistas' misturadas, o Flacbox fornece vistas dedicadas Todos os álbuns / Álbuns exclusivos / Álbuns a solo para apresentar os resultados certos sem ruído.

### Corrija Metadados e Etiquete a Sua Música

Se encontrar tags corrompidas ou codificações desorganizadas (um problema comum em ficheiros rippados ou mais antigos), o editor de tags ID3 integrado pode limpá-las — manualmente ou com pesquisas automáticas no MusicBrainz. Também pode normalizar codificações de caracteres danificadas (ótimo para tags em cirílico, japonês ou chinês provenientes de PCs Windows), pesquisar capas de álbum em falta, e escrever as alterações de volta ao ficheiro original na nuvem automaticamente. Para edição em lote mais aprofundada, instale a nossa aplicação complementar Evertag.

### Transferências Fáceis do Mac, PC ou NAS

Mova música entre o seu computador e o seu iPhone ou iPad com qualquer uma destas ferramentas: SMB, WebDAV, DLNA, Wi-Fi Drive (arrastar e largar em qualquer browser de desktop), Partilha de Ficheiros iTunes / Finder por cabo Lightning ou USB-C, pen drives USB, ou iXpand Flash Drives. Tem um Apple Time Capsule, WD My Cloud, Synology, QNAP, ou outro NAS que expõe SMB / WebDAV / DLNA / FTP / SFTP? Ligue uma vez e transmita toda a sua biblioteca sem ocupar espaço no dispositivo.

### Personalize o Som com o Equalizador

O Flacbox inclui um equalizador de 10 bandas com predefinições estilo iPod (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz, e muitos mais), um pré-amplificador, e a capacidade de guardar as suas próprias predefinições. Quer esteja a ajustar para uns IEMs audiófilo, um HomePod mini, ou um sistema de som do carro, pode moldar o som exatamente como prefere.

### Amigo dos Audiolivros

O Flacbox é um excelente leitor de audiolivros — múltiplos marcadores por faixa, velocidade de reprodução precisa (0,02× a 3,00×), continuar a reprodução exatamente onde parou, botões de salto personalizáveis, e um temporizador de sono que vai diminuindo gradualmente antes de dormir. Os marcadores de capítulos M4B e ficheiros longos são totalmente suportados.

### Transmita em Qualquer Lugar — Incluindo no Carro e no Ecrã Inicial

Transmita música para Apple TV / HomePod via AirPlay 2, envie para colunas Google Chromecast e TVs com Cast, e leve tudo na estrada com o Apple CarPlay. Use widgets no ecrã inicial no iPhone e iPad para ver a faixa a tocar de relance, e o scrobbling Last.fm para manter o seu histórico de escuta em todas as aplicações.

### Privacidade e Segurança

O Flacbox usa apenas SDKs oficiais e logins baseados em OAuth de cada fornecedor de nuvem — a sua palavra-passe nunca chega à aplicação. Os tokens de acesso ficam encriptados no iOS Keychain, todas as transferências são protegidas por TLS, e revogar o acesso na sua conta na nuvem ou remover o Flacbox do dispositivo apaga tudo imediatamente. Proteja a sua biblioteca com um código de acesso opcional para uma camada extra de privacidade.

### Primeiros Passos com o Flacbox

Este guia acompanha-o por cada parte do Flacbox no iPhone, iPad e Mac — desde a ligação de serviços de nuvem, organização da biblioteca, transferência de ficheiros e gestão de listas de reprodução, até ao ajuste fino do equalizador e configuração do motor de áudio. Use os cartões abaixo para ir diretamente à secção de que precisa.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navegação" subtitle="Barra de separadores no iPhone, menu esquerdo no iPad e Mac, mini leitor, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Conexões" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Biblioteca Musical" subtitle="Músicas, álbuns, artistas, géneros, compositores — sincronização, pesquisa, edição de metadados." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Listas de reprodução" subtitle="Crie, importe M3U / M3U8 / CUE, reordene e exporte para M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Ficheiros Locais" subtitle="Música offline, pen drives USB, Wi-Fi Drive, gestor de ficheiros, pastas offline." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Leitor de Áudio" subtitle="Saída hi-res, equalizador, correção de tom, marcadores, AirPlay, Chromecast, velocidade, temporizador de sono." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Configurações" subtitle="Motor de áudio, biblioteca, gestor de ficheiros, CarPlay, widgets, personalização, idioma, cópia de segurança." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Encontre respostas às 50 perguntas mais comuns sobre o Flacbox." >}}

{{< /cards >}}
