---
title: "Configurações"
date: 2020-01-01
description: "Explore todas as configurações no Evermusic, incluindo configuração de áudio, sincronização da biblioteca de música, pastas offline, metadados, personalização, acessibilidade, widgets, CarPlay e opções de backup."
keywords: [
  "Evermusic", "configurações", "configurações de áudio", "sincronização da biblioteca de música",
  "pastas offline", "equalizador", "crossfade", "reprodução gapless",
  "processador de áudio", "configurações de listas de reprodução", "atualização premium",
  "restaurar compras", "gestor de ficheiros", "editor de tags", "WiFi drive",
  "voiceover", "backup da aplicação", "acessibilidade", "localização",
  "widgets", "CarPlay", "áudio espacial", "pitch de áudio"
]
tags: ["evermusic", "guia", "configurações"]
readingTime: 16
---


O ecrã de Configurações é o centro de controlo do Evermusic. A partir daqui pode atualizar para Premium, configurar o leitor de áudio, gerir a sua biblioteca de música, configurar o gestor de ficheiros, personalizar a interface, ativar widgets e CarPlay, fazer backup dos seus dados e aceder a ajuda e informações legais. As secções estão agrupadas sob cabeçalhos: **Compras e atualizações**, preferências da aplicação, **Ajuda** e **Legal e privacidade**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecrã de Configurações do Evermusic" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Compras e Atualizações

### Atualizar para Premium

Atualize a aplicação para a versão Premium para remover todos os limites. A versão gratuita oferece uma compra vitalícia na aplicação e duas opções de subscrição que desbloqueiam o conjunto completo de funcionalidades.

A Partilha Familiar está ativada para todas as compras e planos, pelo que pode partilhar a versão Premium com membros da sua família.

