---
title: "Tagveldtoewijzingen"
date: 2020-02-01
description: "Verken de volledige lijst van audiotagvelden die worden ondersteund door de Evertag-app, inclusief interne veldnamen en toewijzingen over de belangrijkste metadataformaten."
keywords: ["audiometadata", "audiotags", "ID3-tags", "Vorbis Comments", "MP4-tags", "ASF-metadata", "Evertag-tagondersteuning", "muziekbestandstags", "audiotagformaten"]
tags: ["Evertag", "audiotags", "metadata", "ID3", "Vorbis", "MP4", "ASF"]
cascade:
  type: docs
---


Evertag ondersteunt een breed scala aan audiotagvelden die worden gebruikt in populaire formaten zoals ID3, MP4, Vorbis Comments en ASF.  

Deze referentiegids beschrijft elk tagveld, de interne naam in Evertag en hoe het wordt toegewezen aan verschillende metadatastandaarden.   

Gebruik het om beter te begrijpen hoe Evertag taggegevens voor uw muziekbibliotheek organiseert en bewerkt.

## AcoustID: Vingerafdruk
- **APE (ape)**: Acoustid Fingerprint, ACOUSTID_FINGERPRINT
- **ASF/Windows Media (asf, wma)**: Acoustid/Fingerprint
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:Acoustid Fingerprint
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:Acoustid Fingerprint
- **Vorbis Comments (flac, ogg)**: ACOUSTID_FINGERPRINT

## AcoustID: Identificatie
- **APE (ape)**: Acoustid Id, ACOUSTID_ID
- **ASF/Windows Media (asf, wma)**: Acoustid/Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:Acoustid Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:Acoustid Id
- **Vorbis Comments (flac, ogg)**: ACOUSTID_ID

## Album
- **APE (ape)**: Album, ALBUM
- **ASF/Windows Media (asf, wma)**: WM/AlbumTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TALB
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©alb
- **Vorbis Comments (flac, ogg)**: ALBUM

## Albumartiest
- **APE (ape)**: Album Artist, ALBUM ARTIST, ALBUMARTIST
- **ASF/Windows Media (asf, wma)**: WM/AlbumArtist
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE2
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: aART
- **Vorbis Comments (flac, ogg)**: ALBUMARTIST

## Sorteervolgorde albumartiest
- **APE (ape)**: Album Artist Sort, ALBUMARTISTSORT
- **ASF/Windows Media (asf, wma)**: WM/AlbumArtistSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSO2
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soaa
- **Vorbis Comments (flac, ogg)**: ALBUMARTISTSORT

## Albumhoes
- **APE (ape)**: COVER ART (FRONT)
- **ASF/Windows Media (asf, wma)**: WM/Picture
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: APIC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: covr
- **Vorbis Comments (flac, ogg)**: METADATA_BLOCK_PICTURE, COVERART

## Sorteervolgorde album
- **APE (ape)**: Album Sort, ALBUMSORT
- **ASF/Windows Media (asf, wma)**: WM/AlbumSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOA
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soal
- **Vorbis Comments (flac, ogg)**: ALBUMSORT

## Arrangeur
- **APE (ape)**: Arranger, ARRANGER
- **ASF/Windows Media (asf, wma)**: WM/Arranger
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:arranger
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ARRANGER

## Artiest
- **APE (ape)**: Artist, ARTIST
- **ASF/Windows Media (asf, wma)**: Author
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE1
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©ART
- **Vorbis Comments (flac, ogg)**: ARTIST

## Sorteervolgorde artiest
- **APE (ape)**: Artist Sort, ARTISTSORT
- **ASF/Windows Media (asf, wma)**: WM/ArtistSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soar
- **Vorbis Comments (flac, ogg)**: ARTISTSORT

## Artiesten
- **APE (ape)**: Artists, ARTISTS
- **ASF/Windows Media (asf, wma)**: WM/ARTISTS
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:ARTISTS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:ARTISTS
- **Vorbis Comments (flac, ogg)**: ARTISTS

