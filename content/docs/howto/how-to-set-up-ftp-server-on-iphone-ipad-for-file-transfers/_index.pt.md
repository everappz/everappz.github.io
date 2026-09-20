---
title: "Como configurar um servidor FTP no iPhone e iPad para transferências de ficheiros"
description: "Transforme o seu iPhone ou iPad num servidor FTP com o Everdisk e transfira ficheiros de um Mac, PC com Windows, Linux, Android, uma app FTP como o FileZilla ou outro iPhone por Wi-Fi. Configuração completa, o endereço e a porta ftp, acesso de convidado e ligação passo a passo para cada dispositivo."
date: 2026-09-19
tags: ["everdisk", "ftp", "transferencia de ficheiros", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["servidor FTP iPhone", "servidor FTP iPad", "como configurar FTP no iPhone", "app servidor ftp iphone", "ligar FileZilla ao iPhone", "Cyberduck iPhone FTP", "transferir ficheiros iPhone FTP", "ftp iphone para computador", "ftp iphone para iphone", "ligar ao FTP do iPhone a partir do Windows", "endereco porta ftp iphone", "ftp anonimo iphone", "partilhar ficheiros iphone ftp", "ftp iphone para camara nas"]
readingTime: 9
---

{{< author-byline >}}

O FTP é o velho fiável da transferência de ficheiros. Existe há décadas, e é exatamente por isso que é tão útil: quase tudo o que consegue comunicar com um servidor o compreende. Câmaras, smart TVs, routers, unidades de rede, ferramentas de automação e todas as apps FTP de secretária falam FTP. Com o [Everdisk](/products/everdisk) pode executar um servidor FTP no seu iPhone ou iPad, de forma a que o telemóvel se torne um local a que esses dispositivos e apps se podem ligar e mover ficheiros.

Escolha o FTP quando as outras opções não servirem, por exemplo um dispositivo mais antigo ou uma app que só sabe ligar por FTP. Este guia cobre a configuração e como ligar a partir de um Mac, Windows, uma app FTP, Linux, Android e um segundo iPhone.

## O que precisa

- Um iPhone ou iPad com o [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Um computador, app ou dispositivo na **mesma rede Wi-Fi**.
- Os ficheiros que quer partilhar, na pasta Documentos do Everdisk ou em pastas que adicionar.

## Configurar o servidor FTP no Everdisk

### Passo 1: escolher o que partilhar e definir o acesso

Abra o Everdisk, vá ao separador **Partilha** e toque em **O que partilhar**. A pasta Documentos é partilhada por predefinição. Adicione mais com **Adicionar pasta** e **Adicionar ficheiro**.

Abra **Definições**, depois **Partilha**, depois **Acesso**. Ative a **Edição de ficheiros** se quiser que as pessoas enviem, mudem o nome e eliminem, ou desative-a para permitir apenas transferências. Defina um **Login** e uma **Palavra-passe** se quiser um início de sessão, ou deixe-os vazios para que qualquer pessoa se possa ligar como convidado.

### Passo 2: ativar o servidor FTP

Vá a **Definições**, depois **Partilha**, depois **Ligações**, e ative **Outras apps e dispositivos**. Esse é o servidor FTP (tem a etiqueta FTP).

### Passo 3: iniciar a partilha e anotar o endereço

Volte ao separador **Partilha** e toque em **Iniciar**. A secção **Como ligar** mostra o endereço FTP. Tem este aspeto:

```
ftp://192.168.1.20:2121
```

O número a seguir aos dois pontos é a **porta**, que é **2121** por predefinição. A primeira parte é o endereço do seu iPhone na rede Wi-Fi, por isso o seu será diferente. Mantenha o Everdisk aberto no ecrã enquanto um dispositivo estiver ligado.

## Ligar a partir de um Mac

1. Abra o **Finder**, escolha **Ir**, depois **Ligar ao servidor** (ou prima **Command e K**).
2. Escreva o endereço FTP mostrado no Everdisk, por exemplo `ftp://192.168.1.20:2121`.
3. Clique em **Ligar**, depois escolha **Convidado** ou introduza o seu **Login** e **Palavra-passe**.

O Finder monta a partilha FTP para que possa navegar e copiar ficheiros para o seu Mac. Repare que o Finder abre o FTP como só de leitura. Quando quiser enviar a partir de um Mac, use uma app FTP como descrito abaixo.

## Ligar a partir do Windows

1. Abra o **Explorador de Ficheiros** e clique na barra de endereço no topo.
2. Escreva o endereço FTP do Everdisk, por exemplo `ftp://192.168.1.20:2121`, e prima **Enter**.
3. Introduza o seu **Login** e **Palavra-passe** se definiu algum, ou continue como convidado.

Os ficheiros partilhados aparecem na janela e pode copiá-los para o seu PC.

## Ligar com uma app FTP (FileZilla, Cyberduck)

Para envios e controlo total, uma app FTP é a melhor ferramenta. O **FileZilla** e o **Cyberduck** são gratuitos e funcionam no Windows, Mac e Linux.

1. Abra a app e crie uma nova ligação.
2. Defina o **Host** para o endereço Wi-Fi do seu iPhone, e a **Porta** para **2121**.
3. Para o início de sessão, introduza o seu **Login** e **Palavra-passe**, ou escolha **Anónimo** se não definiu nenhum.
4. Ligue-se e arraste ficheiros nos dois sentidos (os envios precisam da Edição de ficheiros ativada).

## Ligar a partir do Linux

1. Abra o seu gestor de ficheiros e escolha **Ligar ao servidor** ou **Outras localizações**.
2. Introduza o endereço, por exemplo `ftp://192.168.1.20:2121`.
3. Ligue-se como convidado ou com o seu início de sessão.

Também pode usar qualquer cliente FTP de Linux a partir do terminal, apontando-o para o mesmo anfitrião e a porta 2121.

## Ligar a partir do Android

O Android não tem um navegador FTP de sistema, por isso use uma app:

1. Instale um cliente FTP como o **AndFTP**, o **FTPCafe** ou um gestor de ficheiros com suporte de FTP como o **Solid Explorer**.
2. Adicione uma ligação com o anfitrião, a **porta 2121** e o seu início de sessão ou Anónimo.
3. Navegue e transfira.

## Ligar a partir de outro iPhone ou iPad

A app Ficheiros do iOS não inclui um cliente FTP, por isso use uma destas opções no segundo dispositivo:

- **O próprio separador Dispositivos do Everdisk.** Abra o Everdisk, vá a **Dispositivos**, toque em **Nova ligação**, escolha **FTP** e introduza o endereço, por exemplo `ftp://192.168.1.20:2121`. Esta é a via mais simples.
- **Uma app FTP dedicada** para iOS, usando o mesmo anfitrião, a porta 2121 e o início de sessão.

## Ligar outro equipamento: câmaras, TVs, routers e NAS

É aqui que o FTP brilha. Muitos dispositivos têm um cliente FTP integrado que consegue enviar ou obter ficheiros:

- **Câmaras** que enviam fotografias por FTP podem enviá-las diretamente para o seu iPhone.
- **Smart TVs, routers, caixas NAS e ferramentas de automação** que suportam FTP podem ligar-se da mesma forma.

Aponte-os para o endereço Wi-Fi do seu iPhone, a porta **2121** e o seu início de sessão (ou Anónimo), usando o endereço mostrado no Everdisk.

## Só de leitura ou de leitura e escrita

O interruptor **Edição de ficheiros** em Definições, Partilha, Acesso controla isto. Ativado permite que as pessoas enviem, mudem o nome e eliminem. Desativado significa que só podem transferir. Escolha só de leitura quando estiver a entregar ficheiros e não quiser que nada seja alterado no seu telemóvel.

## Formas reais de as pessoas usarem isto

- **Ligar o FileZilla ao seu iPhone** e enviar um lote de ficheiros para o telemóvel de uma só vez.
- **Deixar uma app ou dispositivo antigo que só fala FTP** aceder aos seus ficheiros quando nada mais se liga.
- **Receber fotografias de uma câmara** que envia por FTP.
- **Mover ficheiros entre um iPhone e um iPad** usando o separador Dispositivos do Everdisk no dispositivo que os recebe.

## Algumas dicas

- Mantenha o Everdisk aberto enquanto um dispositivo estiver ligado, uma vez que o iOS suspende as apps em segundo plano ao fim de algum tempo.
- Para enviar a partir de um Mac, use o FileZilla ou o Cyberduck em vez do Finder, porque o Finder abre o FTP como só de leitura.
- Deixe o início de sessão vazio para a maior compatibilidade, depois ligue-se como Anónimo, o que a maioria dos clientes FTP oferece.
- O FTP não encripta o seu tráfego. Numa rede em que não confia, use antes o [servidor SMB com encriptação](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Perguntas frequentes

{{% details title="Qual é o endereço e a porta FTP do meu iPhone?" closed="true" %}}
Depois de iniciar a partilha, o Everdisk mostra o endereço no ecrã de Partilha. Tem o aspeto ftp://192.168.1.20:2121. O 2121 é a porta que o Everdisk usa para FTP, e a primeira parte é o endereço do seu iPhone na rede Wi-Fi, por isso o seu será diferente.
{{% /details %}}

{{% details title="Como ligo o FileZilla ou o Cyberduck ao meu iPhone?" closed="true" %}}
Abra a app e crie uma nova ligação. Defina o Host para o endereço Wi-Fi do seu iPhone e a Porta para 2121. Introduza o seu Login e Palavra-passe, ou escolha Anónimo se não definiu nenhum no Everdisk. Ligue-se, e pode arrastar ficheiros nos dois sentidos quando a Edição de ficheiros estiver ativada.
{{% /details %}}

{{% details title="Posso ligar-me ao FTP do meu iPhone a partir do Windows?" closed="true" %}}
Sim. Abra o Explorador de Ficheiros, clique na barra de endereço, escreva o endereço FTP do Everdisk (por exemplo ftp://192.168.1.20:2121) e prima Enter. Introduza o seu início de sessão se definiu algum, ou continue como convidado. Para envios e mais controlo, use antes uma app FTP como o FileZilla.
{{% /details %}}

{{% details title="Preciso de um início de sessão para FTP?" closed="true" %}}
Não, o início de sessão é opcional. Deixe o Login e a Palavra-passe vazios em Definições, Partilha, Acesso, e ligue-se como Anónimo, o que a maioria dos clientes FTP oferece. Defina um início de sessão se quiser que as ligações iniciem sessão primeiro.
{{% /details %}}

{{% details title="Porque é que só consigo transferir e não enviar por FTP?" closed="true" %}}
Há duas razões comuns. Primeiro, o interruptor Edição de ficheiros em Definições, Partilha, Acesso tem de estar ativado para permitir envios, mudanças de nome e eliminações. Segundo, o Finder do Mac abre o FTP como só de leitura, por isso use uma app FTP como o FileZilla ou o Cyberduck quando quiser enviar.
{{% /details %}}

{{% details title="Posso usar FTP entre dois iPhones?" closed="true" %}}
Sim. Inicie o servidor FTP no primeiro iPhone. No segundo, abra o Everdisk, vá ao separador Dispositivos, toque em Nova ligação, escolha FTP e introduza o endereço mostrado no primeiro telemóvel. Uma app FTP dedicada para iOS também funciona, uma vez que a app Ficheiros do iOS não inclui um cliente FTP.
{{% /details %}}

{{% details title="O FTP é seguro?" closed="true" %}}
O FTP simples não encripta o seu tráfego, por isso trate-o como uma ferramenta para redes em que confia, como a sua Wi-Fi de casa. Numa rede que não controla, use o servidor SMB com Exigir encriptação SMB ativado, que protege cada transferência.
{{% /details %}}

{{% details title="Que dispositivos se podem ligar por FTP?" closed="true" %}}
Quase tudo o que tenha um cliente FTP. Isso inclui computadores Mac, Windows e Linux, apps FTP como o FileZilla e o Cyberduck, gestores de ficheiros Android e hardware como câmaras, smart TVs, routers, caixas NAS e ferramentas de automação. Esse amplo alcance é a principal razão para escolher FTP.
{{% /details %}}

{{% details title="Porque é que a minha ligação FTP caiu?" closed="true" %}}
O seu iPhone é o servidor, e o iOS suspende as apps que ficam demasiado tempo em segundo plano. Mantenha o Everdisk aberto no ecrã enquanto um dispositivo estiver ligado, e ligue à corrente durante transferências longas. Certifique-se também de que ambos os dispositivos continuam na mesma rede Wi-Fi.
{{% /details %}}

{{% details title="O Everdisk é gratuito?" closed="true" %}}
Sim, o Everdisk é gratuito para transferir e o servidor FTP está incluído. Uma compra opcional Premium, feita uma única vez, adiciona extras como portas personalizadas e conversão de fotos e vídeos. Pode configurar o FTP e transferir ficheiros sem pagar.
{{% /details %}}

Pronto para experimentar? [Transfira o Everdisk da App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e ligue o seu primeiro cliente FTP em poucos minutos. Perguntas ou comentários? Envie-nos um email para **support@everappz.com**.
