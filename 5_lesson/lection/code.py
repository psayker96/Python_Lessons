data = []
data2 = []
data3 = []

def data_exist(data):
    def decorator(action):
        def wrapper():
            if data:
                return action()
            else:
                print("Виконати неможливо")
        return wrapper
    return decorator

@data_exists(data)
def action1():
    print("1")

@data_exists(data2)
def action2():
    print("2")
    
@data_exists(data3)
def action3():
    print("3")
