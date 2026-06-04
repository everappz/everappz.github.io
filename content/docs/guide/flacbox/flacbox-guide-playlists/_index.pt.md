---
title: "Listas de Reprodução"
date: 2020-02-01
description: "Aprenda a criar, importar, gerir e personalizar listas de reprodução no Flacbox no iPhone, iPad e Mac. Crie listas a partir de ficheiros na nuvem e locais, importe M3U / M3U8 / CUE, reordene músicas, edite a capa, arquive em ZIP, exporte para M3U / CSV / TXT e use o modo offline."
keywords: [
  "Flacbox listas de reprodução", "importar lista M3U", "gestor de listas de reprodução",
  "criar lista de reprodução iPhone", "listas de áudio Flacbox",
  "imagem personalizada lista de reprodução", "eliminar músicas da lista de reprodução",
  "ordenar lista de reprodução Flacbox", "VoiceOver reordenar lista de reprodução",
  "Flacbox exportar M3U", "Flacbox exportar CSV", "arquivo lista de reprodução Flacbox",
  "modo offline lista de reprodução Flacbox", "importar CUE Flacbox", "músicas duplicadas Flacbox"
]
tags: ["guia", "flacbox", "listas-de-reproducao"]
readingTime: 7
---


Na secção de Listas de Reprodução, encontrará ferramentas úteis para gerir as suas coleções musicais. Esta área mostra todas as suas listas de reprodução num único local. No topo, existe um botão **«...»** na barra de navegação que abre um menu com diferentes opções de listas de reprodução, mais uma barra de ferramentas com ações rápidas como Pesquisar, Reproduzir Tudo e Misturar Tudo. Cada lista de reprodução também tem o seu próprio botão **«...»** ao lado do título, dando-lhe mais opções apenas para essa lista.

As listas de reprodução no Flacbox podem conter uma mistura de faixas online da nuvem, ficheiros descarregados offline e ficheiros locais do seu dispositivo — tudo numa lista — e reproduzem-se perfeitamente em conjunto.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playlists Main Screen" image="/docs/guide/flacbox/img/playlists-main.webp" >}}
{{< /cards >}}

## Criar uma Lista de Reprodução

Criar uma nova lista de reprodução é simples. Tem duas opções: toque no botão **+**, ou toque no botão **«...»** localizado no canto superior direito da barra de navegação e escolha Nova Lista de Reprodução. Dê à sua lista um nome significativo e depois toque em Guardar.

Isto aciona o diálogo Adicionar Músicas, onde pode selecionar manualmente as faixas que deseja incluir na sua nova lista. As faixas estão convenientemente categorizadas por tipo de fonte:

- **Biblioteca** — faixas já na sua biblioteca musical.
- **Ficheiros nesta Aplicação** — ficheiros de áudio na pasta Documentos da aplicação (descarregados do armazenamento na nuvem, importados via Wi-Fi Drive, ou adicionados através da Partilha de Ficheiros do Finder).
- **Ficheiros neste Dispositivo** — ficheiros de áudio localizados noutros locais do seu dispositivo, não nesta aplicação.
- **Conexões** — ficheiros online localizados nos seus serviços de armazenamento na nuvem ligados.

Por predefinição, pode adicionar uma única faixa a uma lista de reprodução apenas uma vez. Se quiser permitir duplicados, ative esta funcionalidade em Configurações → Biblioteca Musical → Listas de Reprodução → Duplicados numa Lista de Reprodução → Ativar.

## Importar Lista de Reprodução

No Flacbox, adicionámos a importação de ficheiros M3U / M3U8 / CUE para não ter de recriar listas de reprodução manualmente após mudar de outro leitor.

Primeiro, vá à secção de Listas de Reprodução. Depois, toque no botão Mais no canto superior direito. No menu, selecione Importar Lista de Reprodução.

No ecrã seguinte, escolha a localização do ficheiro. As opções suportadas incluem:

- Armazenamento na nuvem ligado
- Ficheiros na aplicação
- Ficheiros no seu dispositivo

Selecione o armazenamento na nuvem ligado e abra a pasta que contém o ficheiro da lista de reprodução. As extensões de ficheiro de lista de reprodução suportadas incluem M3U, M3U8 e CUE. Selecione o ficheiro da lista e toque em Concluído para confirmar a sua seleção.

