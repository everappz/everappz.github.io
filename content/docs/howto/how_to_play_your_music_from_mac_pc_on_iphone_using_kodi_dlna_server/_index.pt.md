---
title: "Como reproduzir músicas do Mac / PC / Linux / NAS no iPhone usando o servidor Kodi DLNA"
date: 2025-07-25
description: "Transmita músicas do seu computador ou NAS para o iPhone via Wi-Fi usando Kodi DLNA e o aplicativo Evermusic."
keywords: ["servidor kodi dlna", "transmitir música para iphone", "reproduzir música do nas", "evermusic dlna", "música do mac para iphone", "música do windows para iphone", "kodi dlna iphone", "streaming de áudio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "streaming de música", "mac", "nas", "linux", "rede local"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Instale o Kodi no seu Mac, PC, Linux ou NAS, ative o servidor DLNA/UPnP e transmita toda a sua biblioteca musical para iPhone ou iPad usando o aplicativo gratuito Evermusic ou Flacbox via Wi-Fi. Sem assinaturas.

## Introdução

Se você tem um **Mac, PC com Windows, máquina Linux ou dispositivo NAS**, pode facilmente transformá-lo em um **servidor de música pessoal** em casa usando o [Kodi](https://kodi.tv/), uma plataforma de mídia gratuita e de código aberto. Com o servidor **DLNA/UPnP** integrado do Kodi, você pode transmitir toda a sua biblioteca musical para qualquer cliente compatível com DLNA — incluindo seu iPhone ou iPad.

Neste guia, mostraremos passo a passo como:

- Instalar o Kodi no Mac ou PC
- Configurar pastas de música para compartilhamento
- Ativar o servidor de música DLNA
- Acessar essa música usando o aplicativo **Evermusic** ou **Flacbox** para iOS

Esta configuração é 100% gratuita — sem assinaturas, apenas sua própria música transmitida pela sua rede Wi-Fi. Seja para organizar sua grande coleção de MP3, ouvir FLAC via Wi-Fi, ou simplesmente curtir sua música local sem sincronizar via iTunes, esta configuração é perfeita para você.

## Baixe e instale o Kodi no seu Mac / PC / Linux / NAS

Primeiro, visite o site oficial do Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Página principal do Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Clique em **Downloads** e role para encontrar a versão para o seu computador.
Escolha seu sistema operacional. Neste exemplo, usaremos **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Página de downloads do Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Clique em **Intel (x86/64)** se você tem um Mac Intel ou **Apple Silicon** para M1, M2, M3 Mac para iniciar o download.

{{< cards cols="1">}}
{{< card subtitle="Escolha o instalador do macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Aguarde um momento enquanto o instalador é baixado.

{{< cards cols="1">}}
{{< card subtitle="Kodi baixado" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Após o download, localize o arquivo `.dmg` na pasta **Downloads**.

{{< cards cols="1">}}
{{< card subtitle="Instalar o Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Clique duas vezes no arquivo baixado para iniciar o instalador.
Arraste o Kodi para a pasta **Aplicativos** para instalar.

{{< cards cols="1">}}
{{< card title="" subtitle="Instale o Kodi arrastando para Aplicativos" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Abra o Kodi. Pode ser necessário permitir em **Preferências do Sistema → Segurança e Privacidade → Abrir mesmo assim**.

{{< cards cols="1">}}
{{< card subtitle="Tela principal do Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Adicione música à biblioteca do Kodi

Clique no **ícone de engrenagem** (Configurações) na tela inicial.

{{< cards cols="1">}}
{{< card subtitle="Configurações do Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navegue até **Configurações de Mídia → Biblioteca**. Ative **Atualizar biblioteca na inicialização** para a biblioteca de vídeo e música para indexação automática.

{{< cards cols="1">}}
{{< card subtitle="Configurações da biblioteca" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Depois vá para a seção **Música** e clique em **Adicionar música**.

{{< cards cols="1">}}
{{< card subtitle="Adicionar pasta de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Navegue e selecione a pasta onde sua música está armazenada.

{{< cards cols="1">}}
{{< card subtitle="Escolher fonte de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Adicione a fonte de música ao Kodi.

{{< cards cols="1">}}
{{< card subtitle="Adicionar fonte de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Confirme e deixe o Kodi escanear sua biblioteca musical.

{{< cards cols="1">}}
{{< card subtitle="Confirmar fontes de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Aguarde um momento enquanto sua biblioteca é escaneada e totalmente construída.

{{< cards cols="1">}}
{{< card subtitle="Escaneando biblioteca musical" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Ative o servidor DLNA do Kodi

Vá para **Configurações → Serviços → UPnP/DLNA**.

Ative a opção: **Compartilhar minhas bibliotecas**.

O Kodi agora funciona como um servidor DLNA na sua rede Wi-Fi local.

{{< cards cols="1">}}
{{< card subtitle="Ativar DLNA no Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Abrir biblioteca do Kodi

Clique com o botão direito para fechar a janela de configurações e abrir a biblioteca principal do Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Clique com o botão direito para acessar a biblioteca do Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Baixe o aplicativo de streaming de música para iOS

Obtenha um aplicativo cliente DLNA gratuito para iOS que permite transmitir música de diversos serviços de armazenamento em nuvem e servidores DLNA.

- Use o **Evermusic** se sua coleção é principalmente MP3 e outros formatos de áudio padrão.
- Escolha o **Flacbox** se você tem uma biblioteca de música hi-res em formatos como FLAC, ALAC ou DSD.

Ambos os aplicativos estão disponíveis para **iOS** e **macOS**, e são gratuitos.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Baixar Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Baixar Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Adicionar fonte DLNA

Após baixar o aplicativo iOS, abra a seção **Todas as Conexões**.

{{< cards cols="1">}}
{{< card title="" subtitle="Barra lateral principal do aplicativo Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Role para baixo e toque em **Rede local - Dispositivos disponíveis** para descobrir servidores DLNA.
Nesta seção, você verá todos os dispositivos disponíveis na sua rede local. Seu **servidor Kodi DLNA** deve aparecer aqui. Toque no servidor Kodi para conectar.

{{< cards cols="1">}}
{{< card title="" subtitle="Dispositivos DLNA disponíveis no Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

O Evermusic exibirá as pastas da biblioteca compartilhadas pelo Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical do Kodi no Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navegue até a pasta **Músicas** para ver todos os arquivos de áudio disponíveis no seu servidor DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Músicas listadas da pasta remota" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Toque em qualquer arquivo de áudio para começar a transmitir instantaneamente.

{{< cards cols="1">}}
{{< card title="" subtitle="Arquivo MP3 reproduzindo no Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Volte para a seção **Conexões**. O servidor DLNA adicionado aparecerá aqui agora. Toque em seu ícone para reconectar a qualquer momento. Você também pode conectar outros serviços de nuvem desta tela usando os mesmos passos.

Você também pode ativar o **scrobbling do Last.fm** aqui. As estatísticas de reprodução serão salvas na sua conta Last.fm, fornecendo recomendações musicais personalizadas posteriormente.

{{< cards cols="1">}}
{{< card title="" subtitle="Conexões no Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Construir biblioteca musical

Tanto o **Evermusic** quanto o **Flacbox** permitem adicionar música à sua biblioteca e organizá-la por **tags de metadados** como artistas, álbuns, gêneros e compositores.

Para começar, abra a seção **Biblioteca Musical**. Role até **Ferramentas e preferências** e toque em **Adicionar música**.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical do Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Selecione a fonte de música — neste caso, escolha **Conexões**.

{{< cards cols="1">}}
{{< card title="" subtitle="Adicionar nova música no Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Encontre o **servidor Kodi DLNA** nas Conexões e toque para ver pastas e arquivos.

{{< cards cols="1">}}
{{< card title="" subtitle="Escolher servidor DLNA para importar música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Escolha as pastas ou arquivos que deseja adicionar e toque em **Concluído**.

{{< cards cols="1">}}
{{< card title="" subtitle="Selecionar pasta de música para adicionar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

O aplicativo escaneará seus arquivos selecionados e os organizará usando metadados em seções como Artistas, Álbuns, Gêneros e Compositores.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical com categorias" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Criar listas de reprodução

Você também pode criar suas próprias listas de reprodução.

Primeiro, abra a aba **Listas de reprodução**.

{{< cards cols="1">}}
{{< card title="" subtitle="Aba Listas de reprodução no Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Toque no botão **mais (+)** e escolha **Nova lista de reprodução**.

{{< cards cols="1">}}
{{< card title="" subtitle="Criar uma nova lista de reprodução" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Digite um nome para sua lista de reprodução e toque em **Salvar**.

{{< cards cols="1">}}
{{< card title="" subtitle="Digite o nome da lista de reprodução" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Em seguida, escolha uma fonte para adicionar músicas — aqui, selecionamos a **Biblioteca**.

{{< cards cols="1">}}
{{< card title="" subtitle="Adicionar músicas à nova lista de reprodução" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Selecione as músicas desejadas e toque em **Concluído** para adicioná-las.

{{< cards cols="1">}}
{{< card title="" subtitle="Adicionar música da biblioteca à lista de reprodução" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

As faixas selecionadas aparecerão agora na lista de reprodução criada.

{{< cards cols="1">}}
{{< card title="" subtitle="Lista de reprodução criada exibida na lista" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Por padrão, as músicas estão disponíveis para streaming. Para ouvir offline, ative o **Modo offline** — o aplicativo baixará todas as faixas da lista.

{{< cards cols="1">}}
{{< card title="" subtitle="Modo offline ativado para a lista de reprodução" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Toque no botão **Mais ações** para explorar opções adicionais. Você pode:

- Arquivar a lista de reprodução
- Alterar a capa do álbum
- Reordenar faixas
- E mais recursos úteis

{{< cards cols="1">}}
{{< card title="" subtitle="Mais ações de lista de reprodução disponíveis" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Conclusão

Com **Evermusic** e **Flacbox**, transformar seu iPhone, iPad ou Mac em um poderoso reprodutor de música DLNA é fácil. Seja armazenando música na nuvem, em um NAS ou em um servidor de mídia doméstico como o **Kodi**, esses aplicativos permitem transmitir, organizar e curtir sua coleção sem limites.

- Transmita MP3 ou FLAC hi-res diretamente do seu **servidor Kodi DLNA**
- Construa uma biblioteca musical pessoal agrupada por metadados (álbuns, gêneros, compositores)
- Crie e gerencie **listas de reprodução personalizadas**
- Ative o **modo offline** para ouvir em movimento
- Conecte-se a **vários serviços de nuvem** e **dispositivos de rede local**
- Acompanhe seus hábitos de audição com a **integração do Last.fm**

Seja você um audiófilo ou um ouvinte casual, Evermusic e Flacbox oferecem tudo o que você precisa para streaming e organização musical sem interrupções.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Baixar Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Baixar Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Comece a construir sua experiência musical pessoal hoje.

## Perguntas frequentes

{{% details title="O Kodi é gratuito como servidor DLNA?" closed="true" %}}
Sim. O Kodi é completamente gratuito e de código aberto. Funciona em macOS, Windows, Linux e muitos dispositivos NAS.
{{% /details %}}

{{% details title="O Evermusic e o Flacbox suportam streaming de FLAC via DLNA?" closed="true" %}}
Sim. O Flacbox é otimizado para formatos hi-res como FLAC, ALAC e DSD. O Evermusic também suporta reprodução de FLAC junto com MP3 e outros formatos padrão.
{{% /details %}}

{{% details title="Posso ouvir offline após streaming do Kodi?" closed="true" %}}
Sim. Ative o Modo offline em qualquer lista de reprodução e o aplicativo baixará todas as faixas para o seu dispositivo para ouvir sem conexão de rede.
{{% /details %}}

{{% details title="Preciso de uma assinatura premium para usar DLNA?" closed="true" %}}
A versão gratuita suporta até 3 conexões de nuvem ou rede. Premium remove esse limite e permite conectar serviços e servidores DLNA ilimitados.
{{% /details %}}

{{% details title="Meu iPhone precisa estar na mesma rede Wi-Fi que o Kodi?" closed="true" %}}
Sim. O streaming DLNA funciona pela sua rede local. Tanto o servidor Kodi quanto o seu dispositivo iOS devem estar conectados à mesma rede Wi-Fi.
{{% /details %}}

{{% details title="Posso usar esta configuração com um NAS em vez de um Mac ou PC?" closed="true" %}}
Sim. Muitos dispositivos NAS (Synology, QNAP etc.) suportam Kodi ou têm seu próprio servidor DLNA integrado. Evermusic e Flacbox podem conectar a qualquer servidor DLNA/UPnP padrão.
{{% /details %}}
