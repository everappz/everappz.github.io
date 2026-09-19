---
title: "Ligar a Servidores"
date: 2026-08-20
description: "Use o separador Dispositivos do Everdisk para se ligar a outros servidores da sua rede. Adicione e explore servidores DLNA, WebDAV, FTP, SFTP e SMB e unidades NAS, transmita áudio e vídeo, transfira ficheiros e crie, carregue, mude o nome, mova ou elimine em servidores que o permitam."
keywords: ["separador Dispositivos Everdisk", "ligar a NAS", "cliente DLNA iPhone", "cliente WebDAV iPhone", "cliente FTP iPhone", "cliente SFTP iPhone", "cliente SMB iPhone", "ligar a partilha SMB", "explorar servidor de rede", "transmitir a partir de NAS", "transferir de servidor", "ligar nuvem WebDAV"]
tags: ["everdisk", "guia", "dispositivos", "ligacoes"]
readingTime: 9
---


O Everdisk não é apenas uma unidade sem fios - é também um cliente para os outros dispositivos da sua rede. O separador **Dispositivos** permite-lhe ligar-se a servidores **DLNA**, **WebDAV**, **FTP**, **SFTP** e **SMB**, incluindo Macs, PCs com Windows, máquinas Linux, unidades NAS e servidores multimédia, e depois explorar, transmitir e transferir os ficheiros deles.

## O ecrã de Dispositivos

O separador Dispositivos tem duas partes:

- **Ligações** - os servidores que já guardou.
- **Dispositivos Disponíveis** - os servidores que o Everdisk encontra automaticamente na sua rede local.

Para se ligar a algo que o Everdisk já encontrou, basta tocar nele em **Dispositivos Disponíveis**. Para adicionar um servidor manualmente, toque no botão **mais (+)** ou em **Nova Ligação**.

## Adicionar uma nova ligação

Toque em **Nova Ligação** e escolha o tipo de servidor que quer alcançar:

- **DLNA / UPnP** - o melhor para servidores multimédia. Transmita vídeo, música e fotografias a partir de bibliotecas multimédia, unidades de armazenamento em rede e TVs e computadores com DLNA. O DLNA é só de leitura: pode explorar, transmitir e transferir, mas não pode carregar nem alterar ficheiros.
- **WebDAV** - ligue-se a servidores de ficheiros, unidades de armazenamento em rede e unidades na nuvem que suportem WebDAV. Leitura e escrita quando o servidor o permitir.
- **FTP** - comum em routers, unidades de armazenamento em rede e alojamento web. A porta predefinida é a 21 (990 para FTPS seguro); pode definir uma porta personalizada no endereço, por exemplo `ftp://host:2121`. Deixe o início de sessão e a palavra-passe vazios para acesso anónimo.
- **SFTP** - ligue-se em segurança por SSH. A porta predefinida é a 22; use uma porta personalizada no endereço, se necessário, por exemplo `sftp://host:2222`.
- **SMB** - ligue-se a Macs, PCs com Windows, servidores Linux e armazenamento em rede (NAS) que partilham pastas por **SMB / CIFS**. Introduza um endereço como `smb://server-address/share-name/` (exemplos: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). O SMB acrescenta dois campos opcionais: um nome de **Grupo de trabalho** e uma **Versão do protocolo** que pode deixar em **Automática** ou forçar para **SMB1** ou **SMB2**. Se ficheiros ou pastas com carateres especiais não abrirem, tente mudar a versão para **SMB1**.

> O Everdisk liga-se apenas a estes protocolos de rede local e de endereço direto. Não inicia sessão em contas na nuvem como o Google Drive ou o Dropbox. Uma unidade na nuvem só é acessível se esse serviço oferecer um endereço **WebDAV** que possa escrever.

## Introduzir o endereço e iniciar sessão

No editor de ligação, preencha:

- **Título** - um nome simpático para a ligação.
- **URL / endereço** - o endereço do servidor (são mostrados exemplos para cada tipo).
- **Início de sessão** e **Palavra-passe** - deixe ambos vazios se o servidor permitir acesso anónimo.

No WebDAV pode permitir certificados inválidos se o seu servidor usar um autoassinado. Se a identidade de um servidor seguro não puder ser verificada, o Everdisk pede-lhe que confirme antes de confiar nele.

Os utilizadores gratuitos podem guardar até **10** ligações. O Premium remove o limite.

## Explorar, transmitir e transferir

Assim que estiver ligado, toque no servidor para o abrir:

- **Explore** as pastas em lista ou em grelha, ordene-as e veja miniaturas. Os servidores DLNA também mostram detalhes de música e capas.
- **Transmita** áudio e vídeo. O áudio vai para a fila do mini leitor; o vídeo reproduz em ecrã inteiro. É possível avançar enquanto um ficheiro está a ser transmitido.
- **Transfira** ficheiros para o seu dispositivo. Selecione vários de uma vez para uma transferência em lote. As transferências aparecem em **Transferências de Ficheiros** e vão parar à sua pasta **Documentos**.
- **Info** em qualquer item mostra o tipo, o tamanho, a data, o caminho e os detalhes multimédia.

## Alterar ficheiros num servidor

Em servidores que permitem escrita - **WebDAV, FTP, SFTP e SMB** - também pode gerir ficheiros:

- **Nova Pasta**
- **Carregar Ficheiros** a partir do seu dispositivo
- **Mudar o Nome**, **Mover** e **Eliminar** (um item ou vários de uma vez)

Os servidores **DLNA** são só de leitura, por isso estas ações não estão disponíveis nesses casos.

## Acompanhar as suas transferências

As transferências (para dentro e para fora) decorrem em segundo plano e aparecem em **Transferências de Ficheiros**, que abre a partir do canto superior esquerdo do separador **Documentos**. Aí pode acompanhar o progresso e colocar em pausa, retomar, tentar de novo, cancelar ou limpar tarefas. Também pode ajustar as transferências em [Definições → Rede](/docs/guide/everdisk/everdisk-guide-settings) (apenas Wi-Fi vs. Wi-Fi e dados móveis, quantas decorrem em simultâneo e se continuam em segundo plano).

## Passos seguintes

- [Ficheiros e Documentos](/docs/guide/everdisk/everdisk-guide-files) - faça a gestão de tudo o que transferir.
- [Fotografias, Música e Vídeo](/docs/guide/everdisk/everdisk-guide-media) - reproduza o que transmite.
- [Definições](/docs/guide/everdisk/everdisk-guide-settings) - limites de ligações e opções de transferência.
