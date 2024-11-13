class Item:
    price = 10

class DiscontItem(Item):
    discount = 5
    
    @property
    def price(self):
        return super().price - self.discount

class Box:
    def __init__(self, items=[]):
        self.items = items
    
    def total_price(self):
        total = 0
        for item in self.items:
            total += item.total_price() if hasattr(item, 'total_price') else item.price
        return total

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.total_price() if hasattr(item, 'total_price') else item.price
        return total

'''
Пояснення:

Клас DiscontItem:

Використано @property для динамічного обчислення ціни з урахуванням знижки.
Клас Box:

Метод total_price рекурсивно обчислює загальну вартість, перевіряючи, чи має елемент метод total_price (для Box і Cart).
Клас Cart:

Метод add_item додає елемент до кошика.
Метод total_price аналогічний методу Box, але використовується для підрахунку загальної вартості всіх елементів в кошику.
'''

# Створення об'єктів
item1 = Item()
discont_item = DiscontItem()
box1 = Box([item1, discont_item])
box2 = Box([box1, Item()])

# Створення кошика та додавання елементів
cart = Cart()
cart.add_item(item1)
cart.add_item(discont_item)
cart.add_item(box2)

# Розрахунок загальної вартості
total_price = cart.total_price()
print(total_price)

'''
Ключові моменти:

Рекурсія: Використання рекурсії в методах total_price дозволяє обробляти вкладені структури (коробки в коробках).
Поліморфізм: Завдяки поліморфізму, метод total_price може бути викликаний для різних типів об'єктів (Item, DiscontItem, Box), і він буде поводитися відповідно.
Простий інтерфейс: Клас Cart має простий інтерфейс для додавання елементів та підрахунку загальної вартості.
Можливі розширення:

Різні типи знижок: Можна додати класи з різними типами знижок (відсоткова, фіксована сума).
Податки: Можна додати розрахунок податків.
Збереження кошика: Можна зберегти дані кошика в базу даних або файл.
Цей код забезпечує гнучку та розширювану систему для обчислення вартості товарів в кошику, враховуючи різні типи товарів та їх вкладеність.
'''
