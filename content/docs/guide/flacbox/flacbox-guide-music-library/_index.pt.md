---
title: "Biblioteca Musical"
date: 2020-02-01
description: "Aprenda a construir, organizar e sincronizar a sua biblioteca musical no Flacbox no iPhone, iPad e Mac. Adicione faixas manualmente ou sincronize a partir de serviços de nuvem, gira metadados, capas de álbum, listas de reprodução, favoritos, recentes e marcadores. Inclui suporte de áudio Hi-Res, editor de tags MusicBrainz, sincronização online e offline, e opções de personalização."
keywords: [
  "biblioteca musical Flacbox", "sincronizar música da nuvem", "organizar metadados de música",
  "editar tags de áudio Flacbox", "sincronização de música offline", "importar música local",
  "gestão de listas de reprodução Flacbox", "pesquisa de capas de álbum Flacbox",
  "metadados de música iPhone", "guia da aplicação Flacbox",
  "Flacbox MusicBrainz", "Flacbox normalizar tags",
  "biblioteca de música hi-res Flacbox", "biblioteca FFmpeg Flacbox",
  "álbuns solo Flacbox", "vista de compositor Flacbox"
]
tags: ["música", "guia", "flacbox", "biblioteca"]
readingTime: 11
---


Gerir a sua biblioteca musical é muito simples com o Flacbox, onde pode organizar facilmente todas as suas faixas — FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE locais e dezenas de outros formatos — numa única coleção pesquisável. Tem duas opções para construir a sua biblioteca musical: adição manual (escolhe exatamente o que é adicionado) ou sincronização automática (o Flacbox analisa pastas de nuvem designadas e adiciona automaticamente novos ficheiros à medida que aparecem).

