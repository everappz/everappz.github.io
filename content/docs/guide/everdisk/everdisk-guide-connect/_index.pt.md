---
title: "Ligar os Seus Dispositivos"
date: 2026-08-20
description: "Instruções passo a passo para se ligar à sua unidade sem fios Everdisk: veja numa smart TV por DLNA, abra os seus ficheiros em qualquer navegador de Internet, monte o seu dispositivo como uma unidade de rede no Finder, no Windows ou no Linux por WebDAV ou SMB (com criptografia SMB3/AES opcional), ligue aplicações de ficheiros por FTP e transfira por cabo USB para um Mac sem Wi-Fi."
keywords: ["ligar ao Everdisk", "transmitir para TV DLNA", "abrir ficheiros no navegador", "montar unidade de rede Finder", "WebDAV Windows Linux", "aplicacao de ficheiros FTP", "transferencia por cabo USB Mac", "ligar iPhone ao computador", "unidade de rede iPhone"]
tags: ["everdisk", "guia", "ligar"]
readingTime: 11
---


Assim que tocar em **Iniciar** no ecrã de [Partilha](/docs/guide/everdisk/everdisk-guide-sharing), os outros dispositivos podem ligar-se aos seus ficheiros de cinco formas diferentes. Escolha o método que corresponde ao dispositivo que quer usar. Em todos os casos, o **endereço** exato de que precisa é mostrado na secção **Como Ligar** do ecrã de Partilha.

> Ambos os dispositivos têm de estar na **mesma rede Wi-Fi** - ou, no caso de um Mac, ligados por um **cabo USB** (consulte a última secção).

## Ver numa TV (DLNA)

Use isto para mostrar fotografias, vídeos e música numa smart TV ou leitor multimédia.

1. Em **Definições → Partilha → Ligações**, certifique-se de que **TV e Centro Multimédia** está ativado (está por predefinição).
2. No ecrã de Partilha, toque em **Iniciar**.
3. Na sua TV, abra o leitor multimédia integrado ou a aplicação de servidor multimédia (pode chamar-se Media Player, SmartShare, AllShare ou algo semelhante).
4. O seu dispositivo aparece na lista de servidores multimédia pelo seu nome (por exemplo "Speedy-Hare"). Selecione-o.
5. Explore as suas fotografias, vídeos e música partilhados e comece a reproduzir. As miniaturas de pré-visualização aparecem automaticamente.

Notas:

- O DLNA não pode ser protegido por palavra-passe, por isso esta ligação fica aberta a qualquer pessoa na mesma rede Wi-Fi enquanto estiver ativada.
- Se um vídeo não reproduzir numa TV mais antiga, baixe a qualidade do vídeo em **Definições → Partilha → Vídeos**, para que o Everdisk o converta para um formato mais compatível.

## Abrir num navegador de Internet (HTTP)

Use isto para entregar ficheiros a qualquer pessoa com um navegador de Internet - sem aplicações para instalar.

1. Em **Definições → Partilha → Ligações**, certifique-se de que **Navegador** está ativado.
2. Toque em **Iniciar**.
3. No ecrã de Partilha, copie o endereço do **Navegador** (ou mostre o respetivo código QR).
4. No outro telemóvel, tablet ou computador, abra qualquer navegador de Internet (Safari, Chrome, Edge, Firefox) e escreva esse endereço.
5. A página abre com os seus ficheiros partilhados.

No navegador, a outra pessoa pode:

- Alternar entre as vistas de **lista** e de **grelha** e ordenar por nome, data ou tamanho.
- Ver **miniaturas** reais de fotografias, vídeos, PDF e capas de música.
- Abrir uma fotografia numa **galeria** em ecrã inteiro, com deslize, zoom de dois dedos e apresentação de diapositivos.
- Reproduzir música num **leitor** integrado, com fila, ordem aleatória e repetição.
- **Transferir** qualquer ficheiro, ou transferir uma pasta inteira (ou vários itens selecionados) como um único **Archive.zip**.
- **Carregar** ficheiros de volta para o seu dispositivo - apenas se tiver ativado a **Edição de Ficheiros** (consulte [Acesso e Privacidade](/docs/guide/everdisk/everdisk-guide-access)).

## Usar como unidade de rede (WebDAV)

Use isto para fazer o seu dispositivo aparecer como um disco normal num Mac, PC com Windows ou máquina Linux, para que possa arrastar ficheiros nos dois sentidos.

**Num Mac (Finder)**

1. Em **Definições → Partilha → Ligações**, certifique-se de que **Computador** está ativado.
2. Toque em **Iniciar** e anote o endereço **Computador (WebDAV)**.
3. No Finder, escolha **Ir → Ligar ao Servidor** (ou prima **⌘K**).
4. Escreva o endereço WebDAV exatamente como é mostrado e clique em **Ligar**.
5. Introduza o início de sessão e a palavra-passe, se tiver definido algum; caso contrário, ligue-se como convidado.
6. O seu dispositivo abre como qualquer outra unidade de rede. Arraste ficheiros para dentro ou para fora.

**No Windows**

1. Abra o **Explorador de Ficheiros**, clique com o botão direito em **Este PC** e escolha **Adicionar uma localização de rede** (ou mapeie uma unidade de rede).
2. Introduza o endereço WebDAV mostrado no Everdisk.
3. Introduza o início de sessão e a palavra-passe, se tiver definido algum.

