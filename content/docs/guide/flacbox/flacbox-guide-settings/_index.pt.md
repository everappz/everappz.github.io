---
title: "Configurações"
date: 2020-02-01
description: "Explore cada definição do Flacbox — desde preferências de reprodução, motor de áudio FFmpeg / sistema, saída de áudio Hi-Res, ajustes de equalizador, correção de tom, duração do buffer IO, sincronização de metadados, gestão de listas de reprodução, transferências de ficheiros, widgets do ecrã inicial, Apple CarPlay, personalização da interface, idioma, código de acesso, cópia de segurança e restauro, e atualização Premium."
keywords: [
  "definições Flacbox", "configuração leitor áudio", "atualização Premium Flacbox",
  "WiFi Drive", "sincronização metadados", "equalizador", "velocidade reprodução",
  "duplicados lista reprodução", "definições gestor ficheiros", "sincronização música offline",
  "editor tags áudio", "modo escuro", "restaurar compras", "cópia segurança definições",
  "definições widgets Flacbox", "definições CarPlay Flacbox",
  "Flacbox FFmpeg definições", "Flacbox definições taxa amostragem",
  "Flacbox definições correção tom", "Flacbox buffer IO",
  "Flacbox código acesso", "idioma Flacbox", "personalização Flacbox",
  "Flacbox análise"
]
tags: ["guia", "flacbox", "configuracoes"]
readingTime: 16
---


O ecrã de Configurações é o centro de controlo do Flacbox. A partir daqui pode atualizar para Premium, configurar o motor de áudio (codecs do sistema ou FFmpeg), gerir a sua biblioteca musical, configurar o gestor de ficheiros, personalizar o editor de tags de áudio, ativar widgets do ecrã inicial e Apple CarPlay, fazer cópias de segurança dos seus dados, e aceder a ajuda e informações legais. As secções estão agrupadas sob cabeçalhos: Compras e Atualizações, Preferências da Aplicação, Ajuda e Legal & Privacidade.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Settings Main Screen" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Atualizar para Premium

Atualize a aplicação para a versão Premium para remover todos os limites. A versão gratuita da aplicação oferece uma compra única vitalícia dentro da aplicação e duas opções de subscrição (1 mês e 1 ano) para remover todas as restrições e atualizar para Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Upgrade to Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

A **Partilha em Família** está ativada para todas as compras e planos, pelo que pode partilhar a versão Premium com até cinco membros da sua família sem custos adicionais.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Select a Premium Plan" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Pode ler mais sobre compras e a versão Premium aqui: [Qual é a diferença entre Flacbox e Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Partilhar Compras entre iOS e Mac

As compras vitalícias e subscrições são partilhadas entre iOS e Mac, usando o iCloud para sincronizar esta informação. Se tiver a versão Premium no seu dispositivo iOS, certifique-se de que tem a versão mais recente instalada e que o iCloud está ativado. Inicie a aplicação no iOS e aguarde um minuto para que as informações de compra sejam enviadas para o iCloud.

Também pode tentar tocar no botão Restaurar Compras nas definições da aplicação. Depois, instale a versão mais recente da aplicação a partir da App Store no seu Mac e inicie a aplicação. Certifique-se de que tem uma ligação à internet e está a usar a mesma conta iCloud e App Store no Mac que usou no iOS. Aguarde um minuto para que a aplicação descarregue as informações de compra do iCloud — a versão Premium deve ativar-se no seu Mac automaticamente.

## Restaurar Compras num Novo Dispositivo

Para restaurar a sua compra num novo dispositivo, use o menu Compras → Restaurar Compras. Verá a lista das suas compras. Se não as vir todas, confirme que o dispositivo está ligado ao mesmo Apple ID que foi usado para fazer as compras e certifique-se de que o iCloud está ativado.

## Experimentar Premium Gratuitamente

Pode atualizar para a versão Premium gratuitamente, por tempo limitado, usando este menu. Basta ver um anúncio ou falar aos seus amigos sobre a aplicação para obter Premium gratuitamente.

## Compras

