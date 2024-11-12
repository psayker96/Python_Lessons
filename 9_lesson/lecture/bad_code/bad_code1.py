class User:
    def __init__(self,
                 login,
                 password,
                 admin_field1,
                 admin_field2,
                 admin_field3,
                 support_field1,
                 support_field2,
                 support_filed3):
        self.login = login
        self.password = password
        self.admin_field1 = admin_field1
        self.admin_field2 = admin_field2
        self.admin_field3 = admin_field3
        self.support_field1 = support_field1
        self.support_field2 = support_field2
        self.support_field3 = support_field3
    def admin_action1(self):
        pass # 40 стрічок
    def admin_action2(self):
        pass # 35 стрічок

    def support_action1(self):
        pass # 38 стрічок

    def support_action2(self):
        pass # 25 стрічок



class User:
    def __init__(self,
                 login,
                 password):
        self.login = login
        self.password = password


class Admin(User):
    def __init__(self,
               login,
               password,
               admin_field1,
               admin_field2,
               admin_field3):
        super().__init__(login,password)
        self.admin_field1 = admin_field1
        self.admin_field2 = admin_field2
        self.admin_field3 = admin_field3
    def admin_action1(self):
        pass # 40 стрічок
    def admin_action2(self):
        pass # 35 стрічок


# ДОПОВНИТИ ..............
