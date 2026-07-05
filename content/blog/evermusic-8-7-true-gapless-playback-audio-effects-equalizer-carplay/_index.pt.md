---
title: "Evermusic 8.7: reprodução sem intervalos de verdade, efeitos de áudio, normalização de volume e equalizador redesenhado"
date: 2026-07-05
description: "O Evermusic 8.7 para iPhone, iPad e Mac adiciona reprodução sem intervalos de verdade, cinco efeitos de áudio de estúdio (reverb, delay, distorção, compressor, crossfeed), normalização de volume EBU R128, um equalizador de 10 bandas redesenhado com importação/exportação de presets, um motor de streaming AVAudioEngine reconstruído com suporte a FLAC e Ogg Vorbis, além de CarPlay e Tocando agora mais rápidos e precisos."
keywords: ["Evermusic 8.7", "atualização Evermusic", "reprodução sem intervalos real iPhone", "reprodutor de música sem intervalos iOS", "reprodução sem intervalos CarPlay", "efeitos de áudio reprodutor de música iPhone", "reverb delay distorção compressor crossfeed iOS", "crossfeed fones de ouvido iOS", "normalização de volume iPhone", "normalização de loudness reprodutor de música", "normalização EBU R128 iOS", "alternativa ao replay gain iPhone", "equalizador de 10 bandas iPhone", "equalizador gráfico app iOS", "importar exportar presets do equalizador", "reprodutor FLAC iPhone", "reprodutor Ogg Vorbis iOS", "reprodutor de música lossless iPhone 2026", "reprodutor de música AVAudioEngine", "reprodutor de música CarPlay iPhone", "precisão Tocando agora tela bloqueada", "reprodutor de música na nuvem iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Reprodução sem intervalos", "Efeitos de áudio", "Reverb", "Delay", "Distorção", "Compressor", "Crossfeed", "Normalização de volume", "EBU R128", "Equalizador", "FLAC", "Ogg Vorbis", "CarPlay", "Tocando agora", "Liquid Glass", "Novidades"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Resumo:** O [Evermusic 8.7](/products/evermusic) é um lançamento voltado para a qualidade do som para iPhone, iPad e Mac. Ele traz **reprodução sem intervalos de verdade** (sem pausas, cliques ou estalos entre as faixas), um conjunto completo de **efeitos de áudio de estúdio** — reverb, delay, distorção, compressor e crossfeed — e **normalização de volume EBU R128** que mantém o loudness consistente de música para música sem tags de ReplayGain. O **equalizador de 10 bandas** foi redesenhado com novos controles deslizantes, troca de presets mais rápida, presets personalizados que você pode importar e exportar, e um layout melhor no modo paisagem e no iPad. Por dentro, um **motor de streaming AVAudioEngine reconstruído** melhora a confiabilidade e o suporte a formatos, incluindo **FLAC** e **Ogg Vorbis**. O **CarPlay** e o **Tocando agora** estão mais rápidos e precisos na tela bloqueada, no carro e nos controles remotos dos fones de ouvido.

---

## Olá a todos!

O Evermusic 8.7 está disponível para download. Esta atualização é toda sobre como sua música *soa*. Reconstruímos o motor de reprodução para uma reprodução sem intervalos de verdade, adicionamos um conjunto de efeitos de áudio de nível de estúdio, introduzimos a normalização de loudness e redesenhamos o equalizador dos controles deslizantes para cima. Tudo está envolto no novo design **Liquid Glass** da Apple.

[Baixe o Evermusic 8.7 na App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) ou atualize a partir da sua versão existente. O Evermusic é um download gratuito com upgrades opcionais no aplicativo.

## Reprodução sem intervalos de verdade

Reprodução sem intervalos significa que o silêncio entre duas faixas desapareceu. Sem pausa, sem clique, sem estalo — a música atual flui diretamente para a próxima. Isso importa sobretudo para músicas projetadas para serem ouvidas como um todo: **gravações ao vivo, mixagens de DJ, obras clássicas e álbuns conceituais** em que uma faixa se funde diretamente em outra.

Veja o que mudou tecnicamente. O motor de áudio do Evermusic mantém duas faixas em execução ao mesmo tempo: a que você está ouvindo e a próxima na fila. Enquanto a faixa atual toca, a próxima já está sendo **buscada, decodificada e pré-armazenada em buffer** em segundo plano. Quando a faixa atual chega ao fim, o motor faz a transição para a próxima faixa **dentro do reprodutor, e não dentro do fluxo de áudio**. O loop de renderização de saída continua puxando amostras de áudio de um buffer circular contínuo sem nunca parar, de modo que o ouvinte nunca percebe uma transição. A troca acontece entre amostras, e é exatamente por isso que não há intervalo audível.

Isso funciona da mesma forma esteja o arquivo no seu dispositivo, na nuvem ou em um servidor de mídia — o pré-buffer apenas começa um pouco mais cedo para fontes remotas.

## Efeitos de áudio de estúdio

O Evermusic 8.7 adiciona cinco efeitos de áudio em tempo real que você pode empilhar sobre a sua música. Cada um roda como um nó nativo de processamento de áudio no motor de reprodução, então se aplica a tudo o que você toca — arquivos locais, streams na nuvem e rádio pela internet — sem recodificação.

Cada efeito vem com uma **biblioteca curada de presets** para obter um ótimo som com um toque, e o Evermusic **lembra suas configurações exatas** entre sessões. Ajuste qualquer controle e o efeito muda para um estado **Manual**, para que você sempre saiba quando se afastou de um preset.

### Reverb

Adiciona uma sensação de espaço, de uma sala fechada a uma catedral. Construído sobre o `AVAudioUnitReverb` da Apple, oferece **13 presets de ambiente** (Sala pequena, Salão médio, Plate, Catedral e outros), além de um controle de **mix wet/dry** de 0 a 100%, para que você decida quanto espaço adicionar.

### Delay (eco)

Um eco clássico com **10 presets** — Slapback, Eco de fita, Dub, Ambiente e outros. Você pode ajustar o **tempo de delay** (até 2 segundos), o **feedback** (quantas repetições), um **corte passa-baixa** para aquecer as repetições e o **mix wet/dry**.

### Distorção

De uma aspereza sutil à destruição lo-fi completa, movida pelo `AVAudioUnitDistortion` com **22 presets de caráter** (Bit Brush, Cellphone Concert, Radio Tower e outros), um controle de drive de **pré-ganho** e um mix wet/dry para você mesclar o efeito de volta ao sinal limpo.

### Compressor

Um processador de dinâmica (o `AUDynamicsProcessor` da Apple) que equilibra passagens altas e baixas. Ele expõe o conjunto completo de controles profissionais — **limiar, razão/margem, ataque, liberação, expansão e ganho de compensação** — com **10 presets** ajustados para situações reais: Voz / Podcast, Alta madrugada, Diálogo de filme, Ajuste de streaming e Loudness máximo, entre outros.

### Crossfeed

O crossfeed faz a audição em fones de ouvido soar mais natural ao misturar um pouco do canal esquerdo no direito e vice-versa, do jeito que seus ouvidos escutam alto-falantes reais. É construído sobre o conhecido algoritmo **Bauer stereophonic-to-binaural (bs2b)**, com controle sobre o **nível de crossfeed** e a **frequência de corte**, e **6 presets** incluindo as configurações favoritas dos audiófilos *Chu Moy* e *Jan Meier*. É especialmente bom em mixagens estéreo antigas dos anos 1960 e 1970 com panorâmica extrema.

## Normalização de volume

Já montou uma playlist em que uma faixa explode e a próxima é um sussurro? A normalização de volume resolve isso. O Evermusic 8.7 usa a **medição de loudness EBU R128** (o mesmo padrão ITU-R BS.1770 usado em transmissões e por serviços de streaming) para medir o loudness percebido real de cada faixa e conduzi-lo suavemente a um alvo consistente.

Ao contrário do ReplayGain, ela **não** exige nenhuma tag nos seus arquivos e **não** modifica seu áudio. Funciona em tempo real em qualquer coisa que você toque, incluindo streams na nuvem e rádio ao vivo, e se redefine de forma limpa quando você avança ou troca de faixa.

Quatro presets cobrem os casos comuns:

- **Leve** — nivelamento suave (alvo −20 LUFS).
- **Padrão** — o padrão, loudness estilo streaming (alvo −16 LUFS, até +12 dB de reforço para faixas silenciosas).
- **Forte** — correspondência agressiva para bibliotecas muito variadas (alvo −14 LUFS).
- **Noturno** — mais silencioso e consistente para audição noturna em volume baixo (alvo −23 LUFS).

Você não precisa mais mexer no volume entre as músicas.

## Equalizador redesenhado

O **equalizador gráfico de 10 bandas** do Evermusic recebeu um redesign completo. As bandas cobrem de **32 Hz a 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), cada uma ajustável de **−12 dB a +12 dB** em passos finos de 0,1 dB, com um **preamp** de −24 dB a +24 dB para evitar clipping ao reforçar.

