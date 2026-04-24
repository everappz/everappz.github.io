---
title: "Transferir arquivos do computador para o iPhone usando o protocolo SMB"
description: "Aprenda a transferir e acessar arquivos grandes do seu Mac ou PC Windows para o seu iPhone ou iPad usando o Evermusic e o protocolo SMB. Um guia passo a passo para streaming e gerenciamento de arquivos sem interrupções."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transferir arquivos para iPhone SMB", "transmitir música do PC no iPhone", "conectar Mac ao iPhone SMB", "configuração Evermusic SMB", "acessar arquivos do computador iPhone", "compartilhar música Windows iOS", "transferência de arquivos SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Resumo:** Use o Evermusic no seu iPhone ou iPad para acessar arquivos armazenados no seu Mac ou PC Windows pela rede local via SMB. Sem cabos, sem iTunes, sem necessidade de upload para a nuvem. Ative o compartilhamento de arquivos no seu computador, conecte-se no aplicativo e navegue ou reproduza seus arquivos sem fio.

Você tem uma extensa coleção de arquivos grandes no seu MAC ou PC e deseja acessá-los facilmente pelo seu iPhone ou iPad? Nossos aplicativos fornecem uma solução simples.

Siga estas etapas para habilitar o acesso contínuo entre o seu computador e o dispositivo iOS usando o protocolo SMB:

## Etapa 1: Ativar o protocolo SMB no seu computador

**Para MAC:**

1. Abra as "Preferências do Sistema" no seu MAC.
2. Clique em "Compartilhamento".
3. Ative o serviço "Compartilhamento de Arquivos".
4. Adicione sua pasta de música à seção "Pastas Compartilhadas". Adicione um usuário e escolha o nível de permissão (Leitura e Gravação ou Somente Leitura). Você pode optar por "Todos: Somente Leitura" para a pasta de música adicionada.

   ![Tela de configurações do Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Lembre-se da URL do computador (smb://192.168.xx.xx), pois você a usará nas próximas etapas.
6. Clique em "Opções" e ative "Compartilhar arquivos e pastas usando SMB".

   ![Tela de compartilhamento de arquivos do Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Ative o "Compartilhamento de Arquivos do Windows" para as contas disponíveis.

   ![Tela de compartilhamento SMB do Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Para Windows PC:**

1. Clique com o botão direito na sua pasta de música.
2. Selecione "Propriedades".
3. Navegue até a aba "Compartilhamento".
4. Clique em "Compartilhar..."
5. Escolha as pessoas com quem deseja compartilhar a pasta e especifique o nível de permissão. Você pode selecionar "Todos: Leitura" para a pasta de música escolhida.

   ![Tela de compartilhamento SMB do Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Clique em "Concluído".
7. Clique em "Concluído" na janela "Compartilhamento de Arquivos" e lembre-se do caminho da pasta.

   ![Pasta compartilhada SMB do Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Etapa 2: Conectar seu dispositivo iOS

1. Abra o aplicativo no seu iPhone ou iPad.
2. Vá para a aba "Conexões".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Tela de Conexões do Evermusic"
  caption="Tela de Conexões do Evermusic"
  width="400"
>}}

*Se o seu computador aparecer na seção "Dispositivos disponíveis":*

Se o seu computador estiver visível na seção "Dispositivos disponíveis" e você selecionou "Todos: Somente Leitura" na etapa anterior, basta tocar no seu computador e ele se conectará automaticamente.

*Se o seu computador não aparecer automaticamente:*

1. Toque em "Conectar um serviço na nuvem".
2. Selecione "SMB" na tela "Conectar um serviço na nuvem".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Tela Conectar um serviço na nuvem do Evermusic"
  caption="Tela Conectar um serviço na nuvem do Evermusic"
  width="400"
>}}

3. Na tela "Conexão SMB", insira a URL do servidor com o caminho da pasta compartilhada. Você pode usar o nome do servidor ou o IP do servidor:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Insira seu login e senha ou deixe esses campos em branco se você selecionou "Todos: Somente Leitura" na etapa anterior.
5. O campo "WORKGROUP" é opcional e deve ser usado se você tiver um Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Tela do conector SMB do Evermusic"
  caption="Tela do conector SMB do Evermusic"
  width="400"
>}}

