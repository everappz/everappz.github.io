---
title: "Configurações"
date: 2020-02-01
lastmod: 2026-06-01
description: "Explore cada configuração no Evervideo — Leitor de Multimédia (Imagem-em-imagem, descodificação H.264 / HEVC por hardware, equalizador de vídeo, escala, rotação, viewport VR), Áudio (equalizador, taxa de amostragem, canais, buffer IO, modo misto), Legendas (primárias / secundárias, tipo de letra, ficheiro externo, libass), Biblioteca de Multimédia, Gestor de Ficheiros, Wi-Fi Drive, Widgets, Personalização, Idioma, Código de Acesso, Backup e Restauro — para iPhone, iPad e Mac."
keywords: [
  "configurações Evervideo", "configuração de leitor de vídeo", "atualização Premium Evervideo",
  "configurações imagem-em-imagem", "configurações equalizador de vídeo",
  "modo de escala de vídeo", "rotação de vídeo", "descodificador de hardware iPhone",
  "configurações de legendas", "legendas secundárias iOS", "configurações libass",
  "ficheiro de legendas externo", "tipo de letra de legendas",
  "configurações equalizador de áudio", "taxa de amostragem de saída de áudio",
  "canais de saída de áudio", "duração buffer IO", "modo misto áudio",
  "vídeo WiFi Drive", "widgets Evervideo",
  "backup Evervideo", "código de acesso Evervideo",
  "idioma Evervideo", "personalização Evervideo"
]
tags: ["guia", "evervideo", "configurações"]
readingTime: 16
---


O ecrã de Configurações é o centro de controlo do Evervideo. A partir daqui pode atualizar para Premium, configurar os motores de vídeo e áudio (codecs de sistema ou FFmpeg), gerir a Imagem-em-imagem, configurar legendas (primárias, secundárias, libass, ficheiros externos, tipos de letra), organizar a biblioteca de multimédia, configurar o gestor de ficheiros, ativar widgets do ecrã principal, fazer cópia de segurança dos dados e aceder à ajuda e informação legal. As secções estão agrupadas sob cabeçalhos: Compras e Atualizações, Preferências da aplicação, Ajuda, Legal e Privacidade.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecrã Principal de Configurações do Evervideo" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Atualizar para Premium

Atualize a aplicação para a versão Premium para remover todos os limites. A versão gratuita da aplicação oferece uma compra única vitalícia e duas opções de subscrição (1 mês e 1 ano) para remover todas as restrições e atualizar para Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Atualizar para Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

O **Family Sharing** está ativado para todas as compras e planos, para que possa partilhar a versão Premium com até cinco membros da família sem custo extra.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Selecionar um Plano Premium" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Partilhar Compras Entre iOS e Mac

As compras vitalícias e subscrições são partilhadas entre iOS e Mac usando o **iCloud** para sincronizar estas informações. Se tiver Premium no dispositivo iOS, certifique-se de que tem a versão mais recente instalada e que o iCloud está ativado. Inicie a aplicação no iOS e aguarde um minuto para que as informações de compra sejam enviadas para o iCloud, depois inicie a versão Mac — o Premium deve ativar automaticamente.

Também pode tocar no botão **Restaurar Compras** nas configurações da aplicação. Certifique-se de que tem ligação à internet e que está com sessão iniciada na mesma conta iCloud e App Store em ambos os dispositivos.

## Restaurar Compras num Novo Dispositivo

Para restaurar a compra num novo dispositivo, use o menu **Compras → Restaurar Compras**. Verá a lista das suas compras. Se não vir todas, confirme que o dispositivo está ligado ao mesmo Apple ID que foi usado para fazer as compras, e certifique-se de que o iCloud está ativado.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu de Compras nas Configurações do Evervideo" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Experimentar Premium Gratuitamente

Pode atualizar para a versão Premium gratuitamente, por tempo limitado, usando este menu. Basta ver um anúncio ou contar aos amigos sobre a aplicação.

## Atualização de Software

Toque em **Atualização de Software** para verificar se há uma versão mais recente do Evervideo disponível na App Store.

## O Que Há de Novo

Este menu está disponível após o lançamento de uma nova versão. Mostra um resumo das alterações e novas funcionalidades na atualização mais recente.

## Leitor

Tudo relacionado com a reprodução está aqui — áudio, vídeo, legendas, dispositivos, personalização, cache e o temporizador de suspensão.

### Geral

Estas configurações cobrem os aspetos fundamentais do leitor.

