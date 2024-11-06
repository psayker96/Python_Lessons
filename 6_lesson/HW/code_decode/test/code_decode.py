from coding_data import *
from decoding_data import *

while True:
    choice = input("""1 - Code
2 - Decode
q - Quit
Enter option:""")
    if choice == "1":
        coding_menu()
    elif choice == "2":
        decoding()
    elif choice == "q":
        break
    else:
        print("Wrong option!")
    
    
