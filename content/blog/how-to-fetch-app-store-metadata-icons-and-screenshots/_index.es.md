---
title: "Cómo obtener metadatos, iconos y capturas de pantalla de la App Store gratis"
date: 2026-06-13
description: "Guía paso a paso para obtener los metadatos, el icono, las capturas de pantalla y los detalles localizados de la App Store de cualquier app de iOS usando AppLookup.pro, una herramienta de navegador gratuita basada en la API oficial de búsqueda de iTunes."
keywords: [
  "metadatos app store", "obtener datos app store", "descargar icono app store",
  "descargar capturas app store", "herramienta consulta app store", "itunes search api",
  "extractor de metadatos de apps", "metadatos apps iOS", "herramienta gratis api app store",
  "descargar icono de app alta resolución", "investigación de competencia app store",
  "datos localizados app store", "consulta app store por país", "herramienta aso gratis"
]
tags: [
  "Metadatos App Store", "Consulta de Apps", "API de búsqueda de iTunes",
  "Descarga de iconos de apps", "Capturas de pantalla de apps", "Investigación ASO"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Obtén datos de la App Store en segundos

**Versión corta:** [AppLookup.pro](https://applookup.pro) es una herramienta gratuita que extrae datos públicos de cualquier app para iOS, iPadOS, macOS o tvOS. Obtienes el título, la descripción, las novedades, la versión, el precio, las valoraciones, el icono de la app, las capturas de pantalla, los dispositivos compatibles y la respuesta sin procesar de la API de iTunes. Cada campo tiene un botón de copiar con un solo toque. Abre el sitio, pega un enlace de la App Store o escribe el nombre de la app, y ya tienes los datos.

Úsala para:

- **Investigación ASO.** Mira cómo las apps líderes escriben sus títulos, subtítulos, descripciones y palabras clave.
- **Seguimiento de competidores.** Consulta actualizaciones de versión, valoraciones y precios en distintos mercados.
- **Descarga de recursos.** Guarda el icono oficial de la app y las capturas de pantalla a tamaño completo en un solo ZIP.
- **Comprobaciones de localización.** Compara descripción, novedades y capturas de pantalla en más de 40 países de la App Store.
- **Pruebas de API.** Copia el JSON sin procesar de la API de búsqueda de iTunes directamente a tu código o a Postman.

## ¿Qué es AppLookup.pro?

[AppLookup.pro](https://applookup.pro) es una herramienta gratuita de consulta de la App Store basada en el navegador. Funciona por completo en tu dispositivo. Cada resultado viene directamente de la [API oficial de búsqueda de iTunes](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) de Apple. Sin scraping. Sin registro. Sin seguimiento.

### Lo que obtienes

- **Búsqueda por nombre de app o URL de la App Store.** El autocompletado muestra resultados en vivo mientras escribes.
- **Más de 40 tiendas por país.** Cambia entre US, UK, JP, DE, FR, BR y más.
- **Metadatos completos.** Título, subtítulo, desarrollador, bundle ID, versión, precio, tamaño del archivo, valoraciones, fecha de lanzamiento, clasificación de contenido, idiomas y dispositivos compatibles.
- **Recursos en alta resolución.** Iconos de apps y capturas de pantalla para iPhone, iPad, macOS y Apple TV.
- **Descarga masiva en ZIP.** Consigue todos los iconos o todas las capturas en un único archivo.
- **JSON sin procesar de la API de iTunes.** La respuesta exacta de Apple, lista para copiar.
- **Botones de copiar en cada campo.** Un toque y el valor está en tu portapapeles.

## Cómo usar AppLookup.pro paso a paso

### Paso 1. Introduce el nombre de la app o pega una URL de la App Store

Abre [applookup.pro](https://applookup.pro) y empieza a escribir el nombre de la app. El autocompletado muestra resultados de la App Store en vivo mientras escribes.

También puedes pegar un enlace directo de la App Store como `https://apps.apple.com/us/app/instagram/id389801252` o solo el ID de la app. La herramienta extrae el ID por ti. También gestiona URLs de redirección de Google.

![Introduce el nombre de una app o una URL de la App Store en AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Paso 2. Obtén la información de la app y descarga el icono

Haz clic en **Lookup** o pulsa Enter. La herramienta llama a la API oficial de búsqueda de iTunes y muestra el icono de la app, el nombre del desarrollador, la valoración, la versión y el precio en menos de un segundo.

Desplázate hasta la sección **App Icon**. Cada tamaño de icono que devuelve Apple aparece como una tarjeta. Cada tarjeta tiene:

- **Direct Link.** Abre la imagen a tamaño completo en una pestaña nueva.
- **Download.** Guarda el archivo en tu equipo.

Usa **Download All Icons (ZIP)** para obtener todos los tamaños de icono en un solo archivo. Lo mismo ocurre con las capturas de pantalla: cada sección de plataforma tiene su propio botón **Download All (ZIP)**.

![Descarga iconos y capturas de pantalla de apps desde AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Paso 3. Lee los detalles de la app y copia cualquier campo

Desplázate hasta **App Details**. Verás bundle ID, versión, precio, tamaño del archivo, SO mínimo, fecha de lanzamiento, fecha de la última actualización, clasificación de contenido, géneros, IDs de géneros, idiomas, vendedor, ID de artista e ID de track.

Pulsa el botón **Copy** en cualquier tarjeta. El valor pasa a tu portapapeles y el botón muestra una marca verde de 'Copied'.

Lo mismo funciona en **Description**, **What's New** y **Supported Devices**. Estas secciones son desplazables para que puedas leer el texto completo sin perder el sitio, y el botón Copy pone todo el campo en tu portapapeles.

![Visualiza todos los detalles de la App Store y copia cualquier campo con un toque](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Paso 4. Visualiza la respuesta sin procesar de la API de la App Store

¿Necesitas el JSON exacto que devuelve Apple? Desplázate hasta **Raw API Response**. El payload completo de la API de búsqueda de iTunes se muestra en un visor desplazable con un botón **Copy** en la parte superior. Un toque copia todo el objeto JSON.

La **iTunes Lookup URL** se muestra justo encima. Pégala en Postman, curl o tu navegador para reproducir la misma solicitud.

![Visualiza y copia la respuesta JSON sin procesar de la API de búsqueda de iTunes](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Paso 5. Cambia el país para ver la versión localizada

Los metadatos de la App Store cambian según el país. La misma app suele tener un título, subtítulo, descripción, capturas de pantalla y precio diferentes en cada mercado.

Elige un país en el desplegable de la parte superior. La URL en el cuadro de entrada se actualiza automáticamente. Haz clic en **Lookup** de nuevo para volver a consultar la app en ese mercado.

Es la forma más rápida de comprobar cómo un competidor presenta su app en Japón, Alemania, Brasil o cualquiera de los más de 40 países compatibles.

![Cambia entre tiendas de países para ver los metadatos localizados de la App Store](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Paso 6. Copia los metadatos localizados

Una vez que se cargue el resultado del país, cada campo funciona igual. Pulsa **Copy** en la descripción, las novedades, el nombre de la app, el desarrollador, el bundle ID o cualquier tarjeta de detalle para capturar el texto localizado.

Esto facilita crear hojas de cálculo de comparación lado a lado o alimentar copys localizados en una revisión de traducción.

![Copia la descripción y los metadatos localizados de la App Store con un toque](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Quién usa AppLookup.pro

- **Desarrolladores indie** que hacen investigación ASO antes de un lanzamiento.
- **Equipos de ASO y marketing** que siguen actualizaciones y precios de la competencia.
- **Diseñadores** que necesitan el icono oficial en alta resolución y capturas de pantalla para kits de prensa y casos de estudio.
- **Equipos de localización** que auditan qué mercados están cubiertos y dónde sigue saliendo el copy en inglés por defecto.
- **Ingenieros de backend y QA** que prueban integraciones con la API de búsqueda de iTunes sin escribir un scraper.
- **Redactores y bloggers** que necesitan el icono oficial de la app y algunas capturas para un post.

## Privacidad y descargo de responsabilidad

AppLookup.pro se ejecuta en tu navegador. No hay inicio de sesión. No hay seguimiento. No hay registros en el servidor de las apps que consultas. Las solicitudes van directamente desde tu navegador a la [API de búsqueda de iTunes](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) de Apple.

Esta herramienta es **solo para fines educativos y de investigación**. Todos los datos se obtienen de la API pública oficial de Apple y siguen siendo propiedad de Apple Inc. y de los editores de las apps listadas. El uso de la herramienta está sujeto a los [Términos y condiciones de los servicios multimedia de Apple](https://www.apple.com/legal/internet-services/terms/site.html). Respeta los límites de tasa de Apple y no redistribuyas activos protegidos por derechos de autor.

## Pruébala ahora

No necesitas una clave de API, una cuenta de desarrollador ni un plan de pago para inspeccionar los datos de la App Store. Abre [applookup.pro](https://applookup.pro), pega cualquier URL de la App Store y tendrás los metadatos, iconos y JSON sin procesar en segundos.

## Código abierto

AppLookup.pro es de código abierto. Los informes de errores, los nuevos países y los pull requests son bienvenidos.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro en GitHub" icon="github" tag="código abierto" >}}
{{< /cards >}}

---

## Preguntas frecuentes

{{% details title="¿AppLookup.pro es realmente gratis?" closed="true" %}}
Sí. AppLookup.pro es 100 por cien gratis y de código abierto. Funciona en tu navegador. No hay registro, ni nivel de pago, ni límite de uso más allá de los propios límites de la API de búsqueda de iTunes de Apple.
{{% /details %}}

{{% details title="¿De dónde vienen los datos?" closed="true" %}}
Cada resultado se obtiene en tiempo real desde la [API oficial de búsqueda de iTunes](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) de Apple. La herramienta no hace scraping de las páginas de la App Store y no guarda respuestas en ningún servidor.
{{% /details %}}

{{% details title="¿Puedo descargar el icono de la app en alta resolución?" closed="true" %}}
Sí. La sección **App Icon** muestra todas las URLs de icono que devuelve Apple. Cada tarjeta tiene un Direct Link y un botón Download, y un botón Download All Icons ZIP los empaqueta todos en un único archivo.
{{% /details %}}

{{% details title="¿Puedo descargar todas las capturas de la App Store de una vez?" closed="true" %}}
Sí. Cada sección de capturas de pantalla (iPhone, iPad, macOS y Apple TV) tiene un botón **Download All (ZIP)** que reúne todas las capturas a resolución completa.
{{% /details %}}

{{% details title="¿Cómo veo cómo se muestra una app en otro país?" closed="true" %}}
Elige un país en el desplegable de la parte superior de la página. Hay más de 40 tiendas compatibles. Haz clic en **Lookup** de nuevo y la herramienta vuelve a consultar la app para ese país, mostrando el título, descripción, capturas, novedades y precio localizados.
{{% /details %}}

{{% details title="¿Puedo copiar campos individuales como el bundle ID o la fecha de lanzamiento?" closed="true" %}}
Sí. Cada campo de texto en el resultado tiene su propio botón Copy: nombre de la app, desarrollador, descripción, novedades, bundle ID, versión, precio, tamaño del archivo, SO mínimo, fecha de lanzamiento, clasificación de contenido, idiomas, dispositivos compatibles y JSON sin procesar.
{{% /details %}}

{{% details title="¿AppLookup.pro funciona con cualquier app de iOS?" closed="true" %}}
Funciona con cualquier app que esté listada públicamente en al menos un país de la App Store y que devuelva la API de búsqueda de iTunes. Las apps no listadas, retiradas o de distribución empresarial no aparecerán.
{{% /details %}}

{{% details title="¿Admite apps de macOS y Apple TV?" closed="true" %}}
Sí. Si la app tiene capturas de pantalla de macOS o Apple TV en la respuesta de la API de búsqueda de iTunes, AppLookup.pro las muestra en su propio panel desplazable con botones de descarga.
{{% /details %}}

{{% details title="¿Puedo usar el JSON sin procesar en mi propio código?" closed="true" %}}
Sí. La sección Raw API Response muestra el JSON exacto que devuelve Apple. Cópialo en Postman, en un test unitario o en un pipeline de backend. Respeta los términos de la API de Apple y unos límites de tasa razonables.
{{% /details %}}

{{% details title="¿Es seguro pegar URLs de la App Store en la herramienta?" closed="true" %}}
Sí. La URL se analiza en tu navegador. La única llamada de red saliente es la consulta a la API de búsqueda de iTunes de Apple.
{{% /details %}}

{{% details title="¿Cuál es la diferencia entre AppLookup.pro y AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) sirve para leer los metadatos de la App Store de cualquier app publicada: investigación de competencia, descarga de recursos, comprobaciones de localización. [AppKeywords.pro](https://appkeywords.pro) sirve para escribir los metadatos de la App Store de tu propia app: optimización de título, subtítulo y palabras clave con soporte para Fastlane. Las dos herramientas funcionan muy bien juntas.
{{% /details %}}
