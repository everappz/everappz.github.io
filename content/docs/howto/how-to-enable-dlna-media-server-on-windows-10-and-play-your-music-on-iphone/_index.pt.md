---
title: "Como ativar o servidor de mídia DLNA no Windows 10 e reproduzir sua música no iPhone"
date: 2019-11-26
description: "Ative o servidor DLNA no Windows 10 e transmita sua música para o iPhone com o aplicativo Evermusic. Guia de configuração passo a passo incluído."
keywords: ["evermusic", "dlna", "windows 10", "streaming de música no iphone", "servidor de mídia", "rede local", "upnp"]
tags: ["evermusic", "música", "nuvem", "iphone", "armazenamento", "local", "nas", "windows", "wifi", "ouvir", "rede", "remoto", "casa", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Resumo:** O Windows 10 tem um servidor DLNA integrado. Ative-o nas configurações de Rede e Compartilhamento e depois use o aplicativo gratuito **Evermusic** no seu iPhone para transmitir toda a sua biblioteca musical via Wi-Fi. Nenhum software de servidor de terceiros é necessário.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Capa" caption="Streaming de música DLNA para iPhone usando Windows 10 e Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) é uma ferramenta poderosa que permite transmitir facilmente vários conteúdos de mídia, incluindo música, entre dispositivos compatíveis com DLNA na sua rede. A boa notícia é que o Windows 10, e versões anteriores, vêm com um recurso DLNA integrado, eliminando a necessidade de servidores de mídia de terceiros. Veja como ativar o servidor de mídia DLNA no Windows 10 e aproveitar o streaming de música no seu iPhone.

## Como ativar o servidor de mídia DLNA no Windows 10

1. Clique no botão 'Iniciar'.  
2. Selecione o ícone 'Configurações'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Configuração do servidor" caption="Abra as Configurações do Windows" width="500" >}}

3. Na tela 'Configurações do Windows', escolha 'Rede e Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Configurações do Windows" caption="Selecione Rede e Internet" width="500" >}}

4. Em 'Rede', selecione 'Central de Rede e Compartilhamento'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Central de Compartilhamento" caption="Abra a Central de Rede e Compartilhamento" width="500" >}}

5. Na tela 'Central de Rede e Compartilhamento', clique em 'Alterar as configurações de compartilhamento avançadas' no menu esquerdo.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Configurações de compartilhamento avançadas" caption="Alterar configurações de compartilhamento avançadas" width="500" >}}

6. Na tela 'Configurações de compartilhamento avançadas', role para baixo até a seção 'Todas as Redes' e expanda-a clicando na seta.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Ativar descoberta" caption="Expanda as configurações de todas as redes" width="500" >}}

7. Clique em 'Ativar streaming de mídia' para ativar o servidor DLNA.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Ativar servidor" caption="Ativar servidor de streaming de mídia" width="500" >}}

8. Dê um nome à sua biblioteca de mídia e selecione os dispositivos autorizados a acessá-la.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Nome da biblioteca de mídia" caption="Nomeie sua biblioteca de mídia DLNA" width="500" >}}

9. Clique em 'OK' para confirmar. Agora, suas pastas pessoais como Música, Imagens e Vídeos ficarão visíveis para qualquer dispositivo de streaming com suporte UPnP.

## Como desativar o servidor de mídia DLNA no Windows 10

1. Clique em 'Iniciar' e digite 'services' no campo de pesquisa.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Serviços do Windows" caption="Abra os Serviços do Windows" width="500" >}}

2. Na tela 'Serviços', role para encontrar 'Windows Media Player Network Sharing Service'.  
3. Clique duas vezes e defina o 'Tipo de inicialização' como 'Manual'.  
4. Pare o serviço clicando no botão 'Parar'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Parar serviço DLNA" caption="Desativar serviço de compartilhamento de rede DLNA" width="500" >}}

## Como reproduzir música do servidor DLNA no iPhone

1. Instale o aplicativo gratuito **Evermusic** na App Store:  
   [Aplicativo Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Abra a aba 'Conexões' e toque em 'Dispositivos disponíveis' na seção 'Rede Local'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Conexões Evermusic" caption="Evermusic: tela de Conexões" width="500" >}}

3. Aguarde alguns segundos enquanto a lista de dispositivos carrega e toque no servidor Windows Media Player DLNA (ex.: 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Dispositivos disponíveis" caption="Servidores DLNA disponíveis no Evermusic" width="500" >}}

4. Você verá uma lista de pastas disponíveis no servidor de mídia.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Pastas Evermusic" caption="Navegue pelas pastas compartilhadas do servidor DLNA" width="500" >}}

5. Abra qualquer pasta contendo arquivos de áudio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Conteúdo da pasta" caption="Veja o conteúdo das pastas DLNA compartilhadas" width="500" >}}

6. Toque em qualquer arquivo para iniciar o reprodutor de áudio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Reprodutor de áudio" caption="Reproduza arquivo de áudio do DLNA no Evermusic" width="500" >}}

7. Para melhorar sua experiência de áudio, toque no ícone 'Equalizador' perto do indicador de volume na parte inferior da tela para ativar o equalizador estilo iPod com pré-amplificador.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Equalizador" caption="Use o equalizador integrado para reprodução aprimorada" width="500" >}}

## Conclusão

Com o servidor de mídia DLNA no Windows 10 e o Evermusic no seu iPhone, você pode aproveitar streaming de música sem interrupções do computador para o dispositivo móvel. Diga adeus às limitações de armazenamento e olá à música sob demanda!

## Perguntas frequentes

{{% details title="Preciso instalar software de servidor no Windows 10?" closed="true" %}}
Não. O Windows 10 inclui um servidor de mídia DLNA integrado. Você só precisa ativar o streaming de mídia nas configurações da Central de Rede e Compartilhamento. Nenhum software de terceiros é necessário.
{{% /details %}}

{{% details title="Meu iPhone precisa estar na mesma rede Wi-Fi?" closed="true" %}}
Sim. O streaming DLNA funciona pela sua rede local. Tanto o PC com Windows 10 quanto o iPhone devem estar conectados à mesma rede Wi-Fi para que o Evermusic descubra o servidor DLNA.
{{% /details %}}

{{% details title="Quais formatos de áudio posso transmitir via DLNA?" closed="true" %}}
O servidor Windows DLNA compartilha arquivos da pasta Música independentemente do formato. O Evermusic suporta MP3, FLAC, AAC, WAV, OGG, AIFF e muitos outros formatos, então você pode reproduzir praticamente qualquer arquivo de áudio do servidor.
{{% /details %}}

{{% details title="Posso usar o Flacbox em vez do Evermusic?" closed="true" %}}
Sim. O Flacbox também suporta navegação e reprodução DLNA/UPnP. Você pode usar qualquer um dos aplicativos para descobrir e reproduzir música do seu servidor Windows DLNA.
{{% /details %}}

{{% details title="O streaming DLNA usa dados móveis?" closed="true" %}}
Não. O DLNA opera inteiramente na sua rede Wi-Fi local. Não usa nenhum dado móvel. No entanto, ambos os dispositivos devem permanecer conectados à mesma rede durante a reprodução.
{{% /details %}}
