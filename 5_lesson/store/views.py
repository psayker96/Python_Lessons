from admin_presenter import admin_menu
from client_presenter import client_menu
from lib import hr
from auth_presenter import auth_menu
#from factory import *

while True:
    choice = input("""1 - admin
2 - client
q - quit
Enter option:""")
    if choice == "1":
        hr()
        admin_menu()
    if choice == "2":
        hr()
        client_menu()
    if choice == "q":
        break
    hr()
