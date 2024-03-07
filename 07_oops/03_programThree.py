# Inheritance

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectrcCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def full_detail(self):
        return f"{super().full_name()} {self.battery_size}"
     
    
my_car_model = Car("Redbull","RB20")

'''
print(my_car_model.brand)
print(my_car_model.model)
print(my_car_model.full_name())
'''

my_tesla = ElectrcCar("Tesla","Model S", "85kWH")

print(my_tesla.full_detail())