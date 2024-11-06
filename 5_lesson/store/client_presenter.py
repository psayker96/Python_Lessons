from models import items,orders
from datetime import datetime
from lib import (view_items,
                 get_item_number,
                 get_item)
from order_presenter import order_menu

def create_order():
    order = {"name":input("ПІБ отримувача:"),
             "phone_or_email":input("Контактний телефон або email:"),
             "items":cart,
             "date_time":datetime.now(),
             "price":get_price(cart),
             "status":"wait"}
    return order

def get_price(cart):
    price = 0
    for item in cart:
        price += item["price"]
    return price

def client_menu():
    print("Вітаємо у меню клієнта!")
    cart = []
    while True:
        choice = input("""1- Показати усі товари
2 - Додати до кошику товар
3 - Переглянути усі товари в кошику
4 - Очистити кошик
5 - Замовити обрані товари
6 - Меню роботи із замовленнями
q - Вийти
Обрати опцію:""")
        if choice == "1":
            view_items(items)
        if choice == "2":
            item = get_item(items)
            if item:
                cart.append(item)
        if choice == "3":
            view_items(cart)
        if choice == "4":
            cart.clear()
        if choice == "5":
            order = create_order(cart)
            if order is not None:
                orders.append(order)
                print("Замовлення успішно додано!")
                cart = []
        if choice == "6":
            order_menu()
        if choice == "q":
            break
        hr()
