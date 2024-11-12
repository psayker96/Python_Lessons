import copy

class User:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.__password = password

user = User("user","pswrd")
user1 = copy.deepcopy(user)
print(user)
print(user1)

# Створити повну копію записавши її до іншої комірки пам'яті
