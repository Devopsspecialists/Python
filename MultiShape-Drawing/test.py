import turtle


def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for c in ['red', 'purple', 'hotpink', 'blue']:
        t.color(c)
        t.forward(sz)
        t.left(90)

# Set up the window and its attributes
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Spiralling Squares")

# create tess and set some attributes
tess = turtle.Turtle()
tess.pensize(3)

size = 20                        # size of the smallest square
for i in range(25):
    draw_multicolor_square(tess, size)
    size = size + 10             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn

wn.exitonclick()