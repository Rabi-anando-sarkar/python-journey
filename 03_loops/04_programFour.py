# input name of the fruit and color 

fruit = str(input("Enter the name of the fruit : "))
color = str(input("Enter the color of the fruit : "))

# check if the fruit is ripe, overripe or unripe

if(color == "Green"):
    print(f"Your {fruit} is Unripe")
elif(color == "Yellow"):
    print(f"Your {fruit} is Ripe")
elif(color == "Brown"):
    print(f"Your {fruit} is Overripe")
else:
    print("Please Enter a Valid Food Color")

