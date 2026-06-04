---
title: "Leitor de Áudio"
date: 2020-02-01
description: "Aprenda a usar o leitor de áudio do Flacbox no iPhone, iPad e Mac. Controle a reprodução, gira filas, configure o motor de áudio FFmpeg / sistema, altere a taxa de amostragem, correção de tom, duração do buffer IO, equalizador, marcadores de áudio, AirPlay 2, Google Cast, CarPlay, widgets e atalhos de teclado do Mac."
keywords: [
  "guia leitor Flacbox", "definições leitor áudio", "equalizador Flacbox",
  "streaming música AirPlay", "Google Cast música", "marcadores áudio",
  "fila reprodução Flacbox", "repetir aleatório Flacbox", "controlo volume Flacbox",
  "mini leitor macOS", "aplicação música VoiceOver",
  "Flacbox FFmpeg", "correção tom Flacbox", "taxa amostragem Flacbox",
  "DAC externo Flacbox", "som surround Flacbox", "buffer IO Flacbox",
  "velocidade reprodução Flacbox", "temporizador sono Flacbox"
]
tags: ["guia", "flacbox", "leitor"]
readingTime: 14
---


O Leitor de Áudio é o ecrã principal da aplicação onde controla a música e a maioria das funcionalidades de reprodução. É também aqui que o motor de áudio hi-res do Flacbox — construído nos codecs do sistema mais a biblioteca **FFmpeg** incluída — faz o trabalho pesado. Vamos explorar como utilizá-lo.

## Aceder ao Leitor de Áudio

Pode aceder ao leitor em ecrã completo a partir da barra do mini leitor. No iPhone, o mini leitor fica na parte inferior do ecrã principal. No iPad e Mac, fica no lado esquerdo. Para ocultar o mini leitor no iPhone, toque nele uma vez e deslize para baixo. Para fechar completamente o leitor em ecrã completo, toque no botão de fechar no canto inferior direito.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player Main Screen" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Formatos de Áudio Suportados

O Flacbox reproduz os formatos de áudio mais populares — tanto os codecs do sistema da Apple como muitos formatos adicionais tratados pelo motor FFmpeg incluído:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Isso cobre virtualmente todos os formatos modernos com e sem perdas que poderá ter na sua coleção musical pessoal.

## Controlos de Reprodução

Na parte inferior do ecrã do leitor, verá botões para Reproduzir, Pausar, Faixa Seguinte e Faixa Anterior. Existem também botões opcionais como Próximos 30 seg. e Anteriores 30 seg. que pode ativar nas definições da aplicação (útil para audiolivros). Pode avançar ou retroceder rápido mantendo premidos os botões Seguinte / Anterior. Para saltar para uma parte específica de uma faixa, arraste o cursor de reprodução.

## Repetir e Aleatório

Toque no botão de repetir para alternar entre os modos de repetição:

- **Repetir Tudo** — repete em ciclo todas as faixas da sua fila.
- **Repetir Uma** — repete apenas a faixa atual.
- **Parar na Faixa** — pausa quando a faixa atual termina.
- **Não Repetir** — reproduz a fila uma vez sem repetir.

Utilize o botão **Aleatório** para aleatorizar a ordem das faixas na fila.

## Controlo de Volume

Abra o ecrã de Definições de Áudio tocando no ícone de som sob os controlos de reprodução para aceder ao cursor de volume. Encontrará também aqui botões para **Google Cast** e **AirPlay** para poder mudar rapidamente a reprodução para outro dispositivo.

## Google Cast (Chromecast)

Para utilizadores do Google Cast, o ícone **Cast** aparece na parte inferior do leitor. Toque nele para escolher um dispositivo e começar a transmitir. Certifique-se de que o seu dispositivo e o recetor Google Cast estão na mesma rede Wi-Fi. Nota: nem todos os formatos de áudio são compatíveis com o Google Cast — alguns formatos hi-res podem precisar de ser transcodificados.

## AirPlay

Para AirPlay, procure o botão **AirPlay** na parte inferior do leitor. Toque nele e selecione um dispositivo para transmitir. O Flacbox suporta **AirPlay 2**, pelo que pode reproduzir em múltiplos HomePods, Apple TVs ou colunas compatíveis com AirPlay 2 em simultâneo.

