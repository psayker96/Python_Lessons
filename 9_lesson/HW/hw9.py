class MyData:
    def __add__(self, other):
        return 10

    def __sub__(self, other):
        return 100

    def __str__(self):
        return "String"

    def __int__(self):
        return 123

data = MyData()

# Додавання
result_add = data + 5  
print(result_add)

# Віднімання
result_sub = data - 5  
print(result_sub)

# Перетворення в рядок
result_str = str(data)
print(result_str)

# Перетворення в число
result_int = int(data)
print(result_int)
