# Polymorphism

class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " !"
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectrcCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def full_detail(self):
        return f"{super().full_name()} {self.battery_size}"
    
    def fuel_type(self):
        return "Electric Charge"
  
# my_tesla = ElectrcCar("Tesla","Model S","85KWH")    
# print(my_tesla.fuel_type())

Car("Tata","Safari")
Car("Tata","Safari Two")
Car("Tata","Safari Three")
Car("Tata","Safari Four")
# print(safari.fuel_type())
print(Car.total_car)