## Equalizador de Áudio

O Flacbox inclui um **equalizador de 10 bandas** com predefinições estilo iPod. Toque em Equalizador na vista de volume e depois ligue-o no canto superior direito. Pode usar predefinições como Acústico e Reforço de Graves, ou ajustar cada banda de frequência com cursores. Crie as suas próprias predefinições, guarde-as com qualquer nome e aumente o volume geral com o pré-amplificador. Temos instruções mais detalhadas sobre como usar o equalizador [aqui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Barra de Ferramentas do Modo do Leitor

Para alguns estilos de leitor, existe uma barra de ferramentas dedicada no topo do leitor em ecrã completo. Esta barra de ferramentas aloja três botões úteis:

- **Pesquisar** — localizar rapidamente uma faixa específica na sua fila do leitor.
- **Controlo de Velocidade de Reprodução** — ajustar a velocidade de reprodução de 0,02× a 3,00×. Perfeito para audiolivros, podcasts e palestras. Toque em Normal para reverter para a velocidade predefinida.
- **Marcadores de Áudio** — criar múltiplos marcadores por faixa. Temos instruções completas sobre como usar marcadores [aqui](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Fila do Leitor

Para ver a sua fila do leitor, toque no botão de fila no lado direito da música atual. Cada música na fila tem mais ações — toque nos três pontos para as ver. Para reordenar uma música na fila, use o indicador de reordenar perto do título e arraste-o para uma nova posição.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playback Queue" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Comentários / Letras

Para ver comentários de faixas e letras incorporadas, bem como ficheiros LRC, siga estes passos:

1. Abra **Configurações**.
2. Vá a **Leitor de Áudio**.
3. Selecione **Personalização**.
4. Toque em **Botões no ecrã principal**.
5. Ative **Comentários**.

Depois, toque no botão de fila do leitor na parte inferior do ecrã várias vezes para mudar da vista de capa / fila para a vista de comentários. No ecrã de Comentários, deslize para a direita para alternar entre **Comentários**, **Letras Incorporadas** e o **Ficheiro LRC**. Instruções completas estão disponíveis [aqui](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lyrics and Comments Screen" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menu de Opções

Cada música na fila do leitor de áudio tem um menu com mais ações, acedido tocando no botão de três pontos perto do título da música.

- **Reproduzir Seguinte** — adiciona a música ao topo da fila do leitor.
- **Adicionar à Lista de Reprodução** — inclui a música numa lista de reprodução, com a opção de criar uma nova.
- **Adicionar aos Favoritos** — marca a música como favorita para acesso rápido.
- **Transferir** — guarda a música em ficheiros locais, aparecendo no separador **Ficheiros Locais** e na secção **Música Offline**.
- **Editar Tags de Áudio** — abre o editor de tags de áudio integrado para corrigir metadados em falta, modificando a música no seu armazenamento.
- **Mostrar na Pasta** — revela a pasta onde o ficheiro de áudio está armazenado.
- **Mostrar no Finder** — para ficheiros importados do seu Mac, revela a pasta onde o ficheiro de áudio está localizado no seu Mac.
- **Abrir Em** — exporta o ficheiro de áudio para outra aplicação.
- **Eliminar da Fila** — remove a música selecionada da fila do leitor de áudio.
- **Eliminar do Serviço de Nuvem** — elimina a música tanto da biblioteca musical como do armazenamento na nuvem. **Esta ação é irreversível.**
- **Eliminar dos Ficheiros Locais** — elimina a música tanto da biblioteca musical como do armazenamento local. **Esta ação é irreversível.**
- **Eliminar da Biblioteca Musical** — elimina a música da sua biblioteca musical, mantendo o ficheiro no armazenamento.

As mesmas opções estão disponíveis para o item em reprodução na fila do leitor de áudio, que pode aceder tocando no ícone **Mais Ações** perto do título da faixa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Options for an Item in the Playback Queue" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Ações Adicionais do Leitor

Toque no botão **Mais Ações** «...» no lado esquerdo do título da música em reprodução para ver ações adicionais.

- **Continuar Reprodução** — retomar de onde ficou, incluindo a fila e a posição nos media. Particularmente útil para audiolivros. Ativado nas definições da aplicação.
- **Pesquisar** — localizar rapidamente uma faixa específica na sua fila do leitor de áudio.
- **Marcadores** — ver a sua lista de marcadores de áudio criados.
- **Comentários** — ver comentários de faixas e letras incorporadas, bem como ficheiros LRC. Instruções completas [aqui](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Velocidade** — ajustar a velocidade de reprodução ao seu gosto.
- **Recentes** — aceder a uma lista de músicas reproduzidas recentemente.
- **Favoritos** — ver a sua coleção de músicas favoritas.
- **Equalizador de Áudio** — ativar o equalizador de áudio.
- **Temporizador de Sono** — definir um temporizador para parar a reprodução após um intervalo especificado. Ótimo para quando quer adormecer ao som da sua música.
- **Guardar Fila como Lista de Reprodução** — guardar a fila atual do leitor de áudio como uma nova lista de reprodução.
- **Eliminar Fila** — limpar a fila do leitor e parar a reprodução.
- **Configurações** — aceder às definições do leitor de áudio.
- **Ajuda** — encontrar assistência e orientação.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player More Actions Screen" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Marcadores de Áudio

Esta funcionalidade permite criar múltiplos marcadores para faixas na sua biblioteca musical — perfeito para audiolivros, palestras, longas sessões de DJ ou marcar o refrão de uma faixa favorita.

Para criar um novo marcador:

- Comece a reproduzir a música desejada.
- Abra o ecrã do leitor.
- Toque no botão **Marcadores** na barra de ferramentas do modo do leitor.
- Selecione **Adicionar Marcador**.
- Escolha o tempo do marcador e toque em **Concluído** no canto superior direito.

Editar marcadores para a faixa atual é fácil: toque em Editar no canto superior direito para entrar no modo de edição. Neste modo, pode reordenar marcadores, eliminá-los, ajustar o tempo do marcador e alterar os títulos dos marcadores. Instruções mais detalhadas sobre marcadores de áudio estão disponíveis [aqui](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Bookmarks Screen" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Recentes e Favoritos

No ecrã do leitor, toque nos três pontos para aceder a Recentes e Favoritos. Em ambas as secções, pode pesquisar músicas, reproduzir todas, aleatório em todas, exportar a lista e limpar a lista. Temos instruções detalhadas sobre como exportar listas de músicas [aqui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Ligue o iPhone ao seu carro via USB ou Apple CarPlay sem fios e o Flacbox aparece no ecrã inicial do CarPlay, pronto para reproduzir música em segurança enquanto conduz. A interface CarPlay inclui separadores dedicados para Biblioteca, Conexões, Ficheiros Locais e Configurações, com controlos de reprodução, aleatório, repetir, gestão de fila e o equalizador de áudio, tudo disponível sem pegar no telemóvel. Configure a experiência CarPlay nas Configurações → CarPlay — opções de ordenação, paginação, cor do gradiente dos ícones do menu, se as imagens são carregadas, e uma opção para pausar automaticamente a reprodução quando o CarPlay se liga.

[Leia o guia completo do CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox on Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgets do Ecrã Inicial (iPhone e iPad)

O Flacbox suporta widgets do Ecrã Inicial e do Ecrã de Bloqueio do iOS para que possa ver e controlar a reprodução de relance. Certifique-se de que os Widgets estão ativados em Configurações → Widgets → Ativar Widgets, depois prima longamente o Ecrã Inicial ou Ecrã de Bloqueio, toque em **+**, pesquise **Flacbox** e adicione um widget. O widget atualiza-se durante a reprodução para mostrar a capa, título e artista da faixa em reprodução.

## Janela do Mini Leitor (exclusivo Mac)

Os utilizadores de Mac podem usar um mini leitor compacto sempre no topo. Mova o cursor para o canto inferior direito da janela do Flacbox, redimensione-o para o seu tamanho mínimo e toque no botão de recolher. Mantenha-o no topo de qualquer outra janela selecionando Janela → Mostrar Janela Sempre no Topo na barra de menus — perfeito para manter os controlos de música visíveis enquanto trabalha noutra aplicação.

## Atalhos de Teclado (exclusivo Mac)

Para utilizadores de Mac, está disponível um menu de reprodução do sistema na barra de estado com atalhos de teclado. Por exemplo, carregue na barra de espaço para Reproduzir / Pausar. Também estão disponíveis atalhos para Parar, Música Seguinte, Música Anterior, Saltar Tempo, Repetir, Aleatório e Velocidade de Reprodução.

## Definições do Leitor de Áudio

Para aceder às definições, toque no botão Mais no ecrã do leitor e escolha Configurações. Aqui, encontrará várias secções listadas abaixo.

### Geral

Estas definições cobrem os aspetos fundamentais do leitor de áudio, incluindo a fila de reprodução, saída de áudio e guardar o estado do leitor.

- **Modo de Repetição** — escolha como o leitor de áudio se comporta quando uma faixa termina:
  - **Repetir Tudo** — repete todas as faixas na sua fila.
  - **Repetir Uma** — repete apenas a faixa atual.
  - **Parar na Faixa** — pausa a reprodução quando a faixa atual termina.
  - **Não Repetir** — permite que a sua fila seja reproduzida sem repetir.
- **Modo Aleatório** — aleatoriza a ordem das faixas na sua fila. Pode desativar ou ativar.
- **Codec de Áudio** — escolha o motor de áudio utilizado para reprodução:
  - **System Codec + FFmpeg** — prioriza o codec de áudio do sistema sempre que possível, melhorando compatibilidade e estabilidade. A correção de tom e os ajustes da taxa de amostragem de saída de áudio podem ser limitados neste modo.
  - **FFmpeg** — força o codec FFmpeg para todos os ficheiros de áudio, permitindo ajustar a correção de tom e a taxa de amostragem de saída de áudio.
- **Taxa de Amostragem de Saída de Áudio** — ajuste a taxa de amostragem de saída de áudio para otimizar a qualidade do som, especialmente útil com um DAC externo. Valores disponíveis: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** e **96 kHz**.
- **Número de Canais de Saída de Áudio** — para sistemas de áudio multicanal com um DAC externo, especifique o número de canais: **Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround** e **SDDS**.
- **Duração do Buffer IO de Saída de Áudio** — configure a duração do buffer de entrada / saída para reprodução de áudio. Um valor típico para minimizar a latência ao reproduzir áudio de alta resolução é cerca de **5 milissegundos (0,005 segundos)**. O tamanho de buffer aceitável depende do seu ambiente de hardware e software, por isso teste diferentes durações no seu dispositivo alvo e escolha a que melhor equilibra baixa latência e reprodução sem falhas.
- **Modo de Saída de Áudio (apenas iOS)** — configure o modo de saída de áudio misto para que o áudio do Flacbox se misture com outras aplicações. Instruções detalhadas estão [aqui](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Guardar Posição de Reprodução** — garante que a aplicação guarda e restaura a posição de reprodução para músicas na sua biblioteca musical.
- **Guardar Estado do Leitor de Áudio** — preserva o estado do seu leitor de áudio antes de fechar a aplicação. Para continuar a reprodução, toque em **Continuar Reprodução** no topo de qualquer pasta, álbum, artista ou género quando reabrir a aplicação. Também pode restaurar a reprodução para ficheiros individuais tocando na faixa específica.

Depois de ter ativado tanto **Guardar Posição de Reprodução** como **Guardar Estado do Leitor de Áudio**, abra qualquer pasta, álbum, artista ou género e verá um botão **Continuar Reprodução** no topo do ecrã juntamente com a última faixa guardada e posição. Toque nele para retomar exatamente onde ficou.

### Personalização

A personalização permite-lhe personalizar o aspeto do ecrã do leitor de áudio, alterar os controlos disponíveis no ecrã principal, ecrã de bloqueio e barra de estado, e configurar os controlos de salto de tempo.

- **Estilo do Ecrã do Leitor de Áudio** — configure o posicionamento dos elementos no ecrã do leitor de áudio.
- **Estilo de Deslocamento das Capas dos Álbuns** — configure o estilo de deslocamento preferido para as capas dos álbuns.
- **Elementos Adicionais** — ative elementos extra no ecrã do leitor de áudio. **Informações do Formato de Áudio** mostra as informações de áudio da faixa em reprodução acima da capa; **Cursor de Volume de Áudio** mostra o cursor de saída de áudio abaixo dos controlos de reprodução.
- **Ações do Ecrã Principal** — configure quais botões devem estar visíveis por predefinição no ecrã principal do leitor de áudio: **Modo de Repetição e Aleatório, Música Seguinte e Anterior, Saltar Tempo, Temporizador de Sono, Google Chromecast, AirPlay e Bluetooth, Equalizador de Áudio, Pesquisar, Marcadores, Velocidade, Adicionar Marcador, Adicionar aos Favoritos, Comentários** e mais.
- **Controlos de Reprodução no Ecrã de Bloqueio** — escolha quais controlos aparecem no ecrã de bloqueio. Valores possíveis: **Saltar Tempo, Adicionar Marcador, Adicionar aos Favoritos**.
- **Botões de Salto de Tempo** — escolha o intervalo de tempo para os botões de **Saltar Tempo**.

### Carregamento de Ficheiros

Durante o processo de carregamento de ficheiros, pode alterar o tipo de rede utilizado para carregar músicas. Opções disponíveis: **Wi-Fi**, **Wi-Fi e Dados Móveis**.

- **Tempo de Pré-carregamento** — defina o intervalo de tempo de buffering. Aumente este valor se tiver uma ligação de rede fraca.
- **Usar URL Direto** — quando ativado, é usado um URL direto para carregar a música se o servidor suportar. Isto pode acelerar o carregamento de músicas mas pode afetar a estabilidade da reprodução.

### Equalizador de Áudio

Personalize as definições do equalizador de áudio. Pode ler mais sobre como configurar o equalizador de áudio [aqui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocidade de Reprodução

Ajuste a velocidade de reprodução do leitor de áudio de **0,02× a 3,00×**. Toque no ícone de configuração no canto superior direito para mudar para **modo preciso** para ajustes mais finos.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playback Speed Screen" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Correção de Tom

Altere as definições de correção de tom usando os valores predefinidos. Também pode alternar entre valores predefinidos e modo preciso tocando no botão no canto superior direito. A correção de tom está disponível no caminho do codec FFmpeg, com um intervalo de **-1000 a +1000**.

### Cache de Reprodução

As músicas na fila do leitor de áudio são automaticamente transferidas para garantir uma reprodução suave. Se transferir manualmente ficheiros de áudio, pode desativar esta opção para evitar duplicados. Também pode configurar o tamanho da cache do leitor de áudio aqui.

### Temporizador de Sono

Ative um temporizador para parar automaticamente a reprodução após um período especificado — útil quando quer adormecer ao som da música. Toque no ícone de configuração no canto superior direito para o **modo preciso** com granularidade minuto a minuto.

## Acessibilidade

O Flacbox é totalmente acessível com **VoiceOver**. Cada componente tem uma etiqueta e descrição bem concebidas. Quando o VoiceOver está ativo, a aplicação muda para **Modo de Texto** para que apenas os elementos significativos sejam apresentados — melhorando a velocidade de navegação e a clareza. Também pode ativar o Modo de Texto em **Configurações → Acessibilidade → Modo de Texto**.

### Ajustar Cursores com VoiceOver

1. **Selecionar o cursor** — deslize para a esquerda ou direita até o VoiceOver o anunciar.
2. **Ajustar o valor** — toque duas vezes e segure o cursor, depois arraste para cima ou baixo para alterar o valor rapidamente. O VoiceOver anuncia o novo valor à medida que avança.

### Ajustar a Posição da Faixa numa Lista com VoiceOver

1. Toque no ícone do indicador de reordenar perto do título da faixa para lhe dar foco.
2. Toque duas vezes rapidamente no indicador de reordenar. No segundo toque, não levante o dedo — segure-o até ouvir um som indicando que a célula está pronta para ser movida.
3. Mova a célula para a sua nova posição.

Outros componentes funcionam como esperado, usando padrões VoiceOver fornecidos pelo sistema.
