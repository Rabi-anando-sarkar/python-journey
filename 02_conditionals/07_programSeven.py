# take input 

order_size = str(input("Enter Your Order Size : "))
extra_shot = str(input("Extra Shots YES or NO : "))

# conditionals

if extra_shot == "YES":
    print(f"{order_size} coffee with an extra shot")
else:
    print(f"{order_size} coffee")