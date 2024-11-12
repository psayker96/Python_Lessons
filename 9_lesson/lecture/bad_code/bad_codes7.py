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

users1 = []
users2 = []
users3 = []
users4 = []


choice = input("1 2 3 or 4")

if choice == "1":
    user = User1()
    users1.append(user)
if choice == "2":
    user = User2()
    users2.append(user)
if choice == "3":
    user = User3()
    users3.append(user)
if choice == "4":
    user = User4()
    users4.append(user)

print(users1,
      users2,
      users3,
      users4)
        
