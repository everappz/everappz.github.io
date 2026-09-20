---
title: "Partilha"
date: 2026-08-20
description: "Saiba como funciona a partilha no Everdisk: toque em Iniciar para transformar o seu iPhone ou iPad numa unidade sem fios, escolha o que partilhar (ficheiros, pastas, fotografias e música), execute os cinco servidores (DLNA, HTTP, WebDAV, SMB, FTP), encripte a ligação SMB com SMB3 (AES), consulte os endereços de ligação, veja quem está ligado e mantenha a partilha ativa por Wi-Fi ou por um cabo USB."
keywords: ["partilha Everdisk", "unidade sem fios iPhone", "iniciar partilha", "partilhar ficheiros iPhone", "partilhar fotografias pela rede", "DLNA HTTP WebDAV FTP", "o que partilhar", "como ligar", "manter a aplicacao aberta", "partilha por Wi-Fi ou cabo USB"]
tags: ["everdisk", "guia", "partilha"]
readingTime: 9
---


O separador **Partilha** é o coração do Everdisk. É aqui que transforma o seu iPhone ou iPad numa unidade sem fios, escolhe exatamente o que quer partilhar e obtém os endereços que os outros dispositivos usam para se ligarem. É o primeiro separador que vê ao abrir a aplicação.

## Iniciar e parar a partilha

No centro do ecrã de Partilha há um grande botão redondo.

- Toque em **Iniciar** para colocar todos os servidores ativados online de uma só vez. O botão mostra **A iniciar...** e depois **Parar** assim que a partilha estiver ativa.
- Toque em **Parar** para voltar a colocar tudo offline. Os dispositivos ligados são desligados.

Enquanto a partilha estiver a decorrer, os ficheiros, fotografias e música que escolheu ficam disponíveis para qualquer dispositivo da mesma rede que se ligue por um dos cinco métodos indicados abaixo.

> A partilha só funciona enquanto a aplicação estiver aberta. Consulte **Manter a aplicação aberta**, perto do final desta página, para perceber porquê e como manter as transferências grandes a decorrer.

## Escolher o que partilhar

Antes de começar, toque no cabeçalho **O que partilhar** para abrir três grupos. Pode partilhar qualquer combinação deles, mas tem de escolher pelo menos um item antes de poder iniciar a partilha.

**Ficheiros e Pastas**

- A pasta **Documentos** da própria aplicação é partilhada por predefinição. Pode deixar de a partilhar, se preferir.
- Toque em **Adicionar Pasta** para partilhar uma pasta de qualquer local do seu dispositivo, ou em **Adicionar Ficheiro** para partilhar ficheiros individuais.
- Cada item partilhado tem um botão **Info** e um botão **Parar Partilha**.

**Fotografias e Vídeos**

- Ative **Permitir acesso a toda a Biblioteca de Fotografias** para partilhar toda a sua biblioteca de fotografias e vídeos, ou
- Toque em **Adicionar Fotografias** para escolher a dedo apenas as fotografias e vídeos que quer partilhar.

**Música**

- Ative **Permitir acesso a toda a Biblioteca de Música** para partilhar toda a sua biblioteca de música, ou
- Toque em **Adicionar Faixas** para partilhar apenas as músicas selecionadas.
- As faixas protegidas (DRM) ou guardadas apenas na nuvem não podem ser partilhadas.

Se tentar iniciar sem nada selecionado, o Everdisk mostra uma nota **Nada para Partilhar**. Se alterar o que está partilhado com a partilha em curso, **pare e inicie novamente** para aplicar a mudança.

## Os cinco servidores

O Everdisk partilha o mesmo conteúdo de cinco formas ao mesmo tempo. Cada uma foi pensada para um tipo diferente de dispositivo, e cada uma pode ser ativada ou desativada em **Definições → Partilha → Ligações**. Por predefinição, todas as cinco estão ativadas.

- **TV e Centro Multimédia (DLNA)** - para smart TVs e leitores multimédia. Descobrem o seu dispositivo por si próprios e mostram as suas fotografias, vídeos e música, com miniaturas de pré-visualização.
- **Navegador (HTTP)** - para qualquer telemóvel, tablet ou computador. A outra pessoa abre uma ligação num navegador de Internet para explorar e transferir os seus ficheiros. Nada para instalar.
- **Computador (WebDAV)** - para um Mac, PC com Windows ou máquina Linux. O seu dispositivo aparece como uma unidade de rede normal para que possa arrastar ficheiros em ambos os sentidos.
- **Computador (avançado) (SMB)** - uma unidade de rede para Mac, Windows e Linux. Num Mac aparece sozinha na barra lateral do Finder; no Windows, abra-a no Explorador de Ficheiros com um endereço `smb://`. É a única ligação que pode **encriptar**, com encriptação SMB3 (AES).
- **Outras Aplicações e Dispositivos (FTP)** - para aplicações de ficheiros e utilizadores avançados que usam FTP.

