'''
class Item:
    name = ""
    description = ""
    price = 0

    def show(self):
        print(f"""Назва товару {self.name}
Опис товару {self.description}
Ціна товару {self.price}""")

item1 = Item()
item1.price = 100

item2 = Item()

print(item1.price)
item2.show()
'''

#Спадкування
'''
class Article():
    title = "1"
    description = "2"
    text = "3"

class PapperArticle(Article):
    paper = ""

article1 = PapperArticle()
print(article1.text)
'''

#Поліморфізм
'''
class Article():
    title = "1"
    description = "2"
    text = "3"

class PapperArticle(Article):
    title = "11"
    paper = ""

article1 = PapperArticle()
print(article1.title)
'''

#Інкапсуляція

#public - публічні дані 
#protected - умовний захист self._data
#private - приватны дані self.__data

'''
class Data():
    def __init__(self,
                 field1,
                 field2,
                 field3):
        self.__field1 = field1
        self.__field2 = field2
        self.__field3 = field3

    def action(self):
        print(self.__field1)

data = Data(1,2,3)
print(data.__dict__)
'''

#Спадкування
#Композиція(агрегація)
'''
class Cart():
    def __init__(self):
        self.items = []

class Client():
    cart = Cart()


client = Client()

print(client.cart.items)
'''

'''
from pickle import dumps,loads
from json import dumps as jdumps,loads as jloads
import os

class FileWorker:
    def __init__(self,filename):
        self.filename = filename


    def read(self):
        with open(self.filename,"rb") as file:
            return loads(file.read())

    def write(self,data):
        with open(self.filename,"wb") as file:
            file.write(dumps.data)

class JsonFileWorker:
    def __init__(self,filename):
        self.filename = filename


    def read(self):
        with open(self.filename,"r") as file:
            return jloads(file.read())

    def write(self,data):
        with open(self.filename,"w") as file:
            file.write(jdumps.data)
        
class DB():
    def __init__(self,filename):
        self.data = []
        self.file_worker = FileWorker(filename)

        if not os.path.exists(filename):
            self.file_worker.write([])
        else:
            self.file_worker.read()
        
    def save(self):
        self.file_worker.write(self.data)

    def append(self,element):
        self.data.append(element)
        self.save()

    def pop(self,number):
        self.data.pop(number)
        self.save()

    def remove(self,element):
        self.data.remove(element)
        self.save()

db = DB("db.txt")

for number in range(100)
db.append(number)

print(db.data)
'''


        
        




