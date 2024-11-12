from datetime import datetime

def hr():
    print("="*45)

#Товар
class Item:
    
    def create_item(self,
                    name,
                    description,
                    price):
        self.name = name
        self.description = description
        self.price = price

    def enter_item_params(self):
        self.name = input("Введіть назву товару:")
        self.description = input("Введіть опис товару:")
        self.price = round(float(input("Введіть ціну товару:")), 2)

    def show_item(self):
        print(f"""Назва товару {self.name}
Опис товару {self.description}
Ціна товару {self.price}""")

#Категорія
class Category:
    def __init__(self):
        self.categories = []

    def add_category(self):
        self.category = input("Додайте категорію:")
        self.categories.append(self.category)
    
    def show_category(self):
        print("Категорії товару:")
        for number,cat_name in enumerate(self.categories,1):
            print(f"{number}) {cat_name}")
        choice = int(input("Оберіть категорію товару зі списку:"))
        if 0 < choice <= len(self.categories):
            print(self.categories[choice - 1])
        else:
            print("Невірно обрана категорія!")

    def category_menu(self):
        while True:
            choice = input("""1 - Додати категорію
2 - Показати категорії списком та обрати одну
q - Вихід
Обрати опцію:""")
            if choice == "1":
                self.add_category()
            if choice == "2":
                self.show_category()
            if choice == "q":
                break

#Запис
class Record:

    def add_record(self):
        self.record = input("Enter record:")

    def show_record(self):
        print(self.record)


#Стаття
class Article:

    def __init__(self):
        self.articles = []

    def add_article(self):
        self.article = {'name':input("Введіть назву статті:"),
                        'text':input("Введіть текст статті:"),
                        'date_time':str(datetime.now())}
        self.articles.append(self.article)

    def print_articles(self):
        for number,art in enumerate(self.articles,1):
            print(f"{number}) {art}")

    def article_menu(self):
        while True:
            choice = input("""1 - Додати статтю
2 - Показати статті
q - Вийти
Оберіть опцію:""")
            if choice == "1":
                self.add_article()
            if choice == "2":
                self.print_articles()
            if choice == "q":
                break


while True:
    choice = input("""1 - Товари
2 - Категорія
3 - Запис
4 - Стаття
q - Вийти
Оберіть опцію:""")
    if choice == "1":
        hr()
        item = Item()
        item.enter_item_params()
        hr()
        item.show_item()
        hr()
    elif choice == "2":
        hr()
        category = Category()
        category.category_menu()
        hr()
    elif choice == "3":
        hr()
        record = Record()
        record.add_record()
        hr()
        record.show_record()
        hr()
    elif choice == "4":
        hr()
        art = Article()
        art.article_menu()
        hr()
    elif choice == "q":
        break
    else:
        hr()
        print("Невірна опція!")
        hr()
        


        
