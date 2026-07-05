---
title: "Evermusic 8.7: verdadera reproducción sin cortes, efectos de audio, normalización de volumen, ecualizador rediseñado"
date: 2026-07-05
description: "Evermusic 8.7 para iPhone, iPad y Mac añade verdadera reproducción sin cortes, cinco efectos de audio de estudio (reverberación, delay, distorsión, compresor, crossfeed), normalización de volumen EBU R128, un ecualizador de 10 bandas rediseñado con importación/exportación de preajustes, un motor de streaming AVAudioEngine reconstruido con compatibilidad con FLAC y Ogg Vorbis, y un CarPlay y Reproduciendo más rápidos y precisos."
keywords: ["Evermusic 8.7", "actualización Evermusic", "verdadera reproducción sin cortes iPhone", "reproductor de música sin cortes iOS", "reproducción sin cortes CarPlay", "efectos de audio reproductor de música iPhone", "reverberación delay distorsión compresor crossfeed iOS", "crossfeed auriculares iOS", "normalización de volumen iPhone", "normalización de sonoridad reproductor de música", "normalización EBU R128 iOS", "alternativa a ReplayGain iPhone", "ecualizador de 10 bandas iPhone", "ecualizador gráfico app iOS", "importar exportar preajustes ecualizador", "reproductor FLAC iPhone", "reproductor Ogg Vorbis iOS", "reproductor de música sin pérdida iPhone 2026", "AVAudioEngine reproductor de música", "CarPlay reproductor de música iPhone", "precisión Reproduciendo pantalla de bloqueo", "reproductor de música en la nube iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Reproducción sin cortes", "Efectos de audio", "Reverberación", "Delay", "Distorsión", "Compresor", "Crossfeed", "Normalización de volumen", "EBU R128", "Ecualizador", "FLAC", "Ogg Vorbis", "CarPlay", "Reproduciendo", "Liquid Glass", "Novedades"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**En resumen:** [Evermusic 8.7](/products/evermusic) es una versión centrada en la calidad de sonido para iPhone, iPad y Mac. Incorpora **verdadera reproducción sin cortes** (sin pausas, clics ni chasquidos entre pistas), un conjunto completo de **efectos de audio de estudio** (reverberación, delay, distorsión, compresor y crossfeed) y **normalización de volumen EBU R128** que mantiene la sonoridad constante de una canción a otra sin etiquetas de ReplayGain. El **ecualizador de 10 bandas** se ha rediseñado con nuevos controles deslizantes, cambio de preajustes más rápido, preajustes personalizados que puedes importar y exportar, y un mejor diseño en horizontal y en iPad. Internamente, un **motor de streaming AVAudioEngine reconstruido** mejora la fiabilidad y la compatibilidad de formatos, incluidos **FLAC** y **Ogg Vorbis**. **CarPlay** y **Reproduciendo** son más rápidos y precisos en la pantalla de bloqueo, en el coche y desde los mandos de los auriculares.

---

## ¡Hola a todos!

Evermusic 8.7 ya está disponible para descargar. Esta actualización trata por completo sobre cómo *suena* tu música. Reconstruimos el motor de reproducción para lograr una verdadera reproducción sin cortes, añadimos un conjunto de efectos de audio de calidad de estudio, introdujimos la normalización de sonoridad y rediseñamos el ecualizador desde los controles deslizantes hacia arriba. Todo está envuelto en el nuevo diseño **Liquid Glass** de Apple.

[Descarga Evermusic 8.7 desde el App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) o actualiza desde tu versión existente. Evermusic es una descarga gratuita con mejoras opcionales dentro de la app.

## Verdadera reproducción sin cortes

La reproducción sin cortes significa que el silencio entre dos pistas ha desaparecido. Sin pausa, sin clic, sin chasquido: la canción actual fluye directamente hacia la siguiente. Importa sobre todo en la música diseñada para escucharse como un todo: **grabaciones en directo, sesiones de DJ, obras clásicas y álbumes conceptuales** en los que una pista se funde directamente con otra.

Esto es lo que cambió a nivel técnico. El motor de audio de Evermusic mantiene dos pistas en juego a la vez: la que estás oyendo y la siguiente en la cola. Mientras suena la pista actual, la siguiente ya se está **obteniendo, decodificando y almacenando por adelantado** en segundo plano. Cuando la pista actual llega a su final, el motor hace el relevo a la siguiente pista **dentro del reproductor, no dentro del flujo de audio**. El bucle de renderizado de la salida sigue extrayendo muestras de audio de un búfer circular continuo sin detenerse jamás, de modo que el oyente nunca oye un límite. El cambio ocurre entre muestras, y por eso exactamente no hay ningún hueco audible.

Esto funciona igual tanto si el archivo está en tu dispositivo, en la nube o en un servidor multimedia: el almacenamiento por adelantado simplemente empieza un poco antes para las fuentes remotas.

## Efectos de audio de estudio

Evermusic 8.7 añade cinco efectos de audio en tiempo real que puedes apilar sobre tu música. Cada uno se ejecuta como un nodo de procesamiento de audio nativo en el motor de reproducción, de modo que se aplica a todo lo que reproduces (archivos locales, transmisiones en la nube y radio por internet por igual) sin volver a codificar.

Cada efecto viene con una **biblioteca cuidada de preajustes** para conseguir un gran sonido con un toque, y Evermusic **recuerda tus ajustes exactos** entre sesiones. Ajusta cualquier control y el efecto cambia a un estado **Manual**, así siempre sabes cuándo te has alejado de un preajuste.

### Reverberación

Añade una sensación de espacio, desde una sala ceñida hasta una catedral. Construida sobre el `AVAudioUnitReverb` de Apple, ofrece **13 preajustes de espacio** (Sala pequeña, Salón mediano, Placa, Catedral y más) más un control de **mezcla húmedo/seco** de 0 a 100 %, para que decidas cuánto espacio añadir.

### Delay (eco)

Un eco clásico con **10 preajustes**: Slapback, Eco de cinta, Dub, Ambiental y otros. Puedes ajustar el **tiempo de delay** (hasta 2 segundos), la **realimentación** (cuántas repeticiones), un **corte de paso bajo** para calentar las repeticiones y la **mezcla húmedo/seco**.

### Distorsión

Desde una aspereza sutil hasta la destrucción lo-fi total, impulsada por `AVAudioUnitDistortion` con **22 preajustes de carácter** (Bit Brush, Cellphone Concert, Radio Tower y más), un control de impulso de **preganancia** y una mezcla húmedo/seco para que reintegres el efecto en la señal limpia.

### Compresor

Un procesador de dinámica (el `AUDynamicsProcessor` de Apple) que iguala los pasajes fuertes y suaves. Expone el conjunto completo de controles profesionales (**umbral, relación/margen, ataque, liberación, expansión y ganancia de compensación**) con **10 preajustes** afinados para situaciones reales: Voz / Podcast, Madrugada, Diálogo de película, Igualación de streaming y Sonoridad máxima, entre ellos.

### Crossfeed

El crossfeed hace que la escucha con auriculares suene más natural mezclando un poco del canal izquierdo en el derecho y viceversa, tal como tus oídos oyen altavoces reales. Está construido sobre el conocido algoritmo **Bauer stereophonic-to-binaural (bs2b)**, con control sobre el **nivel de crossfeed** y la **frecuencia de corte**, y **6 preajustes** que incluyen las configuraciones favoritas de los audiófilos *Chu Moy* y *Jan Meier*. Es especialmente bueno en mezclas estéreo antiguas de los años 60 y 70 con panoramización extrema.

## Normalización de volumen

¿Alguna vez has creado una lista de reproducción donde una pista retumba y la siguiente es un susurro? La normalización de volumen lo soluciona. Evermusic 8.7 usa la **medición de sonoridad EBU R128** (el mismo estándar ITU-R BS.1770 que se emplea en la radiodifusión y en los servicios de streaming) para medir la sonoridad percibida real de cada pista y dirigirla suavemente hacia un objetivo constante.

A diferencia de ReplayGain, **no** requiere ninguna etiqueta en tus archivos y **no** modifica tu audio. Funciona en tiempo real sobre todo lo que reproduces, incluidas las transmisiones en la nube y la radio en directo, y se restablece de forma limpia cuando avanzas o cambias de pista.

Cuatro preajustes cubren los casos comunes:

- **Ligero**: nivelación suave (objetivo −20 LUFS).
- **Estándar**: el valor predeterminado, sonoridad al estilo del streaming (objetivo −16 LUFS, hasta +12 dB de aumento para pistas silenciosas).
- **Fuerte**: igualación agresiva para bibliotecas muy heterogéneas (objetivo −14 LUFS).
- **Noche**: más silencioso y constante para escucha nocturna a bajo volumen (objetivo −23 LUFS).

Ya no necesitas tocar el volumen entre canciones.

## Ecualizador rediseñado

El **ecualizador gráfico de 10 bandas** de Evermusic recibió un rediseño completo. Las bandas cubren de **32 Hz a 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), cada una ajustable de **−12 dB a +12 dB** en pasos finos de 0,1 dB, con un **preamplificador** de −24 dB a +24 dB para evitar el recorte al amplificar.

