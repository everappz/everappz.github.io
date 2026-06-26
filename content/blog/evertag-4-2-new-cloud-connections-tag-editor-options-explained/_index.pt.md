---
title: "Evertag 4.2: novas conexões na nuvem e opções do editor de tags"
date: 2026-05-09
description: "O Evertag 4.2 acrescenta ligações a Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP e NFS, renova o Wi-Fi Drive e atualiza a interface para o Liquid Glass. Este artigo explica também todas as definições do editor de tags — incluindo ID3v2.4 vs ID3v2.3, escala da capa, tags duplicadas, modos de envio para a nuvem e as opções certas para o Spotify e outros serviços de streaming."
keywords: ["Evertag 4.2", "atualização Evertag", "editor de tags ID3 iPhone", "ID3v2.4 vs ID3v2.3", "editar tags FLAC iOS", "editar tags MP3 iPhone", "editar capa do álbum iOS", "editor de tags para Spotify", "editor de tags Plex", "editor de tags Apple Music", "editor de tags na nuvem Evertag", "editor de tags Internxt", "editor de tags Proton Drive", "editor de tags QNAP", "editor de tags Nextcloud", "editor de tags Amazon S3", "editor de tags SFTP iPhone", "editor de tags FTP áudio", "editor de tags NFS iPhone", "Wi-Fi Drive editor de tags", "tags ID3 duplicadas", "escala da capa", "design Liquid Glass", "editor de metadados de áudio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor de tags", "ID3", "ID3v2.4", "ID3v2.3", "Tags FLAC", "Tags MP3", "Capa de álbum", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Novidades"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**Resumo:** O [Evertag 4.2](/products/evertag) é uma atualização importante do editor de tags de áudio para iPhone, iPad e Mac. Eliminámos bugs-chave de edição de tags e adicionámos mais de 6 novas ligações à nuvem e a servidores — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, além dos protocolos **FTP**, **SFTP** e **NFS**. O Wi-Fi Drive ganhou uma interface renovada, modo de seleção múltipla, fila de envio mais inteligente e transferências mais rápidas. Toda a app está afinada para o design **Liquid Glass**. Este artigo aprofunda também as definições do editor de tags do Evertag — explicando **ID3v2.4 vs ID3v2.3**, **escala da capa**, **tags duplicadas**, **modos de envio para a nuvem**, **eliminação do ficheiro descarregado** e exatamente que opções escolher se estás a preparar áudio para **Spotify**, **Apple Music**, **Plex**, **Jellyfin** ou qualquer outro serviço de streaming.

---

## Olá a todos!

Chegou uma grande atualização do Evertag. Eliminámos bugs-chave de edição de tags e acrescentámos **mais de 6 novas ligações à nuvem e a servidores** para tornar a gestão dos metadados de áudio mais simples do que nunca — quer a tua biblioteca viva numa nuvem focada em privacidade, num NAS auto-alojado ou num servidor genérico FTP/SFTP/NFS.

[Descarrega o Evertag 4.2 da App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) ou atualiza a partir da tua versão atual.

## Suporte alargado a nuvem e servidores

O Evertag liga-se agora nativamente a uma gama mais ampla de opções de nuvem e armazenamento auto-alojado. Podes editar tags ID3, MP4, FLAC, OGG e APE em ficheiros que vivam em qualquer lado.

### Armazenamento na nuvem focado em privacidade: Internxt e Proton Drive

Se te preocupas com a encriptação ponto-a-ponto e o armazenamento de conhecimento zero, duas das nuvens mais respeitadas com foco em privacidade são agora nativas no Evertag:

- **Internxt** — nuvem espanhola open-source, com encriptação pós-quântica e em conformidade com o RGPD. Plano gratuito disponível.
- **Proton Drive** — armazenamento com encriptação ponto-a-ponto dos criadores do Proton Mail e do Proton VPN, com sede na Suíça. Plano gratuito disponível, com planos pagos para bibliotecas maiores.

Podes agora editar metadados diretamente em ficheiros de áudio guardados em qualquer um dos serviços — o ficheiro permanece encriptado em trânsito e apenas as novas tags são reescritas.

### Soluções auto-alojadas: QNAP, Nextcloud, Amazon S3

Para utilizadores que gerem a própria infraestrutura:

- **QNAP** — ligação API nativa a dispositivos QNAP NAS. Edita tags em ficheiros guardados no teu QNAP por Wi-Fi local ou acesso remoto.
- **Nextcloud** — liga a qualquer instância Nextcloud auto-alojada ou gerida.
- **Amazon S3** — aponta o Evertag para qualquer bucket S3 (ou armazenamento compatível com S3 como Backblaze B2, Wasabi, MinIO, Cloudflare R2) e edita os metadados no local.

### Novos protocolos de rede: FTP, SFTP, NFS

O Evertag 4.2 acrescenta três protocolos clássicos para utilizadores com servidores próprios, homelabs ou NAS genéricos:

- **SFTP (SSH File Transfer Protocol)** — a resposta certa para **edição remota e segura de tags no teu próprio servidor**. O SFTP corre sobre SSH, por isso toda a transferência (autenticação e dados de áudio) é encriptada. Se tens um VPS, servidor dedicado ou uma máquina Linux em casa com acesso SSH, podes editar tags em ficheiros remotos sem expor mais nada. Suporta autenticação por palavra-passe e por chave.
- **FTP** — o padrão histórico para transferência de ficheiros. Útil para NAS domésticos mais antigos que expõem FTP mas não têm uma API nativa.
- **NFS (Network File System)** — o protocolo de partilha de facto em Linux e na maioria dos NAS. Menor sobrecarga do que SMB no mesmo hardware.

> **Dica:** o SFTP é o protocolo a escolher para edição remota pela Internet aberta. O FTP e o NFS funcionam melhor na rede local — não os exponhas à Internet a menos que os encapsules numa VPN.

## Melhorias do Wi-Fi Drive

O [**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) é a funcionalidade integrada no Evertag para transferir ficheiros de áudio sem fios entre o computador e o iPhone ou iPad — sem iTunes, sem cabos, sem conta na nuvem. Ambos os dispositivos têm de estar na mesma rede Wi-Fi.

No Evertag 4.2, o Wi-Fi Drive recebe:

- **Interface renovada e moderna** — mais limpa, mais fácil de ler num relance e atualizada para o Liquid Glass.
- **Modo de seleção múltipla** — escolhe vários ficheiros ou pastas e atua sobre eles em lote.
- **Fila de envio mais inteligente** — feedback de progresso mais claro e maior resistência a quebras de rede.
- **Velocidade e fiabilidade globais melhoradas** — transferências mais rápidas para bibliotecas grandes.

É a forma mais rápida de mover um lote de ficheiros de áudio do computador para o telemóvel, editar as tags e devolvê-los — sem qualquer serviço de terceiros.

## Definições do editor de tags: análise aprofundada

Esta é a parte que a maioria dos utilizadores nunca lê — e a parte que decide se as tuas tags funcionam em todo o lado ou só em algumas apps. Abre o Evertag e entra na secção **definições do editor de tags de áudio**. Aqui está o que cada opção realmente faz e qual escolher consoante o que queres alcançar.

### Escala da capa

Quando guardas a capa do álbum dentro de um ficheiro de áudio, o Evertag pode redimensionar a imagem antes de a embeber. As opções disponíveis são:

- **Pequeno** — menor impacto no tamanho do ficheiro, qualidade de imagem mais baixa.
- **Médio** — escolha equilibrada para a maioria dos utilizadores.
- **Grande** — alta qualidade, adequada a leitores com ecrãs grandes e ao CarPlay.
- **Extra grande** — qualidade muito alta, aumento notório do tamanho do ficheiro.
- **Original (Desativado)** — embebe a capa na resolução original. **Sem qualquer redimensionamento.**

**Porque é que isto importa:**

- **Mais qualidade = ficheiro maior.** Uma capa de 3.000 × 3.000 píxeis pode acrescentar vários MB a cada faixa. Multiplicado por um álbum inteiro, o custo em disco soma-se rapidamente.
- **Alguns leitores não lidam bem com imagens embebidas muito grandes.** Aparelhos antigos, alguns sistemas de auto e certos leitores desktop legados podem encravar com capas acima de ~1.500 px ou recusar-se a mostrá-las.
- **Para a maioria dos fluxos de nuvem e streaming**, **Médio** ou **Grande** é o ponto certo. Usa **Original** apenas quando precisas de qualidade de arquivo ou estás a preparar ficheiros para um leitor em que confias.

> A opção **Original** faz parte da atualização de personalização premium do Evertag. Os tamanhos padrão (Pequeno/Médio/Grande/Extra grande) são gratuitos.

### Opções de gravação de tags: ID3v2.4 vs ID3v2.3

É a definição mais importante para a compatibilidade. ID3v2 é o formato de metadados usado dentro dos ficheiros MP3. Existem duas versões muito utilizadas, e diferem em pormenores subtis mas importantes.

#### ID3v2.4

- Mais recente, suporta a **codificação de texto UTF-8** — manipulação correta de escritas não latinas (chinês, russo, japonês, árabe, hebraico, etc.).
- Mais tipos de frame (volume relativo, presets de equalizador, etc.).
- **Recomendado para leitores modernos** que o suportem.

#### ID3v2.3

- Mais antigo mas **a versão de ID3 com maior compatibilidade universal**.
- Não suporta UTF-8 diretamente (usa UTF-16 para texto Unicode).
- **Recomendado quando precisas da máxima compatibilidade** com leitores antigos, sistemas de auto e algumas apps de desktop.

#### Quando ativar o ID3v2.4 no Evertag

- Usas **leitores de áudio modernos** como Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versões atuais) ou leitores Android modernos. ✅ **Liga o ID3v2.4.**
- A tua biblioteca contém **caracteres não latinos** (chinês, coreano, japonês, russo, árabe, grego, hebraico). ✅ **Liga o ID3v2.4** — o UTF-8 trata-os de forma muito mais limpa.

