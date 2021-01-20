print("Calculator starting up!")


while 1==1:
    option = input("Enter C for Circle or T for Triangle: ")
    if option == "C":
        radius = float(input("Input the radius of the circle: "))
        radius = radius**2
        area = radius * 3.14159
        print("The area of the circle is " + str(area))
        break
    elif option == "T":
        base = float(input("Input the base of the triangle: "))
        height = float(input("Input the height of the triangle: "))
        area = (base * height)/2
        print("The area of the triangle is " + str(area))
        break
    else:
        print("Inputted an invalid shape, try again!")

print("Exiting the calculator")