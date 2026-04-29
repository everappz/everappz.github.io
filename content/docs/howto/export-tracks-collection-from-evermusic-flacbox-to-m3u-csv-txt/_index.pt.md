---
title: "Como exportar a coleção de faixas para M3U, CSV e TXT no Evermusic e Flacbox"
date: 2024-01-31
description: "Aprenda a exportar recentes, favoritos, playlists e álbuns do Evermusic e Flacbox para os formatos M3U, CSV ou TXT. Perfeito para scrobbling no Last.fm e reprodução em outros dispositivos."
keywords: ["evermusic exportar", "flacbox exportar", "exportar para m3u", "exportar playlist para csv", "m3u txt csv playlist", "exportação de música"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**Resumo:** Evermusic e Flacbox permitem exportar qualquer coleção de faixas (recentes, favoritos, playlists, álbuns) para arquivos CSV, TXT ou M3U. Use essas exportações para fazer scrobbling no Last.fm, criar backup da sua biblioteca ou reproduzir suas playlists em outros dispositivos.

## Introdução

Exportar seus recentes, favoritos, álbuns e playlists do aplicativo para um arquivo externo pode ser incrivelmente útil. Você pode usar esses arquivos para atualizar seu histórico de reprodução em serviços de scrobbling como o [Last.fm](http://Last.fm), ou ouvir suas playlists em dispositivos externos. Com o Evermusic e o Flacbox, esse processo é fácil. Aqui, mostraremos como exportar seus recentes para CSV/TXT e suas playlists para M3U. No entanto, essa funcionalidade está disponível para qualquer coleção de faixas dentro do aplicativo.

## Escolha o formato

Para exportar seus recentes, abra a seção «Biblioteca de música» e selecione o item de menu «Recentes».

![biblioteca de música](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Na próxima tela, toque no botão «Mais» no canto superior direito e escolha «Exportar lista de músicas».

![exportar recentes](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Na tela «Selecionar formato de arquivo», você tem várias opções – CSV, TXT, M3U.

- CSV

Significa Comma-Separated Values, perfeito para organizar seus dados em um formato de tabela organizado. No arquivo de destino, você encontrará parâmetros como nome do artista, nome do álbum, nome da faixa, carimbo de data/hora (o momento em que você ouviu as faixas), nome do artista do álbum e duração da faixa. Você pode usar esse arquivo posteriormente para atualizar seu histórico de reprodução em serviços de scrobbling como o [Last.fm](http://Last.fm), conforme descrito [aqui](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Aqui estamos falando de um arquivo de texto simples. É direto e objetivo, com parâmetros que incluem nome do artista, nome do álbum, nome da faixa e duração. Útil se você precisa apenas de uma lista de faixas em formato texto.

- M3U

Este formato é essencialmente o padrão para criação de playlists. É ótimo porque você pode exportar sua lista de músicas e curtir suas faixas em qualquer dispositivo, mesmo que não tenha os arquivos originais (se selecionar a opção de URL absoluto para exportação dos arquivos de mídia). No arquivo de saída, você encontrará parâmetros como duração, nome do artista, nome da faixa e localização do arquivo de mídia.

## Formato CSV

Agora, vamos selecionar CSV e ver o que receberemos. Basta escolher CSV e tocar no botão «Exportar».

![selecionar formato de arquivo](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Quando a exportação for concluída, você verá um alerta com duas opções. Tocar em «Mostrar arquivo» revelará o arquivo resultante no diretório de documentos.

![exportação concluída](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Agora você pode enviar esse arquivo, abri-lo em um editor de texto externo ou usá-lo para atualizar seu progresso de reprodução no [Last.fm](http://Last.fm).

![pasta de exportação com arquivos resultantes](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

O arquivo CSV de saída conterá campos no seguinte formato:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Por exemplo:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![arquivo csv exportado](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Formato TXT

O arquivo TXT de saída conterá campos no seguinte formato:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Por exemplo:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![arquivo txt exportado](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Formato M3U

A seguir, vamos guiá-lo pela exportação da sua playlist para o formato M3U, que é o padrão de facto para arquivos de playlist. O principal pré-requisito para uma exportação de playlist bem-sucedida é que todos os arquivos na playlist devem estar localizados no mesmo armazenamento, seja em um serviço de nuvem como o Google Drive, arquivos locais ou arquivos no seu dispositivo. Para iniciar o processo de exportação, abra qualquer playlist e toque no botão «Mais» no canto superior direito, depois escolha o item de menu «Exportar lista de músicas».

![tela da playlist](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Na próxima tela, selecione o formato de arquivo «M3U», onde você encontrará duas opções para «Tipo de localização do arquivo de mídia»:

![tela de seleção do formato de exportação](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Se você escolher «Caminho relativo», a playlist será criada com as localizações dos arquivos de mídia escritas em relação ao arquivo da playlist. Por exemplo:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Neste caso, evite alterar a localização do arquivo M3U após a conclusão da exportação, pois isso quebrará os caminhos dos arquivos de mídia. Para iniciar a reprodução da sua playlist, basta tocar no arquivo de playlist exportado, e o aplicativo localizará automaticamente os arquivos de mídia no seu armazenamento e iniciará a reprodução. Você pode até exportar suas playlists para o armazenamento e depois importá-las novamente no seu novo dispositivo.

2. Se você escolher «URL absoluto», o aplicativo gerará URLs diretas para seus arquivos de mídia. Isso permite reproduzir a playlist em qualquer dispositivo/aplicativo sem precisar que todos os arquivos de mídia estejam no mesmo armazenamento que o arquivo da playlist. Esta opção é suportada apenas para armazenamento em nuvem capaz de gerar URLs diretas de arquivos. No entanto, tenha em mente que, em alguns casos, as URLs geradas podem ter um tempo de vida limitado e podem expirar após algum tempo. Aqui está a lista de serviços de nuvem suportados: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (se em modo convidado)  

A URL do arquivo de mídia de saída será algo como:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Após selecionar o «Tipo de localização do arquivo de mídia», toque em «Exportar». O aplicativo pedirá que você escolha uma pasta de destino para exportar o arquivo M3U. Toque em «Concluído» para confirmar sua seleção.

![selecionar uma pasta](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

O aplicativo gerará um arquivo M3U e fará o upload/moverá para a pasta de destino.

![enviando arquivo m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Quando a exportação for concluída, um alerta do sistema aparecerá com a opção de «Mostrar arquivo».

![alerta de exportação concluída](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Tocar nisto revelará o arquivo exportado no aplicativo.

![arquivo m3u exportado na lista de arquivos](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Se você selecionou «Caminho relativo» como «Tipo de localização do arquivo de mídia» no passo anterior, o arquivo de saída estará no seguinte formato:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![exemplo m3u com caminhos relativos](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Para a opção «URL absoluto», o aplicativo gerará um arquivo M3U no formato:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![exemplo m3u com URLs absolutas de arquivos](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Você pode abrir esse arquivo em qualquer dispositivo/aplicativo que suporte playlists M3U.

![playlist m3u aberta em aplicativo externo](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Considerações finais

Exportar suas faixas do Evermusic e Flacbox dá a você controle total sobre seus dados musicais. Seja para fazer backup do histórico de reprodução, scrobbling no Last.fm ou curtir playlists em dispositivos externos, essas opções de exportação – M3U, CSV e TXT – são ferramentas poderosas projetadas para flexibilidade e compatibilidade. Aproveite esses recursos para melhorar a forma como você organiza, compartilha e revisita sua coleção musical em diferentes plataformas.

## FAQ

{{% details title="Qual formato de exportação devo usar para scrobbling no Last.fm?" closed="true" %}}
Use CSV. Ele inclui carimbos de data/hora e metadados completos necessários por ferramentas de scrobbling como o Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Posso exportar qualquer coleção de faixas, não apenas playlists?" closed="true" %}}
Sim. Você pode exportar recentes, favoritos, álbuns, playlists e qualquer outra coleção de faixas no aplicativo usando os mesmos passos.
{{% /details %}}

{{% details title="Minha playlist M3U funcionará em outros dispositivos?" closed="true" %}}
Se você escolher a opção URL absoluto durante a exportação, o arquivo M3U pode ser reproduzido em qualquer dispositivo que suporte playlists M3U. Note que algumas URLs de nuvem podem expirar com o tempo.
{{% /details %}}

{{% details title="O recurso de exportação é gratuito?" closed="true" %}}
Sim. A exportação de coleções de faixas para M3U, CSV e TXT está disponível nas versões gratuita e premium do Evermusic e Flacbox.
{{% /details %}}

{{% details title="Quais serviços de nuvem suportam exportação com URL absoluto?" closed="true" %}}
A exportação com URL absoluto é suportada para iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive e WebDAV (modo convidado).
{{% /details %}}