Lo nuevo en 8.7:

- **Nuevos controles deslizantes**: controles precisos y receptivos que adoptan el aspecto del control deslizante del sistema nativo de iOS 26 y el material **Liquid Glass**.
- **Cambio de preajustes más rápido y fluido**: salta entre preajustes al instante, con una barra horizontal de preajustes rediseñada en vertical y una columna vertical de preajustes en horizontal.
- **Mejor diseño en horizontal y en iPad**: los controles deslizantes y el selector de preajustes se reorganizan para aprovechar el ancho adicional en lugar de apretujarse en una columna del tamaño de un teléfono.
- **Preajustes personalizados**: crea y guarda tus propias curvas, reordénalas e **importa y exporta** preajustes como archivos `.eqp` para moverlos entre dispositivos o compartirlos.

El ecualizador se ejecuta de forma nativa en el motor (`AVAudioUnitEQ`), así que se aplica a cualquier fuente, y también funciona por AirPlay, Chromecast y CarPlay donde sea compatible.

## Motor de reproducción reconstruido

Internamente, Evermusic 8.7 se ejecuta sobre un **motor de streaming reconstruido** basado en el `AVAudioEngine` de Apple con una canalización de renderizado personalizada. Esto es lo que hace posibles el relevo sin cortes, la cadena de efectos y el ecualizador, y también hace que la reproducción cotidiana sea más fiable.

