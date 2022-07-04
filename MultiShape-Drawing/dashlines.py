from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()

screen.setup(width=1000, height=1000)

screen.title("Multi Shapes Drawing Game")
timy.color("red")
timy.penup()
timy.goto(-500, 0)


def dash_horizontal():
    timy.penup()
    timy.goto(-500, 0)

    for _ in range(50):
        timy.fd(10)
        timy.penup()
        timy.fd(10)
        timy.pendown()


def dash_vertical():
    timy.penup()
    timy.goto(0, -500)
    timy.left(90)

    for _ in range(50):
        timy.fd(10)
        timy.penup()
        timy.fd(10)
        timy.pendown()



