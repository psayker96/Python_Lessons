users = []
items = []
number_of_tries = 3

#Реєстрація
def registration():
    user_login = input("Створіть логін:")
    user_password = input("Створіть пароль:")
    if user_login not in [user['login'] for user in users]:
        user = {'login':user_login,'password':user_password}
        users.append(user)
        print("Ви успішно зареєструвались!")

#Логін
def login():
    user_login = input("Введіть логін:")
    user_password = input("Введіть пароль:")
    for user in users:
        if user_login == user['login'] and user_password == user['password']:
            print(f"Вітаємо вас в системі, {user_login}!")
            return user
        if user_login == user['login'] and user_password != user['password']:
            print("Невірний пароль!")

        
#Перевірка на наявність користувача
def check_try(user):
    global number_of_tries
    if user is None:
        number_of_tries -= 1
        if number_of_tries == 0:
            print("Вичерпано кількість спроб перезапустіть додаток")
        else:
            print(f"Залишилось спроб увійти в систему {number_of_tries}!")

#Додати товар
def add_item():
    items.append({'title':input("Введіть будь ласка назву товару:"),
                  'description':input("Введіть будь ласка опис товару:"),
                  'price':float(input("Введіть будь ласка ціну товара:"))})

#Показати весь товар
def show_all_items():
    for number,item in enumerate(items,1):
        print(f"{number}) {item['title']}")

#Редагувати та видалити обраний зі списку товар
def edit_item():
    show_all_items()
    number_item = input("Введіть номер товару, що необхідно відредагувати:")
    if number_item.isdigit() and 0 < int(number_item) <= len(items):
        number_item = int(number_item) - 1
        while True:
            choice_edit_item = input("""1 - Редагувати товар
2 - Видалити товар
q - Вийти
Оберіть опцію:""")
            if choice_edit_item == "1":
                item = items[number_item]
                item.update({'title':input("Введіть будь ласка назву товару:"),
                             'description':input("Введіть будь ласка опис товару:"),
                             'price':float(input("Введіть будь ласка ціну товара:"))})
            if choice_edit_item == "2":
                items.pop(number_item)
                print("Товар видалено!")
                break
            if choice_edit_item == "q":
                break

#Меню після логіну
def main_menu(user):
    while True:
        choice_store = input("""1 - Додати товар
2 - Переглянути увесь список товарів
3 - Редагувати товар
q - Вийти
Оберіть опцію:""")
        if choice_store == "1":
            add_item()
        elif choice_store == "2":
            show_all_items()
        elif choice_store == "3":
            edit_item()
        elif choice_store == "q":
            break
        else:
            print("Некорректно обрана опція!")


#Вхід або реєстрація
while True:
    choice_login = input("""1 - Зареєструватись
2 - Увійти
q - Вийти з програми
Оберіть опцію:""")
    if choice_login == "1":
        registration()
    elif choice_login == "2":
        if number_of_tries > 0:
            user = login()
            check_try(user)
            if user:
                main_menu(user)
        else:
            print("Crash!")
            break
    elif choice_login == "q":
        break
    else:
        print("Некорректно обрана опція!")