- **Modo de Repetição** — escolha como o leitor se comporta quando um vídeo termina:
  - **Repetir Tudo** — repete todos os vídeos na fila.
  - **Repetir Um** — repete apenas o vídeo atual.
  - **Parar ao Terminar** — pausa quando o vídeo atual termina.
  - **Sem Repetição** — reproduz a fila uma vez sem repetir.
- **Modo de Ordem Aleatória** — aleatorizar a ordem dos vídeos na fila (**Ativado** ou **Desativado**).
- **Guardar Posição de Reprodução** — guarda e restaura a posição de reprodução para vídeos na biblioteca.
- **Guardar Estado do Leitor** — preserva o estado do leitor antes de fechar a aplicação, para poder retomar onde ficou.

### Vídeo

Configure como o Evervideo descodifica e renderiza vídeo.

- **Descodificação Hardware H.264** — ativar / desativar a descodificação AVC acelerada por hardware. Use quando o desempenho da bateria e temperatura importam; desative para compatibilidade com perfis exóticos.
- **Descodificação Hardware H.265 (HEVC)** — o mesmo para HEVC. Os iPhones, iPads e Macs modernos descodificam HEVC de forma eficiente.
- **Formato de Pixel Preferido** — escolha o formato de pixel que o leitor apresenta ao renderizador (as predefinições são ajustadas para o dispositivo).
- **FPS Preferido** — definir um FPS de reprodução alvo. Útil para corresponder a uma taxa de atualização específica do monitor.
- **Modo de Escala de Vídeo** — Ajustar / Preencher / Esticar / Original. Determina como a imagem preenche a área de visualização.
- **Modo de Visualização de Vídeo** (iOS / iPadOS) — como o vídeo é apresentado na vista do leitor.
- **Rotação de Vídeo** — rodar manualmente a imagem 0° / 90° / 180° / 270° (útil para vídeos gravados com a orientação errada).
- **Equalizador de Vídeo** — ajustar brilho, contraste, saturação e matiz com pré-visualização em tempo real. Os presets personalizados podem ser **exportados e importados**.
- **Viewport VR** (iOS / iPadOS) — para vídeos esféricos 360°. Arrastar para olhar à volta, apertar para aproximar.
- **Imagem-em-imagem (PiP)** (iOS / iPadOS) — ativar suporte PiP; a aplicação mudará para uma janela de leitor flutuante quando enviar a aplicação para segundo plano ou tocar no botão PiP.

### Áudio

Configure a reprodução e saída de áudio.

- **Faixa de Áudio** — escolher o fluxo de áudio quando um vídeo tem vários (comentário, dobragem, etc.).
- **Equalizador de Áudio** — EQ de 10 bandas com presets e pré-amplificador. Os presets personalizados podem ser exportados / importados.
- **Taxa de Amostragem de Saída de Áudio** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Útil com DACs externos.
- **Número de Canais de Saída de Áudio** — Mono, Estéreo, 5.1, ITU BS.775-1, SDDS e mais.
- **Duração Preferida do Buffer IO de Saída de Áudio** — o valor típico para reprodução hi-res de baixa latência é cerca de 5 ms (0,005 s). Ajuste para o seu hardware.
- **Modo de Saída de Áudio** (apenas iOS) — o modo misto permite que o áudio do Evervideo se misture com outras aplicações.

### Legendas

O Evervideo inclui suporte abrangente de legendas.

- **Faixa de Legendas** — escolher entre as faixas de legendas incorporadas no ficheiro.
- **Ficheiro de Legendas Externo** — carregar um ficheiro externo `.srt`, `.vtt`, `.ass` ou `.ssa` do dispositivo ou qualquer serviço em nuvem ligado.
- **Tipo de Letra** — escolher um tipo de letra para a faixa de legendas primária.

### Dispositivos (Apenas iOS/iPadOS)

Escolha um dispositivo **AirPlay** ou **Google Chromecast** para saída de vídeo.

### Personalização

- **Estilo de Layout do Leitor** — Mínimo (predefinição para Evervideo), Inferior, Antigo, Clássico e mais.
- **Ações do Ecrã Principal** — escolher quais botões aparecem no ecrã principal do leitor.
- **Controlos do Ecrã de Bloqueio** — Avançar Tempo, Adicionar Marcador, Adicionar aos Favoritos.
- **Intervalos de Avanço Rápido** — escolher o intervalo de tempo para os botões de avanço rápido (5 s, 10 s, 15 s, 30 s, etc.).
- **Estilo de Deslocação de Capas de Álbum** — estilo de deslocação preferido para as capas.
- **Elementos Adicionais** — Informação de Formato de Áudio, Cursor de Volume.

### Carregamento de Ficheiros

Configure como os dados de vídeo são transmitidos da rede.

