# taking age as input in integer form

age = int(input("Enter your age : "))

# check using conditions

if (age < 13):
    print("Child")
elif (age < 20):
    print("Teenager")
elif (age < 60):
    print("Adult")
else:
    print("Senior")