{{< cards cols="1">}}
  {{< card title="" subtitle="Vista de Álbuns da Biblioteca Musical do Flacbox" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Adição Manual

Para adicionar faixas manualmente, toque no ícone **Adicionar Música** localizado no canto superior esquerdo e escolha pastas ou ficheiros de um serviço de armazenamento na nuvem ligado ou ficheiros localizados no seu dispositivo. Quando adiciona faixas à biblioteca, apenas são criados links para essas faixas — os ficheiros reais permanecem nas suas localizações originais para poupar espaço de armazenamento valioso. Se quiser disponibilizar faixas offline, pode usar a ação Transferir do menu de opções ou ativar o Modo Offline para listas de reprodução e coleções de faixas.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Adicionar Músicas à Biblioteca Musical" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Também pode arrastar e largar ficheiros para a biblioteca na versão Mac, ou usar **Abrir Ficheiros…** / **Abrir Pasta…** do seletor de ficheiros do sistema no iPhone e iPad.

## Continuar Reprodução

Restaure a fila do leitor de áudio a partir da última posição guardada se esta funcionalidade estiver ativada nas definições da aplicação. Ative tanto **Guardar Estado do Leitor de Áudio** como **Guardar Posição de Reprodução** em Configurações → Leitor de Áudio → Geral para a melhor experiência. Uma vez ativado, um botão **Continuar Reprodução** aparece no topo de cada ecrã de pasta, álbum, artista, género e lista de reprodução — toque nele para saltar diretamente de volta para a faixa e posição exatas onde ficou.

## Localizações

Todas as faixas na sua biblioteca estão cuidadosamente agrupadas por tipo de fonte e tags musicais. Pode filtrar músicas por localização usando o botão **Mais Ações** no canto superior direito e selecionando **Filtrar**.

### Música Online

Esta secção apresenta música dos seus serviços de armazenamento na nuvem ligados. As faixas aqui são transmitidas a pedido; nada ocupa armazenamento local até que transfira explicitamente ou ative o modo offline.

### Ficheiros Nesta Aplicação

Aqui pode encontrar música disponível para reprodução offline, proveniente dos seus ficheiros locais. Inclui ficheiros no diretório Documentos da aplicação — tudo o que transferiu, importou via Wi-Fi Drive ou adicionou através da Partilha de Ficheiros Finder.

### Ficheiros Neste iPhone / iPad / Mac

Esta categoria inclui música importada para a aplicação a partir do seu dispositivo, adicionada através do diálogo do sistema **Abrir Ficheiros…**. Os ficheiros originais permanecem na sua localização original; o Flacbox mantém apenas um link para eles.

## Categorias

Quando adiciona faixas à sua biblioteca musical, a aplicação lê automaticamente as suas tags de áudio e organiza-as em categorias como Músicas, Músicas Não Reproduzidas, Álbuns, Artistas de Álbum, Artistas, Géneros e Compositores.

## Agrupamento de Tags

Estas categorias ajudam a organizar as suas faixas por tags musicais. Quando adiciona faixas à biblioteca musical, a aplicação lê os seus metadados e agrupa-os por estas categorias. Se não vir todos os seus álbuns, certifique-se de que a aplicação analisou cada faixa. Pode verificar o progresso da análise em Configurações → Biblioteca Musical → Leitura de Metadados → Número de Ficheiros Processados na Biblioteca Musical. Para ficheiros locais, também pode reanalisar pastas offline em Configurações → Biblioteca Musical → Sincronização de Pastas Offline → Iniciar Análise de Pastas Locais. Após o leitor de metadados completar todas as operações, verá as seguintes categorias na sua biblioteca musical:

- **Músicas** — todas as músicas agrupadas pela tag TRACK_TITLE. Pode verificar a ordem de ordenação usando o menu Mais Ações no canto superior direito.
- **Músicas Não Reproduzidas** — todas as músicas que nunca foram reproduzidas.
- **Álbuns** — músicas agrupadas pela tag ALBUM_NAME, ignorando as tags de artista, artista de álbum e compositor. Se tiver vários álbuns com o mesmo nome mas artistas diferentes, considere usar a ordenação de Álbuns Exclusivos descrita abaixo.
- **Artistas de Álbum** — músicas agrupadas apenas pela ALBUM_ARTIST_TAG. Útil para manter compilações e colaborações claramente separadas do trabalho solo.
- **Artistas** — músicas agrupadas apenas pela ARTIST_TAG.
- **Géneros** — músicas agrupadas pela tag GENRE.
- **Compositores** — músicas agrupadas pela tag COMPOSER — inestimável para bibliotecas de música clássica onde «compositor» é o eixo de navegação principal.

## Favoritos

Pode marcar músicas como favoritas no ecrã do leitor de áudio ou usando o menu de opções. Os favoritos aparecem na sua própria secção para que os possa encontrar com um toque.

## Recentes

Esta secção apresenta todas as faixas reproduzidas recentemente. Pode personalizar quantos itens a lista de recentes mantém em Configurações → Biblioteca → Recentes → Alterar Tamanho da Lista, e exportar a lista para M3U / CSV / TXT para fazer cópia de segurança do seu histórico de escuta.

## Marcadores

Pode criar marcadores de áudio enquanto uma música está a reproduzir e geri-los neste ecrã — perfeito para audiolivros, misturas longas, palestras, ou apenas para marcar o refrão de uma faixa favorita. Instruções detalhadas sobre como trabalhar com marcadores de áudio estão disponíveis [aqui](/docs/guide/evermusic/evermusic-guide-music-library).

## Barra de Ferramentas Superior

Localizada logo abaixo da barra de navegação, a barra de ferramentas superior oferece várias ações convenientes: Pesquisar, Reproduzir Tudo, Misturar Tudo e Continuar Reprodução. Pode revelar ou ocultar esta barra de ferramentas com um simples gesto de deslizar para baixo.

## Pesquisa

A funcionalidade de pesquisa permite localizar uma faixa, artista, álbum ou género específico na sua biblioteca musical. No ecrã de Pesquisa, tem acesso às ações Ordenar, Filtrar e vista Grelha / Lista. A pesquisa é executada localmente na base de dados da biblioteca musical, por isso funciona completamente offline e devolve resultados enquanto escreve.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Pesquisa na Biblioteca Musical" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Menu de Opções

Cada música na sua biblioteca musical tem um menu com mais ações, acedido tocando no botão de três pontos perto do título da música. Estas ações variam dependendo de ser uma música individual ou parte de uma coleção.

### Para Músicas Individuais

- **Reproduzir Seguinte** — adiciona a música ao topo da fila do leitor.
- **Reproduzir Mais Tarde** — acrescenta a música ao fundo da fila do leitor.
- **Adicionar a Lista de Reprodução** — adiciona a música a uma lista de reprodução.
- **Adicionar aos Favoritos** — marca a música como favorita para acesso rápido.
- **Baixar** — guarda a música em ficheiros locais. Aparece no separador **Ficheiros Locais** e na secção **Música Offline**.
- **Editar tags de áudio** — abre o editor de tags de áudio integrado para corrigir metadados em falta; note que isto irá alterar a música no seu armazenamento.
- **Mostrar na Pasta** — revela a pasta onde o ficheiro de áudio está armazenado.
- **Mostrar no Finder** — para ficheiros importados do seu Mac, esta ação revela a pasta onde o ficheiro de áudio está localizado no seu Mac.
- **Abrir Em** — exporta o ficheiro de áudio para outra aplicação.
- **Eliminar do Serviço na Nuvem** — remove o ficheiro tanto da biblioteca musical como do armazenamento na nuvem. **Esta ação é irreversível.**
- **Eliminar da Biblioteca Musical** — elimina a música da sua biblioteca musical, mas o ficheiro permanece no armazenamento. Se a sincronização automática estiver ativada e o ficheiro existir no armazenamento remoto, reaparecerá na sua biblioteca após uma operação de sincronização.

### Para Coleções de Músicas

Para coleções de músicas como Álbuns, Artistas, Géneros ou Compositores, o menu de opções inclui as seguintes ações.

- **Reproduzir Tudo** — substitui a fila do leitor por músicas da coleção selecionada.
- **Reproduzir Seguinte** — adiciona as músicas desta coleção ao topo da fila do leitor.
- **Reproduzir Mais Tarde** — acrescenta as músicas desta coleção ao fundo da fila do leitor.
- **Adicionar a Lista de Reprodução** — inclui músicas desta coleção numa lista de reprodução, com a opção de criar uma nova.
- **Ativar Modo Offline** — descarrega músicas desta coleção para ficheiros locais. Os ficheiros aparecem no separador **Ficheiros Locais** e na secção **Música Offline**. Se forem adicionados novos itens à coleção no servidor, serão descarregados automaticamente.
- **Editar Imagem** — altere a capa do álbum para a coleção de músicas.
- **Adicionar ao Arquivo** — agrupe toda a coleção num único ficheiro ZIP para fácil cópia de segurança ou transferência (funcionalidade Premium).
- **Exportar Lista de Músicas** — exporte a coleção para M3U, CSV ou TXT para uso noutros leitores ou para arquivamento.
- **Eliminar da Biblioteca Musical** — remove a coleção de músicas da sua biblioteca musical. Esta ação não elimina os ficheiros reais do armazenamento. Se a sincronização automática estiver ativada e os ficheiros existirem no armazenamento remoto, reaparecerão na sua biblioteca após uma operação de sincronização.

## Modo de Seleção

Pode ativar o modo de seleção usando o botão Mais Ações no canto superior direito. Neste modo, pode selecionar múltiplas faixas de uma vez e realizar ações em lote — adicionar a lista de reprodução, marcar como favorita, eliminar da biblioteca, transferir e mais.

## Detalhe do Álbum

Quando abre as secções Artista, Artista de Álbum ou Compositor, pode ver um seletor para Músicas / Todos os Álbuns / Álbuns Exclusivos / Álbuns Solo.

- **Músicas** — apresenta todas as músicas onde este Artista / Artista de Álbum / Compositor aparece nas tags de áudio.
- **Todos os Álbuns** — mostra álbuns de compilação e todos os álbuns onde o artista está presente.
- **Álbuns Exclusivos** — mostra álbuns onde o artista especificado é o único artista com esse nome de álbum.
- **Álbuns Solo** — mostra álbuns onde apenas as faixas do artista especificado aparecem, mesmo que outros artistas tenham álbuns com o mesmo nome.

Isto é especialmente útil para limpar compilações de «Vários Artistas» em grandes bibliotecas.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ecrã de Detalhe do Álbum" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Configurações

Toque em Mais Ações → Configurações para configurar as suas preferências de biblioteca musical.

### Leitura de Metadados

Quando adiciona faixas à biblioteca, o leitor de metadados entra em ação. Este processo em segundo plano lê todos os metadados das suas faixas e organiza-os por Artista, Álbum, Género e Compositor. Pode ajustar a velocidade de leitura de metadados para carregar dados mais rapidamente — esteja ciente de que uma leitura mais rápida usa mais energia. Também pode desativar completamente o leitor de metadados e mostrar nomes de ficheiros em vez de informações de tags.

Importantemente, o leitor de metadados apenas atualiza metadados na sua biblioteca musical e não altera os ficheiros armazenados na sua conta de nuvem ou armazenamento local. Se deseja editar metadados para ficheiros de áudio, pode fazê-lo usando o editor de tags integrado, que pode ativar a partir da ação correspondente no menu de opções.

### Modos Disponíveis para o Leitor de Metadados

- **Desativado** — o leitor de metadados está desligado e os nomes dos ficheiros são mostrados em vez dos dados de tags de áudio.
- **Música Atual** — a aplicação lê metadados apenas para a música atualmente a reproduzir. Use esta opção se tiver uma ligação de rede lenta para evitar que o leitor de metadados envie muitos pedidos ao servidor de nuvem, o que pode causar interrupções na reprodução.
- **Fila de Reprodução** — a aplicação lê metadados para todas as músicas na fila do leitor de áudio.
- **Biblioteca** — a aplicação lê metadados para todas as músicas na biblioteca musical.

Quando o interruptor **Leitura de Metadados em Segundo Plano** está ativado, o leitor de metadados continua a trabalhar em modo de segundo plano. Note que se a aplicação consumir muita energia durante a reprodução de áudio, o sistema operativo iOS pode suspendê-la.

Por isso, se tiver uma grande coleção musical, é aconselhável usar a versão desktop da aplicação para sincronização de metadados. Pode depois usar a funcionalidade de Cópia de Segurança e Restauro nas definições da aplicação para transferir a biblioteca sincronizada do desktop para o móvel.

Quando a opção **Normalizar Codificação de Metadados** está ativada, a aplicação normaliza automaticamente a codificação de metadados para todas as músicas na biblioteca musical. Isto corrige problemas onde a codificação de tags de áudio está danificada (como após editar ficheiros num PC Windows) e evita que caracteres incorretos apareçam nas informações das faixas.

A ação **Recarregar metadados** assinala cada ficheiro na sua biblioteca musical como tendo metadados em falta, fazendo com que o leitor de metadados atualize cada registo.

Toque em **Iniciar Leitura de Metadados** para acionar o leitor manualmente. O progresso da operação é apresentado abaixo.

### Sincronização Online

A sincronização automática de música online permite adicionar faixas de serviços de nuvem ligados à biblioteca musical automaticamente. Para ativar esta funcionalidade, vá às Definições da Biblioteca Musical e selecione pastas de sincronização.

Com esta opção ativada, a aplicação analisa todas as pastas selecionadas, identifica ficheiros de áudio suportados e integra-os perfeitamente na sua biblioteca. Pode iniciar ou parar a sincronização tocando na ação de menu correspondente.

A sincronização de música online opera exclusivamente quando a aplicação está em primeiro plano, o que significa que sincronizar uma biblioteca grande pode demorar algum tempo. Para acelerar o processo, mantenha a aplicação aberta, ligue-a a uma fonte de alimentação e ative Ecrã → Sempre Ativo nas definições da aplicação.

Alternativamente, pode realizar a sincronização de música online na versão desktop da aplicação e transferir a biblioteca musical para a versão iOS usando a funcionalidade Cópia de Segurança e Restauro.

Também pode definir com que frequência pretende sincronizar a sua biblioteca de música online. Se definir o intervalo para Imediatamente, a sincronização online iniciará cada vez que abrir a aplicação.

### Sincronização Offline

Aqui pode configurar a sincronização de música offline.

#### Pastas Offline Sincronizadas

Quando torna uma pasta de nuvem disponível offline (através do menu Mais Ações), ela aparece na secção Ficheiros Locais → Pastas Offline. A aplicação descarrega o seu conteúdo para o seu dispositivo. Se fizer alterações na pasta na nuvem — como adicionar, remover ou atualizar ficheiros — a aplicação deteta essas alterações e atualiza a cópia local automaticamente.

Neste ecrã, pode iniciar manualmente a sincronização de pastas offline, revelar a pasta offline na sua pasta envolvente e desativar o modo offline para a pasta. Desativar o modo offline remove todas as cópias locais dos ficheiros do seu dispositivo.

#### Intervalo de Tempo

Pode definir o intervalo de tempo para a frequência com que a aplicação deve verificar as pastas offline para modificações.

#### Iniciar Análise de Pastas Locais

Esta opção analisa todas as pastas locais localizadas no diretório Documentos da aplicação para encontrar ficheiros de áudio suportados. Todos estes ficheiros locais são adicionados perfeitamente à sua biblioteca musical. Os ficheiros locais localizados no seu dispositivo mas fora desta aplicação devem ser adicionados à biblioteca musical manualmente, pois a aplicação não tem acesso a ficheiros fora do diretório Documentos da aplicação devido a restrições de segurança iOS / macOS.

#### Importante

É aconselhável iniciar periodicamente a sincronização de música offline para manter a sua biblioteca musical atualizada com os seus ficheiros locais.

### Personalização

Nesta secção, pode configurar o estilo do ecrã da biblioteca musical de acordo com as suas preferências. Estão disponíveis três opções: Menu Simples, Menu Agrupado, Menu com Separadores. Também pode ativar ou desativar a apresentação de capas de álbum nos ecrãs de detalhe de álbum.

### Capas de Álbum

Aqui, pode configurar como a aplicação carrega e armazena as capas dos álbuns.

- **Tipo de Rede** — escolha Wi-Fi ou Wi-Fi e Dados Móveis para transferências de capas.
- **Carregar Capas de Álbum para Ficheiros Online** — quando ativado, as capas de álbum incorporadas são carregadas para ficheiros armazenados no armazenamento na nuvem. Pode usar dados de rede adicionais.
- **Pesquisar na Pasta** — quando ativado, se uma faixa não tiver capa incorporada, a aplicação procura imagens JPEG ou PNG na mesma pasta e usa-as como capa do álbum.
- **Qualidade da Capa** — escolha a qualidade das capas de álbum armazenadas no seu dispositivo.
- **Mostrar na Pasta** — abra a pasta onde as capas de álbum estão em cache para que as possa gerir ou fazer cópia de segurança.
- **Eliminar Tudo** — elimine as capas de álbum em cache para libertar espaço de armazenamento e forçar a aplicação a recarregá-las a pedido.

Por omissão, a aplicação verifica as capas de álbum incorporadas nas suas faixas e apresenta-as se disponíveis. Se não existirem capas de álbum incorporadas e a opção **Pesquisar na Pasta** estiver ativada, a aplicação verifica a pasta envolvente para imagens JPEG ou PNG e usa-as como capas de álbum para todas as faixas dessa pasta.

### Listas de Reprodução

Pode ativar a opção para adicionar a mesma música a uma lista de reprodução duas vezes. Por omissão, esta opção está desativada.

### Recentes

Pode gerir a sua lista de músicas reproduzidas recentemente.

- **Eliminar Lista** — eliminar toda a lista de músicas reproduzidas recentemente.
- **Alterar Tamanho da Lista** — definir o número de itens que aparecem na lista.
- **Exportar Lista de Músicas** — exportar a sua lista de músicas reproduzidas recentemente para M3U, CSV ou TXT. Instruções detalhadas estão disponíveis [aqui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritos

Pode gerir a lista das suas músicas favoritas.

- **Edição Simultânea** — quando ativado, adicionar uma música aos favoritos adiciona-a tanto na biblioteca musical como na secção de ficheiros ao mesmo tempo.
- **Eliminar Lista** — eliminar toda a lista de músicas favoritas.
- **Exportar Lista de Músicas** — semelhante a Recentes, exportar a lista de favoritos para M3U, CSV ou TXT.

### Eliminar Biblioteca

Esta ação irá apagar a base de dados da biblioteca musical, mas deixará os seus ficheiros de música intocados no armazenamento.

### Limite de Carregamento de Conteúdo

Por omissão, a aplicação usa paginação para reduzir o tempo de carregamento de conteúdo e manter grandes bibliotecas responsivas. No entanto, pode desativar esta opção e permitir que a aplicação carregue todos os dados disponíveis de uma vez. Para o fazer, abra as definições da aplicação, desloque para baixo até Personalização → Limite de Carregamento de Conteúdo e escolha Desativado.