#### Quando desativar o ID3v2.4 no Evertag (usar ID3v2.3)

- Estás a preparar ficheiros para um **rádio de auto ou unidade central mais antigos** que não leem tags v2.4.
- Vês **texto ilegível ou tags em falta** em algumas apps após a edição — é um sinal claro de que aí não há suporte para v2.4. Volta para v2.3.
- Apontas a **leitores desktop legados** ou leitores portáteis antigos (primeiros iPods, certos leitores MP3 dos anos 2000–2010).

> **Regra prática:** se as tuas tags aparecem corretamente em todo o lado com v2.4, deixa ligado. Se mesmo um leitor importante mostra caracteres errados, em branco ou não lê as tags, desativa v2.4 e volta a guardar.

#### Tags duplicadas

Quando ativas **Tags duplicadas**, o Evertag escreve campos de metadados comuns (título, artista, álbum, etc.) em **ambas as secções ID3v1 e ID3v2** do ficheiro. Melhora a compatibilidade com leitores muito antigos que só leem ID3v1 (a tag original de 128 bytes no fim do ficheiro).

- **A maioria dos utilizadores não precisa.** Os leitores modernos leem primeiro o ID3v2.
- **Ativa apenas se** lidas com hardware vintage ou software específico que ignora o ID3v2.

