class User:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.password = password

class User1(User):
    def __init__(self,
                 login,
                 password,
                 user1_field1):
        super().__init__(login,password)
        self.user1_field1 = user1_field1

class User2(User):
    def __init__(self,
                 login,
                 password,
                 user2_field2):
        super().__init__(login,password)
        self.user2_field2 = user2_field2

class User3(User):
    def __init__(self,
                 login,
                 password,
                 user1_field3):
        super().__init__(login,password)
        self.user3_field3 = user3_field3

class User4(User):
    def __init__(self,
                 login,
                 password,
                 user1_field4):
        super().__init__(login,password)
        self.user3_field4 = user3_field4
