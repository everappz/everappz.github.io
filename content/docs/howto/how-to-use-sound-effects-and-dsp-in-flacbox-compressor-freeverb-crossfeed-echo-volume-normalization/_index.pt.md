---
title: "Como usar efeitos sonoros e DSP no Flacbox: Compressor, Freeverb, Crossfeed, Echo, normalização de volume e muito mais"
date: 2026-07-24
description: "O guia completo do áudio do Flacbox no iPhone, iPad e Mac. Aprenda como o motor BASS funciona, quais formatos extras ele reproduz (incluindo música MOD e de tracker e DSD) e exatamente o que cada efeito, cada slider e cada preset faz ao seu som, além do equalizador de 10 bandas e da cadeia DSP personalizada."
keywords: ["efeitos de áudio Flacbox", "presets do Flacbox explicados", "motor BASS do Flacbox", "biblioteca de áudio BASS iOS", "reprodutor de música MOD iPhone", "reprodutor de música tracker iOS", "reproduzir MOD XM IT S3M iPhone", "reprodutor DSD iOS", "reprodutor FLAC iPhone", "reprodutor de música lossless iOS", "presets de equalizador Flacbox", "equalizador de 10 bandas iPhone", "normalização de volume iPhone", "EBU R128 iOS", "normalização de loudness reprodutor de música", "crossfeed fones de ouvido iOS", "bs2b crossfeed", "presets de compressor reprodutor de música", "reverb freeverb iOS", "echo delay reprodutor de música", "cadeia DSP reprodutor de música", "reforço de graves iPhone", "como adicionar efeitos à música Flacbox", "melhores ajustes de equalizador iPhone"]
tags: ["Flacbox", "Efeitos de áudio", "Como fazer", "BASS", "Equalizador", "Reforço de graves", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalização de volume", "EBU R128", "Música MOD", "Música tracker", "DSD", "FLAC", "DSP", "Fones de ouvido", "Presets"]
readingTime: 30
---

{{< author-byline >}}

**Resposta curta:** No Flacbox você escolhe um **Motor de reprodução** em **Configurações > Reprodutor de áudio**: **Standard** (o motor de sistema da Apple), **Universal** (o motor FFmpeg) ou **Sound FX** (o **motor BASS™**). O motor que você escolhe decide quais formatos de arquivo são reproduzidos, então a escolha importa. O motor **Sound FX** reproduz formatos extras que a maioria dos apps de iPhone ignora (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus e antigas **músicas MOD e de tracker** como MOD, XM, IT e S3M), e é o único motor que alimenta as ferramentas de som: um **equalizador de 10 bandas**, **Normalização de volume**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** e uma **cadeia DSP** que você mesmo monta. Portanto, para usar os efeitos deste guia, defina primeiro o Motor de reprodução como **Sound FX**. Cada ferramenta tem **presets** prontos. Abra-os em **Configurações > Reprodutor de áudio** (Efeitos de áudio, Equalizador de áudio, Processamento de sinal), ou toque no botão **⋯ (Mais)** no reprodutor e escolha **Efeitos de áudio**. Nada do que você faz aqui altera seus arquivos.

> As explicações de sliders e presets abaixo são as mesmas descrições curtas que o Flacbox mostra dentro do app, misturadas com um pouco de contexto extra para que você tenha o panorama completo antes de tocar.

## Como ler este guia

Toda ferramenta funciona da mesma maneira:

1. **Ligue-a.** Cada efeito tem seu próprio botão de ligar/desligar. Todos começam desligados. Você pode ligar quantos quiser ao mesmo tempo.
2. **Escolha um preset.** Um preset é um ajuste pronto. Toque em um e o som muda na hora. Este guia lista o que **cada** preset faz.
3. **Ajuste fino (opcional).** Abra os sliders para ajustar manualmente. No momento em que você move um slider, o efeito mostra **Manual**, então você sabe que saiu do preset. Cada slider tem um botão de reset.

Nada é salvo em seus arquivos. Estes são efeitos ao vivo. Desligue um efeito e o som original volta imediatamente.

## Escolha seu motor de reprodução (o Sound FX tem os efeitos)

O Flacbox não mistura motores. Você escolhe **um** em **Configurações > Reprodutor de áudio > Motor de reprodução**, e o motor escolhido decide quais formatos de arquivo você pode reproduzir e se os efeitos estão disponíveis. Há três opções, mostradas no app com estes nomes exatos:

1. **Standard.** O motor de sistema integrado da Apple. Usa decodificação por hardware para menor consumo de bateria.
2. **Universal.** O motor FFmpeg, que abre uma gama muito ampla de formatos.
3. **Sound FX.** O **motor BASS™**. Ele reproduz arquivos lossless e de alta resolução com total precisão, adiciona música de módulo (tracker) e alimenta todos os efeitos, o equalizador de 10 bandas e a cadeia DSP deste guia.

Como cada motor suporta seu próprio conjunto de formatos, os arquivos que você pode reproduzir mudam conforme o motor que você seleciona. Mais importante, os efeitos, o equalizador e a cadeia DSP funcionam **apenas** com o motor **Sound FX**, então escolha-o primeiro se quiser usá-los.

O Sound FX é construído sobre o **BASS™**, uma biblioteca de áudio profissional da Un4seen Developments. Você pode ler mais sobre ela na sua página inicial em [un4seen.com](https://www.un4seen.com/).

## Formatos de música: o que o motor Sound FX (BASS™) adiciona (incluindo música MOD e de tracker)

Com o motor **Sound FX (BASS™)** selecionado, o Flacbox reproduz os formatos especializados abaixo, além dos comuns do dia a dia. O mais especial é a **música de módulo**, também chamada de **música de tracker**. Um arquivo de módulo não é uma gravação normal. Ele contém pequenos sons de instrumentos mais uma «partitura» que diz como tocá-los, e o Flacbox reconstrói a música ao vivo a partir dessa partitura, da maneira como esses arquivos foram feitos para serem tocados. Reprodutores normais não conseguem fazer isso.

| Tipo de música | Formatos | Bom saber |
|---|---|---|
| **Música de módulo / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Reconstruída ao vivo pelo reprodutor de módulos BASS™. Ótima para chiptunes e antigas músicas de demoscene ou Amiga. |
| **Lossless moderno** | FLAC | Qualidade total, menor que WAV. |
| **Outro lossless** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Tipos lossless menos comuns, todos suportados. |
| **DSD de alta resolução** | DSF, DFF | Reproduz em hardware normal usando DSD sobre PCM. |
| **Lossy moderno** | Opus, Ogg Vorbis, MP3 | Os tipos habituais de streaming e download. |

O motor Sound FX também reproduz os formatos Apple predominantes (AAC, ALAC, M4A, WAV, AIFF) e transmissões ao vivo, então os efeitos e o equalizador funcionam nesses também.

**Por que isso ajuda você:** se você tem uma mistura de álbuns FLAC, arquivos DSD de alta resolução e uma pasta de antigas músicas de tracker MOD ou XM, o Flacbox reproduz todos, e o equalizador e os efeitos funcionam em cada um deles.

## Os três menus que você vai usar

O Flacbox mantém suas ferramentas de som em três lugares, todos dentro dos ajustes do reprodutor de áudio. Primeiro certifique-se de que seu **Motor de reprodução** esteja definido como **Sound FX** (Configurações > Reprodutor de áudio > Motor de reprodução), porque os efeitos, o equalizador e a cadeia DSP estão disponíveis apenas com esse motor.

- **Efeitos de áudio** (o rack de efeitos): abra o reprodutor, toque em **⋯ (Mais)**, toque em **Efeitos de áudio**. Ou vá em **Configurações > Reprodutor de áudio > Efeitos de áudio**.
- **Equalizador de áudio** (10 bandas e presets): **Configurações > Reprodutor de áudio > Equalizador de áudio**.
- **Processamento de sinal** (sua própria cadeia DSP): **Configurações > Reprodutor de áudio > Processamento de sinal**.

Você também pode definir a **taxa de amostragem de saída**, os **canais** e o **tamanho do buffer** em **Configurações > Reprodutor de áudio**.

## O equalizador de 10 bandas

**O que faz:** Muda o timbre da música, dos graves profundos aos agudos brilhantes. Esta é a melhor ferramenta para um **reforço de graves** limpo ou um topo mais brilhante e nítido. Pense nele como dez botões de volume, cada um para uma faixa diferente do som. Aumente uma banda para trazer aquela parte à frente, diminua para recuá-la. Pequenas mudanças de alguns dB geralmente soam melhor, e funciona em tudo que você reproduz.

**Como funciona:** Dez sliders em **32, 64, 125, 250, 500 Hz e 1, 2, 4, 8, 16 kHz**. Cada um vai de **-12 dB (corte)** a **+12 dB (reforço)**. Há também um **Pré-amplificador** de **-24 a +24 dB** para o nível geral. Você pode salvar seus próprios presets e **exportá-los ou importá-los** entre dispositivos.

**O que cada preset integrado faz (22 presets):**

| Preset | O que faz ao seu som |
|---|---|
| **Flat** | Sem mudança. Todas as bandas em zero. Um ponto de partida limpo. |
| **Acoustic** | Graves quentes e agudos nítidos e presentes. Faz violões e vozes soarem naturais e vivos. |
| **Bass Booster** | Forte elevação nos graves, médios e agudos intocados. Mais punch e peso. |
| **Bass Reducer** | Corta os graves. Útil para salas com muita ressonância, fones baratos ou faixas pesadas. |
| **Treble Booster** | Eleva apenas os agudos. Adiciona brilho e ar, mais detalhe. |
| **Treble Reducer** | Suaviza os agudos. Doma gravações ásperas ou estridentes. |
| **Classical** | Graves cheios e agudos suaves com uma leve queda nos médios. Suave e espaçoso para música orquestral. |
| **Dance** | Graves grandes e agudos brilhantes com médios rebaixados. Punchy e enérgico para faixas de clube. |
| **Deep** | Graves quentes e densos com agudos mais suaves. Um som aconchegante e descontraído. |
| **Electronic** | Graves fortes e agudos brilhantes para sintetizadores e batidas. Amplo e moderno. |
| **Hip-Hop** | Graves pesados e agudos nítidos com médios controlados. Encorpado e punchy. |
| **Jazz** | Quente e suave, com uma pequena queda nos médios. Fácil e natural para jazz acústico. |
| **Latin** | Graves e agudos reforçados com médios limpos. Brilhante e vivo. |
| **Loudness** | Reforça graves e agudos fortemente (uma curva «sorriso»). Soa mais cheio em volume baixo. |
| **Lounge** | Médios à frente com bordas suaves. Relaxado e amigável para vocais. |
| **Piano** | Médios e agudos nítidos para que as notas de piano soem com clareza. |
| **Pop** | Médios elevados para vocais, com graves e agudos recuados. As vozes ficam à frente. |
| **R&B** | Calor de médios-graves muito forte e agudos nítidos. Suave e rico. |
| **Rock** | Graves e agudos reforçados para guitarras e baterias. Enérgico e cheio. |
| **Small Speakers** | Reforça os graves e corta os agudos para ajudar alto-falantes pequenos a soarem mais cheios. |
| **Spoken Word** | Eleva a faixa da voz e corta os graves profundos. Torna a fala clara. |
| **Vocal Booster** | Empurra os médios onde vivem as vozes, cortando ao redor delas. As vozes se destacam. |

**Dica para graves:** Comece com **Bass Booster** e, se soar embolado, puxe o Pré-amplificador para baixo 1 a 2 dB para que nada distorça.

## Normalização de volume (loudness uniforme)

**O que faz:** Algumas músicas tocam mais alto que outras, então você fica mudando o volume. Isto faz cada música tocar aproximadamente no mesmo volume sozinha, para que você não precise. É perfeito para playlists aleatórias que misturam gravações antigas e novas, álbuns diferentes ou fontes diferentes, onde uma faixa pode ser muito mais alta que a próxima.

**Como funciona:** Ele escuta o loudness real de cada faixa usando o padrão **EBU R128** (medido em **LUFS**, a mesma ideia que os serviços de streaming usam), então ajusta cada faixa em direção ao seu alvo. Não precisa de nenhuma tag em seus arquivos e nunca altera o áudio. O EBU R128 mede o loudness que seus ouvidos realmente sentem ao longo de toda a música, não apenas o pico mais alto, e é por isso que corresponde a quão altas as faixas realmente parecem para você. O Flacbox calcula isso ao vivo enquanto a música toca (e verifica o loudness com antecedência quando pode), então aplica uma única mudança de volume estável à faixa. O limite **Max boost** impede que gravações muito baixas sejam empurradas para cima com tanta força que distorçam. Como ele lê o próprio som, funciona em qualquer fonte, incluindo arquivos na nuvem, transmissões ao vivo e música de módulo, mesmo quando os arquivos não têm nenhuma tag de loudness.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Target loudness** | Define o loudness ao qual toda faixa é nivelada. Valores mais altos fazem tudo tocar mais alto no geral. | -30 a -6 LUFS (-16) |
| **Max boost** | Limita quanto as faixas baixas podem ser amplificadas. Valores mais altos aproximam gravações suaves do alvo. | 0 a 24 dB (12) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Light** | Nivelamento suave para audição casual. Iguala saltos óbvios de volume sem empurrar faixas baixas com força. |
| **Standard** | O padrão de uso geral. Um alvo de loudness estilo streaming que combina com a maioria das músicas. Comece aqui. |
| **Strong** | Correspondência agressiva que empurra as faixas baixas para cima com firmeza. Melhor para bibliotecas mistas com grandes diferenças de nível. |
| **Night** | Um alvo geral mais baixo que ainda eleva passagens suaves, para que a audição noturna se mantenha consistente e baixa. |

## Compressor (nivele partes altas e baixas)

**O que faz:** Em uma mesma música, as partes baixas podem ser suaves demais e as altas altas demais. Isto as aproxima, para que a música inteira seja fácil de ouvir, mesmo no carro ou em um lugar barulhento. Ele abaixa suavemente os momentos mais altos e eleva os mais suaves, para que você pare de mexer no volume durante uma única faixa. Isto é diferente da Normalização de volume: o Compressor nivela as coisas **dentro** de uma música, enquanto a Normalização de volume iguala o loudness **entre** músicas. Os dois funcionam bem juntos. Comece com um preset e só abra os sliders se quiser mais controle.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Threshold** | O nível onde a compressão começa. Valores mais baixos comprimem mais o som, mantendo partes baixas e altas mais próximas. | -60 a 0 dB (-20) |
| **Ratio** | Com que intensidade as partes altas são contidas depois de passarem o threshold. Valores mais altos comprimem com mais força, mantendo o som mais uniforme. | 1:1 a 30:1 (4:1) |
| **Attack** | Com que rapidez o efeito responde a um pico alto repentino. Valores curtos capturam transientes; os mais longos os deixam passar. | 0,1 a 1000 ms (10 ms) |
| **Release** | Com que rapidez o efeito solta depois que a parte alta passa. Valores curtos podem bombear; os mais longos soam mais suaves. | 10 ms a 5 s (100 ms) |
| **Master gain** | Reforço final de saída aplicado após o processamento. Aumente-o para elevar o loudness geral depois que a dinâmica for nivelada. | -30 a +30 dB (0) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Transparent** | Rede de segurança quase imperceptível. Preserva a dinâmica quase inteiramente e captura apenas os picos mais altos. |
| **Soft** | Nivelamento leve para audição hi-fi em casa. Suavização sutil sem comprimir a música. |
| **Standard** | Padrão sensato para reprodução de música do dia a dia. O primeiro preset a experimentar. |
| **Heavy** | Nivelamento agressivo para ambientes barulhentos. Carro, sala cheia, audição em volume baixo. |
| **Voice / Podcast** | Ajustado para fala. Attack mais lento deixa passar as sibilantes, ganho de makeup generoso eleva os vocais. |
| **Old Recordings** | Álbuns antigos e vinil restaurado, onde o nível médio está abaixo dos lançamentos modernos. |
| **Late Night** | Compressão pesada mais grande reforço para audição em volume baixo quando vizinhos ou família dormindo importam. |
| **Movie Dialog** | Traz a fala à frente da música e dos efeitos sonoros em uma trilha variada. |
| **Streaming Match** | Mira aproximadamente a normalização de loudness dos serviços de streaming modernos, em torno de -14 LUFS. |
| **Maximum Loudness** | Tudo no máximo. Atinge o limitador; espere um sinal comprimido e muito nivelado. O preset literal de volume máximo. |

## Freeverb (reverb, uma sensação de espaço)

**O que faz:** Adiciona uma sensação de espaço à música, de uma sala pequena a um grande salão. Escolha um preset, ou ajuste você mesmo a mistura seca e molhada, o tamanho da sala, o damping e a largura. O reverb é o eco natural que você ouve em qualquer espaço real, e o Freeverb o recria em software. Um pouco faz gravações planas ou de microfone próximo parecerem mais abertas e vivas. Muito coloca a música em um espaço grande e distante. É um efeito criativo, então mantenha a mistura molhada modesta para resultados naturais.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Dry mix** | Quanto do som original e intocado é mantido. Valores mais altos deixam mais do sinal seco na mistura. | 0 a 1 (0,0) |
| **Wet mix** | Quanto do som reverberado é adicionado. Valores mais altos tornam o reverb mais alto e mais evidente. | 0 a 3 (1,0) |
| **Room size** | O tamanho do espaço imaginado. Valores mais altos dão uma cauda de reverb mais longa e maior, de uma sala pequena a uma catedral. | 0 a 1 (0,5) |
| **Damp** | Com que rapidez as frequências altas somem na cauda. Valores mais altos tornam o reverb mais escuro e quente. | 0 a 1 (0,5) |
| **Width** | A dispersão estéreo do reverb. Valores mais altos fazem o espaço parecer mais amplo entre os canais esquerdo e direito. | 0 a 1 (1,0) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Room** | Um espaço pequeno e fechado. Ambiência sutil que adiciona uma sensação de lugar sem apagar o som. |
| **Studio** | Uma sala de gravação seca e controlada. Reflexão apenas o suficiente para soar natural. |
| **Hall** | Um grande salão de concertos. Uma cauda longa e exuberante que combina com música orquestral e acústica. |
| **Cathedral** | Um enorme espaço de pedra com eco. A cauda de reverb mais longa e dramática. |
| **Plate** | Um reverb de placa de estúdio brilhante e denso. Clássico para vocais e baterias. |
| **Ambience** | Uma ambiência curta e arejada. Adiciona uma leve sensação de espaço permanecendo quase seco. |

## Auto Wah (varredura de filtro funky)

**O que faz:** Um filtro que varre para cima e para baixo por conta própria, para um som wah funky, parecido com voz. Escolha um preset, ou ajuste você mesmo a mistura molhada, o feedback, a taxa, a amplitude e a frequência. É a mesma varredura «wah» que um pedal wah de guitarra faz, mas aqui ela se move sozinha no ritmo da música. Soa ótimo em faixas de funk, disco e eletrônicas. É um efeito ousado e evidente, então pouco já faz muito na audição do dia a dia.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Wet mix** | Quão forte o efeito wah está na mistura. Valores mais altos tornam o filtro de varredura mais evidente. | -2 a +2 (1,5) |
| **Feedback** | Quanto da saída é realimentado no efeito. Valores mais altos tornam o wah mais ressonante e pronunciado. | -1 a +1 (0,5) |
| **Rate** | Com que rapidez o filtro varre para cima e para baixo. Valores mais altos dão um wah mais rápido e rítmico. | 0,1 a 9 Hz (2,0) |
| **Range** | Quão longe o filtro varre, em oitavas. Valores mais altos dão uma varredura mais ampla e dramática. | 0,1 a 9 oitavas (4,3) |
| **Frequency** | A frequência base em torno da qual o filtro varre. Valores mais baixos soam mais profundos; os mais altos soam mais brilhantes. | 1 a 1000 Hz (50) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Classic** | Uma varredura wah clássica e equilibrada. Um bom ponto de partida para funk e rock. |
| **Slow** | Uma varredura lenta e ampla que deriva suavemente para cima e para baixo. Ótima para pads e notas longas. |
| **Funky** | Uma varredura rápida e punchy com bastante movimento. Adiciona mordida rítmica a guitarras e sintetizadores. |
| **Deep** | Uma varredura profunda e ampla começando de uma frequência baixa. Grande e dramática. |
| **Subtle** | Um movimento suave e discreto. Adiciona caráter sem dominar o som. |
| **Resonant** | Um wah nítido e ressonante com feedback alto. Parecido com voz e expressivo. |

## Phaser (varredura giratória)

**O que faz:** Um filtro de varredura que adiciona um movimento giratório e soprante ao som. Escolha um preset, ou ajuste você mesmo o feedback, a taxa, a amplitude e a frequência. Ele adiciona movimento suave e brilho sem mudar as notas. É sutil em vocais e pads, e dramático em sintetizadores e guitarras. Experimente Slow para uma sensação sonhadora ou Jet para um giro forte.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Feedback** | Quanto da saída é realimentado no efeito. Valores mais altos tornam o phaser mais ressonante e pronunciado. | -1 a +1 (0,0) |
| **Rate** | Com que rapidez o filtro varre para cima e para baixo. Valores mais altos dão um phasing mais rápido e rítmico. | 0,1 a 9 Hz (1,0) |
| **Range** | Quão longe o filtro varre, em oitavas. Valores mais altos dão uma varredura mais ampla e dramática. | 0,1 a 9 oitavas (4,0) |
| **Frequency** | A frequência base em torno da qual o filtro varre. Valores mais baixos soam mais profundos; os mais altos soam mais brilhantes. | 1 a 1000 Hz (100) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Classic** | Uma varredura de phaser clássica e equilibrada. Um bom ponto de partida para guitarras e teclados. |
| **Slow** | Uma varredura lenta e ampla que deriva suavemente para cima e para baixo. Ótima para pads e notas longas. |
| **Fast** | Uma varredura rápida e cintilante com bastante movimento. Adiciona movimento e energia. |
| **Deep** | Uma varredura profunda e ampla começando de uma frequência baixa. Grande e dramática. |
| **Subtle** | Um movimento suave e discreto. Adiciona caráter sem dominar o som. |
| **Jet** | Uma varredura intensa e ressonante com feedback alto, o clássico sopro de avião a jato. |

## Flanger (varredura de avião a jato)

**O que faz:** Um delay curto e em movimento que dá ao som um sopro varrido, tipo jato. Escolha um preset, ou ajuste você mesmo a profundidade, o feedback, a taxa e o delay. É um primo mais forte e metálico do phaser, famoso pelo sopro varrido no rock clássico e na música eletrônica. Ajustes sutis adicionam movimento suave, enquanto ajustes profundos são dramáticos e evidentes. Melhor usado com moderação, para efeito.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Depth** | Quão forte é o efeito de varredura. Valores mais altos tornam o flanging mais evidente. | 0 a 100% (25) |
| **Feedback** | Quanto da saída é realimentado no efeito. Valores mais altos tornam o flanger mais ressonante e metálico. | -99 a +99% (-50) |
| **Rate** | Com que rapidez a varredura se move para cima e para baixo. Valores mais altos dão um movimento mais rápido e cintilante. | 0 a 10 Hz (0,25) |
| **Delay** | O tempo de delay base sobre o qual a varredura é construída. Valores mais altos dão um caráter mais profundo e oco. | 0 a 4 ms (2,0) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Classic** | Um flanger clássico e equilibrado. Um bom ponto de partida para guitarras e teclados. |
| **Subtle** | Uma varredura suave e discreta. Adiciona movimento sem dominar o som. |
| **Deep** | Uma varredura profunda e pesada com feedback forte. Grande e dramática. |
| **Jet** | Uma varredura intensa com feedback positivo, o clássico sopro de avião a jato. |
| **Fast** | Uma varredura rápida e cintilante com bastante movimento e energia. |
| **Wide** | Uma varredura lenta e ampla com um delay longo. Exuberante e espaçosa. |

## Echo (repetições)

**O que faz:** Repete o som como ecos que somem, para uma sensação de espaço e profundidade. Escolha um preset, ou ajuste você mesmo a mistura molhada, o feedback e o delay. É como gritar em um cânion: o som volta uma ou mais vezes depois de uma breve pausa. Uma única repetição curta adiciona corpo e uma sensação retrô, enquanto repetições mais longas com mais feedback criam caudas espaçosas e prolongadas. O preset Ping Pong faz as repetições saltarem entre seus ouvidos esquerdo e direito, o que é divertido em fones de ouvido. Mantenha a mistura molhada modesta para que os ecos apoiem a música em vez de cobri-la.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Wet mix** | Quão altos são os ecos comparados ao som original. Valores mais altos fazem as repetições se destacarem mais. | -2 a +2 (0,6) |
| **Feedback** | Quantas vezes o eco se repete. Valores mais altos dão mais repetições que demoram mais para sumir. | -1 a +1 (0,5) |
| **Delay** | O tempo entre os ecos. Valores mais curtos dão um slap-back apertado; valores mais longos dão repetições espaçadas. | 0,01 a 2 s (0,4) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Slapback** | Uma única repetição apertada logo atrás do som. Slap-back rockabilly clássico. |
| **Room** | Um eco curto e natural, como uma sala pequena. Adiciona espaço sem borrar o som. |
| **Tape** | Repetições quentes e médias que somem gradualmente, como um antigo delay de fita. |
| **Dub** | Repetições longas e pesadas com feedback forte. Grande, dubby e espaçosa. |
| **Ping Pong** | Os ecos saltam entre os alto-falantes esquerdo e direito para um amplo efeito estéreo. |
| **Long** | Repetições lentas e amplamente espaçadas que se dissipam bem atrás do som. |

## Chorus (som mais espesso e amplo)

**O que faz:** Engrossa e amplia o som sobrepondo uma cópia deslocada sobre o original. Escolha um preset, ou ajuste você mesmo a mistura molhada/seca, a profundidade, a taxa e o feedback. Faz um instrumento ou voz soar como vários tocando juntos, adicionando cópias ligeiramente desafinadas e em movimento. Isso adiciona riqueza e um brilho suave. Ajustes sutis aquecem as coisas, enquanto ajustes fortes soam exuberantes e sonhadores. É popular em guitarras, teclados e vocais.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Wet/Dry** | Quanto do chorus você ouve comparado ao som original. Valores mais altos tornam o efeito mais evidente. | 0 a 100% (50) |
| **Depth** | Quão longe o tom oscila para cima e para baixo. Valores mais altos dão um som mais espesso e cintilante. | 0 a 100% (25) |
| **Rate** | Com que rapidez o brilho se move. Taxas mais lentas soam suaves e exuberantes; taxas mais rápidas soam mais como vibrato. | 0 a 10 Hz (1,1) |
| **Feedback** | Quanto do efeito é realimentado em si mesmo. Valores mais altos tornam o chorus mais ressonante e intenso. | -99 a +99% (25) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Subtle** | Um engrossamento suave que adiciona calor sem chamar atenção para si mesmo. |
| **Lush** | Um chorus rico e clássico. Um ótimo ajuste geral para guitarras e teclados. |
| **Ensemble** | Um brilho cheio e em camadas que faz um único instrumento soar como vários. |
| **Vibrato** | Totalmente molhado com uma taxa rápida, para um vibrato oscilante em vez de um chorus sutil. |
| **Wide** | Um brilho lento e amplo que abre a imagem estéreo. Espaçoso e sonhador. |
| **Twelve-String** | Um brilho brilhante e ressonante que lembra uma guitarra de doze cordas. |

## Distortion (aspereza e mordida)

**O que faz:** Adiciona aspereza e mordida ao sobrecarregar o som. Escolha um preset, ou ajuste você mesmo o drive, a saída e o tom. Ele deliberadamente torna o som mais áspero, de uma mordida quente e áspera a um tom quebrado e difuso. É um efeito criativo e para diversão, não uma forma de melhorar a qualidade, então use-o em pequenas quantidades. É divertido em faixas eletrônicas, de rock e experimentais. Abaixe o Output se um preset pesado ficar alto demais.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Drive** | Quão forte o som é distorcido. Valores mais altos são mais ásperos e agressivos. | 0 a 100% (15) |
| **Output** | O nível de saída após a distorção. Abaixe-o se um ajuste pesado ficar alto demais. | -60 a 0 dB (-18) |
| **Tone** | Reduz os agudos antes da distorção. Valores mais baixos soam mais escuros e quentes. | 100 a 8000 Hz (8000) |
| **Center** | Em torno de qual frequência a distorção se concentra. Desloca o caráter para mais brilhante ou mais escuro. | 100 a 8000 Hz (2400) |
| **Width** | Quão amplo é esse foco. Estreito soa nítido e nasal; amplo soa cheio e aberto. | 100 a 8000 Hz (2400) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Warm Drive** | Uma aspereza leve e quente que adiciona mordida sem mudar muito o caráter. |
| **Crunch** | Um overdrive crocante clássico, punchy e rítmico. |
| **Overdrive** | Um tom brilhante e conduzido com bastante mordida. Ótimo para sons de solo. |
| **Fuzz** | Um fuzz espesso e saturado. Pesado e cheio de harmônicos. |
| **Metal** | Um tom de alto ganho apertado e focado nos médios para sons agressivos e pesados. |
| **Screamer** | Um overdrive com médios reforçados que atravessa, como um tube screamer. |
| **LoFi** | Uma distorção de banda estreita e esmagada para um caráter lo-fi áspero. |

## Rotate (estéreo giratório)

**O que faz:** Gira o som pelo campo estéreo para um efeito rotativo e giratório. Escolha um preset, ou ajuste você mesmo a taxa. Ele move lentamente o som pelos seus canais esquerdo e direito, um pouco como um alto-falante giratório, o que adiciona uma sensação giratória e hipnótica. Ajustes lentos são suaves e amplos, enquanto ajustes rápidos são vertiginosos e evidentes. É um efeito estéreo, então é mais perceptível em fones de ouvido ou alto-falantes bem posicionados.

**Slider:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Rate** | Com que rapidez o som gira pelo campo estéreo. Valores negativos giram no sentido contrário; zero o mantém parado. | -5 a +5 Hz (1,0) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Slow Pan** | Uma deriva lenta e suave de um lado para o outro. Sutil e ampla. |
| **Sway** | Um balanço estável da esquerda para a direita. Adiciona movimento suave à imagem estéreo. |
| **Rotary** | Um giro médio que lembra um alto-falante giratório. |
| **Fast Spin** | Um giro rápido pelo campo estéreo para um efeito vertiginoso e giratório. |
| **Reverse** | Um giro médio na direção oposta. |
| **Whirl** | Um rodopio muito rápido. Intenso e desorientador. |

## Crossfeed (som natural em fones de ouvido)

Em alto-falantes, cada um dos seus ouvidos ouve tanto o alto-falante esquerdo quanto o direito, apenas em tempos e volumes ligeiramente diferentes. Em fones de ouvido, essa mistura natural desaparece: seu ouvido esquerdo ouve apenas o canal esquerdo e seu ouvido direito apenas o direito. Esse «super estéreo» pode fazer a música parecer dividida dentro da sua cabeça, e gravações com panorâmica extrema, onde um instrumento fica totalmente de um lado, podem parecer não naturais ou cansativas em audições longas.

O Crossfeed corrige isso misturando uma pequena quantidade filtrada de cada canal no outro, com um pequeno delay e uma suave redução das frequências altas. Isso se aproxima de como o som de alto-falantes reais chega aos seus dois ouvidos, incluindo a maneira como sua cabeça sombreia ligeiramente o ouvido mais distante. O resultado é uma imagem mais natural, tipo alto-falante, que fica um pouco à sua frente em vez de dentro da sua cabeça, e reduz a fadiga auditiva em sessões longas. O Flacbox usa o conhecido método **bs2b (Bauer stereophonic-to-binaural)**, um crossfeed de código aberto respeitado, usado por muitos reprodutores audiófilos. Você pode ler sobre o algoritmo na [página do projeto bs2b](https://bs2b.sourceforge.net/).

O **Cutoff** controla quão quente a mistura soa, e o **Feed level** controla quão forte ela é. Os presets cobrem os níveis clássicos do bs2b, de um toque quase imperceptível a uma mistura firme, tipo alto-falante. O Crossfeed é um efeito de fones de ouvido, então deixe-o desligado quando você ouvir em alto-falantes.

**Sliders:**

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Cutoff** | Define onde o vazamento entre canais começa a diminuir. Valores mais baixos dão um efeito mais quente e pronunciado. | 300 a 2000 Hz (700) |
| **Feed level** | Controla quanto de um canal vaza para o outro. Valores mais altos produzem um som mais parecido com alto-falante. | 1 a 15 dB (4,5) |

**Presets:**

| Preset | O que faz |
|---|---|
| **Subtle** | Crossfeed quase imperceptível para audição casual. Suaviza o estéreo com panorâmica extrema sem mudar o equilíbrio tonal. |
| **Chu Moy** | O padrão de uso geral clássico. Equilibrado e levemente quente, funciona em quase qualquer material. Comece aqui. |
| **Strong** | Vazamento mais forte para mixagens com panorâmica mais extrema. Estreitamento estéreo mais evidente. |
| **Jan Meier** | Popular entre entusiastas de fones de ouvido. Feed mais amplo, apresentação mais parecida com alto-falante, leve elevação nos graves. |
| **Speaker-like** | Ajustado para a reprodução mais natural, no estilo de alto-falante, em fones de ouvido. |
| **Vintage Stereo** | Crossfeed agressivo ajustado para mixagens dos anos 1960 e 1970 com baterias e vocais em panorâmica extrema. |

## Processamento de sinal: monte sua própria cadeia DSP

Além dos efeitos prontos, o Flacbox permite que você monte sua própria cadeia em **Configurações > Reprodutor de áudio > Processamento de sinal**. Como o app explica quando a cadeia está vazia: *«Toque em + para adicionar um efeito. Ligue ou desligue cada um com seu botão, arraste para reordenar, toque para editar seus parâmetros e mantenha pressionado para duplicar ou excluir.»*

A **ordem importa**: um filtro antes de uma distorção soa diferente do mesmo filtro depois dela. Você também pode apontar toda a cadeia para **Todos os canais**, **Canal esquerdo** ou **Canal direito**.

Abaixo está cada bloco, com o próprio texto do app para cada slider e cada preset.

### Gain (ajuste de nível)

Aumenta ou diminui o nível em um ponto da cadeia.

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Gain** | Reforça ou corta o nível neste ponto da cadeia. Use-o para recuperar nível após outros efeitos, ou para conduzir os que seguem. | -24 a +24 dB (0) |

| Preset | O que faz |
|---|---|
| **Unity** | Sem mudança no nível. Um ponto de partida neutro. |
| **Cut** | Um grande corte. Doma uma fonte alta, ou abre espaço antes dos efeitos que seguem. |
| **Trim** | Um corte suave para puxar o nível um pouco para trás. |
| **Lift** | Um reforço modesto para elevar uma fonte baixa. |
| **Boost** | Um reforço forte para material baixo, ou para conduzir os efeitos seguintes com mais força. |
| **Max** | Reforço máximo. Alto, cuidado com clipping mais adiante na cadeia. |

### Low Pass (remove agudos)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Cutoff** | Define onde o filtro começa a reduzir os agudos. Abaixe-o para escurecer e suavizar o som; aumente-o em direção ao topo para abrir totalmente. | 20 Hz a 20 kHz (20 kHz) |
| **Resonance** | Enfatiza as frequências bem no cutoff. Mantenha-a baixa para uma redução limpa; aumente-a para uma borda com pico e assobio. | 0,1 a 10 (0,707) |

| Preset | O que faz |
|---|---|
| **Air** | Apara apenas o topo. Tira um pouco da borda sem abafar o som. |
| **Warm** | Uma redução suave dos agudos para um tom mais quente e arredondado. |
| **Mellow** | Notavelmente suavizado. Puxa o brilho para trás para uma sensação descontraída. |
| **Muffled** | Escuro e abafado, como se ouvido através de uma parede. |
| **Telephone** | Um pico estreito e ressonante baixo na faixa. Uma voz fina, tipo telefone. |

### High Pass (remove graves)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Cutoff** | Define onde o filtro começa a reduzir os graves. Aumente-o para afinar os graves e remover ruídos; abaixe-o em direção ao fundo para abrir totalmente. | 20 Hz a 20 kHz (20 Hz) |
| **Resonance** | Enfatiza as frequências bem no cutoff. Mantenha-a baixa para uma redução limpa; aumente-a para uma borda com pico e assobio. | 0,1 a 10 (0,707) |

| Preset | O que faz |
|---|---|
| **Rumble Cut** | Remove ruídos subsônicos e offset DC sem tocar nos graves audíveis. |
| **Tighten** | Apara frequências graves com muita ressonância para um grave mais apertado e limpo. |
| **Thin** | Corta o calor e o corpo, deixando um som mais leve e fino. |
| **Radio** | Só os médios e agudos permanecem, como um pequeno alto-falante de rádio. |
| **Telephone** | Um pico estreito e ressonante alto na faixa. Uma voz fina, tipo telefone. |

### Band Pass (mantém uma banda central)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Center** | Define a frequência que o filtro deixa passar. Tudo acima e abaixo é reduzido. Varra-o para destacar graves, médios ou agudos. | 20 Hz a 20 kHz (1 kHz) |
| **Resonance** | Controla quão ampla é a banda. Valores baixos deixam passar uma faixa ampla; aumente-o para estreitar no centro para um tom nítido e ressonante. | 0,1 a 10 (0,707) |

| Preset | O que faz |
|---|---|
| **Voice** | Uma banda ampla em torno dos médios, onde a maioria dos vocais fica. Um ponto de partida neutro. |
| **Bass** | Isola os graves, deixando apenas o baixo e o bumbo. |
| **Body** | Foca nos médios-graves para um corpo quente e encorpado. |
| **Presence** | Eleva os médios-agudos para clareza e presença. |
| **Telephone** | Uma banda estreita de médios. Um som fino, tipo telefone. |
| **Wah** | Um pico muito estreito e ressonante. Varra o centro para um efeito wah. |

### Notch (remove uma banda estreita)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Frequency** | Define a frequência que o filtro remove. Tudo acima e abaixo passa. Ajuste-o sobre um zumbido ou ressonância para eliminá-lo. | 20 Hz a 20 kHz (60 Hz) |
| **Resonance** | Controla quão amplo é o corte. Valores baixos retiram uma faixa ampla; aumente-o para remover apenas uma banda pontual e deixar o resto intocado. | 0,1 a 10 (8,0) |

| Preset | O que faz |
|---|---|
| **Mains Hum 60** | Remove o zumbido elétrico de 60 Hz (rede da América do Norte). Um ponto de partida neutro. |
| **Mains Hum 50** | Remove o zumbido elétrico de 50 Hz (rede europeia e outras). |
| **Rumble** | Corta um ruído ou ressonância de baixa frequência sem afinar todo o fundo. |
| **Mud** | Retira a lama dos médios-graves para um som mais limpo e nítido. |
| **Boxy** | Remove um som «encaixotado» dos médios. |
| **Harsh** | Doma um pico áspero e penetrante nos médios-agudos. |

### Peaking (banda de EQ paramétrico)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Frequency** | O centro da banda a reforçar ou cortar. Varra-o para encontrar a frequência que você quer moldar. | 20 Hz a 20 kHz (1 kHz) |
| **Gain** | Quanto reforçar ou cortar no centro. Positivo eleva a banda; negativo a retira. | -15 a +15 dB (0) |
| **Q factor** | Define quão ampla é a banda. Valores baixos moldam uma área ampla; valores altos estreitam para mudanças cirúrgicas e pontuais. | 0,1 a 10 (1,0) |

| Preset | O que faz |
|---|---|
| **Presence** | Uma elevação ampla nos médios-agudos para clareza e presença. Um ponto de partida neutro. |
| **Warmth** | Um reforço amplo nos médios-graves que adiciona corpo e calor. |
| **Vocal Boost** | Eleva a faixa central da voz para trazer os vocais à frente. |
| **Cut Mud** | Retira a lama «encaixotada» dos médios-graves para um som mais limpo. |
| **Tame Harsh** | Um corte estreito para domar um pico áspero e penetrante. |
| **Punch** | Um reforço nos graves que adiciona punch e impacto ao fundo. |
| **Sub Boost** | Um reforço profundo bem no fundo para peso extra de sub-grave. |
| **Air** | Uma elevação ampla no topo para um brilho aberto e arejado. |
| **Clarity** | Eleva os médios-agudos para adicionar definição e mordida. |
| **De-Ess** | Um corte estreito na faixa de sibilância para domar sons de S ásperos. |
| **De-Boom** | Corta um acúmulo de baixa frequência com muita ressonância para um grave mais apertado. |
| **Scoop** | Uma queda ampla nos médios para um tom rebaixado e moderno. |

### Low Shelf (controle de graves e reforço de graves)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Frequency** | Define o ponto abaixo do qual o shelf tem efeito. Tudo abaixo dele é reforçado ou cortado em conjunto. | 20 a 2000 Hz (200) |
| **Gain** | Quanto elevar ou baixar os graves. Positivo adiciona peso e calor; negativo os afina. | -15 a +15 dB (0) |

| Preset | O que faz |
|---|---|
| **Warmth** | Uma elevação suave nos graves para calor e corpo. Um ponto de partida neutro. |
| **Bass Boost** | Um reforço sólido dos graves para peso e punch. |
| **Fullness** | Preenche os médios-graves para um som mais cheio e arredondado. |
| **Trim Bass** | Um corte modesto para aliviar uma mixagem pesada de graves. |
| **Cut Lows** | Um corte forte para afinar ou reduzir o excesso de graves. |
| **Big Bottom** | Um grande reforço de graves para peso e ressonância máximos. |

### High Shelf (controle de agudos)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Frequency** | Define o ponto acima do qual o shelf tem efeito. Tudo acima dele é reforçado ou cortado em conjunto. | 1 a 20 kHz (8 kHz) |
| **Gain** | Quanto elevar ou baixar os agudos. Positivo adiciona brilho e ar; negativo suaviza e escurece. | -15 a +15 dB (0) |

| Preset | O que faz |
|---|---|
| **Presence** | Uma elevação suave nos agudos para clareza e detalhe. Um ponto de partida neutro. |
| **Air** | Abre bem o topo para um som arejado e aberto. |
| **Bright** | Um reforço forte para um tom nítido, brilhante e à frente. |
| **Soften** | Um corte modesto para tirar a borda de agudos ásperos. |
| **Tame Highs** | Um corte forte para escurecer e suavizar um som brilhante demais. |
| **Sparkle** | Um grande reforço no topo para brilho e cintilação máximos. |

### Soft Clip (saturação quente)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Drive** | Empurra o sinal com mais força no waveshaper. Quantidades baixas adicionam calor suave; quantidades altas arredondam os picos em saturação espessa e aspereza. | 0 a 40 dB (0) |

| Preset | O que faz |
|---|---|
| **Warm** | Um toque de drive para um calor suave, estilo analógico. |
| **Drive** | Saturação perceptível que engrossa e colore o som. |
| **Crunch** | Drive pesado com uma borda crocante audível. |
| **Fuzz** | Distorção espessa e difusa. Os picos são esmagados com força. |
| **Destroy** | Drive máximo. Aspereza agressiva e totalmente saturada. |

### Bit Crusher (lo-fi retrô)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Bit depth** | Define quantos bits descrevem cada amostra. Menos bits significam passos mais grosseiros e mais ruído de quantização, para um som digital áspero e crocante. | 1 a 16 bits (16) |
| **Sample rate** | Reduz a taxa de amostragem do áudio. A cem por cento a taxa fica intocada; abaixe-a para manter cada amostra por mais tempo, abafando os agudos e adicionando uma borda áspera e com aliasing. | 1% a 100% (100%) |

| Preset | O que faz |
|---|---|
| **Vintage** | Uma queda sutil de qualidade, como um sampler digital antigo. |
| **LoFi** | Lo-fi clássico de 8 bits e meia taxa. Granulado e retrô. |
| **Crunch** | Esmagamento mais pesado com uma borda crocante audível. |
| **Gritty** | Grosseiro e áspero. Os passos entre os níveis são óbvios. |
| **Destroy** | Redução extrema. Áspero, quebrado, quase irreconhecível. |

### Ring Modulator (tons metálicos e robóticos)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Carrier** | Define a frequência do tom pelo qual o sinal é multiplicado. Poucos hertz dão uma oscilação de tremolo; frequências mais altas adicionam harmônicos metálicos, tipo sino e robóticos. | 1 a 4000 Hz (440) |
| **Mix** | Mistura o som modulado com o original. A zero por cento você ouve apenas o sinal seco; a cem por cento apenas o tom totalmente modulado. | 0% a 100% (0%) |

| Preset | O que faz |
|---|---|
| **Tremolo** | Um carrier muito baixo o transforma em um tremolo de amplitude, oscilando o volume. |
| **Robot** | Um carrier médio adiciona harmônicos metálicos para um clássico efeito de voz de robô. |
| **Metallic** | Harmônicos densos e inharmônicos para um tom áspero e metálico. |
| **Bell** | Um carrier mais alto dá um tinido brilhante, tipo sino. |
| **Alien** | Totalmente molhado com um carrier alto. Extremo, alienígena, quase irreconhecível. |

### Tremolo (oscilação de volume)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Rate** | Define com que rapidez o volume pulsa. Taxas mais lentas dão um balanço suave; taxas mais rápidas dão um tremular rápido. | 0,1 a 20 Hz (5) |
| **Depth** | Define quanto o volume cai a cada pulso. A zero por cento o nível é estável; a cem por cento ele mergulha até o silêncio. | 0% a 100% (0%) |

| Preset | O que faz |
|---|---|
| **Gentle** | Um balanço lento e raso. Movimento sutil sem chamar atenção. |
| **Classic** | O clássico tremolo de amplificador: uma taxa média e profundidade moderada. |
| **Deep** | Um pulso forte e profundo que quase cai ao silêncio a cada ciclo. |
| **Fast** | Um tremular rápido para uma sensação cintilante e nervosa. |
| **Chop** | Rápido e com profundidade total. Um corte duro e entrecortado. |

### Delay (echo)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Time** | Define a pausa antes de cada eco. Tempos curtos dão um slapback apertado; tempos mais longos espaçam mais as repetições. | 0,01 a 2 s (0,25) |
| **Feedback** | Define quanto de cada eco é realimentado. Valores baixos dão uma única repetição; valores mais altos constroem uma série longa e prolongada de ecos. | 0 a 0,95 (0,4) |
| **Mix** | Mistura os ecos com o original. A zero por cento você ouve apenas o sinal seco; a cem por cento apenas os ecos. | 0% a 100% (0%) |

| Preset | O que faz |
|---|---|
| **Slapback** | Um único eco curto, apertado contra o original. Rockabilly e duplicação vocal. |
| **Echo** | O echo clássico: uma repetição clara com algumas caudas prolongadas. |
| **Ping** | Uma repetição rápida e saltitante que adiciona movimento rítmico. |
| **Ambient** | Repetições mais longas e suaves que se dissolvem em uma cauda espaçosa. |
| **Dub** | Feedback alto para longas cascatas dubby de eco. |
| **Cavern** | Repetições longas e profundas, como som ecoando por um espaço enorme. |

### Stereo Width (estreite ou amplie)

| Controle | O que faz | Faixa (padrão) |
|---|---|---|
| **Width** | Estreita ou amplia a imagem estéreo. Zero por cento colapsa para mono, cem por cento a deixa intocada, e valores mais altos empurram os lados para fora. Só afeta faixas estéreo no alvo de todos os canais. | 0% a 200% (100%) |

| Preset | O que faz |
|---|---|
| **Wide** | Uma ampliação suave que abre a imagem estéreo. Um ponto de partida neutro. |
| **Wider** | Uma dispersão mais forte para um campo estéreo grande e imersivo. |
| **Max** | Largura máxima. Muito ampla, mas cuidado com problemas de compatibilidade mono. |
| **Narrow** | Puxa os lados para dentro para uma imagem mais apertada e centrada. |
| **Focused** | Quase centrado, com apenas uma pitada de estéreo. |
| **Mono** | Totalmente colapsado para mono. Ambos os alto-falantes reproduzem o mesmo sinal. |

## Como tudo funciona por baixo dos panos (versão simples)

- **Motores:** você escolhe um em Configurações > Reprodutor de áudio > Motor de reprodução: **Standard** (sistema), **Universal** (FFmpeg) ou **Sound FX** (o **motor BASS™** da [Un4seen Developments](https://www.un4seen.com/)). O motor escolhido decide quais formatos são reproduzidos, e os efeitos, o equalizador e a cadeia DSP funcionam apenas no motor Sound FX.
- **Formatos:** o motor BASS™ adiciona FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus e música de módulo (tracker) além dos formatos do sistema e do FFmpeg.
- **Efeitos:** o equalizador, o compressor e a maioria dos efeitos usam os add-ons de efeitos do BASS™. O Freeverb é o reverb Freeverb. Chorus, Flanger e Distortion usam efeitos clássicos estilo DirectX com seus próprios controles.
- **Normalização de volume:** um nivelador de loudness **EBU R128** ao vivo (o padrão de loudness usado em broadcast e streaming).
- **Crossfeed:** o crossfeed **bs2b (Bauer)**, executado dentro do motor BASS™.
- **Cadeia DSP:** seus blocos personalizados, aplicados na ordem exata que você define, em todos os canais ou apenas um lado.
- **Saída:** você pode definir a taxa de amostragem, a contagem de canais e o tamanho do buffer para combinar com seu equipamento.

Como tudo isso é executado ao vivo enquanto a música toca, os efeitos:

- Funcionam em **tempo real** em tudo, incluindo arquivos na nuvem, transmissões e música de módulo.
- **Nunca alteram nem re-salvam** seus arquivos. Desligue um efeito e o original retorna.
- **Lembram seus ajustes** de cada efeito.
- Podem ser **combinados livremente**, já que cada um é separado.

## Receitas simples para experimentar

**Audição do dia a dia**

- **Mais graves, com limpeza:** Equalizador > Bass Booster, depois abaixe o Pré-amplificador 1 a 2 dB. Ou adicione um Low Shelf DSP em Bass Boost.
- **Volume uniforme em uma playlist mista:** Normalização de volume > Standard, mais Compressor > Soft.
- **Polimento geral suave:** Compressor > Transparent, mais Normalização de volume > Light.
- **Vocais mais claros:** Equalizador > Vocal Booster, ou um bloco Peaking DSP em Vocal Boost.
- **Som mais cheio em alto-falantes pequenos de telefone:** Equalizador > Small Speakers.

**Fones de ouvido**

- **Mais agradável e menos cansativo em fones de ouvido:** Crossfeed > Chu Moy ou Jan Meier.
- **Som mais amplo em fones de ouvido:** Stereo Width DSP > Wide, mais Crossfeed > Chu Moy.
- **Corrigir discos dos anos 1960 e 1970 com panorâmica extrema:** Crossfeed > Vintage Stereo.
- **Um pouco de ar e espaço:** Freeverb > Ambience, mantido baixo, mais Crossfeed > Subtle.

**Momentos calmos e áudio falado**

- **Audição noturna e silenciosa:** Normalização de volume > Night, mais Compressor > Late Night.
- **Podcasts e audiolivros:** Compressor > Voice / Podcast, mais Equalizador > Spoken Word.
- **Som mais alto e mais uniforme em um carro barulhento:** Normalização de volume > Strong, mais Compressor > Heavy.

**Corrigindo problemas**

- **Domar uma gravação áspera e brilhante:** Equalizador > Treble Reducer, ou um bloco Peaking DSP em Tame Harsh.
- **Remover zumbido elétrico:** cadeia DSP > Notch > Mains Hum 60 (ou Mains Hum 50 na Europa).
- **Graves mais apertados e limpos:** DSP High Pass > Tighten, para cortar os graves com muita ressonância.
- **Menos ressonância em uma mixagem pesada de graves:** DSP Low Shelf > Trim Bass, ou Peaking > De-Boom.

**Criativo e divertido**

- **Sensação quente e espaçosa:** Freeverb > Hall, mantido baixo.
- **Guitarras sonhadoras e espaçosas:** Chorus > Wide, mais Echo > Long.
- **Lo-fi retrô:** cadeia DSP > Bit Crusher (LoFi) em Soft Clip (Warm).
- **Movimento funky em faixas eletrônicas:** Auto Wah > Funky, ou Phaser > Fast.
- **Clássico sopro de avião a jato:** Flanger > Jet.

## Perguntas frequentes

{{% details title="Que motor de som o Flacbox usa?" closed="true" %}}
Você escolhe um Motor de reprodução em Configurações > Reprodutor de áudio: Standard (o motor de sistema da Apple), Universal (o motor FFmpeg) ou Sound FX (o motor BASS™ da Un4seen Developments, un4seen.com). O motor que você escolhe decide quais formatos de arquivo são reproduzidos. O Sound FX é o que reproduz formatos extras como FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus e música MOD ou de tracker, e é o único motor que fornece os efeitos ao vivo, o equalizador de 10 bandas e a cadeia DSP. Para usar os efeitos, defina o Motor de reprodução como Sound FX.
{{% /details %}}

{{% details title="O Flacbox pode reproduzir MOD, XM, IT e outras músicas de tracker ou módulo?" closed="true" %}}
Sim. O motor BASS™ tem um reprodutor de módulos integrado que carrega arquivos MOD, XM, IT, S3M, MTM, UMX e MO3 e reconstrói a música ao vivo a partir de seus padrões e sons de instrumentos, da maneira como a música de tracker deve ser tocada. Reprodutores comuns de iPhone não conseguem fazer isso. Os efeitos e o equalizador também funcionam na música de módulo.
{{% /details %}}

{{% details title="O Flacbox suporta arquivos DSD e de alta resolução?" closed="true" %}}
Sim. O Flacbox reproduz arquivos DSD (DSF e DFF) através do motor BASS™ usando DSD sobre PCM para que funcionem em hardware de saída normal, além de FLAC, WavPack, Monkey's Audio (APE), Musepack e TrueAudio para reprodução lossless.
{{% /details %}}

{{% details title="Que efeitos sonoros o Flacbox tem?" closed="true" %}}
Um equalizador de 10 bandas, Normalização de volume, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate e Crossfeed, além de uma cadeia DSP que você mesmo monta, com filtros, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay e stereo width. Cada um é separado e pode ser combinado com os outros.
{{% /details %}}

{{% details title="O que é um preset?" closed="true" %}}
Um preset é um ajuste pronto para um efeito. Em vez de mover os sliders você mesmo, você toca em um preset e o som muda para combinar. Todo efeito no Flacbox tem vários presets, e este guia lista o que cada um faz. Se você mover um slider depois de escolher um preset, o efeito mostra «Manual» para avisar que agora está usando seus próprios valores.
{{% /details %}}

{{% details title="Como abro os efeitos de áudio no Flacbox?" closed="true" %}}
Abra o reprodutor Reproduzindo agora, toque no botão ⋯ (Mais) e escolha Efeitos de áudio. Ou vá em Configurações > Reprodutor de áudio > Efeitos de áudio. Toque em um efeito, ligue seu botão e escolha um preset, ou abra os sliders para o ajuste fino.
{{% /details %}}

{{% details title="Onde está o equalizador, e quais são os melhores ajustes?" closed="true" %}}
Vá em Configurações > Reprodutor de áudio > Equalizador de áudio. Ele tem 10 bandas de 32 Hz a 16 kHz, cada uma de -12 a +12 dB, mais um Pré-amplificador de -24 a +24 dB e 22 presets. Para mais graves, use Bass Booster. Para vozes mais claras, use Vocal Booster ou Pop. Para um som mais brilhante, use Treble Booster. Depois ajuste bandas individuais a gosto.
{{% /details %}}

{{% details title="Como reforço os graves no Flacbox?" closed="true" %}}
Duas maneiras fáceis. No Equalizador de áudio, escolha Bass Booster (ou eleve as bandas de 32 Hz e 64 Hz alguns dB). Ou, no Processamento de sinal, adicione um bloco Low Shelf definido para Bass Boost. Em ambos os casos, abaixe o Pré-amplificador ou adicione um bloco Gain de 1 a 2 dB para que os graves fiquem limpos e não distorçam.
{{% /details %}}

{{% details title="Qual preset de equalizador é melhor para a minha música?" closed="true" %}}
Rock e Electronic adicionam energia com graves e agudos fortes. Acoustic, Jazz e Classical permanecem quentes e naturais. Pop e Vocal Booster trazem as vozes à frente. Bass Booster e Hip-Hop adicionam peso. Deep e Loudness soam mais cheios em volume baixo. Comece com o que combina com seu gênero, depois faça o ajuste fino.
{{% /details %}}

{{% details title="O que é a Normalização de volume, e como ela é diferente do ReplayGain?" closed="true" %}}
Ela faz cada faixa tocar aproximadamente no mesmo loudness. Mede o loudness real usando o padrão EBU R128 (em LUFS, como os serviços de streaming) e ajusta cada faixa em direção ao seu alvo, com um limite de max boost. Ao contrário do ReplayGain, ela não precisa de tags em seus arquivos e funciona em qualquer fonte, ao vivo, sem alterar o áudio. Presets: Light, Standard, Strong e Night.
{{% /details %}}

{{% details title="O que é o Crossfeed, e devo usá-lo?" closed="true" %}}
O Crossfeed mistura um pouco dos canais esquerdo e direito para que os fones de ouvido pareçam mais com alto-falantes reais e menos como se o som estivesse preso na sua cabeça. É só para fones de ouvido, então desligue-o para alto-falantes. O Flacbox usa o método bs2b (Bauer), com presets como Chu Moy e Jan Meier.
{{% /details %}}

{{% details title="Qual é a diferença entre o Compressor e a Normalização de volume?" closed="true" %}}
A Normalização de volume iguala o loudness entre músicas diferentes. O Compressor nivela as partes altas e baixas dentro de uma única música. Eles resolvem problemas diferentes e funcionam bem juntos, especialmente em um carro ou em um lugar barulhento.
{{% /details %}}

{{% details title="O que é a cadeia de Processamento de sinal (DSP)?" closed="true" %}}
É um rack que você mesmo monta em Configurações > Reprodutor de áudio > Processamento de sinal. Adicione blocos como filtros, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay e stereo width, coloque-os em qualquer ordem, ligue ou desligue cada um, e aponte a cadeia para todos os canais, esquerdo ou direito. Como a ordem importa, você pode projetar exatamente o som que quer.
{{% /details %}}

{{% details title="Qual é a diferença entre o Equalizador, os efeitos e a cadeia DSP?" closed="true" %}}
O Equalizador é um controle de tom simples de 10 bandas. Os Efeitos de áudio são ferramentas prontas (compressor, reverb, echo e assim por diante) com presets. A cadeia DSP é onde você monta sua própria ordem de efeitos a partir de blocos individuais. Você pode executar os três ao mesmo tempo.
{{% /details %}}

{{% details title="Os efeitos alteram ou danificam meus arquivos de música?" closed="true" %}}
Não. Tudo é aplicado ao vivo enquanto a música toca. Seus arquivos nunca são alterados nem re-salvos. Desligue um efeito e o som original retorna imediatamente.
{{% /details %}}

{{% details title="Posso usar mais de um efeito ao mesmo tempo?" closed="true" %}}
Sim. Cada efeito tem seu próprio botão e não há botão mestre, então qualquer combinação funciona. Por exemplo, Normalização de volume mais Compressor para uma audição uniforme, ou Freeverb mais Crossfeed em fones de ouvido, com o equalizador por cima.
{{% /details %}}

{{% details title="Por que os controles do efeito estão esmaecidos?" closed="true" %}}
O efeito está desligado. Ligue seu botão no topo do editor para usar os controles. Todo efeito começa desligado por padrão.
{{% /details %}}

{{% details title="O que significa a etiqueta Manual?" closed="true" %}}
Significa que você moveu um slider para longe de um preset, então o efeito agora está usando seus próprios valores personalizados em vez de um preset nomeado. Cada slider tem um botão de reset, e escolher um preset novamente substitui seus valores manuais.
{{% /details %}}

{{% details title="Posso salvar e compartilhar meus presets de equalizador?" closed="true" %}}
Sim. Além dos 22 presets integrados, você pode criar os seus, reordená-los e exportá-los ou importá-los para mover seus ajustes para outro dispositivo.
{{% /details %}}

{{% details title="Os efeitos funcionam com CarPlay, streaming e reprodução em segundo plano?" closed="true" %}}
Sim. Os efeitos são executados dentro do motor BASS™, então se aplicam a arquivos locais, drives na nuvem, servidores de mídia, transmissões e música de módulo, e continuam funcionando durante o CarPlay e a reprodução em segundo plano.
{{% /details %}}

{{% details title="Posso mudar a qualidade da saída de áudio?" closed="true" %}}
Sim. Em Configurações > Reprodutor de áudio você pode definir a taxa de amostragem de saída, o número de canais e o tamanho do buffer para combinar com seus fones de ouvido, alto-falantes ou DAC.
{{% /details %}}

{{% details title="Qual é uma boa configuração inicial para fones de ouvido?" closed="true" %}}
Ligue a Normalização de volume (Standard), adicione um Compressor leve (Soft), escolha um preset de equalizador que você goste e ligue o Crossfeed (Chu Moy ou Jan Meier). Deixe reverb, echo e distortion desligados a menos que você queira um som criativo.
{{% /details %}}

---

*BASS é uma marca registrada da Un4seen Developments Ltd. Veja [un4seen.com](https://www.un4seen.com/). O Crossfeed usa o algoritmo bs2b (Bauer stereophonic-to-binaural); veja a [página do projeto bs2b](https://bs2b.sourceforge.net/).*
