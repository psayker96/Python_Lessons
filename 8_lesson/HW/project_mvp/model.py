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
