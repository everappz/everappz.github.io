---
title: "Como configurar um servidor multimédia DLNA/UPnP no iPhone e iPad para streaming"
description: "Transforme o seu iPhone ou iPad num servidor multimédia DLNA/UPnP com o Everdisk e faça streaming de fotografias, vídeos e música para uma smart TV, consola de jogos, VLC ou Kodi por Wi-Fi. Configuração completa e como ligar a partir de TVs Samsung, LG e Sony, Windows, Mac, Linux, Android e outro iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "servidor multimedia", "streaming", "smart tv", "iphone", "ipad", "wifi"]
keywords: ["servidor DLNA iPhone", "servidor UPnP iPad", "como configurar DLNA no iPhone", "streaming para smart TV a partir do iPhone", "servidor multimedia DLNA iOS", "fazer streaming de videos para a TV sem cabo", "ver fotografias do iPhone na TV", "DLNA Samsung TV iPhone", "DLNA LG TV iPhone", "DLNA Sony Bravia iPhone", "VLC DLNA iPhone", "servidor multimedia Kodi DLNA", "servidor multimedia UPnP AV iOS", "streaming de musica para a TV a partir do iPhone", "aplicacao de servidor multimedia iPhone"]
readingTime: 9
---

{{< author-byline >}}

O DLNA (também chamado UPnP AV) é o motor discreto por trás da maioria das smart TVs. É uma linguagem comum que permite a uma TV ou a um leitor multimédia encontrar uma biblioteca de conteúdos na mesma rede Wi-Fi e reproduzir a partir dela, sem nada para instalar na TV. Se o seu iPhone ou iPad puder funcionar como essa biblioteca, as suas fotografias, vídeos e música aparecem sozinhos no ecrã grande.

Este guia mostra como transformar o seu iPhone ou iPad num servidor multimédia DLNA/UPnP com o [Everdisk](/products/everdisk) e como abrir essa biblioteca a partir de uma smart TV, uma consola de jogos, o VLC, o Kodi, um computador, um telemóvel Android e até um segundo iPhone. Tudo funciona pela sua rede Wi-Fi local, por isso nada é enviado para lado nenhum.

## O que precisa