- **Tipo de Rede** — apenas Wi-Fi, ou Wi-Fi + Celular.
- **Tempo de Pré-carregamento** — comprimento do buffer para reprodução mais suave em redes lentas.
- **Usar URL Direto** — quando suportado, usar um URL direto para carregamento mais rápido.

### Cache de Reprodução

Os vídeos na fila do leitor são automaticamente descarregados para garantir uma reprodução suave. Pode desativar esta opção ou configurar o tamanho da cache aqui.

### Temporizador de Suspensão

Ativar um temporizador para parar automaticamente a reprodução após um período especificado. Toque no ícone de configuração para o **modo preciso** com granularidade minuto-a-minuto.

## Biblioteca de Multimédia

Gira a sincronização automática, metadados, capas de álbum, listas de reprodução, recentes e favoritos.

### Leitura de Metadados

Quando adiciona vídeos à biblioteca, o leitor de metadados analisa-os em segundo plano e organiza-os por Álbum e Género. Pode ajustar a velocidade de análise, desativar o leitor ou desencadear uma nova análise completa com **Recarregar metadados**. **Normalizar Codificação de Metadados** corrige automaticamente codificações de caracteres quebradas (comuns com ficheiros de PCs Windows).

### Sincronização Online

Adicionar automaticamente vídeos dos serviços em nuvem e servidores de multimédia ligados à biblioteca. Escolher quais pastas analisar, configurar com que frequência a aplicação deve sincronizar e iniciar / parar a sincronização manualmente. A sincronização online só funciona enquanto a aplicação está ativa — para grandes bibliotecas, use a versão de secretária e depois transfira a biblioteca sincronizada com **Backup e Restauro**.

### Sincronização Offline

Quando marcar uma pasta em nuvem como disponível offline, ela aparece em **Ficheiros → Pastas offline** e é descarregada automaticamente. Os novos ficheiros adicionados online também são descarregados. Configure o intervalo de tempo e desencadeie sincronizações manuais a partir deste ecrã.

### Personalização

- **Estilo do Ecrã da Biblioteca de Multimédia** — Menu Simples, Menu Agrupado, Menu com Separadores.
- Alternar se mostrar capas de álbum grandes nos ecrãs de detalhe.

### Capas de Álbum

- **Tipo de Rede** — Wi-Fi ou Wi-Fi + Celular.
- **Carregar Capas de Álbum para Ficheiros Online** — obter arte incorporada de ficheiros em nuvem (usa dados extra).
- **Pesquisar na Pasta** — usar imagens JPEG / PNG na mesma pasta quando um vídeo não tem capa incorporada.
- **Qualidade da Capa** — ajustar a resolução em que as capas são armazenadas em cache.
- **Mostrar na Pasta** / **Eliminar Tudo** — gerir a cache de arte.

### Listas de reprodução

Ativar a adição do mesmo vídeo a uma lista de reprodução duas vezes (desativado por predefinição).

### Recentes

Gerir a lista de vídeos reproduzidos recentemente — alterar o tamanho, eliminar ou exportar como M3U / CSV / TXT.

### Favoritos

- **Edição Simultânea** — espelhar favoritos entre a biblioteca de multimédia e a secção de ficheiros.
- **Eliminar Lista** — limpar a lista de favoritos.
- **Exportar Lista de Músicas** — exportar favoritos como M3U / CSV / TXT.

### Eliminar Biblioteca de Multimédia

Apagar a base de dados da biblioteca de multimédia. Os seus ficheiros de vídeo e áudio no armazenamento ficam intactos.

## Código de Acesso

Proteja o Evervideo com um **código PIN numérico de 4 dígitos**. Quando ativado, será solicitado a introduzir o código de acesso sempre que a aplicação for iniciada. Combine com iOS Face ID / Touch ID no dispositivo para proteção extra.

## Gestor de Ficheiros

Controla como os ficheiros são transferidos, armazenados e pré-visualizados.

- **Transferências de Ficheiros** — preferência de rede (apenas Wi-Fi ou Wi-Fi + Celular).
- **Número Máximo de Tarefas Paralelas** — definir o número de threads de descarregamento paralelo.
- **Tarefas de Transferência de Ficheiros** — ver os envios e descarregamentos atualmente ativos.
- **Transferências em Segundo Plano** — permitir descarregamentos enquanto a aplicação está em segundo plano.
- **Guardar Ficheiros Descarregados Em** — diretório de descarregamentos predefinido.
- **Pastas offline sincronizadas** — gerir pastas no modo offline.
- **Intervalo de Tempo** — com que frequência as pastas offline são verificadas para alterações.
- **Mostrar Nomes de Ficheiro Completos** — mostrar extensões no gestor de ficheiros.
- **Editar Ficheiros Online** — desativar para mudar para modo somente leitura para serviços em nuvem ligados.
- **Copiar Ficheiros ao Abrir** — como lidar com ficheiros importados de outras aplicações.
- **Miniaturas para Ficheiros** — gerir miniaturas de ficheiros geradas.
- **Eliminar Ficheiros Temporários** — limpar a pasta de cache da aplicação.

