def decorator(action):
    def wrapper():
        print("START!")
        action()
        print("FINISH!")
    return wrapper

@decorator
def print_text():
    text = input("Введіть будь який текст:")

print_text()