O que há de novo no 8.7:

- **Novos controles deslizantes** — controles precisos e responsivos que adotam a aparência do controle deslizante nativo do sistema iOS 26 e o material **Liquid Glass**.
- **Troca de presets mais rápida e suave** — salte entre presets instantaneamente, com uma barra de presets horizontal redesenhada no modo retrato e uma coluna de presets vertical no modo paisagem.
- **Melhor layout no modo paisagem e no iPad** — os controles deslizantes e o seletor de presets se reorganizam para usar a largura extra, em vez de se espremer em uma coluna do tamanho de um telefone.
- **Presets personalizados** — crie e salve suas próprias curvas, reordene-as e **importe e exporte** presets como arquivos `.eqp` para movê-los entre dispositivos ou compartilhá-los.

O equalizador roda nativamente no motor (`AVAudioUnitEQ`), então se aplica a todas as fontes, e também funciona por AirPlay, Chromecast e CarPlay onde houver suporte.

## Motor de reprodução reconstruído

Por dentro, o Evermusic 8.7 roda sobre um **motor de streaming reconstruído** construído sobre o `AVAudioEngine` da Apple com um pipeline de renderização personalizado. É isso que torna possível a transição sem intervalos, a cadeia de efeitos e o equalizador, e também torna a reprodução do dia a dia mais confiável.

