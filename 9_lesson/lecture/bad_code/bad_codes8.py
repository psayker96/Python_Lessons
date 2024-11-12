class User:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.__password = password

user = User()

# Створити повну копію записавши її до іншої комірки пам'яті
