coins_per_work = 100

class BigCompany:
    def __init__(self,workers):
        self.workers = workers

    def get_taxes(self):
        return (self.workers * coins_per_work) * 0.1

class MiddleCompany:
    def __init__(self,workers):
        self.workers = workers

    def get_taxes(self):
        return (self.workers * coins_per_work) * 0.15

class SmallCompany:
    def __init__(self,workers):
        self.workers = workers

    def get_taxes(self):
        return (self.workers * coins_per_work) * 0.25

tax = 0

companies = [BigCompany(100),
             MiddleCompany(50),
             MiddleCompany(50),
             SmallCompany(15),
             SmallCompany(15),
             SmallCompany(15),
             SmallCompany(15),]

for company in companies:
    tax += company.get_tax()
print(tax)
