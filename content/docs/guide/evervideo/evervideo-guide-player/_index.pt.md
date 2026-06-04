---
title: "Leitor de Multimédia"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aprenda a usar o leitor de multimédia Evervideo no iPhone, iPad e Mac. Imagem-em-imagem, descodificação H.264 / HEVC acelerada por hardware, equalizadores de áudio e vídeo, legendas primárias e secundárias, seleção de faixas de áudio e vídeo, escala e rotação de vídeo, velocidade de reprodução, temporizador de suspensão, AirPlay 2, Google Chromecast, fluxos RTSP e o leitor compacto sempre no ecrã."
keywords: [
  "guia do leitor Evervideo", "configurações do leitor de vídeo", "equalizador Evervideo",
  "imagem-em-imagem iPhone", "vídeo PiP iPad", "vídeo PiP Mac",
  "vídeo AirPlay 2", "vídeo Google Chromecast",
  "legenda de vídeo iPhone", "legendas SRT externas",
  "leitor de legendas ASS SSA", "libass iOS",
  "legendas duplas aprendizagem de idiomas",
  "equalizador de vídeo brilho contraste", "equalizador de áudio leitor de vídeo",
  "bloqueio de rotação do leitor", "modo de escala de vídeo iOS",
  "descodificador H.264 hardware iPhone", "descodificador HEVC hardware iPad",
  "velocidade de reprodução de vídeo", "leitor de vídeo FFmpeg iOS",
  "leitor RTSP iPhone", "leitor de vídeo compacto",
  "leitor de vídeo VR 360 iPhone"
]
tags: ["guia", "evervideo", "leitor", "PiP", "legendas", "equalizador de vídeo"]
readingTime: 14
---


O Leitor de Multimédia é o ecrã principal da aplicação onde controla a reprodução e a maioria das funcionalidades do Evervideo. Reproduz tanto ficheiros de vídeo como de áudio e é construído com um leitor personalizado baseado em FFmpeg com descodificação H.264 e HEVC acelerada por hardware que faz o trabalho pesado. Vamos explorar como usá-lo.

## Aceder ao Leitor de Multimédia

Pode chegar ao leitor de ecrã inteiro a partir da barra do leitor compacto. No iPhone, o leitor compacto fica no topo do ecrã principal. No iPad e Mac, fica no lado esquerdo (ou no topo do painel principal). Para recolher o leitor de ecrã inteiro de volta à vista compacta, toque no botão fechar no canto inferior direito ou deslize para baixo. Para ocultar completamente o leitor compacto, toque e deslize para baixo mais uma vez.

O leitor compacto permanece visível enquanto navega na biblioteca, no gestor de ficheiros ou nas configurações, para que nunca perca o vídeo enquanto procura o próximo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Leitor de Multimédia em Ecrã Inteiro do Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Formatos de Vídeo e Áudio Suportados

O Evervideo reproduz praticamente qualquer container e codec moderno através do motor FFmpeg incluído, com descodificação H.264 e HEVC acelerada por hardware em dispositivos suportados.

- **Containers de vídeo:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — e muitos mais.
- **Codecs de vídeo:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — mais praticamente qualquer outro codec que o FFmpeg suporte.
- **Codecs de áudio:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — e muitos mais.
- **Formatos de legendas:** SRT, VTT (WebVTT), ASS / SSA e faixas de legendas em texto ou imagem incorporadas.
- **Protocolos de streaming:** HTTP / HTTPS, HLS (m3u8), RTSP (câmeras IP e IPTV) e streaming direto de ficheiros por SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Isso cobre praticamente qualquer ficheiro de vídeo que seja provável encontrar — incluindo rips MKV, fluxos RTSP de câmeras de segurança e descarregamentos webm AV1.

## Controlos de Reprodução

Na parte inferior do ecrã do leitor, verá botões para Reproduzir, Pausar, Seguinte e Anterior. Há também botões opcionais como Avançar Rápido e Retroceder Rápido (10 segundos por predefinição) que pode ativar nas configurações da aplicação. Mantenha os botões Seguinte / Anterior premidos para avançar ou retroceder rapidamente. Arraste o cursor de reprodução para saltar para qualquer posição.

