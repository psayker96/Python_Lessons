class User:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.password = password
        
class User1(User):
    def __init__(self,
                 login,
                 password):
        super().__init__(login,password)

class User2(User):
    def __init__(self,
                 login,
                 password):
        super().__init__(login,password)

class User3(User):
    def __init__(self,
                 login,
                 password):
        super().__init__(login,password)

class User4(User):
    def __init__(self,
                 login,
                 password):
        super().__init__(login,password)

users1 = []
users2 = []
users3 = []
users4 = []



while True:
    choice = input("1 2 3 or 4:")
    if choice == "1":
        user = User1("user1","pswrd1")
        users1.append(user)
        print(users1)
    elif choice == "2":
        user = User2("user2","pswrd2")
        users2.append(user)
        print(users2)
    elif choice == "3":
        user = User3("user3","pswrd3")
        users3.append(user)
        print(users3)
    elif choice == "4":
        user = User4("user4","pswrd4")
        users4.append(user)
        print(users4)
    else:
        user = None
        print(users1,
              users2,
              users3,
              users4)
        
