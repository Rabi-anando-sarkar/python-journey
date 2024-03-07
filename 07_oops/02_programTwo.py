class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
        
        
        
my_car_model = Car("Redbull","RB20")

print(my_car_model.brand)
print(my_car_model.model)

print(my_car_model.full_name())

        