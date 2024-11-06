def view_items(items):
    for number,item in enumerate(items,1):
        print(f"{number}) {item['name']}")

def get_item_number(items):
    view_items(items)
    item_number = input("Введіть номер товару:")
    if (item_number.isdigit() and
        0 < int(item_number) <= len(items)):
        return int(item_number) - 1

def get_item(items):
    item_number = get_item_number(items)
    if item_number is not None:
        item = items[item_number]
        return item

def hr():
    print("="*45)
