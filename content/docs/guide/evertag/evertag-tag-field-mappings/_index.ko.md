---
title: "태그 필드 매핑"
date: 2020-02-01
description: "내부 필드 이름 및 주요 메타데이터 형식 간의 매핑을 포함하여 Evertag 앱에서 지원하는 오디오 태그 필드의 전체 목록을 살펴보세요."
keywords: ["오디오 메타데이터", "오디오 태그", "ID3 태그", "Vorbis 댓글", "MP4 태그", "ASF 메타데이터", "Evertag 태그 지원", "음악 파일 태그", "오디오 태그 형식"]
tags: ["Evertag", "오디오 태그", "메타데이터", "ID3", "Vorbis", "MP4", "ASF"]
cascade:
  type: docs
---


Evertag는 ID3, MP4, Vorbis Comments, ASF와 같은 인기 형식에서 사용되는 광범위한 오디오 태그 필드를 지원합니다.  

이 참조 가이드는 각 태그 필드, Evertag에서의 내부 이름, 그리고 다양한 메타데이터 표준에 대한 매핑을 설명합니다.   

Evertag가 음악 라이브러리에 대한 태그 데이터를 구성하고 편집하는 방법을 더 잘 이해하기 위해 사용하세요.

## AcoustID: 지문
- **APE (ape)**: Acoustid Fingerprint, ACOUSTID_FINGERPRINT
- **ASF/Windows Media (asf, wma)**: Acoustid/Fingerprint
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:Acoustid Fingerprint
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:Acoustid Fingerprint
- **Vorbis Comments (flac, ogg)**: ACOUSTID_FINGERPRINT

## AcoustID: 식별자
- **APE (ape)**: Acoustid Id, ACOUSTID_ID
- **ASF/Windows Media (asf, wma)**: Acoustid/Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:Acoustid Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:Acoustid Id
- **Vorbis Comments (flac, ogg)**: ACOUSTID_ID

## 앨범
- **APE (ape)**: Album, ALBUM
- **ASF/Windows Media (asf, wma)**: WM/AlbumTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TALB
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©alb
- **Vorbis Comments (flac, ogg)**: ALBUM

## 앨범 아티스트
- **APE (ape)**: Album Artist, ALBUM ARTIST, ALBUMARTIST
- **ASF/Windows Media (asf, wma)**: WM/AlbumArtist
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE2
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: aART
- **Vorbis Comments (flac, ogg)**: ALBUMARTIST

## 앨범 아티스트 정렬 순서
- **APE (ape)**: Album Artist Sort, ALBUMARTISTSORT
- **ASF/Windows Media (asf, wma)**: WM/AlbumArtistSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSO2
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soaa
- **Vorbis Comments (flac, ogg)**: ALBUMARTISTSORT

## 앨범 커버
- **APE (ape)**: COVER ART (FRONT)
- **ASF/Windows Media (asf, wma)**: WM/Picture
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: APIC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: covr
- **Vorbis Comments (flac, ogg)**: METADATA_BLOCK_PICTURE, COVERART

## 앨범 정렬 순서
- **APE (ape)**: Album Sort, ALBUMSORT
- **ASF/Windows Media (asf, wma)**: WM/AlbumSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOA
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soal
- **Vorbis Comments (flac, ogg)**: ALBUMSORT

## 편곡자
- **APE (ape)**: Arranger, ARRANGER
- **ASF/Windows Media (asf, wma)**: WM/Arranger
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:arranger
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ARRANGER

## 아티스트
- **APE (ape)**: Artist, ARTIST
- **ASF/Windows Media (asf, wma)**: Author
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE1
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©ART
- **Vorbis Comments (flac, ogg)**: ARTIST

## 아티스트 정렬 순서
- **APE (ape)**: Artist Sort, ARTISTSORT
- **ASF/Windows Media (asf, wma)**: WM/ArtistSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soar
- **Vorbis Comments (flac, ogg)**: ARTISTSORT

## 아티스트들
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