### Atualizar ficheiros online: como o Evertag gere edições na nuvem

Quando editas tags num ficheiro guardado numa nuvem ligada (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, etc.), o Evertag tem de voltar a enviar o ficheiro modificado. Tu controlas como:

- **Mostrar mensagem de confirmação** *(predefinição, recomendado)* — o Evertag pergunta antes de enviar. Melhor para utilizadores cautelosos e bibliotecas partilhadas.
- **Atualizar automaticamente os metadados do ficheiro** — envia em silêncio depois de cada edição. Melhor para utilizadores solo com ligações rápidas e fiáveis que editam muito.
- **Não atualizar os metadados do ficheiro** — o Evertag edita apenas a cópia local. Útil para pré-visualizar alterações sem enviar para a nuvem.

### Editar ficheiros online: limpeza do ficheiro local

Para editar um ficheiro remoto, o Evertag descarrega-o primeiro para o dispositivo. Depois da edição, escolhes o que acontece a essa cópia local:

- **Eliminar sempre o ficheiro descarregado** — o Evertag remove o ficheiro temporário após a edição. **Recomendado** se tens pouco armazenamento ou trabalhas em ficheiros de outras pessoas.
- **Não eliminar o ficheiro descarregado** — mantém o ficheiro editado no dispositivo. Útil se queres uma cópia offline e uma cópia atualizada na nuvem.

