string = input("Input a string: ")

stringR = ""


for x in range(0, len(string)):
    index = len(string) - x
    stringR = stringR + string[index-1]

print(stringR)