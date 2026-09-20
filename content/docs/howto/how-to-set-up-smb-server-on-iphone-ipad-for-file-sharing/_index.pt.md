---
title: "Como configurar um servidor SMB no iPhone e iPad para partilha de ficheiros"
description: "Transforme o seu iPhone ou iPad num servidor de ficheiros SMB com o Everdisk e abra-o como uma unidade de rede a partir de um Mac, outro iPhone, Linux ou Android por Wi-Fi. Configuração completa, o endereço e a porta smb, encriptação SMB3 opcional e ligação passo a passo para cada dispositivo."
date: 2026-09-19
tags: ["everdisk", "smb", "partilha de ficheiros", "unidade de rede", "iphone", "ipad", "mac", "finder", "encriptacao", "wifi"]
keywords: ["servidor SMB iPhone", "servidor SMB iPad", "como configurar SMB no iPhone", "partilha SMB iPhone", "ligar iPhone SMB Mac Finder", "smb iphone para iphone", "app Ficheiros iOS ligar a servidor SMB", "partilhar ficheiros iPhone SMB", "iphone unidade de rede Finder", "encriptacao SMB3 iOS", "partilha smb iPhone Android", "ligar a SMB a partir do Linux", "iphone como unidade de rede", "partilhar ficheiros entre iphones wifi", "mapear iphone como unidade de rede"]
readingTime: 10
---

{{< author-byline >}}

O SMB é a partilha de ficheiros integrada no macOS, no Windows e no Linux, e em quase todas as unidades de rede (NAS). Quando se liga a uma pasta partilhada noutro computador e ela abre como um disco normal no Finder ou no Explorador de Ficheiros, é o SMB a fazer o trabalho. Com o [Everdisk](/products/everdisk) pode colocar uma partilha SMB no seu iPhone ou iPad, de forma a que o próprio telemóvel apareça como uma unidade de rede que os outros dispositivos navegam, copiam a partir dela e copiam para ela.

Esta é a opção a escolher quando quer que o seu iPhone se comporte como uma verdadeira unidade, e não como uma página web. É rápida, arrasta e larga nos dois sentidos, e é o único tipo de ligação do Everdisk que consegue encriptar cada transferência. Este guia cobre a configuração e como ligar a partir de um Mac, outro iPhone ou iPad, Linux, Android e Windows.

## O que precisa

