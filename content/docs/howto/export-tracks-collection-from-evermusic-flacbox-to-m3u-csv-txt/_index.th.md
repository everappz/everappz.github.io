---
title: "วิธีส่งออกคอลเลกชันเพลงเป็น M3U, CSV และ TXT ใน Evermusic และ Flacbox"
date: 2024-01-31
description: "เรียนรู้วิธีส่งออกล่าสุด รายการโปรด เพลย์ลิสต์ และอัลบั้มจาก Evermusic และ Flacbox เป็นรูปแบบ M3U, CSV หรือ TXT เหมาะสำหรับการ scrobble ไปยัง Last.fm และเล่นบนอุปกรณ์อื่น"
keywords: ["ส่งออก evermusic", "ส่งออก flacbox", "ส่งออกเป็น m3u", "ส่งออกเพลย์ลิสต์เป็น csv", "m3u txt csv เพลย์ลิสต์", "ส่งออกเพลง"]
tags: ["evermusic", "ล่าสุด", "รายการโปรด", "ส่งออก", "m3u", "เพลย์ลิสต์", "csv", "txt", "อัลบั้ม"]
---

{{< author-byline >}}


**สรุป:** Evermusic และ Flacbox ให้คุณส่งออกคอลเลกชันเพลงใดก็ได้ (ล่าสุด, รายการโปรด, เพลย์ลิสต์, อัลบั้ม) เป็นไฟล์ CSV, TXT หรือ M3U ใช้การส่งออกเหล่านี้เพื่อ scrobble ไปยัง Last.fm สำรองข้อมูลคลังเพลง หรือเล่นเพลย์ลิสต์บนอุปกรณ์อื่น

## บทนำ

