class Item:
    def __init__(self,
                 name,
                 description,
                 price):
        self.__name = name
        self.__description = description
        self.__price = price
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_description(self):
        return self.__description
    def set_description(self,description):
        self.__description = description
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price