## ASIN
- **APE (ape)**: ASIN
- **ASF/Windows Media (asf, wma)**: ASIN
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:ASIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:ASIN
- **Vorbis Comments (flac, ogg)**: ASIN

## Streepjescode
- **APE (ape)**: Barcode, BARCODE
- **ASF/Windows Media (asf, wma)**: WM/Barcode
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:BARCODE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:BARCODE
- **Vorbis Comments (flac, ogg)**: BARCODE

## Beats per minuut
- **APE (ape)**: BPM
- **ASF/Windows Media (asf, wma)**: WM/BeatsPerMinute
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TBPM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: tmpo
- **Vorbis Comments (flac, ogg)**: BPM

## Catalognummer
- **APE (ape)**: CatalogNumber, Catalog Number, Catalog, CATALOGNUMBER
- **ASF/Windows Media (asf, wma)**: WM/CatalogNo
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:CATALOGNUMBER
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:CATALOGNUMBER
- **Vorbis Comments (flac, ogg)**: CATALOGNUMBER

## Opmerking
- **APE (ape)**: Comment, COMMENT
- **ASF/Windows Media (asf, wma)**: Comment
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: COMM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©cmt
- **Vorbis Comments (flac, ogg)**: COMMENT

## Compilatie
- **APE (ape)**: Compilation, COMPILATION
- **ASF/Windows Media (asf, wma)**: WM/IsCompilation
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCMP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: cpil
- **Vorbis Comments (flac, ogg)**: COMPILATION

## Componist
- **APE (ape)**: Composer, COMPOSER
- **ASF/Windows Media (asf, wma)**: WM/Composer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCOM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©wrt
- **Vorbis Comments (flac, ogg)**: COMPOSER

## Sorteervolgorde componist
- **APE (ape)**: Composer Sort, COMPOSERSORT
- **ASF/Windows Media (asf, wma)**: WM/ComposerSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soco
- **Vorbis Comments (flac, ogg)**: COMPOSERSORT

## Dirigent
- **APE (ape)**: Conductor, CONDUCTOR
- **ASF/Windows Media (asf, wma)**: WM/Conductor
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE3
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:CONDUCTOR, ©con
- **Vorbis Comments (flac, ogg)**: CONDUCTOR

## Inhoudsgroep
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: WM/ContentGroupDescription
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIT1
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©grp
- **Vorbis Comments (flac, ogg)**: N/A

## Auteursrecht
- **APE (ape)**: Copyright, COPYRIGHT
- **ASF/Windows Media (asf, wma)**: Copyright
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCOP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: cprt
- **Vorbis Comments (flac, ogg)**: COPYRIGHT

## Beschrijving
- **APE (ape)**: Description, DESCRIPTION
- **ASF/Windows Media (asf, wma)**: Description
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: N/A
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: desc
- **Vorbis Comments (flac, ogg)**: DESCRIPTION

## Regisseur
- **APE (ape)**: Director, DIRECTOR
- **ASF/Windows Media (asf, wma)**: WM/Director
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:DIRECTOR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©dir
- **Vorbis Comments (flac, ogg)**: DIRECTOR

## Schijfnummer
- **APE (ape)**: Disc, DISC
- **ASF/Windows Media (asf, wma)**: WM/PartOfSet
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPOS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: disk
- **Vorbis Comments (flac, ogg)**: DISCNUMBER, DISCNUM

## Schijfondertitel
- **APE (ape)**: DiscSubtitle, Disc Subtitle, DISCSUBTITLE
- **ASF/Windows Media (asf, wma)**: WM/SetSubTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSST
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:DISCSUBTITLE
- **Vorbis Comments (flac, ogg)**: DISCSUBTITLE

## Totaal aantal schijven
- **APE (ape)**: Disc, DISC
- **ASF/Windows Media (asf, wma)**: WM/PartOfSet
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPOS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: disk
- **Vorbis Comments (flac, ogg)**: DISCTOTAL, TOTALDISCS

## Gecodeerd door
- **APE (ape)**: EncodedBy, Encoded By, ENCODEDBY
- **ASF/Windows Media (asf, wma)**: WM/EncodedBy
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TENC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©too
- **Vorbis Comments (flac, ogg)**: ENCODEDBY, ENCODED-BY