A aplicação analisa o ficheiro da lista de reprodução, cria uma lista de faixas e localiza esses ficheiros no armazenamento para compilar uma lista de reprodução final, que é então importada para a biblioteca musical. Importante: o ficheiro M3U / CUE deve conter os caminhos corretos para os ficheiros de media, e os ficheiros devem realmente existir nesses caminhos no seu armazenamento. Leia mais sobre a importação de listas de reprodução [aqui](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Ecrã de Detalhes da Lista de Reprodução

Quando abre uma lista de reprodução, aparece o ecrã de Detalhes da Lista. Encontrará um botão **«...»** no canto superior direito com opções da lista, e três botões por baixo da capa: Pesquisar, Continuar Reprodução, Reproduzir Tudo e Misturar Tudo. Existe também uma caixa de verificação de Modo Offline para alternar a sincronização offline completa da lista.

- **Continuar Reprodução** — restaurar a última posição de reprodução guardada para esta lista de reprodução.
- **Pesquisar** — realizar uma pesquisa dentro da lista de reprodução atual.
- **Reproduzir Tudo** — adicionar todas as faixas da lista de reprodução atual à fila do leitor.
- **Misturar Tudo** — como **Reproduzir Tudo**, mas mistura as faixas antes de as adicionar à fila do leitor de áudio.
- **Modo Offline** — descarregar todas as faixas desta lista para ficheiros locais. Quaisquer novos itens adicionados à lista também são descarregados automaticamente.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playlist Detail Screen" image="/docs/guide/flacbox/img/playlist-details-screen.webp" >}}
{{< /cards >}}

## Mais Ações para uma Lista de Reprodução no Ecrã de Listas

Pode aceder a ações para uma lista de reprodução tocando no botão **«...»** perto do título da lista. Ações disponíveis:

- **Reproduzir Tudo** — adiciona as faixas da lista a uma nova fila do leitor.
- **Reproduzir Seguinte** — adiciona as faixas da lista ao topo da fila existente do leitor.
- **Reproduzir Mais Tarde** — adiciona as faixas da lista ao fundo da fila existente do leitor.
- **Editar Imagem** — alterar a capa da lista de reprodução.
- **Ativar Modo Offline** — ativar o modo offline para a lista de reprodução. Tanto as faixas existentes como as novas são descarregadas automaticamente. Leia mais sobre o modo offline [aqui](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Exportar Lista de Músicas** — exportar esta lista de reprodução para **M3U / M3U8 / CSV / TXT** conforme descrito [aqui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Adicionar ao Arquivo** — arquivar esta lista de reprodução (incluindo ficheiro m3u, capa do álbum e todas as faixas) num único ZIP conforme descrito [aqui](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to). Funcionalidade Premium.
- **Adicionar Músicas** — adicionar mais músicas à lista de reprodução atual.
- **Renomear** — renomear a lista de reprodução.
- **Eliminar Lista de Reprodução** — eliminar a lista de reprodução da biblioteca musical. **Esta ação não pode ser desfeita.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox More Actions for a Playlist on the Playlists Main Screen" image="/docs/guide/flacbox/img/more-actions-for-playlist-in-playlists-main-screen.webp" >}}
{{< /cards >}}

## Mais Ações para uma Lista de Reprodução no Ecrã de Detalhes

Pode aceder a ações para uma lista de reprodução tocando no botão **«...»** no canto superior direito. Ações disponíveis:

- **Selecionar** — ativar o modo de seleção de faixas, útil para eliminar múltiplas faixas da lista de reprodução ou alterar a sua ordem.
- **Reproduzir Seguinte** — adicionar as faixas da lista ao topo da fila existente do leitor.
- **Reproduzir Mais Tarde** — adicionar as faixas da lista ao fundo da fila existente do leitor.
- **Adicionar Músicas** — adicionar novas músicas à lista de reprodução.
- **Reorganizar Músicas** — alterar manualmente a ordem das músicas na lista de reprodução usando arrastar e largar.
- **Renomear** — renomear a lista de reprodução atual.
- **Editar Imagem** — alterar a capa do álbum para a lista de reprodução atual.
- **Exportar Lista de Músicas** — exportar esta lista de reprodução para **M3U / M3U8 / CSV / TXT**. Leia mais [aqui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Adicionar ao Arquivo** — comprimir a lista de reprodução atual incluindo todas as faixas e ficheiro m3u em ZIP. Leia mais [aqui](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Ordenar** — alterar a ordem das faixas na lista de reprodução. As opções de ordenação incluem **Título da Música, Número da Música, Álbum, Artista, Artista de Álbum, Género, Compositor, Avaliação, Ano, Batidas por Minuto, Duração, Nome do Ficheiro, Data de Modificação do Ficheiro, Data de Criação do Ficheiro** e **Manual**. A opção de ordenação **Manual** permite reordenar manualmente as músicas usando arrastar e largar.
- **Pesquisar** — pesquisar uma música específica dentro da lista de reprodução atual.
- **Grelha / Lista** — alterar a apresentação do layout do ecrã.
- **Eliminar Lista de Reprodução** — eliminar a lista de reprodução da biblioteca musical. Esta ação não elimina as faixas do seu armazenamento, mas **não pode ser desfeita**.

## Alterar a Ordem das Músicas numa Lista de Reprodução

Para alterar a ordem das músicas numa lista de reprodução, toque no botão **«...»** no canto superior direito e selecione **Selecionar** para entrar no modo de seleção. Use o controlo de reordenar e gestos de arrastar e largar perto de cada faixa para as mover para cima ou para baixo. Tocar no controlo de reordenar move a faixa para o topo da lista. Para sair do modo de seleção e aplicar alterações, toque em **Concluído**.

Para um fluxo de trabalho ainda mais simples em listas de reprodução longas, escolha Mais Ações → Reorganizar Músicas para entrar no modo dedicado de reordenação por arrastar e largar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Rearrange Songs in a Playlist" image="/docs/guide/flacbox/img/playlist-details-rearange-songs.webp" >}}
{{< /cards >}}

## Alterar a Imagem de Capa da Lista de Reprodução

Para alterar a imagem de capa de uma lista de reprodução, toque no botão **«...»** no canto superior direito e selecione **Editar Imagem**. Escolha uma imagem das fontes disponíveis (Fotos, Ficheiros, armazenamento na nuvem, ou uma capa gerada de uma faixa na lista de reprodução), depois confirme tocando em **Concluído**.

## Adicionar Músicas a uma Lista de Reprodução

Abra a lista de reprodução e toque no botão **«...»** no canto superior direito, depois selecione **Adicionar Músicas** para abrir um diálogo. Escolha as faixas que quer adicionar e confirme tocando em **Concluído**.

## Eliminar Múltiplas Músicas de uma Lista de Reprodução

Abra a lista de reprodução, toque no botão **«...»** no canto superior direito e selecione **Selecionar** para entrar no modo de seleção. Escolha as faixas que quer eliminar e toque em **Eliminar da Lista de Reprodução** na parte inferior do ecrã. Confirme tocando em **Concluído**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Selection Mode in the Playlist Detail Screen" image="/docs/guide/flacbox/img/selection-mode-playlist-details-screen.webp" >}}
{{< /cards >}}

## Opções da Faixa

Cada faixa numa lista de reprodução tem uma lista de ações, acessível tocando no botão **«...»**. Se não conseguir ver todas as ações, deslize para baixo para as ver. Pode eliminar a faixa da lista de reprodução, descarregá-la, editar tags de áudio e muito mais.

- **Reproduzir Seguinte** — adiciona a faixa ao topo da fila do leitor.
- **Reproduzir Mais Tarde** — acrescenta a faixa ao fundo da fila do leitor.
- **Adicionar a uma Lista de Reprodução** — adiciona a faixa a outra lista de reprodução.
- **Adicionar aos Favoritos** — marca a faixa como favorita para acesso rápido.
- **Transferir** — torna a faixa disponível offline. Aparece na fila de transferências e no separador **Ficheiros Locais** na secção **Música Descarregada** da biblioteca musical.
- **Editar Tags de Áudio** — abre o editor de tags integrado para alterar metadados da faixa.
- **Abrir Em** — exporta a faixa e abre-a noutra aplicação.
- **Mostrar na Pasta** — revela a pasta onde o ficheiro de áudio está localizado.
- **Mostrar no Finder** — para ficheiros importados do seu Mac, revela a pasta onde o ficheiro de áudio está localizado no seu Mac.
- **Eliminar da Lista de Reprodução** — elimina a faixa da lista de reprodução.
- **Eliminar do Serviço de Nuvem** — elimina a faixa da lista de reprodução e do serviço de nuvem associado. **Esta ação não pode ser desfeita.**
- **Eliminar da Biblioteca Musical** — elimina a faixa da biblioteca musical, deixando o ficheiro no armazenamento intacto.

## Acessibilidade

O Flacbox é totalmente acessível com a tecnologia **VoiceOver**, garantindo que todos os componentes têm uma etiqueta e descrição bem concebidas. Quando o VoiceOver está ativo, a aplicação traduz a interface de utilizador para **Modo de Texto**, exibindo apenas elementos acessíveis e úteis para melhorar a velocidade de navegação e conveniência. Também pode ativar o Modo de Texto em Configurações → Acessibilidade → Modo de Texto.

### Ajustar a Posição da Faixa numa Lista de Reprodução com VoiceOver

1. Abra uma lista de reprodução e toque no botão **Mais**.
2. Selecione **Alterar Ordem das Músicas**. A vista muda para modo de edição.
3. Toque no ícone do indicador de reordenar perto do título da faixa para lhe dar foco.
4. **Toque duas vezes** rapidamente no ícone do indicador de reordenar. No segundo toque, não levante o dedo — segure-o até ouvir um som indicando que a célula está pronta para ser movida.
5. Agora pode mover a célula para uma nova posição.

Outros componentes funcionam como esperado, usando padrões VoiceOver fornecidos pelo sistema.
