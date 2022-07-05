from dashlines import *
from multisides import draw_shape
from triangles import draw_triangles
from squares import draw_squares
from hexagon import draw_hexagon

"""timy = Turtle()
screen = Screen()"""

dash_horizontal()
dash_vertical()
for side in range(3, 11):
    draw_shape(side)

triangle_side = 300
for i in range(10):
    draw_triangles(triangle_side)
    triangle_side -= 30

square_side = 200
for i in range(10):
    draw_squares(square_side)
    square_side -= 20

side = 120
for i in range(10):
    draw_hexagon(side)
    side -= 12

screen.exitonclick()