- **Suporte a formatos aprimorado** — incluindo **FLAC** (via Core Audio) e **Ogg Vorbis** (via `libvorbisfile`), ao lado de MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF e outros.
- **Buffer mais inteligente** — um pré-buffer adaptativo se ajusta à sua conexão, com um buffer circular contínuo alimentando a saída para que pequenas oscilações da rede não virem cortes.
- **Recuperação automática** — uma máquina de estados de rebuffer e uma lógica de nova tentativa com recuo retomam a reprodução de forma limpa após um momento de sinal fraco, em vez de parar a faixa.
- **Menos interrupções** — o mesmo motor conduz arquivos locais, streams na nuvem, servidores de mídia e rádio pela internet, então o comportamento é consistente em toda parte.

## Tocando agora e CarPlay

As telas que você realmente olha enquanto ouve — a **tela bloqueada**, o **CarPlay** e os botões de controle remoto do carro ou dos fones — estão mais precisas e rápidas no 8.7.

- **Informações do Tocando agora mais precisas.** O Evermusic captura o estado do reprodutor sob um bloqueio antes de publicá-lo, então o título, o tempo decorrido, a duração e o estado de reprodução/pausa nunca podem discordar entre si na tela bloqueada ou no carro. Os estados de buffer e carregamento agora são reportados corretamente, em vez de mostrar "tocando" enquanto uma faixa ainda está sendo buscada.
- **Controles remotos confiáveis.** Tocar, pausar, próxima, anterior, avançar, pular, aleatório, repetir e velocidade de reprodução respondem de forma consistente pelos botões dos fones, controles do carro e tela bloqueada, movidos pelo `MPRemoteCommandCenter`.
- **Capas mais rápidas no CarPlay.** As capas de álbum agora carregam várias vezes mais rápido em listas longas (ritmo de lote reduzido de 1,0 s para 0,25 s, com a primeira tela visível carregando imediatamente), e agora aparecem nas linhas compactas da lista do CarPlay no iOS 26 que antes não mostravam capa.
- **Correções de ordenação e estabilidade no CarPlay.** Ordenação mais rápida em bibliotecas grandes e proteção contra travamentos em casos extremos ao rolar listas longas.
- **Atualizações de metadados limitadas.** As atualizações do Tocando agora e dos comandos remotos são limitadas para que mudanças rápidas não inundem o sistema, o que mantém os controles da tela bloqueada e do CarPlay responsivos.

## Outras melhorias