## Repetir e Ordem Aleatória

Toque no botão de repetição para percorrer os modos de repetição:

- **Repetir Tudo** — repete todos os vídeos na fila.
- **Repetir Um** — repete apenas o vídeo atual.
- **Parar ao Terminar** — pausa quando o vídeo atual termina.
- **Sem Repetição** — reproduz a fila uma vez sem repetir.

Use o botão **Ordem Aleatória** para aleatorizar a ordem dos vídeos na fila.

## Imagem-em-imagem (PiP)

No iPhone e iPad, o Evervideo suporta completamente a Imagem-em-imagem (PiP). Toque no ícone PiP no ecrã do leitor ou simplesmente mande o Evervideo para segundo plano — o vídeo continua a ser reproduzido numa janela flutuante acima de todas as outras aplicações. Arraste a janela flutuante para qualquer canto; aperte para redimensionar; toque uma vez para aparecerem os controlos básicos de reprodução / pausa / avançar; toque no pequeno botão de expandir para voltar ao Evervideo completo.

O PiP funciona com todos os formatos de vídeo que o Evervideo reproduz, incluindo ficheiros transmitidos na nuvem e fluxos RTSP. O PiP também continua a funcionar quando o telefone está bloqueado (dependendo da configuração de Bloqueio Automático).

## Leitor Compacto

O leitor compacto é um mini-leitor persistente que permanece visível no topo de cada ecrã na aplicação enquanto navega na biblioteca, no gestor de ficheiros ou nas configurações. Toque nele para expandir para o leitor de ecrã inteiro; deslize para baixo para recolhê-lo novamente.

