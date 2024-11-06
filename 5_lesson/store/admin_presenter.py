from models import items
from lib import (view_items,
                 get_item_number,
                 get_item,
                 hr)

def create_item():
    item = {"name":input("Введіть назву товару:"),
            "description":input("Введіть опис товару:"),
            "price":float(input("Введіть ціну товару:"))}
    return item

def view_items(items):
    for number,item in enumerate(items,1):
        print(f"{number}) {item['name']}")

def admin_menu():
    print("Вітаємо в меню адміністратора!")
    while True:
        choice = input("""1 - Додати товар
2 - Переглянути товари
3 - Відобразити товар
4 - Оновити товар
5 - Видалити товар
q - Вийти
Обрати опцію:""")
        if choice == "1":
            item = create_item()
            items.append(item)
        if choice == "2":
            view_items(items)
        if choice == "3":
            item = get_item(items)
            if item:
                print(item)
        if choice == "4":
            item = get_item(items)
            if item:
                item.update(create_item())
        if choice == "5":
            item = get_item(items)
            if item_number is not None:
                items.pop(item_number)
        if choice == "q":
            break
        hr()
