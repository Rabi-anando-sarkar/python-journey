input_string = 'aabbccddeffgghh'

for char in input_string:
    if(input_string.count(char) == 1):
        print(f"Char {char} is repeated only one time.")
        break