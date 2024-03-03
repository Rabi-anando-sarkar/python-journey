# Taking age and Day as input

age = int(input("Enter your age : "))
day = str(input("Enter the day : "))

# check condition 

# longer syntax

price = 0

if age >= 18:
    price = 12
else:
    price = 8
    
if day == "Wednesday":
    price -= 2
    print("Your Ticket Price Will Be $",price)
else:
    print("Your Ticket Price Will Be $",price)


# shorter syntax

'''
price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2  
    # price = price - 2

print("Your Ticket Price Will Be $",price)
'''