# дані впроваджувати до тексту

#name = 10

# Форматований текст
'''
print(f"Вітаємо Вас {name} !!!")
'''

# 1 виконати дію 1 2 виконати дію 2 3 виконати дію 3
'''
choice = input("""1 виконати дію 1
2 виконати дію 2
3 виконати дію 3
q вихід із програми:""")
'''

# number = input("Введіть дробове число:")
# print(number.isdigit())
# SPLIT - розбити стрічку на дільник
# print(number.split('.'))


# name1 = "Товар 1"
# description1 = "Опис товару 1"
# price = 100

# Структура даних

# 1 СПИСОК LIST
# 2 СЛОВНИК DICT

'''
numbers = [1,3,2,4,34,5,35,345,345,345,345,34,534,53,53,1,1,1,1,1,1,12,312,321,321,321,321,1,1,1,1,1]
print(numbers.count(345))
# help([])

numbers = [1,1,1,1,1,2,2,3,3,33,1,1,1,1,1]
print(len(numbers))

'''
# text = "hello World"
# text.upper()
# print(text)

# data = [1,2,3,4]
# print(data.append(5))
# print(data)

# number = 100000000000000000000000000000000000000000000000000000
# print(id(number))
# number = 5
# print(id(number))

# М'яке копіювання
'''
data = [1,2,3,4,5,6,7,8,9]
data2 = data.copy()

data2.append(10)
print(data)
'''

# elements = [1,1,1,2.2,2.3,2.7,"Hello World",[1,2,3,4,5,6,7]]
# print(elements[7][0])
# БАЗИ ДАНИХ
# items = ["Товар 1","Опис товару 1",157,24,"01001","27","Factory"]

# Словник Dict - структура для опису одного але великого об'єкту



# Журнал заміток

# Додавати замітки
# Читати
# Редагувати
# Видаляти
# Приводити до стрічки

# Замітка містить Заголовок текст опис замітки


# while  допоки

# CREATE
# READ
# UPDATE
# DELETE


notes = []

while True:
    choice = input("""1 додати замітку
2 читати всі замітки
3 робота із однією заміткою
q вихід із системи:""")
    if choice == "1":
        notes.append({"title":input("Введіть заголовок замітки:"),
                      "description":input("Введіть опис замітки:"),
                      "text":input("Введіть текст замітки:")})
    if choice == "2":
        print("-"*25)
        for number,note in enumerate(notes,1):
            print(f"{number}) {note['title']}")
            print("-"*25)

    if choice == "3":
        print("-"*25)
        for number,note in enumerate(notes,1):
            print(f"{number}) {note['title']}")
            print("-"*25)
        number = input("Оберіть номер замітки:")
        if number.isdigit() and 0 < int(number) <= len(notes):
            number = int(number) - 1

            while True:
                new_choice = input("""1 читати замітку
2 редагувати
3 видалити
4 до попереднього меню:""")
                if new_choice == "1":
                    print(notes[number])
                if new_choice == "2":
                    note = notes[number]
                    note.update({"title":input("Новий заголовок:"),
                                 "descripion":input("Новий опис:"),
                                 "text":input("Новий текст:")})
                if new_choice == "3":
                    notes.pop(number)
                    break
                if new_choice == "4":
                    break
                
    if choice == "q":
            break

    print("="*45)

# Нумерація структур даних (enumerate
'''
'''
users = ["User1","User2","User3","User4","User5"]
result = dict(enumerate(users,1))
print(result)

for key,value in result.items(): #[(key,value)]
    print(key,value)


# DRY
'''
number = input("Введіть дробове число:")
number_data = number.split(".")
if number_data[0].isdigit() and number_data[1].isdigit():
    print("Наше число дробове")
'''
# zip команда об'єднання
'''
data = [1,2,3,4,5]
data2 = [100,200,300,400,500]

print(list(zip(data,data2)))
'''
'''
data1 = {"1":"1","2":"2","3":"3","4":"4"}
data2 = {"100":100,"200":200,"300":300,"400":400}

# сформсувати словник де ключами будуть ключі із data1 а значеннями значення із dta2

print(dict(zip(data1.keys(),
               data2.values())))

'''
# Користувач вводить число у змінну  number
# Якщо ввін увів корректно виписати вітаємо Ви ввели число і те що було введенол




