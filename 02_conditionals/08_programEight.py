# Enter Your password

password = input("Enter your password : ")

if(len(password) == 0):
    print("Please Enter a Password")
    exit()

if len(password) >= 11:
    print("Strong Password")
elif len(password) >= 6:
    print("Medium Password")
else:
    print("WeaK Password")