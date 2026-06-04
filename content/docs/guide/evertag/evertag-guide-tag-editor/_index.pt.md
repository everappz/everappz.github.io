---
title: "Editor de Tags"
date: 2020-02-01
description: "Aprenda a usar o Editor de Tags do Evertag para atualizar metadados musicais, editar capas de álbuns, editar em lote vários ficheiros e gerir tags do MusicBrainz. Ideal para organizar a sua biblioteca musical no iOS e Mac."
keywords: [
  "Evertag editor de tags", "editor de metadados áudio", "editor de tags musicais",
  "editar tags áudio iPhone", "editor de capa de álbum", "edição em lote de tags áudio",
  "metadados MusicBrainz", "aplicação organizadora de música", "guia Evertag", "editor de tags ID3"
]
tags: ["guia", "evertag", "editor de tags"]
readingTime: 5
---


O **Editor de Tags** é o ecrã principal da aplicação Evertag onde pode ver e editar metadados de ficheiros de áudio. Abra este ecrã tocando num ficheiro da secção **Ficheiros Locais** ou de qualquer conta de **armazenamento na nuvem** ligada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Modos de Edição

O Evertag fornece dois modos de edição:

- **Modo de ficheiro único**  
  - Navegue entre ficheiros deslizando para a esquerda ou direita no carrossel de capas.  

- **Modo em lote**  
  - Edite múltiplos ficheiros de uma vez e aplique metadados partilhados.  
  - Para ativar, desloque-se para o fundo e toque em **Editar vários ficheiros simultaneamente**.

## Modo de Ficheiro Único

Por predefinição, a aplicação abre o editor de tags no modo de ficheiro único com apenas as opções de edição principais ativadas. Neste modo, pode editar os campos de metadados mais comuns, tais como:

**Título da Faixa, Subtítulo, Artista do Álbum, Álbum, Artista, Compositor, Intérprete, Género, Comentário, Batidas Por Minuto, Podcast, Compilação, Número do Disco, Número da Faixa, Total de Faixas, Classificação, Ano**

Para aceder a todas as tags disponíveis, desloque-se para o fundo do ecrã e toque na opção **Mostrar Tags Avançadas**. Isto mudará o editor para o modo avançado, permitindo-lhe editar mais de **120 campos de metadados**, incluindo **Tags MusicBrainz**, **Letras**, **Classificações de Aviso**, valores de replay-gain, ordens de ordenação, metadados de podcast e muito mais. Use **Configurações → Editor de tags de áudio → Botões no ecrã principal** para ativar permanentemente Mostrar Tags Avançadas para que esteja sempre ativo.

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Modo em Lote

Pode entrar na edição em lote de duas formas:

1. **A partir do Gestor de Ficheiros**  
   - Toque em **Mais ações** (•••) no canto superior direito.  
   - Toque em **Selecionar**, escolha múltiplos ficheiros e depois toque em **Editar tags de áudio**.

2. **A partir do Editor de Tags**  
   - Abra qualquer ficheiro, desloque-se para o fundo e toque em **Editar ficheiros simultaneamente** para carregar todos os ficheiros da mesma pasta.

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Após editar, toque em **Salvar** para aplicar as alterações.

## Editar Letras

O editor avançado expõe o campo **Letras**. Toque nele para abrir a lista de letras — cada entrada de letras tem o seu próprio idioma e descrição, pelo que uma única faixa pode armazenar várias traduções.

Não tem de escrever as letras do zero. O editor inclui atalhos de pesquisa com um toque para as bases de dados de letras mais populares na web, pré-preenchidos com o artista e título da faixa atual:

- **Lrclib** — a base de dados pública preferida para **letras sincronizadas (estilo LRC)**. Use-a quando quer letras sincronizadas que rolam linha a linha em leitores que as suportam.
- **Genius** — grande catálogo com anotações e letras em texto simples precisas.
- **Lyricsify** — base de dados gerida pela comunidade com letras simples e com marcas temporais.
- **Google** — uma pesquisa web geral como alternativa quando as bases de dados dedicadas não têm correspondência.