- Um iPhone ou iPad com o [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Outro dispositivo na **mesma rede Wi-Fi**.
- Os ficheiros que quer partilhar, na pasta Documentos do Everdisk ou em pastas que adicionar.

## Configurar o servidor SMB no Everdisk

### Passo 1: escolher o que partilhar e quem pode escrever

Abra o Everdisk, vá ao separador **Partilha** e toque em **O que partilhar**. A pasta Documentos é partilhada por predefinição. Adicione mais com **Adicionar pasta** e **Adicionar ficheiro**, e ative a sua biblioteca de fotografias ou de música se quiser que fiquem também disponíveis.

Decida se os outros dispositivos podem apenas ler os seus ficheiros, ou também alterá-los. Abra **Definições**, depois **Partilha**, depois **Acesso**, e configure a **Edição de ficheiros**. Com ela ativada, os dispositivos ligados podem copiar ficheiros para o seu telemóvel e mudar-lhes o nome ou eliminá-los. Com ela desativada, a partilha é só de leitura.

Se quiser um início de sessão, defina um **Login** e uma **Palavra-passe** no mesmo ecrã de Acesso. Deixe ambos vazios para permitir acesso de convidado.

### Passo 2: ativar o servidor SMB

Vá a **Definições**, depois **Partilha**, depois **Ligações**, e ative **Computador (avançado)**. Esse é o servidor SMB (tem a etiqueta SMB).

### Passo 3: iniciar a partilha e anotar o endereço

Volte ao separador **Partilha** e toque em **Iniciar**. A secção **Como ligar** mostra agora o endereço SMB. Tem este aspeto:

```
smb://192.168.1.20:4455/Share
```

Três coisas a saber sobre esse endereço:

- O número a seguir aos dois pontos é a **porta**. O Everdisk usa **4455** por predefinição.
- A partilha chama-se **Share**.
- A primeira parte é o endereço do seu iPhone na rede Wi-Fi, por isso será diferente na sua rede.

Mantenha o Everdisk aberto enquanto houver dispositivos ligados, porque o iOS suspende as apps que ficam demasiado tempo em segundo plano.

## Ligar a partir de um Mac

Este é o caso mais fácil, porque o macOS comunica SMB de forma nativa.

A forma mais rápida: abra o **Finder** e procure na barra lateral em **Localizações** ou **Rede**. O Everdisk anuncia-se na rede Wi-Fi, por isso o seu iPhone aparece muitas vezes aí sozinho. Clique nele, depois clique em **Ligar como** e escolha **Convidado**, ou introduza o seu início de sessão.

Para ligar manualmente:

1. No Finder, escolha **Ir**, depois **Ligar ao servidor** (ou prima **Command e K**).
2. Escreva o endereço SMB mostrado no Everdisk, por exemplo `smb://192.168.1.20:4455/Share`.
3. Clique em **Ligar**, depois escolha **Convidado** ou introduza o seu **Login** e **Palavra-passe**.

O seu iPhone abre-se numa janela do Finder. Copie ficheiros para dentro ou para fora arrastando, tal como em qualquer outra unidade (se a Edição de ficheiros estiver ativada).

## Ligar a partir de outro iPhone ou iPad

O iOS e o iPadOS conseguem abrir partilhas SMB na app **Ficheiros** integrada, o que torna as transferências entre telemóveis limpas e rápidas.

No segundo dispositivo:

1. Abra a app **Ficheiros**.
2. Toque no botão **mais** (os três pontos, no canto superior direito no iPhone) e escolha **Ligar ao servidor**.
3. Introduza o endereço SMB do Everdisk, por exemplo `smb://192.168.1.20:4455/Share`.
4. Escolha **Convidado**, ou **Utilizador registado** e introduza o seu início de sessão.
5. A partilha aparece em Localizações na app Ficheiros. Navegue e copie em qualquer direção.

Também pode usar o próprio separador **Dispositivos** do Everdisk no segundo dispositivo, que inclui um cliente SMB. Abra o Everdisk, vá a **Dispositivos**, toque em **Nova ligação**, escolha **SMB** e introduza o endereço.

## Ligar a partir do Linux

1. Abra o seu gestor de ficheiros (Files/Nautilus no GNOME, Dolphin no KDE).
2. Escolha **Outras localizações** ou **Ligar ao servidor**.
3. Introduza o endereço, por exemplo `smb://192.168.1.20:4455/Share`.
4. Ligue-se como convidado, ou introduza o seu início de sessão.

A partir de um terminal também pode executar `smbclient //192.168.1.20/Share -p 4455` e introduzir o seu início de sessão quando for pedido.

## Ligar a partir do Android

O Android não tem um navegador SMB de sistema, por isso use um gestor de ficheiros que suporte SMB:

1. Instale uma app como o **CX File Explorer**, o **Solid Explorer** ou o **X-plore File Manager**.
2. Adicione uma nova ligação **SMB** ou **LAN**.
3. Introduza o anfitrião (o endereço Wi-Fi do seu iPhone), defina a **porta para 4455** e o nome da partilha **Share**.
4. Ligue-se como convidado ou com o seu início de sessão, depois navegue e copie.

## Ligar a partir do Windows

O Windows consegue ler partilhas SMB, com uma ressalva que vale a pena conhecer à partida. O Explorador de Ficheiros integrado só comunica com SMB na porta padrão e não permite escrever uma porta personalizada no caminho, e o Everdisk usa a porta 4455. Por isso, a via simples **Mapear unidade de rede** muitas vezes não a alcança.

Tem duas boas opções no Windows:

- Use um gestor de ficheiros ou cliente SMB que permita definir uma porta personalizada, e aponte-o para o endereço do seu iPhone com a porta **4455** e o nome da partilha **Share**.
- Ou ligue-se a partir do Windows usando antes um dos outros servidores do Everdisk. A [configuração de WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) e a [configuração de FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) funcionam ambas bem a partir do Explorador de Ficheiros do Windows, e a ligação de navegador funciona em qualquer navegador.

Se mesmo assim quiser tentar o Mapear unidade de rede: abra o **Explorador de Ficheiros**, clique com o botão direito em **Este PC**, escolha **Mapear unidade de rede** e introduza o anfitrião e o nome da partilha mostrados no Everdisk. Se não conseguir ligar, é a limitação de porta acima, por isso mude para WebDAV ou FTP.

## Ativar a encriptação para Wi-Fi não fiável

O SMB é a única ligação do Everdisk que consegue encriptar cada transferência, o que importa em redes Wi-Fi que não controla totalmente, como um café ou uma rede de escritório.

1. Em **Definições**, **Partilha**, **Acesso**, defina um **Login** e uma **Palavra-passe**. As ligações encriptadas não podem ser anónimas, por isso este passo é obrigatório.
2. Em **Definições**, **Partilha**, ative **Exigir encriptação SMB**.
3. Pare e volte a iniciar a partilha para que a alteração tenha efeito.

Cada transferência SMB fica então protegida com **encriptação SMB3 (AES)**. O dispositivo que se liga precisa de suportar SMB3, o que o Finder de um Mac moderno e o Windows 10 ou posterior fazem ambos. A Encriptação SMB faz parte da compra Premium feita uma única vez.

## Só de leitura ou de leitura e escrita

O interruptor **Edição de ficheiros** em Definições, Partilha, Acesso controla isto para cada servidor, incluindo o SMB. Ative-o e os dispositivos ligados podem enviar, mudar o nome e eliminar. Desative-o e só podem navegar e copiar ficheiros para fora do seu telemóvel. Escolha só de leitura quando estiver a entregar ficheiros a alguém a quem não quer que altere nada.

## Formas reais de as pessoas usarem isto

- **Mover uma pasta grande para o seu iPhone a partir de um Mac** arrastando-a para a janela do Finder, mais rápido do que um envio pela web.
- **Retirar um dia de fotografias e vídeos do seu telemóvel** para um portátil sem iTunes nem cabo.
- **Enviar ficheiros entre dois iPhones** através da app Ficheiros, sem uma terceira app em nenhum dos lados.
- **Trabalhar num ficheiro no lugar**, abrindo um documento diretamente do telemóvel numa app no seu Mac e voltando a guardá-lo.

## Algumas dicas

- Mantenha o Everdisk aberto enquanto um dispositivo estiver ligado. Bloquear o telemóvel durante muito tempo pode suspender a app e cortar a ligação.
- Se um Mac não conseguir ver o telemóvel na barra lateral do Finder, ligue manualmente com Ligar ao servidor e o endereço smb completo.
- Para a melhor velocidade em transferências grandes, mantenha a qualidade de fotos e vídeos em Original nas Definições.
- Numa rede não fiável, ative Exigir encriptação SMB e desative os outros servidores enquanto trabalha.

## Perguntas frequentes

{{% details title="Qual é o endereço e a porta SMB do meu iPhone?" closed="true" %}}
Depois de iniciar a partilha, o Everdisk mostra o endereço no ecrã de Partilha. Tem o aspeto smb://192.168.1.20:4455/Share. O 4455 é a porta que o Everdisk usa para SMB, e Share é o nome da pasta partilhada. A primeira parte é o endereço do seu iPhone na rede Wi-Fi, por isso o seu será diferente.
{{% /details %}}

{{% details title="Posso ligar-me à partilha SMB do meu iPhone a partir do Windows?" closed="true" %}}
O Explorador de Ficheiros do Windows só se liga a SMB na porta padrão e não aceita uma porta personalizada no caminho, enquanto o Everdisk usa a porta 4455. Por isso, a via simples Mapear unidade de rede muitas vezes não a alcança. Use um gestor de ficheiros que permita definir uma porta personalizada, ou ligue-se a partir do Windows com WebDAV, FTP ou a ligação de navegador. Todos esses funcionam a partir do Windows sem problemas de porta.
{{% /details %}}

{{% details title="Como partilho ficheiros entre dois iPhones com SMB?" closed="true" %}}
Inicie o servidor SMB no primeiro iPhone no Everdisk. No segundo iPhone, abra a app Ficheiros, toque no botão mais, escolha Ligar ao servidor e introduza o endereço smb mostrado no Everdisk (por exemplo smb://192.168.1.20:4455/Share). Ligue-se como Convidado ou com o seu início de sessão, e a partilha aparece na app Ficheiros. Também pode usar o próprio separador Dispositivos do Everdisk no segundo telemóvel.
{{% /details %}}

{{% details title="O meu iPhone aparece automaticamente na barra lateral do Finder do Mac?" closed="true" %}}
Normalmente sim. O Everdisk anuncia a partilha SMB na sua rede Wi-Fi, por isso o seu iPhone aparece muitas vezes em Localizações ou Rede na barra lateral do Finder. Clique nele e escolha Ligar como, depois Convidado ou o seu início de sessão. Se não aparecer, ligue manualmente com Ir, Ligar ao servidor e o endereço smb completo.
{{% /details %}}

{{% details title="Preciso de uma palavra-passe para usar SMB?" closed="true" %}}
Não, o início de sessão é opcional. Deixe o Login e a Palavra-passe vazios em Definições, Partilha, Acesso para permitir acesso de convidado. Defina-os se quiser que as ligações iniciem sessão. Um login e uma palavra-passe só são obrigatórios se ativar Exigir encriptação SMB, porque as ligações encriptadas não podem ser anónimas.
{{% /details %}}

{{% details title="A ligação SMB é encriptada?" closed="true" %}}
Pode ser. O SMB é a única ligação do Everdisk que suporta encriptação. Defina um login e uma palavra-passe, depois ative Exigir encriptação SMB em Definições, Partilha. Cada transferência fica então protegida com SMB3 (AES). O outro dispositivo precisa de suportar SMB3, o que os Macs modernos e o Windows 10 ou posterior fazem. A encriptação é uma funcionalidade Premium.
{{% /details %}}

{{% details title="As pessoas podem alterar ou eliminar os meus ficheiros por SMB?" closed="true" %}}
Só se o permitir. O interruptor Edição de ficheiros em Definições, Partilha, Acesso controla isto. Com ele ativado, os dispositivos ligados podem enviar, mudar o nome e eliminar. Com ele desativado, a partilha é só de leitura e os outros podem navegar e copiar ficheiros para fora do seu telemóvel, mas não podem alterar nada.
{{% /details %}}

{{% details title="Porque é que a minha ligação SMB caiu?" closed="true" %}}
O seu iPhone é o servidor, e o iOS suspende as apps que ficam demasiado tempo em segundo plano. Mantenha o Everdisk aberto no ecrã enquanto um dispositivo estiver ligado, e ligue o telemóvel à corrente durante transferências longas. Certifique-se também de que ambos os dispositivos se mantiveram na mesma rede Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV ou FTP, qual devo usar?" closed="true" %}}
Use SMB quando quiser que o telemóvel se comporte como uma verdadeira unidade de rede num Mac, noutro iPhone, no Linux ou num NAS, e quando quiser encriptação. Use WebDAV quando quiser uma unidade de rede que também funcione bem a partir do Windows. Use FTP para a maior compatibilidade com dispositivos e apps mais antigos. O Everdisk pode executá-los todos ao mesmo tempo, por isso não fica preso a um só.
{{% /details %}}

{{% details title="O Everdisk é gratuito?" closed="true" %}}
Sim, o Everdisk é gratuito para transferir e o servidor SMB está incluído. A compra opcional Premium, feita uma única vez, adiciona a encriptação SMB, portas personalizadas e alguns outros extras. Pode configurar o SMB e partilhar ficheiros sem pagar.
{{% /details %}}

Pronto para experimentar? [Transfira o Everdisk da App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e abra o seu iPhone no Finder em cerca de um minuto. Perguntas ou comentários? Envie-nos um email para **support@everappz.com**.