Pode ler mais sobre compras e a versão Premium aqui: [Qual é a diferença entre Evermusic e Evermusic Premium](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (ícone azul) vs Evermusic Pro (ícone vermelho)

O Evermusic é publicado na App Store sob dois ícones/cores diferentes:

- **Evermusic Free (ícone azul)** está dividido em **duas aplicações App Store separadas com IDs de pacote diferentes** — uma para **iOS/iPadOS** e uma dedicada para **macOS** (binário Universal que funciona em **Apple Silicon e Intel Macs**). As compras Premium na aplicação são **partilhadas entre as aplicações azuis para iOS e Mac via iCloud** — compre Premium no iPhone e ativa automaticamente no Mac (e vice-versa), desde que ambos os dispositivos usem o mesmo Apple ID com iCloud ativado.
- **Evermusic Pro (ícone vermelho)** é uma **única aplicação App Store** com um **único ID de pacote** que funciona em **iPhone, iPad e Apple Silicon Macs (M1 e posteriores)**. Tem a **mesma funcionalidade que o Evermusic Free com um plano Premium ativado**. A aplicação vermelha **não suporta Intel Macs**, razão pela qual o seu preço é ligeiramente inferior ao da compra Premium equivalente na aplicação azul. O Evermusic Pro também **não recolhe quaisquer diagnósticos ou análises do utilizador** — as análises estão completamente desativadas na compilação, sem opção de adesão.

Como os IDs de pacote diferem entre o azul e o vermelho, uma compra Premium na aplicação ativada na aplicação azul não desbloqueia a aplicação vermelha gratuitamente, e vice-versa. Se já usa a aplicação azul com Premium ativado, não há necessidade de instalar a aplicação vermelha — já tem tudo o que o Pro oferece.

### Partilhar Compras Entre iOS e Mac

As compras vitalícias e subscrições são partilhadas entre iOS e Mac usando iCloud. Se já possui Premium no iOS, certifique-se de que tem a versão mais recente instalada e que o iCloud está ativado. Inicie a aplicação no iOS e aguarde um minuto para que as suas informações de compra sejam carregadas para o iCloud.

Também pode tocar em **Restaurar Compras** nas configurações da aplicação. Em seguida, instale a versão mais recente da aplicação a partir da App Store no Mac e inicie a aplicação. Certifique-se de que tem ligação à internet e está registado com a mesma conta iCloud e App Store em ambos os dispositivos. Aguarde um minuto para que a aplicação descarregue as informações de compra do iCloud. A versão Premium deve ativar-se automaticamente no Mac.

### Restaurar Compras num Novo Dispositivo

Para restaurar a sua compra num novo dispositivo, use **Compras → Restaurar Compras**. Verá a lista das suas compras. Se algo estiver em falta, verifique se o dispositivo está ligado à mesma conta iTunes que foi usada para fazer as compras e que o iCloud está ativado.

### Experimentar Premium Gratuitamente

Pode atualizar para a versão Premium gratuitamente por tempo limitado usando este menu. Veja um anúncio curto ou partilhe a aplicação com amigos para desbloquear o Premium temporariamente.

### Compras

Restaure compras anteriores a partir deste menu. Se encontrar erros de ativação, tente ativar a opção **Restaurar Compras no Início da Aplicação**.

### Atualização de Software

Toque em **Atualização de Software** para verificar se uma versão mais recente do Evermusic está disponível. A aplicação comparará a sua versão instalada com a versão mais recente na App Store e informará se uma atualização é recomendada.

### O Que Há de Novo

Este menu fica disponível depois de uma nova versão ser lançada. Mostra um resumo das alterações e novas funcionalidades incluídas na atualização mais recente.

## Configurações do Leitor de Áudio

Todas as configurações do leitor de áudio estão agrupadas aqui: equalizador, reprodução crossfade, cache do leitor de áudio, carregamento de músicas e muito mais. As configurações estão organizadas em sub-secções lógicas.

### Geral

Esta sub-secção contém configurações gerais de fila de reprodução, saída de áudio e guardar estado.

#### Modo de Repetição

Especifica o comportamento do leitor de áudio quando uma faixa termina a reprodução:

- **Repetir Tudo** – faz loop de todas as faixas na fila do leitor.
- **Repetir Uma** – repete apenas a faixa atual.
- **Parar ao Repetir** – pausa a reprodução quando a faixa atual termina.
- **Sem Repetição** – deixa a fila reproduzir sem repetir.

#### Modo Aleatório

Reproduz as faixas numa ordem aleatória. Isto mistura a fila e reproduz as faixas uma a uma na nova ordem. Valores disponíveis: **Aleatório desligado** e **Aleatório ligado**.

#### Processador de Áudio

Valores possíveis: **AVFoundation** e **CoreAudio**. Por padrão, o AVFoundation é usado. Devido a um problema conhecido com o AVFoundation no iOS 17.0–17.6, a reprodução crossfade e o equalizador de áudio não podem ser usados ao mesmo tempo. Para usar crossfade e o equalizador nessas versões do iOS, mude para o processador de áudio CoreAudio.

Se tiver problemas com a reprodução gapless usando AVFoundation, experimente também o CoreAudio. As únicas limitações do CoreAudio são a transmissão pela internet de algumas estações de rádio e certos formatos de áudio, já que não suporta todos os formatos de áudio do sistema (como M4A e alguns outros).

#### Taxa de Amostragem de Saída de Áudio

Defina a taxa de amostragem de saída de áudio de 8 KHz a 384 KHz. Esta opção está disponível apenas quando o processador CoreAudio está selecionado.

#### Número de Canais de Saída de Áudio

Defina o número de canais de saída de áudio — **MONO** ou **STEREO**. Esta opção está disponível apenas quando o processador CoreAudio está selecionado.

#### Algoritmo de Pitch de Áudio

Escolha o algoritmo usado para correção de pitch. Os valores disponíveis são **Domínio do Tempo**, **Espectral** e **Varispeed**. Útil se ajustar a velocidade de reprodução e quiser controlar a qualidade de áudio resultante.

#### Áudio Espacial

O áudio espacial usa métodos psicoacústicos para criar uma experiência de áudio mais imersiva em auriculares e arranjos de altifalantes suportados. Valores possíveis: **Desativado**, **Mono e Estéreo**, **Multicanal**, **Mono Estéreo Multicanal**.

#### Modo de Saída de Áudio

Disponível apenas em iOS. Permite ativar o modo misto para que o áudio desta aplicação se misture com outras aplicações. Pode encontrar instruções sobre como usar o modo misto [aqui](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Guardar Posição de Reprodução

Garante que a aplicação guarda e restaura a posição de reprodução para as músicas na sua biblioteca de música.

#### Guardar Estado do Leitor de Áudio

Guarda o estado do leitor de áudio antes de fechar a aplicação, facilitando a retoma de onde parou.

Depois de ambas as funcionalidades estarem ativadas, abra qualquer pasta, álbum, artista ou género. Verá uma ação **Continuar Reprodução** no topo do ecrã, juntamente com a última música guardada e a posição de reprodução. Toque em **Continuar Reprodução** para restaurar. Para retomar a reprodução de um ficheiro individual, basta tocar nesse ficheiro.

### Personalização

Personalize o aspeto do ecrã do leitor de áudio, escolha quais os controlos visíveis no leitor, ecrã de bloqueio e barra de estado, e configure os botões de saltar tempo.

#### Estilo do Ecrã do Leitor de Áudio

Configure o posicionamento das barras de ferramentas e controlos principais no leitor de áudio.

#### Estilo de Deslocamento de Capas de Álbuns

Escolha o estilo de deslocamento para capas de álbuns no ecrã do leitor de áudio.

#### Elementos Adicionais

Ative elementos extra no ecrã do leitor de áudio. **Informações do Formato de Áudio** exibe as informações técnicas da faixa em reprodução acima da capa; **Barra Deslizante de Volume de Áudio** mostra a barra deslizante de saída de áudio abaixo dos controlos de reprodução.

#### Ações no Ecrã Principal

Configure quais botões estão visíveis no ecrã principal do leitor de áudio. As opções disponíveis incluem Modo de Repetição e Aleatório, Música Seguinte e Anterior, Saltar Tempo, Temporizador de Sono, Google Chromecast, AirPlay e Bluetooth, Equalizador de Áudio, Pesquisar, Marcadores, Velocidade, Adicionar Marcador, Adicionar aos Favoritos, Comentários e muito mais.

#### Controlos de Reprodução no Ecrã de Bloqueio

Escolha quais controlos extra estão ativados no ecrã de bloqueio. Valores possíveis: **Saltar Tempo**, **Adicionar Marcador** e **Adicionar aos Favoritos**.

#### Intervalos de Saltar Tempo

Selecione os intervalos de tempo usados pelos botões de Saltar Tempo para frente e para trás.

### Carregamento de Ficheiros

Escolha o tipo de rede usado para transmitir músicas. Opções disponíveis: **Wi-Fi** e **Wi-Fi e Dados Móveis**.

#### Tempo de Pré-carregamento

Defina o intervalo de buffering. Aumente este valor se tiver uma ligação de rede fraca.

#### Usar URL Direto

Quando ativado, um URL direto é usado para carregar a música se o servidor o suportar. Isto pode acelerar o carregamento de músicas mas pode afetar ligeiramente a estabilidade da reprodução.

#### Otimizar Carregamento de Ficheiros

Quando ativado, o sistema otimiza o carregamento de músicas para o processador de áudio AVFoundation, o que pode melhorar a estabilidade da reprodução. A aplicação usa a tecnologia descrita [aqui](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Equalizador de Áudio

Configure o equalizador de áudio. Pode ler mais sobre predefinições e configurações de EQ [aqui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Dispositivos

Ligue a um dispositivo AirPlay ou Google Chromecast (apenas iOS).

### Velocidade de Reprodução

Ajuste a velocidade de reprodução do leitor de áudio. Para um controlo mais preciso, ative a barra deslizante de precisão tocando no ícone de configuração no canto superior direito.

### Reprodução Crossfade

O Crossfade permite que as músicas fluam continuamente numa mistura contínua — a música seguinte começa a reproduzir alguns segundos antes de a atual terminar. O crossfade não está disponível para AirPlay e Google Chromecast. Neste ecrã, escolha quanto tempo a música atual e a seguinte reproduzem simultaneamente. Se tiver problemas com crossfade e o equalizador de áudio ao mesmo tempo, mude o processador de áudio conforme descrito acima.

### Reprodução Gapless

A reprodução gapless garante que as músicas reproduzem sem qualquer interrupção ou silêncio entre elas. É perfeita para música clássica, gravações ao vivo e álbuns conceituais. Se tiver problemas com a reprodução gapless, mude o processador de áudio conforme descrito acima.

### Cache de Reprodução

As músicas na fila do leitor de áudio são descarregadas automaticamente para reprodução suave. Se descarregar ficheiros de áudio manualmente, pode desativar esta opção para evitar duplicados. Pode também configurar o tamanho da cache do leitor de áudio aqui. Leia mais sobre o modo offline e cache de reprodução aqui: [Reproduzir Música Offline no Evermusic e Flacbox: Descarregar e Sincronizar da Nuvem para Ficheiros Locais](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Temporizador de Sono

Ative um temporizador para parar a reprodução após um tempo limite especificado. Para um controlo mais preciso, ative o modo de precisão tocando no ícone de configuração no canto superior direito.

## Biblioteca

As configurações da biblioteca de música — sincronização automática, leitura de metadados, carregamento de capas de álbuns, listas de reprodução, recentes e favoritos — estão aqui.

### Leitura de Metadados

Quando adiciona faixas à biblioteca, o leitor de metadados processa-as em segundo plano e organiza-as por Artista, Álbum, Género e Compositor. Pode ajustar a velocidade de leitura dos metadados para carregar dados mais rapidamente (ao custo de mais bateria). Pode também desativar completamente o leitor de metadados e mostrar nomes de ficheiros em vez de informações de tags.

O leitor de metadados apenas atualiza a base de dados da biblioteca de música; não altera os ficheiros armazenados na sua conta na nuvem ou armazenamento local. Se precisar de editar metadados de ficheiros de áudio, use o editor de tags incorporado através da ação correspondente no menu de opções.

Quando **Leitura de Metadados em Segundo Plano** está ativada, o leitor continua a trabalhar em modo de segundo plano. Se a aplicação usar muita energia durante a reprodução, o iOS pode suspendê-la.

Se tiver uma grande coleção de música, é aconselhável realizar a sincronização de metadados na versão desktop da aplicação. Pode então transferir a biblioteca de música sincronizada para iOS usando a funcionalidade **Backup e Restauro**.

Quando **Normalizar Codificação de Metadados** está ativado, a aplicação normaliza automaticamente a codificação dos metadados de todas as músicas. Isto corrige problemas onde a codificação de tags de áudio está danificada (por exemplo, após editar ficheiros num PC Windows) e evita que caracteres incorretos apareçam nas informações da faixa.

**Recarregar metadados** marca todos os ficheiros na sua biblioteca de música como tendo metadados em falta, o que faz com que o leitor de metadados atualize cada registo.

**Iniciar Leitura de Metadados** aciona o leitor de metadados manualmente. O progresso é mostrado abaixo da ação.

### Sincronização Online

A sincronização automática de música online adiciona faixas de serviços na nuvem ligados à biblioteca de música automaticamente. Para a ativar, abra as configurações da biblioteca de música e selecione pastas de sincronização.

Com esta opção ativada, a aplicação verifica as pastas selecionadas, identifica ficheiros de áudio suportados e adiciona-os à sua biblioteca. Inicie ou pare a sincronização com a ação de menu correspondente.

A sincronização online funciona apenas quando a aplicação está em primeiro plano, pelo que sincronizar uma grande biblioteca pode demorar algum tempo. Para acelerar, mantenha a aplicação aberta, ligue a uma fonte de energia e ative **Ecrã → Sempre Ativo** nas configurações.

Em alternativa, realize a sincronização online na versão desktop da aplicação e transfira a biblioteca de música para iOS usando **Backup e Restauro**.

Pode também escolher com que frequência a sincronização online é executada. Definir o intervalo para **Imediatamente** desencadeia uma sincronização sempre que abrir a aplicação.

### Sincronização Offline

Configure a sincronização de música offline.

#### Pastas Offline Sincronizadas

Quando marca uma pasta online no servidor na nuvem como disponível offline (usando o menu Mais Ações), ela aparece aqui. O conteúdo da pasta é descarregado para **Ficheiros Locais → Pastas Offline**. Quando a pasta online muda (ficheiros adicionados, removidos ou atualizados), a aplicação verifica as alterações e atualiza a cópia local no seu dispositivo.

Neste ecrã pode iniciar manualmente a sincronização da pasta offline, revelar a pasta offline na sua pasta envolvente e desativar o modo offline para a pasta. Desativar o modo offline remove todas as cópias locais de ficheiros do seu dispositivo.

#### Intervalo de Tempo

Escolha com que frequência a aplicação verifica pastas offline para modificações.

#### Iniciar Análise de Pastas Locais

Analise todas as pastas locais no diretório Documentos da aplicação em busca de ficheiros de áudio suportados. Os ficheiros encontrados são adicionados automaticamente à biblioteca de música. Os ficheiros localizados no seu dispositivo mas fora do diretório Documentos da aplicação devem ser adicionados à biblioteca de música manualmente, pois a aplicação não pode aceder a eles devido às restrições de segurança do iOS/macOS.

**Importante:** É aconselhável iniciar periodicamente a sincronização de música offline para manter a sua biblioteca de música atualizada com os seus ficheiros locais.

### Personalização

Configure o estilo do ecrã da biblioteca de música. Três opções estão disponíveis: **Menu simples**, **Menu agrupado** e **Menu com separadores**. Pode também ativar ou desativar capas de álbuns no ecrã de detalhes do álbum.

### Capas de Álbuns

Escolha como a aplicação carrega e armazena capas de álbuns.

- **Tipo de rede** — escolha **Wi-Fi** ou **Wi-Fi e Dados Móveis** para descarregamentos de capas.
- **Carregar Capas de Álbuns para Ficheiros Online** — quando ativado, as capas de álbuns incorporadas são carregadas para ficheiros armazenados no armazenamento na nuvem. Isto pode usar dados de rede adicionais.
- **Pesquisar na Pasta** — quando ativado, se uma faixa não tiver capa incorporada, a aplicação procura imagens JPEG ou PNG na mesma pasta e usa-as como capa do álbum.
- **Qualidade da Capa** — selecione a qualidade das capas de álbuns armazenadas no seu dispositivo.
- **Mostrar na Pasta** — abra a pasta onde as capas de álbuns estão em cache para que possa geri-las ou fazer backup.
- **Eliminar Tudo** — elimine capas de álbuns em cache para libertar armazenamento e forçar a aplicação a recarregá-las a pedido.

### Listas de Reprodução

Ative a opção de adicionar a mesma música a uma lista de reprodução duas vezes. Por padrão, esta opção está desativada.

### Recentes

Gira a sua lista de músicas reproduzidas recentemente.

- **Eliminar Lista** — elimine a lista completa de músicas reproduzidas recentemente.
- **Alterar Tamanho da Lista** — defina o número de itens que aparecem na lista.
- **Exportar Lista de Músicas** — exporte a sua lista de músicas reproduzidas recentemente como M3U, CSV ou TXT. As instruções detalhadas estão disponíveis [aqui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritos

Gira a lista das suas músicas favoritas.

- **Edição Simultânea** — quando ativado, adicionar uma música aos favoritos adiciona-a tanto na biblioteca de música como na secção de ficheiros simultaneamente.
- **Eliminar Lista** — elimine a lista completa de músicas favoritas.
- **Exportar Lista de Músicas** — tal como Recentes, exporte os favoritos como M3U, CSV ou TXT.

### Eliminar Biblioteca de Música

Apague a base de dados da biblioteca de música. Os seus ficheiros de música no armazenamento ficam intactos.

## Código de Acesso

Ativa o ecrã de proteção por palavra-passe se quiser proteger os dados da sua aplicação.

## Gestor de Ficheiros

A secção Gestor de Ficheiros controla como os ficheiros são transferidos, armazenados e visualizados.

### Transferências de Ficheiros

Escolha a sua preferência de rede para descarregar ficheiros para o seu dispositivo.

### Número Máximo de Tarefas Paralelas

Defina o número de threads de download paralelos. Um número maior acelera os downloads mas requer mais bateria.

### Tarefas de Transferência de Ficheiros

Mostra as tarefas de envio e descarregamento atualmente ativas.

### Transferências em Segundo Plano

Permita downloads enquanto a aplicação está em segundo plano. Se as transferências em segundo plano consumirem muita energia, o iOS pode suspender a aplicação.

### Guardar Ficheiros Descarregados Em

Escolha o diretório de downloads padrão, ou peça à aplicação que pergunte de cada vez.

### Pastas Offline Sincronizadas

Gira a sincronização offline para pastas selecionadas. Para ativar a sincronização offline, toque no botão de três pontos ao lado de uma pasta e selecione **Modo Disponível Offline**. Os novos ficheiros adicionados à pasta na nuvem são descarregados automaticamente para o seu dispositivo. Leia mais sobre modos offline [aqui](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Intervalo de Tempo

Escolha com que frequência as pastas offline são sincronizadas. **Imediatamente** desencadeia uma sincronização sempre que abrir a aplicação.

### Mostrar Nomes Completos dos Ficheiros

Mostre nomes de ficheiros completos, incluindo extensões, no gestor de ficheiros.

### Editar Ficheiros Online

Desative a edição de ficheiros online para mudar para modo só de leitura para serviços na nuvem ligados e prevenir eliminações acidentais. Esta ação remove operações de edição de ficheiros da interface de utilizador.

### Copiar Ficheiros ao Abrir

Especifique como a aplicação lida com ficheiros importados de outras aplicações.

### Miniaturas de Ficheiros

Gira e elimina miniaturas de ficheiros geradas para libertar espaço de armazenamento.

### Eliminar Ficheiros Temporários

Limpe a pasta de cache da aplicação para recuperar espaço de armazenamento.

## Editor de Tags de Áudio

Configure o editor de tags de áudio incorporado.

### Dimensionamento da Capa do Álbum

Escolha o método de dimensionamento usado quando uma capa de álbum é guardada em tags de áudio.

### Atualizar Ficheiros Online

Quando ativado, a aplicação atualiza automaticamente os metadados de um ficheiro no servidor na nuvem após terminar a sua edição.

### Eliminar Ficheiro Após Edição Online

Escolha se a aplicação deve eliminar a cópia descarregada após terminar a edição de um ficheiro online num servidor na nuvem.

### Botões do Ecrã Principal

Escolha quais botões estão visíveis no ecrã principal do editor de tags de áudio.

## Widgets

Ative widgets para que a aplicação atualize os dados de widgets durante a reprodução. As atualizações de widgets requerem energia adicional, portanto ative isto apenas se usar widgets no seu Ecrã Principal ou Ecrã de Bloqueio.

Pode ler mais sobre os widgets do Evermusic no [Guia de Navegação](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Altere as configurações do CarPlay aqui. Este menu também está disponível dentro da interface CarPlay para que possa ajustar a experiência enquanto conduz.

### Ordenar

Configure opções de ordenação para todos os ecrãs CarPlay.

### Limite de Carregamento de Conteúdo

Escolha se a aplicação usa paginação no ecrã CarPlay. A paginação mantém os menus responsivos em dispositivos com memória limitada e grandes bibliotecas.

### Cor do Gradiente dos Ícones do Menu

Selecione o esquema de cores para o ecrã inicial do CarPlay.

### Mostrar Imagens

Desative imagens no ecrã CarPlay para otimizar a velocidade de carregamento e reduzir o uso de memória em grandes bibliotecas.

### Pausar Reprodução Quando Ligado

Ative isto para evitar áudio alto repentino quando liga o seu dispositivo ao CarPlay.

## Wi-Fi Drive

Ative o Wi-Fi Drive para transferir ficheiros de um computador para o seu dispositivo usando um browser web de ambiente de trabalho. As instruções detalhadas sobre como usar o Wi-Fi Drive estão disponíveis [aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalização

Personalize a interface de utilizador de acordo com as suas preferências.

### Ícone da Aplicação

Escolha um ícone de aplicação alternativo para o seu Ecrã Principal.

### Esquema de Cores

Escolha o tema da interface de utilizador e ative o modo escuro. Quando **Padrão** está selecionado, a aplicação segue as configurações de aparência do sistema.

### Estilo de Fundo

Modifique o estilo de fundo da aplicação. Atualmente a única opção é **Capa de Álbum Desfocada**, que usa a capa da faixa em reprodução como fundo desfocado da aplicação.

### Aparência dos Itens na Lista

Ajuste como os itens são exibidos nas listas. Útil em ecrãs pequenos — pode deixar a aplicação ajustar automaticamente a altura das linhas com base no conteúdo, ou mostrar ícones menores nas células da lista para dar mais espaço ao texto.

### Limite de Carregamento de Conteúdo

Por padrão, a aplicação usa paginação para acelerar o carregamento de conteúdo. Pode desativar a paginação para carregar tudo de uma vez.

### Estilo do Ecrã de Ficheiros Locais

Altere o estilo de apresentação da secção **Ficheiros Locais**.

### Estilo do Ecrã da Biblioteca de Música

Personalize o aspeto do ecrã da **Biblioteca de Música**.

### Estilo do Ecrã do Leitor de Áudio

Configure o aspeto do ecrã do **Leitor de Áudio**.

### Estilo do Menu Contextual

Escolha o estilo do menu contextual mostrado quando toca no botão Mais Ações.

## Janela

Disponível no Mac e Catalyst. Configure as preferências relacionadas com a janela, como o tamanho padrão e o comportamento no início.

## Ecrã

Escolha se o ecrã deve ficar ativo enquanto está a usar a aplicação. Útil ao analisar grandes bibliotecas ou ao fazer trabalho prolongado de edição de tags.

## Acessibilidade

Ative o **Modo de Texto** para ocultar todas as imagens na interface de utilizador. O Modo de Texto é ativado automaticamente quando o VoiceOver está ativo e também é útil para configurações muito pequenas ou apenas de texto.

## Idioma

Altere o idioma da aplicação e substitua o padrão do sistema. Atualmente a aplicação suporta as seguintes localizações: Afrikaans, Akan, Albanês, Amárico, Árabe, Arménio, Assamês, Aimará, Azerbaijanês, Bambara, Bengali, Basco, Bielorrusso, Bósnio, Búlgaro, Birmanês, Catalão, Cebuano, Chinês Simplificado, Chinês Tradicional, Corso, Croata, Checo, Dinamarquês, Divehi, Dogri, Neerlandês, Inglês, Esperanto, Estónio, Ewe, Filipino, Finlandês, Francês, Galego, Ganda, Georgiano, Alemão, Grego, Guarani, Gujarati, Crioulo Haitiano, Hausa, Havaiano, Hebraico, Hindi, Hmong, Húngaro, Islandês, Igbo, Iloko, Indonésio, Irlandês, Italiano, Japonês, Javanês, Canarês, Cazaque, Khmer, Kinyarwanda, Coreano, Krio, Curdo, Curdo Sorani, Quirguiz, Laociano, Latim, Letão, Lingala, Lituano, Luxemburguês, Macedônio, Maithili, Malgaxe, Malaio, Malaiala, Maltês, Māori, Marata, Mizo, Mongol, Nepalês, Soto do Norte, Norueguês Bokmål, Nianja, Odia, Oromo, Pastó, Persa, Polaco, Português, Punjabi, Romeno, Russo, Samoano, Sânscrito, Gaélico Escocês, Sérvio, Shona, Sindi, Cingalês, Eslovaco, Esloveno, Somali, Soto do Sul, Espanhol, Sundanês, Suaíli, Sueco, Tajique, Tâmil, Tatar, Telugu, Tailandês, Tsonga, Turco, Turcomano, Ucraniano, Urdu, Uigur, Uzbeque, Vietnamita, Galês, Xhosa, Iídiche, Ioruba, Zulu.

## Backup e Restauro

Faça backup de todos os dados da sua aplicação ou migre-os para outro dispositivo. Pode escolher o que incluir:

- **Base de dados** — todas as faixas e listas de reprodução da sua biblioteca de música. As faixas offline não estão incluídas para manter o tamanho do backup gerível.
- **Capas de Álbuns** — todas as capas de álbuns em cache.
- **Configurações** — todas as configurações da sua aplicação.

Toque em **Fazer Backup dos Dados da Aplicação** para iniciar a operação de backup. Os dados da aplicação são escritos num único ficheiro que pode usar mais tarde para restaurar o estado da aplicação num novo dispositivo ou após reinstalar a aplicação.

Para restaurar dados da aplicação num novo dispositivo, mova o ficheiro de backup para o novo dispositivo usando um serviço na nuvem ligado ou iCloud e abra-o no novo dispositivo.

Temos um guia detalhado passo a passo aqui: [Como Transferir a Sua Biblioteca de Música Entre Dispositivos no Evermusic: Guia Passo a Passo](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Ajuda

Abra o guia da aplicação para obter assistência e orientação sobre como usar a aplicação eficazmente.

## Perguntas Frequentes

Encontre respostas a perguntas comuns na secção de FAQ.

## Enviar Comentários

Tem comentários ou precisa de assistência? Envie os seus comentários para a nossa equipa de suporte diretamente da aplicação.

## Partilhar Esta Aplicação

Partilhe a aplicação com os seus amigos para ajudar a divulgá-la.

## Descobrir Mais Aplicações

Explore outras aplicações da Everappz.

## Termos e Condições

Descreve os termos e condições para usar a aplicação. Por favor leia antes de usar a aplicação.

## Política de Privacidade

Visite a página da política de privacidade para entender as nossas práticas de tratamento de dados. Por favor leia antes de usar a aplicação.

## Análises e Recolha de Dados

Verifique quais os serviços ativados para análises e recolha de dados e desative quaisquer que não queira.

No **Evermusic Free (ícone azul)**, as análises e diagnósticos estão ativados por padrão para nos ajudar a melhorar a aplicação — pode desativá-los aqui a qualquer momento. **O Evermusic Pro (ícone vermelho) não inclui quaisquer análises ou diagnósticos** — a secção está vazia (ou oculta) porque nada é recolhido, e não há opção de adesão.

## Avisos Legais

Contém informações sobre cada biblioteca usada na aplicação, juntamente com o número de versão da aplicação e informações de compilação.
