---
title: "Como importar lista de reprodução M3U para Evermusic e Flacbox"
date: 2024-01-31
description: "Saiba como importar arquivos de listas de reprodução M3U, M3U8 e CUE da nuvem, armazenamento local ou dispositivo para Evermusic e Flacbox."
keywords: ["evermusic", "flacbox", "lista de reprodução", "m3u", "m3u8", "cue", "importar", "aplicativo de música"]
tags: ["evermusic", "importar", "listas de reprodução", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Resumo:** Evermusic e Flacbox suportam a importação de arquivos de listas de reprodução M3U, M3U8 e CUE do armazenamento em nuvem, arquivos locais do aplicativo ou do seu dispositivo. Vá para Listas de reprodução > Mais > Importar lista de reprodução, selecione uma fonte, escolha seu arquivo e o aplicativo cria sua lista de reprodução automaticamente.

M3U, que significa MP3 URL ou Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, é um formato de arquivo de computador usado para listas de reprodução multimídia. Um de seus usos principais é criar arquivos de listas de reprodução de entrada única que apontam para streams na internet. Esses arquivos oferecem acesso conveniente a conteúdo de streaming e são comumente usados para downloads, e-mails e ouvir rádio pela Internet.

Apesar de seu uso generalizado, não existe uma especificação formal para o formato M3U; ele se tornou um padrão de facto. Um arquivo M3U é essencialmente um arquivo de texto simples que especifica as localizações de um ou mais arquivos de mídia. Dependendo da codificação, é salvo com a extensão "m3u" ou "m3u8". Cada entrada no arquivo especifica a localização de um arquivo de mídia, que pode ser um caminho local absoluto, um caminho local relativo à localização do arquivo M3U ou uma URL. As entradas são separadas por quebras de linha, com alguns dispositivos exigindo quebras de linha representadas como CR LF.

Além disso, arquivos M3U podem incluir comentários prefixados pelo caractere "#". No M3U estendido, "#" introduz diretivas M3U estendidas, que podem suportar parâmetros terminados com dois pontos ":".

Em nossos aplicativos Evermusic e Flacbox, implementamos a funcionalidade de importação de arquivos M3U, eliminando a necessidade de criação manual de listas de reprodução. Este guia irá orientá-lo na importação de suas listas de reprodução do armazenamento em nuvem, arquivos locais ou arquivos do seu dispositivo diretamente no aplicativo.

Primeiro, navegue até a seção 'Listas de reprodução'. Em seguida, toque no botão 'Mais' localizado no canto superior direito. No menu que aparece, selecione a opção 'Importar lista de reprodução'.

![ação de importar lista de reprodução](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Na tela seguinte, escolha a localização do arquivo. As opções suportadas incluem:

- Armazenamento em nuvem conectado;
- Arquivos no aplicativo;
- Arquivos no seu dispositivo;

![selecionar localização do arquivo](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Vamos selecionar o armazenamento em nuvem conectado e abrir a pasta contendo o arquivo da lista de reprodução. As extensões de arquivo de lista de reprodução suportadas incluem M3U, M3U8 e CUE. Selecione o arquivo da lista de reprodução e toque em 'Concluído' para confirmar sua seleção.

![selecionar arquivo M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

O aplicativo analisará o arquivo da lista de reprodução e criará uma lista de faixas. Em seguida, localizará esses arquivos no armazenamento e compilará uma lista de reprodução final que será importada para a biblioteca de música. É crucial que seu arquivo M3U/CUE contenha os caminhos corretos para os arquivos de mídia, e os arquivos devem estar localizados nesses caminhos no seu armazenamento.

![lista de reprodução importada](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

O aplicativo suporta tanto caminhos relativos quanto URLs de arquivo absolutos.

Por exemplo:

Lista de reprodução com caminhos relativos:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Lista de reprodução com URLs absolutos:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Se você importar um arquivo de lista de reprodução localizado dentro do aplicativo (seção Arquivos locais), não são necessários passos adicionais.

No entanto, se você quiser importar uma lista de reprodução localizada no seu dispositivo usando o seletor de arquivos do sistema, há uma consideração importante a ter em mente.

Devido às políticas de segurança, o aplicativo só pode acessar o arquivo que você seleciona usando o seletor de arquivos do sistema. No entanto, o arquivo da lista de reprodução pode incluir links para outros arquivos de mídia no seu dispositivo. Para importar uma lista de reprodução do seu dispositivo, você deve selecionar uma pasta contendo tanto o arquivo da lista de reprodução quanto todos os arquivos de mídia vinculados a ele. Neste caso, o aplicativo verificará a pasta selecionada, encontrará o arquivo da lista de reprodução, construirá a lista de faixas e a importará para a biblioteca de música.

Além disso, você pode importar várias listas de reprodução de uma vez tocando no botão "Mais ações" e selecionando "Importar listas de reprodução de uma pasta". O aplicativo então verificará o conteúdo da pasta, encontrará os arquivos de listas de reprodução suportados e os importará para a biblioteca.

## Perguntas frequentes

{{% details title="Quais formatos de lista de reprodução o Evermusic e o Flacbox suportam?" closed="true" %}}
Ambos os aplicativos suportam os formatos de arquivo de lista de reprodução M3U, M3U8 e CUE. Estes cobrem os padrões de lista de reprodução mais comuns usados por reprodutores de música e software de mídia.
{{% /details %}}

{{% details title="Posso importar listas de reprodução do armazenamento em nuvem?" closed="true" %}}
Sim. Você pode importar arquivos de listas de reprodução de qualquer serviço de armazenamento em nuvem conectado, incluindo Google Drive, Dropbox, OneDrive e servidores WebDAV.
{{% /details %}}

{{% details title="Por que algumas faixas estão faltando após a importação?" closed="true" %}}
O arquivo da lista de reprodução deve conter caminhos corretos para seus arquivos de mídia, e esses arquivos devem existir nas localizações especificadas no seu armazenamento. Verifique se os caminhos de arquivo no seu arquivo M3U ou CUE correspondem às localizações reais dos arquivos.
{{% /details %}}

{{% details title="Posso importar várias listas de reprodução de uma vez?" closed="true" %}}
Sim. Use o botão Mais ações e selecione "Importar listas de reprodução de uma pasta". O aplicativo verifica a pasta em busca de todos os arquivos de listas de reprodução suportados e os importa em uma única etapa.
{{% /details %}}

{{% details title="Preciso criar listas de reprodução manualmente?" closed="true" %}}
Não. O recurso de importação elimina a criação manual de listas de reprodução. Basta apontar o aplicativo para seu arquivo M3U, M3U8 ou CUE existente e ele cria a lista de reprodução automaticamente.
{{% /details %}}