## 바코드
- **APE (ape)**: Barcode, BARCODE
- **ASF/Windows Media (asf, wma)**: WM/Barcode
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:BARCODE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:BARCODE
- **Vorbis Comments (flac, ogg)**: BARCODE

## 분당 비트 수
- **APE (ape)**: BPM
- **ASF/Windows Media (asf, wma)**: WM/BeatsPerMinute
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TBPM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: tmpo
- **Vorbis Comments (flac, ogg)**: BPM

## 카탈로그 번호
- **APE (ape)**: CatalogNumber, Catalog Number, Catalog, CATALOGNUMBER
- **ASF/Windows Media (asf, wma)**: WM/CatalogNo
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:CATALOGNUMBER
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:CATALOGNUMBER
- **Vorbis Comments (flac, ogg)**: CATALOGNUMBER

## 댓글
- **APE (ape)**: Comment, COMMENT
- **ASF/Windows Media (asf, wma)**: Comment
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: COMM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©cmt
- **Vorbis Comments (flac, ogg)**: COMMENT

## 편집집
- **APE (ape)**: Compilation, COMPILATION
- **ASF/Windows Media (asf, wma)**: WM/IsCompilation
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCMP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: cpil
- **Vorbis Comments (flac, ogg)**: COMPILATION

## 작곡가
- **APE (ape)**: Composer, COMPOSER
- **ASF/Windows Media (asf, wma)**: WM/Composer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCOM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©wrt
- **Vorbis Comments (flac, ogg)**: COMPOSER

## 작곡가 정렬 순서
- **APE (ape)**: Composer Sort, COMPOSERSORT
- **ASF/Windows Media (asf, wma)**: WM/ComposerSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: soco
- **Vorbis Comments (flac, ogg)**: COMPOSERSORT

## 지휘자
- **APE (ape)**: Conductor, CONDUCTOR
- **ASF/Windows Media (asf, wma)**: WM/Conductor
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE3
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:CONDUCTOR, ©con
- **Vorbis Comments (flac, ogg)**: CONDUCTOR

## 콘텐츠 그룹
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: WM/ContentGroupDescription
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIT1
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©grp
- **Vorbis Comments (flac, ogg)**: N/A

## 저작권
- **APE (ape)**: Copyright, COPYRIGHT
- **ASF/Windows Media (asf, wma)**: Copyright
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCOP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: cprt
- **Vorbis Comments (flac, ogg)**: COPYRIGHT

## 설명
- **APE (ape)**: Description, DESCRIPTION
- **ASF/Windows Media (asf, wma)**: Description
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: N/A
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: desc
- **Vorbis Comments (flac, ogg)**: DESCRIPTION

## 감독
- **APE (ape)**: Director, DIRECTOR
- **ASF/Windows Media (asf, wma)**: WM/Director
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:DIRECTOR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©dir
- **Vorbis Comments (flac, ogg)**: DIRECTOR

## 디스크 번호
- **APE (ape)**: Disc, DISC
- **ASF/Windows Media (asf, wma)**: WM/PartOfSet
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPOS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: disk
- **Vorbis Comments (flac, ogg)**: DISCNUMBER, DISCNUM

## 디스크 부제
- **APE (ape)**: DiscSubtitle, Disc Subtitle, DISCSUBTITLE
- **ASF/Windows Media (asf, wma)**: WM/SetSubTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSST
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:DISCSUBTITLE
- **Vorbis Comments (flac, ogg)**: DISCSUBTITLE

## 디스크 총수
- **APE (ape)**: Disc, DISC
- **ASF/Windows Media (asf, wma)**: WM/PartOfSet
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPOS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: disk
- **Vorbis Comments (flac, ogg)**: DISCTOTAL, TOTALDISCS

## 인코딩한 사람
- **APE (ape)**: EncodedBy, Encoded By, ENCODEDBY
- **ASF/Windows Media (asf, wma)**: WM/EncodedBy
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TENC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©too
- **Vorbis Comments (flac, ogg)**: ENCODEDBY, ENCODED-BY

