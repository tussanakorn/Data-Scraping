import bs4
import requests
import pymongo
import os


def connect_to_database():
    # ใช้ os.environ แทน ไม่ควร hard code อะไรที่เป็น credential
    MONGODB_URI = 'mongodb://heroku_672rlh8s:s18fo4q6ejpm67lmodcn4hqjil@ds161551.mlab.com:61551/heroku_672rlh8s'
    client = pymongo.MongoClient(MONGODB_URI, retryWrites=False)
    db = client['heroku_672rlh8s']
    collection_name = 'covid_stats'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    collection = db[collection_name]
    return collection

def scrape_data():
    response = requests.get('https://www.worldometers.info/coronavirus/')
    html_page = bs4.BeautifulSoup(response.content, 'html.parser')

    selector = 'div.col-md-8 > div.content-inner > div'
    last_update = html_page.select(selector)[1].text[14:]

    selector = 'div#maincounter-wrap > div.maincounter-number > span'
    tags = html_page.select(selector)

    num_cases = int(tags[0].text.strip().replace(',' ,''))
    num_deaths = int(tags[1].text.strip().replace(',' ,''))
    num_recovered = int(tags[2].text.strip().replace(',' ,''))

    document = {"last_update": last_update, "num_cases": num_cases, "num_deaths": num_deaths, "num_recovered": num_recovered}

    return document


def insert_to_database(collection, document):
    collection.insert_one(document)
    print(document)
    print('Document inserted!')


def main():
    collection = connect_to_database()
    print(collection)
    # document = scrape_data()
    # insert_to_database(collection, document)


if __name__ == "__main__":
    main()