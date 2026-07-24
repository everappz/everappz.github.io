---
title: "Como ativar um visualizador de música enquanto reproduz música no iPhone, iPad e Mac"
date: 2026-07-24
description: "Um guia completo para usar um visualizador de música enquanto você reproduz música no iPhone, iPad e Mac. Aprenda como ativá-lo no Evermusic e no Flacbox, como os visuais Milkdrop (projectM) em tempo real reagem à sua música, os controles na tela, como mudar de preset ou usar o modo Auto, e como ele funciona no iOS e no macOS com OpenGL e 500 presets."
keywords: ["visualizador de música iPhone", "visualizador de música iPad", "visualizador de música Mac", "visualizador enquanto reproduz música", "como ativar visualizador de música", "ativar visualizador iPhone", "visualizador Evermusic", "visualizador Flacbox", "Milkdrop iOS", "projectM iOS", "presets Milkdrop", "app de visualizador de áudio", "500 presets de visualizador", "visualizador de música OpenGL", "alternativa ao visualizador do iTunes", "visuais de música psicodélicos iPhone", "visualizador de espectro iOS", "visualizador de música em tela cheia"]
tags: ["Evermusic", "Flacbox", "Visualizador", "Como fazer", "Milkdrop", "projectM", "OpenGL", "iOS", "macOS", "Presets", "Reprodutor de música"]
readingTime: 9
---

{{< author-byline >}}

**Resposta curta:** O [Evermusic](/products/evermusic) e o [Flacbox](/products/flacbox) têm ambos um **visualizador de música** em tela cheia que pinta visuais coloridos em movimento no ritmo da sua música. Abra-o pelo reprodutor **Reproduzindo agora** (**⋯ Mais > Visualização**) ou por **Configurações > Visualização**, depois escolha um preset ou **Auto** e toque em **Iniciar visualização**. Na tela do visualizador, toque uma vez para mostrar ou ocultar os controles e use as setas **Anterior** e **Próximo** para mudar o visual. Ele usa o conhecido motor **Milkdrop (projectM)** com **500 presets**, renderiza com **OpenGL** e funciona no **iPhone, iPad e Mac**. Os passos são os mesmos nos dois apps. Os passos completos estão abaixo.

