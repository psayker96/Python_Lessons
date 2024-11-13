import copy

class UserMixin:
    def copy_user(self):
        return copy.deepcopy(self)

class User(UserMixin):
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.__password = password

user = User("User","Password")

user2 = user.copy_user()
print(id(user))
print(id(user2))
