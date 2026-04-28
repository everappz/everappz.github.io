---
title: "Como conectar o Synology NAS e ouvir música no seu iPhone ou Mac"
date: 2024-09-19
description: "Aprenda como conectar seu Synology NAS usando a API nativa ou QuickConnect e transmitir música de alta qualidade para seu iPhone ou Mac com Evermusic e Flacbox."
keywords: ["synology nas", "transmitir música", "quickconnect", "evermusic synology", "flacbox synology", "reprodutor de música nas", "música nas iphone"]
tags: ["música", "transmissão", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Resumo:** Conecte seu Synology NAS ao Evermusic ou Flacbox usando a API nativa do Synology -- manualmente via endereço IP ou automaticamente via QuickConnect ID. O QuickConnect permite transmitir música remotamente sem encaminhamento de portas. Ambos os aplicativos suportam FLAC, MP3, WAV e outros formatos de alta resolução.

Se você está procurando uma maneira integrada de conectar seu Synology NAS e aproveitar sua biblioteca de música no iPhone ou Mac, os aplicativos Evermusic e Flacbox são as soluções perfeitas. Esses aplicativos suportam uma ampla gama de formatos de áudio, incluindo FLAC, MP3 e WAV, facilitando a transmissão e audição de música de alta qualidade diretamente do seu Synology NAS.

Neste guia, mostraremos como conectar seu Synology NAS ao aplicativo Evermusic ou Flacbox usando a API nativa do Synology e o recurso QuickConnect. Ao aproveitar a API direta do Synology, você pode acessar com segurança sua biblioteca de música fora da rede doméstica sem precisar de configurações complicadas como WebDAV, SMB, DLNA. Com o QuickConnect, você poderá transmitir e gerenciar sua música de qualquer lugar, usando seu iPhone ou Mac.

## Passo 1: Configurar permissões de pasta compartilhada (opcional)

1. Abra o **Painel de Controle** e vá para a seção **Pasta Compartilhada**.

![Pasta Compartilhada](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Selecione a pasta **Music** e clique em **Editar**.

3. Na aba **Permissões**, configure as permissões. Ative o acesso de convidado com Somente leitura se você só precisa ouvir música, ou Leitura/Escrita se precisa modificar arquivos. Salve as alterações.

![Permissões](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Passo 2: Encontrar o endereço IP do Synology NAS

1. Abra o **Painel de Controle** e vá para a aba **Interface de Rede**.

![Interface de Rede](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Ou use seu navegador web para visitar [find.synology.com](http://find.synology.com).

![Encontrar Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Anote o endereço IP do seu Synology NAS (ex.: 192.168.18.137).

## Passo 3: Encontrar as portas de rede do Synology NAS

Você pode encontrar a documentação oficial do Synology para as portas de rede padrão do DSM neste [artigo do Centro de Conhecimento Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

O Synology DSM usa as seguintes portas padrão:
- **HTTP (Acesso Web):** Porta **5000**
- **HTTPS (Acesso Web Seguro):** Porta **5001**

Estas são as portas padrão para acessar a interface DSM.

![Portas de Rede](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Passo 4: Ativar o recurso QuickConnect ID

Um Synology QuickConnect ID é um identificador único que permite acessar seu Synology NAS remotamente pela internet sem precisar configurar configurações de rede complicadas como encaminhamento de portas. O QuickConnect simplifica o acesso remoto usando os servidores do Synology para estabelecer uma conexão entre seu NAS e seu dispositivo, como smartphone ou computador, através do QuickConnect ID.

**Como encontrar ou configurar seu QuickConnect ID:**

1. **Faça login no DSM.**
2. Vá para **Painel de Controle > Acesso Externo > QuickConnect**.
3. **Ative o QuickConnect** e crie ou visualize seu QuickConnect ID único.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Passo 5: Conectar ao Synology NAS no seu iPhone/Mac usando Evermusic ou Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) e [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) são aplicativos reprodutores de música projetados para dispositivos iOS e macOS, cada um oferecendo recursos e capacidades únicos para gerenciar e aproveitar sua biblioteca de música.

1. Abra o aplicativo Evermusic ou Flacbox e vá para a aba **Conexões**.

![Conexões](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Escolha **Conectar um serviço de nuvem** e selecione **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Você tem duas opções de conexão: **manual** usando o endereço IP e a porta do servidor, ou **automática** via QuickConnect ID.

### Conexão manual

Para o método manual, você precisará do endereço IP direto e número da porta obtidos nos passos anteriores.

1. Digite a URL do servidor obtida no passo 2, usando o seguinte formato: PROTOCOLO://ENDEREÇO_IP:NÚMERO_DA_PORTA
   - Use a **porta 5000** para HTTP e a **porta 5001** para conexões HTTPS.

   Por exemplo:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. O número real da porta pode ser confirmado no passo 3 da sua configuração.
3. Digite seu **login** e **senha** do Synology NAS.
4. Toque em **Entrar** para estabelecer a conexão.

![Conexão Manual](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Conexão automática

Para a conexão automática, você usará o **QuickConnect ID** do passo 4. Em vez de digitar manualmente o endereço IP e o número da porta do seu Synology NAS, basta inserir o **QuickConnect ID**. O aplicativo recuperará automaticamente as informações de conexão necessárias.

Este método permite acessar seu NAS remotamente, mesmo fora da sua rede doméstica, para que você possa gerenciar seus arquivos pela internet sem precisar configurar encaminhamento de portas ou endereços IP estáticos.

![Conexão Automática](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Autenticação de dois fatores

A partir do DSM 4.2, o Synology introduziu a **verificação em duas etapas** para aumentar a segurança. Este recurso requer um código de **senha de uso único (OTP)**, gerado por um aplicativo autenticador, além das suas credenciais de login regulares. Se você ativou a verificação em duas etapas, após inserir seu nome de usuário e senha, também precisará inserir o OTP para fazer login na sua sessão DSM.

Observe que, assim que sua sessão expirar, o aplicativo precisará ser reautorizado manualmente. Para reautorizar:

1. Vá para a aba **Conexões** no aplicativo.
2. Toque no botão **Mais ações** ao lado do nome do servidor.
3. Selecione **Configurações** no menu para inserir o novo código de autenticação e concluir o processo de reautorização.

Isso garante que, mesmo acessando seu NAS de uma rede não confiável, seus dados permaneçam seguros.

## Passo 6: Navegar e reproduzir música

1. Uma vez conectado, o dispositivo aparecerá na lista **Dispositivos Conectados**.

![Dispositivos Conectados](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navegue até a pasta **Music** e toque em qualquer arquivo de áudio para iniciar a reprodução.

![Reproduzir Música](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Passo 7: Adicionar pasta da nuvem conectada à biblioteca de música

1. Abra a seção **Biblioteca de Música** no aplicativo.
2. Escolha **Adicionar Música** e selecione **Conexões**.
3. Escolha seu servidor NAS conectado e selecione a pasta **Music**. Toque em **Concluído**.
4. O aplicativo escaneará a pasta de música e adicionará os arquivos de áudio suportados à biblioteca de música. Os metadados serão carregados e suas faixas serão agrupadas por álbum, artista e gênero.

## Conclusão

Seguindo estes passos, você pode facilmente configurar uma conexão no seu Synology NAS e transmitir toda a sua biblioteca de música para seu iPhone ou Mac usando Evermusic ou Flacbox. Esteja em casa ou em movimento, aproveite o acesso integrado e de alta qualidade às suas faixas favoritas de qualquer lugar usando o QuickConnect. Aproveite a flexibilidade e conveniência que esses aplicativos oferecem e comece a gerenciar sua coleção de música com facilidade em todos os seus dispositivos.

Com acesso remoto seguro através do QuickConnect e suporte para uma ampla gama de formatos de áudio, você nunca estará longe da sua música. Agora, seus arquivos armazenados no NAS estão a apenas um toque de distância!

## FAQ

{{% details title="Qual é a diferença entre conexão manual e QuickConnect?" closed="true" %}}
A conexão manual usa o endereço IP e a porta do NAS, que funciona na sua rede local. O QuickConnect usa o serviço de retransmissão do Synology para estabelecer uma conexão de qualquer lugar pela internet, sem encaminhamento de portas.
{{% /details %}}

{{% details title="Posso transmitir música do Synology NAS fora da minha rede doméstica?" closed="true" %}}
Sim. Ative o QuickConnect no seu Synology NAS e use o QuickConnect ID no Evermusic ou Flacbox para transmitir música de qualquer lugar com conexão à internet.
{{% /details %}}

{{% details title="Quais formatos de áudio são suportados ao transmitir do Synology NAS?" closed="true" %}}
Evermusic e Flacbox suportam FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD e muitos outros formatos. Todos os formatos suportados funcionam ao transmitir do Synology NAS.
{{% /details %}}

{{% details title="Preciso de autenticação de dois fatores para conectar?" closed="true" %}}
Não, a 2FA é opcional. No entanto, se você ativou a verificação em duas etapas no seu Synology DSM, o aplicativo solicitará uma senha de uso único durante o login. Você precisará reautorizar quando a sessão expirar.
{{% /details %}}

{{% details title="Devo usar a API nativa do Synology, WebDAV ou SMB para conectar?" closed="true" %}}
A API nativa do Synology com QuickConnect é a melhor escolha para acesso remoto. Para uso em rede local, o SMB é geralmente a opção mais rápida. O WebDAV funciona bem tanto para acesso local quanto remoto. Evermusic e Flacbox suportam todos os três protocolos.
{{% /details %}}
