def groundShip (weight):
    if weight <= 2.00:
        return (1.50*weight)+20.00
    elif weight > 2 and weight <= 6:
        return (3.00*weight)+20.00
    elif weight > 6 and weight <= 10:
        return (4*weight) + 20.00
    else:
        return (4.75*weight) + 20.00

def droneShip (weight):
    if weight <= 2.00:
        return (4.50*weight)
    elif weight > 2 and weight <= 6:
        return (9.00*weight)
    elif weight > 6 and weight <= 10:
        return (12.00*weight)
    else:
        return (14.25*weight)

def total():
    n = float(input("What is the weight? "))

    ground = groundShip(n)
    if ground > 125:
        ground = 125
    drone = droneShip(n)
    ground = round(ground, 2)
    drone = round(drone, 2)
    if ground > drone:
        print("Drone shipping is cheaper")
        print("It will cost $" + str(drone))
    elif ground == drone:
        print("They are equal")
        print("It will cost $" + str(drone))
    if ground < drone and ground == 125:
        print("Premium shipping is the cheapest, it costs $125")
    else:
        print("Ground shipping is cheaper")
        print("It will cost $" + str(ground))

total()