Pode restaurar compras anteriores a partir deste menu. Se encontrar erros de ativação, tente ativar a opção Restaurar Compras ao Iniciar a Aplicação.

## Atualização de Software

Toque em Atualização de Software para verificar se está disponível uma versão mais recente do Flacbox. A aplicação irá comparar a sua versão instalada com a versão mais recente na App Store e informá-lo se uma atualização é recomendada.

## Novidades

Este menu está disponível depois de uma nova versão ser lançada. Mostra um resumo das alterações e novas funcionalidades na atualização mais recente.

## Leitor de Áudio

Esta secção configura o leitor de áudio e o motor de áudio subjacente, incluindo a escolha entre FFmpeg / codec do sistema e as opções de saída de áudio Hi-Res.

### Geral

Estas definições cobrem os aspetos fundamentais do leitor de áudio — fila de reprodução, saída de áudio e guardar o estado do leitor.

- **Modo de Repetição** — escolha como o leitor de áudio se comporta quando uma faixa termina:
  - **Repetir Tudo** — repete todas as faixas na sua fila.
  - **Repetir Uma** — repete apenas a faixa atual.
  - **Parar na Faixa** — pausa a reprodução quando a faixa atual termina.
  - **Não Repetir** — permite que a sua fila seja reproduzida sem repetir.
- **Modo Aleatório** — aleatoriza a ordem das faixas na sua fila. Pode desativar ou ativar.
- **Codec de Áudio** — escolha o motor de áudio utilizado para reprodução:
  - **System Codec + FFmpeg** — prioriza o codec de áudio do sistema sempre que possível, melhorando compatibilidade e estabilidade. A correção de tom e a taxa de amostragem de saída de áudio podem ser limitadas.
  - **FFmpeg** — força o codec FFmpeg para todos os ficheiros de áudio, desbloqueando a correção de tom e a taxa de amostragem de saída de áudio.
