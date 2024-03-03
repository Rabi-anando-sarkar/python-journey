# Taking marks as input

marks = int(input("Enter Your Marks : "))


# Way One

'''

if marks > 100 or marks < 0:
    print("Please Enter Valid Marks.")
elif marks > 90:
    print("Welldone, Your Grade is : A")
elif marks >= 80:
    print("Almost There, Your Grade is : B")
elif marks >= 70:
    print("Can Do Better, Your Grade is : C")
elif marks >= 60:
    print("Practice More, Your Grade is : D")
else:
    print("Better Luck Next Time, Your Grade is : F")

'''

# Way Two

if(marks > 100 or marks < 0):
    print("Please Enter Valid Marks.")
    exit()
    
if(marks >= 90):
    grade = "A"
elif(marks >= 80):
    grade = "B"
elif(marks >= 70):
    grade = "C"
elif(marks >= 60):
    grade = "D"
else:
    grade = "F"
    
print("Your Grade :",grade)