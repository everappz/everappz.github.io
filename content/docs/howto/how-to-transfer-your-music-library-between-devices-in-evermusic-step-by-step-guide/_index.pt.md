---
title: "Como transferir sua biblioteca de músicas entre dispositivos no Evermusic: guia passo a passo"
description: "Transfira facilmente sua biblioteca de músicas do Evermusic, listas de reprodução, capas de álbuns e configurações de um iPhone, iPad ou Mac para outro usando Wi-Fi Drive e ferramentas de backup."
date: 2024-12-29
tags: ["bibliotecademusicas", "transferencia", "wifi", "backup", "webdav", "restauracao"]
keywords: ["transferir biblioteca de músicas Evermusic", "backup e restauração de listas de reprodução Evermusic", "Evermusic WiFi Drive", "sincronizar Evermusic entre dispositivos", "mover banco de dados Evermusic", "transferência de arquivos Evermusic", "restaurar configurações do player de áudio", "transferência de música WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**Resumo:** Para transferir sua biblioteca do Evermusic para um novo dispositivo, crie um backup no dispositivo de origem, inicie o Wi-Fi Drive, conecte o segundo dispositivo pela mesma rede, baixe o backup e os arquivos de música e restaure a partir do backup. Todo o processo leva cerca de 10 minutos, dependendo do tamanho da biblioteca.

Neste guia, vamos orientá-lo na transferência de toda a sua biblioteca de músicas — incluindo banco de dados, capas de álbuns e configurações — de um dispositivo (iPhone ou Mac) para outro. Embora a sincronização automática da biblioteca de músicas e listas de reprodução seja um recurso planejado para o futuro, este processo atualmente precisa ser feito manualmente.

## Passo 1: Crie um backup no primeiro dispositivo

1. **Abra o aplicativo no seu primeiro dispositivo** (aquele com sua biblioteca de músicas, listas de reprodução e serviços em nuvem conectados).
2. **Navegue até Configurações** e selecione a opção **Backup e Restauração**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Na tela de **Backup e Restauração**, escolha os itens para incluir no arquivo de backup:
   - **Banco de dados** (inclui sua biblioteca de músicas e listas de reprodução)
   - **Capas de álbuns**
   - **Configurações**

Essas opções estão ativadas por padrão.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Toque em **Fazer backup dos dados do aplicativo** para iniciar o processo.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Quando o backup estiver concluído, um alerta informativo aparecerá.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Toque em **Mostrar arquivo** para revelar o arquivo de backup no diretório **Documentos**. Os arquivos de backup geralmente são salvos na pasta **Backup**.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Passo 2: Inicie o servidor Wi-Fi Drive

1. Vá para a seção **Conexões** no aplicativo.
2. Role para baixo até **Conectar usando Wi-Fi** e toque nele.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Na próxima tela, toque em **Iniciar Wi-Fi Drive**.

- Opcionalmente, você pode definir um login e senha para segurança, mas isso é desnecessário para redes domésticas.

4. Uma vez iniciado, você verá os endereços de servidor disponíveis. Isso pode ser usado para navegadores de desktop ou aplicativos WebDAV, mas neste guia, prosseguiremos diretamente para os próximos passos.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Passo 3: Conecte seu segundo dispositivo ao primeiro

1. Abra o aplicativo no segundo dispositivo (para onde você deseja transferir a biblioteca).
2. Certifique-se de que ambos os dispositivos estejam conectados à mesma rede Wi-Fi.
3. No segundo dispositivo, abra a aba **Conexões** e selecione **Dispositivos disponíveis**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Você deve ver uma conexão WebDAV chamada **Evermusic** (o servidor que iniciamos no primeiro dispositivo). Toque nela para conectar.

5. Uma vez conectado, você verá todas as pastas do primeiro dispositivo.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Passo 4: Prepare-se para a transferência de arquivos

1. No segundo dispositivo, vá para **Configurações > Gerenciador de arquivos** e ative **Salvar arquivos baixados em - Perguntar sempre**.

- Isso garante que você possa selecionar a pasta de destino para cada download.

2. Retorne à aba **Conexões** e navegue até o servidor WebDAV conectado.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Passo 5: Transfira o backup e os arquivos de música

1. Abra a pasta **Backup** no servidor WebDAV conectado.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Toque no botão **Mais ações** (três pontos) próximo ao arquivo de backup e selecione **Baixar**.

3. Crie uma pasta **Backup** no segundo dispositivo para armazenar os arquivos baixados. Confirme sua seleção tocando em **Concluído**.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Transfira quaisquer arquivos de música adicionais:
   - Verifique a pasta **Baixar** ou outras pastas relevantes no servidor WebDAV.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Use a opção **Selecionar** para escolher arquivos e toque em **Mais ações > Baixar**. Salve-os na pasta correspondente no segundo dispositivo para manter a mesma estrutura de diretórios.

O objetivo é transferir todos os arquivos do primeiro dispositivo para o dispositivo atual, garantindo que a estrutura de pastas permaneça idêntica. Dessa forma, os links na sua biblioteca de músicas e listas de reprodução permanecem intactos. Observe que arquivos locais armazenados fora do diretório Documentos do aplicativo no primeiro dispositivo devem ser transferidos separadamente. Como o aplicativo não pode acessar esses arquivos no modo Wi-Fi Drive, você precisará usar o aplicativo Arquivos do Sistema para a transferência.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Passo 6: Monitore o progresso da transferência

1. No segundo dispositivo, vá para a seção **Arquivos locais** (ou a aba **Baixar** no iPad/Mac).

2. Toque no botão **Atividade de transferência** no canto superior esquerdo para monitorar a fila de transferência.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Passo 7: Restaure os dados do backup

1. Quando o arquivo de backup e todos os arquivos de áudio necessários forem baixados para o segundo dispositivo, abra a pasta **Backup**.

2. Toque no arquivo de backup e uma mensagem de confirmação aparecerá.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Nota:** A restauração substituirá todos os dados atuais da biblioteca de músicas, listas de reprodução, configurações e capas de álbuns pelos dados do backup.

3. Toque em **Restaurar** para iniciar o processo.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Após a restauração ser concluída, um alerta confirmará o sucesso.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Verifique as seções **Listas de reprodução** ou **Biblioteca de músicas** para confirmar a restauração.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Passo 8: Reindexe a biblioteca de músicas

1. Para melhores resultados, reindexe sua biblioteca para garantir que todos os arquivos foram detectados com sucesso.

2. Vá para **Configurações > Biblioteca de músicas > Sincronização de música offline** e selecione **Iniciar varredura de pastas locais**.

Seguindo estes passos, você transferirá com sucesso sua biblioteca de músicas, listas de reprodução e configurações para outro dispositivo. Se encontrar algum problema, não hesite em entrar em contato com o suporte.

## Perguntas frequentes

{{% details title="Posso transferir minha biblioteca do Evermusic sem Wi-Fi?" closed="true" %}}
O Wi-Fi Drive requer que ambos os dispositivos estejam na mesma rede Wi-Fi. Atualmente não há opção de transferência por Bluetooth ou celular. Como alternativa, você pode usar o AirDrop ou o aplicativo Arquivos para mover manualmente o arquivo de backup e as pastas de música entre dispositivos.
{{% /details %}}

{{% details title="As conexões dos serviços em nuvem são transferidas com o backup?" closed="true" %}}
O backup inclui seu banco de dados, listas de reprodução, capas de álbuns e configurações. As credenciais de login dos serviços em nuvem não são incluídas por motivos de segurança. Você precisará reconectar suas contas em nuvem no novo dispositivo após a restauração.
{{% /details %}}

{{% details title="O que acontece com a biblioteca existente no segundo dispositivo?" closed="true" %}}
A restauração de um backup substitui todos os dados existentes da biblioteca de músicas, listas de reprodução, configurações e capas de álbuns no segundo dispositivo. Faça um backup separado do segundo dispositivo primeiro se quiser preservar seus dados.
{{% /details %}}

{{% details title="Este processo funciona entre iPhone e Mac?" closed="true" %}}
Sim. O Evermusic suporta transferência Wi-Fi Drive entre qualquer combinação de iPhone, iPad e Mac. Ambos os dispositivos precisam apenas estar na mesma rede Wi-Fi.
{{% /details %}}

{{% details title="Quanto tempo leva a transferência?" closed="true" %}}
O tempo de transferência depende do tamanho da sua biblioteca de músicas e da velocidade do Wi-Fi. Uma biblioteca típica de alguns gigabytes é transferida em 5-15 minutos em uma rede doméstica padrão.
{{% /details %}}
