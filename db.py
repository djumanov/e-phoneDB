import json
from tinydb import TinyDB
import requests
import random
from datetime import date

base_url = 'http://127.0.0.1:8000/api/'

rams = [3, 4, 6, 8, 12]
memories = [16, 32, 64, 128, 256, 512]

day = list(range(1, 28))
month = list(range(1, 12))
year = list(range(2010, 2022))

db = TinyDB('db.json')
collections = db.tables()
def add_companies():
    for collection_name in collections:
        payload = {
            'name': collection_name,
            'logo': collection_name,
            'description': collection_name + ' description',
            'website': f'www.{collection_name.lower()}.com'
        }
        r = requests.post(url=base_url+'add_company/', data=payload)
        print(r.status_code)


def add_products():
    for collection_name in collections:
        table = db.table(name=collection_name)
        documents = table.all()
        for document in documents:
            payload = {
                'name': document['name'],
                'color': document['color'],
                'ram': random.choice(rams),
                'memory': random.choice(memories),
                'price': float(document['price']),
                'image': document['img_url'],
                'released_date': str(date(day=random.choice(day), month=random.choice(month), year=random.choice(year))),
                'company': document['company']
            }
            # print(payload['released_date'])
            r = requests.post(url=base_url+'create_product/', data=payload)
            print(r.json())


def get_company(id=1):
    r = requests.get(url=f'{base_url}company/{id}')
    print(r.json())

def get_product(id=1):
    r = requests.get(url=f'{base_url}product/{id}')
    print(r.json())


def del_company(id=1):
    r = requests.post(url=f'{base_url}delete_company/{id}')
    print(r.json())


def del_product(id=1):
    r = requests.post(url=f'{base_url}delete_product/{id}')
    print(r.json())


del_company(id=15)