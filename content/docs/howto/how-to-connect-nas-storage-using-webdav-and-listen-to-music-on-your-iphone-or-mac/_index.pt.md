---
title: "Como conectar o armazenamento NAS usando WebDAV e ouvir música no seu iPhone ou Mac"
date: 2024-07-28
description: "Aprenda a configurar o WebDAV no seu Synology NAS e transmitir música para o seu iPhone ou Mac usando Evermusic ou Flacbox. Siga nosso guia passo a passo."
keywords: ["conectar nas", "webdav synology", "transmitir música nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["música", "streaming", "armazenamento", "nas", "conectar", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Resumo:** Instale e ative o WebDAV no seu Synology NAS, configure as permissões da pasta compartilhada e conecte-se pelo Evermusic ou Flacbox usando o endereço IP do NAS e a porta WebDAV (padrão 5005/5006). Você pode transmitir e gerenciar toda a sua biblioteca musical sem copiar arquivos para o seu dispositivo.

Descubra como conectar seu armazenamento NAS usando WebDAV e transmitir facilmente sua biblioteca musical para o seu iPhone ou Mac. WebDAV (Web-based Distributed Authoring and Versioning) é um protocolo que permite gerenciar e compartilhar arquivos pela Internet. Ao configurar o WebDAV no seu NAS, você pode acessar e transmitir sua coleção musical, garantindo que suas músicas favoritas estejam sempre ao seu alcance.

Neste guia, mostraremos como configurar uma conexão WebDAV em um dos servidores NAS mais populares, o Synology NAS. Siga nossos passos simples para configurar o WebDAV no seu Synology NAS, e você poderá navegar, transmitir e gerenciar sua biblioteca musical diretamente do seu iPhone ou Mac.

## Passo 1: Instalar o WebDAV no Synology NAS

1. Faça login no seu Synology NAS e abra o **Centro de Pacotes**.
2. Pesquise "webdav" e instale o pacote WebDAV se ainda não estiver instalado. Abra o servidor WebDAV para configurá-lo.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instalar WebDAV no Synology" width="600" >}}

## Passo 2: Configurar o servidor WebDAV

1. Na página de configurações do WebDAV, marque as caixas para **Ativar HTTP**, **Ativar HTTPS**, **Ativar WebDAV anônimo** e **Ativar DavDepthInfinity**.
2. Clique em **Aplicar** para salvar as alterações. Anote os números das portas para conexões HTTP e HTTPS, que são 5005 e 5006 por padrão.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Configurar as definições do WebDAV" width="600" >}}

## Passo 3: Configurar permissões da pasta compartilhada

1. Abra o **Painel de Controle** e vá para a seção **Pasta Compartilhada**.
2. Selecione a pasta **Música** e clique em **Editar**.
3. Na aba **Permissões**, configure as permissões. Ative o acesso de convidado com Somente leitura se você só precisa ouvir música, ou Leitura/Escrita se precisa modificar arquivos. Salve as alterações.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Permissões da pasta compartilhada" width="600" >}}

## Passo 4: Encontrar o endereço IP do Synology NAS

1. Abra o **Painel de Controle** e vá para a aba **Interface de Rede**, ou use seu navegador para visitar [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Encontrar endereço IP do NAS" width="600" >}}

2. Anote o endereço IP do seu Synology NAS (ex.: 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Endereço IP do Synology NAS" width="600" >}}

## Passo 5: Conectar ao Synology NAS usando Evermusic/Flacbox

1. Abra o app Evermusic ou Flacbox e vá para a aba **Conexões**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Aba Conexões no Evermusic" width="600" >}}

2. Para conexão automática, encontre seu Synology NAS na seção **Dispositivos disponíveis** e toque para conectar.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Lista de dispositivos disponíveis" width="600" >}}

3. Para conexão manual, escolha **Conectar um serviço de nuvem** e selecione **WebDAV**. Digite o endereço do servidor no formato: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (ex.: [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Configuração manual do WebDAV" width="600" >}}

4. Deixe os campos de login e senha vazios para acesso de convidado, ou digite suas credenciais do Synology. Toque em **Entrar**.

## Passo 6: Navegar e reproduzir música

1. Após conectar, o dispositivo aparecerá na lista de **Acessórios conectados**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Dispositivos conectados no Evermusic" width="600" >}}

2. Navegue até a pasta **Música** e toque em qualquer arquivo de áudio para iniciar a reprodução.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Navegando pela pasta de música" width="600" >}}

## Passo 7: Adicionar pasta na nuvem conectada à biblioteca musical

1. Abra a seção **Biblioteca Musical** no app.
2. Escolha **Adicionar Música** e selecione **Conexões**.
3. Escolha o servidor NAS conectado e selecione a pasta **Música**. Toque em **Concluído**.
4. O app escaneará a pasta de música e adicionará os arquivos de áudio compatíveis à biblioteca musical. Os metadados serão carregados e suas faixas serão agrupadas por álbum, artista e gênero.

## Conclusão

Seguindo esses passos, você pode facilmente configurar uma conexão WebDAV no seu Synology NAS e transmitir sua biblioteca musical para o iPhone ou Mac usando Evermusic ou Flacbox. Aproveite o acesso contínuo às suas músicas favoritas a qualquer momento.

## Perguntas frequentes

{{% details title="Quais dispositivos NAS suportam WebDAV?" closed="true" %}}
A maioria das marcas populares de NAS suporta WebDAV, incluindo Synology, QNAP, TrueNAS e Western Digital. Consulte a documentação do fabricante do seu NAS para instruções de configuração do WebDAV.
{{% /details %}}

{{% details title="Qual é a diferença entre WebDAV e SMB para streaming de música do NAS?" closed="true" %}}
O WebDAV funciona via HTTP/HTTPS e é mais adequado para acesso remoto pela internet. O SMB é normalmente mais rápido em redes locais. Evermusic e Flacbox suportam ambos os protocolos, então escolha com base na necessidade de acesso local ou remoto.
{{% /details %}}

{{% details title="Preciso de nome de usuário e senha para WebDAV no Synology?" closed="true" %}}
Não, se você ativar o acesso anônimo WebDAV e configurar permissões de convidado na pasta compartilhada. Para maior segurança, você pode usar suas credenciais do Synology.
{{% /details %}}

{{% details title="Posso transmitir FLAC e outros formatos de alta resolução do NAS via WebDAV?" closed="true" %}}
Sim. Tanto o Evermusic quanto o Flacbox suportam FLAC, ALAC, WAV, DSD e outros formatos de alta resolução ao transmitir do armazenamento NAS via WebDAV.
{{% /details %}}

{{% details title="Por que o app não consegue encontrar meu NAS em Dispositivos disponíveis?" closed="true" %}}
Certifique-se de que seu iPhone/Mac e NAS estejam na mesma rede Wi-Fi. Se a descoberta automática não funcionar, use a opção de conexão manual e insira o endereço IP do NAS e a porta WebDAV diretamente.
{{% /details %}}
