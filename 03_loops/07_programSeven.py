while True:
    number = int(input("Enter a number Between 1 and 10 : "))
    if 1 <= number <= 10:
        print(f"Thank Your Number is : {number}")
        break
    else:
        print(f"{number} is a an Invalid Number Try Again")