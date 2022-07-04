from turtle import Turtle
import random
timy = Turtle()

timy.penup()
timy.goto(-350, -350)
timy.pendown()
colors = ["blue", "lime", "red", "orange red", "magenta", "deep pink", "dark violet", "cyan"]


def draw_squares(square_side):
    for i in range(4):
        timy.fd(square_side)
        timy.left(90)
        square_side -= 5
    timy.color(random.choice(colors))
