---
title: "วิธีเชื่อมต่อที่เก็บข้อมูล NAS ด้วย WebDAV และฟังเพลงบน iPhone หรือ Mac"
date: 2024-07-28
description: "เรียนรู้วิธีกำหนดค่า WebDAV บน Synology NAS และสตรีมเพลงไปยัง iPhone หรือ Mac โดยใช้ Evermusic หรือ Flacbox ทำตามคู่มือทีละขั้นตอนของเรา"
keywords: ["เชื่อมต่อ nas", "webdav synology", "สตรีมเพลง nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["เพลง", "สตรีมมิ่ง", "ที่เก็บข้อมูล", "nas", "เชื่อมต่อ", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**สรุป:** ติดตั้งและเปิดใช้งาน WebDAV บน Synology NAS กำหนดค่าสิทธิ์โฟลเดอร์ที่แชร์ จากนั้นเชื่อมต่อจาก Evermusic หรือ Flacbox โดยใช้ที่อยู่ IP ของ NAS และพอร์ต WebDAV (ค่าเริ่มต้น 5005/5006) คุณสามารถสตรีมและจัดการคลังเพลงทั้งหมดได้โดยไม่ต้องคัดลอกไฟล์ไปยังอุปกรณ์

ค้นพบวิธีเชื่อมต่อที่เก็บข้อมูล NAS ด้วย WebDAV และสตรีมคลังเพลงไปยัง iPhone หรือ Mac ได้อย่างง่ายดาย WebDAV (Web-based Distributed Authoring and Versioning) เป็นโปรโตคอลที่ช่วยให้คุณจัดการและแชร์ไฟล์ผ่านอินเทอร์เน็ต การตั้งค่า WebDAV บน NAS ช่วยให้คุณเข้าถึงและสตรีมคอลเลกชันเพลง ทำให้เพลงโปรดของคุณอยู่ใกล้แค่ปลายนิ้วเสมอ

ในคู่มือนี้ เราจะแสดงวิธีตั้งค่าการเชื่อมต่อ WebDAV บนเซิร์ฟเวอร์ NAS ที่ได้รับความนิยมสูงสุดอย่าง Synology NAS ทำตามขั้นตอนง่ายๆ ของเราเพื่อกำหนดค่า WebDAV บน Synology NAS และคุณจะสามารถเรียกดู สตรีม และจัดการคลังเพลงโดยตรงจาก iPhone หรือ Mac

## ขั้นตอนที่ 1: ติดตั้ง WebDAV บน Synology NAS

1. เข้าสู่ระบบ Synology NAS และเปิด **ศูนย์แพ็กเกจ**
2. ค้นหา "webdav" และติดตั้งแพ็กเกจ WebDAV หากยังไม่ได้ติดตั้ง เปิดเซิร์ฟเวอร์ WebDAV เพื่อกำหนดค่า

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="ติดตั้ง WebDAV บน Synology" width="600" >}}

## ขั้นตอนที่ 2: กำหนดค่าเซิร์ฟเวอร์ WebDAV

1. ในหน้าการตั้งค่า WebDAV ทำเครื่องหมายในช่อง **เปิดใช้งาน HTTP**, **เปิดใช้งาน HTTPS**, **เปิดใช้งาน WebDAV แบบไม่ระบุชื่อ** และ **เปิดใช้งาน DavDepthInfinity**
2. คลิก **ใช้** เพื่อบันทึกการเปลี่ยนแปลง จดหมายเลขพอร์ตสำหรับการเชื่อมต่อ HTTP และ HTTPS ซึ่งค่าเริ่มต้นคือ 5005 และ 5006

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="กำหนดค่าการตั้งค่า WebDAV" width="600" >}}

## ขั้นตอนที่ 3: กำหนดค่าสิทธิ์โฟลเดอร์ที่แชร์

1. เปิด **แผงควบคุม** และไปที่ส่วน **โฟลเดอร์ที่แชร์**
2. เลือกโฟลเดอร์ **เพลง** และคลิก **แก้ไข**
3. ในแท็บ **สิทธิ์** กำหนดค่าสิทธิ์ เปิดใช้งานการเข้าถึงของผู้เยี่ยมชมด้วยสิทธิ์อ่านอย่างเดียวหากคุณต้องการฟังเพลงเท่านั้น หรืออ่าน/เขียนหากคุณต้องการแก้ไขไฟล์ บันทึกการเปลี่ยนแปลง

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="สิทธิ์โฟลเดอร์ที่แชร์" width="600" >}}

## ขั้นตอนที่ 4: ค้นหาที่อยู่ IP ของ Synology NAS

1. เปิด **แผงควบคุม** และไปที่แท็บ **อินเทอร์เฟซเครือข่าย** หรือใช้เว็บเบราว์เซอร์เพื่อเยี่ยมชม [find.synology.com](http://find.synology.com)

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="ค้นหาที่อยู่ IP ของ NAS" width="600" >}}

2. จดที่อยู่ IP ของ Synology NAS (เช่น 192.168.18.137)

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="ที่อยู่ IP ของ Synology NAS" width="600" >}}

## ขั้นตอนที่ 5: เชื่อมต่อกับ Synology NAS โดยใช้ Evermusic/Flacbox

1. เปิดแอป Evermusic หรือ Flacbox และไปที่แท็บ **การเชื่อมต่อ**

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="แท็บการเชื่อมต่อใน Evermusic" width="600" >}}