การส่งออกล่าสุด รายการโปรด อัลบั้ม และเพลย์ลิสต์จากแอปไปยังไฟล์ภายนอกนั้นมีประโยชน์อย่างมาก คุณสามารถใช้ไฟล์เหล่านี้เพื่ออัปเดตประวัติการฟังบนบริการ scrobbling เช่น [Last.fm](http://Last.fm) หรือฟังเพลย์ลิสต์บนอุปกรณ์ภายนอก ด้วย Evermusic และ Flacbox กระบวนการนี้ง่ายมาก ที่นี่เราจะแสดงวิธีส่งออกล่าสุดเป็น CSV/TXT และเพลย์ลิสต์เป็น M3U อย่างไรก็ตาม ฟังก์ชันนี้ใช้ได้กับคอลเลกชันเพลงใดก็ได้ในแอป

## เลือกรูปแบบ

ในการส่งออกล่าสุด ให้เปิดส่วน «คลังเพลง» และเลือกรายการเมนู «ล่าสุด»

![คลังเพลง](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

บนหน้าจอถัดไป แตะปุ่ม «เพิ่มเติม» ที่มุมขวาบน และเลือก «ส่งออกรายการเพลง»

![ส่งออกล่าสุด](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

บนหน้าจอ «เลือกรูปแบบไฟล์» คุณมีตัวเลือกหลายอย่าง — CSV, TXT, M3U

- CSV

ย่อมาจาก Comma-Separated Values (ค่าที่คั่นด้วยจุลภาค) เหมาะสำหรับจัดระเบียบข้อมูลในรูปแบบตาราง ในไฟล์ปลายทาง คุณจะพบพารามิเตอร์ต่างๆ เช่น ชื่อศิลปิน ชื่ออัลบั้ม ชื่อเพลง การประทับเวลา (เวลาที่คุณฟังเพลง) ชื่อศิลปินอัลบั้ม และระยะเวลาของเพลง คุณสามารถใช้ไฟล์นี้ในภายหลังเพื่ออัปเดตประวัติการฟังบนบริการ scrobbling เช่น [Last.fm](http://Last.fm) ตามที่อธิบายไว้[ที่นี่](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/)

- TXT

ที่นี่เราพูดถึงไฟล์ข้อความธรรมดา ง่ายและตรงไปตรงมา พร้อมพารามิเตอร์รวมถึงชื่อศิลปิน ชื่ออัลบั้ม ชื่อเพลง และระยะเวลา มีประโยชน์หากคุณต้องการเพียงรายการเพลงในรูปแบบข้อความ

- M3U

รูปแบบนี้เป็นมาตรฐานโดยพฤตินัยสำหรับการสร้างเพลย์ลิสต์ ดีเพราะคุณสามารถส่งออกรายการเพลงและเพลิดเพลินกับเพลงบนอุปกรณ์ใดก็ได้ แม้ว่าคุณจะไม่มีไฟล์ต้นฉบับ (หากคุณเลือกตัวเลือก URL แบบสัมบูรณ์สำหรับการส่งออกไฟล์มีเดีย) ในไฟล์ผลลัพธ์ คุณจะพบพารามิเตอร์เช่น ระยะเวลา ชื่อศิลปิน ชื่อเพลง และตำแหน่งไฟล์มีเดีย

## รูปแบบ CSV

ตอนนี้มาเลือก CSV และดูว่าเราจะได้อะไร เพียงเลือก CSV แล้วกดปุ่ม «ส่งออก»

![เลือกรูปแบบไฟล์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

เมื่อการส่งออกเสร็จสมบูรณ์ คุณจะเห็นการแจ้งเตือนพร้อมสองตัวเลือก การแตะ «แสดงไฟล์» จะแสดงไฟล์ผลลัพธ์ในไดเรกทอรีเอกสารของคุณ

![ส่งออกเสร็จสมบูรณ์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

ตอนนี้คุณสามารถส่งไฟล์นั้น เปิดในโปรแกรมแก้ไขข้อความภายนอก หรือใช้เพื่ออัปเดตความคืบหน้าการฟังบน [Last.fm](http://Last.fm)

![โฟลเดอร์ส่งออกพร้อมไฟล์ผลลัพธ์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

ไฟล์ CSV ผลลัพธ์จะมีฟิลด์ในรูปแบบต่อไปนี้:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

ตัวอย่าง:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![ไฟล์ csv ที่ส่งออก](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## รูปแบบ TXT

ไฟล์ TXT ผลลัพธ์จะมีฟิลด์ในรูปแบบต่อไปนี้:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

ตัวอย่าง:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![ไฟล์ txt ที่ส่งออก](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## รูปแบบ M3U

ต่อไป เราจะแนะนำคุณเกี่ยวกับการส่งออกเพลย์ลิสต์เป็นรูปแบบ M3U ซึ่งเป็นมาตรฐานโดยพฤตินัยสำหรับไฟล์เพลย์ลิสต์ เงื่อนไขหลักสำหรับการส่งออกเพลย์ลิสต์สำเร็จคือไฟล์ทั้งหมดในเพลย์ลิสต์ต้องอยู่ในที่จัดเก็บเดียวกัน ไม่ว่าจะเป็นบริการคลาวด์เช่น Google Drive ไฟล์ในเครื่อง หรือไฟล์บนอุปกรณ์ของคุณ ในการเริ่มกระบวนการส่งออก ให้เปิดเพลย์ลิสต์ใดก็ได้แล้วแตะปุ่ม «เพิ่มเติม» ที่มุมขวาบน จากนั้นเลือกรายการเมนู «ส่งออกรายการเพลง»

![หน้าจอเพลย์ลิสต์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

บนหน้าจอถัดไป เลือกรูปแบบไฟล์ «M3U» ซึ่งคุณจะพบสองตัวเลือกสำหรับ «ประเภทตำแหน่งไฟล์มีเดีย»:

![หน้าจอเลือกรูปแบบไฟล์ส่งออก](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. หากคุณเลือก «เส้นทางสัมพัทธ์» เพลย์ลิสต์จะถูกสร้างขึ้นโดยตำแหน่งไฟล์มีเดียเขียนสัมพัทธ์กับไฟล์เพลย์ลิสต์ ตัวอย่าง:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   ในกรณีนี้ หลีกเลี่ยงการเปลี่ยนตำแหน่งไฟล์ M3U หลังจากการส่งออกเสร็จสมบูรณ์ เนื่องจากจะทำให้เส้นทางไปยังไฟล์มีเดียเสียหาย ในการเริ่มเล่นเพลย์ลิสต์ เพียงแตะที่ไฟล์เพลย์ลิสต์ที่ส่งออก แล้วแอปจะค้นหาไฟล์มีเดียในที่จัดเก็บของคุณโดยอัตโนมัติและเริ่มเล่น คุณยังสามารถส่งออกเพลย์ลิสต์ไปยังที่จัดเก็บแล้วนำเข้าอีกครั้งบนอุปกรณ์ใหม่ของคุณ

2. หากคุณเลือก «URL แบบสัมบูรณ์» แอปจะสร้าง URL โดยตรงสำหรับไฟล์มีเดียของคุณ ซึ่งช่วยให้คุณเล่นเพลย์ลิสต์บนอุปกรณ์/แอปพลิเคชันใดก็ได้โดยไม่ต้องมีไฟล์มีเดียทั้งหมดอยู่ในที่จัดเก็บเดียวกันกับไฟล์เพลย์ลิสต์ ตัวเลือกนี้รองรับเฉพาะที่จัดเก็บคลาวด์ที่สามารถสร้าง URL ไฟล์โดยตรง อย่างไรก็ตาม โปรดทราบว่าในบางกรณี URL ที่สร้างขึ้นอาจมีอายุจำกัดและอาจหมดอายุหลังจากผ่านไประยะหนึ่ง นี่คือรายการบริการคลาวด์ที่รองรับ: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (ในโหมดผู้เยี่ยมชม)  

URL ไฟล์มีเดียผลลัพธ์จะมีลักษณะประมาณนี้:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

หลังจากเลือก «ประเภทตำแหน่งไฟล์มีเดีย» แล้ว ให้แตะ «ส่งออก» แอปจะแจ้งให้คุณเลือกโฟลเดอร์ปลายทางสำหรับการส่งออกไฟล์ M3U แตะ «เสร็จสิ้น» เพื่อยืนยันการเลือกของคุณ

![เลือกโฟลเดอร์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

แอปจะสร้างไฟล์ M3U และอัปโหลด/ย้ายไปยังโฟลเดอร์ปลายทาง

![กำลังอัปโหลดไฟล์ m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

เมื่อการส่งออกเสร็จสมบูรณ์ จะปรากฏการแจ้งเตือนระบบพร้อมตัวเลือก «แสดงไฟล์»

![การแจ้งเตือนส่งออกเสร็จสมบูรณ์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

การแตะจะแสดงไฟล์ที่ส่งออกในแอป

![ไฟล์ m3u ที่ส่งออกในรายการไฟล์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

หากคุณเลือก «เส้นทางสัมพัทธ์» เป็น «ประเภทตำแหน่งไฟล์มีเดีย» ในขั้นตอนก่อนหน้า ไฟล์ผลลัพธ์จะอยู่ในรูปแบบต่อไปนี้:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![ตัวอย่าง m3u พร้อมเส้นทางสัมพัทธ์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

สำหรับตัวเลือก «URL แบบสัมบูรณ์» แอปจะสร้างไฟล์ M3U ในรูปแบบ:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![ตัวอย่าง m3u พร้อม URL ไฟล์แบบสัมบูรณ์](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

คุณสามารถเปิดไฟล์นั้นบนอุปกรณ์/แอปพลิเคชันใดก็ได้ที่รองรับเพลย์ลิสต์ M3U

![เพลย์ลิสต์ m3u เปิดในแอปภายนอก](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## สรุป

การส่งออกเพลงจาก Evermusic และ Flacbox ให้คุณควบคุมข้อมูลเพลงของคุณได้อย่างสมบูรณ์ ไม่ว่าคุณจะสำรองข้อมูลประวัติการฟัง scrobble ไปยัง Last.fm หรือเพลิดเพลินกับเพลย์ลิสต์บนอุปกรณ์ภายนอก ตัวเลือกการส่งออกเหล่านี้ — M3U, CSV และ TXT — เป็นเครื่องมือที่ทรงพลังที่ออกแบบมาเพื่อความยืดหยุ่นและความเข้ากันได้ ใช้ประโยชน์จากฟีเจอร์เหล่านี้เพื่อปรับปรุงวิธีที่คุณจัดระเบียบ แบ่งปัน และเข้าถึงคอลเลกชันเพลงของคุณข้ามแพลตฟอร์ม

## คำถามที่พบบ่อย

{{% details title="ควรใช้รูปแบบส่งออกใดสำหรับการ scrobble Last.fm?" closed="true" %}}
ใช้ CSV เนื่องจากมีการประทับเวลาและข้อมูลเมตาครบถ้วนที่เครื่องมือ scrobbling เช่น Last.fm-Scrubbler-WPF ต้องการ
{{% /details %}}

{{% details title="ฉันสามารถส่งออกคอลเลกชันเพลงใดก็ได้ ไม่ใช่แค่เพลย์ลิสต์ใช่ไหม?" closed="true" %}}
ใช่ คุณสามารถส่งออกล่าสุด รายการโปรด อัลบั้ม เพลย์ลิสต์ และคอลเลกชันเพลงอื่นๆ ในแอปโดยใช้ขั้นตอนเดียวกัน
{{% /details %}}

{{% details title="เพลย์ลิสต์ M3U ของฉันจะทำงานบนอุปกรณ์อื่นได้ไหม?" closed="true" %}}
หากคุณเลือกตัวเลือก URL แบบสัมบูรณ์ระหว่างการส่งออก ไฟล์ M3U สามารถเล่นบนอุปกรณ์ใดก็ได้ที่รองรับเพลย์ลิสต์ M3U โปรดทราบว่า URL คลาวด์บางรายการอาจหมดอายุเมื่อเวลาผ่านไป
{{% /details %}}

{{% details title="ฟีเจอร์ส่งออกฟรีหรือไม่?" closed="true" %}}
ใช่ การส่งออกคอลเลกชันเพลงเป็น M3U, CSV และ TXT มีให้ทั้งในเวอร์ชันฟรีและพรีเมียมของ Evermusic และ Flacbox
{{% /details %}}

{{% details title="บริการคลาวด์ใดรองรับการส่งออกด้วย URL แบบสัมบูรณ์?" closed="true" %}}
การส่งออกด้วย URL แบบสัมบูรณ์รองรับสำหรับ iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive และ WebDAV (โหมดผู้เยี่ยมชม)
{{% /details %}}