## 인코더 설정
- **APE (ape)**: EncoderSettings, Encoder Settings, ENCODERSETTINGS
- **ASF/Windows Media (asf, wma)**: WM/EncodingSettings
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSSE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ENCODING, ENCODERSETTINGS, ENCODER SETTINGS

## 인코딩 시간
- **APE (ape)**: EncodingTime, Encoding Time, ENCODINGTIME
- **ASF/Windows Media (asf, wma)**: WM/EncodingTime
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDEN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ENCODINGTIME

## 엔지니어
- **APE (ape)**: Engineer, ENGINEER
- **ASF/Windows Media (asf, wma)**: WM/Engineer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:engineer
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:ENGINEER
- **Vorbis Comments (flac, ogg)**: ENGINEER

## 파일 소유자
- **APE (ape)**: FileOwner, File Owner, FILEOWNER
- **ASF/Windows Media (asf, wma)**: FILEOWNER
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOWN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: FILEOWNER

## 파일 유형
- **APE (ape)**: FileType, File Type, FILETYPE
- **ASF/Windows Media (asf, wma)**: FILETYPE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TFLT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: FILETYPE

## 장르
- **APE (ape)**: Genre, GENRE
- **ASF/Windows Media (asf, wma)**: WM/Genre
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCON
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©gen, gnre
- **Vorbis Comments (flac, ogg)**: GENRE

## 그룹화
- **APE (ape)**: Grouping, GROUPING
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: GRP1
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: GROUPING

## 초기 키
- **APE (ape)**: KEY
- **ASF/Windows Media (asf, wma)**: WM/InitialKey
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TKEY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:initialkey
- **Vorbis Comments (flac, ogg)**: KEY

## 관련된 사람들
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

## 언어
- **APE (ape)**: Language, LANGUAGE
- **ASF/Windows Media (asf, wma)**: WM/Language
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TLAN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LANGUAGE
- **Vorbis Comments (flac, ogg)**: LANGUAGE

## 길이
- **APE (ape)**: Length, LENGTH
- **ASF/Windows Media (asf, wma)**: LENGTH
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TLEN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: LENGTH

## 라이선스
- **APE (ape)**: License, LICENSE
- **ASF/Windows Media (asf, wma)**: LICENSE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:LICENSE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LICENSE
- **Vorbis Comments (flac, ogg)**: LICENSE

## 작사가
- **APE (ape)**: Lyricist, LYRICIST
- **ASF/Windows Media (asf, wma)**: WM/Writer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TEXT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LYRICIST
- **Vorbis Comments (flac, ogg)**: LYRICIST

## 가사 보호자 등급
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:ITUNESADVISORY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: rtng
- **Vorbis Comments (flac, ogg)**: ITUNESADVISORY

## 동기화되지 않은 가사
- **APE (ape)**: Lyrics, LYRICS
- **ASF/Windows Media (asf, wma)**: WM/Lyrics
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: USLT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©lyr
- **Vorbis Comments (flac, ogg)**: LYRICS

## 미디어 유형
- **APE (ape)**: Media, MEDIA
- **ASF/Windows Media (asf, wma)**: WM/Media
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMED
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MEDIA
- **Vorbis Comments (flac, ogg)**: MEDIA

## 믹스 DJ
- **APE (ape)**: DJMixer, DJMIXER
- **ASF/Windows Media (asf, wma)**: WM/DJMixer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:DJ-mix
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:DJMIXER
- **Vorbis Comments (flac, ogg)**: DJMIXER

## 믹서
- **APE (ape)**: Mixer, MIXER
- **ASF/Windows Media (asf, wma)**: WM/Mixer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:mix
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MIXER
- **Vorbis Comments (flac, ogg)**: MIXER

## 분위기
- **APE (ape)**: Mood, MOOD
- **ASF/Windows Media (asf, wma)**: WM/Mood
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMOO
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MOOD
- **Vorbis Comments (flac, ogg)**: MOOD

## 악장 이름
- **APE (ape)**: Movement Name, MOVEMENTNAME
- **ASF/Windows Media (asf, wma)**: MOVEMENTNAME
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: MVNM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©mvn
- **Vorbis Comments (flac, ogg)**: MOVEMENTNAME