2. สำหรับการเชื่อมต่ออัตโนมัติ ค้นหา Synology NAS ในส่วน **อุปกรณ์ที่มีให้บริการ** แล้วแตะเพื่อเชื่อมต่อ

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="รายการอุปกรณ์ที่มีให้บริการ" width="600" >}}

3. สำหรับการเชื่อมต่อด้วยตนเอง เลือก **เชื่อมต่อบริการคลาวด์** และเลือก **WebDAV** ป้อนที่อยู่เซิร์ฟเวอร์ในรูปแบบ: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (เช่น [https://192.168.18.137:5006](https://192.168.18.137:5006))

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="การกำหนดค่า WebDAV ด้วยตนเอง" width="600" >}}

4. เว้นช่องชื่อผู้ใช้และรหัสผ่านว่างไว้สำหรับการเข้าถึงของผู้เยี่ยมชม หรือป้อนข้อมูลรับรอง Synology ของคุณ แตะ **เข้าสู่ระบบ**

## ขั้นตอนที่ 6: นำทางและเล่นเพลง

1. เมื่อเชื่อมต่อแล้ว อุปกรณ์จะปรากฏในรายการ **อุปกรณ์ที่เชื่อมต่อ**

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="อุปกรณ์ที่เชื่อมต่อใน Evermusic" width="600" >}}

2. นำทางไปยังโฟลเดอร์ **เพลง** แล้วแตะไฟล์เสียงใดก็ได้เพื่อเริ่มเล่น

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="เรียกดูโฟลเดอร์เพลง" width="600" >}}

## ขั้นตอนที่ 7: เพิ่มโฟลเดอร์คลาวด์ที่เชื่อมต่อไปยังคลังเพลง

1. เปิดส่วน **คลังเพลง** ในแอป
2. เลือก **เพิ่มเพลง** และเลือก **การเชื่อมต่อ**
3. เลือกเซิร์ฟเวอร์ NAS ที่เชื่อมต่อและเลือกโฟลเดอร์ **เพลง** แตะ **เสร็จสิ้น**
4. แอปจะสแกนโฟลเดอร์เพลงและเพิ่มไฟล์เสียงที่รองรับลงในคลังเพลง ข้อมูลเมตาจะถูกโหลด และเพลงของคุณจะถูกจัดกลุ่มตามอัลบั้ม ศิลปิน และประเภท

## สรุป

โดยทำตามขั้นตอนเหล่านี้ คุณสามารถตั้งค่าการเชื่อมต่อ WebDAV บน Synology NAS และสตรีมคลังเพลงไปยัง iPhone หรือ Mac โดยใช้ Evermusic หรือ Flacbox ได้อย่างง่ายดาย เพลิดเพลินกับการเข้าถึงเพลงโปรดได้อย่างราบรื่นทุกเวลา

## คำถามที่พบบ่อย

{{% details title="อุปกรณ์ NAS ใดรองรับ WebDAV?" closed="true" %}}
แบรนด์ NAS ยอดนิยมส่วนใหญ่รองรับ WebDAV รวมถึง Synology, QNAP, TrueNAS และ Western Digital ตรวจสอบเอกสารของผู้ผลิต NAS สำหรับคำแนะนำในการตั้งค่า WebDAV
{{% /details %}}

{{% details title="อะไรคือความแตกต่างระหว่าง WebDAV และ SMB สำหรับการสตรีมเพลงจาก NAS?" closed="true" %}}
WebDAV ทำงานผ่าน HTTP/HTTPS และเหมาะกว่าสำหรับการเข้าถึงระยะไกลผ่านอินเทอร์เน็ต SMB มักจะเร็วกว่าในเครือข่ายท้องถิ่น Evermusic และ Flacbox รองรับทั้งสองโปรโตคอล ดังนั้นเลือกตามว่าคุณต้องการการเข้าถึงแบบท้องถิ่นหรือระยะไกล
{{% /details %}}

{{% details title="ฉันต้องใช้ชื่อผู้ใช้และรหัสผ่านสำหรับ WebDAV บน Synology หรือไม่?" closed="true" %}}
ไม่ หากคุณเปิดใช้งานการเข้าถึง WebDAV แบบไม่ระบุชื่อและกำหนดค่าสิทธิ์ผู้เยี่ยมชมบนโฟลเดอร์ที่แชร์ เพื่อความปลอดภัยที่ดีขึ้น คุณสามารถใช้ข้อมูลรับรอง Synology แทนได้
{{% /details %}}

{{% details title="ฉันสามารถสตรีม FLAC และรูปแบบความละเอียดสูงอื่นๆ จาก NAS ผ่าน WebDAV ได้หรือไม่?" closed="true" %}}
ได้ ทั้ง Evermusic และ Flacbox รองรับ FLAC, ALAC, WAV, DSD และรูปแบบความละเอียดสูงอื่นๆ เมื่อสตรีมจากที่เก็บข้อมูล NAS ผ่าน WebDAV
{{% /details %}}

{{% details title="ทำไมแอปไม่สามารถค้นหา NAS ในอุปกรณ์ที่มีให้บริการ?" closed="true" %}}
ตรวจสอบให้แน่ใจว่า iPhone/Mac และ NAS อยู่ในเครือข่าย Wi-Fi เดียวกัน หากการค้นหาอัตโนมัติไม่ทำงาน ใช้ตัวเลือกการเชื่อมต่อด้วยตนเองและป้อนที่อยู่ IP ของ NAS และพอร์ต WebDAV โดยตรง
{{% /details %}}