### Botões no ecrã principal

O ecrã principal do editor de tags do Evertag pode mostrar ou esconder botões para operações individuais. Ativa apenas os que realmente usas para manter a interface focada:

- **Pesquisar tags de áudio automaticamente** — encontra metadados em falta online a partir da impressão de áudio do ficheiro.
- **Pesquisar tags de áudio manualmente** — pesquisa por título/artista quando a pesquisa automática falha.
- **Pesquisar capa do álbum** — encontra e embebe capas de alta qualidade.
- **Guardar capa do álbum** — exporta a capa embebida para a tua biblioteca de fotos ou ficheiros.
- **Normalizar codificação** — corrige texto não latino mal codificado por codificações antigas (muito útil para faixas em cirílico, chinês e japonês ripadas com software legado).
- **Eliminar tags de áudio** — remove todas as tags de um ficheiro. Útil antes de uma reetiquetagem limpa.

### Mostrar tags estendidas

Ativa isto para mostrar o conjunto completo de campos de metadados além do básico título/artista/álbum/ano — incluindo BPM, maestro, artista original, ambiente, copyright, codificador, comentários, letras e mais. Funcionalidade para utilizadores avançados; a maioria dos casuais não precisa.

### Editar ficheiros simultaneamente

Quando ativado, o Evertag permite editar metadados em **vários ficheiros selecionados ao mesmo tempo** — define o mesmo artista do álbum, ano ou género para um álbum inteiro numa única operação. É a forma mais rápida de organizar uma biblioteca grande e desorganizada.

## Editar tags para Spotify, Apple Music e plataformas de streaming

Uma pergunta comum: «editei as minhas tags no Evertag, enviei os ficheiros e o serviço de streaming mostra metadados errados. O que se passa?»

Resposta curta: **os serviços de streaming nem sempre respeitam as tuas tags locais**. O Apple Music e o Spotify têm bases de dados internas próprias — quando reconhecem uma faixa, sobrescrevem os metadados apresentados com os deles. Mas para **ficheiros enviados**, os teus ficheiros locais (a função «Biblioteca» do Apple Music, os Ficheiros locais do Spotify) e os **envios de distribuidor para plataformas de streaming**, as tuas tags importam mesmo. Aqui fica como configurar o Evertag em cada cenário:

### Preparar ficheiros para o Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — o Apple Music lida corretamente com UTF-8.
- **Capa: Grande** — as apps da Apple mostram bem capas grandes; Original é demasiado.
- **Tags duplicadas: OFF** — não são necessárias.
- Garante que **Artista do álbum** está corretamente preenchido — o Apple Music usa-o para agrupar.

### Preparar ficheiros para os Ficheiros locais do Spotify

Os Ficheiros locais do Spotify só mostram ficheiros bem etiquetados. As tags que o Spotify lê são limitadas.

- **ID3v2.4: ON** na maioria dos casos. Se uma faixa não aparecer corretamente no Spotify após a edição, **experimenta guardar com ID3v2.4 OFF** (ou seja, como ID3v2.3) — o parser do Spotify tem sido historicamente conservador com v2.4.
- **Capa: Médio ou Grande** — o Spotify redimensiona-a de qualquer forma.
- Preenche pelo menos **Título**, **Artista**, **Álbum** e **Número da faixa**.

### Preparar ficheiros para envio por distribuidor (DistroKid, TuneCore, CD Baby, etc.)

Se és um artista a enviar trabalho próprio para plataformas de streaming, o teu distribuidor lê normalmente as tags mas também pede metadados na sua interface. De qualquer forma:

- **ID3v2.3** é muitas vezes a opção mais segura — muitas pipelines de distribuidor foram construídas há anos e preferem o formato antigo.
- Embebe capa **Grande** (a maioria dos distribuidores exige ≥ 1.400 × 1.400 px — verifica as suas diretrizes).
- Não dependas de tags estendidas — os distribuidores leem só os campos principais.

### Preparar ficheiros para Plex, Jellyfin, Navidrome, Subsonic, Emby

Estes servidores multimédia auto-alojados são muito tolerantes. Leem v2.3 e v2.4 sem problemas e lidam bem com UTF-8.

- **ID3v2.4: ON** está bem.
- **Capa: Grande** ou **Extra grande** — estes servidores servem capa a clientes móveis e ecrãs CarPlay, por isso a qualidade conta.
- **Artista do álbum** fortemente recomendado — é o que o Plex/Jellyfin usam para agrupar álbuns por artista corretamente.

### Preparar ficheiros para sistemas de auto e hardware antigo

- **ID3v2.4: OFF** (usa ID3v2.3) — as unidades mais antigas não suportam v2.4, na maioria dos casos.
- **Capa: Médio** — muitos ecrãs de auto encravam com capas grandes embebidas.
- **Tags duplicadas: ON** — alguns sistemas de auto antigos só leem o fallback ID3v1.

## Outras melhorias

### Design Liquid Glass

A interface do Evertag 4.2 está afinada ao novo material **Liquid Glass** da Apple em toda a app — superfícies translúcidas, animações mais suaves e controlos refinados que se integram naturalmente em iOS, iPadOS e macOS.

### Bibliotecas de ligação atualizadas

Atualizámos as bibliotecas internas que o Evertag usa para falar com **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** e outros serviços. Resultado: menos falhas de ligação em casos limite, melhor compatibilidade com versões mais recentes de servidor e maior fiabilidade na edição de tags em ficheiros remotos.

### Correções de tradução e localização

Várias correções de idioma na interface a partir do feedback direto dos utilizadores. Melhor encaixe do texto em botões mais pequenos em várias línguas.

### Pequenas melhorias inspiradas no vosso feedback

Muitas pequenas melhorias com base nas avaliações da App Store e nos e-mails para support@everappz.com. Lemos cada mensagem.

## Obtém o Evertag 4.2

[**Descarrega o Evertag na App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) ou atualiza pela App Store. O Evertag é um download gratuito com upgrades opcionais dentro da app para funcionalidades avançadas. As novas ligações na nuvem, os protocolos de rede, as melhorias do Wi-Fi Drive e a UI Liquid Glass fazem parte da atualização base.

Se gostas da app, deixa uma avaliação na App Store — ajuda imenso. Tens feedback ou um problema? Escreve-nos para **support@everappz.com**. Lemos todas as mensagens.

## Perguntas frequentes

{{% details title="O que há de novo no Evertag 4.2?" closed="true" %}}
O Evertag 4.2 acrescenta mais de 6 novas ligações à nuvem e a servidores (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), um Wi-Fi Drive renovado com seleção múltipla e fila de envio mais inteligente, atualizações de UI Liquid Glass, bibliotecas de ligação atualizadas, correções-chave de edição de tags e melhorias de tradução.
{{% /details %}}

{{% details title="Devo usar ID3v2.4 ou ID3v2.3 no Evertag?" closed="true" %}}
Usa **ID3v2.4** para leitores modernos (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, apps Android modernas) e para bibliotecas com caracteres não latinos — o suporte a UTF-8 dá tags mais limpas em chinês, coreano, japonês, russo, árabe e hebraico. Usa **ID3v2.3** se as tuas tags aparecem incorretamente em algumas apps, se apontas a sistemas de auto antigos ou se uma pipeline de distribuidor de streaming rejeita v2.4. Podes sempre alternar e voltar a guardar.
{{% /details %}}

{{% details title="Porque é que as minhas tags ficam erradas no Spotify depois de editar?" closed="true" %}}
O Spotify mostra sobretudo metadados do seu próprio catálogo — as tuas tags locais só são usadas para «Ficheiros locais» ou para conteúdo que enviaste como artista. Se estás a etiquetar ficheiros para Ficheiros locais do Spotify e não aparecem corretamente, experimenta desativar o ID3v2.4 no Evertag e guardar como ID3v2.3 — o parser do Spotify tem sido historicamente conservador com v2.4.
{{% /details %}}

