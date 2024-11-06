from datetime import datetime

class Blog:
    def __init__(self,
                 name,
                 title,
                 text):
        self.name = name
        self.title = title
        self.text = text
        self.date = datetime.now()
        self.comments = []

    def update(self):
        self.name = input("Введіть ім'я автора:")
        self.title = input("Введіть заголовок:")
        self.text = input("Введіть текст:")
        self.date = datetime.now()

    def show(self):
        print(f"""Заголовок {self.title}
Текст {self.text}
Дата {self.date}
Автор {self.name}""")
        

class Score:
    def __init__(self,value):
        self.value = value


class Comment:
    def __init__(self,
                 author="",
                 text="",
                 score=5):
        self.author = author
        self.text = text
        self.date = datetime.now()
        self.score = Score(score)

    def show(self):
        print(f"""Автор коментаря: {self.author}
Текст коментаря {self.text}
Оцінка {self.score.value}
Дата коментаря {self.date}""")

        



class Admin:
    def __init__(self):
        pass
    
    def create_blog(self):
        blog = Blog(name=input("Ім'я Автора:"),
                    title=input("Заголовок блогу:"),
                    text=input("Текст блогу:"))
        return blog

    def update_blog(self,blog):
        blog.update()


class Reader:
    def __init__(self,
                 name,
                 rate=Score(5)):
        self.name = name
        self.rate = rate
        self.date = datetime.now()

    def create_comment(self):
        comment = Comment(author=self.name,
                          text=input("Текст коментаря:"),
                          score=int(input("Оцінка:")))
        return comment






blogs = []


def view_blogs(blogs):
    for number,blog in enumerate(blogs,1):
        print(f"{number}) {blog.title}")

def get_blog_number(blogs):
    view_blogs(blogs)
    number = input("Оберіть номер блогу:")
    if number.isdigit() and 0 < int(number) <= len(blogs):
        return int(number) - 1

def get_blog(blogs):
    blog_number = get_blog_number(blogs)
    if blog_number is not None:
        return blogs[blog_number]

def hr():
    print("="*45)




    
def admin_menu():
    admin = Admin()
    while True:
        choice = input("""1 створити блог
2 прочитати всі блоги
3 прочитати 1 блог
4 оновити блог
5 видалити блог
q вихід із системи:""")
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
        hr()
        

def blog_menu(blog,reader):
    while True:
        choice = input("""1 читати блог
2 читати коментарі блогу
3 залишити коментар
q до попереднього меню:""")
        if choice == "1":
            blog.show()
        if choice == "2":
            for comment in blog.comments:
                comment.show()
                hr()
        if choice == "3":
            blog.comments.append(reader.create_comment())
        if choice == "q":
            break
        hr()


def reader_menu():
    reader = Reader(name=input("Ваше Ім'я:"))

    while True:
        choice = input("""1 дивитись всі блоги
2 працювати із 1 блогом
q вихід із системи:""")
        if choice == "1":
            view_blogs(blogs)
        if choice == "2":
            blog = get_blog(blogs)
            if blog:
                blog_menu(blog,reader)
        if choice == "q":
            break
    


while True:
    choice = input("1 Ви адмін 2 Ви читач q вихід:")
    if choice == "1":
        admin_menu()
    if choice == "2":
        reader_menu()
    if choice == "q":
        break







