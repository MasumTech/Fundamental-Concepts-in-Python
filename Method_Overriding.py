class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class MotorCycle(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        print("Creating a MotorCycle")
        super().__init__(name, manufacturer, color)
        self.year = 2020
        self.wheels = 2


if __name__ == "__main__":
    m = MotorCycle("ToyotaMoto", "Toyota Japan", "Red", "2020")
    print("Name:", m.name, " Manufacturer:", m.manufacturer, " Color:", m.color, " Year:", m.year, " Wheels:", m.wheels)


''''
class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class Car(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        print("Creating a car")
        super().__init__(name, manufacturer, color)
        self.year = 2020
        self.wheels = 4


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford","Red", "2020")
    print(c.name, c.year, c.wheels)



'''''''''''''
class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self, direction):
        print("Turning", self.name, "to", direction)


class Car(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year

    def change_gear(self, gear_name):
        """Method of chaning gear"""
        print(self.name, "is changing gear to", gear_name)

    def turn(self, direction):
        print(self.name, "is turning", direction)


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford","Red", "2020")
    v = Vehicle("Softail Delux", "Harley-Devidson", "Blue")
    c.turn("right")
    v.turn("right")
    
    '''''''''''