Cada atalho só aparece quando o serviço correspondente é acessível a partir do seu dispositivo. Toque num serviço, copie as letras (ou as marcas temporais LRC) que quer, regresse ao Evertag e cole-as no campo de texto — depois **Salvar** para escrever as letras de volta nas tags do ficheiro de áudio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Escolha um idioma no seletor:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Depois cole ou escreva o texto das letras. O Evertag suporta texto simples e letras sincronizadas — o placeholder mostra um exemplo do formato LRC, que é exatamente o que Lrclib e Lyricsify devolvem para resultados sincronizados.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Definir uma Classificação e Classificação de Aviso

O editor avançado oferece um controlo de estrelas **Classificação** juntamente com um controlo segmentado de **Classificação de Aviso**.

### Classificação por Estrelas

Use o campo **Classificação** para dar a uma faixa uma pontuação pessoal de uma a cinco estrelas. O valor é escrito na tag de classificação padrão do ficheiro (POPM para ID3, `rate` para MP4, `RATING` para Vorbis/APE, etc.), portanto outras aplicações que leem esta tag — incluindo a aplicação Music, Plex, Roon e a maioria dos editores de tags de desktop — verão imediatamente as suas pontuações.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Classificação de Aviso

A **Classificação de Aviso** marca o conteúdo de uma faixa usando um dos valores do padrão Parental Advisory que a iTunes Store e a maioria das plataformas musicais usa:

- **Sem restrições** — o padrão para faixas sem informação de aviso parental. O ficheiro é tratado como adequado para todos os ouvintes e não mostrará qualquer etiqueta de aviso em leitores que respeitam a tag.
- **Explícito** — a faixa contém linguagem ou conteúdo explícito. Leitores que honram os controlos parentais (a aplicação Music, a aplicação Apple TV, exportações Spotify, Plex, etc.) exibirão um crachá **E** junto ao título e, quando as restrições estão ativadas no dispositivo ou conta, podem ocultar a faixa dos perfis de crianças ou recusar-se a reproduzi-la.
- **Limpo** — uma versão censurada ou editada de uma faixa de outra forma explícita. Os leitores exibem um crachá **C** para os ouvintes poderem distinguir uma edição limpa do master explícito original, o que é útil quando ambas as versões vivem na mesma biblioteca.

Deverá definir ou corrigir este campo quando:

- Um ficheiro tem a etiqueta errada (por exemplo, uma edição de rádio limpa que foi erroneamente marcada como Explícita, ou vice-versa).
- Faixas foram convertidas ou transferidas sem a tag e agora estão a aparecer como Sem restrições mesmo que contenham conteúdo explícito — necessário para que os controlos parentais e as bibliotecas partilhadas em família funcionem corretamente.
- Está a preparar um álbum para submissão ou partilha e precisa que cada faixa tenha metadados consistentes.
- Quer que o CarPlay, o Ecrã de Bloqueio, leitores no estilo Apple Music ou software de DJ exibam o crachá **E** / **C** correto junto ao título da faixa.

O valor é armazenado no campo de classificação de aviso padrão para o formato do ficheiro (`rtng` para MP4, `TXXX:ITUNESADVISORY` para ID3, `ITUNESADVISORY` para Vorbis), portanto qualquer leitor que lê metadados de aviso parental verá a sua atualização.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Editar Capa de Álbum

Para alterar uma capa de álbum:

1. Toque no ícone **Câmara** no carrossel de capas.  
2. Escolha a localização da imagem: Ficheiros Locais, Nuvem, Transferências ou Biblioteca de Fotografias.  
3. Selecione uma imagem para aplicar como arte da capa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Mais Ações no Editor de Tags

Opções de edição extra estão disponíveis através da barra de ferramentas abaixo da vista de capas.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Pesquisa Automática de Tags de Áudio