## Wi-Fi Drive

Ativar o Wi-Fi Drive para transferir ficheiros de um computador para o dispositivo usando um browser de secretária, Finder ou Explorador de Ficheiros. Instruções detalhadas estão disponíveis [aqui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widgets

Ativar widgets para que a aplicação atualize os dados dos widgets durante a reprodução. As atualizações de widgets requerem energia adicional, por isso o botão está desativado por predefinição — ative-o apenas se realmente usar widgets no Ecrã Principal ou Ecrã de Bloqueio.

Pode adicionar widgets do Evervideo premindo longamente o Ecrã Principal ou o Ecrã de Bloqueio, tocando em **+**, pesquisando **Evervideo** e escolhendo um tamanho de widget. Os widgets mostram o vídeo em reprodução e abrem diretamente o leitor de ecrã inteiro. Os widgets também funcionam no macOS no Centro de Notificações.

## Personalização

Personalize a interface de utilizador de acordo com as suas preferências.

- **Ícone da Aplicação** — ícone alternativo do Ecrã Principal (Premium).
- **Esquema de Cores** — Escuro, Claro ou Predefinido (segue a aparência do sistema).
- **Estilo de Fundo** — Capa de Álbum Desfocada ou cor sólida.
- **Aparência dos Itens na Lista** — ajuste automático da altura das linhas; mostrar miniaturas menores.
- **Limite de Carregamento de Conteúdo** — ativar / desativar paginação.
- **Estilo do Ecrã de Ficheiros** — Menu Simples ou Menu Agrupado.
- **Estilo do Ecrã da Biblioteca de Multimédia** — Menu Simples / Agrupado / com Separadores.
- **Estilo do Ecrã do Leitor** — Mínimo / Inferior / Antigo / Clássico.
- **Estilo do Menu de Contexto** — menu de sistema ou estilo de folha inferior.

## Janela

Disponível no Mac e Catalyst. Configure preferências relacionadas com a janela, como tamanho predefinido e comportamento ao iniciar.

## Ecrã

Escolha se o ecrã deve permanecer ativo enquanto utiliza a aplicação.

## Acessibilidade

Ative o **Modo de Texto** para ocultar imagens na interface de utilizador. O Modo de Texto é ativado automaticamente quando o VoiceOver está ativo.

## Idioma

Altere o idioma da aplicação e substitua o predefinido do sistema. A alteração aplica-se após fechar completamente e reabrir o Evervideo. São suportados mais de 120 idiomas.

## Backup e Restauro

Faça cópia de segurança de todos os dados da aplicação ou migre-os para outro dispositivo. Escolha o que incluir:

- **Base de Dados** — as entradas da biblioteca de multimédia, listas de reprodução, classificações, favoritos, histórico de visualização. Os ficheiros offline não são incluídos para manter o tamanho do ficheiro gerível.
- **Capas de Álbum** — a sua arte em cache.
- **Configurações** — as suas configurações da aplicação.

Toque em **Backup dos Dados da Aplicação** para iniciar a cópia de segurança. Para restaurar num novo dispositivo, mova o ficheiro de cópia de segurança via iCloud Drive, AirDrop ou qualquer serviço em nuvem ligado e abra-o no novo dispositivo.

## Ajuda

Aceder ao guia da aplicação para obter assistência e orientação sobre como usar a aplicação eficazmente.

## Perguntas Frequentes

Encontre respostas a perguntas comuns na secção FAQ.

## Enviar Feedback

Envie o seu feedback para a nossa equipa de suporte diretamente da aplicação, com informações de diagnóstico anexadas automaticamente.

## Partilhar Esta Aplicação

Partilhe o Evervideo com os seus amigos para espalhar a palavra.

## Descobrir Mais Aplicações

Explore outras aplicações da Everappz.

## Termos e Condições

Leia os termos e condições antes de usar a aplicação.

## Política de Privacidade

Leia a política de privacidade para compreender as nossas práticas de tratamento de dados.

## Análise e Recolha de Dados

Verifique quais os serviços ativados para análise e recolha de dados e desative os que não pretende.

## Avisos Legais

Informação sobre cada biblioteca usada na aplicação junto com o número de versão da aplicação e informação de compilação.