{{< cards cols="1">}}
  {{< card title="" subtitle="Configurações de Vídeo a partir do Leitor Compacto no Ecrã Principal do Evervideo" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Para AirPlay, toque no botão AirPlay no leitor. O Evervideo suporta AirPlay 2, para que possa transmitir vídeo para Apple TV, HomePod ou qualquer altifalante ou smart TV compatível com AirPlay 2. Numa configuração com múltiplos dispositivos AirPlay, pode encaminhar o áudio para múltiplos recetores simultaneamente.

## Google Chromecast

Para utilizadores do Google Cast, o ícone Cast aparece no leitor. Toque nele para escolher um dispositivo e começar a transmitir. Certifique-se de que o telefone e o recetor Cast estão na mesma rede Wi-Fi. Nem todos os codecs são suportados pelo hardware do Chromecast — alguns ficheiros podem necessitar de transcodificação.

## Fluxos RTSP ao Vivo

O Evervideo pode reproduzir fontes RTSP diretamente — câmeras IP, câmeras de campainha, fluxos IPTV, sinais de transmissão e qualquer URL `rtsp://`. Adicione o fluxo como uma ligação RTSP em Ficheiros → Ligações Online → Adicionar link, depois toque para começar a ver. Os fluxos RTSP funcionam na Imagem-em-imagem, no leitor compacto e transmitem por AirPlay 2 e Chromecast tal como um vídeo normal.

## Seleção de Faixa de Áudio

Para vídeos com múltiplas faixas de áudio (comentário, dobragens em idiomas alternativos, faixas do realizador), toque no botão Mais Ações no leitor e escolha Faixa de Áudio — depois selecione a faixa que pretende. Isto é essencial para filmes em língua estrangeira, ficheiros BDMV / MKV com múltiplas dobragens e conteúdo instrucional com faixas de comentários.

## Seleção de Faixa de Vídeo

Alguns ficheiros de vídeo incluem múltiplos fluxos de vídeo (Blu-rays multi-ângulo, cortes alternativos). Escolha Faixa de Vídeo no menu Mais Ações para alternar entre eles durante a reprodução.

## Legendas — Internas e Externas

O Evervideo dá-lhe controlo preciso sobre as legendas:

- **Faixa de legendas** — escolha entre as faixas incorporadas no ficheiro.
- **Ficheiros de legendas externos** — carregue ficheiros `.srt`, `.vtt`, `.ass` ou `.ssa` do seu dispositivo, iCloud Drive ou qualquer serviço em nuvem ligado.
- **Renderização Libass** — a estilização avançada ASS / SSA (tipos de letra, cores, posições, efeitos de karaoke) é renderizada corretamente graças à biblioteca libass incluída.
- **Seleção de tipo de letra** — escolha um tipo de letra personalizado para as legendas primárias e um tipo de letra separado para as legendas secundárias. Os tipos de letra incluídos e qualquer tipo de letra instalado no dispositivo estão disponíveis.

Pode configurar tudo isto em Configurações → Legendas antes da reprodução, ou usar Mais Ações → Legendas no leitor para alterar durante a reprodução.

## Equalizador de Áudio

O Evervideo inclui um equalizador de áudio completo para ajustar as bandas sonoras de vídeo para os seus auscultadores, altifalantes ou sistema de alta-fidelidade. Toque no ícone do equalizador na vista de volume (ou na ação Equalizador de Áudio no menu Mais Ações do leitor), ative o equalizador com o interruptor no canto superior direito, e escolha um preset ou arraste os cursores de banda para criar o seu próprio. Os presets personalizados podem ser exportados e importados para partilhar entre dispositivos ou fazer cópias de segurança.

## Equalizador de Vídeo

Para ajustar a imagem, o Evervideo fornece um equalizador de vídeo dedicado — ajuste o brilho, contraste, saturação e matiz em tempo real durante a reprodução. Tal como o equalizador de áudio, os presets de vídeo personalizados podem ser exportados e importados para partilha ou cópia de segurança. Use-o para iluminar uma cena escura num dia ensolarado, aumentar a saturação em conteúdo desbotado ou aquecer uma tonalidade de cor fria.

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalizador de Vídeo do Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Modo de Escala de Vídeo

Escolha como o vídeo preenche o ecrã:

- **Ajustar** — preservar a proporção original; barras pretas onde necessário.
- **Preencher** — preencher o ecrã inteiro, cortando o vídeo se necessário.
- **Esticar** — esticar o vídeo para preencher o ecrã, distorcendo se necessário.
- **Original** — manter a resolução nativa em 1:1.

## Rotação de Vídeo

Para vídeos gravados com a orientação errada, escolha **Mais Ações → Rotação** e selecione **0°**, **90°**, **180°** ou **270°** para rodar a imagem sem sair do leitor.

## Descodificação por Hardware (H.264 e HEVC)

Em Configurações → Leitor → Vídeo, pode ativar / desativar Descodificação Hardware H.264 e Descodificação Hardware H.265 (HEVC) de forma independente. A descodificação por hardware é mais rápida, usa menos bateria e funciona mais frio — mas em casos raros (ficheiros corrompidos, perfis exóticos) pode precisar de desativar a descodificação por hardware e recorrer à descodificação por software FFmpeg. O Evervideo permite fazer isso ficheiro a ficheiro no menu Mais Ações do leitor.

## Viewport VR 360°

O Evervideo inclui um viewport VR / 360° para ficheiros de vídeo esféricos. Ao reproduzir um vídeo 360°, pode arrastar para olhar à volta, apertar para aproximar e o Evervideo irá deformar a renderização em tempo real.

## Velocidade de Reprodução

Toque no controlo Velocidade na barra de ferramentas do leitor para alterar a velocidade de reprodução — abrande para análise (0,25× ou 0,5×) ou acelere para tutoriais e aulas (1,25×, 1,5×, 2× e até 3×). Toque no ícone de configuração no canto superior direito do ecrã de Velocidade para mudar para o modo preciso com ajustes mais finos. A correção de tom por faixa também está disponível.

{{< cards cols="1">}}
  {{< card title="" subtitle="Velocidade de Reprodução na Barra de Ferramentas Principal do Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Fila do Leitor

Para ver a fila do leitor, toque no botão da fila no leitor. Cada vídeo na fila tem mais ações — toque nos três pontos para as ver. Para reordenar um vídeo na fila, use o indicador de reordenação perto do título e arraste-o para uma nova posição.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fila de Reprodução do Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Temporizador de Suspensão

Abra Configurações → Leitor → Temporizador de Suspensão, ative-o e escolha quanto tempo quer que a reprodução continue antes de parar automaticamente. Também pode adicionar o botão Temporizador de Suspensão diretamente ao ecrã principal do leitor através de Configurações → Leitor → Personalização → Ações do Ecrã Principal.

## Marcadores do Leitor

Guarde o seu lugar em vídeos longos — aulas, audiolivros em vídeo, tutoriais, descarregamentos longos do YouTube — tocando em Adicionar Marcador no menu Mais Ações. Os marcadores aparecem na lista Mais Ações → Marcadores do vídeo e persistem entre sessões.

## Menu Mais Ações

Toque no botão **Mais Ações "..."** no leitor para aceder a funções adicionais.

- **Continuar Reprodução** — retomar a fila a partir da última posição.
- **Pesquisa** — encontrar um vídeo específico na fila.
- **Marcadores** — ver e saltar para marcadores.
- **Velocidade** — ajustar a velocidade de reprodução.
- **Recentes** — vídeos reproduzidos recentemente.
- **Favoritos** — vídeos marcados como favoritos.
- **Equalizador de Áudio** — ativar o equalizador de áudio.
- **Equalizador de Vídeo** — ativar o equalizador de vídeo.
- **Faixa de Áudio** — escolher o fluxo de áudio.
- **Faixa de Vídeo** — escolher o fluxo de vídeo.
- **Legendas** — faixa primária / secundária, ficheiro externo, tipo de letra.
- **Rotação** — rodar a imagem 0° / 90° / 180° / 270°.
- **Modo de Escala** — Ajustar / Preencher / Esticar / Original.
- **Imagem-em-imagem** — entrar no modo PiP.
- **AirPlay** / **Chromecast** — enviar para um dispositivo.
- **Temporizador de Suspensão** — definir um temporizador para parar a reprodução.
- **Guardar Fila como Lista de Reprodução** — guardar a fila atual como uma nova lista de reprodução.
- **Eliminar Fila** — limpar a fila e parar a reprodução.
- **Configurações** — ir diretamente para as configurações do leitor.
- **Ajuda** — abrir orientação.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecrã Mais Ações do Leitor Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Configurações do Leitor

A árvore completa de configurações do Leitor está documentada no [guia de Configurações](/docs/guide/evervideo/evervideo-guide-settings/). As secções mais utilizadas:

- **Geral** — modo de repetição, modo de ordem aleatória, Guardar Estado do Leitor, Guardar Posição de Reprodução, intervalos de avanço rápido.
- **Vídeo** — descodificação hardware H.264 / HEVC, equalizador de vídeo, modo de escala, rotação, modo de visualização, FPS preferido, formato de pixel preferido, viewport VR.
- **Áudio** — equalizador de áudio, taxa de amostragem, canais, duração do buffer IO, modo misto.
- **Legendas** — faixa primária / secundária, seleção de ficheiro externo, tipo de letra, tipo de letra secundário.
- **Dispositivos** (iOS) — AirPlay / Chromecast.
- **Personalização** — estilo de layout do leitor (Mínimo / Inferior / Antigo / Clássico), ações do ecrã principal, controlos do ecrã de bloqueio.
- **Cache de Reprodução** — cache em disco para streaming mais suave.
- **Temporizador de Suspensão** — paragem automática.

## Acessibilidade

O Evervideo é totalmente acessível com VoiceOver. Cada componente tem uma etiqueta e descrição bem concebidas. Quando o VoiceOver está ativo, a aplicação muda para Modo de Texto para que apenas elementos significativos sejam apresentados — melhorando a velocidade de navegação e a clareza. Também pode ativar o Modo de Texto em Configurações → Acessibilidade → Modo de Texto.

### Ajustar Controlos Deslizantes com VoiceOver

1. **Selecione o controlo deslizante** — deslize para a esquerda ou para a direita até o VoiceOver o anunciar.
2. **Ajuste o valor** — toque duas vezes e mantenha o controlo deslizante, depois arraste para cima ou para baixo para alterar o valor rapidamente. O VoiceOver anuncia o novo valor à medida que avança.

Os outros componentes funcionam como esperado, usando os padrões VoiceOver fornecidos pelo sistema.
