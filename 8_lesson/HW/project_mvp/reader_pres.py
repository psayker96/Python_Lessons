from lib import *
from model import Reader,blogs

def reader_menu():
    reader = Reader(name=input("Ваше Ім'я:"))

    while True:
        choice = input("""1 - дивитись всі блоги
2 - працювати із 1 блогом
q - вихід із системи
Оберіть опцію:""")
        if choice == "1":
            view_blogs(blogs)
        if choice == "2":
            blog = get_blog(blogs)
            if blog:
                blog_menu(blog,reader)
        if choice == "q":
            break
