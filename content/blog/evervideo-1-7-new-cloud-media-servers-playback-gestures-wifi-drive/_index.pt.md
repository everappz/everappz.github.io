---
title: "Evervideo 1.7: novo Plex, Jellyfin, streaming na nuvem, gestos de reprodução"
date: 2026-05-18
description: "O Evervideo 1.7 adiciona mais de 10 novas conexões — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — além de novos gestos de reprodução (duplo toque para avançar, toque e segure para velocidade 2x), um Wi-Fi Drive renovado com envio em lote e atualizações de UI Liquid Glass para iPhone, iPad e Mac."
keywords: ["Evervideo 1.7", "atualização Evervideo", "reprodutor de vídeo HD iPhone", "reprodutor de vídeo Plex iOS", "Jellyfin iPhone vídeo", "reprodutor de vídeo Emby iOS", "Subsonic vídeo iOS", "Navidrome vídeo iOS", "streaming de vídeo Internxt", "reprodutor de vídeo Proton Drive", "reprodutor de vídeo QNAP iPhone", "reprodutor de vídeo Nextcloud iOS", "streaming de vídeo Amazon S3", "reprodutor de vídeo SFTP iPhone", "reprodutor de vídeo FTP iOS", "streaming de vídeo NFS iPhone", "transmitir vídeo do NAS iPhone", "reprodutor MKV iPhone", "gestos do reprodutor de vídeo iOS", "duplo toque para avançar vídeo", "transferência de vídeo Wi-Fi Drive iPhone", "design Liquid Glass", "reprodutor de vídeo na nuvem iOS 2026", "transmitir filmes da nuvem iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Gestos de reprodução", "Liquid Glass", "Novidades"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**Resumo:** [Evervideo 1.7](/products/evervideo) é uma grande atualização do reprodutor de vídeo HD para iPhone, iPad e Mac. A versão adiciona mais de 10 novas conexões de nuvem, NAS e servidores de mídia — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, além dos servidores de mídia mais populares **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** e **Emby**, e três protocolos de rede: **FTP**, **SFTP** e **NFS**. Os novos **gestos de reprodução** permitem duplo toque para avançar ou voltar, toque e segure para reproduzir a 2x, e toque único para alternar os controles — tudo sem sair do modo de tela cheia. O Wi-Fi Drive ganhou uma UI renovada com modo de seleção e uma fila de envio mais inteligente. Toda a aplicação foi ajustada para o novo design **Liquid Glass** da Apple.

---

## Olá a todos!

Chegou uma grande atualização do Evervideo. Esta é uma das maiores versões que já lançamos: **mais de 10 novas conexões de nuvem, servidor e rede**, **gestos de reprodução** totalmente novos para controle mais rápido em tela cheia, uma experiência **Wi-Fi Drive** renovada e uma UI ajustada para **Liquid Glass** em iPhone, iPad e Mac.

[Baixe o Evervideo 1.7 na App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) ou atualize a partir da sua versão atual. Usuários de Mac podem obter a [versão desktop aqui](https://apps.apple.com/app/evervideo/id6743504109).

## Mais de 10 novas conexões de nuvem, NAS e servidores de mídia

O Evervideo 1.7 expande o que conta como sua «biblioteca de vídeos». Se seus filmes, séries ou gravações estão em uma nuvem em que você confia, num NAS em casa, ou num servidor de mídia auto-hospedado, o Evervideo agora pode transmitir deles diretamente — sem downloads, sem conversões, sem recodificação.

### Nuvem focada em privacidade: Internxt e Proton Drive

Se você se importa com criptografia de ponta a ponta e armazenamento zero-knowledge, duas das nuvens focadas em privacidade mais respeitadas estão agora nativas no Evervideo:

- **Internxt** — nuvem espanhola de código aberto, com criptografia pós-quântica, em conformidade com o RGPD. Plano gratuito disponível.
- **Proton Drive** — armazenamento com criptografia de ponta a ponta dos criadores do Proton Mail e Proton VPN, com sede na Suíça. Plano gratuito disponível e planos pagos para bibliotecas maiores.

Conecte-se uma vez e seus vídeos serão transmitidos pelo túnel criptografado — o Evervideo nunca vê seus dados em texto claro, e nem o servidor do provedor.

### Armazenamento auto-hospedado: QNAP, Nextcloud, Amazon S3

Para usuários que mantêm a própria infraestrutura:

- **QNAP** — conexão nativa via API a dispositivos QNAP NAS para reprodução de vídeo rápida e confiável por Wi-Fi local ou acesso remoto. Transmita arquivos MKV em 4K diretamente, sem recodificação.
- **Nextcloud** — conecte-se a qualquer instância Nextcloud, auto-hospedada ou gerenciada. Ótimo se você já migrou do Google Drive ou Dropbox por motivos de privacidade.
- **Amazon S3** — aponte o Evervideo para qualquer bucket S3 (ou armazenamento compatível com S3 como Backblaze B2, Wasabi, MinIO, Cloudflare R2) e transmita sua coleção diretamente.

### <a id="media-servers"></a>Servidores de mídia: Plex, Subsonic, Navidrome, Jellyfin, Emby

Esta é a grande novidade para os fãs de vídeo auto-hospedado. O Evervideo 1.7 transforma seu iPhone, iPad ou Mac em um cliente de primeira linha para os servidores de mídia open-source e freemium mais populares:

- **Plex** — o Plex Media Server é **gratuito** para baixar e executar, com assinatura **Plex Pass** opcional para recursos como sincronização móvel, transcodificação por hardware e TV ao vivo. O Evervideo funciona tanto com bibliotecas gratuitas quanto Plex Pass — transmita sua coleção completa de filmes e séries.
- **Subsonic** — o servidor original de streaming auto-hospedado. O servidor oficial Subsonic é **pago** (US$ 1/mês após 30 dias de teste), e o Evervideo também fala a API Subsonic com servidores de vídeo compatíveis.
- **Navidrome** — servidor moderno, leve, **totalmente gratuito e de código aberto**. Implementa a API Subsonic. Roda num Raspberry Pi, NAS ou qualquer máquina Linux.
- **Jellyfin** — servidor de mídia **totalmente gratuito e de código aberto** (um fork comunitário do Emby). Lida com filmes, séries, música, livros e vídeos caseiros. Sem contas, sem telemetria, sem assinaturas. A escolha favorita para quem quer streaming auto-hospedado sem amarras comerciais.
- **Emby** — servidor de mídia **freemium**. O servidor central é gratuito; o **Emby Premiere** é uma compra única ou anual que desbloqueia apps móveis, sincronização offline, Modo Cinema e mais. O Evervideo conecta-se tanto a bibliotecas gratuitas quanto Premiere.

Qualquer que seja o servidor que você usa, o Evervideo transmite sua biblioteca completa — filmes, séries, vídeos caseiros e faixas de legendas incorporadas — com o equalizador de vídeo, suporte 360°, Picture-in-Picture, AirPlay e Chromecast.

### Novos protocolos de rede: FTP, SFTP, NFS

Para usuários com servidores personalizados, homelabs ou NAS genéricos que não vêm com um aplicativo móvel polido, o Evervideo 1.7 adiciona três protocolos clássicos:

- **SFTP (SSH File Transfer Protocol)** — a resposta certa para **streaming seguro e remoto de vídeo do seu próprio servidor**. O SFTP roda em cima do SSH, então toda a transferência (autenticação e dados de vídeo) é criptografada. Se você tem um VPS, servidor dedicado ou máquina Linux em casa com acesso SSH, pode colocar uma pasta de vídeos nele e transmitir pela internet pública sem expor mais nada. Suporta autenticação por senha e por chave.
- **FTP** — o padrão de longa data para transferência de arquivos. Útil se seu **NAS doméstico** (Synology mais antigo, ASUS, D-Link, TerraMaster ou dispositivos genéricos) expõe um servidor FTP, mas não tem integração nativa de API. Melhor usado dentro da sua rede local.
- **NFS (Network File System)** — o protocolo de compartilhamento de fato no Linux e na maioria dos dispositivos NAS. Compartilhamentos NFS são comuns em homelabs e pequenas redes empresariais; o Evervideo agora os monta e transmite vídeo em 4K e HD com baixa sobrecarga.

> **Dica:** SFTP é o protocolo que você quer para streaming pela internet aberta. FTP e NFS são melhores dentro da sua rede local — mantenha-os fora da internet pública, a menos que estejam dentro de uma VPN.

## Novos gestos de reprodução

Assistir a vídeos em tela cheia deve ser sem esforço. O Evervideo 1.7 introduz um conjunto limpo de gestos de toque que permitem controlar a reprodução sem expor os controles na tela — perfeito para filmes, palestras ou qualquer coisa que você queira assistir sem interrupções.

### Duplo toque — avançar ou voltar

Toque duas vezes no **lado direito** da tela para **avançar** por um número configurável de segundos. Toque duas vezes no **lado esquerdo** para **voltar**. Você pode alterar o intervalo (padrão: 10 segundos) em **Configurações → Reprodução → Intervalo de salto por gesto** — escolha qualquer valor entre 5 segundos (para busca fina) e 60 segundos (para pular intros).

Este é o gesto que usuários do YouTube e da Netflix reconhecem instantaneamente, e agora ele é nativo no Evervideo para qualquer vídeo, de qualquer fonte.

### Toque e segure — velocidade 2x temporária

Pressione e segure em qualquer lugar da tela para **acelerar temporariamente a reprodução para 2x**. Solte para voltar à velocidade normal. Perfeito para:

- Pular cenas lentas sem se comprometer com uma mudança permanente de velocidade.
- Escanear rapidamente palestras, tutoriais ou podcasts para encontrar a parte relevante.
- Amostrar filmes antes de se comprometer a assistir à versão completa.

O gesto de segurar não muda sua velocidade de reprodução salva — solte e você volta para onde estava.

### Toque único — mostrar / ocultar controles

Um único toque na tela alterna os controles de reprodução (reproduzir, pausar, barra de busca, legendas, equalizador). Toque uma vez para exibi-los, toque novamente para ocultá-los. Combinado com duplo toque e toque longo, isso significa que você pode passar quase um filme inteiro em modo tela cheia limpo e ainda assim buscar, pausar e escanear em velocidade sempre que precisar.

## Wi-Fi Drive: nova UI e envios mais rápidos

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) é o recurso integrado do Evervideo para **transferir vídeos sem fio do seu computador para seu iPhone ou iPad — sem iTunes, sem cabos, sem conta na nuvem**. Ambos os dispositivos precisam estar na mesma rede Wi-Fi. Você inicia o servidor no app iOS e, depois:

- Abre a URL em qualquer navegador desktop (Safari, Chrome, Firefox, Edge), arrasta seus arquivos de vídeo para a página, e eles são enviados diretamente para o dispositivo, ou
- Monta o dispositivo como um compartilhamento de rede via **Finder do Mac** («Conectar ao servidor…») ou **Explorador de Arquivos do Windows** (Mapear unidade de rede) usando WebDAV.

É a forma mais rápida de mover uma grande coleção local de vídeo para seu telefone ou tablet sem qualquer serviço de terceiros. Veja o [guia passo a passo aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

No Evervideo 1.7, o Wi-Fi Drive ganha:

- **Interface de usuário redesenhada** — mais limpa, mais fácil de ler à primeira vista e atualizada para Liquid Glass.
- **Novo modo de seleção para ações em lote** — selecione múltiplos arquivos ou pastas e atue sobre eles em massa (excluir, mover, copiar).
- **Fila de envio de arquivos melhorada** — melhor feedback de progresso e resiliência a soluços de rede, para que uma conexão Wi-Fi instável não estrague mais uma transferência de 30 GB.
- **Melhor desempenho geral de transferência** — envios mensuravelmente mais rápidos para bibliotecas grandes, especialmente para arquivos MKV em 4K e coleções de filmes.

## Outras melhorias

### Atualizações de design Liquid Glass

A interface do Evervideo 1.7 está atualizada para o novo material **Liquid Glass** da Apple em todo o app — superfícies translúcidas, animações mais suaves e controles refinados que se encaixam naturalmente no iOS 26, iPadOS 26 e macOS 26. Now Playing, o navegador de arquivos e as telas de configurações foram todos reajustados para combinar com a nova estética do sistema.

### Bibliotecas de conexão atualizadas

Renovamos as bibliotecas subjacentes que o Evervideo usa para falar com **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** e outros serviços. O resultado: menos falhas de conexão em casos de borda, melhor suporte para versões mais novas de servidores e maior confiabilidade ao transmitir vídeo em conexões mais lentas ou geograficamente distantes.

### Correções de bugs de reprodução

- Corrigidos problemas de reprodução em certos servidores auto-hospedados onde as transmissões travavam após buscar em grandes arquivos MKV.
- Melhor comportamento de retomada quando a rede cai brevemente no meio da reprodução.
- Sincronização de legendas mais suave em conteúdo de formato longo.

### Correções de localização

Correções de tradução em vários idiomas com base em feedback direto dos usuários. Melhor ajuste de texto em botões menores e em idiomas europeus mais longos (alemão, holandês, francês).

### Pequenos refinamentos inspirados em seus comentários

Muitas pequenas melhorias com base em avaliações da App Store e e-mails para support@everappz.com. Lemos cada mensagem.

## Por que esta atualização importa

O Evervideo 1.7 é construído em torno de três ideias:

1. **Seus vídeos, onde quer que você os mantenha.** Seja sua biblioteca no iCloud Drive, em uma nuvem focada em privacidade como Proton Drive ou Internxt, em um servidor de mídia como Plex ou Jellyfin, em um NAS em casa, ou em um Raspberry Pi rodando Navidrome — o Evervideo agora se conecta a tudo isso nativamente, com a mesma experiência de reprodução em todos os lugares.
2. **Vídeo em tela cheia que parece sem esforço.** Os novos gestos de toque (duplo toque, toque e segure, toque único) trazem o tipo de controle fluido que apps de streaming como YouTube e Netflix treinaram os usuários a esperar, aplicado à *sua* coleção de vídeo.
3. **Transferências mais rápidas do seu computador.** Um Wi-Fi Drive renovado com seleção em lote e uma fila de envio mais inteligente torna a movimentação de grandes coleções de filmes em 4K para seu iPhone ou iPad genuinamente rápida — sem cabos, sem iTunes, sem compressão.

## Obtenha o Evervideo 1.7

[**Baixe o Evervideo na App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) ou atualize de dentro da App Store. A [versão para Mac](https://apps.apple.com/app/evervideo/id6743504109) está disponível separadamente como app universal de Mac. O Evervideo é um download gratuito com upgrades opcionais no app para recursos avançados. As novas conexões de nuvem, suporte a servidores de mídia, gestos de reprodução, melhorias do Wi-Fi Drive e UI Liquid Glass fazem parte da atualização base.

Se você gosta do app, deixe uma avaliação na App Store — isso ajuda muito. Tem comentários ou encontrou um problema? Envie-nos um e-mail para **support@everappz.com**. Lemos cada mensagem.

## Perguntas frequentes

{{% details title="O que há de novo no Evervideo 1.7?" closed="true" %}}
O Evervideo 1.7 introduz suporte a mais de 10 novas conexões (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), novos gestos de reprodução (duplo toque para avançar, toque e segure para velocidade 2x, toque único para alternar controles), um Wi-Fi Drive redesenhado com modo de seleção e fila de envio mais inteligente, atualizações de design Liquid Glass, bibliotecas de conexão atualizadas e muitas correções de bugs.
{{% /details %}}

{{% details title="O Evervideo funciona com o Plex?" closed="true" %}}
Sim. A partir do Evervideo 1.7, você pode se conectar a um Plex Media Server e transmitir sua biblioteca de vídeo completa — filmes, séries e vídeos caseiros. O Plex Media Server é gratuito para executar; o Plex Pass é opcional. O Evervideo suporta configurações gratuitas e Plex Pass, incluindo reprodução direta de MKV, MP4, AVI, MOV e outros formatos sem recodificação.
{{% /details %}}

{{% details title="O Jellyfin ou o Navidrome são suportados no Evervideo?" closed="true" %}}
Sim. Tanto o Jellyfin quanto o Navidrome são totalmente suportados no Evervideo 1.7. O Jellyfin é um servidor de mídia gratuito e de código aberto que lida com vídeo e áudio. O Navidrome é um servidor gratuito e de código aberto que implementa a API Subsonic. O Evervideo se conecta a ambos nativamente.
{{% /details %}}

{{% details title="O Plex, Jellyfin, Emby, Navidrome e Subsonic são gratuitos?" closed="true" %}}
- **Plex** — o servidor é gratuito; o Plex Pass é um upgrade pago opcional.
- **Jellyfin** — totalmente gratuito e de código aberto.
- **Emby** — o servidor é gratuito; o Emby Premiere é pago e desbloqueia sincronização móvel e modo offline.
- **Navidrome** — totalmente gratuito e de código aberto.
- **Subsonic** — o servidor oficial custa US$ 1/mês após um teste de 30 dias, mas sua API é aberta e muitos servidores gratuitos (incluindo Navidrome) a implementam.
{{% /details %}}

{{% details title="Posso transmitir do meu NAS doméstico via SFTP, FTP ou NFS?" closed="true" %}}
Sim. O Evervideo 1.7 adiciona SFTP, FTP e NFS como tipos de conexão nativos. SFTP é a escolha recomendada para streaming a partir do seu próprio servidor pela internet pública porque todo o tráfego é criptografado via SSH. FTP e NFS são melhores dentro da sua rede local ou atrás de uma VPN.
{{% /details %}}

{{% details title="Como conecto o Evervideo a um servidor personalizado usando SFTP?" closed="true" %}}
Abra o Evervideo, vá para a aba Conexões, escolha SFTP e digite o hostname ou IP do servidor, a porta (geralmente 22), o nome de usuário e uma senha ou chave SSH privada. O Evervideo navegará pelas suas pastas remotas e transmitirá arquivos de vídeo diretamente com criptografia de ponta a ponta.
{{% /details %}}

{{% details title="O Evervideo suporta Internxt e Proton Drive?" closed="true" %}}
Sim. Ambas as nuvens focadas em privacidade são suportadas a partir do Evervideo 1.7. Elas se juntam ao MEGA e a outros serviços focados em privacidade já disponíveis no app.
{{% /details %}}

{{% details title="Como funcionam os novos gestos de reprodução?" closed="true" %}}
Na reprodução de vídeo em tela cheia, **toque duas vezes no lado direito** para avançar e **toque duas vezes no lado esquerdo** para voltar por um intervalo configurável (padrão 10 segundos — altere em Configurações). **Toque e segure** em qualquer lugar da tela para acelerar temporariamente para 2x; solte para voltar à normal. **Toque único** em qualquer lugar para alternar os controles de reprodução (mostrar ou ocultar).
{{% /details %}}

{{% details title="Posso alterar o intervalo de salto do duplo toque?" closed="true" %}}
Sim. Vá para **Configurações → Reprodução → Intervalo de salto por gesto** e escolha um valor entre 5 e 60 segundos. A maioria dos usuários mantém em 10 ou 15 segundos.
{{% /details %}}

{{% details title="O que é o Wi-Fi Drive no Evervideo?" closed="true" %}}
O Wi-Fi Drive é o recurso integrado de transferência sem fio de arquivos do Evervideo. Permite enviar vídeos do seu computador para seu iPhone ou iPad pela rede Wi-Fi local — sem iTunes, sem cabos, sem conta na nuvem. Você pode usar qualquer navegador desktop ou um cliente WebDAV como o Finder do Mac ou o Explorador de Arquivos do Windows. Veja o [guia completo do Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="O Evervideo reproduz MKV, AVI e outros formatos do Plex ou Jellyfin?" closed="true" %}}
Sim. O Evervideo reproduz praticamente qualquer formato de vídeo — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — e os transmite diretamente do Plex, Jellyfin, Emby e outros servidores de mídia sem exigir transcodificação para a maioria dos codecs. Isso significa menor carga de CPU no seu servidor e tempos de início mais rápidos.
{{% /details %}}

{{% details title="A atualização do Evervideo 1.7 é gratuita?" closed="true" %}}
Sim. O Evervideo é um download gratuito na App Store, e a 1.7 é uma atualização gratuita para todos os usuários existentes. As novas integrações de nuvem, suporte a servidor de mídia, gestos de reprodução, melhorias do Wi-Fi Drive e UI Liquid Glass fazem parte da atualização base.
{{% /details %}}

{{% details title="Em quais dispositivos o Evervideo 1.7 está disponível?" closed="true" %}}
O Evervideo 1.7 funciona em iPhone, iPad e Mac. AirPlay e Chromecast permitem transmitir a reprodução para uma tela maior. A sincronização do iCloud Drive mantém sua biblioteca e configurações consistentes entre dispositivos.
{{% /details %}}
