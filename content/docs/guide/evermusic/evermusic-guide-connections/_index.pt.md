---
title: "Conexões"
date: 2020-01-01
description: "Aprenda a ligar serviços na nuvem, computadores, dispositivos NAS e a gerir os seus ficheiros de música com o Evermusic. Guia passo a passo para Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing e muito mais."
keywords: [
  "Evermusic", "leitor de música na nuvem", "streaming NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "ligar armazenamento na nuvem", "transferência de música iPhone", "gestor de ficheiros iOS"
]
tags: ["evermusic", "guia", "conexões"]
readingTime: 11
---


No ecrã de Conexões pode ligar todas as fontes que guardam a sua música — serviços populares na nuvem, servidores de media auto-hospedados, o seu Mac ou PC, um NAS pessoal, Apple Time Capsule, WD My Cloud Home, até uma pen USB — e utilizá-las todas a partir de uma interface unificada. As Conexões são também onde configura o Acesso Rápido a pastas profundamente aninhadas na nuvem e onde autentica o Last.fm para scrobbling.

O ecrã está dividido em secções claramente identificadas para que possa escalar de uma única conta iCloud Drive a uma biblioteca distribuída por múltiplas nuvens e dispositivos NAS: Acesso Rápido no topo (as suas pastas favoritas na nuvem), Armazenamento na nuvem (as contas que adicionou), Rede local (dispositivos descobertos via Bonjour), Computador (Wi-Fi Drive, iTunes File Sharing, SMB), Acessórios externos (pens USB ligadas) e Outros serviços (Last.fm e similares).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecrã de Conexões do Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Ligar ao armazenamento na nuvem

- Abra o separador Conexões.
- Selecione Ligar ao armazenamento na nuvem no menu.
- Escolha um serviço de armazenamento na nuvem da lista.
- Inicie sessão na página de autorização oficial do fornecedor (o Evermusic nunca vê a sua palavra-passe).
- Toque em Concluído.