{{% details title="Que tamanho de capa devo escolher no Evertag?" closed="true" %}}
Para a maioria dos utilizadores: **Grande**. Fica ótimo em telemóveis, iPads, Macs e ecrãs de auto modernos sem inflar demasiado os ficheiros. Usa **Médio** se tens uma biblioteca enorme e queres poupar disco. Usa **Original** (sem redimensionamento) só para masters de arquivo ou quando precisas mesmo de qualidade máxima — mas atenção, alguns leitores antigos têm dificuldade com capas embebidas muito grandes. **Original** faz parte da atualização de personalização premium do Evertag.
{{% /details %}}

{{% details title="Capas maiores tornam os meus ficheiros maiores?" closed="true" %}}
Sim. Embeber uma capa de 3.000 × 3.000 px pode acrescentar vários megabytes a um único ficheiro de áudio. Numa biblioteca de 1.000 faixas, dá gigabytes. Se estás apertado de armazenamento, usa Médio ou Grande; se transmites a partir de um NAS onde o tamanho não importa, Extra grande ou Original servem.
{{% /details %}}

{{% details title="O que são Tags duplicadas e devo ativá-las?" closed="true" %}}
As Tags duplicadas escrevem os metadados centrais nas secções ID3v1 (legacy 128 bytes) e ID3v2 (moderna) do ficheiro. Ativa-as só se apontas a leitores muito antigos ou hardware que lê ID3v1. Para tudo o que é moderno (smartphones, computadores, sistemas de auto recentes), deixa desativado.
{{% /details %}}

{{% details title="O Evertag edita tags diretamente em ficheiros na nuvem?" closed="true" %}}
Sim. Liga-te à tua nuvem (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, etc.) ou via FTP/SFTP/NFS, abre um ficheiro e edita tags como se fosse local. O Evertag descarrega o ficheiro, aplica as alterações e volta a enviar a versão atualizada. Podes escolher entre os modos «Perguntar sempre», «Auto-envio» ou «Não enviar» nas definições.
{{% /details %}}

{{% details title="Posso editar tags FLAC no iPhone com o Evertag?" closed="true" %}}
Sim. O Evertag suporta FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE e outros formatos importantes com pleno suporte de leitura/escrita de tags, incluindo capa embebida.
{{% /details %}}

{{% details title="Como edito tags em segurança no meu servidor doméstico com SFTP?" closed="true" %}}
Abre o Evertag, vai a Ligações, escolhe SFTP e introduz o nome do anfitrião ou IP do servidor, a porta (normalmente 22), o nome de utilizador e uma palavra-passe ou uma chave SSH privada. O Evertag percorre as tuas pastas remotas e edita tags diretamente com encriptação ponto-a-ponto sobre SSH.
{{% /details %}}

{{% details title="Posso editar tags em vários ficheiros ao mesmo tempo?" closed="true" %}}
Sim. Ativa **Editar ficheiros simultaneamente** nas definições. Seleciona vários ficheiros, abre o editor de tags e qualquer campo que alteres aplica-se a todos os ficheiros selecionados. É a forma mais rápida de definir o mesmo artista do álbum, ano ou género num álbum inteiro.
{{% /details %}}

{{% details title="A atualização para o Evertag 4.2 é gratuita?" closed="true" %}}
Sim. O Evertag é um download gratuito da App Store, e a 4.2 é uma atualização gratuita para todos os utilizadores existentes. As novas integrações na nuvem, as melhorias do Wi-Fi Drive e a UI Liquid Glass fazem parte da atualização base.
{{% /details %}}

{{% details title="Em que dispositivos está disponível o Evertag 4.2?" closed="true" %}}
O Evertag 4.2 corre em iPhone, iPad e Mac. A sincronização do iCloud Drive mantém as tuas definições do editor de tags consistentes entre dispositivos.
{{% /details %}}
