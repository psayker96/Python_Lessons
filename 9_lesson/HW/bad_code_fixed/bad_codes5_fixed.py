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

while True:
    choice = input("1 2 3 or 4:")
    if choice == "1":
        user = User1("user1","pswrd1")
    elif choice == "2":
        user = User2("user2","pswrd2")
    elif choice == "3":
        user = User3("user3","pswrd3")
    elif choice == "4":
        user = User4("user4","pswrd4")
    else:
        user = None
    print(f"Користучач {user}")
    

        