**No Linux**

1. Abra o seu gestor de ficheiros e escolha **Ligar ao Servidor** (ou use `davs://` / `dav://`).
2. Introduza o endereço WebDAV mostrado no Everdisk.

Se a ligação é só de leitura ou nos dois sentidos depende da definição **Edição de Ficheiros**. Com ela ativada, pode copiar ficheiros para o seu dispositivo e mudar-lhes o nome ou eliminá-los; com ela desativada, a unidade é só de leitura.

## Ligar por SMB (unidade de rede criptografada)

O SMB é uma unidade de rede para Mac, Windows e Linux, assente na partilha de ficheiros já existente nesses sistemas, por isso o seu dispositivo aparece como uma unidade de rede normal - e é a única ligação que pode criptografar.

1. Em **Definições → Partilha → Ligações**, certifique-se de que **Computador (avançado)** (a ligação SMB) está ativado.
2. Toque em **Iniciar** e anote o endereço **SMB**, que tem o aspeto `smb://192.168.1.20:4455/Share`.
3. Ligue-se a partir do seu computador:
   - **Mac:** o seu dispositivo aparece sozinho na **barra lateral do Finder** em **Localizações** (Rede) - basta clicar nele e iniciar sessão. Para se ligar manualmente, escolha **Ir → Ligar ao Servidor** (**⌘K**) e introduza o endereço.
   - **Windows:** abra o **Explorador de Ficheiros**, clique com o botão direito em **Este PC** e escolha **Mapear unidade de rede**, depois introduza `\\<address>\Share` usando o anfitrião e o nome da partilha mostrados no ecrã de Partilha (ou escreva o endereço `smb://` na barra de endereços).
   - **Linux:** no seu gestor de ficheiros escolha **Ligar ao Servidor** e introduza o endereço.
4. Introduza o início de sessão e a palavra-passe, se tiver definido algum; caso contrário, ligue-se como convidado.
5. A partilha chama-se **Share**. Com a **Edição de Ficheiros** ativada pode copiar ficheiros nos dois sentidos; com ela desativada é só de leitura.

**Ativar a criptografia (recomendado em Wi-Fi não fiável)**

O SMB é a única ligação do Everdisk que pode ser criptografada. Para proteger cada transferência com **criptografia SMB3 (AES)**:

1. Em **Definições → Partilha → Acesso**, defina um **Login** e uma **Palavra-passe** - as ligações criptografadas não podem ser anónimas.
2. Em **Definições → Partilha**, ative **Exigir criptografia SMB**.
3. **Pare e inicie** a partilha novamente para que a alteração entre em vigor.

O seu cliente tem de suportar SMB3 - o Finder num Mac moderno, ou o **Windows 10 e posterior**. A criptografia SMB é uma funcionalidade Premium.

## Ligar uma aplicação de ficheiros (FTP)

Use isto para aplicações de gestão e transferência de ficheiros que usam FTP (por exemplo, o FileZilla ou o Cyberduck num computador).

1. Em **Definições → Partilha → Ligações**, certifique-se de que **Outras Aplicações e Dispositivos** está ativado.
2. Toque em **Iniciar** e anote o endereço **FTP**.
3. Na sua aplicação FTP, adicione uma nova ligação com esse endereço.
4. Introduza o início de sessão e a palavra-passe, se tiver definido algum, ou deixe-os vazios para acesso anónimo.

## Transferir por cabo USB (Mac, sem necessidade de Wi-Fi)

Use isto quando não há Wi-Fi, ou quando quer a transferência mais rápida e mais privada. Funciona apenas com um **Mac**.

1. Ligue o seu iPhone ou iPad ao Mac com o cabo de carregamento normal.
2. Se lhe for pedido no dispositivo, toque em **Confiar Neste Computador**.
3. No Everdisk, toque em **Iniciar**. Aparece uma nota **Ligação Rápida Disponível** e o ecrã de Partilha mostra um endereço adicional com um selo **Ligação por Cabo** que termina em `.local`.
4. No Mac, abra o Finder → **Ir → Ligar ao Servidor** (**⌘K**) e introduza esse endereço `.local` (serve tanto para a ligação do Navegador como para a do Computador).
5. O seu dispositivo abre pelo cabo - mais rápido do que o Wi-Fi, e os dados nunca passam pelo router nem pela Internet.

Notas:

- Use o **nome `.local`**, não um endereço IP (os endereços IP só funcionam por Wi-Fi), e nunca `localhost`.
- O caminho por cabo é **só para Mac**. Os PCs com Windows e os dispositivos Android têm de usar Wi-Fi.
- Também pode arrastar ficheiros para a pasta do Everdisk usando o Finder num Mac, ou a aplicação Apple Devices (ou o iTunes) no Windows, através da partilha de ficheiros padrão do iOS.

## Passos seguintes

- [Acesso e Privacidade](/docs/guide/everdisk/everdisk-guide-access) - adicione uma palavra-passe, permita carregamentos, bloqueie um dispositivo.
- [Fotografias, Música e Vídeo](/docs/guide/everdisk/everdisk-guide-media) - partilhe toda a sua biblioteca e defina a qualidade.
- [Ligar a Servidores](/docs/guide/everdisk/everdisk-guide-devices) - aceda a outros dispositivos a partir do Everdisk.
