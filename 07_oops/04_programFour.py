# Encapsulation

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectrcCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def full_detail(self):
        return f"{super().full_name()} {self.battery_size}"
    
    
my_tesla = ElectrcCar("Tesla","Model S", "85kWH")
my_tesla_new = Car("Tesla","Model X")


print(my_tesla.model)
print(my_tesla_new.full_name())
# print(my_tesla.__brand)