---
title: "Como conectar o armazenamento interno do Bluesound VAULT a partir do Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Aprenda como acessar o disco rígido interno do Bluesound VAULT a partir do Evermusic, Flacbox e Evertag usando o protocolo SMB para gerenciar, editar e reproduzir arquivos de áudio."
keywords: ["bluesound vault", "conectar armazenamento smb", "evermusic smb", "flacbox vault", "evertag smb", "armazenamento nas música", "unidade interna vault"]
tags: ["evermusic", "conectar", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Resumo:** Conecte-se ao armazenamento interno do seu Bluesound VAULT via SMB usando Evermusic, Flacbox ou Evertag. Encontre o endereço IP do VAULT no aplicativo BluOS, insira-o como uma conexão SMB com acesso de convidado e comece a reproduzir ou gerenciar seus arquivos de música.

O Bluesound VAULT possui um disco rígido interno e funciona como um armazenamento conectado à rede (NAS). O acesso ao disco rígido interno do VAULT permite adicionar/excluir arquivos, editar tags de metadados a partir dos nossos aplicativos Evermusic, Flacbox, Evertag.

**A seguir estão os passos para acessar o disco rígido interno do seu VAULT:**

1. No aplicativo BluOS, selecione **Ajuda > Diagnósticos**.

2. Na página de **Diagnósticos**, obtenha o **Endereço IP** do VAULT. Este **Endereço IP** será usado nos próximos passos.

3. Abra o Evermusic, Flacbox ou Evertag.

   ![Aplicativos Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Abra a tela "Conexões" e selecione o item de menu "Conectar um serviço de nuvem".

   ![Tela de Conexões do Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Selecione o serviço de nuvem "SMB".

   ![Tela Conectar um Serviço de Nuvem do Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Na "Tela de configuração SMB" insira a URL no seguinte formato:

   ```
   SMB://<<VAULT-IP>>
   ```

   Substitua `<<VAULT-IP>>` pelo **Endereço IP** obtido no Passo 2.

   **Nota:** Deixe os campos de Login e Senha em branco porque o armazenamento VAULT suporta o modo CONVIDADO.

   ![Tela de conexão SMB do Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Toque no botão "Entrar" para salvar a configuração.

8. Abra o armazenamento em nuvem conectado, navegue até a pasta com arquivos de áudio e toque em qualquer arquivo para iniciar o reprodutor de áudio.

   ![Tela do Servidor SMB Aberto do Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Você também pode editar arquivos usando o gerenciador de arquivos integrado.

   ![Tela do Gerenciador de Arquivos do Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Com esses passos simples, você pode acessar facilmente o disco rígido interno do seu Bluesound VAULT e assumir o controle da sua biblioteca de música usando Evermusic, Flacbox ou Evertag.

## Perguntas Frequentes

{{% details title="Preciso de um nome de usuário e senha para me conectar ao Bluesound VAULT?" closed="true" %}}
Não. O Bluesound VAULT suporta acesso de convidado (anônimo) via SMB. Deixe os campos de Login e Senha em branco ao configurar a conexão.
{{% /details %}}

{{% details title="Posso editar tags de música no Bluesound VAULT?" closed="true" %}}
Sim. Usando o Evertag, você pode editar tags de metadados (título, artista, álbum, etc.) de arquivos de áudio armazenados diretamente no disco rígido interno do VAULT.
{{% /details %}}

{{% details title="Quais protocolos o Bluesound VAULT suporta?" closed="true" %}}
O Bluesound VAULT expõe seu armazenamento interno via SMB (Server Message Block). Evermusic, Flacbox e Evertag suportam conexões SMB, tornando a conexão simples.
{{% /details %}}

{{% details title="Posso transmitir música do VAULT sem copiar arquivos para o meu iPhone?" closed="true" %}}
Sim. Uma vez conectado via SMB, você pode transmitir arquivos de áudio diretamente da unidade interna do VAULT sem copiá-los para o seu dispositivo.
{{% /details %}}
