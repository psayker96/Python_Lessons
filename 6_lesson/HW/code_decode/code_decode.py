from coding.coding_data import coding_menu
from decoding.decoding_data import decoding_menu

while True:
    choice = input("""1 - Code
2 - Decode
q - Quit
Enter option:""")
    if choice == "1":
        coding_menu()
    if choice == "2":
        decoding_menu()
    if choice == "q":
        break
    
