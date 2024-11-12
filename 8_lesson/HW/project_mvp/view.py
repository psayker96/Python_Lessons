from model import *
from admin_pres import admin_menu
from reader_pres import reader_menu

while True:
    choice = input("""1 - Ви адмін
2 - Ви читач
q - вихід
Оберіть опцію:""")
    if choice == "1":
        admin_menu()
    if choice == "2":
        reader_menu()
    if choice == "q":
        break