## Encoderinstellingen
- **APE (ape)**: EncoderSettings, Encoder Settings, ENCODERSETTINGS
- **ASF/Windows Media (asf, wma)**: WM/EncodingSettings
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSSE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ENCODING, ENCODERSETTINGS, ENCODER SETTINGS

## Coderingstijd
- **APE (ape)**: EncodingTime, Encoding Time, ENCODINGTIME
- **ASF/Windows Media (asf, wma)**: WM/EncodingTime
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDEN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ENCODINGTIME

## Technicus
- **APE (ape)**: Engineer, ENGINEER
- **ASF/Windows Media (asf, wma)**: WM/Engineer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:engineer
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:ENGINEER
- **Vorbis Comments (flac, ogg)**: ENGINEER

## Bestandseigenaar
- **APE (ape)**: FileOwner, File Owner, FILEOWNER
- **ASF/Windows Media (asf, wma)**: FILEOWNER
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOWN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: FILEOWNER

## Bestandstype
- **APE (ape)**: FileType, File Type, FILETYPE
- **ASF/Windows Media (asf, wma)**: FILETYPE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TFLT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: FILETYPE

## Genre
- **APE (ape)**: Genre, GENRE
- **ASF/Windows Media (asf, wma)**: WM/Genre
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCON
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©gen, gnre
- **Vorbis Comments (flac, ogg)**: GENRE

## Groepering
- **APE (ape)**: Grouping, GROUPING
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: GRP1
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: GROUPING

## Begintoets
- **APE (ape)**: KEY
- **ASF/Windows Media (asf, wma)**: WM/InitialKey
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TKEY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:initialkey
- **Vorbis Comments (flac, ogg)**: KEY

## Betrokken personen
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: N/A

## ISRC
- **APE (ape)**: ISRC
- **ASF/Windows Media (asf, wma)**: WM/ISRC
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSRC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:ISRC
- **Vorbis Comments (flac, ogg)**: ISRC

## Taal
- **APE (ape)**: Language, LANGUAGE
- **ASF/Windows Media (asf, wma)**: WM/Language
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TLAN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LANGUAGE
- **Vorbis Comments (flac, ogg)**: LANGUAGE

## Lengte
- **APE (ape)**: Length, LENGTH
- **ASF/Windows Media (asf, wma)**: LENGTH
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TLEN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: LENGTH

## Licentie
- **APE (ape)**: License, LICENSE
- **ASF/Windows Media (asf, wma)**: LICENSE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:LICENSE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LICENSE
- **Vorbis Comments (flac, ogg)**: LICENSE

## Tekstschrijver
- **APE (ape)**: Lyricist, LYRICIST
- **ASF/Windows Media (asf, wma)**: WM/Writer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TEXT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LYRICIST
- **Vorbis Comments (flac, ogg)**: LYRICIST

## Inhoudswaarschuwingsbeoordeling
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:ITUNESADVISORY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: rtng
- **Vorbis Comments (flac, ogg)**: ITUNESADVISORY

## Niet-gesynchroniseerde songteksten
- **APE (ape)**: Lyrics, LYRICS
- **ASF/Windows Media (asf, wma)**: WM/Lyrics
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: USLT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©lyr
- **Vorbis Comments (flac, ogg)**: LYRICS

## Mediatype
- **APE (ape)**: Media, MEDIA
- **ASF/Windows Media (asf, wma)**: WM/Media
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMED
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MEDIA
- **Vorbis Comments (flac, ogg)**: MEDIA

## Mix DJ
- **APE (ape)**: DJMixer, DJMIXER
- **ASF/Windows Media (asf, wma)**: WM/DJMixer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:DJ-mix
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:DJMIXER
- **Vorbis Comments (flac, ogg)**: DJMIXER

## Mixer
- **APE (ape)**: Mixer, MIXER
- **ASF/Windows Media (asf, wma)**: WM/Mixer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:mix
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MIXER
- **Vorbis Comments (flac, ogg)**: MIXER

