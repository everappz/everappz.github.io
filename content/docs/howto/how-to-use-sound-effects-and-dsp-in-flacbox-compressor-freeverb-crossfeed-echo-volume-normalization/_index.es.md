---
title: "Cómo usar los efectos de sonido y el DSP en Flacbox: Compressor, Freeverb, Crossfeed, Echo, normalización de volumen y más"
date: 2026-07-24
description: "La guía completa del audio de Flacbox en iPhone, iPad y Mac. Aprende cómo funciona el motor BASS, qué formatos adicionales reproduce (incluida la música MOD y de tracker y el DSD), y exactamente qué hace cada efecto, cada control deslizante y cada preajuste a tu sonido, además del ecualizador de 10 bandas y la cadena de DSP personalizada."
keywords: ["efectos de audio Flacbox", "preajustes de Flacbox explicados", "motor BASS de Flacbox", "biblioteca de audio BASS iOS", "reproductor de música MOD iPhone", "reproductor de música tracker iOS", "reproducir MOD XM IT S3M iPhone", "reproductor DSD iOS", "reproductor FLAC iPhone", "reproductor de música sin pérdida iOS", "preajustes de ecualizador Flacbox", "ecualizador de 10 bandas iPhone", "normalización de volumen iPhone", "EBU R128 iOS", "normalización de sonoridad reproductor de música", "crossfeed auriculares iOS", "crossfeed bs2b", "preajustes de compresor reproductor de música", "reverb freeverb iOS", "echo delay reproductor de música", "cadena DSP reproductor de música", "refuerzo de graves iPhone", "cómo añadir efectos a la música Flacbox", "mejores ajustes de ecualizador iPhone"]
tags: ["Flacbox", "Efectos de Audio", "Cómo Hacer", "BASS", "Ecualizador", "Refuerzo de Graves", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalización de Volumen", "EBU R128", "Música MOD", "Música Tracker", "DSD", "FLAC", "DSP", "Auriculares", "Preajustes"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Respuesta corta:** En Flacbox eliges un **Motor de reproducción** en **Ajustes > Reproductor de audio**: **Standard** (el motor del sistema de Apple), **Universal** (el motor FFmpeg) o **Sound FX** (el **motor BASS™**). El motor que elijas decide qué formatos de archivo se reproducen, así que la elección importa. El motor **Sound FX** reproduce formatos adicionales que la mayoría de las apps de iPhone omiten (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus y la vieja **música MOD y de tracker** como MOD, XM, IT y S3M), y es el único motor que activa las herramientas de sonido: un **ecualizador de 10 bandas**, **Normalización de volumen**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** y una **cadena de DSP** que construyes tú mismo. Así que, para usar los efectos de esta guía, primero configura tu Motor de reproducción en **Sound FX**. Cada herramienta tiene **preajustes** ya preparados. Ábrelos en **Ajustes > Reproductor de audio** (Efectos de audio, Ecualizador de audio, Procesamiento de señal), o toca el botón **⋯ (Más)** en el reproductor y elige **Efectos de audio**. Nada de lo que hagas aquí cambia nunca tus archivos.

> Las explicaciones de los controles deslizantes y los preajustes que aparecen abajo son las mismas descripciones breves que Flacbox te muestra dentro de la app, combinadas con un poco de contexto adicional para que tengas el panorama completo antes de tocar.

## Cómo leer esta guía

Todas las herramientas funcionan de la misma manera:

1. **Actívala.** Cada efecto tiene su propio interruptor de encendido/apagado. Al principio están todos apagados. Puedes activar tantos como quieras al mismo tiempo.
2. **Elige un preajuste.** Un preajuste es un ajuste ya preparado. Toca uno y el sonido cambia al instante. Esta guía enumera lo que hace **cada** preajuste.
3. **Ajusta con precisión (opcional).** Abre los controles deslizantes para ajustar a mano. En el momento en que mueves un control deslizante, el efecto muestra **Manual**, así sabes que has salido del preajuste. Cada control deslizante tiene un botón de reinicio.

Nada se guarda en tus archivos. Estos son efectos en vivo. Apaga un efecto y tu sonido original vuelve de inmediato.

## Elige tu motor de reproducción (Sound FX tiene los efectos)

Flacbox no mezcla los motores entre sí. Eliges **uno** en **Ajustes > Reproductor de audio > Motor de reproducción**, y el motor que elijas decide qué formatos de archivo puedes reproducir y si los efectos están disponibles. Hay tres opciones, mostradas en la app con estos nombres exactos:

1. **Standard.** El motor del sistema integrado de Apple. Usa la decodificación por hardware para un menor consumo de batería.
2. **Universal.** El motor FFmpeg, que abre una gama muy amplia de formatos.
3. **Sound FX.** El **motor BASS™**. Reproduce archivos sin pérdida y de alta resolución con total precisión, añade la música de módulos (tracker) y activa todos los efectos, el ecualizador de 10 bandas y la cadena de DSP de esta guía.

Como cada motor admite su propio conjunto de formatos, los archivos que puedes reproducir cambian según el motor que selecciones. Más importante aún, los efectos, el ecualizador y la cadena de DSP funcionan **solo** con el motor **Sound FX**, así que elígelo primero si quieres usarlos.

Sound FX está construido sobre **BASS™**, una biblioteca de audio profesional de Un4seen Developments. Puedes leer más al respecto en su página principal en [un4seen.com](https://www.un4seen.com/).

## Formatos de música: lo que añade el motor Sound FX (BASS™) (incluida la música MOD y de tracker)

Con el motor **Sound FX (BASS™)** seleccionado, Flacbox reproduce los formatos especializados que aparecen a continuación, además de los habituales. El más especial es la **música de módulos**, también llamada **música de tracker**. Un archivo de módulo no es una grabación normal. Contiene pequeños sonidos de instrumentos más una «partitura» que indica cómo reproducirlos, y Flacbox reconstruye la canción en vivo a partir de esa partitura, tal como estos archivos estaban destinados a reproducirse. Los reproductores normales no pueden hacer esto.

| Tipo de música | Formatos | Bueno saber |
|---|---|---|
| **Música de módulos / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Reconstruida en vivo por el reproductor de módulos BASS™. Genial para chiptunes y viejas canciones de la demoscene o de Amiga. |
| **Sin pérdida moderno** | FLAC | Calidad completa, más pequeño que WAV. |
| **Otros sin pérdida** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Tipos sin pérdida menos comunes, todos compatibles. |
| **DSD de alta resolución** | DSF, DFF | Se reproduce en hardware normal usando DSD sobre PCM. |
| **Con pérdida moderno** | Opus, Ogg Vorbis, MP3 | Los tipos habituales de streaming y descarga. |

El motor Sound FX también reproduce los formatos principales de Apple (AAC, ALAC, M4A, WAV, AIFF) y transmisiones en vivo, así que los efectos y el ecualizador también funcionan con esos.

**Por qué esto te ayuda:** si tienes una mezcla de álbumes FLAC, archivos DSD de alta resolución y una carpeta de viejas canciones tracker MOD o XM, Flacbox las reproduce todas, y el ecualizador y los efectos funcionan con cada una de ellas.

## Los tres menús que usarás

Flacbox guarda sus herramientas de sonido en tres lugares, todos dentro de los ajustes del reproductor de audio. Primero asegúrate de que tu **Motor de reproducción** esté configurado en **Sound FX** (Ajustes > Reproductor de audio > Motor de reproducción), porque los efectos, el ecualizador y la cadena de DSP están disponibles solo con ese motor.

- **Efectos de audio** (el rack de efectos): abre el reproductor, toca **⋯ (Más)**, toca **Efectos de audio**. O ve a **Ajustes > Reproductor de audio > Efectos de audio**.
- **Ecualizador de audio** (10 bandas y preajustes): **Ajustes > Reproductor de audio > Ecualizador de audio**.
- **Procesamiento de señal** (tu propia cadena de DSP): **Ajustes > Reproductor de audio > Procesamiento de señal**.

También puedes configurar la **frecuencia de muestreo de salida**, los **canales** y el **tamaño del búfer** en **Ajustes > Reproductor de audio**.

## El ecualizador de 10 bandas

**Qué hace:** Cambia el tono de la música, desde los graves profundos hasta los agudos brillantes. Esta es la mejor herramienta para un **refuerzo de graves** limpio o un extremo superior más brillante y claro. Piénsalo como diez perillas de volumen, cada una para una porción diferente del sonido. Sube una banda para traer esa parte al frente, bájala para llevarla atrás. Los cambios pequeños de unos pocos dB suelen sonar mejor, y funciona con todo lo que reproduces.

**Cómo funciona:** Diez controles deslizantes en **32, 64, 125, 250, 500 Hz y 1, 2, 4, 8, 16 kHz**. Cada uno va de **-12 dB (corte)** a **+12 dB (refuerzo)**. También hay un **Preamplificador** de **-24 a +24 dB** para el nivel general. Puedes guardar tus propios preajustes y **exportarlos o importarlos** entre dispositivos.

**Qué hace cada preajuste integrado (22 preajustes):**

| Preajuste | Qué le hace a tu sonido |
|---|---|
| **Flat** | Sin cambios. Todas las bandas en cero. Un punto de partida limpio. |
| **Acoustic** | Graves cálidos y agudos nítidos y presentes. Hace que las guitarras acústicas y las voces se sientan naturales y vivas. |
| **Bass Booster** | Fuerte realce en los graves, medios y agudos intactos. Más pegada y peso. |
| **Bass Reducer** | Recorta los graves. Útil para salas retumbantes, auriculares baratos o pistas pesadas. |
| **Treble Booster** | Realza solo los agudos. Añade brillo y aire, más detalle. |
| **Treble Reducer** | Suaviza los agudos. Domestica grabaciones ásperas o cortantes. |
| **Classical** | Graves plenos y agudos suaves con una ligera caída en los medios. Suave y espacioso para la música orquestal. |
| **Dance** | Graves grandes y agudos brillantes con medios rebajados. Contundente y enérgico para pistas de club. |
| **Deep** | Extremo grave cálido y denso con agudos más suaves. Un sonido acogedor y relajado. |
| **Electronic** | Graves fuertes y agudos brillantes para sintetizadores y ritmos. Amplio y moderno. |
| **Hip-Hop** | Graves pesados y agudos claros con medios controlados. Con peso y pegada. |
| **Jazz** | Cálido y suave, con una pequeña caída en los medios. Fácil y natural para el jazz acústico. |
| **Latin** | Graves y agudos reforzados con medios limpios. Brillante y animado. |
| **Loudness** | Refuerza los graves y agudos con fuerza (una curva de «sonrisa»). Suena más pleno a bajo volumen. |
| **Lounge** | Medios al frente con bordes suaves. Relajado y amigable para las voces. |
| **Piano** | Medios y agudos claros para que las notas del piano resuenen limpiamente. |
| **Pop** | Medios realzados para las voces, con graves y agudos rebajados. Las voces quedan al frente. |
| **R&B** | Calidez de graves-medios muy fuerte y agudos claros. Suave y rico. |
| **Rock** | Graves y agudos reforzados para guitarras y baterías. Enérgico y pleno. |
| **Small Speakers** | Refuerza los graves y recorta los agudos para ayudar a que los altavoces pequeños suenen más plenos. |
| **Spoken Word** | Realza el rango de la voz y recorta los graves profundos. Hace que el habla sea clara. |
| **Vocal Booster** | Empuja el centro donde viven las voces, recorta a su alrededor. Las voces destacan. |

**Consejo para los graves:** Comienza con **Bass Booster** y luego, si suena turbio, baja el Preamplificador de 1 a 2 dB para que nada se distorsione.

## Normalización de volumen (sonoridad pareja)

**Qué hace:** Algunas canciones suenan más fuerte que otras, así que sigues cambiando el volumen. Esto hace que cada canción se reproduzca aproximadamente al mismo volumen por sí sola, para que no tengas que hacerlo. Es perfecto para listas de reproducción aleatorias que mezclan grabaciones viejas y nuevas, distintos álbumes o distintas fuentes, donde una pista puede ser mucho más fuerte que la siguiente.

**Cómo funciona:** Escucha la sonoridad real de cada pista usando el estándar **EBU R128** (medido en **LUFS**, la misma idea que usan los servicios de streaming), luego ajusta cada pista hacia tu objetivo. No necesita etiquetas en tus archivos y nunca cambia el audio. EBU R128 mide la sonoridad que tus oídos realmente perciben a lo largo de toda la canción, no solo el pico más alto, y por eso coincide con lo fuerte que realmente te parecen las pistas. Flacbox lo calcula en vivo mientras suena la música (y comprueba la sonoridad por adelantado cuando puede), luego aplica un único cambio de volumen estable a la pista. El límite de **Refuerzo máximo** evita que las grabaciones muy silenciosas se suban tanto que se distorsionen. Como lee el sonido en sí, funciona con cualquier fuente, incluidos archivos en la nube, transmisiones en vivo y música de módulos, incluso cuando los archivos no tienen etiquetas de sonoridad en absoluto.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Sonoridad objetivo** | Establece la sonoridad hacia la que se nivela cada pista. Valores más altos hacen que todo suene más fuerte en general. | -30 a -6 LUFS (-16) |
| **Refuerzo máximo** | Limita cuánto pueden amplificarse las pistas silenciosas. Valores más altos acercan las grabaciones suaves al objetivo. | 0 a 24 dB (12) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Light** | Nivelación suave para la escucha informal. Empareja los saltos de volumen evidentes sin subir con fuerza las pistas silenciosas. |
| **Standard** | El valor predeterminado para todo uso. Un objetivo de sonoridad estilo streaming que le va bien a la mayoría de la música. Empieza aquí. |
| **Strong** | Emparejado agresivo que sube con firmeza las pistas silenciosas. Ideal para bibliotecas mixtas con grandes diferencias de nivel. |
| **Night** | Un objetivo general más silencioso que aún realza los pasajes suaves, para que la escucha nocturna se mantenga constante y baja. |

## Compressor (empareja las partes fuertes y silenciosas)

**Qué hace:** En una misma canción, las partes silenciosas pueden ser demasiado suaves y las partes fuertes demasiado altas. Esto las acerca, para que toda la canción sea fácil de escuchar, incluso en el coche o en un lugar ruidoso. Baja suavemente los momentos más fuertes y realza los más suaves, para que dejes de buscar el volumen durante una misma pista. Esto es diferente de la Normalización de volumen: el Compressor empareja las cosas **dentro** de una canción, mientras que la Normalización de volumen iguala la sonoridad **entre** canciones. Los dos funcionan bien juntos. Empieza con un preajuste, y solo abre los controles deslizantes si quieres más control.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Threshold** | El nivel donde comienza la compresión. Valores más bajos aplastan más del sonido, manteniendo las partes silenciosas y fuertes más cerca entre sí. | -60 a 0 dB (-20) |
| **Ratio** | Con qué fuerza se contienen las partes fuertes una vez que superan el umbral. Valores más altos comprimen con más dureza, manteniendo el sonido más parejo. | 1:1 a 30:1 (4:1) |
| **Attack** | Con qué rapidez responde el efecto a un pico fuerte repentino. Valores cortos atrapan los transitorios; los más largos los dejan pasar. | 0.1 a 1000 ms (10 ms) |
| **Release** | Con qué rapidez suelta el efecto después de que pasa la parte fuerte. Valores cortos pueden bombear; los más largos suenan más suaves. | 10 ms a 5 s (100 ms) |
| **Master gain** | Realce final de salida aplicado tras el procesamiento. Súbelo para elevar la sonoridad general una vez emparejada la dinámica. | -30 a +30 dB (0) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Transparent** | Red de seguridad casi imperceptible. Conserva la dinámica casi por completo y solo atrapa los picos más fuertes. |
| **Soft** | Nivelación ligera para la escucha hi-fi en casa. Suavizado sutil sin aplastar la música. |
| **Standard** | Valor predeterminado sensato para la reproducción diaria de música. El primer preajuste que probar. |
| **Heavy** | Emparejado agresivo para entornos ruidosos. Coche, sala concurrida, escucha a bajo volumen. |
| **Voice / Podcast** | Ajustado para el habla. Un ataque más lento deja pasar las sibilantes, y una generosa ganancia de compensación sube las voces. |
| **Old Recordings** | Álbumes antiguos y vinilos restaurados, donde el nivel medio está por debajo de los lanzamientos modernos. |
| **Late Night** | Compresión fuerte más un gran realce para la escucha silenciosa cuando importan los vecinos o la familia dormida. |
| **Movie Dialog** | Sube el habla frente a la música y los efectos de sonido en una banda sonora variada. |
| **Streaming Match** | Apunta aproximadamente a la normalización de sonoridad de los servicios de streaming modernos, en torno a -14 LUFS. |
| **Maximum Loudness** | A tope. Alcanza el limitador; espera una señal aplastada y muy pareja. El preajuste literal de volumen máximo. |

## Freeverb (reverb, una sensación de espacio)

**Qué hace:** Añade una sensación de espacio a la música, desde una habitación pequeña hasta una gran sala. Elige un preajuste, o ajusta tú mismo la mezcla seca y húmeda, el tamaño de la sala, la amortiguación y el ancho. La reverb es el eco natural que oyes en cualquier espacio real, y Freeverb lo recrea por software. Un poco hace que las grabaciones planas o tomadas de cerca se sientan más abiertas y vivas. Mucha coloca la música en un espacio grande y distante. Es un efecto creativo, así que mantén la mezcla húmeda moderada para obtener resultados naturales.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Dry mix** | Cuánto del sonido original e intacto se conserva. Valores más altos dejan más de la señal seca en la mezcla. | 0 a 1 (0.0) |
| **Wet mix** | Cuánto del sonido reverberado se añade. Valores más altos hacen la reverb más fuerte y evidente. | 0 a 3 (1.0) |
| **Room size** | El tamaño del espacio imaginado. Valores más altos dan una cola de reverb más larga y grande, desde una habitación pequeña hasta una catedral. | 0 a 1 (0.5) |
| **Damp** | Con qué rapidez se apagan las altas frecuencias en la cola. Valores más altos hacen la reverb más oscura y cálida. | 0 a 1 (0.5) |
| **Width** | La amplitud estéreo de la reverb. Valores más altos hacen que el espacio se sienta más amplio entre los canales izquierdo y derecho. | 0 a 1 (1.0) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Room** | Un espacio pequeño y ceñido. Ambiente sutil que añade una sensación de lugar sin lavar el sonido. |
| **Studio** | Una sala de grabación seca y controlada. Justo el reflejo suficiente para sonar natural. |
| **Hall** | Una gran sala de conciertos. Una cola larga y exuberante que le va a la música orquestal y acústica. |
| **Cathedral** | Un enorme espacio de piedra con eco. La cola de reverb más larga y dramática. |
| **Plate** | Una reverb de placa de estudio brillante y densa. Clásica para voces y baterías. |
| **Ambience** | Un ambiente corto y aireado. Añade una ligera sensación de espacio manteniéndose mayormente seco. |

## Auto Wah (barrido de filtro funky)

**Qué hace:** Un filtro que barre hacia arriba y hacia abajo por sí solo para un sonido wah funky y parecido a la voz. Elige un preajuste, o ajusta tú mismo la mezcla húmeda, la realimentación, la velocidad, el rango y la frecuencia. Es el mismo barrido «wah» que hace un pedal wah de guitarra, pero aquí se mueve por sí solo al ritmo de la música. Suena genial en pistas funk, disco y electrónicas. Es un efecto audaz y evidente, así que un poco rinde mucho en la escucha cotidiana.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Wet mix** | Cuán fuerte es el efecto wah en la mezcla. Valores más altos hacen el filtro de barrido más evidente. | -2 a +2 (1.5) |
| **Feedback** | Cuánto de la salida se realimenta al efecto. Valores más altos hacen el wah más resonante y pronunciado. | -1 a +1 (0.5) |
| **Rate** | Con qué rapidez barre el filtro hacia arriba y hacia abajo. Valores más altos dan un wah más rápido y rítmico. | 0.1 a 9 Hz (2.0) |
| **Range** | Cuán lejos barre el filtro, en octavas. Valores más altos dan un barrido más amplio y dramático. | 0.1 a 9 octavas (4.3) |
| **Frequency** | La frecuencia base alrededor de la cual barre el filtro. Valores más bajos suenan más profundos; los más altos suenan más brillantes. | 1 a 1000 Hz (50) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Classic** | Un barrido wah clásico y equilibrado. Un buen punto de partida para funk y rock. |
| **Slow** | Un barrido lento y amplio que se desliza suavemente hacia arriba y hacia abajo. Genial para pads y notas largas. |
| **Funky** | Un barrido rápido y contundente con mucho movimiento. Añade mordida rítmica a guitarras y sintetizadores. |
| **Deep** | Un barrido profundo y amplio que parte de una frecuencia baja. Grande y dramático. |
| **Subtle** | Un movimiento suave y discreto. Añade carácter sin dominar el sonido. |
| **Resonant** | Un wah agudo y resonante con alta realimentación. Parecido a la voz y expresivo. |

## Phaser (silbido arremolinado)

**Qué hace:** Un filtro de barrido que añade un movimiento arremolinado y silbante al sonido. Elige un preajuste, o ajusta tú mismo la realimentación, la velocidad, el rango y la frecuencia. Añade movimiento suave y destellos sin cambiar las notas. Es sutil en voces y pads, y dramático en sintetizadores y guitarras. Prueba Slow para una sensación de ensueño o Jet para un remolino fuerte.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Feedback** | Cuánto de la salida se realimenta al efecto. Valores más altos hacen el phaser más resonante y pronunciado. | -1 a +1 (0.0) |
| **Rate** | Con qué rapidez barre el filtro hacia arriba y hacia abajo. Valores más altos dan un fraseo más rápido y rítmico. | 0.1 a 9 Hz (1.0) |
| **Range** | Cuán lejos barre el filtro, en octavas. Valores más altos dan un barrido más amplio y dramático. | 0.1 a 9 octavas (4.0) |
| **Frequency** | La frecuencia base alrededor de la cual barre el filtro. Valores más bajos suenan más profundos; los más altos suenan más brillantes. | 1 a 1000 Hz (100) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Classic** | Un barrido de phaser clásico y equilibrado. Un buen punto de partida para guitarras y teclados. |
| **Slow** | Un barrido lento y amplio que se desliza suavemente hacia arriba y hacia abajo. Genial para pads y notas largas. |
| **Fast** | Un barrido rápido y reluciente con mucho movimiento. Añade movimiento y energía. |
| **Deep** | Un barrido profundo y amplio que parte de una frecuencia baja. Grande y dramático. |
| **Subtle** | Un movimiento suave y discreto. Añade carácter sin dominar el sonido. |
| **Jet** | Un barrido intenso y resonante con alta realimentación, el clásico silbido de avión a reacción. |

## Flanger (barrido de avión a reacción)

**Qué hace:** Un retardo corto y en movimiento que le da al sonido un silbido de barrido tipo jet. Elige un preajuste, o ajusta tú mismo la profundidad, la realimentación, la velocidad y el retardo. Es un primo más fuerte y metálico del phaser, famoso por el barrido silbante del rock clásico y la música electrónica. Los ajustes sutiles añaden movimiento suave, mientras que los profundos son dramáticos y evidentes. Mejor usarlo con moderación, como efecto.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Depth** | Cuán fuerte es el efecto de barrido. Valores más altos hacen el flanging más evidente. | 0 a 100% (25) |
| **Feedback** | Cuánto de la salida se realimenta al efecto. Valores más altos hacen el flanger más resonante y metálico. | -99 a +99% (-50) |
| **Rate** | Con qué rapidez se mueve el barrido hacia arriba y hacia abajo. Valores más altos dan un movimiento más rápido y reluciente. | 0 a 10 Hz (0.25) |
| **Delay** | El tiempo de retardo base sobre el que se construye el barrido. Valores más altos dan un carácter más profundo y hueco. | 0 a 4 ms (2.0) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Classic** | Un flanger clásico y equilibrado. Un buen punto de partida para guitarras y teclados. |
| **Subtle** | Un barrido suave y discreto. Añade movimiento sin dominar el sonido. |
| **Deep** | Un barrido profundo y pesado con fuerte realimentación. Grande y dramático. |
| **Jet** | Un barrido intenso con realimentación positiva, el clásico silbido de avión a reacción. |
| **Fast** | Un barrido rápido y reluciente con mucho movimiento y energía. |
| **Wide** | Un barrido lento y amplio con un retardo largo. Exuberante y espacioso. |

## Echo (repeticiones)

**Qué hace:** Repite el sonido como ecos que se desvanecen para dar una sensación de espacio y profundidad. Elige un preajuste, o ajusta tú mismo la mezcla húmeda, la realimentación y el retardo. Es como gritar en un cañón: el sonido vuelve una o más veces tras una breve pausa. Una única repetición corta añade cuerpo y una sensación retro, mientras que repeticiones más largas con más realimentación crean colas espaciosas y arrastradas. El preajuste Ping Pong rebota las repeticiones entre tus oídos izquierdo y derecho, lo cual es divertido en auriculares. Mantén la mezcla húmeda moderada para que los ecos apoyen la música en lugar de taparla.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Wet mix** | Cuán fuertes son los ecos comparados con el sonido original. Valores más altos hacen que las repeticiones destaquen más. | -2 a +2 (0.6) |
| **Feedback** | Cuántas veces se repite el eco. Valores más altos dan más repeticiones que tardan más en desvanecerse. | -1 a +1 (0.5) |
| **Delay** | El tiempo entre ecos. Valores más cortos dan un slap-back ceñido; los más largos dan repeticiones más espaciadas. | 0.01 a 2 s (0.4) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Slapback** | Una única repetición ceñida justo detrás del sonido. Slap-back clásico de rockabilly. |
| **Room** | Un eco corto y natural, como una habitación pequeña. Añade espacio sin emborronar el sonido. |
| **Tape** | Repeticiones cálidas y medias que se desvanecen gradualmente, como un viejo delay de cinta. |
| **Dub** | Repeticiones largas y pesadas con fuerte realimentación. Grande, dub y espacioso. |
| **Ping Pong** | Los ecos rebotan entre los altavoces izquierdo y derecho para un amplio efecto estéreo. |
| **Long** | Repeticiones lentas y muy espaciadas que se desvanecen lejos detrás del sonido. |

## Chorus (sonido más grueso y amplio)

**Qué hace:** Engrosa y ensancha el sonido superponiendo una copia cambiante sobre el original. Elige un preajuste, o ajusta tú mismo la mezcla húmedo/seco, la profundidad, la velocidad y la realimentación. Hace que un instrumento o voz suene como varios tocando juntos, añadiendo copias ligeramente desafinadas y en movimiento. Esto añade riqueza y un destello suave. Los ajustes sutiles dan calidez, mientras que los ajustes fuertes suenan exuberantes y de ensueño. Es popular en guitarras, teclados y voces.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Wet/Dry** | Cuánto del chorus oyes comparado con el sonido original. Valores más altos hacen el efecto más evidente. | 0 a 100% (50) |
| **Depth** | Cuán lejos oscila el tono hacia arriba y hacia abajo. Valores más altos dan un sonido más grueso y reluciente. | 0 a 100% (25) |
| **Rate** | Con qué rapidez se mueve el destello. Velocidades más lentas suenan suaves y exuberantes; las más rápidas suenan más como vibrato. | 0 a 10 Hz (1.1) |
| **Feedback** | Cuánto del efecto se realimenta a sí mismo. Valores más altos hacen el chorus más resonante e intenso. | -99 a +99% (25) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Subtle** | Un engrosamiento suave que añade calidez sin llamar la atención sobre sí mismo. |
| **Lush** | Un chorus rico y clásico. Un gran ajuste versátil para guitarras y teclados. |
| **Ensemble** | Un destello pleno y en capas que hace que un solo instrumento suene como varios. |
| **Vibrato** | Totalmente húmedo con una velocidad rápida, para un vibrato ondulante en lugar de un chorus sutil. |
| **Wide** | Un destello lento y amplio que abre la imagen estéreo. Espacioso y de ensueño. |
| **Twelve-String** | Un destello brillante y resonante que recuerda a una guitarra de doce cuerdas. |

## Distortion (aspereza y filo)

**Qué hace:** Añade aspereza y filo saturando el sonido. Elige un preajuste, o ajusta tú mismo el drive, la salida y el tono. Endurece deliberadamente el sonido, desde un filo cálido y áspero hasta un tono roto y difuso. Es un efecto creativo y de diversión más que una forma de mejorar la calidad, así que úsalo en pequeñas cantidades. Es divertido en pistas electrónicas, rock y experimentales. Baja la Salida si un preajuste pesado se vuelve demasiado fuerte.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Drive** | Cuán fuerte se distorsiona el sonido. Valores más altos son más ásperos y agresivos. | 0 a 100% (15) |
| **Output** | El nivel de salida tras la distorsión. Bájalo si un ajuste pesado se vuelve demasiado fuerte. | -60 a 0 dB (-18) |
| **Tone** | Recorta los agudos antes de la distorsión. Valores más bajos suenan más oscuros y cálidos. | 100 a 8000 Hz (8000) |
| **Center** | Alrededor de qué frecuencia se enfoca la distorsión. Desplaza el carácter hacia más brillante u oscuro. | 100 a 8000 Hz (2400) |
| **Width** | Cuán amplio es ese enfoque. Estrecho suena agudo y nasal; amplio suena pleno y abierto. | 100 a 8000 Hz (2400) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Warm Drive** | Una aspereza ligera y cálida que añade filo sin cambiar mucho el carácter. |
| **Crunch** | Un overdrive crujiente clásico, contundente y rítmico. |
| **Overdrive** | Un tono brillante y saturado con mucha mordida. Genial para sonidos solistas. |
| **Fuzz** | Un fuzz grueso y saturado. Pesado y lleno de armónicos. |
| **Metal** | Un tono ceñido de alta ganancia enfocado en los medios para sonidos agresivos y pesados. |
| **Screamer** | Un overdrive con medios reforzados que atraviesa la mezcla, como un tube screamer. |
| **LoFi** | Una distorsión aplastada y de banda estrecha para un carácter lo-fi áspero. |

## Rotate (estéreo giratorio)

**Qué hace:** Hace girar el sonido alrededor del campo estéreo para un efecto rotatorio y arremolinado. Elige un preajuste, o ajusta tú mismo la velocidad. Mueve lentamente el sonido alrededor de tus canales izquierdo y derecho, un poco como un altavoz giratorio, lo que añade una sensación arremolinada e hipnótica. Los ajustes lentos son suaves y amplios, mientras que los ajustes rápidos son mareantes y evidentes. Es un efecto estéreo, así que se nota más en auriculares o altavoces bien ubicados.

**Control deslizante:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Rate** | Con qué rapidez gira el sonido alrededor del campo estéreo. Los valores negativos giran en sentido contrario; el cero lo mantiene quieto. | -5 a +5 Hz (1.0) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Slow Pan** | Una deriva lenta y suave de lado a lado. Sutil y amplio. |
| **Sway** | Un balanceo izquierda-derecha constante. Añade movimiento suave a la imagen estéreo. |
| **Rotary** | Un giro medio que recuerda a un altavoz giratorio. |
| **Fast Spin** | Un giro rápido alrededor del campo estéreo para un efecto mareante y arremolinado. |
| **Reverse** | Un giro medio en la dirección opuesta. |
| **Whirl** | Un remolino muy rápido. Intenso y desorientador. |

## Crossfeed (sonido natural en auriculares)

En los altavoces, cada uno de tus oídos oye tanto el altavoz izquierdo como el derecho, solo que con tiempos y volúmenes ligeramente distintos. En auriculares, esa mezcla natural desaparece: tu oído izquierdo oye solo el canal izquierdo y tu oído derecho solo el derecho. Este «súper estéreo» puede hacer que la música se sienta dividida dentro de tu cabeza, y las grabaciones con paneo extremo, donde un instrumento se sitúa por completo en un lado, pueden sentirse antinaturales o fatigosas en escuchas largas.

Crossfeed corrige esto mezclando una pequeña cantidad filtrada de cada canal en el otro, con un retardo diminuto y una suave atenuación de las altas frecuencias. Eso se aproxima a cómo el sonido de altavoces reales llega a tus dos oídos, incluida la forma en que tu cabeza ensombrece ligeramente el oído más lejano. El resultado es una imagen más natural, tipo altavoz, que se sitúa un poco delante de ti en lugar de dentro de tu cabeza, y reduce la fatiga auditiva en sesiones largas. Flacbox usa el conocido método **bs2b (Bauer stereophonic-to-binaural)**, un respetado crossfeed de código abierto usado por muchos reproductores audiófilos. Puedes leer sobre el algoritmo en la [página del proyecto bs2b](https://bs2b.sourceforge.net/).

El **Cutoff** controla cuán cálida suena la mezcla, y el **Feed level** controla cuán fuerte es. Los preajustes cubren los niveles clásicos de bs2b, desde un toque apenas perceptible hasta una mezcla firme y tipo altavoz. Crossfeed es un efecto de auriculares, así que déjalo apagado cuando escuches en altavoces.

**Controles deslizantes:**

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Cutoff** | Establece dónde empieza a atenuarse la fuga entre canales. Valores más bajos dan un efecto más cálido y pronunciado. | 300 a 2000 Hz (700) |
| **Feed level** | Controla cuánto de un canal se fuga al otro. Valores más altos producen un sonido más parecido al de un altavoz. | 1 a 15 dB (4.5) |

**Preajustes:**

| Preajuste | Qué hace |
|---|---|
| **Subtle** | Crossfeed apenas perceptible para la escucha informal. Suaviza el estéreo de paneo extremo sin cambiar el equilibrio tonal. |
| **Chu Moy** | El clásico valor predeterminado para todo uso. Equilibrado y ligeramente cálido, funciona con casi cualquier material. Empieza aquí. |
| **Strong** | Fuga más fuerte para mezclas de paneo más extremo. Estrechamiento estéreo más evidente. |
| **Jan Meier** | Popular entre los entusiastas de los auriculares. Fuga más amplia, presentación más tipo altavoz, ligero realce de graves. |
| **Speaker-like** | Ajustado para la reproducción tipo altavoz más natural sobre auriculares. |
| **Vintage Stereo** | Crossfeed agresivo ajustado para las mezclas de los años 1960 y 1970 con baterías y voces de paneo extremo. |

## Procesamiento de señal: construye tu propia cadena de DSP

Más allá de los efectos ya preparados, Flacbox te permite construir tu propia cadena en **Ajustes > Reproductor de audio > Procesamiento de señal**. Como explica la app cuando la cadena está vacía: *«Toca + para añadir un efecto. Enciende o apaga cada uno con su interruptor, arrastra para reordenar, toca para editar sus parámetros y mantén pulsado para duplicar o eliminar.»*

El **orden importa**: un filtro antes de una distorsión suena distinto al mismo filtro después de ella. También puedes dirigir toda la cadena a **Todos los canales**, **Canal izquierdo** o **Canal derecho**.

A continuación aparece cada bloque, con el texto propio de la app para cada control deslizante y cada preajuste.

### Gain (recorte de nivel)

Sube o baja el nivel en un punto de la cadena.

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Gain** | Refuerza o recorta el nivel en este punto de la cadena. Úsalo para recuperar nivel tras otros efectos, o para saturar los que siguen. | -24 a +24 dB (0) |

| Preajuste | Qué hace |
|---|---|
| **Unity** | Sin cambio de nivel. Un punto de partida neutro. |
| **Cut** | Un gran corte. Domestica una fuente fuerte, o hace sitio antes de los efectos que siguen. |
| **Trim** | Un corte suave para bajar un poco el nivel. |
| **Lift** | Un realce modesto para subir una fuente silenciosa. |
| **Boost** | Un realce fuerte para material silencioso, o para saturar con más fuerza los efectos siguientes. |
| **Max** | Realce máximo. Fuerte, cuidado con el recorte más adelante en la cadena. |

### Low Pass (elimina los agudos)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Cutoff** | Establece dónde empieza el filtro a atenuar los agudos. Bájalo para oscurecer y suavizar el sonido; súbelo hacia arriba para abrir por completo. | 20 Hz a 20 kHz (20 kHz) |
| **Resonance** | Enfatiza las frecuencias justo en el punto de corte. Mantenlo bajo para una atenuación limpia; súbelo para un filo puntiagudo y silbante. | 0.1 a 10 (0.707) |

| Preajuste | Qué hace |
|---|---|
| **Air** | Recorta solo la parte más alta. Quita un poco de filo sin apagar el sonido. |
| **Warm** | Una atenuación suave de los agudos para un tono más cálido y redondo. |
| **Mellow** | Notablemente suavizado. Baja el brillo para una sensación relajada. |
| **Muffled** | Oscuro y apagado, como si se oyera a través de una pared. |
| **Telephone** | Un pico estrecho y resonante bajo en el rango. Una voz delgada, tipo teléfono. |

### High Pass (elimina los graves)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Cutoff** | Establece dónde empieza el filtro a atenuar los graves. Súbelo para adelgazar el extremo grave y quitar el retumbe; bájalo hacia abajo para abrir por completo. | 20 Hz a 20 kHz (20 Hz) |
| **Resonance** | Enfatiza las frecuencias justo en el punto de corte. Mantenlo bajo para una atenuación limpia; súbelo para un filo puntiagudo y silbante. | 0.1 a 10 (0.707) |

| Preajuste | Qué hace |
|---|---|
| **Rumble Cut** | Elimina el retumbe subsónico y el desplazamiento de DC sin tocar el extremo grave audible. |
| **Tighten** | Recorta las frecuencias graves retumbantes para un bajo más ceñido y limpio. |
| **Thin** | Recorta la calidez y el cuerpo, dejando un sonido más ligero y delgado. |
| **Radio** | Solo quedan los medios y agudos, como el altavoz de una radio pequeña. |
| **Telephone** | Un pico estrecho y resonante alto en el rango. Una voz delgada, tipo teléfono. |

### Band Pass (mantiene una banda media)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Center** | Establece la frecuencia que pasa el filtro. Todo lo de arriba y abajo se atenúa. Barre para seleccionar graves, medios o agudos. | 20 Hz a 20 kHz (1 kHz) |
| **Resonance** | Controla cuán ancha es la banda. Valores bajos dejan pasar un rango amplio; súbelo para estrechar en torno al centro y lograr un tono agudo y resonante. | 0.1 a 10 (0.707) |

| Preajuste | Qué hace |
|---|---|
| **Voice** | Una banda amplia alrededor del rango medio donde se sitúan la mayoría de las voces. Un punto de partida neutro. |
| **Bass** | Aísla el extremo grave, dejando solo el bajo y el bombo. |
| **Body** | Se enfoca en los graves-medios para un cuerpo cálido y cuadrado. |
| **Presence** | Realza los medios-agudos para claridad y presencia. |
| **Telephone** | Una banda estrecha de rango medio. Un sonido delgado, tipo teléfono. |
| **Wah** | Un pico muy estrecho y resonante. Barre el centro para un efecto wah. |

### Notch (elimina una banda estrecha)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Frequency** | Establece la frecuencia que elimina el filtro. Todo lo de arriba y abajo pasa. Sintonízalo sobre un zumbido o una resonancia para recortarlo. | 20 Hz a 20 kHz (60 Hz) |
| **Resonance** | Controla cuán ancho es el corte. Valores bajos ahuecan un rango amplio; súbelo para quitar solo una banda puntual y dejar el resto intacto. | 0.1 a 10 (8.0) |

| Preajuste | Qué hace |
|---|---|
| **Mains Hum 60** | Elimina el zumbido eléctrico de 60 Hz (red eléctrica norteamericana). Un punto de partida neutro. |
| **Mains Hum 50** | Elimina el zumbido eléctrico de 50 Hz (red europea y otras). |
| **Rumble** | Recorta un retumbe o resonancia de baja frecuencia sin adelgazar todo el extremo grave. |
| **Mud** | Ahueca la turbiedad de los graves-medios para un sonido más limpio y claro. |
| **Boxy** | Elimina un bocinazo cuadrado del rango medio. |
| **Harsh** | Domestica un pico áspero y penetrante en los medios-agudos. |

### Peaking (banda de EQ paramétrica)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Frequency** | El centro de la banda a reforzar o recortar. Barre para encontrar la frecuencia que quieres moldear. | 20 Hz a 20 kHz (1 kHz) |
| **Gain** | Cuánto reforzar o recortar en el centro. Positivo realza la banda; negativo la ahueca. | -15 a +15 dB (0) |
| **Q factor** | Establece cuán ancha es la banda. Valores bajos moldean un área amplia; valores altos estrechan para cambios quirúrgicos y puntuales. | 0.1 a 10 (1.0) |

| Preajuste | Qué hace |
|---|---|
| **Presence** | Un realce amplio de medios-agudos para claridad y presencia. Un punto de partida neutro. |
| **Warmth** | Un realce amplio de graves-medios que añade cuerpo y calidez. |
| **Vocal Boost** | Realza el rango vocal central para traer las voces al frente. |
| **Cut Mud** | Ahueca la turbiedad cuadrada de los graves-medios para un sonido más limpio. |
| **Tame Harsh** | Un corte estrecho para domesticar un pico áspero y penetrante. |
| **Punch** | Un realce grave que añade pegada e impacto al extremo grave. |
| **Sub Boost** | Un realce profundo en lo más bajo para un peso extra de sub-graves. |
| **Air** | Un realce amplio en la parte más alta para un brillo abierto y aireado. |
| **Clarity** | Realza los medios-agudos para añadir definición y filo. |
| **De-Ess** | Un corte estrecho en el rango de sibilancia para domesticar las S ásperas. |
| **De-Boom** | Recorta una acumulación retumbante de baja frecuencia para un extremo grave más ceñido. |
| **Scoop** | Una caída amplia del rango medio para un tono ahuecado y moderno. |

### Low Shelf (control de graves y refuerzo de graves)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Frequency** | Establece la esquina por debajo de la cual actúa el shelf. Todo lo que está debajo se refuerza o recorta en conjunto. | 20 a 2000 Hz (200) |
| **Gain** | Cuánto subir o bajar el extremo grave. Positivo añade peso y calidez; negativo lo adelgaza. | -15 a +15 dB (0) |

| Preajuste | Qué hace |
|---|---|
| **Warmth** | Un realce suave del extremo grave para calidez y cuerpo. Un punto de partida neutro. |
| **Bass Boost** | Un realce sólido de los graves para peso y pegada. |
| **Fullness** | Llena los graves-medios para un sonido más pleno y redondo. |
| **Trim Bass** | Un corte modesto para aligerar una mezcla cargada de graves. |
| **Cut Lows** | Un corte fuerte para adelgazar o quitar el retumbe del extremo grave. |
| **Big Bottom** | Un gran realce del extremo grave para máximo peso y retumbe. |

### High Shelf (control de agudos)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Frequency** | Establece la esquina por encima de la cual actúa el shelf. Todo lo que está por encima se refuerza o recorta en conjunto. | 1 a 20 kHz (8 kHz) |
| **Gain** | Cuánto subir o bajar el extremo agudo. Positivo añade brillo y aire; negativo suaviza y oscurece. | -15 a +15 dB (0) |

| Preajuste | Qué hace |
|---|---|
| **Presence** | Un realce suave del extremo agudo para claridad y detalle. Un punto de partida neutro. |
| **Air** | Abre la parte más alta para un sonido aireado y abierto. |
| **Bright** | Un realce fuerte para un tono nítido, brillante y al frente. |
| **Soften** | Un corte modesto para quitar el filo a los agudos ásperos. |
| **Tame Highs** | Un corte fuerte para oscurecer y suavizar un sonido demasiado brillante. |
| **Sparkle** | Un gran realce de la parte más alta para máximo destello y brillo. |

### Soft Clip (saturación cálida)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Drive** | Empuja la señal con más fuerza hacia el modelador de onda. Cantidades bajas añaden calidez suave; cantidades altas redondean los picos en una saturación gruesa y áspera. | 0 a 40 dB (0) |

| Preajuste | Qué hace |
|---|---|
| **Warm** | Un toque de drive para una calidez suave, estilo analógico. |
| **Drive** | Saturación perceptible que engrosa y colorea el sonido. |
| **Crunch** | Drive fuerte con un filo crujiente audible. |
| **Fuzz** | Distorsión gruesa y difusa. Los picos quedan muy aplastados. |
| **Destroy** | Drive máximo. Aspereza agresiva y totalmente saturada. |

### Bit Crusher (lo-fi retro)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Bit depth** | Establece cuántos bits describen cada muestra. Menos bits significan pasos más gruesos y más ruido de cuantización, para un sonido digital crujiente y áspero. | 1 a 16 bits (16) |
| **Sample rate** | Submuestrea el audio. Al cien por cien la frecuencia queda intacta; bájalo para mantener cada muestra más tiempo, apagando los agudos y añadiendo un filo áspero y con aliasing. | 1% a 100% (100%) |

| Preajuste | Qué hace |
|---|---|
| **Vintage** | Una caída sutil de calidad, como un sampler digital temprano. |
| **LoFi** | Lo-fi clásico de 8 bits y media frecuencia. Granuloso y retro. |
| **Crunch** | Aplastamiento más fuerte con un filo crujiente audible. |
| **Gritty** | Grueso y áspero. Los pasos entre niveles son evidentes. |
| **Destroy** | Reducción extrema. Áspero, roto, apenas reconocible. |

### Ring Modulator (tonos metálicos y robóticos)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Carrier** | Establece la frecuencia del tono por el que se multiplica la señal. Unos pocos hercios dan un trémolo ondulante; frecuencias más altas añaden armónicos metálicos, tipo campana y robóticos. | 1 a 4000 Hz (440) |
| **Mix** | Mezcla el sonido modulado con el original. Al cero por ciento oyes solo la señal seca; al cien por cien solo el tono totalmente modulado. | 0% a 100% (0%) |

| Preajuste | Qué hace |
|---|---|
| **Tremolo** | Una portadora muy baja lo convierte en un trémolo de amplitud, ondulando el volumen. |
| **Robot** | Una portadora media añade armónicos metálicos para un clásico efecto de voz de robot. |
| **Metallic** | Armónicos densos e inarmónicos para un tono áspero y metálico. |
| **Bell** | Una portadora más alta da un tañido brillante, tipo campana. |
| **Alien** | Totalmente húmedo con una portadora alta. Extremo, alienígena, apenas reconocible. |

### Tremolo (oscilación de volumen)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Rate** | Establece con qué rapidez pulsa el volumen. Velocidades más lentas dan un balanceo suave; las más rápidas dan un tartamudeo veloz. | 0.1 a 20 Hz (5) |
| **Depth** | Establece cuánto baja el volumen en cada pulso. Al cero por ciento el nivel es estable; al cien por cien baja hasta el silencio total. | 0% a 100% (0%) |

| Preajuste | Qué hace |
|---|---|
| **Gentle** | Un balanceo lento y superficial. Movimiento sutil sin llamar la atención. |
| **Classic** | El clásico trémolo de amplificador: una velocidad media y una profundidad moderada. |
| **Deep** | Un pulso fuerte y profundo que casi baja al silencio en cada ciclo. |
| **Fast** | Un aleteo rápido para una sensación reluciente y nerviosa. |
| **Chop** | Rápido y a plena profundidad. Un corte duro y tartamudeante. |

### Delay (eco)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Time** | Establece la pausa antes de cada eco. Tiempos cortos dan un slapback ceñido; tiempos más largos separan más las repeticiones. | 0.01 a 2 s (0.25) |
| **Feedback** | Establece cuánto de cada eco se realimenta. Valores bajos dan una única repetición; valores más altos construyen una serie larga y arrastrada de ecos. | 0 a 0.95 (0.4) |
| **Mix** | Mezcla los ecos con el original. Al cero por ciento oyes solo la señal seca; al cien por cien solo los ecos. | 0% a 100% (0%) |

| Preajuste | Qué hace |
|---|---|
| **Slapback** | Un único eco corto, ceñido contra el original. Rockabilly y doblaje vocal. |
| **Echo** | El eco clásico: una repetición clara con unas pocas colas arrastradas. |
| **Ping** | Una repetición rápida y rebotante que añade movimiento rítmico. |
| **Ambient** | Repeticiones más largas y suaves que se diluyen en una cola espaciosa. |
| **Dub** | Alta realimentación para cascadas largas y dub de eco. |
| **Cavern** | Repeticiones largas y profundas, como sonido resonando por un espacio enorme. |

### Stereo Width (estrecha o ensancha)

| Control | Qué hace | Rango (predeterminado) |
|---|---|---|
| **Width** | Estrecha o ensancha la imagen estéreo. El cero por ciento colapsa a mono, el cien por cien la deja intacta, y valores más altos empujan los lados más lejos. Solo afecta a las pistas estéreo en el destino de Todos los canales. | 0% a 200% (100%) |

| Preajuste | Qué hace |
|---|---|
| **Wide** | Un ensanchamiento suave que abre la imagen estéreo. Un punto de partida neutro. |
| **Wider** | Un ensanche más fuerte para un campo estéreo grande e inmersivo. |
| **Max** | Ancho máximo. Muy amplio, pero cuidado con los problemas de compatibilidad mono. |
| **Narrow** | Junta los lados para una imagen más ceñida y centrada. |
| **Focused** | Casi centrado, con solo un toque de estéreo. |
| **Mono** | Totalmente colapsado a mono. Ambos altavoces reproducen la misma señal. |

## Cómo funciona todo por dentro (versión simple)

- **Motores:** eliges uno en Ajustes > Reproductor de audio > Motor de reproducción: **Standard** (sistema), **Universal** (FFmpeg) o **Sound FX** (el **motor BASS™** de [Un4seen Developments](https://www.un4seen.com/)). El motor que elijas decide qué formatos se reproducen, y los efectos, el ecualizador y la cadena de DSP funcionan solo en el motor Sound FX.
- **Formatos:** el motor BASS™ añade FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus y música de módulos (tracker) además de los formatos del sistema y de FFmpeg.
- **Efectos:** el ecualizador, el compresor y la mayoría de los efectos usan los complementos de efectos de BASS™. Freeverb es la reverb Freeverb. Chorus, Flanger y Distortion usan efectos clásicos estilo DirectX con sus propios controles.
- **Normalización de volumen:** un nivelador de sonoridad **EBU R128** en vivo (el estándar de sonoridad usado en la radiodifusión y el streaming).
- **Crossfeed:** el crossfeed **bs2b (Bauer)**, ejecutado dentro del motor BASS™.
- **Cadena de DSP:** tus bloques personalizados, aplicados en el orden exacto que establezcas, en todos los canales o solo en un lado.
- **Salida:** puedes configurar la frecuencia de muestreo, el número de canales y el tamaño del búfer para que coincidan con tu equipo.

Como todo esto funciona en vivo mientras suena la música, los efectos:

- Funcionan en **tiempo real** con todo, incluidos archivos en la nube, transmisiones y música de módulos.
- **Nunca cambian ni vuelven a guardar** tus archivos. Apaga un efecto y el original vuelve.
- **Recuerdan tus ajustes** para cada efecto.
- Se pueden **mezclar y combinar** libremente, ya que cada uno es independiente.

## Recetas simples para probar

**Escucha cotidiana**

- **Más graves, con limpieza:** Ecualizador > Bass Booster, luego baja el Preamplificador de 1 a 2 dB. O añade un Low Shelf de DSP en Bass Boost.
- **Volumen parejo en una lista de reproducción mixta:** Normalización de volumen > Standard, más Compressor > Soft.
- **Pulido general suave:** Compressor > Transparent, más Normalización de volumen > Light.
- **Voces más claras:** Ecualizador > Vocal Booster, o un bloque Peaking de DSP en Vocal Boost.
- **Sonido más pleno en altavoces pequeños de teléfono:** Ecualizador > Small Speakers.

**Auriculares**

- **Más agradable y menos fatigoso en auriculares:** Crossfeed > Chu Moy o Jan Meier.
- **Sonido más amplio en auriculares:** Stereo Width de DSP > Wide, más Crossfeed > Chu Moy.
- **Arregla los discos de paneo extremo de los años 1960 y 1970:** Crossfeed > Vintage Stereo.
- **Un poco de aire y espacio:** Freeverb > Ambience, mantenido bajo, más Crossfeed > Subtle.

**Momentos tranquilos y audio hablado**

- **Escucha silenciosa nocturna:** Normalización de volumen > Night, más Compressor > Late Night.
- **Podcasts y audiolibros:** Compressor > Voice / Podcast, más Ecualizador > Spoken Word.
- **El sonido más fuerte y parejo en un coche ruidoso:** Normalización de volumen > Strong, más Compressor > Heavy.

**Solucionar problemas**

- **Domestica una grabación áspera y brillante:** Ecualizador > Treble Reducer, o un bloque Peaking de DSP en Tame Harsh.
- **Eliminar el zumbido eléctrico:** cadena de DSP > Notch > Mains Hum 60 (o Mains Hum 50 en Europa).
- **Graves más ceñidos y limpios:** High Pass de DSP > Tighten, para recortar el extremo grave retumbante.
- **Menos retumbe en una mezcla cargada de graves:** Low Shelf de DSP > Trim Bass, o Peaking > De-Boom.

**Creativo y divertido**

- **Sensación cálida y espaciosa:** Freeverb > Hall, mantenido bajo.
- **Guitarras de ensueño y espaciosas:** Chorus > Wide, más Echo > Long.
- **Lo-fi retro:** cadena de DSP > Bit Crusher (LoFi) hacia Soft Clip (Warm).
- **Movimiento funky en pistas electrónicas:** Auto Wah > Funky, o Phaser > Fast.
- **Clásico barrido de avión a reacción:** Flanger > Jet.

## Preguntas frecuentes

{{% details title="¿Qué motor de sonido usa Flacbox?" closed="true" %}}
Eliges un Motor de reproducción en Ajustes > Reproductor de audio: Standard (el motor del sistema de Apple), Universal (el motor FFmpeg) o Sound FX (el motor BASS™ de Un4seen Developments, un4seen.com). El motor que elijas decide qué formatos de archivo se reproducen. Sound FX es el que reproduce formatos adicionales como FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus y música MOD o tracker, y es el único motor que ofrece los efectos en vivo, el ecualizador de 10 bandas y la cadena de DSP. Para usar los efectos, configura el Motor de reproducción en Sound FX.
{{% /details %}}

{{% details title="¿Puede Flacbox reproducir MOD, XM, IT y otra música tracker o de módulos?" closed="true" %}}
Sí. El motor BASS™ tiene un reproductor de módulos integrado que carga archivos MOD, XM, IT, S3M, MTM, UMX y MO3 y reconstruye la canción en vivo a partir de sus patrones y sonidos de instrumentos, tal como está destinada a reproducirse la música tracker. Los reproductores normales de iPhone no pueden hacer esto. Los efectos y el ecualizador también funcionan con la música de módulos.
{{% /details %}}

{{% details title="¿Admite Flacbox archivos DSD y de alta resolución?" closed="true" %}}
Sí. Flacbox reproduce archivos DSD (DSF y DFF) a través del motor BASS™ usando DSD sobre PCM para que funcionen en hardware de salida normal, además de FLAC, WavPack, Monkey's Audio (APE), Musepack y TrueAudio para la reproducción sin pérdida.
{{% /details %}}

{{% details title="¿Qué efectos de sonido tiene Flacbox?" closed="true" %}}
Un ecualizador de 10 bandas, Normalización de volumen, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate y Crossfeed, además de una cadena de DSP que construyes tú mismo con filtros, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay y stereo width. Cada uno es independiente y se puede combinar con los demás.
{{% /details %}}

{{% details title="¿Qué es un preajuste?" closed="true" %}}
Un preajuste es un ajuste ya preparado para un efecto. En lugar de mover los controles deslizantes tú mismo, tocas un preajuste y el sonido cambia para coincidir. Cada efecto en Flacbox tiene varios preajustes, y esta guía enumera lo que hace cada uno. Si mueves un control deslizante tras elegir un preajuste, el efecto muestra «Manual» para indicarte que ahora usa tus propios valores.
{{% /details %}}

{{% details title="¿Cómo abro los efectos de audio en Flacbox?" closed="true" %}}
Abre el reproductor Now Playing, toca el botón ⋯ (Más) y elige Efectos de audio. O ve a Ajustes > Reproductor de audio > Efectos de audio. Toca un efecto, enciende su interruptor y elige un preajuste, o abre los controles deslizantes para ajustar con precisión.
{{% /details %}}

{{% details title="¿Dónde está el ecualizador y cuáles son los mejores ajustes?" closed="true" %}}
Ve a Ajustes > Reproductor de audio > Ecualizador de audio. Tiene 10 bandas de 32 Hz a 16 kHz, cada una de -12 a +12 dB, más un Preamplificador de -24 a +24 dB y 22 preajustes. Para más graves, usa Bass Booster. Para voces más claras, usa Vocal Booster o Pop. Para un sonido más brillante, usa Treble Booster. Luego ajusta bandas individuales a tu gusto.
{{% /details %}}

{{% details title="¿Cómo refuerzo los graves en Flacbox?" closed="true" %}}
Dos formas fáciles. En el Ecualizador de audio, elige Bass Booster (o sube las bandas de 32 Hz y 64 Hz unos pocos dB). O, en Procesamiento de señal, añade un bloque Low Shelf configurado en Bass Boost. En ambos casos, baja el Preamplificador o añade un bloque Gain de 1 a 2 dB para que los graves se mantengan limpios y no se distorsionen.
{{% /details %}}

{{% details title="¿Qué preajuste de ecualizador es mejor para mi música?" closed="true" %}}
Rock y Electronic añaden energía con graves y agudos fuertes. Acoustic, Jazz y Classical se mantienen cálidos y naturales. Pop y Vocal Booster empujan las voces al frente. Bass Booster y Hip-Hop añaden peso. Deep y Loudness suenan más plenos a bajo volumen. Empieza con el que coincida con tu género, luego ajusta con precisión.
{{% /details %}}

{{% details title="¿Qué es la Normalización de volumen y en qué se diferencia de ReplayGain?" closed="true" %}}
Hace que cada pista se reproduzca aproximadamente a la misma sonoridad. Mide la sonoridad real usando el estándar EBU R128 (en LUFS, como los servicios de streaming) y ajusta cada pista hacia tu objetivo, con un límite de refuerzo máximo. A diferencia de ReplayGain, no necesita etiquetas en tus archivos y funciona con cualquier fuente, en vivo, sin cambiar el audio. Preajustes: Light, Standard, Strong y Night.
{{% /details %}}

{{% details title="¿Qué es Crossfeed y debería usarlo?" closed="true" %}}
Crossfeed mezcla un poco de los canales izquierdo y derecho para que los auriculares se sientan más como altavoces reales y menos como si el sonido estuviera atrapado en tu cabeza. Es solo para auriculares, así que apágalo para los altavoces. Flacbox usa el método bs2b (Bauer), con preajustes como Chu Moy y Jan Meier.
{{% /details %}}

{{% details title="¿Cuál es la diferencia entre el Compressor y la Normalización de volumen?" closed="true" %}}
La Normalización de volumen iguala la sonoridad entre distintas canciones. El Compressor empareja las partes fuertes y silenciosas dentro de una misma canción. Resuelven problemas diferentes y funcionan bien juntos, especialmente en un coche o en un lugar ruidoso.
{{% /details %}}

{{% details title="¿Qué es la cadena de Procesamiento de señal (DSP)?" closed="true" %}}
Es un rack que construyes tú mismo en Ajustes > Reproductor de audio > Procesamiento de señal. Añade bloques como filtros, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay y stereo width, ponlos en cualquier orden, enciende o apaga cada uno, y dirige la cadena a todos los canales, el izquierdo o el derecho. Como el orden importa, puedes diseñar exactamente el sonido que quieres.
{{% /details %}}

{{% details title="¿Cuál es la diferencia entre el Ecualizador, los efectos y la cadena de DSP?" closed="true" %}}
El Ecualizador es un control de tono simple de 10 bandas. Los Efectos de audio son herramientas ya preparadas (compresor, reverb, echo, etc.) con preajustes. La cadena de DSP es donde construyes tu propio orden de efectos a partir de bloques individuales. Puedes ejecutar los tres al mismo tiempo.
{{% /details %}}

{{% details title="¿Los efectos cambian o dañan mis archivos de música?" closed="true" %}}
No. Todo se aplica en vivo mientras suena la música. Tus archivos nunca se cambian ni se vuelven a guardar. Apaga un efecto y el sonido original vuelve de inmediato.
{{% /details %}}

{{% details title="¿Puedo usar más de un efecto al mismo tiempo?" closed="true" %}}
Sí. Cada efecto tiene su propio interruptor y no hay un interruptor maestro, así que cualquier combinación funciona. Por ejemplo, Normalización de volumen más Compressor para una escucha pareja, o Freeverb más Crossfeed en auriculares, con el ecualizador encima.
{{% /details %}}

{{% details title="¿Por qué están atenuados los controles del efecto?" closed="true" %}}
El efecto está apagado. Enciende su interruptor en la parte superior del editor para usar los controles. Cada efecto está apagado de forma predeterminada.
{{% /details %}}

{{% details title="¿Qué significa la etiqueta Manual?" closed="true" %}}
Significa que moviste un control deslizante fuera de un preajuste, así que el efecto ahora usa tus propios valores personalizados en lugar de un preajuste con nombre. Cada control deslizante tiene un botón de reinicio, y elegir un preajuste de nuevo reemplaza tus valores manuales.
{{% /details %}}

{{% details title="¿Puedo guardar y compartir mis preajustes de ecualizador?" closed="true" %}}
Sí. Además de los 22 preajustes integrados, puedes crear los tuyos, reordenarlos y exportarlos o importarlos para llevar tus ajustes a otro dispositivo.
{{% /details %}}

{{% details title="¿Funcionan los efectos con CarPlay, streaming y reproducción en segundo plano?" closed="true" %}}
Sí. Los efectos funcionan dentro del motor BASS™, así que se aplican a archivos locales, unidades en la nube, servidores multimedia, transmisiones y música de módulos, y siguen funcionando durante CarPlay y la reproducción en segundo plano.
{{% /details %}}

{{% details title="¿Puedo cambiar la calidad de salida de audio?" closed="true" %}}
Sí. En Ajustes > Reproductor de audio puedes configurar la frecuencia de muestreo de salida, el número de canales y el tamaño del búfer para que coincidan con tus auriculares, altavoces o DAC.
{{% /details %}}

{{% details title="¿Cuál es una buena configuración inicial para auriculares?" closed="true" %}}
Activa la Normalización de volumen (Standard), añade un Compressor ligero (Soft), elige un preajuste de ecualizador que te guste y activa Crossfeed (Chu Moy o Jan Meier). Deja apagados la reverb, el echo y la distorsión a menos que quieras un sonido creativo.
{{% /details %}}

---

*BASS es una marca comercial de Un4seen Developments Ltd. Consulta [un4seen.com](https://www.un4seen.com/). Crossfeed usa el algoritmo bs2b (Bauer stereophonic-to-binaural); consulta la [página del proyecto bs2b](https://bs2b.sourceforge.net/).*