- **Refinamentos do design Liquid Glass** por todo o aplicativo — superfícies translúcidas, animações mais suaves e controles refinados no iOS, iPadOS e macOS.
- **Novos widgets da Tela de Início** com lógica de atualização aprimorada que os mantém sincronizados sem consumir bateria extra.
- Correções para versões recentes do iOS.
- Correções de localização em vários idiomas.
- Muitas melhorias menores baseadas nos seus e-mails e avaliações na App Store.

## Por que esta atualização importa

O Evermusic 8.7 foi construído em torno de uma ideia: **sua música deve soar da melhor forma possível, em qualquer fonte.**

1. **Álbuns inteiros, como foram concebidos.** A reprodução sem intervalos de verdade significa que sets ao vivo, mixagens de DJ e álbuns conceituais finalmente tocam do jeito que o artista masterizou.
2. **Um estúdio no seu bolso.** Reverb, delay, distorção, compressor, crossfeed, um equalizador redesenhado e normalização de loudness dão a você controle real sobre o seu som, não apenas um interruptor de ligar/desligar.
3. **A mesma experiência em toda parte.** Arquivos locais, unidades na nuvem, servidores de mídia e rádio pela internet passam todos pelo mesmo motor reconstruído, com um Tocando agora preciso e um CarPlay mais rápido por cima.

## Obtenha o Evermusic 8.7

[**Baixe o Evermusic na App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) ou atualize dentro da App Store. O Evermusic é um download gratuito com upgrades opcionais no aplicativo para recursos avançados.

Se você gosta do aplicativo, deixe uma avaliação na App Store — isso ajuda de verdade. Tem um comentário ou encontrou um problema? Escreva para nós em **support@everappz.com**. Lemos cada mensagem.

## Perguntas frequentes

{{% details title="O que há de novo no Evermusic 8.7?" closed="true" %}}
O Evermusic 8.7 adiciona reprodução sem intervalos de verdade, cinco efeitos de áudio de estúdio (reverb, delay, distorção, compressor e crossfeed), normalização de volume EBU R128, um equalizador de 10 bandas redesenhado com presets personalizados e importação/exportação, um motor de streaming AVAudioEngine reconstruído com suporte a formatos aprimorado (incluindo FLAC e Ogg Vorbis), CarPlay e Tocando agora mais rápidos e precisos, atualizações do design Liquid Glass, widgets da Tela de Início renovados e correções de bugs e de localização.
{{% /details %}}

{{% details title="O Evermusic tem reprodução sem intervalos de verdade?" closed="true" %}}
Sim. A partir do Evermusic 8.7, a reprodução é verdadeiramente sem intervalos: não há pausa, clique ou estalo entre as faixas. O motor faz o pré-buffer e decodifica a próxima faixa enquanto a atual toca, e faz a transição entre amostras de áudio em um buffer circular contínuo, de modo que a passagem é inaudível. Funciona com arquivos locais, streams na nuvem e servidores de mídia, e é ideal para álbuns ao vivo, mixagens de DJ e álbuns conceituais.
{{% /details %}}

{{% details title="Quais efeitos de áudio o Evermusic 8.7 inclui?" closed="true" %}}
Cinco efeitos em tempo real: **reverb** (13 presets de ambiente, mix wet/dry), **delay/eco** (10 presets com tempo de delay, feedback, passa-baixa e mix), **distorção** (22 presets de caráter com pré-ganho e mix), **compressor** (um processador de dinâmica completo com limiar, razão, ataque, liberação, expansão e ganho de compensação, além de 10 presets) e **crossfeed** (crossfeed para fones de ouvido Bauer bs2b com controles de nível e corte e 6 presets). Cada efeito vem com presets curados, e suas configurações personalizadas são lembradas entre sessões.
{{% /details %}}

{{% details title="O que é o crossfeed e por que eu usaria?" closed="true" %}}
O crossfeed mistura uma pequena quantidade filtrada de cada canal estéreo no outro, do jeito que seus ouvidos naturalmente escutam alto-falantes reais em uma sala. Em fones de ouvido, isso reduz a separação exagerada e "dentro da cabeça" de gravações com panorâmica extrema e torna audições longas mais confortáveis. O Evermusic usa o conhecido algoritmo Bauer stereophonic-to-binaural (bs2b) e inclui presets como Chu Moy e Jan Meier. É especialmente eficaz em mixagens estéreo antigas dos anos 1960 e 1970.
{{% /details %}}

