class Car:
    def __init_(self,
                wheels_type="1",
                stop_system_type="1"):
        if wheels_type == "1":
            self.wheel_field1 = "1"
            self.wheel_field2 = "2"
            self.wheel_field3 = "3"
        else:
            self.wheel_field1 = "3"
            self.wheel_field2 = "2"
            self.wheel_field3 = "1"
            
        if stop_system_type == "1":
            self.system_type_field1 = "1"
            self.system_type_field2 = "2"
            self.system_type_field3 = "3"            
        else:
            self.system_type_field1 = "3"
            self.system_type_field2 = "2"
            self.system_type_field3 = "1"  
