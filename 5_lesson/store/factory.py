from models import items,orders,admins
from random import uniform

def create_item():
    item = {"name":input("Введіть назву товару:"),
            "description":input("Введіть опис товару:"),
            "price":float(input("Введіть ціну товару:"))}
    return item
 
def create_item(count):
    for number in range(count):
        item = {"name":f"Товар номер {number}",
        "description":f"Опис товару {number}"
        "price":uniform(1,1000)}
    items.append(item)
    
create_item(25)
admins.append[{"login":"admin","password":"123"}]