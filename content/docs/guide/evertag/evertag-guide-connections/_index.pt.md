---
title: "Conexões"
date: 2020-02-01
description: "Aprenda a ligar armazenamento na nuvem, NAS e o seu computador ao Evertag. Aceda e edite ficheiros de áudio diretamente a partir do armazenamento na nuvem, NAS pessoal ou Mac/PC."
keywords: [
  "configuração cloud Evertag", "ligar iCloud ao Evertag", "acesso a ficheiros SMB iOS",
  "editor de tags áudio WebDAV", "edição de metadados NAS", "Wi-Fi Drive Evertag",
  "transferir ficheiros de áudio para iPhone", "Evertag iTunes File Sharing", "editar tags FLAC da nuvem"
]
tags: ["guia", "evertag", "conexões"]
readingTime: 11
---


Neste ecrã, pode ligar várias fontes que contêm os seus ficheiros de áudio. Pode integrar serviços de cloud populares como Google Drive, Dropbox, OneDrive, iCloud e outros, bem como ligar o seu Mac ou PC. Adicionalmente, tem a opção de editar ficheiros de áudio localizados no Apple Time Capsule, WD Cloud Home ou em qualquer NAS que utilize SMB ou WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Acesso rápido

No topo do ecrã de Conexões encontrará uma lista de **Acesso rápido**. Qualquer pasta na nuvem que adicione aos favoritos — mesmo que esteja vários níveis abaixo — aparece aqui para poder aceder sem navegar pelas pastas superiores todas as vezes.

## Ligar ao armazenamento na nuvem

- Abra o separador 'Conexões'  
- Selecione 'Ligar ao armazenamento na nuvem' no menu  
- Escolha um serviço de armazenamento na nuvem da lista  
- Introduza as suas credenciais e toque em 'Concluído.'

Se encontrar algum problema, verifique a sua ligação à internet e o login/palavra-passe.  
Na versão Premium da aplicação, pode adicionar um número ilimitado de serviços.

## Serviços de armazenamento na nuvem suportados

Atualmente, a aplicação suporta os serviços de armazenamento na nuvem mais populares: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), bem como qualquer servidor SMB ou WebDAV.

## Segurança e privacidade

Utilizamos apenas SDKs oficiais e ligações seguras para interagir com os serviços de cloud ligados. O seu login e palavra-passe não são acessíveis à aplicação. Todos os pedidos da aplicação ao serviço de cloud são encriptados.

Quando introduz o seu login e palavra-passe, a aplicação mostra-lhe a página de autorização oficial fornecida pelo fornecedor do serviço de cloud, e todo o processo de autorização ocorre fora da aplicação. O fornecedor do serviço de cloud envia um token de autenticação para a aplicação após a autorização bem-sucedida, e esse token é utilizado para fazer chamadas à API.

Um token de autenticação é uma chave digital que permite a aplicações de terceiros interagir com o armazenamento na nuvem. O token de autenticação é armazenado no seu dispositivo num armazenamento de sistema seguro chamado Keychain. Pode transferir os seus ficheiros do serviço de cloud ligado para o dispositivo, e esses ficheiros serão colocados no diretório 'Documentos' da aplicação. Pode remover esses ficheiros a qualquer momento usando o gestor de ficheiros integrado.

A aplicação não partilha qualquer informação da conta de cloud ligada. Pode revogar o acesso à sua conta de cloud a qualquer momento abrindo a página de definições da conta no seu navegador web.

## Revogar token de autenticação

