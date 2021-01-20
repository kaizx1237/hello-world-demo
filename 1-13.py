class Car:
    def __init__(self, type, color, year):
        self.type = type
        self.color = color
        self.year = year

    def increaseYear(self):
        self.year += 1

    def old(self):
        if (2020-self.year) > 20:
            print("Your car is old")
        else:
            print("Your car is not old")

    def __str__(self):
        return "Your car is a " + self.color + " " + self.type + " from " + str(self.year)


c1 = Car("Toyota", "red", 2008)

c1.old()
print(c1)
c1.increaseYear()
c1.old()
print(c1)