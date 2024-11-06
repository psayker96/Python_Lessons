users = []

def login():
    user_login = input("Enter login:")
    user_password = input("Enter password:")
    for user in users:
        if user_login == user["login"] and user_password == ["password"]:
            print(f"Successfully logged in as {user_name}!")

def registration():
    user_login = input("Enter login:")
    user_password = input("Enter password:")
    if user_login not in [user["login"] for user in users]:
        user = {"login":user_login,"password":user_password}
        users.append(user)
        print("Registration successfully completed")

number_of_try = 3

def check_try(user):
    global number_of_try
    if user is None:
        number_of_try -= 1
        print(f"Tries left {number_of_try}")
    else:
        print("All tries are wasted!")

def main_menu(user):
    print(f"Welcome, {user['login']}")
    while True:
        choice = input("Enter option:")
        if choice == "q":
            break
        
while True:
    choice = input("""1 - Regestration
2 - Login
q - Exit
Enter option:""")
    if choice == "1":
        registration()
    if choice == "2":
        user = login()
        check_try(user)
        if user:
            main_menu(user)
    if choice == "q":
        break
