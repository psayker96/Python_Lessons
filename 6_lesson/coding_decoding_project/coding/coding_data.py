def info_about_file(filename):
    with open(filename,"rb") as file:
        data = {"name":filename,
                "size":len(file.read())}
        return data

def get_all_data():
    data = []
    while True:
        choice = input("Ім'я файлу або q для завершення:")
        if filename == "q":
            break
        data.append(info_about_file(filename))
    return data
filedata = None        
while True:
    choice = input("1 - code q - quit")
    if choice == "1":
        filedata = get_all_data()
        with open("files_data.txt","w") as file:
            file.write(dumps(filedata))
        result_file = input("Filename where data saves:")
        with open(result_file,"wb") as result_file:    
            for data in filedata:
                with open(data["name"],"rb") as file:
                    result_file.write(file.read())
            
    if choice == "q":
        break