Esta ação ativa o motor de pesquisa inteligente de tags, que encontra e preenche metadados completos para o seu ficheiro de áudio com base nas informações existentes.  
A aplicação usa a base de dados MusicBrainz — uma das bases de dados de tags mais abrangentes — com mais de **50 milhões** de faixas.

### Pesquisar Capa de Álbum

Use metadados para pesquisar na web a arte do álbum correta.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Depois de encontrada, guarde a imagem nas suas **Fotografias** usando o menu de contexto do sistema.

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Depois disso, regresse ao editor de tags, toque no ícone da Câmara, vá para **Biblioteca de Fotografias** e selecione a imagem guardada. A aplicação vai defini-la como a capa do seu ficheiro de áudio.

Pode ajustar como as imagens de capa são dimensionadas nas configurações da aplicação.

### Guardar Arte do Álbum

Esta ação guarda a arte do álbum atual na pasta **Documentos**, para poder reutilizá-la mais tarde.

### Normalizar Codificação

Esta ação irá normalizar a codificação de texto de todas as tags nos metadados do ficheiro de áudio. É especialmente útil se estiver a fazer a transição de um PC com Windows, onde os ficheiros podem usar codificações diferentes que aparecem como caracteres ilegíveis ou corrompidos num Mac.

### Pesquisa Manual de Tags

Pesquise metadados de álbuns manualmente usando a base de dados MusicBrainz.  

- Selecione o álbum  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Escolha a música correta  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Escolha quais tags aplicar  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Toque em **Concluído** para aplicar os metadados selecionados à sua faixa.

### Excluir Tags de Áudio

Limpe todos os campos de metadados de um ficheiro. Útil ao começar do zero. Toque em **Salvar** para confirmar.

## Configurações do Editor de Tags

Navegue para **Configurações → Editor de tags de áudio** para personalizar o comportamento.

### Dimensionamento de Capa de Álbum

Selecione como as capas de álbuns devem ser dimensionadas ao serem guardadas em ficheiros de áudio. Pode desativar o dimensionamento para manter o tamanho da imagem original, mas tenha em atenção que alguns leitores podem não suportar ficheiros de capa grandes. A opção "tamanho original" faz parte das funcionalidades de personalização Premium.

### Opções de Guardar Tags

- **ID3v2.4** — quando ativado, a aplicação guarda tags no formato ID3v2.4 sempre que possível. Desative para reverter para o ID3v2.3 mais amplamente suportado se as suas tags de áudio não forem exibidas corretamente em leitores ou dispositivos mais antigos.
- **Tags duplicadas** — quando ativado, os campos de metadados comuns são duplicados nas duas secções de tags do ficheiro. Isto melhora a compatibilidade com leitores de áudio mais antigos, mas na maioria dos casos não é necessário.

### Opções de Atualização de Metadados de Ficheiros na Nuvem

Pode controlar como a aplicação atualiza metadados para ficheiros de áudio armazenados em serviços de cloud:

- **Mostrar mensagem de confirmação**  
  Perguntar antes de aplicar alterações de metadados a ficheiros de cloud.

- **Atualizar automaticamente os metadados do ficheiro**  
  Guardar alterações de metadados no ficheiro de cloud automaticamente após edição.

- **Não atualizar os metadados do ficheiro**  
  Ignorar a atualização de ficheiros de cloud — as alterações aplicar-se-ão apenas localmente.

### Editar Ficheiros Online

Escolha o que acontece às cópias localmente transferidas de ficheiros de cloud após edição:

- **Eliminar sempre o ficheiro transferido**  
  Remover a cópia local após guardar as alterações.

- **Não eliminar o ficheiro transferido**  
  Manter o ficheiro transferido no seu dispositivo após edição.

### Botões do Ecrã Principal

Personalize quais as ações que aparecem no ecrã principal do editor de tags (Pesquisa automática de tags, Pesquisa manual de tags, Pesquisar capa de álbum, Guardar arte do álbum, Normalizar codificação, Excluir tags de áudio). Pode também alternar **Mostrar tags avançadas** e **Editar ficheiros simultaneamente** para que o editor abra sempre no seu modo preferido.