Para instruções de ligação passo a passo de cada tipo, consulte [Ligar os Seus Dispositivos](/docs/guide/everdisk/everdisk-guide-connect).

## Como Ligar e endereços de ligação

Depois de tocar em Iniciar, a secção **Como Ligar** mostra um cartão para cada servidor ativo com o **endereço** exato a escrever no outro dispositivo. Cada endereço é fácil de copiar - toque nele para o copiar, use o botão **Partilhar** para o enviar, ou toque no botão **info (ⓘ)** para instruções detalhadas por protocolo.

- O cartão DLNA mostra um endereço de descrição do dispositivo que termina em `/device-desc.xml`, para os leitores que o pedem.
- Quando o seu dispositivo está ligado a um Mac por cabo, aparece um endereço adicional com um selo **Ligação por Cabo** que usa o nome `.local` do seu dispositivo.

Também pode abrir o endereço como um **código QR**, para que a câmara de outro dispositivo o abra diretamente.

## Quem está ligado

A secção **Quem está Ligado** apresenta, em tempo real, os dispositivos atualmente ligados a si. Toque no botão de mais ações junto a qualquer dispositivo para **Bloquear este dispositivo** se não o reconhecer. Os dispositivos bloqueados são geridos em [Acesso e Privacidade](/docs/guide/everdisk/everdisk-guide-access).

## O nome e o avatar do seu dispositivo

Cada dispositivo tem um nome simpático (como "Speedy-Hare") e um avatar colorido. É o nome que uma TV, um computador ou outra aplicação mostra para o seu dispositivo na rede, para que seja fácil de identificar. Pode gerar de novo o nome e o avatar gratuitamente, ou definir um nome, ícone ou avatar de fotografia personalizados com o Premium. Consulte [Definições](/docs/guide/everdisk/everdisk-guide-settings).

## Partilha por Wi-Fi ou por cabo USB

A partilha pode decorrer em duas situações:

- **Por Wi-Fi** - o seu dispositivo e os outros dispositivos estão na mesma rede Wi-Fi.
- **Por cabo USB** - o seu dispositivo está ligado a um **Mac** por cabo, mesmo quando não há Wi-Fi nenhum. É mais rápido do que o Wi-Fi e continua a funcionar num avião, num hotel ou numa rede bloqueada.

Se não houver Wi-Fi nem cabo disponíveis, o botão **Iniciar** fica desativado e aparece uma nota **Sem Ligação Wi-Fi**. Se a ligação cair durante a partilha, o Everdisk para a partilha automaticamente e avisa-o. Toque no botão de info em qualquer destas notas para uma explicação completa.

## Manter a aplicação aberta

Como o seu iPhone ou iPad está a funcionar como servidor, **a partilha só funciona enquanto o Everdisk estiver aberto no ecrã**. Se fechar a aplicação ou bloquear o dispositivo por muito tempo, o sistema pode suspender a aplicação e a partilha para.

Para transferências grandes:

- Mantenha o Everdisk aberto e em primeiro plano.
- Ligue o seu dispositivo à corrente.
- Defina o **Bloqueio Automático** como **Nunca** na aplicação Definições do iOS enquanto transfere.

Pode ativar **Avisar antes de desligar** (em Definições → Partilha) para que o Everdisk o lembre de reabrir a aplicação antes de o sistema a suspender. Toque no botão de info no banner **Manter a aplicação aberta** para mais detalhes.

## Passos seguintes

- [Ligar os Seus Dispositivos](/docs/guide/everdisk/everdisk-guide-connect) - ligue uma TV, um computador, um navegador, um telemóvel ou um cabo USB.
- [Acesso e Privacidade](/docs/guide/everdisk/everdisk-guide-access) - adicione uma palavra-passe e controle a edição.
- [Definições](/docs/guide/everdisk/everdisk-guide-settings) - ative ou desative servidores e ajuste a qualidade.