## Stemming
- **APE (ape)**: Mood, MOOD
- **ASF/Windows Media (asf, wma)**: WM/Mood
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMOO
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MOOD
- **Vorbis Comments (flac, ogg)**: MOOD

## Bewegingsnaam
- **APE (ape)**: Movement Name, MOVEMENTNAME
- **ASF/Windows Media (asf, wma)**: MOVEMENTNAME
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: MVNM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©mvn
- **Vorbis Comments (flac, ogg)**: MOVEMENTNAME

## Bewegingsnummer
- **APE (ape)**: Movement, MOVEMENT
- **ASF/Windows Media (asf, wma)**: MOVEMENT
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: MVIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©mvi
- **Vorbis Comments (flac, ogg)**: MOVEMENT

## Totaal aantal bewegingen
- **APE (ape)**: Movement Total, MOVEMENTTOTAL
- **ASF/Windows Media (asf, wma)**: MOVEMENTTOTAL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: MVIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©mvc
- **Vorbis Comments (flac, ogg)**: MOVEMENTTOTAL

## MusicBrainz: Albumartiest-ID
- **APE (ape)**: MUSICBRAINZ_ALBUMARTISTID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Artist Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Artist Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Artist Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMARTISTID

## MusicBrainz: Album-ID
- **APE (ape)**: MUSICBRAINZ_ALBUMID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMID

## MusicBrainz: Uitkomstland album
- **APE (ape)**: MUSICBRAINZ_ALBUMRELEASECOUNTRY
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Release Country
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Release Country
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Release Country
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMRELEASECOUNTRY

## MusicBrainz: Albumstatus
- **APE (ape)**: MUSICBRAINZ_ALBUMSTATUS
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Status
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Status
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Status
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMSTATUS

## MusicBrainz: Albumtype
- **APE (ape)**: MUSICBRAINZ_ALBUMTYPE
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Type
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Type
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Type
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMTYPE

## MusicBrainz: Artiest-ID
- **APE (ape)**: MUSICBRAINZ_ARTISTID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Artist Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Artist Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Artist Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ARTISTID

## MusicBrainz: Schijf-ID
- **APE (ape)**: MUSICBRAINZ_DISCID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Disc Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Disc Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Disc Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_DISCID

## MusicBrainz: Origineel album-ID
- **APE (ape)**: MUSICBRAINZ_ORIGINALALBUMID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Original Album Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Original Album Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Original Album Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ORIGINALALBUMID

## MusicBrainz: Originele artiest-ID
- **APE (ape)**: MUSICBRAINZ_ORIGINALARTISTID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Original Artist Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Original Artist Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Original Artist Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ORIGINALARTISTID

## MusicBrainz: Uitgavegroep-ID
- **APE (ape)**: MUSICBRAINZ_RELEASEGROUPID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Release Group Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Release Group Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Release Group Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_RELEASEGROUPID

## MusicBrainz: Uitgave track-ID
- **APE (ape)**: MUSICBRAINZ_RELEASETRACKID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Release Track Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Release Track Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Release Track Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_RELEASETRACKID

## MusicBrainz: Track-ID
- **APE (ape)**: MUSICBRAINZ_TRACKID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Track Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: UFID:http://musicbrainz.org
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Track Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_TRACKID

## MusicBrainz: TRM ID
- **APE (ape)**: MUSICBRAINZ_TRMID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/TRM Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz TRM Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz TRM Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_TRMID

## MusicBrainz: Werk-ID
- **APE (ape)**: MUSICBRAINZ_WORKID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Work Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Work Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Work Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_WORKID

## Muzikantcredits
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMCL
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: N/A

## MusicIP: Vingerafdruk
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicMagic Fingerprint
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:fingerprint
- **Vorbis Comments (flac, ogg)**: N/A

## MusicIP: PUID
- **APE (ape)**: MUSICIP_PUID
- **ASF/Windows Media (asf, wma)**: MusicIP/PUID
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicIP PUID
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicIP PUID
- **Vorbis Comments (flac, ogg)**: N/A

## Verteller
- **APE (ape)**: Narrator, NARRATOR
- **ASF/Windows Media (asf, wma)**: NARRATOR
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:NARRATOR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©nrt
- **Vorbis Comments (flac, ogg)**: NARRATOR

