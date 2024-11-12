# 1 запитати файли які необхідно закодувати
# 2 отримати інформацію назва розмір .....
# 3 отриману інформацію по файлам зберігти у файл із даними (.txt)
# 4 всі прочитані дані записати у результуючий який обирає користувач
from json import dumps,loads

def info_about_file(filename):
    with open(filename,"rb") as file:
        data = {"name":filename,
                "size":len(file.read())}
        return data

def get_all_data():
    data = []
    while True:
        filename = input("Ім'я файлу або q для завершення:")
        if filename == "q":
            break
        data.append(info_about_file(filename))
    return data

def coding_menu():
    filedata = None
    base_path = "coding/"
    while True:
        choice = input("1 кодувати q вихід:")
        if choice == "1":
            filedata = get_all_data()
            with open(base_path + "files_data.txt","w") as file:
                file.write(dumps(filedata))
            result_file = input("Введіть назву файлу куди необхідно зберегти інформацію:")
            with open(base_path + result_file,"wb") as result_file:
                for data in filedata:
                    with open(data["name"],"rb") as file:
                        result_file.write(file.read())
        if choice == "q":
            break
