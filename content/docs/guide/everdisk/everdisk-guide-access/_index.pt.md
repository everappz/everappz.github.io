---
title: "Acesso e Privacidade"
date: 2026-08-20
description: "Mantenha a sua partilha do Everdisk segura: proteja o acesso com um início de sessão e palavra-passe, encripte a ligação SMB com SMB3 (AES), controle se os dispositivos ligados podem carregar, mudar o nome e eliminar com a Edição de Ficheiros, bloqueie dispositivos desconhecidos, escolha entre lixo e eliminação permanente e perceba porque é que tudo permanece na sua rede local."
keywords: ["protecao por palavra-passe Everdisk", "encriptacao SMB", "encriptacao SMB3 AES", "interruptor edicao de ficheiros", "bloquear dispositivo", "dispositivos bloqueados", "eliminar ficheiros permanentemente", "apenas rede local", "partilha de ficheiros privada", "DLNA sem palavra-passe", "seguranca de rede"]
tags: ["everdisk", "guia", "acesso", "privacidade", "seguranca"]
readingTime: 8
---


O Everdisk mantém os seus ficheiros na sua própria rede e dá-lhe controlos simples sobre quem lhes pode aceder e o que pode fazer. Encontra estes controlos em **Definições → Partilha → Acesso**, além de algumas definições relacionadas no Gestor de Ficheiros.

## Proteger o acesso com um início de sessão e palavra-passe

Por predefinição, qualquer pessoa na mesma rede que tenha o seu endereço pode abrir os seus ficheiros partilhados. Para exigir um início de sessão:

1. Vá a **Definições → Partilha → Acesso**.
2. Introduza um **Início de sessão** e uma **Palavra-passe**.
3. Agora as ligações **Navegador (HTTP)**, **Computador (WebDAV)**, **Computador (avançado) (SMB)** e **Outras Aplicações e Dispositivos (FTP)** pedem todas esses dados antes de mostrarem os seus ficheiros.

Deixe ambos os campos vazios para acesso aberto. A sua palavra-passe é guardada em segurança no Keychain do dispositivo.

> **O DLNA está sempre aberto.** A ligação TV e Centro Multimédia (DLNA) não pode ser protegida por palavra-passe, por isso, assim que estiver ativada, qualquer dispositivo na mesma rede Wi-Fi pode explorar a sua multimédia partilhada. Desative-a se só quiser ligações protegidas, e partilhe apenas em redes de confiança.

## Encriptar a ligação SMB (SMB3 / AES)

Um início de sessão e palavra-passe controlam **quem** se pode ligar, mas os próprios dados continuam a viajar sem cifragem na maioria das ligações. **O SMB é a única ligação que o Everdisk pode encriptar**, o que baralha cada transferência para que mais ninguém na mesma rede a consiga ler.

Para a ativar:

1. Defina um **Início de sessão** e uma **Palavra-passe** como acima - as ligações encriptadas não podem ser anónimas.
2. Vá a **Definições → Partilha** e ative **Exigir encriptação SMB**.
3. **Pare e inicie** a partilha novamente para que a alteração entre em vigor.

Cada transferência SMB fica então protegida com **encriptação SMB3 (AES)**. O dispositivo que se liga tem de suportar SMB3 - o Finder num Mac moderno, ou o **Windows 10 e posterior**. É uma ótima escolha em Wi-Fi em que não confia totalmente. A encriptação SMB é uma funcionalidade Premium.

## Permitir ou bloquear a edição (Edição de Ficheiros)

O interruptor **Edição de Ficheiros** controla se os dispositivos ligados podem apenas ver os seus ficheiros, ou também alterá-los.

- **Ativado** (a predefinição): os dispositivos ligados podem **carregar, mudar o nome e eliminar** os seus ficheiros partilhados - por isso o seu dispositivo funciona como uma verdadeira unidade de rede nos dois sentidos.
- **Desativado**: os seus ficheiros partilhados ficam **só de leitura**. Os outros podem ver e transferir, mas não podem adicionar nem alterar nada.

Ativá-lo mostra um breve aviso, porque permite que outras pessoas modifiquem os seus ficheiros. Apresenta um selo **Importante** enquanto estiver ativado.

## Bloquear um dispositivo

Se vir um dispositivo que não reconhece:

1. No ecrã de Partilha, encontre-o em **Quem está Ligado**.
2. Toque no respetivo botão de mais ações e escolha **Bloquear este dispositivo**.

Os dispositivos bloqueados estão listados em **Definições → Partilha → Acesso → Dispositivos Bloqueados**, onde pode **desbloquear** um ou **Desbloquear Todos**. O bloqueio segue o dispositivo mesmo que o seu endereço de rede mude (para as ligações do Navegador, do Computador e da TV).

## Lixo vs. eliminação permanente

Quando um ficheiro é eliminado - por si no gestor de ficheiros, ou por um dispositivo ligado - vai normalmente para um **lixo** recuperável, para que o possa recuperar.

Se preferir que os ficheiros sejam removidos imediatamente, sem recuperação, ative **Eliminar Ficheiros Permanentemente** em **Definições → Gestor de Ficheiros → Eliminação de Ficheiros**. Está desativado por predefinição. **Afeta o gestor de ficheiros no dispositivo** e as **eliminações feitas pela rede**; não altera a forma como a biblioteca de Fotografias ou a biblioteca de Música do sistema tratam a eliminação.

## Tudo permanece local

O Everdisk partilha apenas pela sua **rede local** - nada é carregado para a Internet e não existe qualquer conta na nuvem pelo meio. Vale a pena saber algumas coisas:

- O Everdisk precisa da permissão **Rede Local** do iOS para que os dispositivos próximos o consigam encontrar. Se essa permissão estiver desativada, uma nota explica como a voltar a ativar na aplicação Definições do iOS.
- Para maior privacidade, partilhe apenas quando estiver numa rede Wi-Fi **doméstica ou privada** de confiança, e tenha cuidado em redes Wi-Fi públicas. Um início de sessão e palavra-passe ajudam, mas não substituem uma rede de confiança.
- A **opção mais privada de todas é um cabo USB para um Mac** - os dados vão diretamente pelo cabo e nunca passam pelo router nem pela Internet. Consulte [Ligar os Seus Dispositivos](/docs/guide/everdisk/everdisk-guide-connect).

## Passos seguintes

- [Partilha](/docs/guide/everdisk/everdisk-guide-sharing) - escolha o que partilhar e inicie a partilha.
- [Definições](/docs/guide/everdisk/everdisk-guide-settings) - todas as definições de Acesso e do Gestor de Ficheiros num só lugar.
