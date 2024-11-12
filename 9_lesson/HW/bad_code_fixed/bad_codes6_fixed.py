class Car:
    def __init_(self,
                wheels_type,
                stop_system_type):
        self.wheels_type = wheels_type
        self.stop_system_type = stop_system_type

    def wheels_types_params(self):
        self.wheels_type = input("Введите любую цифру:")
        if self.wheels_type == "1":
            self.wheel_field1 = "1"
            self.wheel_field2 = "2"
            self.wheel_field3 = "3"
            print(self.wheels_type,
                  self.wheel_field1,
                  self.wheel_field2,
                  self.wheel_field3)
        else:
            self.wheel_field1 = "3"
            self.wheel_field2 = "2"
            self.wheel_field3 = "1"
            print(self.wheels_type,
                  self.wheel_field1,
                  self.wheel_field2,
                  self.wheel_field3)

    def stop_system_type(self):
        self.stop_system_type = input("Введите любую цифру:")
        if self.stop_system_type == "1":
            self.system_type_field1 = "1"
            self.system_type_field2 = "2"
            self.system_type_field3 = "3"
            print(self.stop_system_type,
                  system_type_field1,
                  system_type_field2,
                  system_type_field3)
        else:
            self.system_type_field1 = "3"
            self.system_type_field2 = "2"
            self.system_type_field3 = "1"
            print(self.stop_system_type,
                  system_type_field1,
                  system_type_field2,
                  system_type_field3)

car = Car()
car.wheels_types_params()
car.stop_system_type()