{{< cards cols="1">}}
  {{< card title="" subtitle="Seletor de fornecedor de armazenamento na nuvem" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Se encontrar problemas, verifique novamente a sua ligação à internet e as credenciais de início de sessão, e certifique-se de que a autenticação de dois fatores está corretamente configurada para esse serviço.  
Na versão Premium da aplicação pode adicionar um número ilimitado de serviços. Os utilizadores gratuitos podem ligar uma única conta na nuvem de cada vez.

## Serviços de armazenamento na nuvem suportados

O Evermusic suporta toda a gama de serviços populares na nuvem e auto-hospedados. Os utilizadores gratuitos têm o mesmo catálogo de fornecedores, mas com o limite de uma conta; o Premium desbloqueia contas ilimitadas e remove a maioria dos outros limites.

- **Contas pessoais na nuvem:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidores auto-hospedados e bibliotecas de media:** Plex · Jellyfin · Emby · Subsonic (e todos os servidores compatíveis com Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (e Owncloud, via API partilhada) · Synology Drive · QNAP.
- **Protocolos NAS e partilha de ficheiros:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (autenticação por palavra-passe ou chave pública), NFS e DLNA (só leitura — reprodução e transferência).
- **Armazenamento de objetos compatível com S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage ou qualquer endpoint S3-API.
- **Descoberta na rede local:** a secção Dispositivos disponíveis lista automaticamente todos os dispositivos na sua rede Wi-Fi que se anunciam via Bonjour / mDNS — servidores Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, routers AirPort com unidades ligadas, e assim por diante.

## Segurança e privacidade

Utilizamos apenas SDK oficial e ligações seguras para interagir com os serviços na nuvem ligados. O seu login e palavra-passe não estão disponíveis para a aplicação. Todos os pedidos da aplicação ao serviço na nuvem são encriptados.

Quando introduz o seu login e palavra-passe, a aplicação mostra-lhe a página de autorização oficial fornecida pelo fornecedor do serviço na nuvem e todo o processo de autorização é feito fora da aplicação. O fornecedor do serviço na nuvem envia um token de autenticação para a aplicação após autorização bem-sucedida e esse token é usado para fazer chamadas API.

O token de autenticação é uma chave digital que permite a aplicações de terceiros interagir com o armazenamento na nuvem. O token de autenticação é armazenado no seu dispositivo num armazenamento de sistema seguro chamado Keychain. Pode transferir os seus ficheiros do serviço na nuvem ligado para o dispositivo e esses ficheiros serão colocados no diretório "Documentos" da aplicação. Pode remover esses ficheiros a qualquer momento usando o gestor de ficheiros integrado.

A aplicação não partilha nenhuma informação da conta na nuvem ligada. Pode revogar o acesso à sua conta na nuvem a qualquer momento abrindo a página de definições da conta no seu navegador web.

## Rejeitar o token de autenticação

Inicie sessão na sua conta no navegador web e navegue para a página de definições. Aí pode encontrar todas as aplicações de terceiros ligadas à sua conta na nuvem e remover qualquer uma delas se não quiser usar essa aplicação. Instruções detalhadas disponíveis [aqui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Também pode desligar as contas na nuvem ligadas na aplicação e o token de autenticação será igualmente removido do seu dispositivo. Se remover a aplicação do seu dispositivo, todos os dados transferidos e tokens de acesso serão também removidos.

## Desligar um armazenamento na nuvem ou alterar a configuração

- Aceda às Opções de Armazenamento na Nuvem: primeiro, localize o armazenamento na nuvem que pretende gerir na interface da aplicação.
- Toque no Botão '...': junto ao título do serviço, verá um botão '...'. Toque nele para aceder a opções adicionais.
  - **Renomear**: se quiser alterar o nome do serviço na nuvem como aparece na sua lista, selecione 'Renomear'.
  - **Configurações**: para modificar a configuração ou os dados de autenticação do serviço na nuvem, escolha 'Configurações'. Por vezes, pode ser necessário reautorizar o serviço na nuvem ligado se o token de autorização tiver expirado.
  - **Desconectar**: se quiser cortar completamente a ligação entre a aplicação e o serviço na nuvem, selecione 'Desconectar'. Tenha em atenção que escolher esta opção irá remover todas as músicas associadas a este serviço na nuvem da biblioteca de música da sua aplicação, mas permanecerão no servidor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu de Mais Ações para armazenamento na nuvem ligado" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Ligar a um Computador ou NAS

Também pode ligar o seu computador, NAS pessoal ou outros dispositivos de rede usando protocolo SMB, DLNA ou WebDAV.

## Ligar ao computador usando SMB

- Toque em "Ligar ao armazenamento na nuvem" → SMB.
- Introduza o endereço IP do computador e o nome da pasta partilhada no campo URL usando o formato smb://endereço-ip-computador/nome-pasta-partilhada
- Escolha a versão do protocolo: Auto, SMB1, SMB2
- Introduza o login e a palavra-passe (se necessário)
- Toque em "Concluído".

Se a sua ligação for bem-sucedida, verá o armazenamento ligado na secção "Armazenamento na nuvem".  
Um tutorial completo sobre como ligar o seu Mac ou PC usando SMB está disponível [aqui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Definições de Ligação SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Ligar ao NAS usando WebDAV

Todos os passos são os mesmos, exceto o campo URL.  
O URL deve estar no formato http://nome-servidor, ou https://nome-servidor se o servidor suportar SSL.
Um tutorial completo sobre como ligar armazenamento NAS usando protocolo WebDAV está disponível [aqui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Definições de Ligação WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Ligar ao Computador ou NAS usando DLNA

Também pode partilhar uma biblioteca de música localizada no seu PC Windows ou NAS pessoal usando o protocolo DLNA e aceder a essa biblioteca na aplicação conforme descrito [aqui](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). O DLNA é um protocolo popular e amplamente utilizado, mas apenas permite reproduzir ou transferir música. Não é possível enviar ficheiros nem criar novas pastas no servidor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Definições de Ligação DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dispositivos disponíveis

Esta secção apresenta todos os dispositivos na sua rede local aos quais pode ligar através da aplicação.  
Para estabelecer uma ligação com um dispositivo, siga estes passos:

- Abra a aplicação e vá para a secção "Dispositivos Disponíveis".
- Toque no dispositivo ao qual quer ligar a partir da lista.
- Se necessário, introduza os seus dados de início de sessão para concluir a ligação.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispositivos Disponíveis na Rede Local" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

O Wi-Fi Drive é uma tecnologia conveniente que permite transferências de ficheiros sem fios do seu computador para o seu dispositivo iOS através de um navegador de computador.  
Para utilizar esta funcionalidade de forma eficaz, certifique-se de que o seu dispositivo e computador estão ligados à mesma rede Wi-Fi.  
Aqui está um guia passo a passo sobre como utilizar o Wi-Fi Drive.

## Ativar o Wi-Fi Drive

- Abra a aplicação e vá para o separador "Conexões".
- Selecione "Ligar via Wi-Fi" para aceder ao ecrã principal do Wi-Fi Drive.
- Toque em "Iniciar Wi-Fi Drive" para ativar o Wi-Fi Drive.

## Aceder ao Wi-Fi Drive no seu Computador

- No seu computador (de secretária ou portátil), abra um navegador web (como Chrome, Firefox ou Safari).
- Na barra de endereço do navegador, introduza o URL fornecido pela aplicação.

## Transferir Ficheiros Sem Fios

Quando a página web correspondente ao seu dispositivo iOS abrir no navegador, pode facilmente arrastar e largar ficheiros do seu computador para a página web.  
Os ficheiros que arrastar e largar começarão a ser transferidos para o seu dispositivo iOS e ficarão acessíveis dentro da aplicação.

{{< cards cols="1">}}
  {{< card title="" subtitle="Definições do Servidor Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Instruções detalhadas sobre como transferir ficheiros sem fios usando WiFi-Drive estão disponíveis [aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

O iTunes File Sharing é outra tecnologia que permite transferir ficheiros do computador para o dispositivo usando a aplicação Finder no Mac e o cabo Lightning.  
- Basta ligar um dispositivo ao computador usando um cabo e executar a aplicação Finder no Mac.
- Abra "Localizações" → "O Seu Dispositivo Ligado" → "Ficheiros" → e encontre a aplicação Evermusic.
- Toque no ícone da aplicação para ver todas as pastas partilhadas.
- Copie ficheiros do computador para a pasta partilhada no dispositivo usando arrastar e largar.

Instruções detalhadas sobre como usar o iTunes File Sharing estão disponíveis [aqui](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing no Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Ligar uma pen USB

Se tiver um cartão SD, pode ligá-lo usando um leitor de cartões lightning. A aplicação suporta atualmente leitores de cartões certificados pela Apple e iXpand Flash Drives. Se tiver um iXpand Flash Drive — insira-o na porta lightning e abra a aplicação. Verá uma mensagem 'Dispositivo externo ligado' e informações sobre o dispositivo. Basta tocar no ícone da pen para aceder à pasta de música e tocar em qualquer ficheiro de áudio para começar a reproduzir. Temos instruções detalhadas sobre como ligar uma pen USB ao iPhone e ouvir música ou gerir ficheiros nela, disponíveis [aqui](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestor de Ficheiros

Quando tiver ligado um serviço de armazenamento na nuvem, toque no seu ícone para ver todos os ficheiros e pastas disponíveis. Pode usar o gestor de ficheiros integrado para trabalhar com estes ficheiros — transferir, renomear, mover e muito mais. Quando iniciar uma transferência, o ficheiro aparecerá na fila de transferência. Para ver a fila de transferência, vá para o separador "Ficheiros Locais" e toque nas setas giratórias no canto superior esquerdo. Todos os ficheiros e pastas transferidos estão disponíveis na secção "Ficheiros Locais".

## Barra de Ferramentas Superior

A barra de ferramentas superior, convenientemente localizada sob a barra de navegação, oferece várias ações úteis de fácil acesso. Pode mostrar ou ocultar esta barra de ferramentas usando um simples gesto de deslizar para baixo. Aqui estão as ações disponíveis:

- **Pesquisar**: esta opção permite-lhe realizar uma pesquisa rápida no diretório atual, tornando fácil localizar ficheiros ou pastas específicos.
- **Continuar Reprodução**: se estiver ativado nas definições da aplicação, esta funcionalidade restaura a fila do leitor de áudio e a última posição de media para a pasta atual. É uma forma conveniente de retomar onde parou na sua biblioteca de música.
- **Reproduzir Tudo**: ao selecionar esta ação, a aplicação irá procurar na pasta atual e nas suas subpastas, adicionando todos os ficheiros de áudio encontrados a uma nova fila do leitor. Isto é útil quando quer reproduzir toda a música num determinado diretório.
- **Reproduzir Aleatoriamente**: semelhante a "Reproduzir Tudo", esta ação procura na pasta atual e nas suas subpastas, mas mistura os ficheiros antes de os adicionar à fila do leitor de áudio. É uma ótima forma de desfrutar da sua música em ordem aleatória.

{{< cards cols="1">}}
  {{< card title="" subtitle="Barra de Ferramentas Superior Dentro de uma Pasta na Nuvem" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opções de Pasta

Quando abre uma pasta dentro da aplicação, encontrará um conjunto prático de ações disponíveis tocando no botão "..." no canto superior direito do ecrã.  
Aqui está uma descrição destas ações:

- **Selecionar**: ative o modo de seleção de ficheiros. Este modo permite-lhe escolher um ou mais ficheiros dentro da pasta, facilitando a execução de ações nos itens selecionados.
- **Nova Pasta**: crie uma nova pasta dentro da pasta atual. Esta funcionalidade permite-lhe organizar os seus ficheiros e manter a sua biblioteca bem estruturada.
- **Ativar modo offline**: ative o modo offline para a pasta atual. O modo offline vai além da simples transferência; monitoriza ativamente a pasta para detetar alterações. Se adicionar novos ficheiros à pasta online, a aplicação irá transferi-los automaticamente para o seu dispositivo. Isto garante que a sua biblioteca local fica atualizada com as alterações no servidor.
- **Enviar Ficheiros**: envie ficheiros do seu dispositivo para a pasta online. Esta ação permite-lhe transferir ficheiros para a nuvem ou servidor, tornando-os acessíveis de qualquer lugar.
- **Pesquisar**: pesquise ficheiros específicos dentro da pasta atual. Isto é especialmente útil para localizar rapidamente itens específicos numa coleção grande.
- **Ordenar**: ordene ficheiros dentro da pasta por critérios como nome, tamanho ou data de edição. O modo de ordenação predefinido normalmente espelha a ordem de classificação no servidor, mas pode alterá-lo de acordo com as suas preferências.
- **Vista Grelha/Lista**: alterne entre dois modos de visualização: vista de tabela e vista de miniaturas. A vista de tabela apresenta os ficheiros numa lista, enquanto a vista de miniaturas exibe representações visuais dos ficheiros, facilitando a identificação do conteúdo rapidamente.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu de Mais Ações da Pasta Atual" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Editar Ficheiros Online

Quando precisar de gerir múltiplos ficheiros no seu armazenamento na nuvem no Evermusic, pode usar o modo de seleção para simplificar as suas ações. Siga estes passos para uma gestão de ficheiros eficaz:

- **Ativar o Modo de Seleção**: abra a aplicação no seu dispositivo e navegue para a secção que contém o seu armazenamento na nuvem. Procure o botão "..." (reticências) no canto superior direito. Toque nele e escolha o item de menu "Selecionar" para ativar o modo de seleção.
- **Escolher Ficheiros**: notará que aparecem caixas de verificação junto a cada ficheiro ou pasta listado. Escolha um ou vários ficheiros ou pastas tocando simplesmente nas caixas de verificação junto a eles.
- **Executar Várias Ações**: quando tiver selecionado os ficheiros ou pastas que quer gerir, terá acesso a várias ações adaptadas às suas necessidades.

{{< cards cols="1">}}
  {{< card title="" subtitle="Modo de Seleção para Ficheiros Online" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Ações de ficheiro

Junto ao título do ficheiro, notará um símbolo de reticências "..." (três pontos) — este é o menu de ações.  
Toque nele para revelar uma lista de ações disponíveis:

- **Reproduzir a Seguir**: opte por esta ação para inserir o ficheiro escolhido no topo da fila do leitor, garantindo que é reproduzido imediatamente após o item em reprodução.
- **Reproduzir Mais Tarde**: selecionar esta opção adiciona o ficheiro ao fundo da fila do leitor, garantindo que é reproduzido após a fila existente.
- **Adicionar à Biblioteca de Música**: esta ação permite-lhe incorporar o ficheiro na sua biblioteca de música, tornando-o facilmente acessível e organizado por artista, álbum, género ou compositor.
- **Adicionar a uma Lista de Reprodução**: use esta ação para adicionar o ficheiro a uma lista de reprodução existente ou criar uma nova.
- **Editar tags de áudio**: ao selecionar esta opção, pode aceder ao editor de tags integrado do Evermusic, permitindo-lhe modificar as tags de áudio do ficheiro escolhido. O ficheiro será temporariamente transferido para um diretório temporário e depois carregado para o armazenamento após confirmar as alterações.
- **Adicionar aos Favoritos**: esta ação adiciona o ficheiro à sua lista de ficheiros favoritos para acesso rápido e conveniente.
- **Baixar**: escolha esta ação para transferir o ficheiro ou pasta para o seu dispositivo, tornando-o acessível para uso offline.
- **Renomear**: esta opção permite-lhe renomear o ficheiro diretamente no armazenamento remoto, permitindo nomes de ficheiros personalizados.
- **Mover**: opte por esta ação para realocar o ficheiro para uma pasta diferente no seu armazenamento na nuvem, ajudando a manter uma estrutura de ficheiros organizada.
- **Abrir Em**: use esta ação para exportar o ficheiro para outra aplicação compatível. O ficheiro será transferido para o seu dispositivo e depois aparecerá o diálogo de Partilha.
- **Excluir**: tenha cuidado com esta ação, pois remove permanentemente o ficheiro do seu armazenamento na nuvem. Esta eliminação não pode ser anulada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu de Mais Ações para um Único Ficheiro" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Se a lista de ações exceder o espaço disponível no ecrã, basta deslizar para baixo dentro do menu de ações para aceder a opções adicionais.

## Ações de pasta

Para cada pasta no seu armazenamento na nuvem, tem várias ações disponíveis. Para aceder a estas opções, basta tocar no ícone de reticências "..." localizado junto ao título da pasta. Se não vir todas as ações, deslize para baixo para revelar mais opções. Aqui estão as ações disponíveis:

- **Reproduzir Tudo**: substitua a fila atual do leitor com todos os itens da pasta selecionada.
- **Reproduzir a Seguir**: adicione a pasta inteira ao topo da fila do leitor, logo após o item em reprodução.
- **Reproduzir Mais Tarde**: acrescente o conteúdo da pasta ao fundo da fila do leitor.
- **Adicionar à Biblioteca de Música**: esta ação integra perfeitamente o conteúdo da pasta na sua biblioteca de música, tornando-o facilmente acessível e organizado por artista, álbum, género ou compositor.
- **Adicionar à Lista de Reprodução**: pode incluir a pasta inteira numa lista de reprodução. Também tem a opção de criar uma nova lista de reprodução, e o nome da pasta será automaticamente atribuído.
- **Adicionar aos Favoritos**: use esta ação para adicionar a pasta à sua lista de ficheiros favoritos para acesso rápido e conveniente.
- **Ativar modo offline**: ao ativar o modo offline para uma pasta selecionada, a aplicação vai além da simples transferência. Verifica continuamente se há alterações e, se novos ficheiros forem adicionados à pasta online, serão transferidos automaticamente para a aplicação.
- **Baixar**: transfira todo o conteúdo da pasta para o seu dispositivo para acesso offline.
- **Renomear**: renomeie a pasta diretamente no armazenamento remoto.
- **Mover**: realoque a pasta para uma localização diferente no seu armazenamento na nuvem.
- **Excluir**: tenha cuidado com esta ação pois remove permanentemente a pasta e o seu conteúdo do seu armazenamento na nuvem. Esta ação não pode ser anulada.


## Acesso Rápido

A secção de Acesso Rápido está localizada no topo do ecrã. Dá-lhe acesso rápido aos seus ficheiros favoritos e recentemente abertos dos serviços na nuvem ligados.
Sempre que abre um ficheiro ou pasta da nuvem, é adicionado à lista "Abertos Recentemente". Para limpar esta lista, abra "Recentes", toque no botão "Mais Ações" e escolha "Eliminar Lista". Também pode marcar pastas profundamente aninhadas como Favoritos para aceder a elas rapidamente sem percorrer a estrutura de diretórios.

## Outros Serviços

Esta secção exibe funcionalidades extra que melhoram a sua experiência. Atualmente, a aplicação suporta scrobbling Last.fm. Quando ligado, as suas estatísticas de reprodução são enviadas automaticamente para a sua conta Last.fm. Pode visitar o seu perfil Last.fm mais tarde para ver análises de audição e obter recomendações de música personalizadas. Instruções detalhadas de configuração estão disponíveis [aqui](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
