---
title: "Ficheiros"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aprenda a usar o separador Ficheiros no Evervideo no iPhone, iPad e Mac. Ligue serviços em nuvem, dispositivos NAS, servidores de multimédia e fluxos RTSP num só lugar. Gira vídeos offline, a fila de transferências, descarregamentos, Wi-Fi Drive, iTunes / Finder File Sharing e unidades USB. Inclui iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA e armazenamento compatível com S3."
keywords: [
  "ficheiros Evervideo", "conexões Evervideo", "ficheiros locais Evervideo",
  "configuração de vídeo em nuvem iPhone", "ligar Google Drive vídeo", "streaming SMB vídeo",
  "leitor WebDAV iOS", "vídeo DLNA iPhone", "streaming NAS vídeo",
  "transferência de vídeo Wi-Fi Drive", "Evervideo iTunes File Sharing", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "modo offline vídeo Evervideo", "fila de transferências Evervideo",
  "gestor de ficheiros Evervideo", "pasta Documentos Evervideo",
  "leitor de vídeo Synology", "leitor de vídeo QNAP",
  "leitor de vídeo Apple Time Capsule", "USB DAC vídeo",
  "leitor de vídeo iXpand", "leitor de vídeo S3"
]
tags: ["guia", "evervideo", "ficheiros", "conexões", "nuvem", "NAS", "Plex", "RTSP"]
readingTime: 14
---

O separador Ficheiros é o gestor de ficheiros tudo-em-um do Evervideo. Ao contrário da maioria das aplicações de vídeo que separam o armazenamento em nuvem dos ficheiros locais em separadores diferentes, o Evervideo combina ambos num único ecrã com scroll para que possa mover-se de um servidor Plex para uma pasta em nuvem para a pasta Documentos do iPhone sem saltar entre separadores.

O separador Ficheiros está dividido em secções claras que aparecem nesta ordem no ecrã:

- **Acesso Rápido** — recentes e favoritos para ficheiros e pastas que abriu mais recentemente.
- **Ficheiros Nesta Aplicação** — o que se encontra na pasta Documentos da sandbox do Evervideo.
- **Ficheiros Neste iPhone / iPad / Mac** — vídeos noutros locais no dispositivo, acessíveis através do seletor de ficheiros do sistema.
- **Armazenamento em Nuvem** — cada conta em nuvem, NAS e servidor de multimédia que ligou.
- **Dispositivos Disponíveis** — servidores e unidades detetados automaticamente por Bonjour / mDNS na sua rede local.

No canto superior direito do ecrã Ficheiros há um botão Transferências (ícone de setas giratórias). Toque nele para abrir a Fila de Transferências onde monitoriza cada descarregamento e envio de todas as suas fontes.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ficheiros Evervideo em Armazenamentos Ligados" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Ligar ao Armazenamento em Nuvem

A secção Armazenamento em Nuvem do separador Ficheiros é onde todas as contas ligadas, NAS, servidores de multimédia e fluxos ficam — lado a lado, numa lista com scroll.

