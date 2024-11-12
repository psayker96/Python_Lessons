class User1:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.password = password

class User2:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.password = password


class User3:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.password = password


class User4:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.password = password

choice = input("1 2 3 or 4:")
if choice == "1":
    user = User1()
elif choice == "2":
    user = User2()
elif choice == "3":
    user = User3()
elif choice == "4":
    user = User4()
else:
    user = None
print(f"Користучач {user}")
    

        
