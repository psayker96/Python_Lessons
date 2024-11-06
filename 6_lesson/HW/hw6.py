#Task1
print("Task 1")
print("="*45)

with open("task1.txt","w") as file:
    for numbers in range(1,101):
        file.write(str(numbers) + '\n')

print("Це інформативне повідомлення, що код завдання 1 спрацював!")          
print("="*45)

#Task2
print("Task 2")
print("="*45)

filename = input("Введіть назву файлу у форматі *.txt, де * ім'я файлу(наприклад, task1.txt):")
file_1 = open(filename,"r")
print(file_1.read())
print("="*45)

#Task3
print("Task 3")
print("="*45)

with open("image.png","rb") as source_image,\
     open("1.png","wb") as destination_image:
    destination_image.write(source_image.read())

print("Це інформативне повідомлення, що код завдання 3 спрацював!") 
print("="*45)
