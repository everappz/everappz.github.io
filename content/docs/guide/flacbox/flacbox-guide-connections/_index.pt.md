---
title: "Conexões"
date: 2020-02-01
description: "Aprenda a ligar serviços de nuvem e dispositivos NAS ao Flacbox. Transmita música de alta resolução do iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk e mais. Use SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, Partilha de Ficheiros iTunes / Finder e pen drives USB."
keywords: [
  "configuração cloud Flacbox", "ligar Google Drive ao Flacbox", "streaming SMB",
  "leitor WebDAV iOS", "aplicação DLNA", "streaming áudio NAS", "Wi-Fi Drive iPhone",
  "transferir ficheiros para iPhone", "Flacbox Partilha Ficheiros iTunes", "ligar NAS ao iPhone",
  "aplicação música Synology Drive", "aplicação música QNAP", "aplicação música Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "aplicação música scrobbling Last.fm",
  "música iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["guia", "flacbox", "conexões", "nuvem", "NAS"]
readingTime: 12
---


Neste ecrã, pode ligar todas as fontes que contêm a sua música. Pode integrar serviços de nuvem populares como Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive e muitos mais, bem como o seu Mac, PC ou NAS através de protocolos padrão. Quer a sua coleção esteja num serviço compatível com streaming como o Dropbox ou num NAS pessoal como Synology, QNAP, Buffalo, Apple Time Capsule ou WD My Cloud Home, o Flacbox liga-se a todos a partir de um único ecrã.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecrã de Conexões do Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Ligar ao Armazenamento na Nuvem

- Abra o separador **Conexões**.
- Selecione **Ligar ao armazenamento na nuvem** no menu.
- Escolha um serviço de armazenamento na nuvem da lista.
- Introduza as suas credenciais na página de autorização oficial fornecida pelo fornecedor de nuvem, e depois toque em **Concluído**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Adicionar um Serviço de Armazenamento na Nuvem" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Se encontrar algum problema, verifique a sua ligação à internet e o seu login / palavra-passe. Na versão Premium da aplicação, pode adicionar um número ilimitado de serviços; a versão gratuita suporta até três.

## Serviços de Armazenamento na Nuvem, Servidores de Media e Protocolos Suportados

O Flacbox suporta uma gama excecionalmente ampla de fontes para a sua música. Tudo abaixo funciona a partir de um único ecrã **Ligar ao armazenamento na nuvem**.

**Armazenamento pessoal na nuvem:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servidores auto-hospedados:** Plex · Jellyfin · Emby · Subsonic (e todos os servidores compatíveis com Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (e ownCloud via API partilhada) · Synology Drive · QNAP.

**Protocolos NAS e partilha de ficheiros:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, palavra-passe ou autenticação por chave pública) · NFS · DLNA / UPnP (reprodução e transferência).

**Armazenamento de objetos compatível com S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualquer outro endpoint S3-API.

**Descoberta na rede local:** A secção Dispositivos disponíveis lista automaticamente cada serviço Bonjour / mDNS na sua rede Wi-Fi para que possa ligar sem digitar endereços IP.

Cada ligação usa o **SDK oficial ou protocolo aberto** do serviço, com autorização baseada em OAuth onde suportado. Pode ligar várias contas do mesmo serviço (por exemplo, duas contas Google Drive, um Dropbox pessoal ao lado de um do trabalho, ou um servidor Plex e um Jellyfin) e navegar por eles lado a lado no ecrã de Conexões.

## Segurança e Privacidade

Usamos apenas SDKs oficiais e ligações seguras para interagir com serviços de nuvem ligados. O seu login e palavra-passe não são acessíveis à aplicação — todas as transferências são encriptadas com TLS.

Quando introduz o seu login e palavra-passe, a aplicação mostra-lhe a página de autorização oficial fornecida pelo fornecedor do serviço de nuvem, e todo o processo de autorização acontece fora da aplicação. O fornecedor do serviço de nuvem envia então um token de autenticação para a aplicação após autorização bem-sucedida, e esse token é usado para fazer chamadas de API.

Um token de autenticação é uma chave digital que permite a aplicações de terceiros interagir com o armazenamento na nuvem em seu nome. O token é armazenado no seu dispositivo no armazenamento seguro do sistema da Apple (Keychain), que está encriptado em repouso e protegido pelo código de acesso do seu dispositivo ou bloqueio biométrico. Pode descarregar ficheiros dos serviços de nuvem ligados para o seu dispositivo; esses ficheiros são colocados no diretório Documentos da aplicação e podem ser removidos a qualquer momento usando o gestor de ficheiros integrado.

A aplicação não partilha qualquer informação das suas contas de nuvem ligadas com a Everappz, anunciantes, ou qualquer terceiro. Pode revogar o acesso à sua conta de nuvem a qualquer momento abrindo a página de definições da conta no seu browser.

## Rejeitar Token de Autenticação

Para revogar um token de autenticação, inicie sessão na sua conta de nuvem num browser e navegue até à página de segurança ou aplicações ligadas. Aí pode encontrar cada aplicação de terceiros que está ligada à sua conta de nuvem e remover qualquer uma delas se já não quiser usá-la. Instruções detalhadas para contas Google estão disponíveis [aqui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Também pode desligar a conta de nuvem dentro da própria aplicação — quando o fizer, o token de autenticação é imediatamente eliminado do seu dispositivo. Se desinstalar a aplicação do seu dispositivo, todos os dados descarregados e tokens de acesso são removidos automaticamente junto com ela.

## Desligar um Armazenamento na Nuvem ou Alterar Configuração

- **Aceder às opções de armazenamento na nuvem** — localize o serviço ligado no ecrã **Conexões**.
- **Toque no botão "..."** junto ao título do serviço para abrir opções adicionais:
  - **Renomear** — altere o nome do serviço de nuvem como aparece na sua lista.
  - **Configurações** — modifique a configuração ou dados de autenticação. Por vezes pode precisar de reautorizar o serviço de nuvem ligado se o token de autorização tiver expirado.
  - **Desconectar** — corte completamente a ligação entre a aplicação e o serviço de nuvem. Isto remove todas as músicas associadas a esse serviço da biblioteca musical da aplicação, mas deixa-as intocadas no servidor.

## Ligar a um Computador ou NAS

Também pode ligar o seu computador, NAS pessoal, ou outros dispositivos de rede usando os protocolos SMB, DLNA ou WebDAV. Esta é a forma mais fácil de trazer uma biblioteca de música doméstica existente — seja ela num Mac, PC Windows, caixa Synology, ou NAS — para o Flacbox sem copiar nada.

## Ligar a um Computador Usando SMB

- Toque em **Ligar ao armazenamento na nuvem → SMB**.
- Introduza o endereço IP do computador e o nome da pasta partilhada no campo URL usando o formato `smb://endereço-ip-computador/nome-pasta-partilhada`.
- Escolha a versão do protocolo: **Auto**, **SMB1** ou **SMB2**.
- Introduza o seu login e palavra-passe (se necessário).
- Toque em **Concluído**.

Se a ligação for bem-sucedida, verá o armazenamento ligado na secção **Armazenamento na Nuvem**. Um tutorial completo sobre como ligar o seu Mac ou PC usando SMB está disponível [aqui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Ligar a um NAS Usando WebDAV

Todos os passos são os mesmos que para SMB, exceto para o campo URL. O URL deve estar no formato `http://nome-servidor` ou `https://nome-servidor` se o servidor suportar SSL. O WebDAV funciona com **Synology, QNAP, Nextcloud, ownCloud** e muitos outros servidores — em qualquer lugar onde um endpoint WebDAV esteja disponível.

Um tutorial completo sobre como ligar um NAS usando WebDAV está disponível [aqui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Ligar a um Computador ou NAS Usando DLNA

Também pode partilhar uma biblioteca de música localizada no seu PC Windows ou NAS pessoal usando o protocolo DLNA / UPnP e aceder a essa biblioteca na aplicação como descrito [aqui](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). O DLNA é um protocolo popular e amplamente suportado, mas só lhe permite reproduzir ou descarregar música — não pode enviar ficheiros ou criar novas pastas num servidor DLNA.

## Ligar a um NAS ou Servidor Usando FTP, FTPS ou SFTP

O Flacbox também suporta os protocolos clássicos de transferência de ficheiros. Para ligar um servidor via FTP ou FTPS, toque em **Ligar ao armazenamento na nuvem → FTP**, introduza o URL do host no formato `ftp://nome-servidor` (ou `ftps://nome-servidor` para uma ligação encriptada), forneça o seu login e palavra-passe, e depois toque em **Concluído**. Para **SFTP** (SSH File Transfer Protocol), escolha **SFTP** em vez disso e forneça uma palavra-passe ou par de chaves SSH. Ambos funcionam com dispositivos NAS, hosts Linux e qualquer servidor que tenha um daemon FTP / FTPS / SSH.

## Ligar a uma Partilha NFS

O Flacbox inclui suporte a **NFS** (Network File System) — útil para hosts Linux, servidores BSD e dispositivos NAS que preferem expor bibliotecas de música via NFS em vez de SMB. Selecione **NFS** no menu **Ligar ao armazenamento na nuvem**, introduza o endereço do servidor e o caminho exportado, e toque em **Concluído**.

## Ligar um Servidor Plex Media Server

O Flacbox pode ligar diretamente a um Plex Media Server e navegar pela sua biblioteca musical por Artistas, Álbuns, Géneros e Listas de reprodução. Toque em **Ligar ao armazenamento na nuvem → Plex**, inicie sessão com a sua conta Plex, escolha um servidor, e a biblioteca aparece ao lado dos seus serviços de nuvem. Servidores Plex na mesma rede local também são descobertos automaticamente na secção **Dispositivos disponíveis**.

## Ligar um Servidor Jellyfin ou Emby

Tanto o **Jellyfin** (open-source) como o **Emby** (comercial) funcionam nativamente no Flacbox. Toque em **Ligar ao armazenamento na nuvem → Jellyfin** ou **Emby**, introduza o URL do seu servidor (algo como `http://ip-servidor:8096`) e as credenciais, e a sua biblioteca musical está pronta para transmitir. Como com o Plex, as bibliotecas na rede local são listadas automaticamente nos **Dispositivos disponíveis**.

## Ligar um Servidor Subsonic ou Navidrome

O Flacbox suporta a API Subsonic, o que significa que funciona com o **Subsonic** em si, o **Navidrome** e todos os outros servidores compatíveis com Subsonic — incluindo Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Toque em **Ligar ao armazenamento na nuvem → Subsonic**, introduza o URL do servidor e as credenciais, e a biblioteca aparece no ecrã de Conexões. Esta é a forma mais fácil de dar ao Flacbox acesso a uma coleção musical auto-hospedada sem expor a partilha de ficheiros subjacente.

## Ligar ao Armazenamento de Objetos Compatível com S3

Para quem auto-hospeda e audiófilos que usam armazenamento de objetos na nuvem, o Flacbox inclui um conector compatível com S3. Toque em **Ligar ao armazenamento na nuvem → Armazenamento S3**, depois introduza o URL do endpoint, região, chave de acesso, chave secreta e nome do bucket. Funciona com AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualquer outro serviço que exponha um endpoint S3-API.

## Dispositivos Disponíveis

Esta secção apresenta todos os dispositivos na sua rede local aos quais se pode ligar a partir do Flacbox via descoberta Bonjour. Para estabelecer uma ligação, siga estes passos:

- Abra a aplicação e vá à secção **Dispositivos disponíveis** em Conexões.
- Toque no dispositivo ao qual se quer ligar.
- Se necessário, introduza os seus dados de login para completar a ligação.

Esta é a forma mais rápida de descobrir uma partilha SMB, WebDAV, DLNA na sua rede doméstica sem digitar endereços IP manualmente.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dispositivos Disponíveis na Rede Local" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

O Wi-Fi Drive é uma tecnologia conveniente que permite transferências sem fios de ficheiros do computador para o dispositivo iOS via qualquer browser de desktop. Para usar esta funcionalidade de forma eficaz, certifique-se de que o seu dispositivo e computador estão ligados à mesma rede Wi-Fi. Aqui está um guia passo a passo sobre como usar o Wi-Fi Drive.

### Ativar o Wi-Fi Drive

- Abra a aplicação e vá ao separador **Conexões**.
- Selecione **Ligar via Wi-Fi** para aceder ao ecrã principal do Wi-Fi Drive.
- (Opcional) Defina um nome de utilizador e palavra-passe para o servidor web incorporado para proteger o acesso.
- Toque em **Iniciar Wi-Fi Drive** para ativar o Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Aceder ao Wi-Fi Drive no Computador

- No seu computador (desktop ou laptop), abra um browser (como Chrome, Firefox ou Safari).
- Na barra de endereço do browser, introduza o URL fornecido pela aplicação.

### Transferir Ficheiros Sem Fios

Quando a página web correspondente ao seu dispositivo iOS abrir no browser, pode facilmente arrastar e largar ficheiros do seu computador para a página web. Os ficheiros que largar começarão a transferir para o seu dispositivo iOS e estarão acessíveis dentro do Flacbox.

Também pode montar o Wi-Fi Drive diretamente no Finder no macOS (Ir → Ligar ao Servidor…) ou no Explorador de Ficheiros no Windows (Mapear Unidade de Rede…) e tratar o seu iPhone ou iPad como uma unidade de rede normal.

Instruções detalhadas sobre como transferir ficheiros sem fios usando o Wi-Fi Drive estão disponíveis [aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Partilha de Ficheiros iTunes / Finder

A Partilha de Ficheiros iTunes (agora Partilha de Ficheiros Finder no macOS Catalina e posterior) é outra forma de transferir ficheiros de um computador para um dispositivo usando um cabo Lightning ou USB-C.

- Ligue o dispositivo ao computador usando um cabo e execute o **Finder** no Mac (ou **iTunes** no Windows).
- Abra **Localizações → O Seu Dispositivo Ligado → Ficheiros** e encontre a aplicação Flacbox.
- Toque no ícone da aplicação para ver todas as pastas partilhadas.
- Copie ficheiros do computador para a pasta partilhada no dispositivo usando arrastar e largar.

Instruções detalhadas sobre como usar a Partilha de Ficheiros Finder estão disponíveis [aqui](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Ligar uma Pen Drive USB

Se tiver um cartão SD ou pen drive USB, pode ligá-lo usando um leitor Lightning para USB / SD Card ou uma pen USB-C (em iPad e iPhone 15 / 16 / 17 / Pro). A aplicação suporta leitores de cartões certificados pela Apple e iXpand Flash Drives. Com uma iXpand Flash Drive, insira-a na porta Lightning e abra a aplicação — verá uma mensagem Dispositivo Externo Ligado e as informações do dispositivo. Toque no ícone da pen drive para aceder à pasta de música e toque em qualquer ficheiro de áudio para começar a reproduzir.

Temos instruções detalhadas sobre como ligar uma pen drive USB ao iPhone e ouvir música ou gerir ficheiros nela [aqui](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestor de Ficheiros

Depois de ligar um serviço de armazenamento na nuvem, toque no seu ícone para ver todos os ficheiros e pastas disponíveis. Pode usar o gestor de ficheiros integrado para trabalhar com estes ficheiros — descarregar, renomear, mover, enviar, eliminar e mais. Quando iniciar uma transferência, o ficheiro aparece na fila de transferências. Para abrir a fila de transferências, vá ao separador Ficheiros Locais e toque no ícone de setas giratórias no canto superior esquerdo. Todos os ficheiros e pastas descarregados estão disponíveis na secção Ficheiros Locais.

## Barra de Ferramentas Superior

A barra de ferramentas superior, convenientemente localizada abaixo da barra de navegação, oferece várias ações úteis para fácil acesso. Pode mostrá-la ou ocultá-la com um simples gesto de deslizar para baixo.

- **Pesquisar** — realize uma pesquisa rápida no diretório atual, tornando fácil localizar ficheiros ou pastas específicas.
- **Continuar Reprodução** — se ativado nas definições da aplicação, restaura a fila do leitor de áudio e a última posição de media para a pasta atual. Uma forma prática de retomar onde ficou.
- **Reproduzir Tudo** — analisa a pasta atual e as suas subpastas e depois adiciona todos os ficheiros de áudio encontrados a uma nova fila do leitor. Útil quando quer reproduzir cada faixa num diretório.
- **Misturar Tudo** — como Reproduzir Tudo, mas mistura os ficheiros antes de os adicionar à fila do leitor de áudio. Ótimo para redescobrir uma pasta antiga de música.

## Opções de Pasta

Quando abrir uma pasta, encontrará um conjunto prático de ações disponíveis tocando no botão **"..."** no canto superior direito.

- **Selecionar** — ative o modo de seleção de ficheiros. Isto permite-lhe escolher um ou mais ficheiros dentro da pasta e executar ações em toda a seleção.
- **Nova Pasta** — crie uma nova pasta na pasta atual. Ótimo para manter a sua biblioteca bem estruturada.
- **Ativar modo offline** — ative o modo offline para a pasta atual. O modo offline vai além de um simples descarregamento: monitoriza ativamente a pasta para detetar alterações. Se adicionar novos ficheiros online, eles aparecerão automaticamente no seu dispositivo.
- **Enviar Ficheiros** — envie ficheiros do seu dispositivo para a pasta online. Isto torna-os acessíveis de qualquer lugar via o mesmo serviço de nuvem.
- **Pesquisar** — pesquise ficheiros específicos na pasta atual.
- **Ordenar** — ordene ficheiros por nome, tamanho, data de modificação ou por metadados. O modo de ordenação predefinido espelha a ordem de ordenação no servidor, mas pode alterá-lo de acordo com as suas preferências.
- **Vista em Grelha / Lista** — alterne entre vista de tabela e vista em miniatura. A vista de tabela mostra uma lista compacta; a vista em miniatura mostra grandes pré-visualizações de arte para identificação visual rápida.

## Editar Ficheiros Online

Quando precisar de gerir vários ficheiros no seu armazenamento na nuvem, use o **Modo de Seleção** para simplificar as suas ações:

- **Ativar Modo de Seleção** — toque no botão **"..."** no canto superior direito e escolha **Selecionar**.
- **Escolher Ficheiros** — aparecem caixas de verificação junto a cada ficheiro e pasta. Toque para selecionar um ou vários itens.
- **Executar Ações** — depois de ter selecionado os ficheiros ou pastas, terá acesso a Reproduzir Seguinte, Reproduzir Mais Tarde, Adicionar à Biblioteca Musical, Adicionar a uma Lista de Reprodução, Copiar, Enviar, Mover, Renomear e Eliminar.

Se preferir tratar o armazenamento na nuvem ligado como apenas de leitura (para evitar eliminações acidentais), ative Configurações → Gestor de Ficheiros → Editar Ficheiros Online → Desligado para ocultar todas as operações destrutivas da interface.

## Ações de Ficheiro

Toque no ícone **"..."** perto do título de um ficheiro para revelar o seu menu de ações:

- **Reproduzir Seguinte** — insira o ficheiro no topo da fila do leitor, para que reproduza logo após a faixa atual.
- **Reproduzir Mais Tarde** — acrescente o ficheiro ao fundo da fila do leitor.
- **Adicionar à Biblioteca Musical** — incorpore o ficheiro na sua biblioteca musical, organizada por artista, álbum, género ou compositor.
- **Adicionar a uma Lista de Reprodução** — adicione o ficheiro a uma lista de reprodução existente ou crie uma nova.
- **Editar tags de áudio** — abra o editor de tags integrado para modificar metadados. Para ficheiros online, a faixa é temporariamente descarregada, editada e depois reenviada após confirmação.
- **Adicionar aos Favoritos** — adicione o ficheiro à sua lista de favoritos para acesso rápido.
- **Baixar** — descarregue o ficheiro ou pasta para o seu dispositivo para uso offline.
- **Renomear** — renomeie o ficheiro diretamente no armazenamento remoto.
- **Mover** — mova o ficheiro para uma pasta diferente no seu armazenamento na nuvem.
- **Abrir Em** — exporte o ficheiro para outra aplicação compatível. O ficheiro é descarregado para o seu dispositivo, depois aparece a folha de partilha do sistema.
- **Excluir** — remova permanentemente o ficheiro do seu armazenamento na nuvem. **Esta ação não pode ser desfeita.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Mais Ações para um Ficheiro no Armazenamento na Nuvem Ligado" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Se a lista de ações exceder o espaço disponível no ecrã, basta deslocar para baixo no menu de ações para aceder a opções adicionais.

## Ações de Pasta

Para cada pasta no seu armazenamento na nuvem, tem uma grande variedade de ações disponíveis tocando no ícone **"..."** junto ao título da pasta. Se não ver todas as ações, deslize para baixo para revelar mais.

- **Reproduzir Tudo** — substitua a fila atual do leitor por cada item na pasta selecionada.
- **Reproduzir Seguinte** — adicione toda a pasta ao topo da fila do leitor.
- **Reproduzir Mais Tarde** — acrescente o conteúdo da pasta ao fundo da fila do leitor.
- **Adicionar à Biblioteca Musical** — incorpore o conteúdo da pasta na sua biblioteca musical.
- **Adicionar a Lista de Reprodução** — adicione toda a pasta a uma lista de reprodução. Também tem a opção de criar uma nova; o nome é preenchido automaticamente com o nome da pasta.
- **Adicionar aos Favoritos** — adicione a pasta aos seus favoritos para acesso rápido.
- **Ativar modo offline** — além de um simples descarregamento, esta opção monitoriza continuamente a pasta para novos ficheiros e descarrega-os automaticamente conforme aparecem online.
- **Baixar** — descarregue todo o conteúdo da pasta para o seu dispositivo para acesso offline.
- **Renomear** — renomeie a pasta diretamente no armazenamento remoto.
- **Mover** — mova a pasta para uma localização diferente no seu armazenamento na nuvem.
- **Arquivo (ZIP)** — agrupe o conteúdo da pasta num único ficheiro ZIP (funcionalidade Premium).
- **Excluir** — remova permanentemente a pasta e o seu conteúdo do seu armazenamento na nuvem. **Esta ação não pode ser desfeita.**

## Acesso Rápido

A secção de Acesso Rápido está localizada no topo do ecrã. Dá-lhe acesso rápido aos seus ficheiros favoritos e recentemente abertos dos serviços de nuvem ligados. Sempre que abrir um ficheiro ou pasta da nuvem, é adicionado à lista de Recentemente Abertos. Para limpar esta lista, abra Recentes, toque no botão Mais Ações e escolha Eliminar Lista. Também pode marcar pastas profundamente aninhadas como Favoritos para as aceder rapidamente sem ter de percorrer a estrutura de diretórios.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Links Online e Acesso Rápido" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Outros Serviços

Esta secção apresenta funcionalidades extra que melhoram a sua experiência. Atualmente, a aplicação suporta scrobbling **Last.fm** — quando ligado, as suas estatísticas de reprodução são automaticamente enviadas para a sua conta Last.fm. Pode depois visitar o seu perfil Last.fm para ver análises de escuta e obter recomendações musicais personalizadas. Instruções de configuração detalhadas estão disponíveis [aqui](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ligar Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
