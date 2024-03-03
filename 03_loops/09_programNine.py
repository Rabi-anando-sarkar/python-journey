# Enter your year

year = int(input("Enter your Year : "))

# check if its a leap year or not

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Yes,{year} is Leap year")
else:
    print(f"{year} is not a Leap year")
    
