import turtle
import random

pst = {}
x, y = 0, 0
z = turtle.Turtle()
z.hideturtle()
turtle.tracer(6, 8)
color = ['red', 'blue', 'yellow', 'orange', 'black', 'gold', 'green', 'pink', 'violet']

size = [0.001, 0.002, 0.003]


def ZVZ(size, color, rotation, x, y):
    z.speed(10)
    z.hideturtle()
    z.pencolor(color)
    z.fillcolor(color)
    z.up()
    z.setheading(rotation)
    z.goto(x, y)
    z.down()
    z.begin_fill()
    for i in range(5):
        z.fd(10 * size)
        z.left(144)
    z.end_fill()


for i in range(100):

    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)
    while (x in pst or y in pst):
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
    pst.setdefault(x, y)
    ZVZ(random.randrange(1, 5), random.choice(color), random.randrange(1, 361), x, y)