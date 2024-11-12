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


choice = input("1 2 3 or 4:")
while True:
    if choice == "1":
        user1 = User1("user1","pswrd1")
        users1.append(user1)
    elif choice == "2":
        user2 = User2("user2","pswrd2")
        users2.append(user2)
    elif choice == "3":
        user3 = User3("user3","pswrd3")
        users3.append(user3)
    elif choice == "4":
        user4 = User4("user4","pswrd4")
        users4.append(user4)
    else:
        user = None
        print(users1,
              users2,
              users3,
              users4)
        
