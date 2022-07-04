from turtle import Turtle
import random
timy = Turtle()

timy.penup()
timy.goto(200, -150)
timy.pendown()
colors = ["blue", "lime", "red", "orange red", "magenta", "deep pink", "dark violet", "cyan"]


def draw_hexagon(hexagon_side):
    for i in range(6):
        timy.fd(hexagon_side)
        timy.left(300)
        hexagon_side -= 2
    timy.color(random.choice(colors))