## 악장 번호
- **APE (ape)**: Movement, MOVEMENT
- **ASF/Windows Media (asf, wma)**: MOVEMENT
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: MVIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©mvi
- **Vorbis Comments (flac, ogg)**: MOVEMENT

## 악장 총수
- **APE (ape)**: Movement Total, MOVEMENTTOTAL
- **ASF/Windows Media (asf, wma)**: MOVEMENTTOTAL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: MVIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©mvc
- **Vorbis Comments (flac, ogg)**: MOVEMENTTOTAL

## MusicBrainz: 앨범 아티스트 ID
- **APE (ape)**: MUSICBRAINZ_ALBUMARTISTID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Artist Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Artist Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Artist Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMARTISTID

## MusicBrainz: 앨범 ID
- **APE (ape)**: MUSICBRAINZ_ALBUMID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMID

## MusicBrainz: 앨범 발매 국가
- **APE (ape)**: MUSICBRAINZ_ALBUMRELEASECOUNTRY
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Release Country
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Release Country
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Release Country
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMRELEASECOUNTRY

## MusicBrainz: 앨범 상태
- **APE (ape)**: MUSICBRAINZ_ALBUMSTATUS
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Status
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Status
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Status
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMSTATUS

## MusicBrainz: 앨범 유형
- **APE (ape)**: MUSICBRAINZ_ALBUMTYPE
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Album Type
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Album Type
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Album Type
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ALBUMTYPE

## MusicBrainz: 아티스트 ID
- **APE (ape)**: MUSICBRAINZ_ARTISTID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Artist Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Artist Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Artist Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ARTISTID

## MusicBrainz: 디스크 ID
- **APE (ape)**: MUSICBRAINZ_DISCID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Disc Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Disc Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Disc Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_DISCID

## MusicBrainz: 원본 앨범 ID
- **APE (ape)**: MUSICBRAINZ_ORIGINALALBUMID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Original Album Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Original Album Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Original Album Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ORIGINALALBUMID

## MusicBrainz: 원본 아티스트 ID
- **APE (ape)**: MUSICBRAINZ_ORIGINALARTISTID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Original Artist Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Original Artist Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Original Artist Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_ORIGINALARTISTID

## MusicBrainz: 발매 그룹 ID
- **APE (ape)**: MUSICBRAINZ_RELEASEGROUPID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Release Group Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Release Group Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Release Group Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_RELEASEGROUPID

## MusicBrainz: 발매 트랙 ID
- **APE (ape)**: MUSICBRAINZ_RELEASETRACKID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Release Track Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Release Track Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Release Track Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_RELEASETRACKID

## MusicBrainz: 트랙 ID
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

## MusicBrainz: 작품 ID
- **APE (ape)**: MUSICBRAINZ_WORKID
- **ASF/Windows Media (asf, wma)**: MusicBrainz/Work Id
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:MusicBrainz Work Id
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:MusicBrainz Work Id
- **Vorbis Comments (flac, ogg)**: MUSICBRAINZ_WORKID

## 뮤지션 크레딧
- **APE (ape)**: N/A
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMCL
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: N/A

## MusicIP: 지문
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

## 내레이터
- **APE (ape)**: Narrator, NARRATOR
- **ASF/Windows Media (asf, wma)**: NARRATOR
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:NARRATOR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©nrt
- **Vorbis Comments (flac, ogg)**: NARRATOR

## 인터넷 라디오 소유자
- **APE (ape)**: NETRADIOOWNER
- **ASF/Windows Media (asf, wma)**: WM/RadioStationOwner
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRSO
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: NETRADIOOWNER

## 인터넷 라디오 방송국
- **APE (ape)**: NETRADIOSTATION
- **ASF/Windows Media (asf, wma)**: WM/RadioStationName
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRSN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: NETRADIOSTATION

## 원본 앨범
- **APE (ape)**: Original Album, ORIGINAL ALBUM, ORIGINALALBUM
- **ASF/Windows Media (asf, wma)**: WM/OriginalAlbumTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOAL
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALALBUM

## 원본 아티스트
- **APE (ape)**: Original Artist, ORIGINAL ARTIST, ORIGINALARTIST
- **ASF/Windows Media (asf, wma)**: WM/OriginalArtist
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOPE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©ope
- **Vorbis Comments (flac, ogg)**: ORIGINALARTIST

## 원본 파일 이름
- **APE (ape)**: Original Filename, ORIGINALFILENAME
- **ASF/Windows Media (asf, wma)**: WM/OriginalFilename
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOFN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALFILENAME

## 원본 작사가
- **APE (ape)**: Original Lyricist, ORIGINALLYRICIST
- **ASF/Windows Media (asf, wma)**: WM/OriginalLyricist
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TOLY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALLYRICIST

## 원본 발매일
- **APE (ape)**: Original Date, ORIGINALDATE
- **ASF/Windows Media (asf, wma)**: WM/OriginalReleaseDate
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDOR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:originaldate
- **Vorbis Comments (flac, ogg)**: ORIGINALDATE

## 원본 발매 연도
- **APE (ape)**: Original Year, ORIGINALYEAR
- **ASF/Windows Media (asf, wma)**: WM/OriginalReleaseYear
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: N/A
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: ORIGINALYEAR

## 연주자
- **APE (ape)**: Performer, PERFORMER
- **ASF/Windows Media (asf, wma)**: WM/Performer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TMCL:instrument
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: perf
- **Vorbis Comments (flac, ogg)**: PERFORMER

## 팟캐스트
- **APE (ape)**: Podcast, PODCAST
- **ASF/Windows Media (asf, wma)**: PODCAST
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: PCST
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: pcst
- **Vorbis Comments (flac, ogg)**: PODCAST

## 팟캐스트 카테고리
- **APE (ape)**: Podcast Category, PODCASTCATEGORY
- **ASF/Windows Media (asf, wma)**: PODCASTCATEGORY
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TCAT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: catg
- **Vorbis Comments (flac, ogg)**: PODCASTCATEGORY

## 팟캐스트 설명
- **APE (ape)**: Podcast Description, PODCASTDESCRIPTION
- **ASF/Windows Media (asf, wma)**: PODCASTDESCRIPTION
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDES
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ldes
- **Vorbis Comments (flac, ogg)**: PODCASTDESCRIPTION

## 팟캐스트 ID
- **APE (ape)**: Podcast Id, PODCASTID
- **ASF/Windows Media (asf, wma)**: PODCASTID
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TGID
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: egid
- **Vorbis Comments (flac, ogg)**: PODCASTID

## 팟캐스트 키워드
- **APE (ape)**: Podcast Keywords, PODCASTKEYWORDS
- **ASF/Windows Media (asf, wma)**: PODCASTKEYWORDS
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TKWD
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: keyw
- **Vorbis Comments (flac, ogg)**: PODCASTKEYWORDS

## 팟캐스트 URL
- **APE (ape)**: Podcast URL, PODCASTURL
- **ASF/Windows Media (asf, wma)**: PODCASTURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WFED
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: purl
- **Vorbis Comments (flac, ogg)**: PODCASTURL

## 프로듀서
- **APE (ape)**: Producer, PRODUCER
- **ASF/Windows Media (asf, wma)**: WM/Producer
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIPL:producer
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:PRODUCER, ©prd
- **Vorbis Comments (flac, ogg)**: PRODUCER

## 발행자
- **APE (ape)**: Publisher, PUBLISHER
- **ASF/Windows Media (asf, wma)**: WM/Publisher
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPUB
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©pub
- **Vorbis Comments (flac, ogg)**: PUBLISHER

## 평점
- **APE (ape)**: Rating, RATING
- **ASF/Windows Media (asf, wma)**: WM/SharedUserRating
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: POPM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: rate
- **Vorbis Comments (flac, ogg)**: RATING

