# blog title:str text:str
# CRUD

from pickle import dumps,loads
import os

DB = "db.png"

def show_blogs(blogs):
    for number,blog in enumerate(blogs,1):
        print(f"{number}) {blog['title']}")
        
def create_blog():
    blog = {"title":input("Заголовок:"),
            "text":input("Текст:")}
    return blog

def get_blog_number(blogs):
    show_blogs(blogs)
    blog_number = input("Оберіть номер блогу:")
    if blog_number.isdigit() and 0 < int(blog_number) <= len(blogs):
        return int(blog_number) - 1

def get_blog(blogs):
    blog_number = get_blog_number(blogs)
    if blog_number is not None:
        return blogs[blog_number]

def read_from_file(filename):
    with open(filename,"rb") as file:
        return loads(file.read())

def write_to_file(filename,data):
    with open(filename,"wb") as file:
        file.write(dumps(data))

if not os.path.exists(DB):
    write_to_file(DB,[])   


while True:
    choice = input("""1 додати блог
2 переглянути всі блоги
3 детальний перегляд одного блогу
4 оновити блог
5 видалити певний блог
q вихід із системи:""")
    if choice == "1":
        blogs = read_from_file(DB)
        blogs.append(create_blog())
        write_to_file(DB,blogs)
    if choice == "2":
        blogs = read_from_file(DB)
        show_blogs(blogs)
    if choice == "3":
        blogs = read_from_file(DB)
        blog = get_blog(blogs)
        print(blog)
    if choice == "4":
        blogs = read_from_file(DB)
        blog = get_blog(blogs)
        blog.update(create_blog())
        write_to_file(DB,blogs)
    if choice == "5":
        blogs = read_from_file(DB)
        blog_number = get_blog_number(blogs)
        blogs.pop(blog_number)
        write_to_file(DB,blogs)
    if choice == "q":
        break
    print("="*40)


# Синхронізація даних

#from pickle import dumps,loads
'''
from json import dumps,loads
import os

def create_blog():
    blog = {"title":input("Заголовок:"),
            "text":input("Текст:")}
    return blog

def show_blogs(blogs):
    for number,blog in enumerate(blogs,1):
        print(f"{number}) {blog['title']}")

def get_blog_number(blogs):
    show_blogs(blogs)
    blog_number = input("Оберіть номер блогу:")
    if blog_number.isdigit() and 0 < int(blog_number) <= len(blogs):
        return int(blog_number) - 1

def get_blog(blogs):
    blog_number = get_blog_number(blogs)
    if blog_number is not None:
        return blogs[blog_number]
      
def read_from_file(filename):
    with open(filename,"r") as file:
        return loads(file.read())

def write_to_file(filename,data):
    with open(filename,"w") as file:
        file.write(dumps(data))

DB = "db2.txt"

if not os.path.exists(DB):
    write_to_file(DB,[])

blogs = read_from_file(DB)

while True:
    choice = input("""1 додати блог
2 переглянути всі блоги
3 детальний перегляд одного блогу
4 оновити блог
5 видалити певний блог
q вихід із системи:""")
    if choice == "1":
        blogs.append(create_blog())   
    if choice == "2":
        show_blogs(blogs)
    if choice == "3":
        blog = get_blog(blogs)
        print(blog)
    if choice == "4":
        blog = get_blog(blogs)
        blog.update(create_blog())
    if choice == "5":
        blog_number = get_blog_number(blogs)
        blogs.pop(blog_number)
    if choice == "q":
        break
    write_to_file(DB,blogs)
    print("="*40)

'''
