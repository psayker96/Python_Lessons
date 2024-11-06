users = []

def login():
    user_login = input("Логін користувача:")
    user_password = input("Пароль користувача:")
    for user in users:
        if user_login == user["login"] and user_password == user["password"]:
            print(f"Ви увійшли як {user_login}")
            return user

def registration():
    user_login = input("Логін користувача:")
    user_password = input("Пароль користувача:")
    if user_login not in [user["login"] for user in users]:
        user = {"login":user_login,"password":user_password}
        users.append(user)
        print("Зареєстровані успішно")

number_of_try = 3 

def check_try(user):
   global number_of_try
   if user is None:
       number_of_try -= 1
       print(f"Кількість спроб {number_of_try}")
   else:
       print("Вичерпано кількість спроб перезапустіть додаток") 


def main_menu(user):
    print(f"Вітаємо Вас користувач: {user['login']}")
    while True:
        choice = input("q для виходу:")
        if choice == "q":
            break


while True:
    choice = input("1 registration 2 login q exit:")
    if choice == "1":
        registration()
    if choice == "2":
        if number_of_try > 0:
            user = login()
            check_try(user)
            if user:
                main_menu(user)
                
    if choice == "q":
        break