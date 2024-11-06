from models import admins
from admin_presenter import admin_menu

def login(users):
    user_login = input("Логін:")
    user_password = input("Пароль:")
    for user in users:
        if (user['login'] == user_login and
            user['password'] == user_password)
            return user

def auth_menu():
    print("Вітаємо у меню аутентифікації!")
    
    while True:
        choice = input("""1 - Вхід
q - Вихід
Оберіть опцію:""")
        if choice == "1":
            user = login()
            if admin:
                admin_menu()
        if choice == "q":
            break