goods = []

while True:
    choice = input("""1 - Створити товар
2 - Список товарів
3 - Редагувати товар
q - вийти
Оберіть опцію:""")
    if choice == "1":
        goods.append({"title":input("Введіть назву товару:"),
                     "description":input("Введіть опис товару:"),
                     "price":float(input("Введіть ціну товара:"))})
        
    if choice == "2":
        print("*"*20)
        for number,item in enumerate(goods,1):
            print(f"{number})  {item['title']}")
            print("*"*20)

    if choice == "3":
        print("*"*20)
        for number,item in enumerate(goods,1):
            print(f"{number})  {item['title']}")
            print("*"*20)
        number = input("Введіть номер товару, що необхідно відредагувати:")
        if number.isdigit() and 0 < int(number) <= len(goods):
            number = int(number) - 1

            while True:
                choice_3 = input("""1 - Редагувати товар
2 - Видалити товар
q - вийти
Оберіть опцію:""")
                if choice_3 == "1":
                    item = goods[number]
                    item.update({"title":input("Нова назва товару:"),
                                 "description":input("Новий опис товару:"),
                                 "price":float(input("Нова ціна товара:"))})
                if choice_3 == "2":
                    goods.pop(number)
                    print("Товар видалено!")
                    break
                if choice_3 == "q":
                    break
    if choice == "q":
        break
       

                
                
