'''
try:
    number = int(input("Введіть число:"))
except:
    print("Виникла помилка!")
    
try:
    number = int(input("Введіть число:"))
except Exception as e:
    print(f"Виникла помилка: {e}")
    
try:
    print(1/0)
except ZerroDivisionError:
    print("Виникла помилка!")
except Exception as e:
    print(f"Виникла помилка: {e}")
    
try:
    text = "Hello"
    text.new_command
except Exception as e:
    print(f"Виникла помилка: {e}")
    
try:
    data = []
    data = [1]
except Exception as e:
    print(f"Виникла помилка: {e}")

try:
    text1 = "Hello"
    def action():
        text1 += "World!"
    action()
except Exception as e:
    print(f"Виникла помилка: {e}")
    
def hard_number_work(number1:int):
    if type(number1) != int:
        raise ValueError("Некорректний тип даних")
        
hard_number_work("1")        
'''

'''
with open("file1.png","rb") as file,\
     open("file2.png","rb") as file2,\
     open("new_file.png","wb") as result_file:
    result_file.write(file.read())
    result_file.write(file2.read())
'''

'''
with open("file1.png","rb") as file,\
     open("file2.png","rb") as file2,\
     open("new_file.png","wb") as result_file:
    size = len(file1.read())
    result_file.seek(size)
    file.write(result_file.read())
'''


items = [{"name":"Товар","price":100}]

with open("db3.txt","r") as file:
    print(file.read()[0])


'''
#Закодувати до байтів
import pickle

items = [{"name":"Товар",price:100}]

print(pickle.dumps(items))
'''
