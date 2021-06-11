
import bs4  
import requests
import pymongo
import os
from flask import Flask , request , jsonify
import json
from datetime import date , datetime
import time

app = Flask(__name__)

def New_Url():
    response =  requests.get('https://www.thairath.co.th/news/crime')
    html_page = bs4.BeautifulSoup(response.content , 'html.parser')
    selector = 'a'
    #ข่าวล่าสุด 1
    news_one_tag_1 = html_page.select(selector)[181]['href']
    main_url_1 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_1
    #ข่าวล่าสุด 2
    news_one_tag_2 = html_page.select(selector)[183]['href']
    main_url_2 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_2
    #ข่าวล่าสุด 3
    news_one_tag_3 = html_page.select(selector)[185]['href']
    main_url_3 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_3
    #ข่าวล่าสุด 4
    news_one_tag_4 = html_page.select(selector)[187]['href']
    main_url_4 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_4
    #ข่าวล่าสุด 5
    news_one_tag_5 = html_page.select(selector)[189]['href']
    main_url_5 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_5
    #-ข่าวยอดนิยม 1
    news_one_tag_6 = html_page.select(selector)[192]['href']
    main_url_6 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_6
    #ข่าวยอดนิยม 2
    news_one_tag_7 = html_page.select(selector)[195]['href']
    main_url_7 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_7
    #ข่าวยอดนิยม 3
    news_one_tag_8 = html_page.select(selector)[198]['href']
    main_url_8 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_8
    #สกู๊ปพิเศษ
    news_one_tag_9 = html_page.select(selector)[201]['href']
    main_url_9 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_9
    #ข่าวทั่วไป 3
    news_one_tag_10 = html_page.select(selector)[179]['href']
    main_url_10 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_10
    #ข่าวทั่วไป 2
    news_one_tag_11 = html_page.select(selector)[177]['href']
    main_url_11 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_11
    #ข่าวทั่วไป 1
    news_one_tag_12 = html_page.select(selector)[175]['href']
    main_url_12 = 'https://www.thairath.co.th/news/crime'+ news_one_tag_12

    doc_url = {'main_url_1' : main_url_1,
                'main_url_2' : main_url_2,
                'main_url_3' : main_url_3,
                'main_url_4' : main_url_4,
                'main_url_5' : main_url_5,
                'main_url_6' : main_url_6,
                'main_url_7' : main_url_7,
                'main_url_8' : main_url_8,
                'main_url_9' : main_url_9,
                'main_url_10' : main_url_10,
                'main_url_11' : main_url_11,
                'main_url_12' : main_url_12
                }
    return doc_url

def get_data_thairath(main_url):
    respone = requests.get(main_url)
    html_page = bs4.BeautifulSoup(respone.content , 'html.parser')
  
    title = thairath_title(html_page)
    datetime = thairath_datetime( html_page)
    description = thairath_desc( html_page)
    category = thairath_category(html_page)
    img = thairath_img(html_page)
    tags = thairath_tags(html_page)

    documents = {'title' : title,
               'datetime' : datetime,
               'description' :  description,
               'category' : category,
               'URL_News' : main_url,
               'img' : img,
               'tags' : tags
               }

    return documents

def thairath_title(main_html_page):
    selector = 'h1'
    main_title_tag = main_html_page.select(selector)[0]
    main_title = main_title_tag.text
    return main_title

def thairath_datetime( main_html_page):
    ts = time.gmtime()
    date_ts = (time.strftime('%Y-%m-%d %H:%M:%S' , ts))  
    date = date_ts[0:10]
 
    return date
       
def thairath_desc( main_html_page):
    selector = 'p'
    main_desc_texts = ''
    main_desc_tags = main_html_page.select(selector)
    for tag in main_desc_tags:
        main_desc_texts += (tag.text)
    return main_desc_texts

def thairath_category( main_html_page):
    selector = 'a'
    main_category_tags = main_html_page.select(selector)[175]
    main_category = main_category_tags.text
    return main_category


def thairath_img(main_html_page):
    img_list = []
    selector = 'div.css-1qqrjyc.evs3ejl0 img'
    main_img_tags = main_html_page.select(selector)
    for img in main_img_tags:
      imgs = img['src']
      img_list.append(imgs)
    return  img_list

def thairath_tags(main_html_page):
    elements = main_html_page.select('div.css-sq8bxp.evs3ejl16 span')
    tags_list = []
    for element in elements:
        tags_list.append(element.text)
    return tags_list

def connect_to_database():
    #ใช้os.environ ไม่ควรใช้ hard code อะำรที่เป็น credential
    #MONGODB_URI = os.environ['MONGODB_URI']
    MONGODB_URI = 'mongodb://heroku_9nsxmlxq:s59q6n2krkan61n3lidf4d794o@ds137283.mlab.com:37283/heroku_9nsxmlxq'
    client = pymongo.MongoClient(MONGODB_URI , retryWrites = False)
    db = client['heroku_9nsxmlxq']
    collection_name = 'Film_News_project'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    collection = db[collection_name]
    return collection

def insert_to_database(collection,document):
    query = {}
    title_list = []
    cursors = collection.find(query)
    for cursor in cursors:
        cursor_title = cursor['title']
        title_list.append(cursor_title)

    if document['title'] not in  title_list:
        collection.insert_one(document)
        print('Document Inserted!')
            
def main():
    urls = New_Url()
    for url in urls.values():
        main_url = url
        document = get_data_thairath(main_url)
        collection = connect_to_database()
        insert_to_database(collection,document)
    
    app.run(debug=True)

@app.route('/news1')
def home():
    ts = time.gmtime()
    date_ts = (time.strftime('%Y-%m-%d %H:%M:%S' , ts))  
    date = date_ts[0:10]
    datetime = request.args.get('datetime' , default = date)
    limit = request.args.get('limit' , default=20 ,type=int)
    tags = request.args.get('tag')
    collection = connect_to_database()
    #query = {}
    query = {'$or' :[{'datetime': datetime},{'tags' : tags}]}
    projection = {'_id' : 0}
    try:

        if limit <= 20:
            cursor = collection.find(query , projection = projection).limit(limit)
            documents = [document for document in cursor]
    
        return jsonify(documents)
    except:
        return('limit must be less than or equal to 20 only!!')
    
if __name__ == '__main__':
    main()
    