- **Mejor compatibilidad de formatos**: incluidos **FLAC** (mediante Core Audio) y **Ogg Vorbis** (mediante `libvorbisfile`), junto con MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF y más.
- **Almacenamiento en búfer más inteligente**: un búfer previo adaptativo escala con tu conexión, con un búfer circular continuo que alimenta la salida para que los breves cortes de red no se conviertan en interrupciones.
- **Recuperación automática**: una máquina de estados de rebúfer y una lógica de reintentos con espera reanudan la reproducción de forma limpia tras un momento de señal débil en lugar de detener la pista.
- **Menos interrupciones**: el mismo motor impulsa los archivos locales, las transmisiones en la nube, los servidores multimedia y la radio por internet, así que el comportamiento es coherente en todas partes.

## Reproduciendo y CarPlay

Las pantallas que realmente miras mientras escuchas (la **pantalla de bloqueo**, **CarPlay** y los botones de mando de tu coche o auriculares) son más precisas y rápidas en 8.7.

- **Información de Reproduciendo más precisa.** Evermusic captura el estado del reproductor bajo un bloqueo antes de publicarlo, de modo que el título, el tiempo transcurrido, la duración y el estado de reproducción/pausa nunca pueden contradecirse entre sí en la pantalla de bloqueo o en el coche. Los estados de almacenamiento en búfer y de carga ahora se informan correctamente en lugar de mostrar "reproduciendo" mientras una pista aún se está obteniendo.
- **Mandos remotos fiables.** Reproducir, pausar, siguiente, anterior, buscar, saltar, aleatorio, repetir y velocidad de reproducción responden todos de forma coherente desde los botones de los auriculares, los mandos del coche y la pantalla de bloqueo, impulsados por `MPRemoteCommandCenter`.
- **Carátulas de CarPlay más rápidas.** Las carátulas de los álbumes ahora se cargan varias veces más rápido en listas largas (el ritmo de los lotes se redujo de 1,0 s a 0,25 s, y la primera pantalla visible se carga de inmediato), y ahora aparecen en las filas compactas de las listas de CarPlay de iOS 26 que antes no mostraban carátula.
- **Correcciones de ordenación y estabilidad en CarPlay.** Ordenación más rápida en bibliotecas grandes y refuerzo contra fallos en casos límite al desplazarse por listas largas.
- **Actualizaciones de metadatos limitadas.** Las actualizaciones de Reproduciendo y de los comandos remotos se limitan para que los cambios rápidos ya no saturen el sistema, lo que mantiene receptivos los controles de la pantalla de bloqueo y de CarPlay.

## Otras mejoras