## Eigenaar internetradio
- **APE (ape)**: NETRADIOOWNER
- **ASF/Windows Media (asf, wma)**: WM/RadioStationOwner
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRSO
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: NETRADIOOWNER

## Internetradiostation
- **APE (ape)**: NETRADIOSTATION
- **ASF/Windows Media (asf, wma)**: WM/RadioStationName
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRSN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: NETRADIOSTATION

## Origineel album
- **APE (ape)**: Original Album, ORIGINAL ALBUM, ORIGINALALBUM
- **ASF/Windows Media (asf, wma)**: WM/OriginalAlbumTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOAL
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALALBUM

## Originele artiest
- **APE (ape)**: Original Artist, ORIGINAL ARTIST, ORIGINALARTIST
- **ASF/Windows Media (asf, wma)**: WM/OriginalArtist
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOPE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©ope
- **Vorbis Comments (flac, ogg)**: ORIGINALARTIST

## Originele bestandsnaam
- **APE (ape)**: Original Filename, ORIGINALFILENAME
- **ASF/Windows Media (asf, wma)**: WM/OriginalFilename
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOFN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALFILENAME

## Originele tekstschrijver
- **APE (ape)**: Original Lyricist, ORIGINALLYRICIST
- **ASF/Windows Media (asf, wma)**: WM/OriginalLyricist
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOLY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALLYRICIST

## Originele uitgavedatum
- **APE (ape)**: Original Date, ORIGINALDATE
- **ASF/Windows Media (asf, wma)**: WM/OriginalReleaseDate
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDOR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:originaldate
- **Vorbis Comments (flac, ogg)**: ORIGINALDATE

## Origineel uitgavejaar
- **APE (ape)**: Original Year, ORIGINALYEAR
- **ASF/Windows Media (asf, wma)**: WM/OriginalReleaseYear
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: N/A
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALYEAR

## Uitvoerder
- **APE (ape)**: Performer, PERFORMER
- **ASF/Windows Media (asf, wma)**: WM/Performer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMCL:instrument
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: perf
- **Vorbis Comments (flac, ogg)**: PERFORMER

## Podcast
- **APE (ape)**: Podcast, PODCAST
- **ASF/Windows Media (asf, wma)**: PODCAST
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: PCST
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: pcst
- **Vorbis Comments (flac, ogg)**: PODCAST

## Podcastcategorie
- **APE (ape)**: Podcast Category, PODCASTCATEGORY
- **ASF/Windows Media (asf, wma)**: PODCASTCATEGORY
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCAT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: catg
- **Vorbis Comments (flac, ogg)**: PODCASTCATEGORY

## Podcastbeschrijving
- **APE (ape)**: Podcast Description, PODCASTDESCRIPTION
- **ASF/Windows Media (asf, wma)**: PODCASTDESCRIPTION
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDES
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ldes
- **Vorbis Comments (flac, ogg)**: PODCASTDESCRIPTION

## Podcast-ID
- **APE (ape)**: Podcast Id, PODCASTID
- **ASF/Windows Media (asf, wma)**: PODCASTID
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TGID
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: egid
- **Vorbis Comments (flac, ogg)**: PODCASTID

## Podcasttrefwoorden
- **APE (ape)**: Podcast Keywords, PODCASTKEYWORDS
- **ASF/Windows Media (asf, wma)**: PODCASTKEYWORDS
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TKWD
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: keyw
- **Vorbis Comments (flac, ogg)**: PODCASTKEYWORDS

## Podcast-URL
- **APE (ape)**: Podcast URL, PODCASTURL
- **ASF/Windows Media (asf, wma)**: PODCASTURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WFED
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: purl
- **Vorbis Comments (flac, ogg)**: PODCASTURL

## Producer
- **APE (ape)**: Producer, PRODUCER
- **ASF/Windows Media (asf, wma)**: WM/Producer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:producer
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:PRODUCER, ©prd
- **Vorbis Comments (flac, ogg)**: PRODUCER

