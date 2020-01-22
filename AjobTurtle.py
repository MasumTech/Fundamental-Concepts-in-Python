import turtle


class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class of new type of turtle"""
    def forward(self, pixel):
        super().backward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        print("I won't turn right, because I am ajob!")


if __name__ == "__main__":
    montu = AjobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.left(-145)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)

    jhontu = turtle.Turtle()
    jhontu.shape("turtle")
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(45)
    jhontu.backward(100)
    jhontu.right(90)
    jhontu.forward(10)

    turtle.done()




'''''''''
import turtle

class Ajobturtle(turtle.Turtle):
    """Ajobturtle is a class of new turtle"""
    pass


if __name__=="__main__":
    montu = Ajobturtle()
    print(type(montu))
    montu.left(30)
    montu.forward(200)


    turtle.done( )
    
'''''
