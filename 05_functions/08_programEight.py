def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    
print_kwargs(job = "Web developer",name = "Rabi",salary=100000)