---
title: "Como obter metadados, ícones e capturas de tela da App Store grátis"
date: 2026-06-13
description: "Guia passo a passo para obter metadados, ícone, capturas de tela e detalhes localizados da App Store de qualquer app iOS usando o AppLookup.pro, uma ferramenta de navegador grátis baseada na API oficial iTunes Search."
keywords: [
  "metadados app store", "obter dados app store", "baixar ícone app store",
  "baixar capturas app store", "ferramenta consulta app store", "itunes search api",
  "extrator de metadados de app", "metadados de app iOS", "ferramenta grátis api app store",
  "baixar ícone de app alta resolução", "pesquisa de concorrentes app store",
  "dados localizados app store", "consulta app store por país", "ferramenta aso grátis"
]
tags: [
  "Metadados App Store", "Consulta de App", "API iTunes Search",
  "Download de Ícones de App", "Capturas de App", "Pesquisa ASO"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

## Obtenha dados da App Store em segundos

**Versão curta:** o [AppLookup.pro](https://applookup.pro) é uma ferramenta grátis que extrai dados públicos de qualquer app iOS, iPadOS, macOS ou tvOS. Você obtém o título, a descrição, as novidades, a versão, o preço, as avaliações, o ícone do app, as capturas de tela, os dispositivos compatíveis e a resposta bruta da API do iTunes. Cada campo tem um botão de copiar com um toque. Abra o site, cole um link da App Store ou digite o nome do app e você terá os dados.

Use para:

- **Pesquisa ASO.** Veja como os top apps escrevem títulos, subtítulos, descrições e palavras chave.
- **Acompanhamento de concorrentes.** Verifique atualizações de versão, avaliações e preços em diferentes mercados.
- **Download de assets.** Salve o ícone oficial e as capturas de tela em tamanho real em um único ZIP.
- **Verificações de localização.** Compare descrição, novidades e capturas em mais de 40 países da App Store.
- **Testes de API.** Copie o JSON bruto da iTunes Search API direto para o seu código ou para o Postman.

## O que é o AppLookup.pro?

O [AppLookup.pro](https://applookup.pro) é uma ferramenta grátis de consulta à App Store que funciona no navegador. Ela roda inteiramente no seu dispositivo. Cada resultado vem direto da [API oficial iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) da Apple. Sem scraping. Sem cadastro. Sem rastreamento.

### O que você obtém

- **Busca por nome do app ou URL da App Store.** O autocompletar mostra resultados ao vivo enquanto você digita.
- **Mais de 40 lojas por país.** Alterne entre US, UK, JP, DE, FR, BR e outros.
- **Metadados completos.** Título, subtítulo, desenvolvedor, bundle ID, versão, preço, tamanho do arquivo, avaliações, data de lançamento, classificação de conteúdo, idiomas e dispositivos compatíveis.
- **Assets em alta resolução.** Ícones de app e capturas de tela para iPhone, iPad, macOS e Apple TV.
- **Download em ZIP em massa.** Pegue todos os ícones ou todas as capturas em um único arquivo.
- **JSON bruto da iTunes API.** A resposta exata da Apple, pronta para copiar.
- **Botões de copiar em cada campo.** Um toque coloca o valor na sua área de transferência.

## Como usar o AppLookup.pro passo a passo

### Passo 1. Digite o nome do app ou cole uma URL da App Store

Abra o [applookup.pro](https://applookup.pro) e comece a digitar o nome do app. O autocompletar mostra resultados ao vivo da App Store enquanto você digita.

Você também pode colar um link direto da App Store como `https://apps.apple.com/us/app/instagram/id389801252` ou apenas o ID do app. A ferramenta extrai o ID para você. Ela também lida com URLs de redirecionamento do Google.

![Digite um nome de app ou URL da App Store no AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Passo 2. Obtenha as informações do app e baixe o ícone

Clique em **Lookup** ou pressione Enter. A ferramenta chama a iTunes Search API oficial e mostra o ícone do app, o nome do desenvolvedor, a avaliação, a versão e o preço em menos de um segundo.

Role até a seção **App Icon**. Cada tamanho de ícone que a Apple retorna aparece como um cartão. Cada cartão tem:

- **Direct Link.** Abre a imagem em tamanho real em uma nova aba.
- **Download.** Salva o arquivo no seu computador.

Use **Download All Icons (ZIP)** para pegar todos os tamanhos de ícone em um único arquivo. O mesmo vale para as capturas de tela: cada seção de plataforma tem seu próprio botão **Download All (ZIP)**.

![Baixe ícones e capturas de tela de apps a partir do AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Passo 3. Leia os detalhes do app e copie qualquer campo

Role até **App Details**. Você verá bundle ID, versão, preço, tamanho do arquivo, SO mínimo, data de lançamento, data da última atualização, classificação de conteúdo, gêneros, IDs de gêneros, idiomas, vendedor, artist ID e track ID.

Toque no botão **Copy** em qualquer cartão. O valor vai para sua área de transferência e o botão mostra um sinal verde de 'Copied'.

O mesmo funciona em **Description**, **What's New** e **Supported Devices**. Essas seções são roláveis para que você possa ler o texto inteiro sem perder o lugar, e o botão Copy coloca o campo inteiro na sua área de transferência.

![Veja todos os detalhes da App Store e copie qualquer campo com um toque](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Passo 4. Veja a resposta bruta da API da App Store

Precisa do JSON exato que a Apple retorna? Role até **Raw API Response**. O payload completo da iTunes Search API aparece em um visualizador rolável com um botão **Copy** no topo. Um toque copia todo o objeto JSON.

A **iTunes Lookup URL** é mostrada logo acima. Cole no Postman, no curl ou no seu navegador para repetir a mesma requisição.

![Veja e copie a resposta JSON bruta da iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Passo 5. Mude o país para ver a versão localizada

Os metadados da App Store mudam por país. O mesmo app costuma ter título, subtítulo, descrição, capturas e preço diferentes em cada mercado.

Escolha um país no menu suspenso no topo. A URL na caixa de entrada é atualizada automaticamente. Clique em **Lookup** de novo para buscar o app nesse mercado.

É a forma mais rápida de verificar como um concorrente apresenta o app no Japão, na Alemanha, no Brasil ou em qualquer um dos mais de 40 países suportados.

![Alterne entre lojas por país para ver metadados localizados da App Store](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Passo 6. Copie os metadados localizados

Quando o resultado do país carrega, cada campo funciona da mesma forma. Toque em **Copy** na descrição, nas novidades, no nome do app, no desenvolvedor, no bundle ID ou em qualquer cartão de detalhe para capturar o texto localizado.

Isso facilita montar planilhas de comparação lado a lado ou alimentar textos localizados em uma revisão de tradução.

![Copie descrição e metadados localizados da App Store com um toque](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Quem usa o AppLookup.pro

- **Desenvolvedores indie** que fazem pesquisa de ASO antes de um lançamento.
- **Times de ASO e marketing** que acompanham atualizações e preços de concorrentes.
- **Designers** que pegam o ícone oficial em alta resolução e capturas para press kits e estudos de caso.
- **Times de localização** que auditam quais mercados estão cobertos e onde ainda sai o texto padrão em inglês.
- **Engenheiros de backend e QA** que testam integrações com a iTunes Search API sem escrever um scraper.
- **Escritores e blogueiros** que precisam do ícone oficial do app e de algumas capturas para um post.

## Privacidade e aviso legal

O AppLookup.pro roda no seu navegador. Não há login. Não há rastreamento. Não há registro no servidor dos apps que você consulta. As requisições vão direto do seu navegador para a [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) da Apple.

Esta ferramenta é destinada **apenas para fins educacionais e de pesquisa**. Todos os dados são obtidos da API pública oficial da Apple e continuam sendo propriedade da Apple Inc. e das editoras dos apps listados. O uso da ferramenta está sujeito aos [Termos e Condições dos Serviços de Mídia Apple](https://www.apple.com/legal/internet-services/terms/site.html). Respeite os limites de taxa da Apple e não redistribua assets protegidos por direitos autorais.

## Experimente agora

Você não precisa de uma chave de API, conta de desenvolvedor ou plano pago para inspecionar dados da App Store. Abra o [applookup.pro](https://applookup.pro), cole qualquer URL da App Store e você terá os metadados, ícones e JSON bruto em segundos.

## Código aberto

O AppLookup.pro é de código aberto. Relatórios de bugs, novos países e pull requests são bem-vindos.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro no GitHub" icon="github" tag="código aberto" >}}
{{< /cards >}}

---

## Perguntas frequentes

{{% details title="O AppLookup.pro é mesmo grátis?" closed="true" %}}
Sim. O AppLookup.pro é 100 por cento grátis e de código aberto. Roda no seu navegador. Não há cadastro, não há nível pago e não há limite de uso além dos próprios limites da iTunes Search API da Apple.
{{% /details %}}

{{% details title="De onde vêm os dados?" closed="true" %}}
Cada resultado é obtido em tempo real da [API oficial iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) da Apple. A ferramenta não faz scraping das páginas da App Store e não armazena respostas em nenhum servidor.
{{% /details %}}

{{% details title="Posso baixar o ícone do app em alta resolução?" closed="true" %}}
Sim. A seção **App Icon** mostra todas as URLs de ícone que a Apple retorna. Cada cartão tem um Direct Link e um botão Download, e um botão Download All Icons ZIP empacota todos em um único arquivo.
{{% /details %}}

{{% details title="Posso baixar todas as capturas de tela da App Store de uma só vez?" closed="true" %}}
Sim. Cada seção de capturas de tela (iPhone, iPad, macOS e Apple TV) tem um botão **Download All (ZIP)** que reúne todas as capturas em resolução total.
{{% /details %}}

{{% details title="Como vejo como um app aparece em outro país?" closed="true" %}}
Escolha um país no menu suspenso no topo da página. Mais de 40 lojas são suportadas. Clique em **Lookup** de novo e a ferramenta busca o app para aquele país, mostrando título, descrição, capturas, novidades e preço localizados.
{{% /details %}}

{{% details title="Posso copiar campos individuais como bundle ID ou data de lançamento?" closed="true" %}}
Sim. Cada campo de texto no resultado tem seu próprio botão Copy: nome do app, desenvolvedor, descrição, novidades, bundle ID, versão, preço, tamanho do arquivo, SO mínimo, data de lançamento, classificação de conteúdo, idiomas, dispositivos compatíveis e JSON bruto.
{{% /details %}}

{{% details title="O AppLookup.pro funciona para qualquer app iOS?" closed="true" %}}
Funciona para qualquer app listado publicamente em pelo menos um país da App Store e retornado pela iTunes Search API. Apps não listados, removidos ou distribuídos em modo enterprise não aparecerão.
{{% /details %}}

{{% details title="Ele suporta apps para macOS e Apple TV?" closed="true" %}}
Sim. Se o app tiver capturas de macOS ou Apple TV na resposta da iTunes Search API, o AppLookup.pro as mostra em um painel rolável próprio com botões de download.
{{% /details %}}

{{% details title="Posso usar o JSON bruto no meu próprio código?" closed="true" %}}
Sim. A seção Raw API Response mostra o JSON exato que a Apple retorna. Copie para o Postman, para um teste unitário ou para um pipeline de backend. Respeite os termos da API da Apple e limites de taxa razoáveis.
{{% /details %}}

{{% details title="É seguro colar URLs da App Store na ferramenta?" closed="true" %}}
Sim. A URL é analisada no seu navegador. A única chamada de rede de saída é a consulta para a iTunes Search API da Apple.
{{% /details %}}

{{% details title="Qual é a diferença entre o AppLookup.pro e o AppKeywords.pro?" closed="true" %}}
O [AppLookup.pro](https://applookup.pro) serve para ler metadados da App Store de qualquer app publicado: pesquisa de concorrentes, download de assets, verificações de localização. O [AppKeywords.pro](https://appkeywords.pro) serve para escrever metadados da App Store para o seu próprio app: otimização de título, subtítulo e palavras chave com suporte ao Fastlane. As duas ferramentas funcionam muito bem juntas.
{{% /details %}}
