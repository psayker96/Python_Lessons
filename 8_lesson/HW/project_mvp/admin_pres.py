from lib import *
from model import Admin,blogs

def admin_menu():
    admin = Admin()
    while True:
        choice = input("""1 - створити блог
2 - прочитати всі блоги
3 - прочитати 1 блог
4 - оновити блог
5 - видалити блог
q - вихід із системи
Оберіть опцію:""")
        if choice == "1":
            blog = admin.create_blog()
            blogs.append(blog)
        if choice == "2":
            view_blogs(blogs)
        if choice == "3":
            blog = get_blog(blogs)
            if blog:
                hr()
                blog.show() 
        if choice == "4":
            blog = get_blog(blogs)
            if blog:
                admin.update_blog(blog)
        if choice == "5":
            blog_number = get_blog_number(blogs)
            if blog_number is not None:
                blogs.pop(blog_number)
        if choice == "q":
            break