## Uitgever
- **APE (ape)**: Publisher, PUBLISHER
- **ASF/Windows Media (asf, wma)**: WM/Publisher
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPUB
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©pub
- **Vorbis Comments (flac, ogg)**: PUBLISHER

## Beoordeling
- **APE (ape)**: Rating, RATING
- **ASF/Windows Media (asf, wma)**: WM/SharedUserRating
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: POPM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: rate
- **Vorbis Comments (flac, ogg)**: RATING

## Platenlabel
- **APE (ape)**: Label, LABEL
- **ASF/Windows Media (asf, wma)**: LABEL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:LABEL
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LABEL, ©lab
- **Vorbis Comments (flac, ogg)**: LABEL

## Uitgaveland
- **APE (ape)**: Release Country, RELEASECOUNTRY
- **ASF/Windows Media (asf, wma)**: RELEASECOUNTRY
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:RELEASECOUNTRY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: RELEASECOUNTRY

## Uitgavestatus
- **APE (ape)**: Release Status, RELEASESTATUS
- **ASF/Windows Media (asf, wma)**: RELEASESTATUS
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:RELEASESTATUS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: RELEASESTATUS

## Uitgavetype
- **APE (ape)**: Release Type, RELEASETYPE
- **ASF/Windows Media (asf, wma)**: RELEASETYPE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:RELEASETYPE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: RELEASETYPE

## Gemixt door
- **APE (ape)**: MixArtist, MIXARTIST
- **ASF/Windows Media (asf, wma)**: WM/ModifiedBy
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE4
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REMIXER
- **Vorbis Comments (flac, ogg)**: REMIXER

## Replay Gain: Albumversterking
- **APE (ape)**: REPLAYGAIN_ALBUM_GAIN
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_ALBUM_GAIN
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_ALBUM_GAIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_ALBUM_GAIN
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_ALBUM_GAIN

## Replay Gain: Albumpiek
- **APE (ape)**: REPLAYGAIN_ALBUM_PEAK
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_ALBUM_PEAK
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_ALBUM_PEAK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_ALBUM_PEAK
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_ALBUM_PEAK

## Replay Gain: Albumbereik
- **APE (ape)**: REPLAYGAIN_ALBUM_RANGE
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_ALBUM_RANGE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_ALBUM_RANGE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_ALBUM_RANGE
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_ALBUM_RANGE

## Replay Gain: Referentievolume
- **APE (ape)**: REPLAYGAIN_REFERENCE_LOUDNESS
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_REFERENCE_LOUDNESS
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_REFERENCE_LOUDNESS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_REFERENCE_LOUDNESS
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_REFERENCE_LOUDNESS

## Replay Gain: Trackversterking
- **APE (ape)**: REPLAYGAIN_TRACK_GAIN
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_TRACK_GAIN
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_TRACK_GAIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_TRACK_GAIN
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_TRACK_GAIN

## Replay Gain: Trackpiek
- **APE (ape)**: REPLAYGAIN_TRACK_PEAK
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_TRACK_PEAK
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_TRACK_PEAK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_TRACK_PEAK
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_TRACK_PEAK

## Replay Gain: Trackbereik
- **APE (ape)**: REPLAYGAIN_TRACK_RANGE
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_TRACK_RANGE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_TRACK_RANGE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_TRACK_RANGE
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_TRACK_RANGE

## Script
- **APE (ape)**: Script, SCRIPT
- **ASF/Windows Media (asf, wma)**: WM/Script
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SCRIPT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:SCRIPT
- **Vorbis Comments (flac, ogg)**: SCRIPT

## Beweging tonen
- **APE (ape)**: Show Movement, SHOWMOVEMENT
- **ASF/Windows Media (asf, wma)**: SHOWMOVEMENT
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SHOWMOVEMENT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: shwm
- **Vorbis Comments (flac, ogg)**: SHOWMOVEMENT

## Shownaam
- **APE (ape)**: Show Name, SHOWNAME
- **ASF/Windows Media (asf, wma)**: SHOWNAME
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SHOWNAME
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: tvsh
- **Vorbis Comments (flac, ogg)**: SHOWNAME

