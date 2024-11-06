# 1 TRY EXCEPT
'''
try:
    text = "Hello"
    def action():
        text += "!!!"
    action()
except ZeroDivisionError:
    print("Ділення на 0")
except Exception as e:
    print(f"Виникли помилки {e}")
print("END")
'''
'''
def hard_number_work(number:int):
    if type(number) != int:
        raise ValueError("Некорретний тип даних")

hard_number_work("1")
'''  
# 2 TRY DECORATOR
'''
def try_decorator(action):
    def wrapper(*args,**kwargs):
        try:
            return action(*args,**kwargs)
        except Exception as e:
            print("нажаль виникла помилка")
    return wrapper

@try_decorator
def get_number():
    number = input("Введіть номер:")
    return int(number)

get_number()
'''
# 3 FILES

# RAM

# ROM

# open() Відкрити
# open(filename,режим)

# R - читання
# W - перезапису
# A - дозапису
# ---------------------
# READ FILES
'''
file = open("db.txt","r")
# read() - прочитати все
# readlines - прочитати все порядково
#print(file.read())
#file.seek(0)
#print(file.read())

data = file.readlines()
for line in data:
    print(line.strip())

file.close()
'''
# WRITE

# file = open("db2.txt","a")
# write(data) - записати до файлу data:str - що записати до файлу
# file.write("Вітаємо у програмі")
# file.close()

# Контекстний менеджер
'''
with open("db.txt","r") as file1,\
     open("db2.txt","w") as file2:
    file2.write(file1.read())
'''
# TXT DOC DOCX ODF Для запису
'''
with open("db.txt","r") as file1,\
     open("db2.pdf","w") as file2:
    file2.write(file1.read())
'''

# RB  WB  AB
# B - bytes
# БАЗОВЕ КОДУВАННЯ ІНФОРМАЦІЇ
'''
with open("graph.png","rb") as file,\
     open("2.png","rb") as file2,\
     open("new_image.png","wb") as result_file:
    result_file.write(file.read())
    result_file.write(file2.read())
'''
'''
with open("new_image.png","rb") as result_file,\
     open("graph.png","rb") as file1,\
     open("secret.png","wb") as file2:
    size = len(file1.read())
    result_file.seek(size)
    file2.write(result_file.read())
'''

# Завантаження файлів із інтернету
'''
import requests

data = requests.get("https://t3.ftcdn.net/jpg/05/85/86/44/360_F_585864419_kgIYUcDQ0yiLOCo1aRjeu7kRxndcoitz.jpg").content

with open("new_image.png","wb") as file:
    file.write(data)
'''

# РОБОТА ІЗ ЗМІНИМИ
'''
items = [{"name":"Товар 1","price":100}]

with open("db.txt","r") as file:
    print(file.read()[0])
'''
# дані -> bytes (із типами і службовою інформацією) -> до файлу
# считати і перекодувати
# СЕРІАЛІЗАЦІЯ ДАНИХ

# import pickle
# закодувати до байтів dumps
# items = [{"name":"Товар 1","price":100}]
# декодувати loads
'''
with open("db.txt","rb") as file:
    print(type(pickle.loads(file.read())))
'''
# JSON
'''
import json

items = [{'name':'Товар 1','price':100}]

# dumps - кодувати loads - декодувати
print(json.dumps(items))
'''
'''
with open("db.txt","r") as file:
    print(json.loads(file.read()))
'''