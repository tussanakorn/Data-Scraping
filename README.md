# Python fundamental for Data Science by Botnoi Classroom #
### Data Scraping, API,  Flask, Database(MongoDB), Heroku and Cronjob

## Project Description
ให้เราดึงข้อมูลจากข่าวจากเว็บไซต์ thairath.co.th โดยเลือกหนึ่งในประเภทข่าวจาก

https://www.thairath.co.th/news/royal
https://www.thairath.co.th/news/local
https://www.thairath.co.th/news/business
https://www.thairath.co.th/news/foreign
https://www.thairath.co.th/news/society
https://www.thairath.co.th/news/crime

เมื่อเลือกได้แล้ว เราจะเห็น Section ข่าวอื่น ๆ จะเห็นว่ามีข่าวใหม่ทั้งหมด 12 ข่าวที่อยู่ในหน้าแรก ให้เราเขียน Script เพื่อดึงข้อมูลข่าวเหล่านี้ จากนั้นเก็บข้อมูลไว้ใน Database MongoDB (atlas หรือ mlab) โดยห้ามเก็บข่าวซ้ำกับข่าวที่มีอยู่ใน Database แล้ว

โดยดาต้าข่าวหนึ่งข่าวจะต้องมี field ดังนี้
1. title - ชื่อข่าว เก็บเป็น String
2. publish_date - วันที่ เก็บเป็น Datetime Object
3. desc - เนื้อหาของข่าวเป็น String
4. tags - แท็กที่เกี่ยวข้อง เก็บเป็น Array ของ String
5. cover_img - รูปหลักของข่าว เก็บเป็น String
6. news_url - ลิ้งข่าว เก็บเป็น String
7. category - ประเภทข่าว เก็บเป็น String


จากนั้น Deploy script อันนี้ขึ้น Heroku แล้วสั่งให้รันทุก ๆ หนึ่งชั่วโมง

เมื่อเราทำ Scheduler เรียบร้อยแล้ว ให้เราทำการสร้าง Web API ที่สามารถ serve ข้อมูลข่าวใน Database ของเราได้
โดย API เส้นนี้จะต้องสามารถ filter ได้ดังนี้
1. date - จะต้องสามารถกรองเฉพาะข่าวปล่อยออกมาในวันที่กำหนดได้
2. tag - จะต้องสามารถกรองเฉพาะข่าวที่มีแท็กที่กำหนดได้
3. limit - จะต้องสามารถเลือกแสดงจำนวนข่าวตามจำนวนที่กำหนดได้ (สูงสุด 20 ข่าวต่อ 1 request)
แล้วก็สามารถกรอง date และ tag พร้อมกันได้

Deploy API เส้นนี้บน Heroku ให้เรียบร้อยเป็นอันเสร็จ

Product สุดท้ายจะได้ลิ้ง API ของแต่ละคนที่สามารถ serve ข้อมูลข่าวได้ และอัพเดทเรื่อย ๆ ผ่าน Heroku Scheduler

# Certificate of Achievement
[![certifficate-Botnoi.png](https://i.postimg.cc/mg3jhgyc/certifficate-Botnoi.png)](https://postimg.cc/9DMZnVSV)
