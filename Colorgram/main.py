import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(197, 165, 118), (141, 80, 57), (221, 201, 136), (60, 94, 120), (164, 152, 54), (136, 162, 180),
              (130, 34, 23), (53, 118, 86), (73, 38, 30), (193, 94, 78), (145, 177, 149), (21, 91, 70), (163, 145, 158),
              (34, 60, 76), (114, 72, 77), (227, 176, 165), (59, 41, 44), (181, 204, 175), (137, 26, 29), (16, 71, 59),
              (90, 146, 126), (27, 84, 86), (39, 65, 91), (221, 175, 177), (104, 128, 155), (181, 191, 207)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
