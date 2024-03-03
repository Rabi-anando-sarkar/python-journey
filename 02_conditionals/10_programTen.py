# Enter your pet 

pet = str(input("Is your Pet a Cat or a Dog : "))
age = int(input("Enter Your Pet's age : "))

# food distribution

if(pet == "Cat"):
    if(age > 5):
        print("Senior Cat Food is Recommended For Your Cat")
    else:
        print("Junior Cat Food is Recommended For Your Cat")
elif(pet == "Dog"):
    if(age > 2):
        print("Senior Dog Food is Recommended For Your Dog")
    else:
        print("Junior Dog Food is Recommended For Your Dog")
else:
    print("Please Enter a Valid Pet.")