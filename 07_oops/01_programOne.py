class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    
my_car = Car("Redbull", "RB20")

print(my_car.brand)
print(my_car.model)

my_new_car = Car("Mercedes","M15 E")
print(my_new_car.model)