## 레코드 레이블
- **APE (ape)**: Label, LABEL
- **ASF/Windows Media (asf, wma)**: LABEL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:LABEL
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:LABEL, ©lab
- **Vorbis Comments (flac, ogg)**: LABEL

## 발매 국가
- **APE (ape)**: Release Country, RELEASECOUNTRY
- **ASF/Windows Media (asf, wma)**: RELEASECOUNTRY
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:RELEASECOUNTRY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: RELEASECOUNTRY

## 발매 상태
- **APE (ape)**: Release Status, RELEASESTATUS
- **ASF/Windows Media (asf, wma)**: RELEASESTATUS
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:RELEASESTATUS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: RELEASESTATUS

## 발매 유형
- **APE (ape)**: Release Type, RELEASETYPE
- **ASF/Windows Media (asf, wma)**: RELEASETYPE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:RELEASETYPE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: RELEASETYPE

## 리믹스한 사람
- **APE (ape)**: MixArtist, MIXARTIST
- **ASF/Windows Media (asf, wma)**: WM/ModifiedBy
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TPE4
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REMIXER
- **Vorbis Comments (flac, ogg)**: REMIXER

## Replay Gain: 앨범 게인
- **APE (ape)**: REPLAYGAIN_ALBUM_GAIN
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_ALBUM_GAIN
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_ALBUM_GAIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_ALBUM_GAIN
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_ALBUM_GAIN

## Replay Gain: 앨범 피크
- **APE (ape)**: REPLAYGAIN_ALBUM_PEAK
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_ALBUM_PEAK
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_ALBUM_PEAK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_ALBUM_PEAK
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_ALBUM_PEAK

## Replay Gain: 앨범 범위
- **APE (ape)**: REPLAYGAIN_ALBUM_RANGE
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_ALBUM_RANGE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_ALBUM_RANGE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_ALBUM_RANGE
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_ALBUM_RANGE

## Replay Gain: 참조 음량
- **APE (ape)**: REPLAYGAIN_REFERENCE_LOUDNESS
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_REFERENCE_LOUDNESS
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_REFERENCE_LOUDNESS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_REFERENCE_LOUDNESS
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_REFERENCE_LOUDNESS

## Replay Gain: 트랙 게인
- **APE (ape)**: REPLAYGAIN_TRACK_GAIN
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_TRACK_GAIN
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_TRACK_GAIN
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_TRACK_GAIN
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_TRACK_GAIN

## Replay Gain: 트랙 피크
- **APE (ape)**: REPLAYGAIN_TRACK_PEAK
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_TRACK_PEAK
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_TRACK_PEAK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_TRACK_PEAK
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_TRACK_PEAK

## Replay Gain: 트랙 범위
- **APE (ape)**: REPLAYGAIN_TRACK_RANGE
- **ASF/Windows Media (asf, wma)**: REPLAYGAIN_TRACK_RANGE
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:REPLAYGAIN_TRACK_RANGE
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:REPLAYGAIN_TRACK_RANGE
- **Vorbis Comments (flac, ogg)**: REPLAYGAIN_TRACK_RANGE

## 스크립트
- **APE (ape)**: Script, SCRIPT
- **ASF/Windows Media (asf, wma)**: WM/Script
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SCRIPT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:SCRIPT
- **Vorbis Comments (flac, ogg)**: SCRIPT

## 악장 표시
- **APE (ape)**: Show Movement, SHOWMOVEMENT
- **ASF/Windows Media (asf, wma)**: SHOWMOVEMENT
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SHOWMOVEMENT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: shwm
- **Vorbis Comments (flac, ogg)**: SHOWMOVEMENT

## 쇼 이름
- **APE (ape)**: Show Name, SHOWNAME
- **ASF/Windows Media (asf, wma)**: SHOWNAME
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SHOWNAME
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: tvsh
- **Vorbis Comments (flac, ogg)**: SHOWNAME

## 쇼 이름 정렬 순서
- **APE (ape)**: Show Name Sort, SHOWNAMESORT
- **ASF/Windows Media (asf, wma)**: SHOWNAMESORT
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:SHOWNAMESORT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: sosn
- **Vorbis Comments (flac, ogg)**: SHOWNAMESORT

