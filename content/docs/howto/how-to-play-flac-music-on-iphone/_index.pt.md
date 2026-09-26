---
title: "Como reproduzir música FLAC (lossless) no meu iPhone"
date: 2024-01-29
lastmod: 2026-09-26
description: "Como reproduzir FLAC no iPhone e iPad em 2026 com o Flacbox, um reprodutor de alta resolução com mais de 120 formatos, saída até 384 kHz, suporte a DAC USB, um equalizador de 10 bandas, o motor de áudio BASS, efeitos em tempo real como reverberação e delay, um processador DSP e um visualizador de música com 500 predefinições. Faça streaming da nuvem ou do NAS e reproduza offline."
keywords: ["como reproduzir flac no iphone", "reprodutor flac iphone", "flac", "iphone", "lossless", "áudio de alta resolução", "reprodutor dsd ios", "dac usb iphone", "384khz", "música", "flacbox", "streaming", "offline", "equalizador", "dsp", "visualizador de música", "motor bass"]
tags: ["música", "nuvem", "reprodutor", "gestor de transferências", "equalizador", "lossless", "alta resolução", "offline", "FLAC", "DSD", "DAC", "streamer", "visualizador", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**Resumo:** Para reproduzir FLAC num iPhone precisa de um reprodutor de terceiros, porque a aplicação Música da Apple não suporta FLAC. Instale o [Flacbox](/products/flacbox) (é gratuito) e depois transfira os seus ficheiros através do Wi-Fi Drive ou USB, ou ligue o seu armazenamento na nuvem ou NAS. A sua biblioteca FLAC reproduz com qualidade total, até 384 kHz e 32-bit através de um DAC USB. O Flacbox também reproduz mais de 120 formatos, incluindo FLAC, DSD, ALAC, APE, WAV, OGG e OPUS, e acrescenta um equalizador de 10 bandas, o motor de áudio profissional BASS com efeitos em tempo real, um processador DSP e um visualizador de música em ecrã inteiro.

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## Porque é que o meu iPhone não reproduz FLAC nativamente?

A Apple tem o seu próprio formato lossless chamado ALAC (Apple Lossless), e a aplicação Música está construída em torno dele em vez do FLAC. Desde o iOS 11, a aplicação Ficheiros consegue pré-visualizar um único ficheiro FLAC, mas não tem biblioteca de música, nem listas de reprodução, nem fila, nem equalizador, nem streaming da nuvem. É um visualizador de ficheiros, não um reprodutor de música.

Por isso, tem duas opções reais:

1. Reproduzir FLAC com uma aplicação de reprodução, para que os seus ficheiros fiquem exatamente como estão. Esta é a que recomendamos.
2. Converter FLAC para ALAC, que é de lossless para lossless, e depois sincronizar com a aplicação Música.

Se tem uma verdadeira coleção FLAC, a primeira opção é melhor. Evita uma biblioteca duplicada, poupa o tempo de conversão e as suas pastas e a qualidade de alta resolução permanecem intactas. O Flacbox foi feito exatamente para isto.

## Opção 1: Reproduzir FLAC com o Flacbox

O Flacbox é um reprodutor de música de alta resolução para iPhone, iPad e Mac. Transforma o seu armazenamento na nuvem, NAS ou computador na sua própria biblioteca de música privada, sem conversão e sem subscrição.

### Passo 1. Instalar o Flacbox

O Flacbox é gratuito e funciona em iPhone, iPad e Mac.

{{< app-details product="flacbox" >}}

### Passo 2. Coloque os seus ficheiros FLAC na aplicação

Escolha a forma que for mais fácil para si:

- **Wi-Fi Drive** — abra Conexões, depois Computador, depois Conectar via Wi-Fi e arraste os ficheiros a partir de qualquer navegador no computador. Veja o [guia do Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).
- **Armazenamento na nuvem** — ligue o iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive e mais 20, e depois faça streaming diretamente da nuvem.
- **NAS ou computador** — ligue através de SMB, WebDAV, DLNA, FTP, SFTP ou NFS (Synology, QNAP, WD My Cloud, Time Capsule ou qualquer partilha Samba). A lista completa está no [guia de Conexões](/docs/guide/flacbox/flacbox-guide-connections).
- **Pen USB** — ligue uma SanDisk iXpand ou qualquer leitor externo e reproduza [diretamente da unidade](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it), sem importar.
- **Partilha de ficheiros do iTunes ou Finder** — através de um cabo Lightning ou USB-C.

### Passo 3. Prima Reproduzir

As suas faixas aparecem na biblioteca com etiquetas e capas lidas diretamente dos próprios ficheiros, agrupadas por Álbum, Artista, Género e Compositor. Cada faixa mostra o seu codec e resolução exatos, por exemplo FLAC, 96 kHz, 24-bit.

## Saída de alta resolução, DAC USB e multicanal

O Flacbox foi feito para quem se importa com a qualidade do som, e não apenas com uma reprodução casual:

- **Taxa de amostragem** — reproduz de 8 kHz até 384 kHz, com saída multicanal de 1 a 7 canais (até 5.1 e ITU BS.775-1).
- **Suporte a DAC USB** — tudo acima de 48 kHz é reproduzido na sua resolução real através de um DAC USB. Pela própria saída do iPhone, o iOS reamostra o áudio tal como faz para todas as aplicações, por isso um DAC é a forma de obter alta resolução bit-perfect.
- **Saída ajustável** — defina a taxa de amostragem, o número de canais e a duração do buffer de IO (cerca de 5 ms para alta resolução de baixa latência) em Configurações, depois Reprodutor de Áudio.
- **Tom e velocidade** — correção fina de tom, além de velocidade de reprodução de 0.02× a 3.00×.

## Reproduz mais de 120 formatos, não apenas FLAC

Além do FLAC, o Flacbox integra o FFmpeg para poder reproduzir formatos que o iOS não consegue abrir sozinho. Não precisa de converter nem de arrumar primeiro uma biblioteca mista:

- **Lossless e alta resolução** — FLAC, ALAC, WAV, AIFF, APE, WV (WavPack) e DSD (DSF e DFF, incluindo DSD64, DSD128 e DSD256).
- **Com perdas** — MP3, AAC, M4A, OGG, OPUS, WMA, MPC e mais.
- **Música tracker e MOD** — ficheiros clássicos de chiptune e demoscene MOD, XM, IT, S3M, MTM, UMX e MO3 que a maioria dos reprodutores não consegue abrir.

São mais de 120 formatos no total, o que cobre praticamente tudo numa coleção de música moderna.

## Três motores de áudio, incluindo o motor BASS

Pode escolher o motor de reprodução em Configurações, depois Reprodutor de Áudio, depois Codec de Áudio:

- **System Codec + FFmpeg** — máxima compatibilidade e estabilidade.
- **FFmpeg** — força o caminho do FFmpeg, que desbloqueia a correção de tom e uma taxa de amostragem de saída personalizada.
- **Motor BASS™** — o núcleo de reprodução profissional adicionado no [Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer). Desbloqueia os efeitos de áudio em tempo real, o processador DSP, o visualizador de música, a reprodução de tracker e MOD e a reamostragem de alta qualidade. Também acrescenta controlo de tom independente (±60 semitons) e controlo de andamento (0.1× a 4×).

## Equalizador de 10 bandas, reforço de graves e pré-amplificador

O Flacbox inclui um equalizador gráfico de 10 bandas com predefinições ao estilo do iPod, como Acoustic, Bass Booster, Rock, Pop, Jazz, Classical e Dance. Há um pré-amplificador para realçar faixas de baixo volume sem distorção, e pode guardar as suas próprias predefinições. Ajuste-o para auscultadores intra-auriculares, um HomePod ou o sistema de som do carro. Para um passo a passo completo, veja o [guia do equalizador](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalizador do Reprodutor de Áudio Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Efeitos de áudio em tempo real

Quando o motor BASS está ativado, obtém onze efeitos em tempo real que pode empilhar e ajustar enquanto a música toca. Nada é recodificado, e desativar um efeito devolve o som original de imediato:

- **Reverberação** — de uma pequena sala a uma catedral.
- **Delay e eco multi-tap** — de um slapback curto a uma cauda ambiente longa.
- **Crossfeed** — mistura os canais estéreo para que os auscultadores soem mais como colunas reais em misturas com panorâmica acentuada.
- **Compressor** — equilibra as partes altas e baixas, o que é ótimo para o carro ou o ginásio.
- **Chorus, Flanger, Phaser, Auto-Wah, Distortion e Stereo Rotation** — efeitos criativos de modulação e caráter.

O Flacbox também tem nivelamento automático de volume baseado na norma de sonoridade EBU R128 de qualidade profissional. Os álbuns e as listas em modo aleatório tocam a um nível constante, para que não esteja sempre a mexer no volume. Vem com as predefinições Light, Standard, Strong e Night.

## Crie o seu próprio processador DSP

Para além dos efeitos, o Flacbox oferece-lhe um processador DSP de 14 filtros em tempo real que configura você mesmo. Pode adicionar filtros profissionais e bandas de EQ paramétrico, saturação e um bit crusher, e processadores criativos como tremolo, ring modulator e largura estéreo. Tudo funciona ao vivo naquilo que reproduz, desde um FLAC local a um stream da nuvem, e as configurações de DSP estão até disponíveis no CarPlay.

## Visualizador de música em ecrã inteiro

O Flacbox tem um visualizador de música incorporado que desenha visuais coloridos em movimento ao ritmo da sua música. Utiliza o conhecido motor Milkdrop (projectM) com 500 predefinições, desenhado com OpenGL em iPhone, iPad e Mac. Abra-o a partir do reprodutor tocando no botão Mais e depois em Personalização. Escolha uma predefinição ou use o modo Auto para as alternar a cada 30 segundos com um crossfade suave. Para ajuda passo a passo, veja o guia sobre [como ativar o visualizador de música](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Visualizador de Música Flacbox (Milkdrop e projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## Nuvem, NAS e reprodução offline

Faça streaming diretamente de mais de 30 serviços na nuvem, incluindo iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive e Internxt. Também pode ligar servidores auto-hospedados como Plex, Jellyfin, Emby, Subsonic e Navidrome, e qualquer NAS através de SMB, WebDAV, DLNA, FTP, SFTP ou NFS.

Quando quiser ter a sua música consigo, o gestor de transferências incorporado guarda listas de reprodução, artistas, álbuns ou pastas inteiras para ouvir offline. O Modo Offline sincroniza depois automaticamente as novas faixas à medida que aparecem na nuvem. Pouco espaço? Limpe a cache com um toque e continue a fazer streaming.

## Tudo o resto que os ouvintes exigentes querem

- **Biblioteca organizada** — agrupada por Músicas, Álbuns, Artistas de álbum, Artistas, Géneros e Compositores, com pesquisa rápida que funciona offline.
- **Editor de etiquetas ID3** — corrija metadados desorganizados e codificações danificadas (cirílico, japonês, chinês) e grave as alterações de volta no ficheiro.
- **Listas de reprodução** — crie, reordene, importe e exporte M3U, M3U8 e CUE, e disponibilize-as offline.
- **Apple CarPlay** — um ecrã dedicado no carro para a biblioteca, a nuvem, a música local e offline, com o equalizador a bordo.
- **AirPlay 2 e Chromecast** — transmita para HomePods, Apple TV e colunas com Cast.
- **Ferramentas para audiolivros** — múltiplos marcadores, velocidade ajustável, temporizador para dormir e retoma a partir de onde parou.
- **Widgets e mais** — widgets no Ecrã Principal e no Ecrã Bloqueado, scrobbling do Last.fm, letras sincronizadas e LRC, e acessibilidade completa com VoiceOver.

O Flacbox é gratuito. O Premium remove os limites da versão gratuita relativos a contas na nuvem, listas de reprodução e pastas offline, e está disponível como compra vitalícia única ou subscrição mensal ou anual, com Partilha com a Família.

{{< app-details product="flacbox" >}}

## Opção 2: Converter FLAC para ALAC para a aplicação Música

Se realmente quiser os seus rips dentro da aplicação Música da Apple, pode convertê-los. De FLAC para ALAC é de lossless para lossless, por isso não perde qualidade nenhuma:

1. No computador, faça a conversão em lote com uma ferramenta gratuita como o XLD no Mac ou o foobar2000 no Windows. Ambos mantêm as suas etiquetas.
2. Adicione os ficheiros ALAC à sua biblioteca do Música ou do iTunes.
3. Sincronize com o iPhone através do Finder no Mac ou da aplicação Apple Devices no Windows.

As desvantagens são reais. Passa a manter duas cópias da sua biblioteca, cada edição de metadados implica outra sincronização, e o layout da aplicação Música permanece fixo, sem listas de reprodução baseadas em regras, sem equalizador, sem DSP e sem streaming da nuvem ou do NAS no dispositivo. É por isso que a maioria das pessoas com coleções FLAC sérias escolhe a primeira opção.

## FAQ

{{% details title="O iPhone consegue reproduzir ficheiros FLAC nativamente?" closed="true" %}}
Apenas de forma limitada. A aplicação Ficheiros consegue pré-visualizar um único ficheiro FLAC desde o iOS 11, mas não há biblioteca, listas de reprodução, fila, equalizador nem streaming da nuvem. Para ouvir a sério, use uma aplicação de reprodução como o Flacbox.
{{% /details %}}

{{% details title="Posso reproduzir FLAC de 24-bit ou 96kHz (ou superior) no iPhone?" closed="true" %}}
Sim. O Flacbox suporta saída de alta resolução até 384 kHz. Para reproduzir acima de 48 kHz na resolução real, ligue um DAC USB externo, porque a saída incorporada do iPhone reamostra o áudio para todas as aplicações.
{{% /details %}}

{{% details title="O Flacbox converte o FLAC para outro formato?" closed="true" %}}
Não. O Flacbox reproduz o FLAC na sua qualidade lossless original, sem conversão. Os efeitos e o DSP são aplicados ao vivo apenas durante a reprodução, e nunca alteram os seus ficheiros.
{{% /details %}}

{{% details title="Perco qualidade ao converter FLAC para ALAC?" closed="true" %}}
Não. O FLAC e o ALAC são ambos lossless, por isso a conversão é bit-perfect. Só gasta tempo e abdica de conveniência, uma vez que fica com duas bibliotecas para manter e tem de sincronizar de novo após as edições.
{{% /details %}}

{{% details title="Que formatos de áudio suporta o Flacbox?" closed="true" %}}
Mais de 120 formatos, incluindo FLAC, DSD (DSF e DFF), ALAC, APE, WAV, AIFF, WV, OGG, OPUS, MP3, AAC, M4A, WMA, e até música tracker e MOD como MOD, XM, IT e S3M.
{{% /details %}}

{{% details title="O Flacbox tem equalizador, efeitos e visualizador?" closed="true" %}}
Sim. Tem um equalizador de 10 bandas com predefinições e um pré-amplificador. Tem também um motor BASS profissional com onze efeitos em tempo real (reverberação, delay, eco multi-tap, crossfeed, compressor, chorus, flanger, phaser, auto-wah, distortion e stereo rotation), além de nivelamento de volume EBU R128, um processador DSP de 14 filtros e um visualizador Milkdrop em ecrã inteiro com 500 predefinições.
{{% /details %}}

{{% details title="Posso fazer streaming de FLAC a partir do meu NAS ou nuvem?" closed="true" %}}
Sim. O Flacbox liga-se a mais de 30 serviços na nuvem e a um NAS ou computador através de SMB, WebDAV, DLNA, FTP, SFTP e NFS. Toda a sua biblioteca fica disponível sem copiar ficheiros para o iPhone, e pode transferir faixas para reprodução offline a qualquer momento.
{{% /details %}}

{{% details title="O Flacbox é mesmo gratuito?" closed="true" %}}
O Flacbox é gratuito, com funcionalidades essenciais como o equalizador, o streaming da nuvem e a reprodução offline. O Premium remove os limites da versão gratuita relativos a contas na nuvem, listas de reprodução e pastas offline, e vem como compra vitalícia única ou subscrição mensal ou anual, com Partilha com a Família.
{{% /details %}}
