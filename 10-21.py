num1 = int(input("Number 1? "))
num2 = int(input("Number 2?"))

def mult():
    z = (num1*num2) + 100

    if num1 == 5 or num2 == 5:
        return "Cannot compute " + str(num1) + " times " + str(num2)
    else:
        return z - 50

print(mult())