{{< cards cols="1">}}
  {{< card title="" subtitle="Secção Armazenamento em Nuvem no Separador Ficheiros do Evervideo" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Abra o separador **Ficheiros**.
- Desça para a secção **Armazenamento em Nuvem**.
- Toque em **Ligar ao armazenamento em nuvem** no menu.
- Escolha um serviço de armazenamento em nuvem da lista.
- Introduza as suas credenciais na página de autorização oficial fornecida pelo fornecedor de nuvem, depois toque em **Concluído**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Ligar um Serviço de Armazenamento em Nuvem" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Se encontrar problemas, verifique a sua ligação à internet e o seu login / palavra-passe. Na versão Premium da aplicação, pode adicionar um número ilimitado de serviços; a versão gratuita suporta até três.

## Serviços de Armazenamento em Nuvem, Servidores de Multimédia e Protocolos Suportados

O Evervideo suporta uma gama excecionalmente ampla de fontes para os seus vídeos. Tudo abaixo funciona a partir de um único fluxo de Ligação ao armazenamento em nuvem.

**Armazenamento pessoal em nuvem:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servidores de multimédia auto-hospedados:** Plex · Jellyfin · Emby · Subsonic (e cada servidor compatível com Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (e ownCloud através da API partilhada) · Synology Drive · QNAP.

**Protocolos NAS e partilha de ficheiros:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, palavra-passe ou autenticação por chave pública) · NFS · DLNA / UPnP (reprodução e descarregamento).

**Fluxos ao vivo e câmeras IP:** RTSP — aponte o Evervideo para qualquer URL `rtsp://` e reproduz imediatamente. Ótimo para câmeras de segurança, fluxos IPTV, câmeras de campainha, monitores de bebé e fontes similares ao vivo.

**Armazenamento de objetos compatível com S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualquer outro endpoint de API S3.

**Bibliotecas no dispositivo:** a biblioteca de Fotografias (todos os vídeos, gravações de ecrã, álbuns de fotografias) e a biblioteca da aplicação Música (Álbuns, Géneros, Listas de reprodução) — ambas disponíveis dentro da Biblioteca de Multimédia sem necessidade de copiar nada.

**Descoberta de rede local:** a secção Dispositivos Disponíveis lista automaticamente todos os serviços Bonjour / mDNS na sua rede Wi-Fi — servidores Plex, Jellyfin, Emby, Synology, QNAP, routers AirPort com unidades anexadas, Apple Time Capsule — para que possa tocar para ligar sem digitar um endereço IP.

Cada ligação usa o SDK oficial ou o protocolo aberto do serviço, com autorização baseada em OAuth onde suportado. Pode ligar múltiplas contas do mesmo serviço (por exemplo, duas contas Google Drive, ou um servidor Plex e um Jellyfin) e navegar por elas lado a lado na secção Armazenamento em Nuvem.

## Segurança e Privacidade

O Evervideo usa apenas SDKs oficiais e ligações seguras para interagir com os serviços em nuvem ligados. O seu login e palavra-passe não são acessíveis à aplicação — todas as transferências são encriptadas por TLS.

Quando introduz o seu login e palavra-passe, a aplicação mostra-lhe a página de autorização oficial fornecida pelo fornecedor de serviços em nuvem, e todo o processo de autorização ocorre fora da aplicação. O fornecedor de serviços em nuvem envia então um token de autenticação para a aplicação após autorização bem-sucedida, e esse token é usado para fazer chamadas à API.

Um token de autenticação é uma chave digital que permite que aplicações de terceiros interajam com o armazenamento em nuvem em seu nome. O token é armazenado no dispositivo no armazenamento seguro de sistema da Apple (Keychain), que é encriptado em repouso e protegido pelo código de acesso do seu dispositivo ou bloqueio biométrico. Pode descarregar ficheiros dos serviços em nuvem ligados para o seu dispositivo; esses ficheiros são colocados no diretório Documentos da aplicação e podem ser removidos a qualquer momento usando o gestor de ficheiros incorporado.

A aplicação não partilha qualquer informação das suas contas em nuvem ligadas com a Everappz, anunciantes ou qualquer terceiro. Pode revogar o acesso à sua conta em nuvem a qualquer momento abrindo a página de definições da conta no seu navegador web.

## Revogar Token de Autenticação

Para revogar um token de autenticação, inicie sessão na sua conta em nuvem num navegador web e navegue até à página de segurança ou aplicações ligadas. Aí pode encontrar cada aplicação de terceiros que está ligada à sua conta em nuvem e remover qualquer uma delas se já não quiser utilizá-la. Instruções detalhadas para contas Google estão disponíveis [aqui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Também pode desligar a conta em nuvem dentro da própria aplicação — quando o fizer, o token de autenticação é imediatamente eliminado do seu dispositivo. Se desinstalar a aplicação do dispositivo, todos os dados descarregados e tokens de acesso são removidos automaticamente com ela.

## Desligar um Armazenamento em Nuvem ou Alterar Configuração

- **Aceder às opções de armazenamento em nuvem** — localize o serviço ligado na secção **Armazenamento em Nuvem** do separador Ficheiros.
- **Toque no botão "..."** ao lado do título do serviço para abrir opções adicionais:
  - **Renomear** — altere o nome do serviço em nuvem como aparece na sua lista.
  - **Configurações** — modifique a configuração ou os dados de autenticação. Às vezes pode ser necessário re-autorizar o serviço em nuvem ligado se o token de autorização expirou.
  - **Desconectar** — corte completamente a ligação entre a aplicação e o serviço em nuvem. Remove todos os vídeos associados a esse serviço da sua biblioteca de multimédia, mas deixa-os intactos no servidor.

## Ligar a um Computador ou NAS

Pode ligar o seu computador, NAS pessoal ou outro dispositivo de rede usando o protocolo SMB, WebDAV, FTP / FTPS, SFTP, NFS ou DLNA. Esta é a forma mais fácil de trazer uma biblioteca de multimédia doméstica existente — quer esteja num Mac, PC Windows, Synology, QNAP, Apple Time Capsule ou WD My Cloud Home — para o Evervideo sem copiar nada.

### Ligar a um Computador Usando SMB

- Toque em **Ligar ao armazenamento em nuvem → SMB**.
- Introduza o endereço IP do computador e o nome da pasta partilhada usando o formato `smb://endereco-ip-computador/nome-pasta-partilhada`.
- Escolha a versão do protocolo: **Auto**, **SMB1** ou **SMB2**.
- Introduza o seu login e palavra-passe (se necessário).
- Toque em **Concluído**.

Se a ligação for bem-sucedida, a partilha aparece na secção Armazenamento em Nuvem. Um tutorial completo sobre como ligar o Mac ou PC usando SMB está disponível [aqui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Ligar a um NAS Usando WebDAV

Todos os passos são os mesmos que para SMB, exceto o campo URL. Use `http://nome-servidor` ou `https://nome-servidor` se o servidor suportar SSL. WebDAV funciona com Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home e qualquer outro servidor com um endpoint WebDAV.

Um tutorial completo sobre WebDAV está disponível [aqui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Ligar via DLNA / UPnP

Partilhe uma biblioteca de multimédia localizada no seu PC Windows ou NAS usando o protocolo DLNA / UPnP e aceda a ela dentro do Evervideo conforme descrito [aqui](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA é amplamente suportado, mas apenas permite reproduzir ou descarregar vídeos — não pode enviar ficheiros ou criar novas pastas num servidor DLNA.

### Ligar Usando FTP, FTPS ou SFTP

O Evervideo também suporta os protocolos clássicos de transferência de ficheiros. Para ligar um servidor via FTP ou FTPS, toque em Ligar ao armazenamento em nuvem → FTP, introduza o URL do anfitrião no formato `ftp://nome-servidor` (ou `ftps://nome-servidor` para uma ligação encriptada), forneça o seu login e palavra-passe e toque em Concluído. Para SFTP (SSH File Transfer Protocol), escolha SFTP e forneça uma palavra-passe ou par de chaves SSH.

### Ligar a uma Partilha NFS

O Evervideo inclui suporte NFS (Network File System) — útil para anfitriões Linux, servidores BSD e dispositivos NAS que preferem expor bibliotecas de vídeo via NFS em vez de SMB. Escolha NFS no menu Ligar ao armazenamento em nuvem, introduza o endereço do servidor e o caminho exportado e toque em Concluído.

## Ligar um Plex Media Server

O Evervideo pode ligar diretamente a um Plex Media Server e navegar nas suas bibliotecas de Filmes, Séries de TV e Vídeos Domésticos. Toque em Ligar ao armazenamento em nuvem → Plex, inicie sessão com a sua conta Plex, escolha um servidor e a biblioteca aparece ao lado dos seus serviços em nuvem. Os servidores Plex na mesma rede local também são descobertos automaticamente na secção Dispositivos Disponíveis.

## Ligar um Servidor Jellyfin ou Emby

Tanto o Jellyfin (open-source) como o Emby (comercial) funcionam nativamente no Evervideo. Toque em Ligar ao armazenamento em nuvem → Jellyfin ou Emby, introduza o URL do servidor (tipicamente algo como `http://ip-servidor:8096`) e as credenciais, e a sua biblioteca está pronta para transmitir.

## Ligar um Servidor Subsonic ou Navidrome

O Evervideo fala a API Subsonic, o que significa que funciona com o próprio Subsonic, Navidrome e todos os outros servidores compatíveis com Subsonic — incluindo Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) e Ampache. Toque em Ligar ao armazenamento em nuvem → Subsonic, introduza o URL do servidor e as credenciais, e a biblioteca aparece na secção Armazenamento em Nuvem.

## Ligar um Fluxo RTSP (Câmeras IP, Live TV, IPTV)

O Evervideo tem suporte RTSP nativo, para que possa apontá-lo para qualquer fonte RTSP — câmeras de segurança, câmeras de campainha, fornecedores IPTV, monitores de bebé, sinais de transmissão — e o Evervideo irá capturar e descodificar o fluxo em direto. Toque em Ligações Online → Adicionar link, cole o URL completo (`rtsp://ip-camera:porta/caminho-fluxo`), forneça login e palavra-passe se necessário, e toque em Concluído.

## Ligar ao Armazenamento de Objetos Compatível com S3

Para utilizadores com alojamento próprio e utilizadores avançados que usam armazenamento de objetos em nuvem, o Evervideo inclui um conector compatível com S3. Toque em Ligar ao armazenamento em nuvem → Armazenamento S3, e depois introduza o URL do endpoint, região, chave de acesso, chave secreta e nome do bucket. Funciona com AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualquer outro endpoint de API S3.

## Dispositivos Disponíveis

Esta secção mostra cada dispositivo na sua rede local ao qual pode ligar-se a partir do Evervideo via descoberta Bonjour / mDNS — servidores Plex, Jellyfin, Emby, Synology, QNAP, routers AirPort com unidades anexadas, Apple Time Capsule, e assim por diante. Para estabelecer uma ligação:

- Desça até à secção Dispositivos Disponíveis no separador Ficheiros.
- Toque no dispositivo ao qual quer ligar-se.
- Se necessário, introduza os seus dados de início de sessão para completar a ligação.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Dispositivos Disponíveis na Rede Local" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

O Wi-Fi Drive permite transferir ficheiros sem fios do seu computador para o dispositivo iOS através de qualquer browser de secretária, Finder ou Explorador de Ficheiros. O seu dispositivo e computador devem estar na mesma rede Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Ativar Wi-Fi Drive

- No separador Ficheiros, desça até Armazenamento em Nuvem → Ligar via Wi-Fi para abrir o ecrã principal do Wi-Fi Drive.
- (Opcional) Defina um nome de utilizador e palavra-passe para o servidor web incorporado.
- Toque em Iniciar Wi-Fi Drive.

### Aceder ao Wi-Fi Drive no Computador

- Abra um browser no seu computador (Chrome, Firefox, Safari, etc.).
- Introduza o URL mostrado pela aplicação.
- Arraste e largue ficheiros do seu computador para a página web — começarão a ser transferidos para o dispositivo iOS.

Também pode montar o Wi-Fi Drive diretamente no **Finder** no macOS (Ir → Ligar ao Servidor…) ou no Explorador de Ficheiros no Windows (Mapear Unidade de Rede…) e tratar o iPhone ou iPad como uma unidade de rede normal.

Instruções detalhadas estão disponíveis [aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

O iTunes File Sharing (agora Finder File Sharing no macOS Catalina e posterior) permite transferir ficheiros usando um cabo Lightning ou USB-C. Ligue o dispositivo, abra o Finder no Mac (ou iTunes no Windows), encontre o Evervideo na lista de aplicações e copie os ficheiros para a sua pasta partilhada.

## Ligar uma Pen USB ou Cartão SD

Ligue uma pen USB ou cartão SD ao iPhone, iPad ou Mac através do adaptador Lightning-para-USB / USB-C ou leitor de cartões. Abra Ficheiros → Ficheiros Neste iPhone → Abrir Pasta, navegue até à unidade e escolha um ficheiro de vídeo ou pasta. O Evervideo reproduz ficheiros diretamente da unidade sem os copiar para o armazenamento interno — útil para grandes bibliotecas 4K.

## Navegação de Pastas em Armazenamentos Ligados

Toque em qualquer serviço em nuvem ligado para abrir o seu navegador de ficheiros. As pastas mostram miniaturas de vídeo quando disponíveis, e tocar num vídeo inicia a reprodução imediatamente enquanto continua a transmitir o resto do ficheiro em segundo plano.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Navegar Pastas em Armazenamentos Ligados" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Acesso Rápido

A secção Acesso Rápido fica no topo do separador Ficheiros. Dá-lhe acesso rápido aos seus ficheiros e pastas favoritos e abertos recentemente — tanto de serviços em nuvem como do armazenamento no dispositivo. Sempre que abre um ficheiro ou pasta da nuvem, é adicionado à lista de Abertos Recentemente. Pode marcar pastas profundamente aninhadas como Favoritos para aceder rapidamente sem ter de percorrer a estrutura de diretórios.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Ligações Online e Acesso Rápido" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Ficheiros Nesta Aplicação

Esta secção mostra ficheiros e pastas armazenados no diretório Documentos da sandbox do Evervideo — tudo o que descarregou da nuvem, transferiu via Wi-Fi Drive, copiou através do Finder File Sharing ou importou de outra aplicação.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Ficheiros Nesta Aplicação" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Pasta Documentos

A pasta Documentos é a raiz de tudo dentro de Ficheiros Nesta Aplicação. Pode criar subpastas, renomear ficheiros, movê-los e agrupá-los como quiser.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Ficheiros Locais — Pasta Documentos" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Ficheiros Neste iPhone / iPad / Mac

Esta secção mostra vídeos localizados no dispositivo mas em aplicações diferentes. Pode importá-los para o Evervideo usando o seletor de ficheiros do sistema:

- Toque em Abrir Ficheiros… para selecionar ficheiros específicos.
- Toque em Abrir Pasta… para selecionar uma pasta inteira.

Também pode usar Ligar uma Pasta para criar uma ligação a uma pasta no dispositivo com acesso de leitura / escrita — perfeito para trabalhar com uma pasta no iCloud Drive ou uma unidade USB anexada sem copiar nada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Ficheiros Neste Dispositivo" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Pastas Especiais

No separador Ficheiros verá várias pastas especiais que o Evervideo cria e usa automaticamente:

- **Baixar** — cada ficheiro descarregado da nuvem aparece aqui por predefinição. Personalize em Configurações → Gestor de Ficheiros → Guardar Ficheiros Descarregados Em.
- **Cache do Leitor** — a cache do leitor de multimédia. Por predefinição, o leitor descarrega vídeos futuros para reprodução suave. Pode desativar a cache nas configurações da aplicação ou simplesmente eliminar esta pasta.
- **iCloud** — os ficheiros nesta pasta sincronizam em todos os seus dispositivos ligados à mesma conta iCloud.
- **Pastas offline** — quando marca uma pasta, lista de reprodução, álbum ou género como disponível offline, os ficheiros são descarregados para esta pasta.

## Barra de Ferramentas Superior

A barra de ferramentas superior, localizada sob a barra de navegação, oferece várias ações que pode mostrar ou ocultar com um gesto de deslize para baixo:

- **Pesquisa** — realize uma pesquisa dentro da pasta ou secção atual.
- **Continuar Reprodução** — se ativado nas configurações, restaura a fila do leitor e a última posição do vídeo para a pasta atual.
- **Reproduzir Tudo** — analise a pasta atual e as suas subpastas e adicione ficheiros à fila do leitor.
- **Ordem Aleatória** — como Reproduzir Tudo, mas mistura antes de adicionar.

## Opções de Pasta

Quando abre uma pasta, toque no botão **"..."** no canto superior direito para estas ações:

- **Selecionar** — ativar o modo de seleção de ficheiros.
- **Nova Pasta** — criar uma nova pasta dentro da pasta atual.
- **Ativar Modo Offline** — ativar sincronização offline para a pasta atual. Novos ficheiros adicionados online são descarregados automaticamente.
- **Enviar Ficheiros** — enviar ficheiros do dispositivo para a pasta online.
- **Pesquisa** — pesquisar dentro da pasta.
- **Ordenar** — ordenar ficheiros por nome, tamanho, data de modificação ou metadados.
- **Vista em Grelha / Lista** — alternar entre vista de tabela e vista de miniaturas. A vista de miniaturas mostra grandes pré-visualizações de cartaz de vídeo.

## Modo de Seleção

Toque em **"..."** no canto superior direito e escolha **Selecionar** para entrar no modo de seleção. Aparecem caixas de verificação ao lado de cada ficheiro e pasta. Toque para selecionar um ou vários itens e depois realize ações em lote: Reproduzir a Seguir, Reproduzir Mais Tarde, Adicionar à Biblioteca de Multimédia, Adicionar a uma Lista de Reprodução, Copiar, Enviar, Mover, Renomear ou Eliminar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Modo de Seleção no Gestor de Ficheiros" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Se preferir tratar o armazenamento em nuvem ligado como somente leitura (para evitar eliminações acidentais), ative Configurações → Gestor de Ficheiros → Editar Ficheiros Online → Desativado para ocultar todas as operações destrutivas da interface.

## Ações de Ficheiro

Toque no ícone **"..."** perto do título de um ficheiro para revelar o menu de ações:

- **Reproduzir a Seguir** — insira o ficheiro no topo da fila do leitor.
- **Reproduzir Mais Tarde** — adicione o ficheiro ao fim da fila do leitor.
- **Adicionar à Biblioteca de Multimédia** — incorpore o ficheiro na sua biblioteca de multimédia, organizada por Álbum e Género.
- **Adicionar a uma Lista de Reprodução** — adicione o ficheiro a uma lista de reprodução existente ou crie uma nova.
- **Editar Etiquetas** — abra o editor de etiquetas incorporado para modificar metadados. Para ficheiros online, o ficheiro é temporariamente descarregado, editado e depois reenviado após confirmação.
- **Adicionar aos Favoritos** — adicione o ficheiro à sua lista de favoritos para acesso rápido.
- **Baixar** — descarregue o ficheiro ou pasta para o dispositivo para uso offline.
- **Renomear** — renomeie o ficheiro diretamente no armazenamento remoto.
- **Mover** — mova o ficheiro para uma pasta diferente no armazenamento em nuvem.
- **Adicionar ao Arquivo** — agrupe o ficheiro num único ficheiro ZIP (funcionalidade Premium).
- **Abrir Em** — exporte o ficheiro para outra aplicação compatível através da folha de partilha do sistema.
- **Excluir** — remova permanentemente o ficheiro. **Esta ação não pode ser desfeita.**

## Ações de Pasta

Para cada pasta no armazenamento em nuvem, tem muitas ações disponíveis tocando no ícone **"..."** ao lado do título da pasta.

- **Reproduzir Tudo** — substitua a fila atual do leitor por cada vídeo na pasta.
- **Reproduzir a Seguir / Reproduzir Mais Tarde** — adicione a pasta inteira à fila.
- **Adicionar à Biblioteca de Multimédia** — incorpore o conteúdo da pasta na sua biblioteca de multimédia.
- **Adicionar à Lista de Reprodução** — adicione a pasta inteira a uma lista de reprodução.
- **Adicionar aos Favoritos** — adicione a pasta aos seus favoritos.
- **Ativar Modo Offline** — para além de um simples descarregamento, monitoriza continuamente a pasta em busca de novos ficheiros e descarrega-os automaticamente quando aparecem online.
- **Baixar** — descarregue todo o conteúdo da pasta para o dispositivo para acesso offline.
- **Renomear / Mover** — renomeie ou mova a pasta no armazenamento remoto.
- **Adicionar ao Arquivo** — agrupe o conteúdo da pasta num ficheiro ZIP (funcionalidade Premium).
- **Excluir** — remova permanentemente a pasta e o seu conteúdo. **Esta ação não pode ser desfeita.**

## Fila de Transferências

No canto superior direito do separador Ficheiros há um botão **Transferências** (ícone de setas giratórias). Toque nele para abrir a Fila de Transferências — uma lista de cada descarregamento e envio ativo de todas as suas fontes, com progresso em tempo real, velocidade e ETA por ficheiro.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Fila de Transferências de Ficheiros" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Pode pausar, retomar, repetir transferências falhadas, reorganizar itens para priorizar descarregamentos específicos ou cancelá-los individualmente. Também pode ajustar a velocidade da fila de transferências (máximo de tarefas paralelas), tipo de rede (apenas Wi-Fi ou Wi-Fi + Celular) e transferências em segundo plano em Configurações → Gestor de Ficheiros.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Ações na Fila de Transferências de Ficheiros" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Modo Offline e Pastas Offline Sincronizadas

O modo offline é uma funcionalidade útil que lhe permite ver os seus vídeos favoritos mesmo quando não está ligado à internet. Quando ativa o modo offline para qualquer pasta, lista de reprodução, álbum ou género, todos os ficheiros dessa coleção são automaticamente descarregados para o dispositivo para reprodução offline. Aparecem na secção Pastas offline.

Quando adiciona novos ficheiros ao servidor remoto, eles também são descarregados automaticamente — para que a sua coleção offline se mantenha atualizada sem que faça nada. Para sincronizar manualmente, toque nos três pontos no canto superior direito de uma pasta offline e selecione Sincronizar.

Pode ajustar o tempo limite de sincronização em Configurações → Gestor de Ficheiros → Pastas offline sincronizadas → Intervalo de Tempo.

Instruções detalhadas estão disponíveis [aqui](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalização

Em Configurações → Personalização pode configurar a forma como o separador Ficheiros é apresentado:

- **Estilo do Ecrã de Ficheiros** — Menu Simples (mostra a lista de pastas diretamente) ou Menu Agrupado (agrupa o conteúdo por categoria — Acesso Rápido, Pastas Especiais, Armazenamento em Nuvem, etc.).
