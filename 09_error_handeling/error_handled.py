# version 1

file = open('youtube.txt', 'w')

try:
    file.write('Start a pyhton project')
finally:
    file.close()

# version 2 
# ye jab file ke saath interaction karoge
# isme with hee use krna hota hai 
    
with open('youtube.txt', 'w') as file:
    file.write("starting python")