## Sorteervolgorde shownaam
- **APE (ape)**: Show Name Sort, SHOWNAMESORT
- **ASF/Windows Media (asf, wma)**: SHOWNAMESORT
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SHOWNAMESORT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: sosn
- **Vorbis Comments (flac, ogg)**: SHOWNAMESORT

## Ondertitel
- **APE (ape)**: Subtitle, SUBTITLE
- **ASF/Windows Media (asf, wma)**: WM/SubTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIT3
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:SUBTITLE
- **Vorbis Comments (flac, ogg)**: SUBTITLE

## Tracknummer
- **APE (ape)**: Track, TRACK
- **ASF/Windows Media (asf, wma)**: WM/TrackNumber
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRCK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: trkn
- **Vorbis Comments (flac, ogg)**: TRACKNUMBER, TRACKNUM

## Tracktitel
- **APE (ape)**: Title, TITLE
- **ASF/Windows Media (asf, wma)**: Title
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIT2
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©nam
- **Vorbis Comments (flac, ogg)**: TITLE

## Sorteervolgorde tracktitel
- **APE (ape)**: Title Sort, TITLESORT
- **ASF/Windows Media (asf, wma)**: WM/TitleSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: sonm
- **Vorbis Comments (flac, ogg)**: TITLESORT

## Totaal aantal tracks
- **APE (ape)**: Track, TRACK
- **ASF/Windows Media (asf, wma)**: WM/TrackNumber
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRCK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: trkn
- **Vorbis Comments (flac, ogg)**: TRACKTOTAL, TOTALTRACKS

## Website
- **APE (ape)**: Weblink, WEBLINK, WEBSITE
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: N/A
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WEBSITE

## Werktitel
- **APE (ape)**: Work, WORK
- **ASF/Windows Media (asf, wma)**: WM/Work
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:WORK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©wrk
- **Vorbis Comments (flac, ogg)**: WORK

## Schrijver
- **APE (ape)**: Writer, WRITER
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:Writer
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WRITER

## WWW
- **APE (ape)**: WWW
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WXXX
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWW

## WWW: Artiest
- **APE (ape)**: Artist URL, ARTISTURL, WWWARTIST
- **ASF/Windows Media (asf, wma)**: WM/AuthorURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WOAR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©prl
- **Vorbis Comments (flac, ogg)**: WWWARTIST

## WWW: Audiobestand
- **APE (ape)**: File URL, FILEURL, WWWAUDIOFILE
- **ASF/Windows Media (asf, wma)**: WM/AudioFileURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WOAF
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWAUDIOFILE

## WWW: Audiobron
- **APE (ape)**: Source URL, SOURCEURL, WWWAUDIOSOURCE
- **ASF/Windows Media (asf, wma)**: WM/AudioSourceURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WOAS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWAUDIOSOURCE

## WWW: Commerciële informatie
- **APE (ape)**: Commercial Info URL, COMMERCIALINFOURL, WWWCOMMERCIALINFO
- **ASF/Windows Media (asf, wma)**: WM/PromotionURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WCOM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWCOMMERCIALINFO

## WWW: Auteursrecht
- **APE (ape)**: Copyright URL, COPYRIGHTURL, WWWCOPYRIGHT
- **ASF/Windows Media (asf, wma)**: CopyrightURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WCOP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWCOPYRIGHT

## WWW: Betaling
- **APE (ape)**: Buy URL, BUYURL, WWWPAYMENT
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WPAY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWPAYMENT

## WWW: Uitgever
- **APE (ape)**: Publisher URL, PUBLISHERURL, WWWPUBLISHER
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WPUB
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWPUBLISHER

## WWW: Radiopagina
- **APE (ape)**: Radio URL, RADIOURL, WWWRADIOPAGE
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WORS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWRADIOPAGE

## Jaar
- **APE (ape)**: Year, YEAR
- **ASF/Windows Media (asf, wma)**: WM/Year
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDRC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©day
- **Vorbis Comments (flac, ogg)**: DATE, YEAR
