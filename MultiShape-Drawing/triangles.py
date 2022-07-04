from turtle import Turtle
import random
timy = Turtle()

timy.penup()
timy.goto(100, 100)
timy.pendown()
colors = ["blue", "lime", "red", "orange red", "magenta", "deep pink", "dark violet", "cyan"]


def draw_triangles(triangle_side):
    for i in range(3):
        timy.fd(triangle_side)
        timy.left(120)
        triangle_side -= 5
    timy.color(random.choice(colors))