Inicie sessão na sua conta num navegador web e navegue até à página de definições. Aí pode encontrar todas as aplicações de terceiros ligadas à sua conta de cloud e remover qualquer uma delas se já não quiser utilizar essa aplicação. Instruções detalhadas estão disponíveis [aqui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Pode também desligar as contas de cloud ligadas na aplicação, e o token de autenticação também será removido do seu dispositivo. Se remover a aplicação do seu dispositivo, todos os dados transferidos e tokens de acesso também serão removidos.

## Desligar um armazenamento na nuvem ou alterar configuração

- Aceder às Opções de Armazenamento na Nuvem: primeiro, localize o armazenamento na nuvem que deseja gerir na interface da aplicação.  
- Toque no Botão '...': junto ao título do serviço, verá um botão '...'. Toque nele para aceder a opções adicionais.  
  - **Renomear**: se quiser alterar o nome do serviço de cloud como aparece na sua lista, selecione 'Renomear.'  
  - **Configurações**: para modificar a configuração ou dados de autenticação do serviço de cloud, escolha 'Configurações.' Por vezes, pode ser necessário reautorizar o serviço de cloud ligado se o token de autorização tiver expirado.  
  - **Desconectar**: se deseja cortar completamente a ligação entre a aplicação e o serviço de cloud, selecione 'Desconectar.' Tenha em atenção que esta opção removerá todas as músicas associadas a este serviço de cloud da biblioteca musical da aplicação, mas permanecerão no servidor.

## Ligar ao Computador ou NAS

Pode também ligar o seu computador, NAS pessoal ou outros dispositivos de rede usando o protocolo SMB, DLNA ou WebDAV.

## Ligar ao computador usando SMB

- Toque em "Ligar ao armazenamento na nuvem" → SMB.  
- Introduza o endereço IP do computador e o nome da pasta partilhada no campo URL usando o formato smb://endereço-ip-computador/nome-pasta-partilhada  
- Escolha a versão do protocolo: Auto, SMB1, SMB2  
- Introduza login e palavra-passe (se necessário)  
- Toque em "Concluído."

Se a sua ligação for bem-sucedida, verá o armazenamento ligado na secção "Armazenamento na nuvem."  
Um tutorial completo sobre como ligar o seu Mac ou PC usando SMB está disponível [aqui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Ligar ao NAS usando WebDAV

Todos os passos são os mesmos, exceto o campo URL.  
O URL deve estar no formato http://nome-servidor, ou https://nome-servidor se o servidor suportar SSL.  
Um tutorial completo sobre como ligar NAS usando o protocolo WebDAV está disponível [aqui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dispositivos disponíveis

Esta secção apresenta todos os dispositivos na sua rede local aos quais se pode ligar através da aplicação.  
Para estabelecer uma ligação com um dispositivo, siga estes passos:

- Abra a aplicação e vá para a secção "Dispositivos disponíveis."  
- Toque no dispositivo ao qual se quer ligar a partir da lista.  
- Se necessário, introduza os seus dados de login para concluir a ligação.

## Wi-Fi Drive

Wi-Fi Drive é uma tecnologia conveniente que permite transferências de ficheiros sem fios do seu computador para o seu dispositivo iOS através de um navegador de ambiente de trabalho.  
Para utilizar esta funcionalidade eficazmente, certifique-se de que o seu dispositivo e computador estão ligados à mesma rede Wi-Fi.  
Aqui está um guia passo a passo sobre como usar o Wi-Fi Drive.

## Ativar Wi-Fi Drive

- Abra a aplicação e vá para o separador "Conexões."  
- Selecione "Ligar via Wi-Fi" para aceder ao ecrã principal do Wi-Fi Drive.  
- Toque em "Iniciar Wi-Fi Drive" para ativar o Wi-Fi Drive.

## Aceder ao Wi-Fi Drive no Computador

- No seu computador (de secretária ou portátil), abra um navegador web (como Chrome, Firefox ou Safari).  
- Na barra de endereços do navegador, introduza o URL fornecido pela aplicação.

## Transferir Ficheiros Sem Fios

Assim que a página web correspondente ao seu dispositivo iOS abrir no navegador, pode facilmente arrastar e largar ficheiros do seu computador para a página web.  
Os ficheiros que arrastar e largar começarão a ser transferidos para o seu dispositivo iOS e estarão acessíveis dentro da aplicação.

Instruções detalhadas sobre como transferir ficheiros sem fios usando Wi-Fi Drive estão disponíveis [aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing é outra tecnologia que lhe permite transferir ficheiros de um computador para um dispositivo usando a aplicação Finder no seu Mac e um cabo Lightning.  
- Basta ligar o dispositivo ao computador usando um cabo e executar a aplicação Finder no seu Mac.  
- Abra "Localizações" → "O Seu Dispositivo Ligado" → "Ficheiros" → e encontre a aplicação atual.  
- Toque no ícone da aplicação para ver todas as pastas partilhadas.  
- Copie ficheiros do computador para a pasta partilhada no dispositivo usando arrastar e largar.

Instruções detalhadas sobre como usar iTunes File Sharing estão disponíveis [aqui](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Ligar uma memória USB

Se tiver um cartão SD ou pen USB, pode ligá-la usando um leitor de cartões Lightning ou USB-C no iPhone/iPad, ou ligá-la diretamente a um Mac. A aplicação suporta atualmente leitores de cartões certificados pela Apple. Temos instruções detalhadas sobre como ligar uma memória USB ao seu iPhone ou iPad e gerir os ficheiros nela localizados, disponíveis [aqui](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). As unidades ligadas aparecem na secção **Acessórios conectados** do ecrã de Conexões.

## Gestor de Ficheiros

Depois de ligar um serviço de armazenamento na nuvem, toque no seu ícone para ver todos os ficheiros e pastas disponíveis. Pode usar o gestor de ficheiros integrado para trabalhar com estes ficheiros — transferir, renomear, mover e muito mais. Quando iniciar uma transferência, o ficheiro aparecerá na fila de transferências. Para ver a fila de transferências, vá ao separador "Ficheiros locais" e toque nas setas giratórias no canto superior esquerdo. Todos os ficheiros e pastas transferidos estão disponíveis na secção "Ficheiros locais."

## Barra de Ferramentas Superior

A barra de ferramentas superior, convenientemente localizada abaixo da barra de navegação, oferece várias ações úteis de fácil acesso. Pode mostrar ou ocultar esta barra usando um simples gesto de deslizar para baixo. Aqui estão as ações disponíveis:

- **Pesquisar**: esta opção permite-lhe realizar uma pesquisa rápida no diretório atual, facilitando a localização de ficheiros ou pastas específicos.  

## Opções de Pasta

Quando abre uma pasta dentro da aplicação, encontrará um conjunto de ações disponíveis tocando no botão "..." no canto superior direito do ecrã.  
Aqui está um resumo dessas ações:

- **Selecionar**: ative o modo de seleção de ficheiros. Este modo permite-lhe escolher um ou mais ficheiros dentro da pasta, facilitando a realização de ações nos itens selecionados.  
- **Nova Pasta**: crie uma nova pasta dentro da pasta atual. Esta funcionalidade permite-lhe organizar os seus ficheiros e manter a sua biblioteca bem estruturada.   
- **Carregar Ficheiros**: carregue ficheiros do seu dispositivo para a pasta online. Esta ação permite-lhe transferir ficheiros para a nuvem ou servidor, tornando-os acessíveis de qualquer lugar.  
- **Pesquisar**: pesquise ficheiros específicos dentro da pasta atual. Isto é especialmente útil para localizar rapidamente itens específicos numa grande coleção.  
- **Ordenar**: ordene ficheiros dentro da pasta por critérios como nome, tamanho ou data de edição. O modo de ordenação predefinido normalmente espelha a ordem de ordenação no servidor, mas pode alterá-la de acordo com as suas preferências.  
- **Vista em Grelha/Lista**: alterne entre dois modos de visualização: vista em tabela e vista em miniaturas. A vista em tabela apresenta ficheiros numa lista, enquanto a vista em miniaturas exibe representações visuais dos ficheiros, facilitando a identificação do conteúdo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Editar Ficheiros Online

Quando precisa de gerir vários ficheiros no armazenamento na nuvem nesta aplicação, pode usar o modo de seleção para simplificar as suas ações. Siga estes passos para uma gestão eficaz de ficheiros:

- **Ativar Modo de Seleção**: abra a aplicação no seu dispositivo e navegue para a secção que contém o armazenamento na nuvem. Procure o canto superior direito onde encontrará o botão "..." (reticências). Toque nele e escolha o item de menu "Selecionar" para ativar o modo de seleção.  
- **Escolher Ficheiros**: notará caixas de verificação a aparecer junto a cada ficheiro ou pasta listado. Escolha um ou múltiplos ficheiros ou pastas tocando simplesmente nas caixas de verificação ao lado deles.  
- **Realizar Várias Ações**: depois de selecionar os ficheiros ou pastas que deseja gerir, terá acesso a várias ações adaptadas às suas necessidades:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Ações de ficheiro

Junto ao título do ficheiro, notará um símbolo de reticências "..." (três pontos) — este serve como menu de ações.  
Toque nele para revelar uma lista de ações disponíveis:

- **Editar tags de áudio**: ao selecionar esta opção, pode aceder ao editor de tags integrado, permitindo-lhe modificar tags de áudio do ficheiro escolhido. O ficheiro será temporariamente transferido para um diretório temporário e depois carregado para o armazenamento depois de confirmar as alterações.  
- **Adicionar aos Favoritos**: esta ação adiciona o ficheiro à sua lista de ficheiros favoritos para acesso rápido e conveniente.  
- **Baixar**: escolha esta ação para transferir o ficheiro ou pasta para o seu dispositivo, tornando-o acessível para uso offline.  
- **Renomear**: esta opção permite-lhe renomear o ficheiro diretamente no armazenamento remoto, permitindo uma nomenclatura personalizada.  
- **Mover**: opte por esta ação para mover o ficheiro para uma pasta diferente dentro do armazenamento na nuvem, ajudando a manter uma estrutura de ficheiros organizada.  
- **Abrir Em**: use esta ação para exportar o ficheiro para outra aplicação compatível. O ficheiro será transferido para o seu dispositivo e depois aparecerá a caixa de diálogo Partilhar.  
- **Excluir**: tenha cuidado com esta ação, pois remove permanentemente o ficheiro do armazenamento na nuvem. **Esta eliminação não pode ser desfeita**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Se a lista de ações exceder o espaço disponível no ecrã, basta deslizar para baixo dentro do menu de ações para aceder a opções adicionais.

## Ações de pasta

Para cada pasta no armazenamento na nuvem, tem várias ações disponíveis. Para aceder a estas opções, toque simplesmente no ícone de reticências "..." localizado junto ao título da pasta. Se não vir todas as ações, deslize para baixo para revelar mais opções. Aqui estão as ações disponíveis:

- **Adicionar aos Favoritos**: use esta ação para adicionar a pasta à sua lista de ficheiros favoritos para acesso rápido e conveniente.  
- **Baixar**: transfira todo o conteúdo da pasta para o seu dispositivo para acesso offline.  
- **Renomear**: renomeie a pasta diretamente no armazenamento remoto.  
- **Mover**: mova a pasta para uma localização diferente dentro do armazenamento na nuvem.  
- **Excluir**: tenha cuidado com esta ação, pois remove permanentemente a pasta e o seu conteúdo do armazenamento na nuvem. **Esta ação não pode ser desfeita**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
