num = 3

for i in range(1,11):
    if(i % 5 == 0):
        continue
    print(f"{num} * {i} = {i * num}")