from models import order,available_status
from lib import hr

def view_orders(orders):
    for key,value in available_status:
        print(f"{number}) {status}")
    status = input("Введіть номер потрібного статусу:")
    if status in available_status:
        status = available_status.get(status_number)
    current_orders = [order for order in orders if orders['status'] == status]
    for number,order in enumerate(current_orders,1):
        print(f"""{number})
{order}""")
        hr()

def order_menu():
    print("Вітаємо у меню із замовленнями!")
    while True:
        choice = input("""1 - Відобразити всі замовлення
2 - Детальний перегляд замовлення
3 - Підтвердити замовлення
4 - Відхилити замовлення
5 - Доопрацювання
q - Вихід із системи
Обрати опцію:""")
        if choice == "1":
            view_orders(orders)
        if choice == "2":
            pass
        if choice == "3":
            pass
        if choice == "4":
            pass
        if choice == "5":
            pass
        if choice == "q":
            break
        hr()
