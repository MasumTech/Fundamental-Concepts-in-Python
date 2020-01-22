class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping")


class Car(Vehicle):
    """Car class"""
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4
        print("A new car has been created. Name:", self.name)
        print("It has", self.wheels, "wheels")
        print("The car was built in", self.year)



    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red", "2020")

    c.change_gear("p")

'''''''''''''''''''''
class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping")


class Car(Vehicle):
    """Car class"""

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red")
    c.drive()
    c.brake()
    c.change_gear("p")
    
    
    
''''''''''''''''''''''''
class Vehicle:
     """Base class for all vehicles"""
     def __init__(self, name, manufacturer, color):
         self.name = name
         self.manufacturer = manufacturer
         self.color = color

     def drive(self):
         print("Driving", self.manufacturer, self.name)

     def turn(self, direction):
         print("Turning", self.name, "to", direction)

     def brake(self):
         print(self.name, "is stopping")

class Car(Vehicle):
    """Car class"""
    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustang 5.0 GT Couple", "Ford", "Red")
    c =  Car("Mustang 5.0 GT Coupe", "Ford", "Red")


    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn("left")
    v2.turn("right")

    v1.brake()
    v2.brake()
    v3.brake()

    c.change_gear("forward")
    '''''''''''''''''''''




