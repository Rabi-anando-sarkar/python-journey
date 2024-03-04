even_number = int(input("Enter Your Number : "))

sum = 0

for i in range(0,even_number+1):
    if(i % 2 == 0):
        sum += i
        
print(f"Sum of Even Number is : {sum}")