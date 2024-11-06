'''
import requests

data = requests.get("https://t3.ftcdn.net/jpg/05/85/86/44/360_F_585864419_kgIYUcDQ0yiLOCo1aRjeu7kRxndcoitz.jpg").content

with open("new_image.png","wb") as file:
    file.write(data)
'''

'''
import pickle

#items = [{"name":"Товар",price:100}]

with open("db.txt","rb") as file:
    print(pickle.loads(file.read()))
'''

import json

items = [{"name":"Товар","price":100}]
with open("db3.txt","rb") as file:
    print(json.dumps(items))
    print(json.loads(file.read()))
