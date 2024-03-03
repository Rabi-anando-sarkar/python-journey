# Enter distance

distance = float(input("Enter Distance : "))

# Conditions to check mode of transport

if distance < 0 or distance > 100:
    print("Please Enter a Valid Distance")
    exit()

if distance > 15:
    print("Looks like we need a Car")
elif distance > 3:
    print("Oh we can Take our Bike")
else:
    print("We should Walk.")