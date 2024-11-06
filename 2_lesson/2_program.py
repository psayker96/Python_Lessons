'''
data2 = [1,2,1,2,1,2,1,2,1,2,1,2,
         [1,3,2,
          [1,4,5,
           [1,2,3,4,
            [1,2,155]]]]]
print(data2[12][3][3][4][2])
'''

'''
data2 = {"1":"1",
         "2":"2",
         "3":"3",
         "4":{"1":"1",
              "2":"2",
              "3":{"1":"5",
                   "7":155}}}
print(data2["4"]["3"]["7"])
'''

notes = []
while True:
    choice = input("""1 додати замітку
2 читати всі замітки
3 читати замітку повністю
4 оновити замітку
5 видалити заміткуq вихід із системи:""")
    if choice == "1":
        notes.append({"title":input("Введіть заголовок замітки:"),
                      "description":input("Введіть опис замітки:"),
                      "text":input("Введіть текст замітки:")})
    if choice == "2":
        print("-"*25)
        for note in dict(enumerate(notes.1)).items():
            print(f"{number}) {note['title']}")
            print("-"*25)

    if choice == "3":
        print(*notes)
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
        
        