- **Refinamientos del diseño Liquid Glass** en toda la app: superficies translúcidas, animaciones más fluidas y controles refinados en iOS, iPadOS y macOS.
- **Nuevos widgets de la pantalla de inicio** con una lógica de actualización mejorada que los mantiene sincronizados sin consumir batería adicional.
- Correcciones para versiones recientes de iOS.
- Correcciones de localización en varios idiomas.
- Muchas mejoras menores basadas en tus correos y reseñas del App Store.

## Por qué importa esta actualización

Evermusic 8.7 se construye en torno a una idea: **tu música debe sonar lo mejor posible, en cualquier fuente.**

1. **Álbumes completos, tal como se pensaron.** La verdadera reproducción sin cortes significa que los sets en directo, las sesiones de DJ y los álbumes conceptuales por fin suenan como los masterizó el artista.
2. **Un estudio en tu bolsillo.** Reverberación, delay, distorsión, compresor, crossfeed, un ecualizador rediseñado y normalización de sonoridad te dan control real sobre tu sonido, no solo un interruptor de encendido/apagado.
3. **La misma experiencia en todas partes.** Los archivos locales, las unidades en la nube, los servidores multimedia y la radio por internet pasan todos por el mismo motor reconstruido, con un Reproduciendo preciso y un CarPlay más rápido por encima.

## Consigue Evermusic 8.7

[**Descarga Evermusic desde el App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) o actualiza desde dentro del App Store. Evermusic es una descarga gratuita con mejoras opcionales dentro de la app para funciones avanzadas.

Si te gusta la app, deja una valoración en el App Store: de verdad ayuda. ¿Tienes comentarios o te has encontrado con algún problema? Escríbenos a **support@everappz.com**. Leemos cada mensaje.

## Preguntas frecuentes