## 부제
- **APE (ape)**: Subtitle, SUBTITLE
- **ASF/Windows Media (asf, wma)**: WM/SubTitle
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIT3
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ----:com.apple.iTunes:SUBTITLE
- **Vorbis Comments (flac, ogg)**: SUBTITLE

## 트랙 번호
- **APE (ape)**: Track, TRACK
- **ASF/Windows Media (asf, wma)**: WM/TrackNumber
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRCK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: trkn
- **Vorbis Comments (flac, ogg)**: TRACKNUMBER, TRACKNUM

## 트랙 제목
- **APE (ape)**: Title, TITLE
- **ASF/Windows Media (asf, wma)**: Title
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TIT2
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©nam
- **Vorbis Comments (flac, ogg)**: TITLE

## 트랙 제목 정렬 순서
- **APE (ape)**: Title Sort, TITLESORT
- **ASF/Windows Media (asf, wma)**: WM/TitleSortOrder
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TSOT
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: sonm
- **Vorbis Comments (flac, ogg)**: TITLESORT

## 트랙 총수
- **APE (ape)**: Track, TRACK
- **ASF/Windows Media (asf, wma)**: WM/TrackNumber
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TRCK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: trkn
- **Vorbis Comments (flac, ogg)**: TRACKTOTAL, TOTALTRACKS

## 웹사이트
- **APE (ape)**: Weblink, WEBLINK, WEBSITE
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: N/A
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WEBSITE

## 작품 제목
- **APE (ape)**: Work, WORK
- **ASF/Windows Media (asf, wma)**: WM/Work
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TXXX:WORK
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©wrk
- **Vorbis Comments (flac, ogg)**: WORK

## 작가
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

## WWW: 아티스트
- **APE (ape)**: Artist URL, ARTISTURL, WWWARTIST
- **ASF/Windows Media (asf, wma)**: WM/AuthorURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WOAR
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©prl
- **Vorbis Comments (flac, ogg)**: WWWARTIST

## WWW: 오디오 파일
- **APE (ape)**: File URL, FILEURL, WWWAUDIOFILE
- **ASF/Windows Media (asf, wma)**: WM/AudioFileURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WOAF
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWAUDIOFILE

## WWW: 오디오 소스
- **APE (ape)**: Source URL, SOURCEURL, WWWAUDIOSOURCE
- **ASF/Windows Media (asf, wma)**: WM/AudioSourceURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WOAS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWAUDIOSOURCE

## WWW: 상업 정보
- **APE (ape)**: Commercial Info URL, COMMERCIALINFOURL, WWWCOMMERCIALINFO
- **ASF/Windows Media (asf, wma)**: WM/PromotionURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WCOM
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWCOMMERCIALINFO

## WWW: 저작권
- **APE (ape)**: Copyright URL, COPYRIGHTURL, WWWCOPYRIGHT
- **ASF/Windows Media (asf, wma)**: CopyrightURL
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WCOP
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWCOPYRIGHT

## WWW: 결제
- **APE (ape)**: Buy URL, BUYURL, WWWPAYMENT
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WPAY
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWPAYMENT

## WWW: 발행자
- **APE (ape)**: Publisher URL, PUBLISHERURL, WWWPUBLISHER
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WPUB
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWPUBLISHER

## WWW: 라디오 페이지
- **APE (ape)**: Radio URL, RADIOURL, WWWRADIOPAGE
- **ASF/Windows Media (asf, wma)**: N/A
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: WORS
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: N/A
- **Vorbis Comments (flac, ogg)**: WWWRADIOPAGE

## 연도
- **APE (ape)**: Year, YEAR
- **ASF/Windows Media (asf, wma)**: WM/Year
- **ID3v2 (afc, aif, aifc, aiff, mp3, wav)**: TDRC
- **MP4 (3g2, m4a, m4b, m4p, m4r, m4v, mp4)**: ©day
- **Vorbis Comments (flac, ogg)**: DATE, YEAR
