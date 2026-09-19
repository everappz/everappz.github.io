---
title: "Definições"
date: 2026-08-20
description: "Uma visita completa às definições do Everdisk: perfil do dispositivo (nome e avatar), os cinco servidores de ligação, controlos de acesso, criptografia SMB (SMB3/AES), qualidade de fotografias e vídeos, portas personalizadas, miniaturas DLNA, opções de rede e transferência, opções do gestor de ficheiros e Premium."
keywords: ["definicoes Everdisk", "nome avatar do dispositivo", "servidores de ligacao", "qualidade de fotografias e videos", "portas personalizadas HTTP WebDAV FTP", "miniaturas DLNA", "transferencias em paralelo", "eliminar ficheiros permanentemente", "cache de miniaturas", "Everdisk Premium"]
tags: ["everdisk", "guia", "definicoes"]
readingTime: 12
---


O separador **Definições** agrupa tudo em três áreas principais - **Partilha**, **Rede** e **Gestor de Ficheiros** - além do Premium, do feedback e das ligações legais. Esta página explica cada definição e a respetiva predefinição.

## Premium

No topo das Definições vê o seu estado Premium, ou um botão **Desbloquear todas as funcionalidades**. O Everdisk é gratuito, com alguns limites; uma compra única **Premium Vitalícia** remove-os. Consulte [Premium](#premium-lifetime) no final desta página.

## Definições de Partilha

### Geral

- **Iniciar a partilha do dispositivo automaticamente** - inicia a partilha assim que abre a aplicação. *(Premium.)*
- **Partilhar Pasta Documentos** - partilha a pasta Documentos da própria aplicação. Ativado por predefinição.
- **Avisar antes de desligar** - lembra-o de reabrir a aplicação antes de o sistema a suspender em segundo plano. Desativado por predefinição; pede a permissão de notificações da primeira vez.

### Perfil do Dispositivo

- **Nome do Dispositivo** - o nome que os outros dispositivos veem para si na rede. Toque para editar. *(Premium.)*
- **Avatar do Dispositivo** - o ícone e a cor de fundo do seu dispositivo. Pode escolher um ícone, um gradiente de fundo ou **escolher um avatar das Fotografias**. *(Premium.)*
- **Gerar de Novo Nome e Avatar** e **Gerar de Novo Avatar** - obtenha um novo nome e/ou avatar aleatório. *(Gratuito.)*

### Acesso

- **Início de sessão** e **Palavra-passe** - exigem um início de sessão para as ligações do Navegador, do Computador e de Outras Aplicações.
- **Edição de Ficheiros** - permite que os dispositivos ligados carreguem, mudem o nome e eliminem. Ativado por predefinição.
- **Dispositivos Bloqueados** - faça a gestão dos dispositivos que bloqueou.

Consulte [Acesso e Privacidade](/docs/guide/everdisk/everdisk-guide-access) para mais detalhes.

### Ligações

Ative ou desative cada servidor. Todos os cinco estão ativados por predefinição, e cada um tem um botão de info (ⓘ) com instruções de ligação:

- **TV e Centro Multimédia** (DLNA)
- **Navegador** (HTTP)
- **Computador** (WebDAV)
- **Computador (avançado)** (SMB) - uma unidade de rede para Mac, Windows e Linux; num Mac aparece sozinha na barra lateral do Finder. A única ligação que pode ser criptografada.
- **Outras Aplicações e Dispositivos** (FTP)

### Fotografias

- **Formato** - Original ou Mais Compatível (JPEG).
- **Qualidade** - Original, Alta, Média ou Baixa.

Qualquer opção que não seja Original converte as fotografias à medida que são partilhadas, o que é mais lento. A conversão é uma funcionalidade Premium.

### Vídeos

- **Formato** - Original ou Mais Compatível (H.264 MP4).
- **Qualidade** - Original, Alta, Média ou Baixa.

A mesma ideia das Fotografias: o Original é o mais rápido e a conversão é Premium. Baixe a qualidade se uma TV mais antiga não conseguir reproduzir um vídeo.

### Avançado

- **Porta HTTP** (predefinição 80), **Porta WebDAV** (predefinição 8080), **Porta SMB** (predefinição 4455), **Porta FTP** (predefinição 2121). O DLNA escolhe a sua porta automaticamente. *(Alterar as portas é Premium; os utilizadores gratuitos podem ver os valores.)*

### Criptografia SMB

- **Exigir criptografia SMB** - cifra cada transferência SMB com **criptografia SMB3 (AES)** para que mais ninguém na rede consiga ler os seus ficheiros. Desativado por predefinição. Requer um **início de sessão e palavra-passe** definidos acima (as ligações criptografadas não podem ser anónimas) e um cliente que suporte SMB3, como o Finder num Mac moderno ou o Windows 10 e posterior. As alterações entram em vigor da próxima vez que iniciar a partilha. *(Premium.)*

### Miniaturas DLNA

- **Mostrar Miniaturas** - publica imagens de pré-visualização para as TVs. Ativado por predefinição (gratuito).
- Escolha que tamanhos publicar: **Pequeno (160px)**, **Médio (640px)**, **Grande (1024px)**, **Extra Grande (4096px)**.

## Definições de Rede

- **Transferências de Ficheiros** - use apenas **Wi-Fi**, ou **Wi-Fi e Dados Móveis**, para as transferências. Predefinição Wi-Fi.
- **Limite de Transferências em Paralelo** - quantas transferências decorrem em simultâneo. Predefinição 5.
- **Transferências em Segundo Plano** - mantêm as transferências a decorrer enquanto usa outros ecrãs. Ativado por predefinição.
- **Miniaturas de Ficheiros** - se as miniaturas dos ficheiros noutros dispositivos são obtidas apenas por Wi-Fi ou também por dados móveis. Predefinição Wi-Fi.

## Definições do Gestor de Ficheiros

- **Eliminar Ficheiros Permanentemente** - elimina imediatamente, sem lixo. Desativado por predefinição. Consulte [Acesso e Privacidade](/docs/guide/everdisk/everdisk-guide-access).
- **Repor Todas as Mensagens de Aviso** - traz de volta os banners de dicas que fechou.
- **Cache de Miniaturas** - veja quanto espaço ocupam as miniaturas em cache e **Limpar Cache de Miniaturas**.

## Feedback e legal

Na parte de baixo pode **Avaliar esta Aplicação**, **Enviar Feedback**, **Obter Mais Aplicações** e abrir os **Termos e Condições** e a **Política de Privacidade**.

## Premium Lifetime

O Everdisk é gratuito. Uma única compra **Premium Vitalícia** - um pagamento único, não uma subscrição - desbloqueia:

- **Pastas Ilimitadas** - partilhe mais de 5 pastas.
- **Ligações Ilimitadas** - guarde mais de 10 servidores no separador Dispositivos.
- **Conversão de Fotografias e Vídeos** - partilhe em qualquer qualidade que não seja a Original.
- **Criptografia SMB** - proteja as transferências SMB com criptografia SMB3 (AES).
- **Portas Personalizadas** - defina as suas próprias portas HTTP, WebDAV, SMB e FTP.
- **Iniciar Partilha Automaticamente** - inicie a partilha automaticamente ao abrir a aplicação.
- **Personalização do Dispositivo** - um nome de dispositivo, ícone de avatar, gradiente de fundo ou avatar de fotografia personalizados.

O Premium está associado ao seu Apple ID. Use **Restaurar Compras** para o desbloquear nos seus outros dispositivos com sessão iniciada no mesmo Apple ID.

## Passos seguintes

- [Partilha](/docs/guide/everdisk/everdisk-guide-sharing) - o ecrã de Partilha em detalhe.
- [Acesso e Privacidade](/docs/guide/everdisk/everdisk-guide-access) - palavras-passe, edição e bloqueio.
- [FAQ](/docs/faq/everdisk) - respostas rápidas às perguntas mais frequentes.