{{% details title="¿Qué hay de nuevo en Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 añade verdadera reproducción sin cortes, cinco efectos de audio de estudio (reverberación, delay, distorsión, compresor y crossfeed), normalización de volumen EBU R128, un ecualizador de 10 bandas rediseñado con preajustes personalizados e importación/exportación, un motor de streaming AVAudioEngine reconstruido con mejor compatibilidad de formatos (incluidos FLAC y Ogg Vorbis), un CarPlay y Reproduciendo más rápidos y precisos, actualizaciones del diseño Liquid Glass, widgets de la pantalla de inicio renovados, y correcciones de errores y de localización.
{{% /details %}}

{{% details title="¿Tiene Evermusic verdadera reproducción sin cortes?" closed="true" %}}
Sí. A partir de Evermusic 8.7, la reproducción es realmente sin cortes: no hay pausa, clic ni chasquido entre pistas. El motor almacena por adelantado y decodifica la siguiente pista mientras suena la actual y hace el relevo entre las muestras de audio sobre un búfer circular continuo, de modo que la transición es inaudible. Funciona con archivos locales, transmisiones en la nube y servidores multimedia, y es ideal para álbumes en directo, sesiones de DJ y álbumes conceptuales.
{{% /details %}}

{{% details title="¿Qué efectos de audio incluye Evermusic 8.7?" closed="true" %}}
Cinco efectos en tiempo real: **reverberación** (13 preajustes de espacio, mezcla húmedo/seco), **delay/eco** (10 preajustes con tiempo de delay, realimentación, paso bajo y mezcla), **distorsión** (22 preajustes de carácter con preganancia y mezcla), **compresor** (un procesador de dinámica completo con umbral, relación, ataque, liberación, expansión y ganancia de compensación, más 10 preajustes) y **crossfeed** (crossfeed para auriculares Bauer bs2b con controles de nivel y corte y 6 preajustes). Cada efecto viene con preajustes cuidados, y tus ajustes personalizados se recuerdan entre sesiones.
{{% /details %}}

{{% details title="¿Qué es el crossfeed y por qué lo usaría?" closed="true" %}}
El crossfeed mezcla una pequeña cantidad filtrada de cada canal estéreo en el otro, tal como tus oídos oyen de forma natural los altavoces reales en una habitación. Con auriculares, esto reduce la separación exagerada, de "dentro de la cabeza", de las grabaciones con panoramización extrema y hace más cómoda la escucha prolongada. Evermusic usa el conocido algoritmo Bauer stereophonic-to-binaural (bs2b) e incluye preajustes como Chu Moy y Jan Meier. Es especialmente eficaz en mezclas estéreo antiguas de los años 60 y 70.
{{% /details %}}

{{% details title="¿Cómo funciona la normalización de volumen en Evermusic?" closed="true" %}}
Evermusic 8.7 mide la sonoridad percibida de cada pista usando el estándar EBU R128 (ITU-R BS.1770) en tiempo real y ajusta suavemente el nivel hacia un objetivo constante para que las pistas no den saltos de volumen. No requiere etiquetas de ReplayGain ni altera tus archivos. Hay cuatro preajustes disponibles (Ligero (−20 LUFS), Estándar (−16 LUFS), Fuerte (−14 LUFS) y Noche (−23 LUFS)) y la normalización se restablece de forma limpia cuando avanzas o cambias de pista.
{{% /details %}}

{{% details title="¿La normalización de volumen de Evermusic es lo mismo que ReplayGain?" closed="true" %}}
Logra el mismo objetivo (una sonoridad constante entre pistas) pero funciona de otra manera. ReplayGain depende de etiquetas de sonoridad almacenadas dentro de tus archivos. El normalizador de Evermusic mide la sonoridad en directo usando EBU R128, así que funciona con cualquier fuente, incluidas las transmisiones en la nube y la radio por internet, incluso cuando los archivos no tienen ninguna etiqueta.
{{% /details %}}

{{% details title="¿Cuántas bandas tiene el ecualizador de Evermusic, y puedo crear mis propios preajustes?" closed="true" %}}
El ecualizador de Evermusic es un ecualizador gráfico de 10 bandas que cubre de 32 Hz a 16 kHz, con cada banda ajustable de −12 dB a +12 dB en pasos de 0,1 dB y un preamplificador de −24 dB a +24 dB. Incluye preajustes integrados, te permite crear y guardar preajustes personalizados y admite importar y exportar preajustes como archivos .eqp para moverlos o compartirlos entre dispositivos.
{{% /details %}}

{{% details title="¿Qué cambió en el ecualizador de Evermusic 8.7?" closed="true" %}}
El ecualizador se rediseñó con nuevos controles deslizantes más precisos que adoptan el aspecto del control deslizante del sistema de iOS 26 y de Liquid Glass, un cambio de preajustes más rápido y fluido, y un mejor diseño en horizontal y en iPad (una barra horizontal de preajustes en vertical y una columna vertical de preajustes en horizontal). Se admiten los preajustes personalizados y la importación/exportación .eqp.
{{% /details %}}

{{% details title="¿Es compatible Evermusic 8.7 con FLAC y Ogg Vorbis?" closed="true" %}}
Sí. El motor reconstruido reproduce FLAC (mediante Core Audio) y Ogg Vorbis (mediante libvorbisfile), junto con MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF y más, desde archivos locales, unidades en la nube y servidores multimedia.
{{% /details %}}

{{% details title="¿Qué mejoró en CarPlay y en la pantalla de bloqueo?" closed="true" %}}
Las carátulas de los álbumes en CarPlay se cargan varias veces más rápido en listas largas y ahora aparecen en las filas compactas de las listas de iOS 26 que antes no mostraban ninguna. La información de Reproduciendo en la pantalla de bloqueo y en CarPlay es más precisa: el título, el tiempo transcurrido, la duración y el estado de reproducción/pausa se capturan juntos para que no puedan contradecirse, y los estados de almacenamiento en búfer se informan correctamente. Los mandos remotos (reproducir, pausar, siguiente, anterior, buscar, aleatorio, repetir, velocidad) responden de forma fiable desde los auriculares y el coche, y la ordenación en CarPlay en bibliotecas grandes es más rápida.
{{% /details %}}

{{% details title="¿Los efectos de audio y el ecualizador funcionan con streaming en la nube y CarPlay?" closed="true" %}}
Sí. Los efectos, el ecualizador y la normalización de volumen se ejecutan de forma nativa dentro del motor de reproducción, así que se aplican a todo lo que reproduce Evermusic (archivos locales, unidades en la nube, servidores multimedia y radio por internet) y siguen funcionando durante la reproducción en CarPlay y, donde sea compatible, por AirPlay y Chromecast.
{{% /details %}}

{{% details title="¿Es gratuita la actualización a Evermusic 8.7, y qué dispositivos admite?" closed="true" %}}
Sí. Evermusic es una descarga gratuita desde el App Store, y 8.7 es una actualización gratuita para los usuarios existentes, con mejoras opcionales dentro de la app para funciones avanzadas. Funciona en iPhone, iPad y Mac. CarPlay requiere un vehículo o una unidad compatible con CarPlay.
{{% /details %}}
