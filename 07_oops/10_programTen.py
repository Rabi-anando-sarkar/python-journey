# solution for 7th program rest in order

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
    
    @staticmethod
    def general_decription():
        return "Cars Are means of Transport"
    
class ElectrcCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def full_detail(self):
        return f"{super().full_name()} {self.battery_size}"
    
    def fuel_type(self):
        return "Electric Charge"
    

my_car = Car("Tata","Safari")

# print(my_car.general_decription())
print(Car.general_decription())