{{% details title="Como funciona a normalização de volume no Evermusic?" closed="true" %}}
O Evermusic 8.7 mede o loudness percebido de cada faixa usando o padrão EBU R128 (ITU-R BS.1770) em tempo real e ajusta suavemente o nível em direção a um alvo consistente para que as faixas não deem saltos de volume. Ela não exige tags de ReplayGain e não altera seus arquivos. Há quatro presets disponíveis — Leve (−20 LUFS), Padrão (−16 LUFS), Forte (−14 LUFS) e Noturno (−23 LUFS) — e a normalização se redefine de forma limpa quando você avança ou troca de faixa.
{{% /details %}}

{{% details title="A normalização de volume do Evermusic é a mesma coisa que o ReplayGain?" closed="true" %}}
Ela alcança o mesmo objetivo — loudness consistente entre as faixas — mas funciona de forma diferente. O ReplayGain depende de tags de loudness armazenadas dentro dos seus arquivos. O normalizador do Evermusic mede o loudness ao vivo usando o EBU R128, então funciona em qualquer fonte, incluindo streams na nuvem e rádio pela internet, mesmo quando os arquivos não têm tag alguma.
{{% /details %}}

{{% details title="Quantas bandas tem o equalizador do Evermusic e posso criar meus próprios presets?" closed="true" %}}
O equalizador do Evermusic é um equalizador gráfico de 10 bandas que cobre de 32 Hz a 16 kHz, com cada banda ajustável de −12 dB a +12 dB em passos de 0,1 dB e um preamp de −24 dB a +24 dB. Ele inclui presets integrados, permite criar e salvar presets personalizados e suporta importar e exportar presets como arquivos .eqp para que você possa movê-los ou compartilhá-los entre dispositivos.
{{% /details %}}

{{% details title="O que mudou no equalizador do Evermusic 8.7?" closed="true" %}}
O equalizador foi redesenhado com novos controles deslizantes mais precisos que adotam a aparência do controle deslizante do sistema iOS 26 e do Liquid Glass, troca de presets mais rápida e suave, e um layout melhor no modo paisagem e no iPad (uma barra de presets horizontal no modo retrato e uma coluna de presets vertical no modo paisagem). Presets personalizados e importação/exportação de .eqp são suportados.
{{% /details %}}

{{% details title="O Evermusic 8.7 suporta FLAC e Ogg Vorbis?" closed="true" %}}
Sim. O motor reconstruído reproduz FLAC (via Core Audio) e Ogg Vorbis (via libvorbisfile), junto com MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF e outros, a partir de arquivos locais, unidades na nuvem e servidores de mídia.
{{% /details %}}

{{% details title="O que melhorou no CarPlay e na tela bloqueada?" closed="true" %}}
As capas de álbum do CarPlay carregam várias vezes mais rápido em listas longas e agora aparecem nas linhas compactas da lista do iOS 26 que antes não mostravam nenhuma. As informações do Tocando agora na tela bloqueada e no CarPlay estão mais precisas — o título, o tempo decorrido, a duração e o estado de reprodução/pausa são capturados juntos para que não possam discordar, e os estados de buffer são reportados corretamente. Os controles remotos (tocar, pausar, próxima, anterior, avançar, aleatório, repetir, velocidade) respondem de forma confiável pelos fones e pelo carro, e a ordenação do CarPlay em bibliotecas grandes está mais rápida.
{{% /details %}}

{{% details title="Os efeitos de áudio e o equalizador funcionam com streaming na nuvem e CarPlay?" closed="true" %}}
Sim. Os efeitos, o equalizador e a normalização de volume rodam nativamente dentro do motor de reprodução, então se aplicam a tudo o que o Evermusic toca — arquivos locais, unidades na nuvem, servidores de mídia e rádio pela internet — e continuam funcionando durante a reprodução no CarPlay e, onde houver suporte, por AirPlay e Chromecast.
{{% /details %}}

{{% details title="A atualização para o Evermusic 8.7 é gratuita e quais dispositivos ela suporta?" closed="true" %}}
Sim. O Evermusic é um download gratuito na App Store, e o 8.7 é uma atualização gratuita para usuários existentes, com upgrades opcionais no aplicativo para recursos avançados. Ele roda em iPhone, iPad e Mac. O CarPlay requer um veículo ou central compatível com CarPlay.
{{% /details %}}
