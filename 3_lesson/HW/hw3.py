data = [1,2,31,23,213,213,123,1,1,1,21,2,3,231,2321,31,31,23,13,2,23,23,2,2321]
data2 = [3,2,4,34,5,45,6,65,756,4,56,856,756,67,856,234,54,754,235,547,34,346,455,3,54,634,434,634,5,2345]

print(f"Список data: {data}")
print(f"Список data2: {data2}")

"""
Вивести унікальні елементи в обох списках або позбутись дублювання,
завдання 1 та 2 мають схожу мету, але по різному сфорульоване
"""

data_1 = list(set(data))
data2_1 = list(set(data2))
print(f"Вивести унікальні елементи в списку data: {data_1}!")
print(f"Вивести унікальні елементи в списку data2: {data2_1}!")
print(f"Вивести унікальні елементи в обох списках: {data_1 + data2_1}!")

#Знайти перетин обох списків
data_set = set(data)
data2_set = set(data2)
print(f"Вивід перетину обох списків: {data_set.intersection(data2_set)}!")





