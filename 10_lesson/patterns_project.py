# 2 типи користувачів admin із власною бд клієнт із власною бд
# Адміністрато може створювати 2 типи товарів 1 звичайний 2 акційний
# Товар може бути 2 різних кольорів
# Клієнт може додавати до кошику будь який товар в бідь якій кількості
# і дізнаватись загальну вартість



# ДОДАТИ КЛАС КОРИСТУВАЧА ПІДТРИМКИ ІЗ ВЛАСНОЮ БД І МЕНЮ









class Cart:
    def __init__(self,items=[]):
        self.items = items
        

class Item: # КОМПОНІВНИК ДЛЯ ЦІНИ
    def __init__(self,
                 name="",
                 price=0):
        self.name = name
        self.price = price

    def set_data(self):
        self.name = input("Вкажіть назву:")
        self.price = float(input("Вкажіть ціну:"))

class DiscontItem(Item):
    def __init__(self,
                 name="",
                 price=0,
                 discont=0):
        super().__init__(name,price)
        self.discont = discont
        
    def set_data(self):
        super().set_data()
        self.discont = float(input("Вкажіть знижку:"))
    

class ClientAdapter:
    def __init__(self,
                 item,
                 count):
        # pass ..............



def get_item_class(item_type):
    available_types = {"1":Item,
                       "2":DiscontItem}
    return available_types.get(item_type)

items = []
        

class User:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.__password = password

    def check_data(self,
                   login,
                   password):
        if (self.login == login and
            self.__password == password):
            return True
        else:
            return False
        

class Admin(User):
    pass

class Client(User):
    def __init__(self,
                 login,
                 password):
        super().__init__(login,password)
        self.cart = Cart()

class Support(User):
    pass

admins = []
clients = []
supports = []

def support_menu(support):
    print("МЕНЮ ПІДТРИМКИ")
    while True:
        choice = input("q exit:")
        if choice == "q":
            break

def admin_menu(admin):
    # ДОРЕАЛІЗУВАТИ
    print("МЕНЮ АДМІНІСТРАТОРА")
    while True:
        choice = input("""1 create
2 read all
3 read one
4 udapte
5 delete
q exit:""")
        if choice == "1":
            item_type = input("1 звичайний 2 акційний:")# "1"
            item_class = get_item_class(item_type)# Item
            if item_class:  # True
                item = item_class()  # ПОРОЖНІЙ ITEM
                item.set_data()
                items.append(item)
        if choice == "2":
            # 1 отримати список товарів
            # 2 вивести номер і назву товару починаючи із 1
        if choice == "3":
            # 1 вивести товари
            # 2 запитати номер
            # 3 перевірити номер
            # 4 отримати за номером
            # 5 вивести інформацію
        if choice == "4":
            pass
        if choice == "5":
            pass
        if choice == "q":
            break


def client_menu(client):
    print("МЕНЮ КЛІЄНТА")
    while True:
        choice = input("""1 read all
2 add to cart
3 view cart
4 clear cart
5 get_price
q exit:""")
        if choice == "1":
            pass
        if choice == "2":
            pass
        if choice == "3":
            pass
        if choice == "4":
            pass
        if choice == "5":
            pass
        
        if choice == "q":
            break






        


class UserFactory:
    available_users = {"admin":{"class":Admin,
                                "db":admins,
                                "menu":admin_menu},
                       "client":{"class":Client,
                                 "db":clients,
                                 "menu":client_menu},
                       "support":{"class":Support,
                                 "db":supports,
                                 "menu":support_menu}}
    def get_class(self,user_type):
        data = self.available_users.get(user_type)
        return data["class"]
    def get_db(self,user_type):
        data = self.available_users.get(user_type)
        return data["db"]
    def get_menu(self,user_type):
        data = self.available_users.get(user_type)
        return data["menu"]
    
user_factory = UserFactory()


def registration(user_type):
    db = user_factory.get_db(user_type)
    user_login = input("Введіть логін:")
    user_password = input("Введіть пароль:")
    if user_login not in [user.login for user in db]:
        user_class = user_factory.get_class(user_type)
        user = user_class(user_login,user_password)
        db.append(user)


def login(user_type):
    db = user_factory.get_db(user_type)
    user_login = input("Введіть логін:")
    user_password = input("Введіть пароль:")
    for user in db:
        if user.check_data(user_login,user_password):
            return user


available_types = {"1":"admin",
                   "2":"client",
                   "3":"support"}


def auth_menu(user_type):
    while True:
        choice = input("1 registration 2 login q exit:")
        if choice == "1":
            registration(user_type)
        if choice == "2":
            user = login(user_type)
            if user:
               menu =  user_factory.get_menu(user_type)
               menu(user)
        if choice == "q":
            break


while True:
    choice = input("1 admin 2 client q exit:")
    if choice == "q":
        break
    if choice in available_types:
        user_type = available_types.get(choice)
        auth_menu(user_type)







# 1 РОЗБИТИ НА ФАЙЛИ MVP
# 2 ДОРЕАЛІЗУВАТИ ЧИСТИНУ АДМІНІСТРАТОРА
# 3 ДОРЕАЛІЗУВАТИ КЛІЄНТСЬКИЙ АДАПТЕР
# 4 РЕАЛІЗУВАТИ ЧАСТИНУ КЛІЄНТА











