import random
from turtle import Turtle

timy = Turtle()

timy.penup()
timy.goto(-290, 350)
timy.pendown()
colors = ["blue", "lime", "red", "orange red", "magenta", "deep pink", "dark violet", "cyan"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        timy.forward(100)
        timy.right(angle)
    timy.color(random.choice(colors))
