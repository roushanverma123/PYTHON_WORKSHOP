import turtle

myturtle = turtle.Turtle()
myturtle.speed(0)


def sq():
    myturtle.forward(100)
    myturtle.right(90)


for i in range(51):

    for i in range(4):
        sq()
    myturtle.right(7)