- **Taxa de Amostragem de Saída de Áudio** — ajuste a taxa de amostragem de saída. Valores disponíveis: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** e **96 kHz**.
- **Número de Canais de Saída de Áudio** — para sistemas multicanal com um DAC externo: Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround e SDDS.
- **Duração do Buffer IO de Saída de Áudio** — configure a duração do buffer. Um valor típico para minimizar a latência é cerca de **5 milissegundos (0,005 segundos)**. Teste diferentes durações no seu dispositivo.
- **Modo de Saída de Áudio (apenas iOS)** — configure o modo de saída de áudio misto. Instruções detalhadas [aqui](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Guardar Posição de Reprodução** — guarda e restaura a posição de reprodução para músicas na sua biblioteca musical.
- **Guardar Estado do Leitor de Áudio** — preserva o estado do leitor de áudio antes de fechar a aplicação, facilitando retomar de onde ficou.

Depois de ter ativado tanto **Guardar Posição de Reprodução** como **Guardar Estado do Leitor de Áudio**, abra qualquer pasta, álbum, artista ou género e verá um botão **Continuar Reprodução** no topo do ecrã.

### Personalização

A personalização permite-lhe personalizar o aspeto do ecrã do leitor de áudio, alterar os controlos disponíveis no ecrã principal, ecrã de bloqueio e barra de estado, e configurar os controlos de salto de tempo.

- **Estilo do Ecrã do Leitor de Áudio** — configure o posicionamento dos elementos no ecrã do leitor de áudio.
- **Estilo de Deslocamento das Capas dos Álbuns** — configure o estilo de deslocamento preferido para as capas dos álbuns.
- **Elementos Adicionais** — ative elementos extra no ecrã do leitor de áudio. Informações do Formato de Áudio mostra as informações de áudio da faixa em reprodução acima da capa; Cursor de Volume de Áudio mostra o cursor de saída de áudio abaixo dos controlos de reprodução.
- **Ações do Ecrã Principal** — configure quais botões devem estar visíveis por predefinição: Modo de Repetição e Aleatório, Música Seguinte e Anterior, Saltar Tempo, Temporizador de Sono, Google Chromecast, AirPlay e Bluetooth, Equalizador de Áudio, Pesquisar, Marcadores, Velocidade, Adicionar Marcador, Adicionar aos Favoritos, Comentários e mais.
- **Controlos de Reprodução no Ecrã de Bloqueio** — escolha quais controlos aparecem no ecrã de bloqueio. Valores possíveis: Saltar Tempo, Adicionar Marcador, Adicionar aos Favoritos.
- **Botões de Salto de Tempo** — escolha o intervalo de tempo para os botões de Saltar Tempo.

### Carregamento de Ficheiros

Durante o carregamento de ficheiros, pode alterar o tipo de rede. Opções disponíveis: **Wi-Fi**, **Wi-Fi e Dados Móveis**.

- **Tempo de Pré-carregamento** — defina o intervalo de tempo de buffering. Aumente se tiver uma ligação de rede fraca.
- **Usar URL Direto** — quando ativado, é usado um URL direto para carregar a música se o servidor suportar. Pode acelerar o carregamento mas pode afetar a estabilidade.

### Equalizador de Áudio

Configure o equalizador de áudio de 10 bandas, predefinições e pré-amplificador. Pode ler mais sobre como configurar o equalizador de áudio [aqui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocidade de Reprodução

Ajuste a velocidade de reprodução de **0,02× a 3,00×**. Toque no ícone de configuração no canto superior direito para mudar para **modo preciso**.

### Correção de Tom

Altere as definições de correção de tom ou mude para **modo preciso** tocando no botão no canto superior direito. Disponível no caminho do codec FFmpeg, com um intervalo de **-1000 a +1000**.

### Cache de Reprodução

As músicas na fila são automaticamente transferidas para garantir uma reprodução suave. Se transferir manualmente ficheiros de áudio, pode desativar esta opção para evitar duplicados. Também pode configurar o tamanho da cache aqui.

### Temporizador de Sono

Ative um temporizador para parar automaticamente a reprodução após um período especificado. Toque no ícone de configuração no canto superior direito para o **modo preciso** com granularidade minuto a minuto.

## Biblioteca

As definições da sua biblioteca musical — sincronização automática, leitura de metadados, carregamento de capas de álbuns, listas de reprodução, recentes e favoritos — estão aqui.

### Leitura de Metadados

Quando adiciona faixas à biblioteca, o **leitor de metadados** entra em ação. Este processo em segundo plano lê todos os metadados das suas faixas e organiza-as por Artista, Álbum, Género e Compositor. Pode ajustar a velocidade de leitura de metadados para carregar dados mais rapidamente (com custos de bateria). Também pode desativar o leitor de metadados e exibir nomes de ficheiros em vez de informações de tags.

O leitor de metadados **apenas atualiza metadados na sua biblioteca musical** e não altera os ficheiros armazenados na sua conta cloud ou armazenamento local. Para editar metadados nos próprios ficheiros de áudio, use o **editor de tags** integrado através da ação correspondente no menu de opções.

Quando **Leitura de Metadados em Segundo Plano** está ativa, o leitor continua a trabalhar em modo de segundo plano. Se a aplicação usar demasiada energia durante a reprodução de áudio, o iOS pode suspendê-la.

Se tiver uma grande coleção musical, execute a sincronização de metadados na versão desktop da aplicação e transfira a biblioteca musical sincronizada para iOS usando **Cópia de Segurança e Restauro**.

Quando **Normalizar Codificação de Metadados** está ativado, a aplicação normaliza automaticamente a codificação de metadados para todas as músicas. Isto corrige codificações de tags corrompidas (por exemplo após editar ficheiros num PC Windows) e evita que caracteres incorretos apareçam nas informações das faixas.

**Recarregar Metadados** marca todos os ficheiros na sua biblioteca musical como tendo metadados em falta, o que faz com que o leitor de metadados atualize todos os registos.

**Iniciar Leitura de Metadados** aciona manualmente o leitor de metadados. O progresso é mostrado abaixo da ação.

### Sincronização Online

A sincronização online automática de música adiciona faixas de serviços cloud ligados à biblioteca musical automaticamente. Para a ativar, abra as definições da biblioteca musical e selecione pastas de sincronização.

Com esta opção ativada, a aplicação analisa as pastas selecionadas, identifica ficheiros de áudio suportados e adiciona-os à sua biblioteca. Inicie ou pare a sincronização com a ação de menu correspondente.

A sincronização online funciona apenas quando a aplicação está em primeiro plano, por isso sincronizar uma biblioteca grande pode demorar algum tempo. Para acelerar, mantenha o Flacbox aberto, ligue o dispositivo à corrente e ative **Configurações → Ecrã → Sempre Ativo**.

Também pode escolher com que frequência a sincronização online é executada. Definir o intervalo para **Imediatamente** aciona uma sincronização toda vez que abre a aplicação.

### Sincronização Offline

Configure a sincronização de música offline.

#### Pastas Offline Sincronizadas

Quando marca uma pasta online no seu servidor cloud como disponível offline (usando o menu **Mais Ações**), ela aparece aqui. O conteúdo da pasta é descarregado para **Ficheiros Locais → Pastas Offline**. Quando a pasta online muda (ficheiros adicionados, removidos ou atualizados), a aplicação verifica as alterações e atualiza a cópia local no seu dispositivo.

Neste ecrã pode iniciar manualmente a sincronização de pastas offline, revelar a pasta offline na sua pasta de encerramento e desativar o modo offline para a pasta. Desativar o modo offline remove todas as cópias locais de ficheiros do seu dispositivo.

#### Intervalo de Tempo

Escolha com que frequência a aplicação verifica as pastas offline para modificações.

#### Iniciar Pesquisa de Pastas Locais

Pesquisa todas as pastas locais no diretório **Documentos** da aplicação para ficheiros de áudio suportados. Os ficheiros encontrados são adicionados à biblioteca musical automaticamente. Os ficheiros localizados no seu dispositivo mas fora do diretório Documentos da aplicação devem ser adicionados à biblioteca musical manualmente, pois a aplicação não pode aceder a eles devido a restrições de segurança do iOS / macOS.

**Importante:** É aconselhável iniciar periodicamente a sincronização de música offline para manter a sua biblioteca musical atualizada com os seus ficheiros locais.

### Personalização

Configure o estilo do ecrã da biblioteca musical. Três opções disponíveis: **Menu Simples, Menu Agrupado, Menu com Separadores**. Também pode ativar ou desativar capas de álbuns no ecrã de detalhes do álbum.

### Capas de Álbuns

Configure como a aplicação carrega e armazena as capas dos álbuns.

- **Tipo de Rede** — escolha **Wi-Fi** ou **Wi-Fi e Dados Móveis** para descarregar capas.
- **Carregar Capas de Álbuns para Ficheiros Online** — quando ativado, as capas incorporadas são carregadas para ficheiros armazenados no armazenamento cloud. Pode usar dados de rede adicionais.
- **Pesquisar na Pasta** — quando ativado, se uma faixa não tiver capa incorporada, a aplicação procura imagens JPEG ou PNG na mesma pasta.
- **Qualidade da Capa** — selecione a qualidade das capas de álbuns armazenadas no seu dispositivo.
- **Mostrar na Pasta** — abra a pasta onde as capas de álbuns estão em cache.
- **Eliminar Todas** — elimine as capas de álbuns em cache para libertar espaço de armazenamento e forçar a aplicação a recarregá-las a pedido.

### Listas de Reprodução

Ative a opção para adicionar a mesma música a uma lista de reprodução duas vezes. Por predefinição, esta opção está desativada.

### Recentes

Gira a sua lista de músicas reproduzidas recentemente.

- **Eliminar Lista** — elimine toda a lista de músicas reproduzidas recentemente.
- **Alterar Tamanho da Lista** — defina o número de itens que aparecem na lista.
- **Exportar Lista de Músicas** — exporte a sua lista de músicas reproduzidas recentemente como M3U, CSV ou TXT. Instruções detalhadas disponíveis [aqui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritos

Gira a lista das suas músicas favoritas.

- **Edição Simultânea** — quando ativado, adicionar uma música aos favoritos adiciona-a tanto na biblioteca musical como na secção de ficheiros em simultâneo.
- **Eliminar Lista** — elimine toda a lista de músicas favoritas.
- **Exportar Lista de Músicas** — tal como Recentes, exporte favoritos como M3U, CSV ou TXT.

### Eliminar Biblioteca Musical

Apague a base de dados da biblioteca musical. Os seus ficheiros de música no armazenamento ficam intactos.

## Código de Acesso

Ative o ecrã de código de acesso para proteger os dados da sua aplicação com um código numérico de 4 dígitos. Quando ativado, será pedido para inserir o código de acesso toda vez que a aplicação for iniciada. Combine com iOS Face ID / Touch ID no dispositivo para proteção extra.

## Gestor de Ficheiros

A secção do Gestor de Ficheiros controla como os ficheiros são transferidos, armazenados e pré-visualizados.

### Transferências de Ficheiros

Escolha as suas preferências de rede para descarregar ficheiros para o seu dispositivo.

### Número Máximo de Tarefas Paralelas

Defina o número de fios de transferência paralelos. Um número maior acelera as transferências mas usa mais bateria.

### Tarefas de Transferência de Ficheiros

Exibe as tarefas de carregamento e transferência atualmente ativas.

### Transferências em Segundo Plano

Permita transferências enquanto a aplicação está em segundo plano. Se as transferências em segundo plano consumirem muita energia, o iOS pode suspender a aplicação.

### Guardar Ficheiros Transferidos Em

Escolha o diretório de transferências predefinido, ou peça à aplicação para perguntar sempre.

### Pastas Offline Sincronizadas

Gira a sincronização offline para pastas selecionadas. Para ativar a sincronização offline, toque no botão de três pontos ao lado de uma pasta e selecione **Modo Disponível Offline**. Os novos ficheiros adicionados à pasta cloud são descarregados para o seu dispositivo automaticamente. Leia mais sobre modos offline [aqui](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Intervalo de Tempo

Escolha com que frequência as pastas offline são sincronizadas. **Imediatamente** aciona uma sincronização toda vez que abre a aplicação.

### Mostrar Nomes de Ficheiros Completos

Mostrar nomes de ficheiros completos, incluindo extensões, no gestor de ficheiros.

### Editar Ficheiros Online

Desative a edição de ficheiros online para mudar para o modo só de leitura para os serviços cloud ligados e prevenir eliminações acidentais. Esta ação remove operações de edição de ficheiros da interface de utilizador.

### Copiar Ficheiros ao Abrir

Especifique como a aplicação trata os ficheiros importados de outras aplicações.

### Miniaturas para Ficheiros

Gira e elimine miniaturas de ficheiros geradas para libertar espaço de armazenamento.

### Eliminar Ficheiros Temporários

Limpe a pasta de cache da aplicação para recuperar espaço de armazenamento.

## Editor de Tags de Áudio

Configure o editor de tags de áudio integrado — útil para correção em lote de problemas de artista / álbum / ano / género / capa de álbum em ficheiros cloud e locais.

### Redimensionamento da Capa do Álbum

Escolha o método de redimensionamento usado quando uma capa de álbum é guardada nas tags de áudio.

### Atualizar Ficheiros Online

Quando ativado, a aplicação atualiza automaticamente os metadados de um ficheiro no servidor cloud depois de terminar a edição.

### Eliminar Ficheiro Após Edição Online

Escolha se a aplicação deve eliminar a cópia descarregada depois de terminar a edição de um ficheiro online num servidor cloud.

### Botões do Ecrã Principal

Escolha quais botões são visíveis no ecrã principal do editor de tags de áudio.

Para uma edição em lote mais profunda de muitos ficheiros de uma vez, instale a nossa aplicação companheira **Evertag**.

## Widgets

Ative os widgets para que a aplicação atualize os dados dos widgets durante a reprodução. As atualizações de widgets requerem energia adicional, por isso o interruptor está desativado por predefinição — ative-o apenas se realmente usar widgets no seu Ecrã Inicial ou Ecrã de Bloqueio.

Pode adicionar widgets do Flacbox pressionando longamente o seu Ecrã Inicial ou Ecrã de Bloqueio, tocando em **+**, pesquisando **Flacbox** e escolhendo um tamanho de widget. Os widgets mostram a capa atual, título da faixa e artista, e tocam diretamente para o leitor em ecrã completo. Os widgets também funcionam no macOS no Centro de Notificações.

## CarPlay

Altere as definições do CarPlay aqui. Este menu também está disponível dentro da interface CarPlay para poder ajustar a experiência enquanto conduz.

### Ordenar

Configure as opções de ordenação para todos os ecrãs do CarPlay.

### Limite de Carregamento de Conteúdo

Escolha se a aplicação usa paginação no ecrã CarPlay. A paginação mantém os menus responsivos em bibliotecas grandes.

### Cor do Gradiente dos Ícones do Menu

Selecione o esquema de cores para o ecrã inicial do CarPlay.

### Mostrar Imagens

Desative imagens no ecrã CarPlay para otimizar a velocidade de carregamento e reduzir o uso de memória em bibliotecas grandes.

### Pausar Reprodução ao Ligar

Ative isto para evitar áudio alto repentino quando liga o seu dispositivo ao CarPlay.

## Wi-Fi Drive

Ative o **Wi-Fi Drive** para transferir ficheiros de um computador para o seu dispositivo usando um navegador web de desktop, Finder ou Explorador de Ficheiros. Instruções detalhadas sobre como usar o Wi-Fi Drive estão disponíveis [aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalização

Personalize a interface de utilizador de acordo com as suas preferências.

### Ícone da Aplicação

Escolha um ícone de aplicação alternativo para o seu Ecrã Inicial (Premium).

### Esquema de Cores

Escolha o tema da interface de utilizador e ative o modo escuro. Quando **Predefinido** está selecionado, a aplicação segue as definições de aparência do dispositivo.

### Estilo de Fundo

Modifique o estilo de fundo da aplicação. Atualmente a única opção é **Capa de Álbum Desfocada**, que usa a capa da faixa em reprodução como fundo desfocado da aplicação.

### Aparência dos Itens na Lista

Ajuste como os itens são exibidos nas listas. Útil em ecrãs pequenos — pode deixar a aplicação ajustar automaticamente a altura da linha com base no conteúdo, ou mostrar ícones menores nas células da lista.

### Limite de Carregamento de Conteúdo

Por predefinição, a aplicação usa paginação para acelerar o carregamento de conteúdo. Pode desativar a paginação para carregar tudo de uma vez.

### Estilo do Ecrã de Ficheiros Locais

Altere o estilo de apresentação da secção **Ficheiros Locais**.

### Estilo do Ecrã da Biblioteca Musical

Personalize o aspeto do ecrã da **Biblioteca Musical**.

### Estilo do Ecrã do Leitor de Áudio

Configure o aspeto do ecrã do **Leitor de Áudio**.

### Estilo do Menu de Contexto

Escolha o estilo do menu de contexto mostrado quando toca no botão **Mais Ações**.

## Janela

Disponível no Mac e Catalyst. Configure preferências relacionadas com a janela, como o tamanho predefinido e o comportamento no início.

## Ecrã

Escolha se o ecrã deve permanecer ativo enquanto estiver a usar a aplicação. Útil ao analisar bibliotecas grandes ou ao fazer trabalho prolongado de edição de tags.

## Acessibilidade

Ative o **Modo de Texto** para ocultar todas as imagens na interface de utilizador. O Modo de Texto é ativado automaticamente quando o VoiceOver está ativo e também é útil para configurações muito pequenas ou apenas de texto.

## Idioma

Altere o idioma da aplicação e substitua o predefinido do sistema. A alteração aplica-se depois de fechar completamente e reabrir o Flacbox. As localizações atualmente suportadas incluem: Africâner, Akan, Albanês, Amárico, Árabe, Arménio, Assamês, Aimará, Azerbaijano, Bambara, Bengali, Basco, Bielorrusso, Bósnio, Búlgaro, Birmanês, Catalão, Cebuano, Chinês (Simplificado), Chinês (Tradicional), Corso, Croata, Checo, Dinamarquês, Dhivehi, Dogri, Holandês, Inglês, Esperanto, Estónico, Ewe, Filipino, Finlandês, Francês, Galego, Ganda, Georgiano, Alemão, Grego, Guarani, Gujarati, Crioulo Haitiano, Hausa, Havaiano, Hebraico, Hindi, Hmong, Húngaro, Islandês, Igbo, Iloko, Indonésio, Irlandês, Italiano, Japonês, Javanês, Canarês, Cazaque, Khmer, Kinyarwanda, Coreano, Krio, Curdo, Curdo Sorani, Quirguiz, Laociano, Latim, Letão, Lingala, Lituano, Luxemburguês, Macedónico, Maithili, Malgaxe, Malaio, Malaiala, Maltês, Maori, Marata, Mizo, Mongol, Nepalês, Sotho do Norte, Norueguês Bokmål, Nyanja, Odia, Oromo, Pashto, Persa, Polaco, Português, Punjabi, Romeno, Russo, Samoano, Sânscrito, Gaélico Escocês, Sérvio, Shona, Sindhi, Cingalês, Eslovaco, Esloveno, Somali, Sotho do Sul, Espanhol, Sundanês, Suaíli, Sueco, Tajique, Tâmil, Tatar, Telugu, Tailandês, Tsonga, Turco, Turcomano, Ucraniano, Urdu, Uigur, Uzbeque, Vietnamita, Galês, Xhosa, Iídiche, Ioruba, Zulu.

## Cópia de Segurança e Restauro

Use esta funcionalidade para fazer cópia de segurança de todos os dados da sua aplicação ou migrá-los para outro dispositivo. Pode escolher o que incluir:

- **Base de Dados** — todas as suas faixas na biblioteca musical, incluindo listas de reprodução. As faixas offline não estão incluídas para manter o tamanho do ficheiro de cópia de segurança gerível.
- **Capas de Álbuns** — todas as capas de álbuns em cache.
- **Configurações** — todas as definições da sua aplicação.

Toque em **Fazer Cópia de Segurança dos Dados da Aplicação** para iniciar a cópia de segurança. Os dados da aplicação são escritos num único ficheiro que pode usar mais tarde para restaurar o estado da aplicação num novo dispositivo ou depois de reinstalar a aplicação.

Para restaurar dados da aplicação num novo dispositivo, mova o ficheiro de cópia de segurança para o novo dispositivo usando um serviço cloud ligado ou iCloud e abra-o no novo dispositivo.

Instruções detalhadas passo a passo: [Como Transferir a Sua Biblioteca Musical Entre Dispositivos: Guia Passo a Passo](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Ajuda

Aceda ao guia da aplicação para assistência e orientação sobre como usar a aplicação de forma eficaz.

## Perguntas Frequentes

Encontre respostas a perguntas comuns na secção FAQ.

## Enviar Comentários

Tem comentários ou precisa de assistência? Envie os seus comentários diretamente da aplicação para a nossa equipa de suporte.

## Partilhar Esta Aplicação

Partilhe a aplicação com os seus amigos para divulgar a palavra.

## Descobrir Mais Aplicações

Explore outras aplicações da Everappz.

## Termos e Condições

Descreve os termos e condições para usar a aplicação. Por favor leia-os antes de usar a aplicação.

## Política de Privacidade

Visite a página da política de privacidade para compreender as nossas práticas de tratamento de dados. Por favor leia-a antes de usar a aplicação.

## Análise e Recolha de Dados

Verifique quais serviços estão ativados para análise e recolha de dados e desative os que não quer.

## Avisos Legais

Contém informações sobre cada biblioteca usada na aplicação juntamente com o número de versão da aplicação e informações de compilação.