- Um iPhone ou iPad com o [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Uma TV, leitor ou computador na **mesma rede Wi-Fi** que o seu dispositivo.
- As fotografias, vídeos ou música que quer reproduzir, já no seu iPhone (na app Fotos, na app Música ou na pasta Documentos do Everdisk).

## Configurar o servidor DLNA no Everdisk

### Passo 1: escolher o que partilhar

Abra o Everdisk e vá ao separador **Partilha**. Toque em **O que partilhar** e escolha o seu conteúdo:

- Ative **Permitir acesso a toda a biblioteca de fotografias** para partilhar todos os álbuns, ou toque em **Adicionar fotografias** para escolher alguns.
- Ative **Permitir acesso a toda a biblioteca de músicas** para partilhar as suas canções, ou toque em **Adicionar faixas** para uma seleção.
- Adicione pastas ou ficheiros com **Adicionar pasta** e **Adicionar ficheiro**. A pasta Documentos da própria app é partilhada por predefinição.

Precisa de ter pelo menos um item selecionado antes de a partilha poder começar.

### Passo 2: ativar TV e central de multimédia (DLNA)

Vá a **Definições**, depois **Partilha**, depois **Ligações**. Certifique-se de que **TV e central de multimédia** está ativado. Está ativado por predefinição e tem a etiqueta DLNA. É este o servidor que as TVs e os leitores procuram.

### Passo 3: iniciar a partilha

De volta ao separador **Partilha**, toque no grande botão **Iniciar**. O seu dispositivo é agora um servidor multimédia na sua rede Wi-Fi. Aparece aos outros dispositivos com o seu nome amigável, o mesmo que é mostrado como nome do dispositivo na app (algo como "Speedy-Hare" até o alterar).

O streaming DLNA está sempre aberto, por isso não há palavra-passe para introduzir na TV. Mantenha o Everdisk aberto no ecrã enquanto vê, porque o iOS suspende as apps que são enviadas totalmente para segundo plano.

## Reproduzir numa smart TV

Este é o caso mais comum e normalmente demora cerca de trinta segundos.

1. Coloque a TV na **mesma rede Wi-Fi** que o seu iPhone.
2. Abra o leitor multimédia integrado da TV. O nome depende da marca: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** ou **SmartThings** (Samsung), **Content Share** ou **SimplyShare**.
3. Procure a lista de servidores multimédia ou fontes. O seu dispositivo aparece aí pelo seu nome.
4. Selecione-o, navegue até às suas fotografias, vídeos ou música e carregue em reproduzir.

As miniaturas de pré-visualização aparecem automaticamente, para que possa encontrar o álbum de férias ou o filme certo sem adivinhar.

### Que TVs funcionam

A maioria das TVs **Samsung, LG, Sony BRAVIA, Panasonic (firmware VIERA), Philips e Hisense** tem DLNA integrado e funciona logo. **As consolas PlayStation e Xbox e a maioria dos recetores AV** também.

Algumas plataformas deixam-no de fora: **TVs Roku, Amazon Fire TV, Vizio SmartCast e o Google TV simples** sem uma app multimédia do fabricante. Se a sua TV for uma destas e não conseguir encontrar o seu dispositivo, é normalmente essa a razão. Nessas TVs, instale uma app de leitor DLNA como o VLC ou o Kodi, ou aceda aos seus ficheiros através de um navegador, usando o [guia de configuração de WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Algumas marcas mantiveram o DLNA a funcionar mesmo depois de removerem o logótipo oficial de DLNA, por isso, se parecer que não existe, procure um dos nomes de leitor multimédia acima.

## Reproduzir no VLC ou Kodi no Windows, Mac e Linux

O VLC e o Kodi são gratuitos, funcionam em todos os sistemas de secretária e comunicam bem por DLNA. São a forma fiável de abrir a sua biblioteca do Everdisk num computador.

**VLC (Windows, Mac, Linux):**

1. Abra o VLC.
2. Mostre a lista de reprodução (no Windows e no Linux prima **Ctrl+L**, no Mac abra a **Playlist** a partir do menu Ver).
3. Na barra lateral, abra **Universal Plug'n'Play** em Rede local.
4. O seu dispositivo aparece na lista. Clique nele e escolha um ficheiro.

**Kodi (Windows, Mac, Linux):**

1. Vá a **Vídeos**, **Música** ou **Imagens**, depois **Ficheiros**, depois **Adicionar fonte** (ou **Procurar**).
2. Escolha **Dispositivos UPnP**.
3. Selecione o seu dispositivo e navegue pela sua biblioteca.

No Windows também pode abrir o **Windows Media Player**, expandir **Outras Bibliotecas** na barra lateral, e o seu dispositivo aparece aí.

## Reproduzir no Android

Os telemóveis e tablets Android não têm um navegador DLNA de sistema, por isso use uma app:

- **VLC para Android**: abra o menu lateral, toque em **Rede local**, e o seu dispositivo aparece nos servidores UPnP.
- **BubbleUPnP** ou uma app UPnP semelhante: o seu dispositivo aparece na lista de servidores, e estas apps também podem enviar a reprodução para uma TV.

## Reproduzir noutro iPhone ou iPad

Dois dispositivos, uma biblioteca. Digamos que as fotografias estão no seu iPhone e quer vê-las no seu iPad.

- O caminho mais simples é o próprio separador **Dispositivos** do Everdisk no segundo dispositivo. Funciona como cliente DLNA e também como servidor. Abra o Everdisk no iPad, vá a **Dispositivos**, e o seu iPhone aparece em **Dispositivos disponíveis**. Toque nele para navegar e reproduzir.
- Qualquer app de leitor DLNA para iOS também funciona, como o VLC ou um navegador UPnP. Abra a sua vista de rede local e escolha o seu iPhone.

## Reproduzir numa consola de jogos

- **PlayStation 5 e 4**: abra a app **Media** (Galeria de Multimédia), e o seu dispositivo aparece como um servidor multimédia que pode navegar.
- **Xbox**: use uma app de leitor multimédia que suporte DLNA, depois escolha o seu dispositivo na lista de servidores.

## Se o seu dispositivo não aparecer na lista

Alguns leitores permitem adicionar um servidor multimédia por endereço em vez de esperar que seja descoberto. No ecrã de **Partilha** do Everdisk, o cartão DLNA mostra um endereço de descrição do dispositivo que termina em `/device-desc.xml`. Introduza esse endereço no campo de adicionar servidor do leitor.

Se mesmo assim não aparecer, verifique três coisas: ambos os dispositivos estão na mesma rede Wi-Fi (não numa rede de convidados que bloqueie o tráfego entre dispositivos), o Everdisk está aberto e a partilha está iniciada, e **TV e central de multimédia** está ativado nas Definições.

## Se um vídeo não reproduzir

O DLNA entrega o ficheiro à TV tal como está, e a TV tem de conseguir descodificá-lo. Se um clipe se recusar a reproduzir, o seu formato provavelmente não é suportado por essa TV. Duas soluções:

- Abra **Definições**, depois **Partilha**, depois **Vídeos**, e reduza a **Qualidade**. O Everdisk converte então o vídeo para um formato mais compatível à medida que faz o streaming. (A conversão é uma funcionalidade Premium.)
- Ou abra o mesmo ficheiro num navegador usando a ligação de navegador do Everdisk, que é mais tolerante quanto a formatos.

## Formas reais de as pessoas usarem isto

- **Noite de cinema em família.** Os vídeos gravados no seu telemóvel reproduzem na TV da sala sem cabo nem Apple TV.
- **Fotografias de férias no ecrã grande.** Abra a sua biblioteca de Fotos na TV e passe pela viagem com toda a gente na sala.
- **Música de fundo numa festa.** Aponte uma coluna DLNA ou um recetor AV para a sua biblioteca de Música e deixe-a a tocar.
- **Ver numa TV de hotel** que tenha um leitor multimédia, assim que ambos os dispositivos estiverem na rede Wi-Fi do quarto.

## Algumas dicas

- Mantenha o Everdisk aberto enquanto faz streaming. Se bloquear o telemóvel durante muito tempo, o iOS pode suspender a app e a reprodução para.
- Ligue o telemóvel à corrente para sessões de filmes longas.
- Para o streaming mais rápido, mantenha o **Formato** e a **Qualidade** em **Original** nas Definições, e só os reduza se uma TV específica tiver dificuldades com um ficheiro.
- O DLNA é apenas streaming. Ninguém do lado da TV pode alterar ou eliminar os seus ficheiros. Para transferência de ficheiros nos dois sentidos, use antes o servidor [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) ou [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/).

## Perguntas frequentes

{{% details title="Qual é a diferença entre DLNA e UPnP?" closed="true" %}}
Estão intimamente relacionados. O UPnP é a norma de rede subjacente, e o DLNA é o perfil multimédia construído sobre ela que as TVs e os leitores usam para partilhar e reproduzir fotografias, vídeos e música. No uso do dia a dia, as palavras são intermutáveis. Quando ativa TV e central de multimédia no Everdisk, o seu dispositivo torna-se um servidor multimédia DLNA/UPnP que qualquer cliente DLNA pode navegar.
{{% /details %}}

{{% details title="Preciso de instalar alguma coisa na minha TV?" closed="true" %}}
Não. Se a sua TV suportar DLNA, já tem um leitor multimédia que consegue encontrar o seu dispositivo na rede Wi-Fi. Só instala o Everdisk no iPhone ou iPad que tem o conteúdo. Se a sua TV não suportar DLNA, instale um leitor como o VLC ou o Kodi num dispositivo ligado a ela.
{{% /details %}}

{{% details title="Porque é que o meu iPhone não aparece na TV?" closed="true" %}}
Verifique se ambos os dispositivos estão na mesma rede Wi-Fi. As redes de convidados e algumas redes de escritório ou de hotel bloqueiam os dispositivos de se verem uns aos outros, o que impede o DLNA. Depois confirme que o Everdisk está aberto com a partilha iniciada, e que TV e central de multimédia está ativado em Definições, Partilha, Ligações. Se a TV mesmo assim não o encontrar, adicione o servidor manualmente usando o endereço de descrição do dispositivo que termina em /device-desc.xml.
{{% /details %}}

{{% details title="O streaming DLNA precisa de palavra-passe?" closed="true" %}}
Não. O DLNA está sempre aberto a qualquer pessoa na mesma rede Wi-Fi enquanto estiver ativado, e é por isso que não há início de sessão do lado da TV. Isso não faz mal numa rede doméstica em que confia. Numa rede em que não confia, desative TV e central de multimédia quando terminar, ou use antes o servidor SMB com encriptação.
{{% /details %}}

{{% details title="Posso fazer streaming para um Chromecast ou Roku?" closed="true" %}}
O Chromecast e o Roku não funcionam como leitores DLNA de origem, por isso não encontram o seu dispositivo diretamente. A solução é instalar uma app DLNA que consiga fazer cast, como o VLC ou o BubbleUPnP num telemóvel, e enviar a reprodução para o Chromecast ou o Roku a partir daí. Na maioria das outras smart TVs, o DLNA funciona sem nada disto.
{{% /details %}}

{{% details title="Um vídeo reproduz sem som ou não abre. O que posso fazer?" closed="true" %}}
É um formato que a TV não consegue descodificar. Abra Definições, Partilha, Vídeos no Everdisk e reduza a Qualidade para que a app converta o vídeo para um formato mais compatível à medida que faz o streaming. Também pode abrir o mesmo ficheiro através da ligação de navegador, que lida com mais formatos.
{{% /details %}}

{{% details title="Posso fazer streaming de música, não só de vídeo?" closed="true" %}}
Sim. Ative Permitir acesso a toda a biblioteca de músicas, ou adicione faixas específicas, e depois inicie a partilha. As suas canções aparecem em qualquer coluna DLNA, recetor AV ou TV, com capa e detalhes da faixa. A música é sempre partilhada na sua qualidade original.
{{% /details %}}

{{% details title="A app tem de ficar aberta enquanto vejo?" closed="true" %}}
Sim. O seu iPhone está a funcionar como servidor, e o iOS suspende as apps que são enviadas totalmente para segundo plano durante muito tempo. Mantenha o Everdisk no ecrã enquanto faz streaming, e ligue à corrente para sessões longas.
{{% /details %}}

{{% details title="Como faço streaming de um iPhone para outro iPad?" closed="true" %}}
Inicie a partilha no iPhone, depois abra o Everdisk no iPad e vá ao separador Dispositivos. O iPhone aparece em Dispositivos disponíveis como servidor multimédia. Toque nele para navegar e reproduzir. O Everdisk funciona como cliente DLNA e como servidor, por isso não precisa de outra app.
{{% /details %}}

{{% details title="O Everdisk é gratuito?" closed="true" %}}
Sim, o Everdisk é gratuito para transferir e o servidor multimédia DLNA está incluído. Uma compra opcional Premium Vitalícia, feita uma única vez, adiciona extras como a conversão de fotos e vídeos para TVs mais antigas, portas personalizadas e mais. Pode configurar e usar o streaming DLNA sem pagar.
{{% /details %}}

Pronto para experimentar? [Transfira o Everdisk da App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e faça streaming do seu primeiro álbum para a TV em poucos minutos. Perguntas ou comentários? Envie-nos um email para **support@everappz.com**.
