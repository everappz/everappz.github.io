---
title: "Como configurar um servidor WebDAV no iPhone e iPad para acesso e partilha de ficheiros"
description: "Transforme o seu iPhone ou iPad num servidor WebDAV com o Everdisk e monte-o como unidade de rede no Finder do Mac, no Explorador de Ficheiros do Windows, no Linux, no Android ou noutro iPhone por Wi-Fi. Configuração completa, o endereço e a porta WebDAV, e ligação passo a passo para cada dispositivo."
date: 2026-09-19
tags: ["everdisk", "webdav", "unidade de rede", "partilha de ficheiros", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["servidor WebDAV iPhone", "servidor WebDAV iPad", "como configurar WebDAV no iPhone", "montar iPhone como unidade de rede", "ligar iPhone WebDAV Mac Finder", "WebDAV Explorador de Ficheiros Windows iPhone", "iphone unidade de rede Windows", "WebDAV Linux iPhone", "aceder aos ficheiros do iPhone a partir do computador", "webdav iphone para iphone", "partilhar ficheiros iPhone WebDAV", "mapear unidade de rede iphone", "transferir ficheiros iphone webdav", "endereco porta webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

O WebDAV transforma uma pasta numa unidade de rede que um computador pode abrir no seu gestor de ficheiros normal. Funciona sobre o mesmo protocolo web que o seu navegador usa, e é por isso que viaja bem entre Mac, Windows e Linux sem controladores especiais. Com o [Everdisk](/products/everdisk) pode executar um servidor WebDAV no seu iPhone ou iPad, de forma a que o telemóvel apareça como uma unidade que pode navegar, copiar a partir dela e copiar para ela a partir de quase qualquer computador.

O WebDAV é a melhor escolha quando o Windows está envolvido, porque o Explorador de Ficheiros do Windows liga-se a ele de forma limpa. Este guia cobre a configuração e como ligar a partir de um Mac, Windows, Linux, Android e um segundo iPhone.

## O que precisa

- Um iPhone ou iPad com o [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Um computador ou outro dispositivo na **mesma rede Wi-Fi**.
- Os ficheiros que quer partilhar, na pasta Documentos do Everdisk ou em pastas que adicionar.

## Configurar o servidor WebDAV no Everdisk

### Passo 1: escolher o que partilhar e definir o acesso

Abra o Everdisk, vá ao separador **Partilha** e toque em **O que partilhar**. A pasta Documentos é partilhada por predefinição. Adicione mais com **Adicionar pasta** e **Adicionar ficheiro**.

Abra **Definições**, depois **Partilha**, depois **Acesso**. Ative a **Edição de ficheiros** se quiser que os computadores ligados copiem ficheiros para o seu telemóvel e lhes mudem o nome ou os eliminem, ou desative-a para uma unidade só de leitura. Defina aqui um **Login** e uma **Palavra-passe** se quiser um início de sessão, ou deixe-os vazios para acesso de convidado.

### Passo 2: ativar o servidor WebDAV

Vá a **Definições**, depois **Partilha**, depois **Ligações**, e ative **Computador**. Esse é o servidor WebDAV (tem a etiqueta WebDAV).

### Passo 3: iniciar a partilha e anotar o endereço

Volte ao separador **Partilha** e toque em **Iniciar**. A secção **Como ligar** mostra o endereço WebDAV. Tem este aspeto:

```
http://192.168.1.20:8080
```

O número a seguir aos dois pontos é a **porta**, que é **8080** por predefinição. A primeira parte é o endereço do seu iPhone na rede Wi-Fi, por isso o seu será diferente. Mantenha o Everdisk aberto no ecrã enquanto um dispositivo estiver ligado.

## Ligar a partir de um Mac

1. Abra o **Finder**, escolha **Ir**, depois **Ligar ao servidor** (ou prima **Command e K**).
2. Escreva o endereço WebDAV mostrado no Everdisk, por exemplo `http://192.168.1.20:8080`.
3. Clique em **Ligar**, depois escolha **Convidado** ou introduza o seu **Login** e **Palavra-passe**.

O seu iPhone abre-se numa janela do Finder e comporta-se como uma pasta normal. Copie ficheiros em qualquer direção se a Edição de ficheiros estiver ativada.

## Ligar a partir do Windows

O Windows tem um cliente WebDAV integrado, por isso isto funciona a partir do Explorador de Ficheiros.

1. Abra o **Explorador de Ficheiros**, clique com o botão direito em **Este PC** na barra lateral e escolha **Adicionar uma localização de rede** (também pode usar **Mapear unidade de rede**).
2. Quando for pedido o endereço, escreva o mesmo endereço WebDAV do Everdisk, por exemplo `http://192.168.1.20:8080`, e clique em **Seguinte**.
3. Introduza o seu **Login** e **Palavra-passe** se definiu algum.

O dispositivo aparece então em Este PC como uma localização de rede que pode abrir e a partir da qual pode copiar ficheiros. Se o Windows se recusar a ligar da primeira vez, certifique-se de que o serviço **WebClient** está em execução (procure Serviços no menu Iniciar, encontre o WebClient e configure-o para arrancar), depois tente de novo.

## Ligar a partir do Linux

1. Abra o seu gestor de ficheiros e escolha **Ligar ao servidor** ou **Outras localizações**.
2. Introduza o endereço com um prefixo WebDAV, por exemplo `dav://192.168.1.20:8080` (use `davs://` apenas se configurou TLS).
3. Ligue-se como convidado ou introduza o seu início de sessão.

## Ligar a partir do Android

O Android não tem um navegador WebDAV de sistema, por isso use um gestor de ficheiros que o suporte:

1. Instale uma app como o **Solid Explorer** ou o **CX File Explorer**.
2. Adicione uma nova ligação **WebDAV**.
3. Introduza o anfitrião e a **porta 8080**, escolha o esquema `http` e adicione o seu início de sessão se definiu algum.

## Ligar a partir de outro iPhone ou iPad

A app Ficheiros do iOS não inclui um cliente WebDAV, por isso use uma destas opções:

- **O próprio separador Dispositivos do Everdisk.** No segundo dispositivo, abra o Everdisk, vá a **Dispositivos**, toque em **Nova ligação**, escolha **WebDAV** e introduza o endereço, por exemplo `http://192.168.1.20:8080`. Esta é a via mais simples e não precisa de nada mais.
- **Uma app WebDAV** como o Documents da Readdle, que pode adicionar uma ligação WebDAV com o mesmo endereço e início de sessão.

## Prefere uma ligação rápida em vez de uma unidade?

Se só precisa de obter um ficheiro depressa e não quer montar uma unidade de todo, ative a ligação **Navegador** em Definições, Partilha, Ligações. O Everdisk dá-lhe então um endereço web que pode abrir em qualquer navegador em qualquer dispositivo para navegar e transferir os seus ficheiros. É a forma mais rápida de entregar um ficheiro a um PC com Windows, a um Chromebook ou ao telemóvel de um amigo.

## Só de leitura ou de leitura e escrita

O interruptor **Edição de ficheiros** em Definições, Partilha, Acesso decide isto. Ativado significa que os computadores ligados podem enviar, mudar o nome e eliminar. Desativado significa que a unidade é só de leitura, por isso os outros podem ver e copiar os seus ficheiros mas não os podem alterar.

## Formas reais de as pessoas usarem isto

- **Copiar ficheiros para o seu iPhone a partir de um PC com Windows** mapeando-o como uma localização de rede e arrastando-os.
- **Descarregar fotografias e documentos para um portátil** usando o gestor de ficheiros que já conhece, sem cabo e sem iTunes.
- **Editar um documento no lugar** a partir do seu Mac, abrindo-o diretamente do telemóvel e voltando a guardá-lo.
- **Mover uma pasta entre um iPhone e um iPad** usando o separador Dispositivos do Everdisk no dispositivo que a recebe.

## Algumas dicas

- Mantenha o Everdisk aberto enquanto um dispositivo estiver ligado. Bloquear o telemóvel durante muito tempo pode suspender a app.
- No Windows, se a ligação falhar, inicie o serviço WebClient e tente o endereço de novo.
- O WebDAV e o SMB montam-se ambos como unidades de rede. Use WebDAV quando o Windows estiver envolvido, e [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) quando quiser a velocidade do Finder e encriptação.
- Para as transferências mais rápidas, mantenha a qualidade de fotos e vídeos em Original nas Definições.

## Perguntas frequentes

{{% details title="Qual é o endereço e a porta WebDAV do meu iPhone?" closed="true" %}}
Depois de iniciar a partilha, o Everdisk mostra o endereço no ecrã de Partilha. Tem o aspeto http://192.168.1.20:8080. O 8080 é a porta que o Everdisk usa para WebDAV, e a primeira parte é o endereço do seu iPhone na rede Wi-Fi, por isso o seu será diferente.
{{% /details %}}

{{% details title="Como me ligo ao WebDAV do meu iPhone a partir do Windows?" closed="true" %}}
Abra o Explorador de Ficheiros, clique com o botão direito em Este PC e escolha Adicionar uma localização de rede ou Mapear unidade de rede. Introduza o endereço WebDAV do Everdisk, por exemplo http://192.168.1.20:8080, depois introduza o seu início de sessão se definiu algum. Se o Windows não se ligar, certifique-se de que o serviço WebClient está em execução (procure Serviços, encontre o WebClient, inicie-o) e tente de novo.
{{% /details %}}

{{% details title="Posso usar WebDAV entre dois iPhones?" closed="true" %}}
Sim, mas a app Ficheiros do iOS não tem cliente WebDAV, por isso use o Everdisk no segundo dispositivo. Abra o separador Dispositivos, toque em Nova ligação, escolha WebDAV e introduza o endereço mostrado no primeiro telemóvel. Uma app WebDAV como o Documents da Readdle também funciona.
{{% /details %}}

{{% details title="O WebDAV precisa de palavra-passe?" closed="true" %}}
Não, o início de sessão é opcional. Deixe o Login e a Palavra-passe vazios em Definições, Partilha, Acesso para acesso de convidado, ou defina-os se quiser que as ligações iniciem sessão.
{{% /details %}}

{{% details title="Outras pessoas podem alterar os meus ficheiros por WebDAV?" closed="true" %}}
Só se o permitir. O interruptor Edição de ficheiros em Definições, Partilha, Acesso controla isto. Ativado permite que os dispositivos ligados enviem, mudem o nome e eliminem. Desativado torna a unidade só de leitura, por isso os outros podem ver e copiar mas não alterar nada.
{{% /details %}}

{{% details title="WebDAV ou SMB, qual é a diferença?" closed="true" %}}
Ambos montam o seu iPhone como uma unidade de rede. O WebDAV funciona sobre o protocolo web e liga-se de forma limpa a partir do Explorador de Ficheiros do Windows, o que é a sua principal vantagem. O SMB é a partilha de ficheiros nativa em Mac, Linux e dispositivos NAS, é normalmente mais rápido num Mac, e é a única ligação do Everdisk que consegue encriptar transferências. O Everdisk pode executar ambos ao mesmo tempo.
{{% /details %}}

{{% details title="Porque é que a minha unidade WebDAV se desliga?" closed="true" %}}
O seu iPhone é o servidor, e o iOS suspende as apps que ficam demasiado tempo em segundo plano. Mantenha o Everdisk aberto no ecrã enquanto um dispositivo estiver ligado, e ligue à corrente durante transferências longas. Confirme também que ambos os dispositivos continuam na mesma rede Wi-Fi.
{{% /details %}}

{{% details title="Posso ligar-me por WebDAV sem Wi-Fi?" closed="true" %}}
Sim, se ligar o seu iPhone a um Mac com um cabo. O Everdisk mostra então um endereço extra de ligação por cabo que o Mac ligado pode abrir no Finder, o que funciona mesmo sem Wi-Fi nenhuma. Pelo cabo, só esse Mac consegue aceder ao dispositivo.
{{% /details %}}

{{% details title="O Everdisk é gratuito?" closed="true" %}}
Sim, o Everdisk é gratuito para transferir e o servidor WebDAV está incluído. Uma compra opcional Premium, feita uma única vez, adiciona extras como portas personalizadas e conversão de fotos e vídeos. Pode configurar o WebDAV e partilhar ficheiros sem pagar.
{{% /details %}}

Pronto para experimentar? [Transfira o Everdisk da App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e monte o seu iPhone como uma unidade em poucos minutos. Perguntas ou comentários? Envie-nos um email para **support@everappz.com**.
