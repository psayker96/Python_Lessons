# 1 запитати файл із даними
# 2 запитати результуючий файлу
# 3 прочитати результуючий файл
# 4 і почастинно записати із назвами попередніх файлів
from json import loads

def decoding():
    result_file = input("Результуючий файл:")
    file_data = input("Файл із даними:")

    with open(file_data,"r") as file:
        file_data = loads(file.read())
    
    with open(result_file,"rb") as result_file:
        for data in file_data:
            result_data = result_file.read(data["size"])

            with open(data["name"],"wb") as new_file:
                new_file.write(result_data)
