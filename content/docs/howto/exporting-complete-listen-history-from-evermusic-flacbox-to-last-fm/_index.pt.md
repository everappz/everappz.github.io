---
title: "Exporte seu histórico completo de audição do Evermusic e Flacbox para o Last.fm"
date: 2024-01-30
description: "Aprenda como exportar seu histórico de músicas do Evermusic e Flacbox e enviá-lo para o Last.fm usando arquivos CSV e a ferramenta Last.fm Scrubbler para Windows."
keywords: ["evermusic", "flacbox", "lastfm", "histórico de músicas", "scrobbling", "exportar faixas", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "recentes", "lastfm", "exportar", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Resumo:** Exporte seu histórico de audição do Evermusic ou Flacbox como um arquivo CSV e depois envie-o para o Last.fm usando a ferramenta gratuita Last.fm-Scrubbler-WPF no Windows. O scrobbling automático também está disponível nativamente em ambos os aplicativos.

**Atualização:** O scrobbling automático já está disponível! Saiba mais aqui: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling é uma maneira simples de salvar automaticamente detalhes básicos como o título e o artista da música que você está ouvindo em um serviço online. Depois, você pode revisar seu histórico de audição.

[Last.fm](https://www.last.fm/home), alimentado por um sistema de recomendação musical chamado Audioscrobbler, oferece este serviço gratuitamente. Ele cria um perfil detalhado do seu gosto musical registrando as faixas que você ouve, seja de estações de rádio pela internet, do seu computador ou de diversos dispositivos de música portáteis. Você pode visitar o site posteriormente para receber recomendações de novos artistas ou álbuns que combinem com seu gosto musical.

Você pode enviar seu histórico de audição para o [Last.fm](http://Last.fm) a partir dos aplicativos Evermusic e Flacbox usando uma ferramenta gratuita, e vamos mostrar como fazer isso.

Abra a seção 'Biblioteca de Música' do aplicativo e role até a seção 'Acesso rápido'. Toque no item de menu 'Recentes'.

![tela da biblioteca de música](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Na tela 'Recentes', toque no botão 'Mais' no canto superior direito para ativar o menu 'Mais ações'. Toque no item de menu 'Exportar lista de músicas'.

![tela de recentes](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Na tela 'Selecionar formato de arquivo', você tem a possibilidade de selecionar o formato do arquivo de destino. Opções disponíveis - CSV, TXT, M3U.

![tela de seleção de formato de arquivo](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Significa Comma-Separated Values, perfeito para organizar seus dados em um formato de tabela organizado. No arquivo de destino, você encontrará parâmetros como Nome do Artista, Nome do Álbum, Nome da Faixa, Carimbo de Data/Hora (o momento em que você ouviu as faixas), Nome do Artista do Álbum e Duração da Faixa.

TXT: Aqui estamos falando de um arquivo de texto simples. É simples e direto, com parâmetros incluindo Nome do Artista, Nome do Álbum, Nome da Faixa e Duração.

M3U: Este formato é essencialmente a escolha padrão para criar playlists. É ótimo porque você pode exportar sua lista de músicas e curtir suas faixas em qualquer dispositivo, mesmo que você não tenha os arquivos originais (desde que selecione a opção de URL absoluta para os arquivos de mídia). No arquivo de saída, você encontrará parâmetros como Duração, Nome do Artista, Nome da Faixa e Localização do Arquivo de Mídia.

Para nossa tarefa, selecionar CSV é a escolha certa. Usaremos este arquivo com o software gratuito Last.fm-Scrubbler-WPF para enviar nosso histórico de audição para o serviço [Last.fm](http://Last.fm). Simplesmente escolha CSV e pressione o botão 'Exportar'.

![tela de exportação concluída](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Após a exportação ser concluída, simplesmente toque no botão 'Mostrar arquivo', e o aplicativo revelará o arquivo criado na sua pasta de documentos. Em seguida, toque no botão 'Mais ações' ao lado do nome do arquivo e selecione a opção 'Abrir em' no menu. Nosso próximo passo é copiar o arquivo exportado para o seu computador desktop. Você pode fazer isso facilmente selecionando a opção AirDrop no menu 'Abrir em'.

![mais ações para o arquivo exportado](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

A seguir, usaremos um cliente gratuito de código aberto do [Last.FM](http://Last.FM) que está disponível apenas na plataforma Windows. Este cliente permite que você atualize eficientemente seu histórico de audição no [Last.FM](http://Last.FM) usando o arquivo CSV que acabamos de exportar.

Agora, se você não está usando um computador Windows no momento, não se preocupe. Você ainda pode acessar este cliente instalando o VirtualBox no seu Mac e usando o arquivo de imagem oficial do ambiente de desenvolvimento do Windows.

Aqui está o que você precisa fazer:

- Instale o VirtualBox no seguinte link: [Baixar VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Baixe e instale o ambiente de desenvolvimento do Windows neste link: [Ambiente de Desenvolvimento Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

No seu computador Windows (ou no aplicativo VirtualBox com a imagem Windows Development) baixe e instale o [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - software gratuito de código aberto disponível no GitHub. Testamos na versão 1.28 que você pode baixar aqui: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Página de download do Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Na seção 'Assets', clique em [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) para baixar o arquivo de instalação. Descompacte o arquivo baixado e abra a pasta descompactada.

- IMPORTANTE

Este aplicativo ainda está em beta. Os criadores do aplicativo não fizeram muitos testes. Eles recomendam tentar fazer scrobble em uma conta de teste primeiro e verificar se as coisas que você quer scrobblar funcionam corretamente. Especialmente se você fizer scrobble de muitas faixas de uma vez. Por favor, tenha cuidado com suas contas.

Execute o Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Na tela principal do aplicativo, simplesmente clique em 'Não conectado', localizado no canto inferior esquerdo, para ativar a tela 'Adicionar conta'.

![Tela de adicionar conta](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Insira suas credenciais de login.

![tela de inserir credenciais de login](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Clique no botão 'Login' para adicionar sua conta.

![Clique no botão Login para adicionar sua conta.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Abra a aba 'File Parse Scrobbler' para começar a importar o arquivo CSV do aplicativo Evermusic.

![Abra a aba File Parse Scrobbler para começar a importar o arquivo CSV do aplicativo Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Escolha 'Parser: CSV' e clique no botão 'Settings'.

Na tela seguinte, você pode escolher a ordem dos parâmetros no seu arquivo CSV.

Campos individuais podem ser delimitados por aspas e PRECISAM ser delimitados por aspas se o campo contiver qualquer um dos delimitadores definidos. Por exemplo:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Portanto, deixe todas as configurações padrão; a única coisa que você precisa alterar é ativar a caixa de seleção no campo 'Has Fields Enclosed In Quotes'.

Clique em 'Save & Close' para aplicar as alterações.

![escolha a ordem dos parâmetros no seu arquivo CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

O scrobbling por análise de arquivo tem dois modos. Eles podem ser alterados com o ComboBox 'Scrobbling Mode'.

Modo Normal: Neste modo, as faixas serão scrobbladas com o carimbo de data/hora do scrobble analisado. Apenas scrobbles mais recentes que 14 dias podem ser scrobblados.

Modo Importação: Neste modo, as faixas serão scrobbladas com o carimbo de data/hora calculado a partir do 'Finish Time' e da duração selecionada entre cada faixa. Isso permite o scrobbling das faixas mesmo que o carimbo de data/hora do scrobble analisado seja mais antigo que 14 dias. Portanto, a primeira faixa (mais acima) no arquivo CSV será scrobblada com o 'Finish Time'.

Escolha um arquivo CSV gerado anteriormente pelo aplicativo Evermusic no campo 'File:' e clique em 'Parse'. Em alguns casos, você pode ver um alerta de erro dizendo que alguns scrobbles não puderam ser analisados. Não há problema se você tiver algumas faixas sem metadados completos como Nome do Artista.

![alguns scrobbles não puderam ser analisados](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Clique no botão 'Check All' para selecionar todas as faixas analisadas.

![Clique no botão Check All para selecionar todas as faixas analisadas.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Clique no botão 'Preview' para verificar todas as alterações que serão enviadas ao servidor.

![Clique no botão Preview para verificar todas as alterações que serão enviadas ao servidor.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Clique no botão 'Scrobble' para enviar todas as alterações ao servidor.

![Clique no botão Scrobble para enviar todas as alterações ao servidor.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Anteriormente, o Last.fm-Scrubbler-WPF não tinha um limite de scrobbles por dia. Isso mudou agora, pois algumas pessoas usaram o Scrubbler para scrobblar tantas faixas que causou problemas para a página do Last.fm. O limite de scrobbles é atualmente de 2800 scrobbles por dia. Quando você tenta scrobblar mais do que isso, receberá uma mensagem de erro. Há planos para adicionar uma 'fila de scrobbles', para que se você precisar scrobblar mais de 2800 faixas, elas sejam adicionadas a uma fila e scrobbladas automaticamente após algum tempo. Você pode verificar quantos scrobbles restam na visualização de seleção de usuário.

Quando todos os registros forem enviados com sucesso ao servidor, você verá uma mensagem na parte inferior da janela do aplicativo confirmando: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Agora você pode abrir seu perfil na página do [Last.fm](http://Last.fm) e verificar todas as alterações.

![seu perfil na página do Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Perguntas frequentes

{{% details title="Posso fazer scrobble automaticamente sem exportar arquivos CSV?" closed="true" %}}
Sim. Tanto o Evermusic quanto o Flacbox agora suportam scrobbling automático para o Last.fm. Veja o guia: [Como fazer scrobble para o Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="E se meu CSV tiver faixas com mais de 14 dias?" closed="true" %}}
Use o Modo Importação no Last.fm-Scrubbler-WPF. Ele recalcula os carimbos de data/hora a partir do Finish Time, permitindo que você faça scrobble de faixas independentemente da data original.
{{% /details %}}

{{% details title="Não tenho um computador Windows. Posso usar o Last.fm-Scrubbler mesmo assim?" closed="true" %}}
Sim. Instale o VirtualBox no seu Mac e baixe a imagem gratuita do Ambiente de Desenvolvimento Windows da Microsoft. Execute o Last.fm-Scrubbler-WPF dentro da máquina virtual.
{{% /details %}}

{{% details title="Por que alguns scrobbles não foram analisados?" closed="true" %}}
Faixas sem metadados essenciais (como nome do artista) não podem ser analisadas. Isso é esperado e não afeta outras faixas no arquivo.
{{% /details %}}

{{% details title="Existe um limite diário de scrobbles?" closed="true" %}}
Sim. O Last.fm-Scrubbler-WPF permite até 2.800 scrobbles por dia. Se você precisar fazer mais scrobbles, divida o processo em vários dias.
{{% /details %}}