6. Depois de conectar seu computador usando o protocolo SMB, ele aparecerá na seção "Serviços na nuvem" da tela "Conexões".
7. Abra o serviço conectado e navegue até a pasta desejada.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Pasta SMB aberta no Evermusic"
  caption="Pasta SMB aberta no Evermusic"
  width="400"
>}}

8. Você pode utilizar o gerenciador de arquivos integrado para editar seus arquivos conforme necessário.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Gerenciador de arquivos do Evermusic"
  caption="Gerenciador de arquivos do Evermusic"
  width="400"
>}}

## Etapa 3: Solução para pastas SMB2 com caracteres especiais

Às vezes, você pode encontrar problemas com pastas contendo caracteres especiais ao usar o protocolo SMB2. Aqui estão algumas etapas para resolver esse problema:

1. **Ativar SMB 1:**  
   • Como solução temporária, tente ativar o SMB 1 no seu servidor e nas configurações do aplicativo. Isso pode ajudar a contornar os problemas relacionados a caracteres especiais nos nomes das pastas.

2. **Usar o menu de abertura de arquivos do sistema:**  
   • Navegue até "Arquivos locais".  
   • Role para baixo até a seção "Arquivos neste dispositivo".  
   • Toque em "Abrir arquivos..." ou "Abrir pastas...".  
   • Localize seu servidor e selecione os arquivos ou pastas necessários.  
   • Toque em "Abrir" para confirmar sua seleção.

3. **Protocolos alternativos:**  
   • Se o problema persistir, considere conectar-se ao seu NAS usando os protocolos WebDAV ou DLNA se o seu NAS suportar essas opções. Esses protocolos podem lidar com caracteres especiais de forma mais adequada.

Seguindo essas etapas, você pode mitigar os problemas com caracteres especiais nos nomes das pastas ao usar o protocolo SMB2.

## Conclusão

Com essas etapas, você pode acessar facilmente sua vasta coleção de arquivos do seu MAC ou PC no seu iPhone ou iPad usando nossos aplicativos.

## Perguntas frequentes

{{% details title="Posso acessar arquivos no meu PC pelo meu iPhone sem iTunes?" closed="true" %}}
Sim. O Evermusic se conecta ao seu computador via SMB na sua rede Wi-Fi local. Não é necessária sincronização com iTunes ou Finder. Ative o compartilhamento de arquivos no seu PC e conecte-se diretamente pelo aplicativo.
{{% /details %}}

{{% details title="O acesso a arquivos SMB funciona pela internet?" closed="true" %}}
Não. O SMB é um protocolo de rede local. Seu iPhone e computador devem estar na mesma rede Wi-Fi. Para acesso remoto, envie os arquivos para um serviço na nuvem como Google Drive ou Dropbox e conecte-se a ele no Evermusic.
{{% /details %}}

{{% details title="Quais tipos de arquivo posso acessar via SMB?" closed="true" %}}
O Evermusic suporta MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC e outros formatos de áudio. Você também pode navegar e gerenciar arquivos não-áudio usando o gerenciador de arquivos integrado.
{{% /details %}}

{{% details title="Posso transferir arquivos de um NAS para meu iPhone usando SMB?" closed="true" %}}
Sim. A maioria dos dispositivos NAS (Synology, QNAP, WD My Cloud e outros) suportam SMB. Conecte-se ao seu NAS usando as mesmas etapas deste guia.
{{% /details %}}

{{% details title="Preciso copiar arquivos para meu iPhone para reproduzi-los?" closed="true" %}}
Não. O Evermusic transmite arquivos diretamente do seu computador ou NAS pela rede. Os arquivos não são copiados para o seu iPhone, a menos que você opte por baixá-los para reprodução offline.
{{% /details %}}

{{% details title="O compartilhamento de arquivos SMB é seguro?" closed="true" %}}
O compartilhamento de arquivos SMB funciona apenas na sua rede local. Outros dispositivos em redes diferentes não podem acessar suas pastas compartilhadas. Para segurança adicional, use login e senha em vez de acesso anônimo (Todos).
{{% /details %}}