{{< cards cols="1">}}
{{< card title="" subtitle="Visualizador de música: preset Starfield Sectors" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" imageStyle="border-radius: clamp(14px, 2vw, 28px);" >}}
{{< /cards >}}

## O que é o visualizador?

O visualizador é um espetáculo de luzes em movimento que reage à sua música em tempo real. Enquanto a música toca, o som comanda as formas, cores e o movimento na tela, então os momentos calmos parecem tranquilos e os momentos altos explodem de energia. É ótimo em uma tela grande, em um Mac, ou apenas para apreciar a música de um jeito novo. O mesmo visualizador está integrado tanto no **Evermusic** quanto no **Flacbox**, e funciona da mesma maneira em cada um.

Por baixo dos panos, ele usa **presets estilo Milkdrop** através do motor de código aberto **projectM**, a mesma família de visuais que muitas pessoas lembram dos reprodutores de música de desktop. Cada preset é uma cena animada diferente, e o app vem com **500 deles**. Os visuais são desenhados com **OpenGL** para uma animação suave e acelerada por GPU.

## Como ativar o visualizador

Há duas maneiras de abri-lo, e elas são as mesmas no Evermusic e no Flacbox.

**Pelo reprodutor (mais rápido):**

1. Abra a tela do reprodutor **Reproduzindo agora**.
2. Toque no botão **⋯ (Mais)**.
3. Toque em **Visualização**.

**Pelas Configurações:**

1. Vá para a aba **Configurações**.
2. Toque em **Visualização**.

De qualquer forma, você chega ao **seletor de presets**.

## O seletor de presets

O seletor de presets é uma lista simples onde você escolhe como o visualizador começa:

- **Auto** fica no topo da lista. Escolha-o para deixar o app embaralhar os presets por conta própria, mudando para um novo a cada **30 segundos** com um suave **crossfade**. Esta é a maneira mais fácil de apreciar o espetáculo sem tocar em nada.
- **Qualquer preset nomeado** (a lista está ordenada por nome) inicia o visualizador com aquele visual exato. O preset que você usou por último é lembrado e destacado, então é fácil encontrá-lo de novo.

Depois de fazer sua escolha, toque em **Iniciar visualização** e o espetáculo em tela cheia começa. Como o app diz: *«Selecione um preset para começar com ele, ou use o modo Auto que embaralha os presets, mudando a cada 30 segundos com um suave crossfade.»*

## Os controles na tela do visualizador

O visualizador funciona em tela cheia para que nada atrapalhe os visuais. **Toque em qualquer lugar uma vez** para abrir os controles, e toque de novo (ou apenas espere alguns segundos) para ocultá-los e obter uma imagem limpa em tela cheia.

Quando os controles estão visíveis, você verá:

- **Título do preset e contador (centro superior).** O nome do preset atual, com um contador embaixo, como **429 / 500**, para que você sempre saiba qual está vendo e quantos existem. Na captura de tela acima, o preset atual é **Starfield Sectors**.
- **Setas Anterior e Próximo (embaixo).** Toque em **Próximo (>)** para pular para o próximo visual, ou **Anterior (<)** para voltar. Isso permite folhear os presets manualmente até encontrar um que você adore.
- **Botão Fechar (canto superior).** Toque nele para sair do visualizador e voltar ao app.

A tela também **permanece acesa** enquanto o visualizador está ligado, então ela não vai escurecer nem bloquear no meio do espetáculo.

## Como mudar o preset

Você tem duas maneiras fáceis de mudar o visual:

1. **Manualmente.** Toque na tela para mostrar os controles, depois use as setas **Anterior** e **Próximo** para percorrer os presets um de cada vez. O título e o contador no topo se atualizam conforme você avança, e o app lembra o último preset em que você parou para a próxima vez.
2. **Automaticamente.** Inicie o visualizador no modo **Auto** (pelo seletor de presets). O app então embaralha os presets para você, mudando a cada **30 segundos** com um suave crossfade, para que o espetáculo continue mudando por conta própria.

## iPhone, iPad e Mac

O visualizador funciona tanto no Evermusic quanto no Flacbox, no **iOS e no macOS**:

- **No iPhone e no iPad**, ele preenche a tela e é desenhado com **OpenGL ES**, então permanece suave mesmo em uma tela Retina.
- **No Mac**, o app abre o visualizador em sua própria janela e o desenha com **OpenGL de desktop** nativo, então você obtém os mesmos visuais Milkdrop reativos na tela grande.

De qualquer forma, os visuais reagem exatamente ao áudio que você está reproduzindo, seja um arquivo FLAC local, uma faixa de um drive na nuvem ou servidor de mídia, ou uma transmissão de rádio pela internet.

## Dicas

- **Toque uma vez para ocultar os controles** para uma imagem limpa em tela cheia, depois toque de novo para trazê-los de volta.
- **Experimente o modo Auto** na primeira vez, depois mude para escolher presets manualmente quando encontrar estilos que você goste.
- **O contador (como 429 / 500)** ajuda você a lembrar dos favoritos, para que possa voltar a um preset de que gostou.
- **Mantenha a reprodução.** Os visuais seguem a música, então quanto mais dinâmica a faixa, mais a cena se move.
- **No Mac**, redimensione a janela do visualizador para caber na sua tela ou em uma segunda tela.

## Perguntas frequentes

{{% details title="Como ativo o visualizador no Evermusic ou no Flacbox?" closed="true" %}}
Abra o reprodutor Reproduzindo agora, toque no botão ⋯ (Mais) e escolha Visualização. Você também pode abri-lo em Configurações > Visualização. Depois escolha um preset (ou Auto) e toque em Iniciar visualização. Os passos são os mesmos nos dois apps.
{{% /details %}}

{{% details title="Em que o visualizador é baseado?" closed="true" %}}
Ele usa o motor de código aberto projectM, que reproduz presets estilo Milkdrop. Estes são os visuais animados e reativos à música que muitas pessoas conhecem dos reprodutores de música de desktop. Tanto o Evermusic quanto o Flacbox incluem 500 presets e os desenham com OpenGL.
{{% /details %}}

{{% details title="Quantos presets de visualizador existem?" closed="true" %}}
500 presets. Cada um é uma cena animada diferente, e você pode percorrê-los com as setas Próximo e Anterior, ou deixar o modo Auto embaralhá-los para você.
{{% /details %}}

{{% details title="O visualizador reage à música?" closed="true" %}}
Sim. Os visuais respondem ao áudio que você está reproduzindo em tempo real, então as formas, cores e o movimento mudam com a batida e a energia da faixa. Funciona com arquivos locais, drives na nuvem, servidores de mídia e rádio pela internet.
{{% /details %}}

{{% details title="Como mudo o preset do visualizador?" closed="true" %}}
Toque na tela uma vez para mostrar os controles, depois use as setas Anterior e Próximo embaixo para navegar entre os presets. O nome e o contador no topo (por exemplo, 429 / 500) se atualizam conforme você os muda. Você também pode iniciar no modo Auto para que o app mude os presets automaticamente.
{{% /details %}}

{{% details title="O que é o modo Auto?" closed="true" %}}
O modo Auto, escolhido pelo seletor de presets, embaralha os presets por conta própria, mudando para um novo a cada 30 segundos com um suave crossfade. É a maneira mais fácil de apreciar o espetáculo sem tocar na tela.
{{% /details %}}

{{% details title="Como oculto os controles na tela?" closed="true" %}}
Toque na tela uma vez para ocultar os controles e ter uma visão limpa em tela cheia, e toque de novo para trazê-los de volta. Os controles também se ocultam sozinhos após alguns segundos.
{{% /details %}}

{{% details title="O visualizador funciona no Mac?" closed="true" %}}
Sim. No Mac, tanto o Evermusic quanto o Flacbox abrem o visualizador em sua própria janela e o desenham com OpenGL de desktop nativo, então você obtém os mesmos visuais Milkdrop reativos à música em uma tela grande.
{{% /details %}}

{{% details title="O visualizador funciona no iPhone e no iPad?" closed="true" %}}
Sim. No iPhone e no iPad ele funciona em tela cheia, desenhado com OpenGL ES para uma animação suave em telas Retina.
{{% /details %}}

{{% details title="Minha tela vai escurecer ou bloquear enquanto o visualizador está funcionando?" closed="true" %}}
Não. O app mantém a tela acesa enquanto o visualizador está ligado, então o espetáculo não será interrompido pelo escurecimento ou bloqueio da tela.
{{% /details %}}

{{% details title="O app lembra o preset que eu escolhi?" closed="true" %}}
Sim. O último preset que você selecionou é salvo e destacado no seletor de presets, então é fácil voltar ao seu favorito.
{{% /details %}}

{{% details title="Onde aparece o nome do preset atual?" closed="true" %}}
No centro superior da tela do visualizador, junto com um contador como 429 / 500 que mostra em qual preset você está do conjunto completo. No exemplo da captura de tela, o preset é Starfield Sectors.
{{% /details %}}
